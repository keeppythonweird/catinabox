# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

import _ast
import py
import sys
import tokenize

import pytest
import mccabe


HISTKEY = "mccabe/mtimes"


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption(
        '--mccabe', action='store_true',
        help="run mccabe on .py files")
    parser.addini(
        "mccabe-complexity", type="linelist",
        help="each line specifies a glob pattern and whitespace "
             "separated the maximal complexity for the given pattern (or 0 to "
             "deactivate checking). example: *.py 10")


def pytest_sessionstart(session):
    config = session.config
    if config.option.mccabe:
        config._mccabe_complexities = Complexities(
            config.getini("mccabe-complexity"))
        config._mccabe_mtimes = config.cache.get(HISTKEY, {})


def pytest_collect_file(path, parent):
    config = parent.config
    if config.option.mccabe and path.ext == '.py':
        complexity = config._mccabe_complexities(path)
        if complexity != 0:
            return McCabeItem(path, parent, complexity)


def pytest_sessionfinish(session):
    config = session.config
    if hasattr(config, "_mccabe_mtimes"):
        config.cache.set(HISTKEY, config._mccabe_mtimes)


class McCabeError(Exception):
    """ indicates an error during McCabe checks. """


class McCabeItem(pytest.Item, pytest.File):

    def __init__(self, path, parent, complexity):
        super(McCabeItem, self).__init__(path, parent)
        self._mtime = None
        if hasattr(self, 'add_marker'):
            self.add_marker("mccabe")
        else:
            self.keywords["mccabe"] = True
        self.complexity = complexity

    def setup(self):
        mtimes = self.config._mccabe_mtimes
        self._mtime = self.fspath.mtime()
        old = mtimes.get(str(self.fspath), 0)
        if old == (self._mtime, self.complexity):
            pytest.skip("file(s) previously passed McCabe checks")

    def runtest(self):
        found_errors, out = check_file(self.fspath, self.complexity)
        if found_errors:
            raise McCabeError("\n".join(out))
        # update mtime only if test passed
        # otherwise failures would not be re-run next time
        self.config._mccabe_mtimes[str(self.fspath)] = (self._mtime,
                                                        self.complexity)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(McCabeError):
            return excinfo.value.args[0]
        return super(McCabeItem, self).repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, "mccabe-check"


class Complexities:

    DEFAULT_COMPLEXITY = 7

    def __init__(self, lines):
        self.complexities = []
        for line in lines:
            i = line.find("#")
            if i != -1:
                line = line[:i]
            try:
                glob, val = line.split(None, 1)
            except ValueError:
                glob, val = None, line
            self.complexities.append((glob, int(val)))

    def __call__(self, path):
        for (glob, complexity) in self.complexities:
            if not glob or path.fnmatch(glob):
                return complexity
        return self.DEFAULT_COMPLEXITY


def check_file(path, complexity):
    if not hasattr(tokenize, 'open'):
        code = path.read()
    else:
        with tokenize.open(path.strpath) as f:
            code = f.read()

    filename = py.builtin._totext(path)
    try:
        tree = compile(code, filename, "exec", _ast.PyCF_ONLY_AST)
    except SyntaxError:
        return 1, get_syntax_error_msg(filename)

    errors = []
    checker = mccabe.McCabeChecker(tree, filename)
    checker.max_complexity = complexity
    lines = code.split('\n')
    for lineno, _offset, text, _checker in checker.run():
        if is_ignored_line(lines[lineno - 1].strip()):
            continue
        errors.append('%s:%s: %s' % (filename, lineno, text))
    return len(errors), errors


def get_syntax_error_msg(filename):
    errors = []
    value = sys.exc_info()[1]
    (lineno, offset, text) = value.lineno, value.offset, value.text
    if text is None:
        errors.append("%s: problem decoding source" % filename)
    else:
        line = text.splitlines()[-1]

        if offset is not None:
            offset = offset - (len(text) - len(line))

        msg = '%s:%d: %s' % (filename, lineno, value.args[0])
        msg = "%s\n%s" % (msg, line)

        if offset is not None:
            msg = "%s\n%s" % (msg, "%s^" % (" " * offset))
        errors.append(msg)
    return errors


def is_ignored_line(line):
    return line.endswith('# noqa') or line.endswith('# pragma: no mccabe')
