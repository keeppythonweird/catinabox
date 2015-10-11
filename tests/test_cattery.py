import pytest

from catinabox import cattery


###########################################################################
# add_cats
###########################################################################
@pytest.fixture
def a_cattery():
    return cattery.Cattery()


def test__add_cats__succeeds(a_cattery):
    a_cattery.add_cats(["Fluffy", "Snookums"])
    assert a_cattery.cats == ["Fluffy", "Snookums"]
    assert a_cattery.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(a_cattery):
    a_cattery.add_cats(["Fluffy", "Junior"])
    a_cattery.remove_cat("Fluffy")
    assert a_cattery.cats == ["Junior"]
    assert a_cattery.num_cats == 1


def test__remove_cat__no_cats__fails(a_cattery):
    with pytest.raises(cattery.CatNotFound):
        a_cattery.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(a_cattery):
    a_cattery.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        a_cattery.remove_cat("Snookums")
