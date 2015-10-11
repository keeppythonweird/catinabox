from catinabox import catmath
import pytest


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(11) == 55


def test__cat_years_to_hooman_years__partial_year__succeeds():
    assert catmath.cat_years_to_hooman_years(2.5) == 12.5


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.6) == 3


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


def test__cat_years_to_hooman_years__negative_year__succeeds():
    assert catmath.cat_years_to_hooman_years(-1) == -5


def test__cat_years_to_hooman_years__NaN__fails():
    with pytest.raises(TypeError):
        catmath.cat_years_to_hooman_years(None)
