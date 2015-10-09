# Control time with mock and patch

This assumes you have setup your environment as described in [run_tests.md]
and that you are in your virtualenv.

1. Take a look at the ```cat_nap``` method in
   [catactivies.py](../catinabox/catactivities.py). This method 
   sleeps for the provided amount of time if the nap will be
   satisfying. If it won't be, an exception is raised.

2. Look at [the test stubs](../tests/test_catactivities.py):

    * ```test__cat_nap__satisfying_nap```
    * ```test__cat_nap__not_satisfying```
   
3. Fill in the body of these tests, using ```mock.patch``` to control the
   behaviour of ```time.sleep```.
   
   Be sure to check that ```time.sleep``` is called correctly!

4. When you have filled in the body of these tests, run them:

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```
  
5. When the tests run successfully, push them to your pull request:

  ```bash
  (catpy)user@host:~/catinabox$ git commit -a
  (catpy)user@host:~/catinabox$ git push origin master
  ```
  
