from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(7) == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__not_multiple_of_4__fails():
    assert catmath.is_cat_leap_year(1999) is False


def test__is_cat_leap_year__is_100_year__not_multiple_of_400__fails():
    assert catmath.is_cat_leap_year(1900) is False


def test__is_cat_leap_year__is_100_year__multiple_of_400__succeeds():
    assert catmath.is_cat_leap_year(2000) is True
