#!/usr/bin/env python
import psutil

while (1):
    print(f"{psutil.cpu_percent(0.2)}%, {psutil.cpu_freq().current}MHz")
