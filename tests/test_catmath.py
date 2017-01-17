import pytest

from catinabox import catmath


@pytest.mark.parametrize(('input_', 'expected'), [(40, 200),
                                                  (0.5, 2.5),
                                                  (0, 0)])
def test__cat_years_to_hooman_years__returns_success(input_, expected):
    assert catmath.cat_years_to_hooman_years(input_) == expected


# BONUS MATERIAL FOR STEP 2


@pytest.mark.parametrize(['year', 'bool_'], [(2000, True),
                                             (2004, True)])
def test__is_cat_leap_year__succeeds(year, bool_):
    assert catmath.is_cat_leap_year(year) is bool_


@pytest.mark.parametrize(['year', 'bool_'], [(2001, False),
                                             (2100, False)])
def test__is_cat_leap_year__fails(year, bool_):
    assert catmath.is_cat_leap_year(year) is bool_
