from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 7
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.1
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = catmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__2004():
    assert catmath.is_cat_leap_year(2004) is True


def test__is_cat_leap_year__not_divisible_by_4_is_not_leap_year():
    assert catmath.is_cat_leap_year(1933) is False


def test__is_cat_leap_year__divisible_by_100_is_not_leap_year():
    assert catmath.is_cat_leap_year(1900) is False


def test__is_cat_leap_year__divisible_only_by_4_is_not_leap_year():
    assert catmath.is_cat_leap_year(1800) is False


def test__is_cat_leap_year__not_divisible_by_400_is_not_leap_year():
    assert catmath.is_cat_leap_year(1700) is False


def test__is_cat_leap_year__divisible_by_4_400_is_not_leap_year():
    assert catmath.is_cat_leap_year(1660) is True
