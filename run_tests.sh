#!/usr/bin/env bash
pytest -s -vvv --cov=nyoibo --cov-report term-missing tests
