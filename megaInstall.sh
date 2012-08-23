#!/bin/bash

PM=false
clear

# Install the pre-reqs
if command -v apt-get > /dev/null
  then
    echo "Using apt-get"
    sudo apt-get -y update
    sudo apt-get -y install curl git python python-pip
    $PM = true
  fi
if command -v yum > /dev/null
  then
    if $PM == false
      then
        echo "Using yum"
        sudo yum update
        sudo yum -y install curl git python python-pip
        $PM = true
    fi
  fi
if command -v pacman >/dev/null
  then
    if $PM == false
      then
        echo"Using pacman"
        sudo pacman -Syu curl git python2 python2-pip
        $PM = true
    fi
  fi

# I beg of you, get a package manager!
if $PM == false
  then
    echo "Install pre-reqs manually and use install.sh"
    exit
  fi

# Run the install script
./install.sh
