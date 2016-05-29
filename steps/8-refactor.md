# Refactoring for unit testability

This assumes you have setup your environment as described in [run_tests.md]
and that you are in your virtualenv.

![hero](../pics/catinabox.png)

1. Take a look at the code in `catinabox/catgenerator.py` and think about
   how you would write unit tests for it. There's a lot going on in that
   one method isn't there!
   
   Think about the mocks you would need, and what test cases you would
   cover.

2. Refactor `cat_generator` to be more unit testable:

   * What responsibilities does `cat_generator` have?
   * Can you break `cat_generator` into several methods, each of which
     does only one thing?

3. Write unit tests for the refactored `catinabox/catgenerator.py` in
   `tests/test_catgenerator.py`. Try to get as much coverage as possible.
   
4. As you refactor and write new tests, run them:

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```

5. When the tests run successfully, push them to your pull request:

  ```bash
  (catpy)user@host:~/catinabox$ git commit -a
  (catpy)user@host:~/catinabox$ git push origin master
  ```

## BONUS

If you finish writing tests for your refactored code, make a copy of the
original `catgenerator.py` and write unit tests for it. Compare theses tests
with the tests for the refactored version. What are benefits and drawbacks
of each? How many tests cases do you need in each case?