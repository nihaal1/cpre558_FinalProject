#!/usr/bin/env python
import subprocess
import os
import psutil
import threading
import time

def run_script(script_name):
    subprocess.Popen(["python", script_name])

def monitor_cpu(dijkstra_process, matrix_process):
    while dijkstra_process.poll() is None or matrix_process.poll() is None:
        cpu_percentage = psutil.cpu_percent(0.5)
        cpu_frequency = psutil.cpu_freq().current
        print(f"{cpu_percentage}, {cpu_frequency}")
        # You can add additional logic or logging here if needed
        # For example, you might want to log the metrics to a file
        time.sleep(1)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    # Run dijkstraIntensive.py in the background
    dijkstra_process = subprocess.Popen(["python", "dijkstraIntensive.py"])

    # Run matrixMul.py in the background
    matrix_process = subprocess.Popen(["python", "matrixMul.py"])

    # Start monitoring CPU in a separate thread
    monitor_thread = threading.Thread(target=monitor_cpu, args=(dijkstra_process, matrix_process))
    monitor_thread.start()

    # Wait for both processes to finish
    dijkstra_process.wait()
    matrix_process.wait()

    # Wait for the monitoring thread to finish
    monitor_thread.join()

