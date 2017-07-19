# Testing using Parametrization

This assumes you have setup your environment as described in [run_tests.md]
and that you are in your virtualenv.

![hero](../pics/hero.png)

1. Try enhancing your tests in `tests/test_catmath.py` to make use of
   `pytest.mark.parametrize`.

   ```python
   @pytest.mark.parametrize('age', [
       ...
   ])
   def test_cat_to_hooman(age):
       ...
   ```

2. Try enhancing your tests in `tests/test_safecatmath.py` to also use
   `pytest.mark.parametrize`.

3. Take a look at the `McCattery` class in `catinabox/mccattery.py`.
   Doesn't it look an awful lot like the `Cattery`?

   In this step you will attempt (and succeed!) in making the tests in
   `tests/test_cattery.py` run against both the `Cattery` and `McCattery`.
   This step assumes that you have completed the previous activity where
   you refactored the cattery tests to use a fixture.

   ```python
   @pytest.fixture
   def cattery_client():
       return cattery.Cattery()

   def test_the_things(cattery_client):
       ...
   ```

   First we start by parameterizing the fixture.

   ```python
   @pytest.fixture(params=[
       ...
   ])
   def cattery_client(request):
       ...
   ```

   Don't worry about the magical `request` argument for now. It can do
   a lot of things, but we'll be using its ability to access that
   `params` argument we passed to `pytest.fixture`.

   Everytime pytest goes to create this fixture, it will assign the next
   thing in `params` to `request.param`. As you hopefully heard from the
   slides, pytest will run every possible permutation of fixtures and
   the tests that require them.

   Think of all the testing possibilities!
  
4. When the tests run successfully, push them to your pull request:

  ```bash
  (catpy)user@host:~/catinabox$ git commit -a
  (catpy)user@host:~/catinabox$ git push origin master
  ```

## BONUS

Take a look at [fixture parameterization](http://pytest.org/latest/fixture.html#fixture-parametrize).
How could this be useful for testing the `mccattery` module?

Take a look at [test_mccattery.py](https://github.com/keeppythonweird/catinabox/blob/solutions/tests/test_mccattery.py)
for a solution.
