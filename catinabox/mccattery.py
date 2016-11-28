from datetime import datetime
from .cattery import Cattery


class McCattery(Cattery):

    """A more analytics-centered verison of the Cattery."""

    def __init__(self):
        super(McCattery, self).__init__()
        self._history = []

    @property
    def history(self):
        return self._history

    def add_cats(self, names):
        """Add cats with the specified names to the cattery.

        :param names: A list of the names of cats to add to the cattery.

        """
        super(McCattery, self).add_cats(names)
        for name in names:
            self._history.append("Added {!r} to the McCattery on {!r}".format(
                name, str(datetime.now())))

    def remove_cat(self, name):
        """Remove the specified cat from the cattery.

        The first cat found in the cattery with the specified name will be
        removed.

        :param name: The name of the cat to remove.

        """
        super(McCattery, self).remove_cat(name)
        self._history.append("Removed {!r} from the McCattery on {!r}".format(
            name, str(datetime.now())))
