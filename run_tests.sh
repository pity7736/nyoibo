#!/usr/bin/env bash
echo "Build cython modules..."
python setup.py build_ext
echo "Installing project locally..."
pip install -e .
echo "Running pytest..."
pytest -s -vvv --cov=nyoibo --cov-report term-missing tests
