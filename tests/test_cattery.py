import pytest

from catinabox import cattery


@pytest.fixture
def cat_object():
    cat = cattery.Cattery()
    return cat


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(cat_object):
    cat_object.add_cats(["Fluffy", "Snookums"])
    assert cat_object.cats == ["Fluffy", "Snookums"]
    assert cat_object.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(cat_object):
    cat_object.add_cats(["Fluffy", "Junior"])
    cat_object.remove_cat("Fluffy")
    assert cat_object.cats == ["Junior"]
    assert cat_object.num_cats == 1


def test__remove_cat__no_cats__fails(cat_object):
    with pytest.raises(cattery.CatNotFound):
        cat_object.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cat_object):
    cat_object.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        cat_object.remove_cat("Snookums")
