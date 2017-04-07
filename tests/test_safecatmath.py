import pytest
from catinabox import safecatmath


@pytest.mark.parametrize("cat, human", [
                         (7, 35),
                         (0.1, 0.5),
                         (0, 0)
                         ])
def test__cat_years_to_hooman_years__middle_age__succeeds(cat, human):
    hooman_age = safecatmath.cat_years_to_hooman_years(cat)
    assert hooman_age == human


@pytest.mark.parametrize("invalid_year", [
                         -1, 1001, "Dog", float('nan')
                         ])
def test__cat_years_to_hooman_years__less_0__raises(invalid_year):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(invalid_year)


"""
def test__cat_years_to_hooman_years__older_than_1000__raises():
    cat_years = 1001
    with pytest.raises(Exception) as excinfo:
        safecatmath.cat_years_to_hooman_years(cat_years)

    assert "InvalidAge" in str(excinfo.type)


def test__cat_years_to_hooman_years__string__raises():
    cat_years = "Dog"
    with pytest.raises(Exception) as excinfo:
        safecatmath.cat_years_to_hooman_years(cat_years)

    assert "InvalidAge" in str(excinfo.type)


def test__cat_years_to_hooman_years__nan__raises():
    cat_years = float('nan')
    with pytest.raises(Exception) as excinfo:
        safecatmath.cat_years_to_hooman_years(cat_years)

    assert "InvalidAge" in str(excinfo.type)
"""
