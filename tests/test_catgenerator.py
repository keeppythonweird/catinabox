import pytest
from catinabox import catgenerator


def test__get_random_cat_name__pass():
    catgenerator.get_random_cat_name()


def test__get_random_cat_name__raises_error_if_endpoint_unavaliable(mocker):
    mocker.patch.object(catgenerator, "NAME_GENERATOR_API_ENDPOINT")
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.get_random_cat_name()


def test__make_cat_birthday():
    birthday = catgenerator.make_cat_birthday()
    assert len(birthday) > 5


def test__cat_generator__pass():
    cat = catgenerator.cat_generator()
    next(cat)


def test__cat_generator__unique_cats():
    randomcat = catgenerator.cat_generator()
    cat_1 = next(randomcat)
    cat_2 = next(randomcat)

    assert cat_1["name"] != cat_2["name"]
    assert cat_1["birthday"] != cat_2["birthday"]
