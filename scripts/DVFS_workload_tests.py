import os
import time
import threading
import subprocess
import csv

# Constants
LOG_FILE = 'cpu_metrics_log.csv'
THREAD_COUNT = 4  # Adjust based on CPU cores

# Function to generate CPU load
def cpu_intensive_task(duration, intensity):
    end_time = time.time() + duration
    while time.time() < end_time:
        [x**2 for x in range(intensity)]

# Function to change CPU governor
def change_governor(governor, frequency=None):
    os.system(f'echo {governor} | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor')
    if frequency:
        os.system(f'echo {frequency} | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_setspeed')

# Function to get current CPU frequency
def get_current_frequency():
    return subprocess.getoutput('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')

# Function to get CPU temperature
def get_cpu_temperature():
    return subprocess.getoutput('vcgencmd measure_temp').split('=')[1].split("'")[0]

# Function to log metrics
def log_metrics(governor, frequency, temperature):
    with open(LOG_FILE, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([time.time(), governor, frequency, temperature])

# Main workload execution
def run_workload(duration, intensity, governor, frequency=None):
    threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=cpu_intensive_task, args=(duration, intensity))
        t.start()
        threads.append(t)

    change_governor(governor, frequency)

    for t in threads:
        t.join()

    # Log metrics after workload
    current_freq = get_current_frequency()
    temp = get_cpu_temperature()
    log_metrics(governor, current_freq, temp)

# Main
if __name__ == "__main__":
    # Setup log file
    with open(LOG_FILE, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Governor', 'Frequency', 'Temperature'])

    # Example usage: Run a workload for 60 seconds with high intensity
    # under the 'performance' governor
    run_workload(300, 10000, 'ondemand')
    # Add more scenarios as needed
