#!/bin/bash

echo conservative | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
