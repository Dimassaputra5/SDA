import numpy as np

def MergeSort(A, m, B, n):
    """Merge 2 sorted arrays - O(m + n)
    
    Args:
        A: Array 1 (sorted)
        m: Size array 1
        B: Array 2 (sorted)
        n: Size array 2
    """
    result = []
    i = j = 0
    while i < m and j < n:
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    result.extend(A[i:m])
    result.extend(B[j:n])
    return result


def gen_merge_data(n):
    """Generate data untuk merge sorted arrays
    Kedua array punya ukuran yang sama (n)
    """
    arr1 = np.sort(np.random.rand(int(n)))
    arr2 = np.sort(np.random.rand(int(n)))
    return (arr1, int(n), arr2, int(n))