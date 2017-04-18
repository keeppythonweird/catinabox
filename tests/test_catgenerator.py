import pytest

from catinabox import catgenerator


# Write tests for the refactored `catinabox.catgenerator`

def test__get_cat_name_success():
    name = catgenerator.get_cat_name()
    assert isinstance(name, str)


def test__get_birthday_success():
    birthday = catgenerator.get_birthday()
    assert isinstance(birthday, str)


def test__get_cat_name_fail():
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.get_cat_name(
                url="http://thisdoesnotexisit12321321312.com")


def test__check_cat_generator():
    x = 0
    catlist = []
    for item in catgenerator.cat_generator():
        if x < 5:
            catlist.append(item)
        else:
            break
        x += 1
    assert len(catlist) == 5
