#!/bin/sh

clear

echo "FlowDo Autorun Script"
echo " "


echo "Checking for pip3 installation ..."
if which pip3 >/dev/null;
then
  echo "pip3 is already installed."
else
  echo "pip3 isn't found."
  echo "Installing pip3 ..."
  sudo apt install python3-pip -y
  echo "Successfully installed pip3."
fi

echo "Checking the Dependencies...."
pip3 install numpy pandas datetime matplotlib

echo " "
echo "Now, You are all set!"
