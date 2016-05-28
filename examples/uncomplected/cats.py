import random


class Cat(object):
    def __init__(self, name, last_ate=None):
        self.name = name
        self.last_ate = last_ate

    def feed(self, food):
        self.last_ate = food

    def __eq__(self, other):
        return (
            other.name == self.name and
            other.last_ate == self.last_ate
        )


def get_cat_name():
    cat_names = ["Fluffles", "Enzo", "Lisa", "Berto", "Jillian", "Amy",
                 "Bella", "Moe", "Tibby"]
    return random.choice(cat_names)


def get_food():
    return random.choice(
        ["vinegar", "vegemite", "vanilla", "acorn squash",
         "Canadian bacon", "alligator", "cayenne pepper", "adobo",
         "almond butter",
         "garlic"])


def setup_cats(num_cats):
    cats = [Cat(name=get_cat_name()) for _ in range(num_cats)]

    for cat in cats:
        cat.feed(get_food())

    return cats
