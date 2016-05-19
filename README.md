# catinabox - Intro to Testing and Test Automation in Python
[![Build Status](https://travis-ci.org/keeppythonweird/catinabox.svg?branch=master)](https://travis-ci.org/keeppythonweird/catinabox)

Coverage status:
* Master (test stubs only): [![Coverage Status (Pre tests)](https://coveralls.io/repos/keeppythonweird/catinabox/badge.svg?branch=master&service=github)](https://coveralls.io/github/keeppythonweird/catinabox?branch=master)
* [Solutions branch](https://github.com/keeppythonweird/catinabox/tree/solutions) (all tests added): [![Coverage Status (Post tests)](https://coveralls.io/repos/keeppythonweird/catinabox/badge.svg?branch=solutions&service=github)](https://coveralls.io/github/keeppythonweird/catinabox?branch=solutions)

Accompanies the [Intro to Testing and Test Automation in Python slide deck](https://docs.google.com/presentation/d/1cNgZdkw2cik4i4Mc1Ka7frPAdZky3hwpq0vycBDMufE/edit). Aesthetic inspired by [@sailorhg](https://twitter.com/sailorhg).

![catinabox](pics/catinabox.png)

This repo holds a tutorial which will walk you through adding unit tests,
exploring these features of unit testing in general and pytest in particular:
- Basic unit testing
- Observing test success and coverage using
  [Travis CI](https://travis-ci.org/) and [coveralls](https://coveralls.io/).

# Requirements

1. Github accounts
2. Python (2.7 or 3.x) with:
  - pip
  - virtualenv
5. Git (either Github for Windows or command-line git)
6. Text editor or IDE (e.g. Pycharm)

# Tutorial Steps

1. [Setup and run tests](./steps/1-run_tests.md)
2. [Test a simple function](./steps/2-simple_function.md)
3. [Create and build a pull request](./steps/3-pull.md)
4. [Testing incorrect input](./steps/4-input.md)
5. [Testing classes with fixtures](./steps/5-classes.md)
6. [Using mock and patch](./steps/6-mock.md)
7. [Parameterized tests](./steps/7-params.md)

Solutions are visible by viewing [the solutions branch](https://github.com/keeppythonweird/catinabox/tree/solutions).

![cattery](pics/cattery.png)
