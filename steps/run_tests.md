# Setup your environment and run the tests

Before you can start adding test coverage, you'll need to create a fork for
your changes, setup your environment and run your tests.

1. You will be pushing changes back to the repo, so you can create a pull
   request and run your tests on our build servers, so you'll need to make a
   fork.

   Fork [catinabox](https://github.com/keeppythonweird/catinabox) though
   the github webpage, using the `Fork` button.

2. Checkout your fork:

  ```bash
  user@host:~$ git clone git@github.com:<MYUSERNAME>/catinabox.git
  ```

3. Let's create a virtual environment so you can install packages without
   affecting the rest of your system. Create a virtual environment for running
   `catinabox``:

  ```bash
  user@host:~$ cd catinabox
  user@host:~/catinabox$ virtualenv catpy
  ```

4. Activate your virtual environment.

  If you are using Linux or a Mac:

  ```bash
  user@host:~/catinabox$ source catpy/bin/activate
  (catpy)user@host:~/catinabox$
  ```

  If you are on Windows:

  ```
  $ .\catpy\Scripts\activate
  ```

  You are now in your virtual environment, as indicated by the `(catpy)` prefix
  in your shell prompt.

5. "Install" catinabox to your site-packages to make sure pytest can find it.

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py develop
  ```

6. Now that you're setup, you can run the tests!

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```

The tests pass, but why is the coverage so low? Because most of the tests
are empty! You'll be filling them in during the next steps.
