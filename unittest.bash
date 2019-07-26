#!/usr/bin/env bash

python3 -m unittest discover testing/unittest

coverage run -m unittest discover -s testing/unittest

coverage report -m --omit="*/test*"

coverage html --omit="*/test*" -d reports/unittest_coverage_report

