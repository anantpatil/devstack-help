#!/usr/bin/env bash

# most of the systems have nopasswdlogin as a group; mostly ubuntu based
# ones; just add the user to the group
sudo gpasswd -a stack nopasswdlogin
