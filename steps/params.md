# Testing using Parametrization

After each of these steps please feel free to commit your changes, run your tests, and push them to Github!

```bash
$ <Make changes to tests.>
$ python setup.py test
$ git commit -a
$ git push origin master
$ <Check your pull request for Travis build results!>
```

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

   First we start by parametrizing the fixture.

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
