import pytest
from catinabox import catmath


@pytest.mark.parametrize("input, expected", [
    (3, 15),
    (0.2, 1.0),
    (0, 0)
])
def test__cat_years_to_hooman_years__succeeds(input, expected):
    assert catmath.cat_years_to_hooman_years(input) == expected


# BONUS MATERIAL FOR STEP 2

@pytest.mark.parametrize("input, expected", [
    (1757, False),
    (1900, False),
    (2000, True),
    (2004, True)
])
def test__is_cat_leap_year(input, expected):
    assert catmath.is_cat_leap_year(input) is expected
