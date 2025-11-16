import numpy as np

def InsertionSort(A, n):
    arr = A.copy()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def gen_insertionsort_data(n):
    """Generate data untuk insertion sort"""
    arr = np.random.rand(int(n))
    return (arr, int(n))
