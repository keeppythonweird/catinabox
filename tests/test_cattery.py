import pytest

from catinabox import cattery


class TestCattery(object):

    ###########################################################################
    # add_cats
    ###########################################################################

    def test__add_cats__succeeds(self):
        c = cattery.Cattery()
        assert False

    ###########################################################################
    # remove_cat
    ###########################################################################

    def test__remove_cat__succeeds(self):
        c = cattery.Cattery()
        assert False

    def test__remove_cat__no_cats__fails(self):
        c = cattery.Cattery()
        with pytest.raises(cattery.CatNotFound):
            c.remove_cat("Snookums")

    def test__remove_cat__cat_not_in_cattery__fails(self):
        c = cattery.Cattery()
        c.add_cats(["Fluffy"])
        with pytest.raises(cattery.CatNotFound):
            c.remove_cat("Snookums")

    ###########################################################################
    # feed_cats
    ###########################################################################

    def test__feed_cats__succeeds(self):
        c = cattery.Cattery()
        c.add_cats(["Fluffy", "Snookums"])
        c.feed_cats(["burger", "salmon"])

        assert c.cats == [{"name": "Fluffy", "food_eaten": ["burger"]},
                          {"name": "Snookums", "food_eaten": ["salmon"]}]

    def test__feed_cats__not_enough_food__fails(self):
        c = cattery.Cattery()
        c.add_cats(["Fluffy", "Snookums"])
        with pytest.raises(cattery.NotEnoughFood):
            c.feed_cats(["burger"])

    def test__feed_cats__no_cats__wastes_food(self):
        c = cattery.Cattery()
        c.feed_cats(["burger", "salmon", "pizza"])
        assert c.cats == []

    def test__feed_cats__too_much_food__wastes_food(self):
        c = cattery.Cattery()
        c.add_cats(["Fluffy", "Snookums"])
        c.feed_cats(["burger", "salmon", "pizza"])

        assert c.cats == [{"name": "Fluffy", "food_eaten": ["burger"]},
                          {"name": "Snookums", "food_eaten": ["salmon"]}]
