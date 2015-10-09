class CatNotFound(Exception):
    """The requested cat was not found in the cattery."""
    def __init__(self, name):
        super(CatNotFound, self).__init__(
            "Cat with name {!r} not found in cattery.".format(name)
        )
        self.name = name


class Cattery(object):
    """ A collection of cats."""
    def __init__(self):
        self._cats = []

    @property
    def num_cats(self):
        return len(self._cats)

    @property
    def cats(self):
        return self._cats

    def add_cats(self, names):
        """Add cats with the specified names to the cattery.

        :param names: A list of the names of cats to add to the cattery.
        """
        self._cats.extend(names)

    def remove_cat(self, name):
        """Remove the specified cat from the cattery.

        The first cat found in the cattery with the specified name will be
        removed.

        :param name: The name of the cat to remove.
        """
        cats = [cat for cat in self._cats if cat == name]
        if len(cats) == 0:
            raise CatNotFound(name)
        self._cats.remove(cats[0])

