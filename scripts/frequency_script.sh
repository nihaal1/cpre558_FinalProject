#!/bin/bash

while true; do
	cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
	sleep 0.5
done
