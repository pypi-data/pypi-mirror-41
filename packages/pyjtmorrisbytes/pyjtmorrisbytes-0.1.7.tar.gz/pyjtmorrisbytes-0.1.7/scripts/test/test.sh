#!/usr/bin/bash
export FLASK_ENV='testing'
export ENV='Testing'
export APP_NAME='pyjtmorrisbytes'
export DATABASE_URL = 'psql://postgres@localhost/test-pyjtmorrisbytes'
export DO_COMPILE = 'true'
# ./scripts/build/build-cython.sh
print "hello from test.sh"