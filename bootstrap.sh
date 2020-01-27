# !/usr/bin/env bash

YQ="-y -q"
export DEBIAN_FRONTEND=noninteractive
apt update $YQ
apt upgrade $YQ

# prerequirements
apt install $YQ build-essential libssl-dev libffi-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libreadline-dev wget

# python3.8.1 from source
PYTHON_VERSION='3.8.1'

cd /tmp
wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
tar -xf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION
./configure --enable-optimizations
make --jobs $(nproc) && make install
cd /home/vagrant
rm -rf /tmp/*

# alias
ln -s -f /usr/local/bin/python3 /usr/local/bin/python

# python environment
apt install $YQ libpq-dev

# postgresql
su -c "printf 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main' >> /etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt update $YQ
apt install $YQ postgresql-11 postgresql-contrib-11

while IFS='' read -r line || [[ -n "$line" ]]; do
    su postgres -c "psql -c \"$line\" "
done < /vagrant/local_deploy/psql/init_db.sql

# gettext
apt install $YQ gettext

# # memcached
# apt install $YQ memcached

# # rabbitmq
# RABBITMQ_USER='guest_community_user'
# RABBITMQ_PASSWORD='password123'

# apt install $YQ rabbitmq-server
# rabbitmqctl add_user $RABBITMQ_USER $RABBITMQ_PASSWORD
# rabbitmqctl set_user_tags $RABBITMQ_USER administrator
# rabbitmqctl set_permissions -p / $RABBITMQ_USER ".*" ".*" ".*"
# systemctl restart rabbitmq-server

# install dependencies
VAGRANT_HOME='/home/vagrant'
VENV_PATH="$VAGRANT_HOME/venv"
python -m venv $VENV_PATH

ACTIVATE_ENV="$VENV_PATH/bin/activate"
source $ACTIVATE_ENV
printf "export DJANGO_SETTINGS_MODULE=root.settings.dev" >> $ACTIVATE_ENV

pip install --upgrade pip
# pip install -r /vagrant/src/requirements.txt
chown -R vagrant:vagrant $VENV_PATH


