from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    #assert True
    assert catmath.cat_years_to_hooman_years(8) == 40 


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    #assert True
    assert catmath.cat_years_to_hooman_years(0.9) == 4.5


def test__cat_years_to_hooman_years__0__returns_0():
    #assert True
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    
def test__is_cat_leap_year_fails():
    assert catmath.is_cat_leap_year(2023) is False
    
def test__is_cat_leap_year_modulo100_succeeds():
    assert catmath.is_cat_leap_year(2000) is True
    
def test__is_cat_leap_year_divisible_by_100_is_not_leap_year():
    assert catmath.is_cat_leap_year(1900) is False    
    
def test_is_cat_leap_year_modulo400_succeeds():
    assert catmath.is_cat_leap_year(2400) is True
    
def test_is_cat_leap_year_modulo4_fails():
    assert catmath.is_cat_leap_year(1806) is False
    
