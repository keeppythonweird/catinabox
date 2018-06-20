from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_years = 10
    human_years = catmath.cat_years_to_hooman_years(cat_years)
    assert human_years == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_years = 0.5
    human_years = catmath.cat_years_to_hooman_years(cat_years)
    assert human_years == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2
def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
