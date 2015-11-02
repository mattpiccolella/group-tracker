#! /bin/bash

# Update apt-get
echo "Updating system"
sudo apt-get -qq update
sudo apt-get -yqqf upgrade

# Install Git
command -v git > /dev/null
if [ $? -ne 0 ]; then
  echo "Installing Git"
  sudo apt-get -yqq install git
fi

# Install Build Essentials
echo "Installing Build Essentials"
sudo apt-get -y install build-essential python-dev

# Install Pip
command -v pip > /dev/null
if [ $? -ne 0 ]; then
  echo "Installing Pip"
  sudo apt-get -yqq install python-pip
fi

# Install Ruby
sudo apt-get -y install ruby

# Install SASS
sudo gem install sass

# Install MongoDB
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
sudo apt-get install -y mongodb-org

mongod &
sudo pip install -r config/requirements.txt
