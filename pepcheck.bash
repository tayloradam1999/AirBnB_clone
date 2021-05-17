#!/bin/bash
autopep8 -i -a models/*.py tests/*.py
pep8 models/*.py tests/*.py
