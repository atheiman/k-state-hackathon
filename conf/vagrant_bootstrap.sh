#!/usr/bin/env bash



PROJ_NAME=k-state-hackathon
PROJ_DIR=/vagrant

REQUIREMENTS_FILE=$PROJ_DIR/conf/requirements.txt
DJANGO_MANGT_FILE=$PROJ_DIR/manage.py
SETTINGS_PY_PATH=settings.dev
DJANGO_MANGT_VERBOSITY=2
STATIC_ROOT=$PROJ_DIR/static_root

VIRTUALENV_DIR=/opt/virtualenvs
VIRTUALENV=$VIRTUALENV_DIR/$PROJ_NAME

PIP=$VIRTUALENV/bin/pip
PYTHON=$VIRTUALENV/bin/python
GUNICORN=$VIRTUALENV/bin/gunicorn

GUNICORN_CONFIG=$PROJ_DIR/conf/gunicorn_config.wsgi
GUNICORN_SYSTEM_FILES=/tmp/*gunicorn*

NGINX_CONF_DIR=/etc/nginx
NGINX_SITE_CONF=$PROJ_DIR/conf/nginx_site_conf



pretty_print() {
    echo -e "\n\n--$MESSAGE--\n"
}



cd $PROJ_DIR



# Install OS Level Packages
MESSAGE="INSTALLING OS LEVEL PACKAGES"; pretty_print
apt-get update
apt-get install --yes mysql-client libmysqlclient-dev python-dev python-pip nginx
pip install --upgrade --verbose virtualenv



# Setup a virtualenv
MESSAGE="SETTING UP VIRTUALENV"; pretty_print
# If a virtualenv does not exist, then create it
if [ ! -f "$PIP" ]; then
    mkdir --parents $VIRTUALENV
    virtualenv $VIRTUALENV
fi
$PIP install --requirement=$REQUIREMENTS_FILE --upgrade --verbose



# Migrate the database
$PYTHON $DJANGO_MANGT_FILE migrate --settings=$SETTINGS_PY_PATH --verbosity=$DJANGO_MANGT_VERBOSITY



# Prepare static files
MESSAGE="PREPARING STATIC FILES"; pretty_print
rm --recursive --force --verbose $STATIC_ROOT
mkdir --verbose --parents $STATIC_ROOT/static
# collect all apps static files to one dir for serving
$PYTHON $DJANGO_MANGT_FILE collectstatic --settings=$SETTINGS_PY_PATH --noinput --clear --verbosity=$DJANGO_MANGT_VERBOSITY



# Run gunicorn to serve django site
MESSAGE="LAUNCHING GUNICORN"; pretty_print
# Be sure gunicorn processes are killed
pkill -f $PROJ_NAME
rm --force --verbose GUNICORN_SYSTEM_FILES
$GUNICORN --config=$GUNICORN_CONFIG conf.wsgi &



# Configure nginx to proxy django site and serve static files
MESSAGE="CONFIGURING AND LAUNCHING NGINX"; pretty_print
# Be sure nginx is not running
nginx -s quit
pkill nginx
rm --force --verbose $NGINX_CONF_DIR/sites-*/$PROJ_NAME
ln --symbolic --verbose $NGINX_SITE_CONF $NGINX_CONF_DIR/sites-enabled/$PROJ_NAME
nginx
