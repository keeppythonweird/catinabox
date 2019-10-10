import pytest
from catinabox import catmath


@pytest.mark.parametrize("age, expected", [
    (10, 50),
    (0.5, 2.5),
    (0, 0)
])
def test__cat_years_to_hooman_years(age, expected):
    assert catmath.cat_years_to_hooman_years(age) == expected


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2000) is True
    assert catmath.is_cat_leap_year(2100) is False
    assert catmath.is_cat_leap_year(1997) is False
