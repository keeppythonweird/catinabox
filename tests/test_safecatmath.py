from catinabox import safecatmath
import pytest


@pytest.mark.parametrize(
    'age,hooman_age',
    [(7, 35), (0.1, 0.5), (0, 0)]
    )
def test_cat_years_to_hooman_years__succeeds(age, hooman_age):
    assert safecatmath.cat_years_to_hooman_years(age) == hooman_age


@pytest.mark.parametrize(
    'age',
    [1001, '100', float('nan')]
    )
def test_cat_years_to_hooman_years__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)
