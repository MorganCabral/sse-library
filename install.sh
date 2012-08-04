#!/bin/bash

# Grab the repo from github.
git clone https://github.com/MorganCabral/sse-library.git

# Go into the project directory.
cd sse-library

# Setup the virtual environment we'll be using for development.
# It doesn't particularly matter what you call this.
virtualenv env

# Note: At this point, there should be the project itself, an env directory and a file called requirements.txt.

# Install project dependencies.
source env/bin/activate && pip install -r requirements.txt && deactivate

# Note: If we go the PostgreSQL route, set up the db users and such here.

# Run syncdb to setup the datebase schema.
source env/bin/activate && cd sse_library && ./manage.py syncdb && deactivate
