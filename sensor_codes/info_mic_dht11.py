#!/usr/bin/env python

import subprocess
import psutil
import time

def run_script(script_name):
    return subprocess.Popen(['python', script_name])

def measure_metrics(processes, duration):
    start_time = time.time()

    cpu_percent_list = []
    cpu_freq_list = []

    while time.time() - start_time < duration:
        for process in processes:
            if process.poll() is not None:
                continue

            cpu_percent = psutil.cpu_percent(0.1)
            cpu_freq = psutil.cpu_freq().current

            cpu_percent_list.append(cpu_percent)
            cpu_freq_list.append(cpu_freq)

        time.sleep(0.1)

    for process in processes:
        if process.poll() is None:
            process.terminate()
            process.wait()

    avg_cpu_percent = sum(cpu_percent_list) / len(cpu_percent_list)
    avg_cpu_freq = sum(cpu_freq_list) / len(cpu_freq_list)
    total_time = time.time() - start_time

    print(f"Average CPU Percent: {avg_cpu_percent}%")
    print(f"Average CPU Frequency: {avg_cpu_freq} MHz")
    print(f"Total Time: {total_time} seconds")

if __name__ == "__main__":
    # Run mic.py and dht11_new.py simultaneously
    mic_process = run_script('mic.py')
    dht_process = run_script('dht11_new.py')

    # Measure metrics for 22 seconds
    measure_metrics([mic_process, dht_process], duration=10)

