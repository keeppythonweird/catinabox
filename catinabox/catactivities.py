import time


SECONDS_IN_MINUTE = 60
LENGTH_OF_SATISFYING_NAP = SECONDS_IN_MINUTE * 5


class NapWillNotBeSatisfying(Exception):
    """The nap is not long enough to be satisfying."""
    def __init__(self, nap_seconds):
        super(NapWillNotBeSatisfying, self).__init__(
            "Nap for {!r} seconds is not long enough; must be at least {!r} "
            "seconds to be satisfying".format(
                nap_seconds, LENGTH_OF_SATISFYING_NAP)
        )
        self.nap_seconds = nap_seconds


def cat_nap(nap_seconds):
    if nap_seconds < LENGTH_OF_SATISFYING_NAP:
        raise NapWillNotBeSatisfying(nap_seconds)
    time.sleep(nap_seconds)
