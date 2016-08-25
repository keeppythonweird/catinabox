import pytest
from catinabox import catmath


# def test__cat_years_to_hooman_years__middle_age__succeeds():
#     assert catmath.cat_years_to_hooman_years(7.5) == 37.5
#
#
# def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
#     assert catmath.cat_years_to_hooman_years(0.5) == 2.5
#
#
# def test__cat_years_to_hooman_years__0__returns_0():
#     assert catmath.cat_years_to_hooman_years(0) == 0
#
#
@pytest.mark.parametrize("test_input, expected", [
    (1, 5),
    (3, 15),
    (5, 25),
    (0, 0),
    (0.5, 2.5),
])
def test__cat_years_to_hooman_years(test_input, expected):
    assert catmath.cat_years_to_hooman_years(test_input) == expected


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2015) is False
    assert catmath.is_cat_leap_year(100) is False
    assert catmath.is_cat_leap_year(400) is True
