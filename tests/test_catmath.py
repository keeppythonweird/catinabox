from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(10) == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2


def modulus_4(year):
    if year % 4 != 0:
        return False
    else:
        return True


def test__modulus_4__succeeds():
    assert modulus_4(2016) is True


def test__modulus_4_fails():
    assert modulus_4(2015) is False
