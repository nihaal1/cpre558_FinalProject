#!/usr/bin/env python

import subprocess
import psutil
import time

def run_video(video_path):
    # Start VLC in the background to play the video
    vlc_process = subprocess.Popen(['vlc', video_path])

    # Measure the start time
    start_time = time.time()

    # Monitor CPU utilization and frequency
    cpu_percent_list = []
    cpu_freq_list = []
    while vlc_process.poll() is None:  # While VLC is running
        cpu_percent = psutil.cpu_percent(0.5)
        cpu_freq = psutil.cpu_freq().current
        cpu_percent_list.append(cpu_percent)
        cpu_freq_list.append(cpu_freq)
        time.sleep(0.5)

    # Measure the end time
    end_time = time.time()

    # Wait for VLC to finish
    vlc_process.wait()

    # Calculate average CPU percent and frequency
    avg_cpu_percent = sum(cpu_percent_list) / len(cpu_percent_list)
    avg_cpu_freq = sum(cpu_freq_list) / len(cpu_freq_list)

    # Calculate the total time the video ran
    total_time = end_time - start_time

    print(f"Average CPU Percent: {avg_cpu_percent}%")
    print(f"Average CPU Frequency: {avg_cpu_freq} MHz")
    print(f"Total Time to Run Video: {total_time} seconds")

if __name__ == "__main__":
    video_file_path = "video.mp4"  # Replace with the actual path to your video file
    run_video(video_file_path)


