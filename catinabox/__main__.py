from __future__ import print_function
import errno

from nameko.runners import ServiceRunner
import eventlet

from .web import CatInABoxService


def main():
    runner = ServiceRunner(config={})
    runner.add_service(CatInABoxService)
    runner.start()

    print('http://localhost:8000')

    runnlet = eventlet.spawn(runner.wait)
    while True:
        try:
            runnlet.wait()
        except OSError as exc:
            if exc.errno == errno.EINTR:
                # this is the OSError(4) caused by the signalhandler.
                # ignore and go back to waiting on the runner
                continue
            raise
        except KeyboardInterrupt:
            print  # looks nicer with the ^C e.g. bash prints in the terminal
            try:
                runner.stop()
            except KeyboardInterrupt:
                print  # as above
                runner.kill()
        else:
            # runner.wait completed
            break


if __name__ == '__main__':
    main()
