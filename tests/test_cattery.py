import pytest

from catinabox import cattery


###########################################################################
# add_cats
###########################################################################
@pytest.fixture
def add_cats():
    return


def test__add_cats__succeeds(add_cats):
    c = cattery.Cattery()
    c.add_cats(["Fluffy", "Snookums"])
    assert c.cats == ["Fluffy", "Snookums"]
    assert c.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

@pytest.fixture
def remove_cat():
    return


def test__remove_cat__succeeds(remove_cat):
    c = cattery.Cattery()
    c.add_cats(["Fluffy", "Junior"])
    c.remove_cat("Fluffy")
    assert c.cats == ["Junior"]
    assert c.num_cats == 1


def test__remove_cat__no_cats__fails(remove_cat):
    c = cattery.Cattery()
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(remove_cat):
    c = cattery.Cattery()
    c.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Snookums")
