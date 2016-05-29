from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 8
    expected_hooman_age = 40
    actual_hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert actual_hooman_age == expected_hooman_age


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.1
    expected_hooman_age = 0.5
    actual_hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert actual_hooman_age == expected_hooman_age


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    expected_hooman_age = 0
    actual_hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert actual_hooman_age == expected_hooman_age


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__divisible_by_400():
    assert catmath.is_cat_leap_year(2000) is True


def test__is_cat_leap_year__not_divisible_by_400():
    assert catmath.is_cat_leap_year(1900) is False
