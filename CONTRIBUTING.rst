.. highlight:: shell

============
贡献
============

欢迎您的贡献！
你能如下方式贡献:

贡献类型:
----------------------


提交 bugs
~~~~~~~~~~~

可以在这里 https://github.com/llango/shaphinx/issues 提交bug。

如果提交bug，请包括:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

修复 bugs 
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

实现的功能
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

编写文档
~~~~~~~~~~~~~~~~~~~

Shaphinx could always use more documentation, whether as part of the
official A Sphinx Theme docs, in docstrings, or even on the web in blog posts,
articles, and such.

提交反馈
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/llango/shaphinx/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

开始
------------

Ready to contribute? Here's how to set up `shaphinx` for local development.

1. Fork the `shaphinx` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/shaphinx.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv shaphinx
    $ cd shaphinx/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 shaphinx tests
    $ python setup.py test or pytest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

拉请求向导
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/llango/shaphinx/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::


    $ python -m unittest tests.test_shaphinx

发布
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.
