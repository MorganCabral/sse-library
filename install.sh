#!/bin/bash

# Grab the repo from github.
git clone https://github.com/MorganCabral/sse-library.git

# Go into the project directory.
cd sse-library

# Setup the virtual environment we'll be using for development.
# It doesn't particularly matter what you call this.
virtualenv env

# Activate the virtual environment.
source env/bin/activate 

# Note: At this point, there should be the project itself, an env directory and a file called requirements.txt.

# Install project dependencies.
pip install -r requirements.txt

# Note: If we go the PostgreSQL route, set up the db users and such here.

# Run syncdb to setup the datebase schema.
#cd sse_library && python manage.py syncdb

# We're done here. Get out of the virtual environment.
deactivate
