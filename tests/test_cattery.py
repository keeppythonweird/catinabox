import pytest

from catinabox import cattery


@pytest.fixture()
def cats():
    return cattery.Cattery()

###########################################################################
# add_cats
###########################################################################


def test__add_cats__succeeds(cats):
    cats.add_cats(["Fluffy", "Snookums"])
    assert cats.cats == ["Fluffy", "Snookums"]
    assert cats.num_cats == 2

###########################################################################
# remove_cat
###########################################################################


def test__remove_cat__succeeds(cats):
    cats.add_cats(["Fluffy", "Junior"])
    cats.remove_cat("Fluffy")
    assert cats.cats == ["Junior"]
    assert cats.num_cats == 1


def test__remove_cat__no_cats__fails(cats):
    with pytest.raises(cattery.CatNotFound):
        cats.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cats):
    cats.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        cats.remove_cat("Snookums")
