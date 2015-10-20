import pytest
from catinabox import catmath

'''
def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(6) == 30


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
'''


@pytest.mark.parametrize("age, expected", [
    (6, 30),
    (0.5, 2.5),
    (0, 0)
])
def test__cat_years_to_hooman(age, expected):
    assert catmath.cat_years_to_hooman_years(age) == expected
