# Write tests for incorrect input

This assumes you have setup your environment as described in [run_tests.md]
and that you are in your virtualenv.

1. This time we will be writing tests for [safecatmath.py](../catinabox/safecatmath.py).
   This module contains a new version of ```cat_years_to_hooman_years```.

2. Look at [the existing tests](../tests/test_safecatmath.py).
   You can see we have similar test cases to the ones we had for
   ```cat_years_to_hooman_years``` but several more cases have been added:
   
   * ```test__cat_years_to_hooman_years__less_0__raises```
   * ```test__cat_years_to_hooman_years__older_than_1000__raises```
   * ```test__cat_years_to_hooman_years__string__raises```
   
3. Fill in the body of these tests, using ```pytest.raises```.

4. When you have filled in the body of these tests, run them:

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```
  
5. When the tests run successfully, push them to your pull request:

  ```bash
  (catpy)user@host:~/catinabox$ git commit -a
  (catpy)user@host:~/catinabox$ git push origin master
  ```
  
