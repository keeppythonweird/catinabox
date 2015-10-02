import copy


NEW_CAT_TEMPLATE = {"food_eaten": []}


class CatNotFound(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Cat with name {name} not found in cattery.".format(
            name=self.name
        )


class NotEnoughFood(Exception):
    def __init__(self, num_cats, foods_to_feed):
        self.num_cats = num_cats
        self.foods_to_feed = foods_to_feed

    def __str__(self):
        return "Provided food {food} isn't enough for {num_cats} cats".format(
            food=self.foods_to_feed, num_cats=self.num_cats
        )


class Cattery(object):
    """ A collection of cats.

    The collection can be added to and removed from, and the cats can be fed.
    """
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
        for name in names:
            new_cat = copy.deepcopy(NEW_CAT_TEMPLATE)
            new_cat.update({"name": name})
            self._cats.append(new_cat)

    def remove_cat(self, name):
        """Remove the specified cat from the cattery.

        The first cat found in the cattery with the specified name will be
        removed.

        :param name: The name of the cat to remove.
        """
        cats = [cat for cat in self._cats
                if cat["name"] == name]
        if len(cats) == 0:
            raise CatNotFound(name)
        self._cats.remove(cats[0])

    def feed_cats(self, foods_to_feed):
        """Feed the specified foods to the cats in the cattery.

        If all cats cannot be fed, an exception will be raised.
        If too much food is provided, the extra will go to waste.

        :param foods_to_feed: A list with a string for each food item to feed
                              to the cats.
        """
        if len(foods_to_feed) < self.num_cats:
            raise NotEnoughFood(self.num_cats, foods_to_feed)

        for cat, food in zip(self._cats, foods_to_feed):
            cat["food_eaten"].append(food)
