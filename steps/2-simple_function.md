# Write tests for a simple function

This assumes you have setup your environment as described in [run_tests.md]
and that you are in your virtualenv.

![calico](../pics/calico.png)

If you get stuck, [take a peek at the solution](https://github.com/keeppythonweird/catinabox/blob/solutions/tests/test_catmath.py).

1. We will be writing tests for [catmath.py](../catinabox/catmath.py).
   This module contains only one function ```cat_years_to_hooman_years```.

2. Look at [the existing tests](../tests/test_catmath.py). You can see there
   are test stubs:
   
   * ```test__cat_years_to_hooman_years__middle_age__succeeds```
   * ```test__cat_years_to_hooman_years__less_than_one_year__succeeds```
   * ```test__cat_years_to_hooman_years__0__returns_0```
   
3. Fill in the body of these tests. Based on their names, what test case do
   you think each of these is trying to cover?
   
   Each test should be calling ```cat_years_to_hooman_years``` with different
   input and asserting based on the output.

4. When you have filled in the body of these tests, run them:

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```
  
5. (Optional) Bonus: Try to write some tests for ```is_cat_leap_year```. (When 
   these tests run successfully, you should see an increase in coverage!) Are
   you sufficiently convinced that this function works now? Why or why not?

   We'd love to have a discussion about this with you if you get this far. Every
   developer will have different opinions about this :)
