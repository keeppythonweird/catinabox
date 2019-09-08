import pytest
from catinabox import catmath


@pytest.mark.parametrize('age', [8])
def test__cat_years_to_hooman_years__middle_age__succeeds(age):
    assert catmath.cat_years_to_hooman_years(age) == 40


@pytest.mark.parametrize('age', [0.5])
def test__cat_years_to_hooman_years__less_than_one_year__succeeds(age):
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


@pytest.mark.parametrize('age', [0])
def test__cat_years_to_hooman_years__0__returns_0(age):
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2


@pytest.mark.parametrize('year', [2008, 2012, 2016])
def test__is_cat_leap_year__succeeds(year):
    assert catmath.is_cat_leap_year(year) is True


@pytest.mark.parametrize('year', [2009, 2011, 2015])
def test__is_cat_lear_year__fails(year):
    assert catmath.is_cat_leap_year(year) is False
