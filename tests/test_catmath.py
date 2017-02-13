from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 6
    human_eq = catmath.cat_years_to_hooman_years(cat_age)
    assert human_eq == 30


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.7
    human_eq = catmath.cat_years_to_hooman_years(cat_age)
    assert human_eq == 3.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    human_eq = catmath.cat_years_to_hooman_years(cat_age)
    assert human_eq == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(1761) is False


def test__is_cat_leap_year__succeeds_year_100_cond():
    assert catmath.is_cat_leap_year(2100) is False


def test__is_cat_leap_year__succeeds_year_400_cond():
    assert catmath.is_cat_leap_year(2400) is True
