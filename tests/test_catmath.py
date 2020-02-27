from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 10
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.5
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0


def test_felipe():
    assert catmath.is_cat_leap_year(5) is False


def test_benicio():
    assert catmath.is_cat_leap_year(104) is True


def test_maiara():
    assert catmath.is_cat_leap_year(500) is False


def test_final():
    assert catmath.is_cat_leap_year(400) is True
