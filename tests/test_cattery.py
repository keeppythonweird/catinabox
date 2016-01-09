import pytest

from catinabox import cattery, mccattery


@pytest.fixture(params=[
    cattery.Cattery,
    mccattery.McCattery,
])
def my_awesome_fixture(request):
    return request.param()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(my_awesome_fixture):
    my_awesome_fixture.add_cats(["Fluffy", "Snookums"])
    assert my_awesome_fixture.cats == ["Fluffy", "Snookums"]
    assert my_awesome_fixture.num_cats == 2
    if isinstance(my_awesome_fixture, mccattery.McCattery):
        assert len(my_awesome_fixture.history) == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(my_awesome_fixture):
    my_awesome_fixture.add_cats(["Fluffy", "Junior"])
    my_awesome_fixture.remove_cat("Fluffy")
    assert my_awesome_fixture.cats == ["Junior"]
    assert my_awesome_fixture.num_cats == 1
    if isinstance(my_awesome_fixture, mccattery.McCattery):
        assert len(my_awesome_fixture.history) == 3


def test__remove_cat__no_cats__fails(my_awesome_fixture):
    with pytest.raises(cattery.CatNotFound):
        my_awesome_fixture.remove_cat("Fluffles")
    if isinstance(my_awesome_fixture, mccattery.McCattery):
        assert len(my_awesome_fixture.history) == 0


def test__remove_cat__cat_not_in_cattery__fails(my_awesome_fixture):
    my_awesome_fixture.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        my_awesome_fixture.remove_cat("Snookums")
