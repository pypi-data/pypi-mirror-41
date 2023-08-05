threedi-scenario-downloader
==========================================

The threedi-scenario-downloader package includes functions in order to automate most used download actions on the 3Di results.
Example methods are:

- Download raw results
- Download logging
- Download maximum waterdepth (non-temporal raster)
- Download waterdepth (temporal raster, supply timestamp for snapshot) 
- Find all scenarios model slug or scenario name


Installation
------------

We can be installed with::

  $ pip install threedi-scenario-downloader

(TODO: after the first release has been made)


Development installation of this project itself
-----------------------------------------------

We're installed with `pipenv <https://docs.pipenv.org/>`_, a handy wrapper
around pip and virtualenv. Install that first with ``pip install
pipenv``. Then run::

    $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
    $ pipenv install --dev

There will be a script you can run like this::

    $ pipenv run run-threedi-scenario-downloader

It runs the `main()` function in `threedi-scenario-downloader/scripts.py`,
adjust that if necessary. The script is configured in `setup.py` (see
`entry_points`).

In order to get nicely formatted python files without having to spend manual
work on it, run the following command periodically::

  $ pipenv run black threedi-scenario-downloader

Run the tests regularly. This also checks with pyflakes, black and it reports
coverage. Pure luxury::

  $ pipenv run pytest

The tests are also run automatically on "travis", you'll see it in the pull
requests. There's also `coverage reporting
<https://coveralls.io/github/nens/threedi-scenario-downloader>`_ on
coveralls.io (once it has been set up).
