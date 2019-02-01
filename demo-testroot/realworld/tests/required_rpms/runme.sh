#!/bin/bash

# Ensure all rpms in rpmlist are present.
# Return 0 for all present, 1 for any missing
# Print status on stdout


EXIT=0
while read pkg
do
	echo $pkg | grep -q ^# && continue
	[ -z "$pkg" ] && continue
	rpm -q $pkg || EXIT=1
done < ./rpmlist

exit $EXIT
