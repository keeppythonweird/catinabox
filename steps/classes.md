# Testing Classes with Fixtures

1. Refactor the Cattery tests in `tests/test_cattery.py` to use a py.test
   fixture.

   ```python
   @pytest.fixture
   def my_awesome_fixture():
       ...

   def test_stuff(my_awesome_fixture):
       ...
   ```

2. Try adding a `scope` argument to `pytest.fixture`. What happens when
   you try setting it to `scope`, `session`, or `module`?

   ```python
   @pytest.fixture(scope='session')
   def my_awesome_fixture():
       ...
   ```
