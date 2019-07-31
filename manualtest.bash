#!/usr/bin/env bash

rm manual.db

export environment=manual

python3 -m unittest discover testing/manual_test

