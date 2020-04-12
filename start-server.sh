#!/bin/bash
grep_output=$(sudo hciconfig -a | grep "UP RUNNING PSCAN ISCAN")

if $grep_output 
then
	echo "making device discoverable"
	sudo hciconfig hci0 piscan 
else
	echo "device already discoverable"
fi

echo "running main"
sudo python3 main.py
