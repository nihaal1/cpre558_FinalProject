#!/usr/bin/env python

#!/usr/bin/env python
import subprocess
import psutil
import threading
import time

def run_script(script_name):
    subprocess.Popen(["python", script_name])

def monitor_cpu(dijkstra_process, cpu_percent_list, cpu_freq_list):
    while dijkstra_process.poll() is None:
        cpu_percent = psutil.cpu_percent(0.1)
        cpu_freq = psutil.cpu_freq().current

        cpu_percent_list.append(cpu_percent)
        cpu_freq_list.append(cpu_freq)

        print(f"Current CPU Percent: {cpu_percent}% | Current CPU Frequency: {cpu_freq} MHz")
        time.sleep(0.1)  # Adjust the sleep duration as needed

def main():
    # Run dijkstraIntensive.py in the background
    dijkstra_process = subprocess.Popen(["python", "matrixMul.py"])

    # Lists to store CPU metrics
    cpu_percent_list = []
    cpu_freq_list = []

    # Start monitoring CPU in a separate thread
    monitor_thread = threading.Thread(target=monitor_cpu, args=(dijkstra_process, cpu_percent_list, cpu_freq_list))
    monitor_thread.start()

    # Measure the start time
    start_time = time.time()

    # Wait for dijkstraIntensive.py to finish
    dijkstra_process.wait()

    # Measure the end time
    end_time = time.time()

    # Wait for the monitoring thread to finish
    monitor_thread.join()

    # Calculate average CPU percent and frequency
    avg_cpu_percent = sum(cpu_percent_list) / len(cpu_percent_list)
    avg_cpu_freq = sum(cpu_freq_list) / len(cpu_freq_list)

    # Calculate the total time taken
    total_time = end_time - start_time

    print(f"\nAverage CPU Percent: {avg_cpu_percent}%")
    print(f"Average CPU Frequency: {avg_cpu_freq} MHz")
    print(f"Total Time: {total_time} seconds")

if __name__ == "__main__":
    main()

