from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 8
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 40


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.2
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 1


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__normal_leap_year__is_leap_year():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__divided_by_400__is_leap_year():
    assert catmath.is_cat_leap_year(2000) is True


def test__is_cat_leap_year__divieded_by_100__is_no_leap_year():
    assert catmath.is_cat_leap_year(1900) is False


def test__is_cat_leap_year__normal_year__is__no_leap_year():
    assert catmath.is_cat_leap_year(2017) is False
