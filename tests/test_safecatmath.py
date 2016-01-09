import pytest

from catinabox import safecatmath


@pytest.mark.parametrize('age, expected', [
    (7, 35),
    (8.7, 43.5),
    (11.0, 55.0),
])
def test__cat_years_to_hooman_years__middle_age__succeeds(age, expected):
    hooman_age = safecatmath.cat_years_to_hooman_years(age)
    assert hooman_age == expected


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_age = safecatmath.cat_years_to_hooman_years(0.1)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = safecatmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0


def test__cat_years_to_hooman_years__less_0__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(-2)


@pytest.mark.parametrize('age', [
    1000.1,
    680000,
])
def test__cat_years_to_hooman_years__older_than_1000__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)


@pytest.mark.parametrize('age', [
    "35.1",
    "Not valid age!!",
    [2, 7.15],
    {"prog": True},
])
def test__cat_years_to_hooman_years__string__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)
