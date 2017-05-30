from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(4) == 20
    assert catmath.cat_years_to_hooman_years(5) == 25
    assert catmath.cat_years_to_hooman_years(6) == 30
    assert catmath.cat_years_to_hooman_years(7) == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(.1) == 0.5
    assert catmath.cat_years_to_hooman_years(.3) == 1.5
    assert catmath.cat_years_to_hooman_years(.5) == 2.5
    assert catmath.cat_years_to_hooman_years(.8) == 4


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__not_mod_4():
    assert catmath.is_cat_leap_year(2001) is False


def test__is_cat_leap_year__not_mod_100():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__not_mod_400():
    assert catmath.is_cat_leap_year(1700) is False


def test__is_cat_leap_year__else():
    assert catmath.is_cat_leap_year(1600) is True
