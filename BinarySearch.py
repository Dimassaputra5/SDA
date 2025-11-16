import math as mt
import numpy as np

def BinarySearch(A, n, T):
    L = 0
    R = n -1
    while L <= R:
        m = L + mt.floor((R-L)/2)
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m -1
        else:
            return m
    return -1

def gen_binarysearch_data(n):
    """Generate (sorted_array, array_size, target_value)"""
    arr = np.sort(np.random.randint(0, 100000, size=int(n)))
    target = arr[np.random.randint(0, len(arr))]
    return (arr, int(n), target)  # Return sebagai TUPLE




