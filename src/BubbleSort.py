import numpy as np
def BubbleSort(A, n):
    """Bubble Sort - O(n^2)
    
    Args:
        A: Array
        n: Ukuran array
    """
    arr = A.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def gen_bubblesort_data(n):
    """Generate data untuk bubble sort
    Return: (array, array_size)
    """
    arr = np.random.rand(int(n))
    return (arr, int(n))