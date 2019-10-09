import pytest

from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(7) == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

testdata = [
    (4, True),
    (1757, False),
    (2004, True),
    (1900, False),
    (2000, True)
]


@pytest.mark.parametrize('year, expected', testdata)
def test__is_cat_leap_year__succeeds(year, expected):
    assert catmath.is_cat_leap_year(year) is expected
