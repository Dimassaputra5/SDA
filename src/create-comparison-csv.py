"""
COMPREHENSIVE COMPARISON & ANALYSIS
Export semua data komparasi ke satu CSV lengkap

CSV Output:
1. comparison_all_algorithms.csv - Semua algoritma dalam satu file
2. comparison_summary.csv - Ringkasan performa
3. comparison_speedup.csv - Analisis speedup
4. comparison_growth_rate.csv - Verifikasi Big-O growth
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
        print("\nPlease run dataset-generator.py first!")
        return
    
    # Read all data
    df_search = pd.read_csv('results_search.csv')
    df_random = pd.read_csv('results_sorting_sorting_random.csv')
    df_sorted = pd.read_csv('results_sorting_sorting_sorted.csv')
    df_reverse = pd.read_csv('results_sorting_sorting_reverse.csv')
    
    # CSV 1: ALL ALGORITHMS COMPARISON
    print("\n1. Creating comparison_all_algorithms.csv...")
    with open('comparison_all_algorithms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Data Type', 'Input Size (n)', 'Comparisons', 'Time (seconds)', 'Complexity Class', 'Notes'])
        
        # Search algorithms
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Linear Search', 'Sorted', size, int(row['Linear Comparisons']), float(row['Linear Time (sec)']), 'O(n)', 'Target at 90%'])
            writer.writerow(['Binary Search', 'Sorted', size, int(row['Binary Comparisons']), float(row['Binary Time (sec)']), 'O(log n)', 'Target at 90%'])
        
        # Sorting algorithms - Random
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Bubble Sort', 'Random', size, int(row['Bubble Comparisons']), float(row['Bubble Time (sec)']), 'O(n^2)', 'Average case'])
            writer.writerow(['Selection Sort', 'Random', size, int(row['Selection Comparisons']), float(row['Selection Time (sec)']), 'O(n^2)', 'Average case'])
            writer.writerow(['Insertion Sort', 'Random', size, int(row['Insertion Comparisons']), float(row['Insertion Time (sec)']), 'O(n^2)', 'Average case'])
            writer.writerow(['Merge Sort', 'Random', size, int(row['Merge Comparisons']), float(row['Merge Time (sec)']), 'O(n log n)', 'Consistent'])
            writer.writerow(['Quick Sort', 'Random', size, int(row['Quick Comparisons']), float(row['Quick Time (sec)']), 'O(n log n)', 'Average case'])
        
        # Sorting algorithms - Best case (Sorted)
        for _, row in df_sorted.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Bubble Sort', 'Sorted', size, int(row['Bubble Comparisons']), float(row['Bubble Time (sec)']), 'O(n)', 'Best case'])
            writer.writerow(['Selection Sort', 'Sorted', size, int(row['Selection Comparisons']), float(row['Selection Time (sec)']), 'O(n^2)', 'No benefit'])
            writer.writerow(['Insertion Sort', 'Sorted', size, int(row['Insertion Comparisons']), float(row['Insertion Time (sec)']), 'O(n)', 'Best case'])
            writer.writerow(['Merge Sort', 'Sorted', size, int(row['Merge Comparisons']), float(row['Merge Time (sec)']), 'O(n log n)', 'Consistent'])
            writer.writerow(['Quick Sort', 'Sorted', size, int(row['Quick Comparisons']), float(row['Quick Time (sec)']), 'O(n log n)', 'Good case'])
        
        # Sorting algorithms - Worst case (Reverse)
        for _, row in df_reverse.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Bubble Sort', 'Reverse', size, int(row['Bubble Comparisons']), float(row['Bubble Time (sec)']), 'O(n^2)', 'Worst case'])
            writer.writerow(['Selection Sort', 'Reverse', size, int(row['Selection Comparisons']), float(row['Selection Time (sec)']), 'O(n^2)', 'Same as avg'])
            writer.writerow(['Insertion Sort', 'Reverse', size, int(row['Insertion Comparisons']), float(row['Insertion Time (sec)']), 'O(n^2)', 'Worst case'])
            writer.writerow(['Merge Sort', 'Reverse', size, int(row['Merge Comparisons']), float(row['Merge Time (sec)']), 'O(n log n)', 'Consistent'])
            writer.writerow(['Quick Sort', 'Reverse', size, int(row['Quick Comparisons']), float(row['Quick Time (sec)']), 'O(n^2)', 'Can be worst'])
    
    print("   Created: comparison_all_algorithms.csv")
    
    # CSV 2: SUMMARY COMPARISON
    print("\n2. Creating comparison_summary.csv...")
    with open('comparison_summary.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Category', 'Input Size (n)', 'Fastest Algorithm', 'Time (sec)', 'Slowest Algorithm', 'Time (sec)', 'Speed Difference (x)'])
        
        # Search comparison
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            linear_time = float(row['Linear Time (sec)'])
            binary_time = float(row['Binary Time (sec)'])
            speedup = linear_time / binary_time
            writer.writerow(['Search', size, 'Binary Search', f"{binary_time:.6f}", 'Linear Search', f"{linear_time:.6f}", f"{speedup:.2f}"])
        
        # Sorting comparison - Random data
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            times = {
                'Bubble Sort': float(row['Bubble Time (sec)']),
                'Selection Sort': float(row['Selection Time (sec)']),
                'Insertion Sort': float(row['Insertion Time (sec)']),
                'Merge Sort': float(row['Merge Time (sec)']),
                'Quick Sort': float(row['Quick Time (sec)'])
            }
            fastest = min(times, key=times.get)
            slowest = max(times, key=times.get)
            speedup = times[slowest] / times[fastest]
            writer.writerow(['Sorting (Random)', size, fastest, f"{times[fastest]:.6f}", slowest, f"{times[slowest]:.6f}", f"{speedup:.2f}"])
    
    print("   Created: comparison_summary.csv")
    
    # CSV 3: SPEEDUP ANALYSIS
    print("\n3. Creating comparison_speedup.csv...")
    with open('comparison_speedup.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Comparison', 'Input Size (n)', 'Algorithm A', 'Algorithm A Time', 'Algorithm B', 'Algorithm B Time', 'Speedup (A/B)', 'Comparison Reduction (%)'])
        
        # Binary vs Linear Search
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            linear_comps = int(row['Linear Comparisons'])
            binary_comps = int(row['Binary Comparisons'])
            linear_time = float(row['Linear Time (sec)'])
            binary_time = float(row['Binary Time (sec)'])
            speedup = linear_time / binary_time
            comp_reduction = ((linear_comps - binary_comps) / linear_comps) * 100
            writer.writerow(['Search Algorithms', size, 'Linear Search', f"{linear_time:.6f}", 'Binary Search', f"{binary_time:.6f}", f"{speedup:.2f}", f"{comp_reduction:.2f}"])
        
        # Quick vs Bubble Sort (Random)
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            bubble_comps = int(row['Bubble Comparisons'])
            quick_comps = int(row['Quick Comparisons'])
            bubble_time = float(row['Bubble Time (sec)'])
            quick_time = float(row['Quick Time (sec)'])
            speedup = bubble_time / quick_time
            comp_reduction = ((bubble_comps - quick_comps) / bubble_comps) * 100
            writer.writerow(['Sorting (Random)', size, 'Bubble Sort', f"{bubble_time:.6f}", 'Quick Sort', f"{quick_time:.6f}", f"{speedup:.2f}", f"{comp_reduction:.2f}"])
    
    print("   Created: comparison_speedup.csv")
    
    # CSV 4: GROWTH RATE ANALYSIS
    print("\n4. Creating comparison_growth_rate.csv...")
    with open('comparison_growth_rate.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Size 1', 'Comparisons 1', 'Size 2', 'Comparisons 2', 'Size Growth (x)', 'Comparisons Growth (x)', 'Theoretical Complexity', 'Matches Theory?'])
        
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
            writer.writerow(['Linear Search', size1, linear1, size2, linear2, f"{size_growth:.2f}", f"{linear_growth:.2f}", 'O(n)', 'Yes' if matches_linear else 'Close'])
            
            # Binary Search
            binary1 = int(row1['Binary Comparisons'])
            binary2 = int(row2['Binary Comparisons'])
            binary_growth = binary2 / binary1 if binary1 > 0 else 0
            matches_log = binary_growth < size_growth / 2
            writer.writerow(['Binary Search', size1, binary1, size2, binary2, f"{size_growth:.2f}", f"{binary_growth:.2f}", 'O(log n)', 'Yes' if matches_log else 'Close'])
        
        # Sorting algorithms growth (Random data)
        for i in range(len(df_random) - 1):
            row1 = df_random.iloc[i]
            row2 = df_random.iloc[i + 1]
            size1 = int(row1['Input Size'])
            size2 = int(row2['Input Size'])
            size_growth = size2 / size1
            expected_n2 = size_growth ** 2
            
            # Bubble Sort
            bubble1 = int(row1['Bubble Comparisons'])
            bubble2 = int(row2['Bubble Comparisons'])
            bubble_growth = bubble2 / bubble1
            matches_n2 = abs(bubble_growth - expected_n2) < expected_n2 * 0.3
            writer.writerow(['Bubble Sort', size1, bubble1, size2, bubble2, f"{size_growth:.2f}", f"{bubble_growth:.2f}", 'O(n^2)', 'Yes' if matches_n2 else 'Close'])
            
            # Selection Sort
            selection1 = int(row1['Selection Comparisons'])
            selection2 = int(row2['Selection Comparisons'])
            selection_growth = selection2 / selection1
            matches_n2_sel = abs(selection_growth - expected_n2) < expected_n2 * 0.3
            writer.writerow(['Selection Sort', size1, selection1, size2, selection2, f"{size_growth:.2f}", f"{selection_growth:.2f}", 'O(n^2)', 'Yes' if matches_n2_sel else 'Close'])
            
            # Merge Sort
            merge1 = int(row1['Merge Comparisons'])
            merge2 = int(row2['Merge Comparisons'])
            merge_growth = merge2 / merge1
            matches_nlogn = size_growth < merge_growth < size_growth ** 2
            writer.writerow(['Merge Sort', size1, merge1, size2, merge2, f"{size_growth:.2f}", f"{merge_growth:.2f}", 'O(n log n)', 'Yes' if matches_nlogn else 'Close'])
            
            # Quick Sort
            quick1 = int(row1['Quick Comparisons'])
            quick2 = int(row2['Quick Comparisons'])
            quick_growth = quick2 / quick1
            matches_nlogn_q = size_growth < quick_growth < size_growth ** 2
            writer.writerow(['Quick Sort', size1, quick1, size2, quick2, f"{size_growth:.2f}", f"{quick_growth:.2f}", 'O(n log n)', 'Yes' if matches_nlogn_q else 'Close'])
    
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
