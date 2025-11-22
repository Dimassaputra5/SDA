"""
COMPREHENSIVE COMPARISON & ANALYSIS
Export semua data komparasi ke satu CSV lengkap

CSV Output:
1. comparison_all_algorithms.csv - Semua algoritma dalam satu file
2. comparison_summary.csv - Ringkasan performa
3. comparison_speedup.csv - Analisis speedup
"""

import csv
import pandas as pd
from pathlib import Path


def create_comprehensive_comparison():
    """Buat CSV komparasi lengkap dari semua hasil testing"""
    
    print("="*80)
    print("CREATING COMPREHENSIVE COMPARISON CSV")
    print("="*80)
    
    # Check if result files exist
    required_files = [
        'results_search.csv',
        'results_sorting_sorting_random.csv',
        'results_sorting_sorting_sorted.csv',
        'results_sorting_sorting_reverse.csv'
    ]
    
    missing_files = [f for f in required_files if not Path(f).exists()]
    if missing_files:
        print("\nError: Missing required files:")
        for f in missing_files:
            print(f"  - {f}")
        print("\nPlease run dataset-generator-fixed.py first!")
        return
    
    # Read all data
    df_search = pd.read_csv('results_search.csv')
    df_random = pd.read_csv('results_sorting_sorting_random.csv')
    df_sorted = pd.read_csv('results_sorting_sorting_sorted.csv')
    df_reverse = pd.read_csv('results_sorting_sorting_reverse.csv')
    
    # ============================================================
    # CSV 1: ALL ALGORITHMS COMPARISON (COMPREHENSIVE)
    # ============================================================
    
    print("\n1. Creating comparison_all_algorithms.csv...")
    
    with open('comparison_all_algorithms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Algorithm', 'Data Type', 'Input Size (n)',
            'Comparisons', 'Time (seconds)', 
            'Complexity Class', 'Notes'
        ])
        
        # Search algorithms
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            
            # Linear Search
            writer.writerow([
                'Linear Search', 'Sorted', size,
                int(row['Linear Comparisons']),
                float(row['Linear Time (sec)']),
                'O(n)', 'Target at 90% position'
            ])
            
            # Binary Search
            writer.writerow([
                'Binary Search', 'Sorted', size,
                int(row['Binary Comparisons']),
                float(row['Binary Time (sec)']),
                'O(log n)', 'Target at 90% position'
            ])
        
        # Sorting algorithms - Random
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            
            writer.writerow([
                'Bubble Sort', 'Random', size,
                int(row['Bubble Comparisons']),
                float(row['Bubble Time (sec)']),
                'O(n^2)', 'Average case'
            ])
            
            writer.writerow([
                'Insertion Sort', 'Random', size,
                int(row['Insertion Comparisons']),
                float(row['Insertion Time (sec)']),
                'O(n^2)', 'Average case'
            ])
            
            writer.writerow([
                'Merge Sort', 'Random', size,
                int(row['Merge Comparisons']),
                float(row['Merge Time (sec)']),
                'O(n log n)', 'Consistent performance'
            ])
        
        # Sorting algorithms - Best case (Sorted)
        for _, row in df_sorted.iterrows():
            size = int(row['Input Size'])
            
            writer.writerow([
                'Bubble Sort', 'Already Sorted', size,
                int(row['Bubble Comparisons']),
                float(row['Bubble Time (sec)']),
                'O(n)', 'Best case with early exit'
            ])
            
            writer.writerow([
                'Insertion Sort', 'Already Sorted', size,
                int(row['Insertion Comparisons']),
                float(row['Insertion Time (sec)']),
                'O(n)', 'Best case - no shifts needed'
            ])
            
            writer.writerow([
                'Merge Sort', 'Already Sorted', size,
                int(row['Merge Comparisons']),
                float(row['Merge Time (sec)']),
                'O(n log n)', 'Consistent - unaffected by input'
            ])
        
        # Sorting algorithms - Worst case (Reverse)
        for _, row in df_reverse.iterrows():
            size = int(row['Input Size'])
            
            writer.writerow([
                'Bubble Sort', 'Reverse Sorted', size,
                int(row['Bubble Comparisons']),
                float(row['Bubble Time (sec)']),
                'O(n^2)', 'Worst case - max swaps'
            ])
            
            writer.writerow([
                'Insertion Sort', 'Reverse Sorted', size,
                int(row['Insertion Comparisons']),
                float(row['Insertion Time (sec)']),
                'O(n^2)', 'Worst case - max shifts'
            ])
            
            writer.writerow([
                'Merge Sort', 'Reverse Sorted', size,
                int(row['Merge Comparisons']),
                float(row['Merge Time (sec)']),
                'O(n log n)', 'Consistent - unaffected by input'
            ])
    
    print("   Created: comparison_all_algorithms.csv")
    
    # ============================================================
    # CSV 2: SUMMARY COMPARISON (Best performers at each size)
    # ============================================================
    
    print("\n2. Creating comparison_summary.csv...")
    
    with open('comparison_summary.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Category', 'Input Size (n)',
            'Fastest Algorithm', 'Time (sec)',
            'Slowest Algorithm', 'Time (sec)',
            'Speed Difference (x)'
        ])
        
        # Search comparison
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            linear_time = float(row['Linear Time (sec)'])
            binary_time = float(row['Binary Time (sec)'])
            speedup = linear_time / binary_time
            
            writer.writerow([
                'Search', size,
                'Binary Search', f"{binary_time:.6f}",
                'Linear Search', f"{linear_time:.6f}",
                f"{speedup:.2f}"
            ])
        
        # Sorting comparison - Random data
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            bubble_time = float(row['Bubble Time (sec)'])
            insertion_time = float(row['Insertion Time (sec)'])
            merge_time = float(row['Merge Time (sec)'])
            
            # Find fastest and slowest
            times = {
                'Bubble Sort': bubble_time,
                'Insertion Sort': insertion_time,
                'Merge Sort': merge_time
            }
            
            fastest = min(times, key=times.get)
            slowest = max(times, key=times.get)
            speedup = times[slowest] / times[fastest]
            
            writer.writerow([
                'Sorting (Random)', size,
                fastest, f"{times[fastest]:.6f}",
                slowest, f"{times[slowest]:.6f}",
                f"{speedup:.2f}"
            ])
    
    print("   Created: comparison_summary.csv")
    
    # ============================================================
    # CSV 3: SPEEDUP ANALYSIS
    # ============================================================
    
    print("\n3. Creating comparison_speedup.csv...")
    
    with open('comparison_speedup.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Comparison', 'Input Size (n)',
            'Algorithm A', 'Algorithm A Time',
            'Algorithm B', 'Algorithm B Time',
            'Speedup (A/B)', 'Comparison Reduction (%)'
        ])
        
        # Binary vs Linear Search
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            linear_comps = int(row['Linear Comparisons'])
            binary_comps = int(row['Binary Comparisons'])
            linear_time = float(row['Linear Time (sec)'])
            binary_time = float(row['Binary Time (sec)'])
            
            speedup = linear_time / binary_time
            comp_reduction = ((linear_comps - binary_comps) / linear_comps) * 100
            
            writer.writerow([
                'Search Algorithms', size,
                'Linear Search', f"{linear_time:.6f}",
                'Binary Search', f"{binary_time:.6f}",
                f"{speedup:.2f}", f"{comp_reduction:.2f}"
            ])
        
        # Merge vs Bubble Sort (Random)
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            bubble_comps = int(row['Bubble Comparisons'])
            merge_comps = int(row['Merge Comparisons'])
            bubble_time = float(row['Bubble Time (sec)'])
            merge_time = float(row['Merge Time (sec)'])
            
            speedup = bubble_time / merge_time
            comp_reduction = ((bubble_comps - merge_comps) / bubble_comps) * 100
            
            writer.writerow([
                'Sorting (Random)', size,
                'Bubble Sort', f"{bubble_time:.6f}",
                'Merge Sort', f"{merge_time:.6f}",
                f"{speedup:.2f}", f"{comp_reduction:.2f}"
            ])
        
        # Merge vs Insertion Sort (Random)
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            insertion_comps = int(row['Insertion Comparisons'])
            merge_comps = int(row['Merge Comparisons'])
            insertion_time = float(row['Insertion Time (sec)'])
            merge_time = float(row['Merge Time (sec)'])
            
            speedup = insertion_time / merge_time
            comp_reduction = ((insertion_comps - merge_comps) / insertion_comps) * 100
            
            writer.writerow([
                'Sorting (Random)', size,
                'Insertion Sort', f"{insertion_time:.6f}",
                'Merge Sort', f"{merge_time:.6f}",
                f"{speedup:.2f}", f"{comp_reduction:.2f}"
            ])
    
    print("   Created: comparison_speedup.csv")
    
    # ============================================================
    # CSV 4: GROWTH RATE ANALYSIS
    # ============================================================
    
    print("\n4. Creating comparison_growth_rate.csv...")
    
    with open('comparison_growth_rate.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Algorithm', 'Size 1', 'Comparisons 1', 
            'Size 2', 'Comparisons 2',
            'Size Growth (x)', 'Comparisons Growth (x)',
            'Theoretical Complexity', 'Matches Theory?'
        ])
        
        # Search algorithms growth
        for i in range(len(df_search) - 1):
            row1 = df_search.iloc[i]
            row2 = df_search.iloc[i + 1]
            
            size1 = int(row1['Input Size'])
            size2 = int(row2['Input Size'])
            size_growth = size2 / size1
            
            # Linear Search
            linear1 = int(row1['Linear Comparisons'])
            linear2 = int(row2['Linear Comparisons'])
            linear_growth = linear2 / linear1
            matches_linear = abs(linear_growth - size_growth) < 1.5
            
            writer.writerow([
                'Linear Search', size1, linear1, size2, linear2,
                f"{size_growth:.2f}", f"{linear_growth:.2f}",
                'O(n) - Linear', 'Yes' if matches_linear else 'Close'
            ])
            
            # Binary Search
            binary1 = int(row1['Binary Comparisons'])
            binary2 = int(row2['Binary Comparisons'])
            binary_growth = binary2 / binary1 if binary1 > 0 else 0
            
            # O(log n) should grow much slower than size
            matches_log = binary_growth < size_growth / 2
            
            writer.writerow([
                'Binary Search', size1, binary1, size2, binary2,
                f"{size_growth:.2f}", f"{binary_growth:.2f}",
                'O(log n) - Logarithmic', 'Yes' if matches_log else 'Close'
            ])
        
        # Sorting algorithms growth (Random data)
        for i in range(len(df_random) - 1):
            row1 = df_random.iloc[i]
            row2 = df_random.iloc[i + 1]
            
            size1 = int(row1['Input Size'])
            size2 = int(row2['Input Size'])
            size_growth = size2 / size1
            
            # Bubble Sort
            bubble1 = int(row1['Bubble Comparisons'])
            bubble2 = int(row2['Bubble Comparisons'])
            bubble_growth = bubble2 / bubble1
            # O(n²) growth should be ~size_growth²
            expected_n2 = size_growth ** 2
            matches_n2 = abs(bubble_growth - expected_n2) < expected_n2 * 0.3
            
            writer.writerow([
                'Bubble Sort', size1, bubble1, size2, bubble2,
                f"{size_growth:.2f}", f"{bubble_growth:.2f}",
                'O(n^2) - Quadratic', 'Yes' if matches_n2 else 'Close'
            ])
            
            # Merge Sort
            merge1 = int(row1['Merge Comparisons'])
            merge2 = int(row2['Merge Comparisons'])
            merge_growth = merge2 / merge1
            # O(n log n) should grow between O(n) and O(n²)
            matches_nlogn = size_growth < merge_growth < size_growth ** 2
            
            writer.writerow([
                'Merge Sort', size1, merge1, size2, merge2,
                f"{size_growth:.2f}", f"{merge_growth:.2f}",
                'O(n log n) - Linearithmic', 'Yes' if matches_nlogn else 'Close'
            ])
    
    print("   Created: comparison_growth_rate.csv")
    
    print("\n" + "="*80)
    print("COMPARISON CSV FILES COMPLETED!")
    print("="*80)
    print("\nGenerated files:")
    print("  1. comparison_all_algorithms.csv    - Semua data lengkap")
    print("  2. comparison_summary.csv            - Ringkasan best/worst")
    print("  3. comparison_speedup.csv            - Analisis speedup detail")
    print("  4. comparison_growth_rate.csv        - Verifikasi Big-O growth")
    print("\nSemua file siap untuk analisis dan presentasi!")
    print("="*80)


if __name__ == "__main__":
    print("\n" + "="*80)
    print("COMPREHENSIVE COMPARISON GENERATOR")
    print("Kelompok 2 - CSV Analysis")
    print("="*80)
    
    create_comprehensive_comparison()
