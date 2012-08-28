#!/bin/bash

# Install the pre-reqs with a package manager.
if [[ $1="--no-prereqs" ]]; then
	echo "Prereq installation skipped."
elif command -v apt-get > /dev/null; then
  echo "Installing prereqs with apt-get..."
  sudo apt-get -y update
  sudo apt-get -y install curl git python python-pip
elif command -v yum > /dev/null; then
  echo "Installing prereqs with yum..."
  sudo yum update
  sudo yum -y install curl git python python-pip
elif command -v pacman >/dev/null; then
  echo "Installing prereqs with pacman..."
  sudo pacman -S curl git python2 python2-pip
else
  echo "Your package manager is not supported by this script. Install pre-reqs manually and then run install.sh again."
  exit
fi

# Upgrade pip and install virtualenv with pip.
echo "Upgrading pip and installing virtualenv..."
if command -v pip2 > /dev/null; then
  pip_command="sudo pip2"
elif command -v pip > /dev/null; then
  pip_command="sudo pip"
else
  echo "Pip was not installed properly. Please make sure that either \"pip\" or \"pip2\" is executable."
  exit
fi
$pip_command install --upgrade pip virtualenv

# Grab the repo from github.
git clone https://github.com/MorganCabral/sse-library.git

# Go into the project directory.
cd sse-library

# Setup the virtual environment we'll be using for development.
# It doesn't particularly matter what you call this.
virtualenv env

# Activate the virtual environment.
. env/bin/activate 

# Note: At this point, there should be the project itself, an env directory and a file called requirements.txt.

# Install project dependencies.
pip install -r requirements.txt

# Note: If we go the PostgreSQL route, set up the db users and such here.

echo "sse-library is installed."
echo "Make sure to run syncdb before attempting to run the app."

# We're done here. Get out of the virtual environment.
deactivate
