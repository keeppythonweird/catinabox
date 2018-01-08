from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(8) == 40


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.8) == 4


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__not_divisible_by_4__isnt_leap_year():
    assert catmath.is_cat_leap_year(1357) is False


def test__is_cat_leap_year__divisible_by_100__isnt_leap_year():
    assert catmath.is_cat_leap_year(1700) is False


def test__is_cat_leap_year__centurial_leap_year__is_leap_year():
    assert catmath.is_cat_leap_year(2000) is True


def test__is_cat_leap_year__typical_leap_year__is_leap_year():
    assert catmath.is_cat_leap_year(2008) is True
