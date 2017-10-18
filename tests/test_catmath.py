from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    catage = 5
    assert catmath.cat_years_to_hooman_years(catage) == 25


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    catage = 0.5
    assert catmath.cat_years_to_hooman_years(catage) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    catage = 0
    assert catmath.cat_years_to_hooman_years(catage) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
