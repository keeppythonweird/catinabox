# Create a pull request and see your progress - Travis CI and Coveralls

In this step, you will commit your changes, and create a pull request. This
will kick off continuous integration and coverage reporting, which you can
see from your pull request.

![coveralls](../pics/coveralls.png)

1. Take a look at:
  * [The current build status](https://travis-ci.org/keeppythonweird/catinabox)
  * [The current coverage](https://coveralls.io/github/keeppythonweird/catinabox?branch=master)
  
  You can see that the build is successfully passing, but the overall coverage
  is pretty low.
  
2. Commit your new unit tests from [the previous step](./2-simple_function.md)
  to your fork of `catinabox`:
  
  ```bash
  user@host:~$ git commit -a
  ```
3. When you are happy with your commit and your changes, push them back to your
   fork:
   
  ```bash
  user@host:~$ git push origin pycon2016
  ```

4. Visit github and open a new pull request:

  1. [https://github.com/keeppythonweird/catinabox](https://github.com/keeppythonweird/catinabox)
  2. 'Open Pull Request' or 'Pull Requests' -> 'New Pull Request'

5. As soon as the pull request is created, you will see three checks run:
  
  1. Travis CI - Running all tests for python 2.7
  2. Travis CI - Running all tests for python 3.4
  3. Coveralls measuring the test coverage for your branch

6. If you see a build failure, you can run all tests locally:

  ```bash
  user@host:~$ python setup.py test
  ```
  
  However if the failure is with the other major version of python (e.g.
  you are running 3.4 locally but the 2.7 build broke) you will not be able
  to reproduce the failure.
  
