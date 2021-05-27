import pytest

from catinabox import safecatmath


@pytest.mark.parametrize("age, expected", [
    (7, 35),
    (0.1, 0.5),
    (0, 0)
])
def test__cat_years_to_hooman_years(age, expected):
    assert safecatmath.cat_years_to_hooman_years(age) == expected

"""
def test__cat_years_to_hooman_years__middle_age__succeeds():
    hooman_age = safecatmath.cat_years_to_hooman_years(7)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_age = safecatmath.cat_years_to_hooman_years(0.1)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = safecatmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0
"""


@pytest.mark.parametrize("age", [
    -5,
    2100,
    "two",
    float('nan')
])
def test__cat_years_to_hooman_years__invalid_input__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)

"""
def test__cat_years_to_hooman_years__less_0__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(-5)


def test__cat_years_to_hooman_years__older_than_1000__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(2100)


def test__cat_years_to_hooman_years__string__raises():
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years('two')


def test__cat_years_to_hooman_years__nan__raises():
    hooman_age = float('nan')
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(hooman_age)
"""
