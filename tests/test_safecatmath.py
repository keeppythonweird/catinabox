import pytest
from catinabox import safecatmath
import numpy as np


@pytest.mark.parametrize('age', [7])
def test__cat_years_to_hooman_years__middle_age__succeeds(age):
    hooman_age = safecatmath.cat_years_to_hooman_years(age)
    assert hooman_age == 35


@pytest.mark.parametrize('age, expected', [(0.1, 0.5)])
def test__cat_years_to_hooman_years__less_than_one_year(age, expected):
    hooman_age = safecatmath.cat_years_to_hooman_years(age)
    assert hooman_age == expected


@pytest.mark.parametrize('age', [0])
def test__cat_years_to_hooman_years__0__returns_0(age):
    hooman_age = safecatmath.cat_years_to_hooman_years(age)
    assert hooman_age == 0


@pytest.mark.parametrize('age', [-1, -2])
def test__cat_years_to_hooman_years__less_0__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)


# @pytest.mark.parametrize('age', [1000])
# def test__cat_years_to_hooman_years__older_than_1000__raises(age):
#     with pytest.raises(safecatmath.InvalidAge):
#         safecatmath.cat_years_to_hooman_years(age)


@pytest.mark.parametrize('age', ['5', '#5', 'five'])
def test__cat_years_to_hooman_years__string__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)


@pytest.mark.parametrize('age', [float('nan'), np.nan])
def test__cat_years_to_hooman_years__nan__raises(age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(age)
