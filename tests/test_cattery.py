import pytest

from catinabox import cattery


@pytest.fixture()
def cattery_obj():
    return cattery.Cattery()


###########################################################################
# add_cats
###########################################################################


def test__add_cats__succeeds(cattery_obj):

    cattery_obj.add_cats(["Fluffy", "Snookums"])
    assert cattery_obj.cats == ["Fluffy", "Snookums"]
    assert cattery_obj.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(cattery_obj):
    cattery_obj.add_cats(["Fluffy", "Junior"])
    cattery_obj.remove_cat("Fluffy")
    assert cattery_obj.cats == ["Junior"]
    assert cattery_obj.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_obj):
    with pytest.raises(cattery.CatNotFound):
        cattery_obj.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cattery_obj):
    cattery_obj.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        cattery_obj.remove_cat("Snookums")
