import shlex
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


with open('requirements.txt') as fd:
    requirements = [line.rstrip() for line in fd]

with open('test_requirements.txt') as fd:
    test_requirements = [line.rstrip() for line in fd]


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''
        self.default_args = [
            '--cov=catinabox',
            '--cov-report=term-missing',
            'tests',
        ]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.default_args + shlex.split(self.pytest_args))
        sys.exit(errno)


setup(name='catinabox',
      version='0.0.1',
      author='Keep Python Weird',
      author_email='about@keeppythonweird.com',
      install_requires=requirements,
      tests_require=test_requirements,
      cmdclass={'test': PyTest},
      packages=find_packages())
