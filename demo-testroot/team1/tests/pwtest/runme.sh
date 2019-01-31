#!/bin/bash
# A test to see if you have a password file

[ -f /etc/passwd ] && exit 0 || exit 1
