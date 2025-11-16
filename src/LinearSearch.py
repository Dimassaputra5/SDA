import numpy as np

def LinearSearch(A, n, T):
    for i in range(n):
        if A[i] == T:
            return i    
    return -1

def gen_linearsearch_data(n):
    """Generate data untuk linear search
    Return: (array, array_size, target_value)
    """
    arr = np.random.randint(0, 100000, size=int(n))
    target = arr[np.random.randint(0, len(arr))]
    return (arr, int(n), target)