"""
DATASET GENERATOR & COMPREHENSIVE TESTING

Script ini akan:
1. Generate datasets dalam berbagai ukuran
2. Test 7 algoritma (Linear, Binary, Bubble, Selection, Insertion, Merge, Quick)
3. Export hasil ke CSV
4. Siap untuk visualisasi
"""

import time
import random
import csv
from typing import List, Tuple
from algoritma import (
    linear_search,
    binary_search,
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

def generate_all_datasets():
    """Generate semua dataset yang diperlukan"""
    
    print("="*80)
    print("GENERATING DATASETS")
    print("="*80)
    
    datasets = {
        'search': {},
        'sorting_random': {},
        'sorting_sorted': {},
        'sorting_reverse': {}
    }
    
    # Dataset untuk search (bisa lebih besar)
    search_sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 2000000]
    
    print("\n1. Generating SEARCH datasets...")
    for size in search_sizes:
        print(f"   - Size {size:>8,}: ", end="")
        # Sorted array untuk binary search
        arr = sorted([random.randint(1, size * 10) for _ in range(size)])
        datasets['search'][size] = arr
        print("berhasil")
    
    # Dataset untuk sorting
    sorting_sizes = [100, 500, 1000, 2000, 5000, 10000, 20000]
    
    print("\n2. Generating SORTING datasets (Random)...")
    for size in sorting_sizes:
        print(f"   - Size {size:>8,}: ", end="")
        arr = [random.randint(1, 1000) for _ in range(size)]
        datasets['sorting_random'][size] = arr
        print("berhasil")
    
    print("\n3. Generating SORTING datasets (Already Sorted)...")
    for size in sorting_sizes:
        print(f"   - Size {size:>8,}: ", end="")
        arr = list(range(1, size + 1))
        datasets['sorting_sorted'][size] = arr
        print("berhasil")
    
    print("\n4. Generating SORTING datasets (Reverse Sorted)...")
    for size in sorting_sizes:
        print(f"   - Size {size:>8,}: ", end="")
        arr = list(range(size, 0, -1))
        datasets['sorting_reverse'][size] = arr
        print("berhasil")
    
    print("\n   All datasets generated!")
    return datasets


# ============================================================
# TESTING & CSV EXPORT
# ============================================================

def test_search_algorithms(datasets):
    """Test search algorithms dan export ke CSV"""
    
    print("\n" + "="*80)
    print("TESTING SEARCH ALGORITHMS")
    print("="*80)
    
    results = []
    
    for size, arr in datasets['search'].items():
        print(f"\nTesting n = {size:,}")
        
        # Target di posisi ~90%
        target = arr[int(size * 0.9)]
        
        # Linear Search
        start = time.perf_counter()
        idx, l_comps = linear_search(arr, target)
        l_time = time.perf_counter() - start
        
        # Binary Search
        start = time.perf_counter()
        idx, b_comps = binary_search(arr, target)
        b_time = time.perf_counter() - start
        
        results.append({
            'size': size,
            'linear_comps': l_comps,
            'linear_time': l_time,
            'binary_comps': b_comps,
            'binary_time': b_time
        })
        
        print(f"  Linear:  {l_comps:>8,} comps, {l_time:.6f} sec")
        print(f"  Binary:  {b_comps:>8,} comps, {b_time:.6f} sec")
        print(f"  Speedup: {l_time/b_time:>8.1f}x")
    
    # Export to CSV
    with open('results_search.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Input Size', 'Linear Comparisons', 'Linear Time (sec)', 
                        'Binary Comparisons', 'Binary Time (sec)', 'Speedup'])
        
        for r in results:
            writer.writerow([
                r['size'],
                r['linear_comps'],
                f"{r['linear_time']:.6f}",
                r['binary_comps'],
                f"{r['binary_time']:.6f}",
                f"{r['linear_time']/r['binary_time']:.2f}"
            ])
    
    print("\n Results exported to: results_search.csv")
    return results


def test_sorting_algorithms(datasets, dataset_type):
    """Test sorting algorithms untuk dataset type tertentu"""
    
    print(f"\n" + "="*80)
    print(f"TESTING SORTING ALGORITHMS - {dataset_type.upper().replace('_', ' ')}")
    print("="*80)
    
    results = []
    
    for size, base_arr in datasets[dataset_type].items():
        print(f"\nTesting n = {size:,}")
        
        result = {'size': size}
        
        # Bubble Sort
        arr = base_arr.copy()
        start = time.perf_counter()
        _, b_comps, b_swaps = bubble_sort(arr)
        b_time = time.perf_counter() - start
        result['bubble_comps'] = b_comps
        result['bubble_time'] = b_time
        print(f"  Bubble:    {b_comps:>10,} comps, {b_time:>8.4f} sec")
        
        # Selection Sort
        arr = base_arr.copy()
        start = time.perf_counter()
        _, s_comps, s_swaps = selection_sort(arr)
        s_time = time.perf_counter() - start
        result['selection_comps'] = s_comps
        result['selection_time'] = s_time
        print(f"  Selection: {s_comps:>10,} comps, {s_time:>8.4f} sec")
        
        # Insertion Sort
        arr = base_arr.copy()
        start = time.perf_counter()
        _, i_comps, i_shifts = insertion_sort(arr)
        i_time = time.perf_counter() - start
        result['insertion_comps'] = i_comps
        result['insertion_time'] = i_time
        print(f"  Insertion: {i_comps:>10,} comps, {i_time:>8.4f} sec")
        
        # Merge Sort
        arr = base_arr.copy()
        start = time.perf_counter()
        _, m_comps = merge_sort(arr)
        m_time = time.perf_counter() - start
        result['merge_comps'] = m_comps
        result['merge_time'] = m_time
        print(f"  Merge:     {m_comps:>10,} comps, {m_time:>8.4f} sec")
        
        # Quick Sort
        arr = base_arr.copy()
        start = time.perf_counter()
        _, q_comps, q_swaps = quick_sort(arr)
        q_time = time.perf_counter() - start
        result['quick_comps'] = q_comps
        result['quick_time'] = q_time
        print(f"  Quick:     {q_comps:>10,} comps, {q_time:>8.4f} sec")
        
        results.append(result)
    
    # Export to CSV
    filename = f'results_sorting_{dataset_type}.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Input Size', 
                        'Bubble Comparisons', 'Bubble Time (sec)',
                        'Selection Comparisons', 'Selection Time (sec)',
                        'Insertion Comparisons', 'Insertion Time (sec)',
                        'Merge Comparisons', 'Merge Time (sec)',
                        'Quick Comparisons', 'Quick Time (sec)'])
        
        for r in results:
            writer.writerow([
                r['size'],
                r['bubble_comps'],
                f"{r['bubble_time']:.4f}",
                r['selection_comps'],
                f"{r['selection_time']:.4f}",
                r['insertion_comps'],
                f"{r['insertion_time']:.4f}",
                r['merge_comps'],
                f"{r['merge_time']:.4f}",
                r['quick_comps'],
                f"{r['quick_time']:.4f}"
            ])
    
    print(f"\n Results exported to: {filename}")
    return results


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    # Generate all datasets
    print("\nStep 1: Generating datasets...")
    datasets = generate_all_datasets()
    
    # Test search algorithms
    print("\nStep 2: Testing search algorithms...")
    search_results = test_search_algorithms(datasets)
    
    # Test sorting algorithms - Random
    print("\nStep 3: Testing sorting algorithms (Random data)...")
    sorting_random = test_sorting_algorithms(datasets, 'sorting_random')
    
    # Test sorting algorithms - Sorted
    print("\nStep 4: Testing sorting algorithms (Already sorted)...")
    sorting_sorted = test_sorting_algorithms(datasets, 'sorting_sorted')
    
    # Test sorting algorithms - Reverse
    print("\nStep 5: Testing sorting algorithms (Reverse sorted)...")
    sorting_reverse = test_sorting_algorithms(datasets, 'sorting_reverse')
    
    # Final summary
    print("\n" + "="*80)
    print("TESTING COMPLETED!")
    print("="*80)
    print("\nGenerated CSV files:")
    print("  1. results_search.csv")
    print("  2. results_sorting_sorting_random.csv")
    print("  3. results_sorting_sorting_sorted.csv")
    print("  4. results_sorting_sorting_reverse.csv")
    print("\nUse visualisasi_grafik.py untuk membuat grafik dari data ini!")
    print("="*80)
