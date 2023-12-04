#!/usr/bin/env python
import subprocess
import os

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    # Run dijkstraIntensive.py in the background
    dijkstra_process = subprocess.Popen(["python", "dijkstraIntensive.py"])

    # Run matrixMul.py in the background
    matrix_process = subprocess.Popen(["python", "matrixMul.py"])

    # Wait for both processes to finish
    dijkstra_process.wait()
    matrix_process.wait()

