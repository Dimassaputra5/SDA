"""
ANALISIS KOMPLEKSITAS ALGORITMA
Implementasi lengkap:
- Search: Linear Search, Binary Search
- Sort Simple: Bubble Sort, Selection Sort, Insertion Sort
- Sort Advanced: Merge Sort, Quick Sort
"""
import time
import random
from typing import List, Tuple

def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Linear Search - O(n)"""
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Binary Search - O(log n)"""
    comparisons = 0
    left, right = 0, len(arr) - 1
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons


def bubble_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    """Bubble Sort - O(n²)"""
    n = len(arr)
    comparisons, swaps = 0, 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, comparisons, swaps


def selection_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    """Selection Sort - O(n²)"""
    n = len(arr)
    comparisons, swaps = 0, 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return arr, comparisons, swaps


def insertion_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    """Insertion Sort - O(n²)"""
    n = len(arr)
    comparisons, shifts = 0, 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
    
    return arr, comparisons, shifts
    """Merge Sort - O(n log n)"""


def merge_sort(arr: List[int]) -> Tuple[List[int], int]:
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_comps = merge_sort(arr[:mid])
    right, right_comps = merge_sort(arr[mid:])
    merged, merge_comps = merge(left, right)
    return merged, left_comps + right_comps + merge_comps


def merge(left: List[int], right: List[int]) -> Tuple[List[int], int]:
    """Helper untuk merge sort"""
    result = []
    comparisons = 0
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparisons


def quick_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    if len(arr) <= 1:
        return arr, 0, 0
    comparisons, swaps = [0], [0]  # Use list untuk pass by reference
    _quick_sort_helper(arr, 0, len(arr) - 1, comparisons, swaps)
    return arr, comparisons[0], swaps[0]


def _quick_sort_helper(arr: List[int], low: int, high: int, 
                       comparisons: List[int], swaps: List[int]) -> None:
    while low < high:
        if high - low < 10:
            _insertion_sort_range(arr, low, high, comparisons, swaps)
            break
        pivot_idx = _partition(arr, low, high, comparisons, swaps)
        if pivot_idx - low < high - pivot_idx:
            _quick_sort_helper(arr, low, pivot_idx - 1, comparisons, swaps)
            low = pivot_idx + 1
        else:
            _quick_sort_helper(arr, pivot_idx + 1, high, comparisons, swaps)
            high = pivot_idx - 1


def _insertion_sort_range(arr: List[int], low: int, high: int,
                          comparisons: List[int], swaps: List[int]) -> None:
    """Insertion sort untuk subarray kecil"""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        
        while j >= low and arr[j] > key:
            comparisons[0] += 1
            arr[j + 1] = arr[j]
            swaps[0] += 1
            j -= 1
        
        if j >= low:
            comparisons[0] += 1
        
        arr[j + 1] = key


def _median_of_three(arr: List[int], low: int, high: int,
                     comparisons: List[int], swaps: List[int]) -> int:
    """Pilih pivot menggunakan median-of-three untuk menghindari worst case"""
    mid = (low + high) // 2
    
    # Sort low, mid, high
    comparisons[0] += 1
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
        swaps[0] += 1
    
    comparisons[0] += 1
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
        swaps[0] += 1
        
        comparisons[0] += 1
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
            swaps[0] += 1
    
    # Move median to high-1 position
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    swaps[0] += 1
    
    return high - 1


def _partition(arr: List[int], low: int, high: int, 
               comparisons: List[int], swaps: List[int]) -> int:
    """Partition function dengan median-of-three pivot"""
    # Use median-of-three for better pivot selection
    if high - low >= 3:
        pivot_idx = _median_of_three(arr, low, high, comparisons, swaps)
        pivot = arr[pivot_idx]
    else:
        pivot = arr[high]
    
    i = low - 1
    
    for j in range(low, high):
        comparisons[0] += 1
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
    
    if i + 1 != high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
    
    return i + 1


def compare_search_algorithms(arr_size: int = 1000, num_tests: int = 5):
    """
    Bandingkan performa Linear Search vs Binary Search
    """
    print("=" * 70)
    print(f"SEARCH ALGORITHMS COMPARISON (Array Size: {arr_size})")
    print("=" * 70)
    
    results = {
        'linear': {'comparisons': [], 'times': []},
        'binary': {'comparisons': [], 'times': []}
    }
    
    for test_num in range(num_tests):
        arr = sorted([random.randint(1, arr_size * 10) for _ in range(arr_size)])
        
        target = arr[int(arr_size * 0.9)]
        
        start = time.perf_counter()
        idx, comps = linear_search(arr, target)
        elapsed = time.perf_counter() - start
        results['linear']['comparisons'].append(comps)
        results['linear']['times'].append(elapsed * 1000)  # Convert to ms
        
        start = time.perf_counter()
        idx, comps = binary_search(arr, target)
        elapsed = time.perf_counter() - start
        results['binary']['comparisons'].append(comps)
        results['binary']['times'].append(elapsed * 1000)
    
    avg_linear_comps = sum(results['linear']['comparisons']) / num_tests
    avg_linear_time = sum(results['linear']['times']) / num_tests
    avg_binary_comps = sum(results['binary']['comparisons']) / num_tests
    avg_binary_time = sum(results['binary']['times']) / num_tests
    
    print(f"\nLinear Search (O(n)):")
    print(f"  Average Comparisons: {avg_linear_comps:.0f}")
    print(f"  Average Time: {avg_linear_time:.4f} ms")
    
    print(f"\nBinary Search (O(log n)):")
    print(f"  Average Comparisons: {avg_binary_comps:.0f}")
    print(f"  Average Time: {avg_binary_time:.4f} ms")
    
    print(f"\nSpeedup:")
    print(f"  Comparisons: {avg_linear_comps / avg_binary_comps:.2f}x fewer")
    print(f"  Time: {avg_linear_time / avg_binary_time:.2f}x faster")


def compare_sorting_algorithms(arr_size: int = 1000, num_tests: int = 3):
    """
    Bandingkan performa semua sorting algorithms
    """
    print("\n" + "=" * 70)
    print(f"SORTING ALGORITHMS COMPARISON (Array Size: {arr_size})")
    print("=" * 70)
    
    results = {
        'bubble': {'comparisons': [], 'times': []},
        'selection': {'comparisons': [], 'times': []},
        'insertion': {'comparisons': [], 'times': []},
        'merge': {'comparisons': [], 'times': []},
        'quick': {'comparisons': [], 'times': []}
    }
    
    for test_num in range(num_tests):
        arr = [random.randint(1, 1000) for _ in range(arr_size)]
        
        # Bubble Sort
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps, _ = bubble_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['bubble']['comparisons'].append(comps)
        results['bubble']['times'].append(elapsed * 1000)
        
        # Selection Sort
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps, _ = selection_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['selection']['comparisons'].append(comps)
        results['selection']['times'].append(elapsed * 1000)
        
        # Insertion Sort
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps, _ = insertion_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['insertion']['comparisons'].append(comps)
        results['insertion']['times'].append(elapsed * 1000)
        
        # Merge Sort
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps = merge_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['merge']['comparisons'].append(comps)
        results['merge']['times'].append(elapsed * 1000)
        
        # Quick Sort
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps, _ = quick_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['quick']['comparisons'].append(comps)
        results['quick']['times'].append(elapsed * 1000)
    
    complexity = {
        'bubble': 'O(n²)',
        'selection': 'O(n²)',
        'insertion': 'O(n²)',
        'merge': 'O(n log n)',
        'quick': 'O(n log n) avg'
    }
    
    for algo in ['bubble', 'selection', 'insertion', 'merge', 'quick']:
        avg_comps = sum(results[algo]['comparisons']) / num_tests
        avg_time = sum(results[algo]['times']) / num_tests
        
        print(f"\n{algo.capitalize()} Sort ({complexity[algo]}):")
        print(f"  Average Comparisons: {avg_comps:,.0f}")
        print(f"  Average Time: {avg_time:.2f} ms")
    
    # Calculate speedups relative to merge sort
    merge_avg_time = sum(results['merge']['times']) / num_tests
    
    print(f"\nSpeedup (vs Merge Sort):")
    for algo in ['bubble', 'selection', 'insertion', 'quick']:
        avg_time = sum(results[algo]['times']) / num_tests
        speedup = avg_time / merge_avg_time
        if speedup > 1:
            print(f"  {algo.capitalize()}: {speedup:.2f}x slower")
        else:
            print(f"  {algo.capitalize()}: {1/speedup:.2f}x faster")
