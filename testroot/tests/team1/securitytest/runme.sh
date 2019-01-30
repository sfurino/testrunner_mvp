#!/bin/bash
# Because all hackers will leave this file, determine
# if your system is hacked, and fail if it is.

[ -f /etc/hacked_by ] && exit 1 || exit 0
