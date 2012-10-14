# sse-library [![Build Status](https://secure.travis-ci.org/MorganCabral/sse-library.png?branch=master)](http://travis-ci.org/MorganCabral/sse-library)
A CMS driven library book management system built on top of Django. This is being developed by the Society of Software Engineers at RIT. More to come in the fall....

## Installation
This script tries to automagically install prereqs for you with a package
manager, and then sets up additional things you will need for working on the
library. If your system doesn't have a compatible package manager, you can
install the preqreqs manually and then run the rest of the install script as
usual.

### Windows
1. Open PowerShell (cmd.exe will not work).
2. `(New-Object System.Net.WebClient).DownloadString("http://bit.ly/Rn6VNl") | Invoke-Expression`

Pro Tip: You can right click to paste stuff into PowerShell.

### Mac OS
1. Read and follow the [Homebrew and
Python](https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python) article.
2. `bash <(curl https://raw.github.com/MorganCabral/sse-library/master/install.sh -o -) --no-prereqs`

### Linux with apt-get/yum/pacman (Ubuntu/Debian/Fedora/Red Hat/Arch/etc.)
1. `bash <(curl https://raw.github.com/MorganCabral/sse-library/master/install.sh -o -)`

### Other systems
1. [Install Curl, Git, Python 2.7.x and PIP
manually.](https://github.com/MorganCabral/sse-library/wiki/Installation-Prereqs)
2. `bash <(curl https://raw.github.com/MorganCabral/sse-library/master/install.sh -o -) --no-prereqs`
