# sse-library [![Build Status](https://secure.travis-ci.org/rit-sse/sse-library.png?branch=master)](http://travis-ci.org/rit-sse/sse-library)
A CMS driven library book management system built on top of Django. This is being developed by the Society of Software Engineers at RIT. More to come in the fall....

## Installation
This script tries to automagically install prereqs for you with a package
manager, and then sets up additional things you will need for working on the
library. If your system doesn't have a compatible package manager, you can
install the preqres manually and then run the rest of the install script as
usual.

### Systems with apt-get/yum/pacman (Ubuntu/Debian/Fedora/Red Hat/Arch/etc.)
1. `bash <(curl https://raw.github.com/rit-sse/sse-library/master/install.sh -o -)`

### Mac OS
1. Read and follow the [Homebrew and
Python](https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python) article.
2. `bash <(curl https://raw.github.com/rit-sse/sse-library/master/install.sh -o -) --no-prereqs`

### Other systems
1. [Install Curl, Git, Python 2.7.x and PIP
manually.](https://github.com/rit-sse/sse-library/wiki/Installation-Prereqs)
2. `bash <(curl https://raw.github.com/rit-sse/sse-library/master/install.sh -o -) --no-prereqs`
