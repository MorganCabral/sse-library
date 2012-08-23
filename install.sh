#!/bin/bash

PM=false
clear

# Install the pre-reqs.
if command -v apt-get > /dev/null
  then
    echo "Installing prereqs with apt-get..."
    sudo apt-get -y update
    sudo apt-get -y install curl git python python-pip
    $PM = true
  fi
if command -v yum > /dev/null
  then
    if $PM == false
      then
        echo "Installing prereqs with yum..."
        sudo yum update
        sudo yum -y install curl git python python-pip
        $PM = true
    fi
  fi
if command -v pacman >/dev/null
  then
    if $PM == false
      then
        echo "Installing prereqs with pacman..."
        sudo pacman -S curl git python2 python2-pip
        $PM = true
    fi
  fi

# I beg of you, get a package manager!
if $PM == false
  then
    echo "Install pre-reqs manually and use install.sh"
    exit
  fi

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
