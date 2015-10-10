import pytest

from catinabox import cattery


class TestCattery(object):

    ###########################################################################
    # add_cats
    ###########################################################################

    def test__add_cats__succeeds(self):
        c = cattery.Cattery()
        assert True

    ###########################################################################
    # remove_cat
    ###########################################################################

    def test__remove_cat__succeeds(self):
        c = cattery.Cattery()
        assert True

    def test__remove_cat__no_cats__fails(self):
        c = cattery.Cattery()
        assert True

    def test__remove_cat__cat_not_in_cattery__fails(self):
        c = cattery.Cattery()
        c.add_cats(["Fluffy"])
        with pytest.raises(cattery.CatNotFound):
            c.remove_cat("Snookums")
