import pytest

from catinabox import cattery


@pytest.fixture
def ctry():
    return cattery.Cattery()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(ctry):
    ctry.add_cats(["Fluffy", "Snookums"])
    assert ctry.cats == ["Fluffy", "Snookums"]
    assert ctry.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(ctry):
    ctry.add_cats(["Fluffy", "Junior"])
    ctry.remove_cat("Fluffy")
    assert ctry.cats == ["Junior"]
    assert ctry.num_cats == 1


def test__remove_cat__no_cats__fails(ctry):
    with pytest.raises(cattery.CatNotFound):
        ctry.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(ctry):
    ctry.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        ctry.remove_cat("Snookums")
