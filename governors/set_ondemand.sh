#!/bin/bash

echo ondemand | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
