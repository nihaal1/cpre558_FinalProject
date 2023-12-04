#!/usr/bin/env python

import numpy as np
import time

def cpu_intensive_matrix_multiply(matrix_a, matrix_b):
    result = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))

    for i in range(matrix_a.shape[0]):
        for j in range(matrix_b.shape[1]):
            for k in range(matrix_b.shape[0]):
                # Simulate CPU-intensive task
                result[i, j] += matrix_a[i, k] * matrix_b[k, j]
                _ = result[i, j]  # Just to make sure the result is used

    return result

if __name__ == "__main__":
    # Creating two random matrices for multiplication
    matrix_size = 100
    matrix_a = np.random.rand(matrix_size, matrix_size)
    matrix_b = np.random.rand(matrix_size, matrix_size)

    start_time = time.time()
    result_matrix = cpu_intensive_matrix_multiply(matrix_a, matrix_b)
    end_time = time.time()

    print(f"Matrix multiplication completed in {end_time - start_time:.4f} seconds.")

