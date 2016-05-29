# Testing Classes with Fixtures

This assumes you have setup your environment as described in [run_tests.md]
and that you are in your virtualenv.

![cattery](../pics/cattery.png)

If you get stuck, [take a peek at the solution](https://github.com/keeppythonweird/catinabox/blob/solutions/tests/test_cattery.py).

1. Refactor the Cattery tests in [test_cattery.py](../tests/test_cattery.py)
   to use a py.test fixture.

   ```python
   @pytest.fixture
   def cattery_client():
       ...

   def test__add_cats__succeeds(cattery_client):
       ...
   ```

2. Try adding a `scope` argument to `pytest.fixture`. What happens when
   you try setting it to `scope`, `session`, or `module`?

   ```python
   @pytest.fixture(scope='session')
   def cattery_client():
       ...
   ```

3. When you are done, run your tests:

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```
  
4. When the tests run successfully, push them to your pull request:

  ```bash
  (catpy)user@host:~/catinabox$ git commit -a
  (catpy)user@host:~/catinabox$ git push origin master
  ```


## BONUS

Take a look at the [builtin fixtures](https://pytest.org/latest/builtin.html#builtin-fixtures-function-arguments<Paste>)
that pytest provides. Are there any that would be useful for these, or
any of the previous tests you have written so far? Can you think of some
ways you might use fixtures when writing tests for your other projects?

We'd love to discuss this with you!
