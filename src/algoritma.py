"""
ANALISIS KOMPLEKSITAS ALGORITMA
Implementasi lengkap:
- Search: Linear Search, Binary Search
- Sort: Bubble Sort, Insertion Sort, Merge Sort
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


def merge_sort(arr: List[int]) -> Tuple[List[int], int]:
    """Merge Sort - O(n log n)"""
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
    Bandingkan performa Bubble, Insertion, dan Merge Sort
    """
    print("\n" + "=" * 70)
    print(f"SORTING ALGORITHMS COMPARISON (Array Size: {arr_size})")
    print("=" * 70)
    
    results = {
        'bubble': {'comparisons': [], 'times': []},
        'insertion': {'comparisons': [], 'times': []},
        'merge': {'comparisons': [], 'times': []}
    }
    
    for test_num in range(num_tests):
        arr = [random.randint(1, 1000) for _ in range(arr_size)]
        
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps, _ = bubble_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['bubble']['comparisons'].append(comps)
        results['bubble']['times'].append(elapsed * 1000)
        
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps, _ = insertion_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['insertion']['comparisons'].append(comps)
        results['insertion']['times'].append(elapsed * 1000)
        
        test_arr = arr.copy()
        start = time.perf_counter()
        _, comps = merge_sort(test_arr)
        elapsed = time.perf_counter() - start
        results['merge']['comparisons'].append(comps)
        results['merge']['times'].append(elapsed * 1000)
    
    for algo in ['bubble', 'insertion', 'merge']:
        avg_comps = sum(results[algo]['comparisons']) / num_tests
        avg_time = sum(results[algo]['times']) / num_tests
        
        complexity = {
            'bubble': 'O(n²)',
            'insertion': 'O(n²)',
            'merge': 'O(n log n)'
        }
        
        print(f"\n{algo.capitalize()} Sort ({complexity[algo]}):")
        print(f"  Average Comparisons: {avg_comps:,.0f}")
        print(f"  Average Time: {avg_time:.2f} ms")
    
    # Calculate speedups relative to merge sort
    bubble_speedup = sum(results['bubble']['times']) / sum(results['merge']['times'])
    insertion_speedup = sum(results['insertion']['times']) / sum(results['merge']['times'])
    
    print(f"\nSpeedup (Merge Sort vs others):")
    print(f"  vs Bubble: {bubble_speedup:.2f}x faster")
    print(f"  vs Insertion: {insertion_speedup:.2f}x faster")
