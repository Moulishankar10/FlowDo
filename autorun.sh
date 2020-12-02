#!/bin/sh

clear

echo "FlowDo Autorun Script"
echo ""
echo "Checking for Python Installation..."

if which python3 >/dev/null;
then
  echo "Python 3 is already installed."
else
  echo "Python isn't found."
  echo "Installing Python 3..."
  sudo apt install python3 -y
  echo "Successfully installed Python 3."
fi

if which pip3 >/dev/null;
then
  echo "pip3 is already installed."
else
  echo "pip3 isn't found."
  echo "Installing pip3..."
  sudo apt install python3-pip -y
  echo "Successfully installed pip3."
fi

echo "Checking the Dependencies...."
pip3 install numpy pandas datetime matplotlib

echo "Now, You are all set!"
