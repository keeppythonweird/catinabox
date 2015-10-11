from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 8
    human_age = catmath.cat_years_to_hooman_years(cat_age)
    assert human_age == 40


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.8
    human_age = catmath.cat_years_to_hooman_years(cat_age)
    assert human_age == 4


def test__cat_years_to_hooman_years__0__returns_0():
    human_age = catmath.cat_years_to_hooman_years(0)
    assert human_age == 0
