#!/bin/bash

# Ensure all rpms in rpmlist are present.
# Return 0 for all present, 1 for any missing
# Print status on stdout


RPMLIST=""
while read pkg
do
	echo $pkg | grep -q ^# && continue
	[ -z "$pkg" ] && continue
	RPMLIST="$RPMLIST $pkg"
done < ./rpmlist

rpm -q $RPMLIST 
exit $?
