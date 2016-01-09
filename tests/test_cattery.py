import pytest

from catinabox import cattery


@pytest.fixture
def my_awesome_fixture():
    return cattery.Cattery()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(my_awesome_fixture):
    my_awesome_fixture.add_cats(["Fluffy", "Snookums"])
    assert my_awesome_fixture.cats == ["Fluffy", "Snookums"]
    assert my_awesome_fixture.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(my_awesome_fixture):
    my_awesome_fixture.add_cats(["Fluffy", "Junior"])
    my_awesome_fixture.remove_cat("Fluffy")
    assert my_awesome_fixture.cats == ["Junior"]
    assert my_awesome_fixture.num_cats == 1


def test__remove_cat__no_cats__fails(my_awesome_fixture):
    with pytest.raises(cattery.CatNotFound):
        my_awesome_fixture.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(my_awesome_fixture):
    my_awesome_fixture.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        my_awesome_fixture.remove_cat("Snookums")
