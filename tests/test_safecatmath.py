import pytest

from catinabox import safecatmath


@pytest.mark.parametrize("input, expected", [
    (7, 35),
    (0.1, 0.5),
    (0, 0)
])
def test__cat_years_to_hooman_years__succeeds(input, expected):
    hooman_age = safecatmath.cat_years_to_hooman_years(input)
    assert hooman_age == expected


@pytest.mark.parametrize("input", [
    -1, 10001, "5", float('nan')
])
def test__cat_years_to_hooman_years__raises(input):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(input)
