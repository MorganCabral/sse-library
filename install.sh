# Replace the following with your system's equivalent.
sudo apt-get update && sudo apt-get install python virtualenv # Ubuntu
# sudo yum update && yum install python virtualenv # Fedora/RHEL/etc.
# sudo pacman -Syu python virtualenv # Arch

# Put the project somewhere. Doesn't particularly matter where.
mkdir ~/Projects/PROJECT_NAME && cd ~/Projects/PROJECT_NAME

# Setup the virtual environment we'll be using for development.
# It doesn't particularly matter what you call this.
virtualenv env

# Activate the virtual environment.
source env/bin/activate

# Note: At this point you should see "(env)" somewhere in your
# terminal input line thingy.

# Grab the repo from github.
git clone *REPO-URL-HERE*

# Note: At this point, you should have the django project, your virtual
# environment and a requirements.txt file in your project directory.

# Install project dependencies.
pip install -r requirements.txt

# Note: If we go the PostgreSQL route, set up the db users and such here.

# Run syncdb to setup the datebase schema.
cd PROJECT_NAME && python manage.py syncdb

# Note: If using gunicorn, use this command instead of the follow.
python manage.py run_gunicorn

# Start up a local dev server to test with.
python manage.py runserver

# Run this if you want to get out of the virtual environment.
deactivate