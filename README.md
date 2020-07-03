Python repository template
==========================


Things that it has:
-------------------

* requirements with:
    - pytest
    - pytest coverage
    - radon
    - pre-commit
    - sphinx and sphinx rtd theme
* coverage basic configuration
* sh for run radon and tests


Things that you must complete
------------------------------

* Set dir name to run radon in ``run_randon.sh``. Example: ``radon cc -a -s -nb project_name/``
* Set dir name to coverage in testing ``run_tests.sh``. Example: ``pytest -s -vvv --cov=project_name --cov-report term-missing tests``
* Check pre-commit version in ``.pre-commit-config.yaml``
* Set specific version in ``requirements_dev.txt``
