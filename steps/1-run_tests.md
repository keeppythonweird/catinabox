# Setup your environment and run the tests

Before you can start adding test coverage, you'll need to create a fork for
your changes, setup your environment and run your tests.

1. You will be pushing changes back to the repo, so you can create a pull
   request and run your tests on our build servers, so you'll need to make a
   fork.

   Fork [catinabox](https://github.com/keeppythonweird/catinabox) though
   the github webpage, using the `Fork` button.

![fork](../pics/fork.png)

2. Clone your fork:

  ```bash
  user@host:~$ git clone git@github.com:<MYUSERNAME>/catinabox.git
  ```
  
3. Create a branch and push it to your fork:

  ```bash
  user@host:~$ cd catinabox
  user@host:catinabox$ git checkout -b tutorial_wip
  user@host:catinabox$ git push origin tutorial_wip
  ```
  
  `tutorial_wip` is the name of the branch and can be any arbitrary string.
  [More information on git branches is available in the github documentation](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches).

4. Let's create a virtual environment so you can install packages without
   affecting the rest of your system. Create a virtual environment for running
   `catinabox``:

  ```bash
  user@host:~/catinabox$ virtualenv catpy
  ```

5. Activate your virtual environment.

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

6. "Install" catinabox to your site-packages to make sure pytest can find it.

  ```bash
  (catpy)user@host:~/catinabox$ pip install -e .
  (catpy)user@host:~/catinabox$ pip install -r test_requirements.txt
  ```

7. Now that you're setup, you can run the tests!

  ```bash
  (catpy)user@host:~/catinabox$ python setup.py test
  ```

The tests pass, but why is the coverage so low? Because most of the tests
are empty! You'll be filling them in during the next steps.
