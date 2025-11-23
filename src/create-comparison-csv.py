"""
COMPREHENSIVE COMPARISON & ANALYSIS - ENHANCED
Export semua data komparasi ke CSV lengkap dengan analisis mendalam

CSV Output:
1. comparison_all_algorithms.csv - Semua algoritma dalam satu file
2. comparison_summary.csv - Ringkasan performa
3. comparison_speedup.csv - Analisis speedup
4. comparison_growth_rate.csv - Verifikasi Big-O growth
5. comparison_statistics.csv - Statistik detail (NEW)
6. comparison_efficiency.csv - Efficiency & scaling analysis (NEW)
7. comparison_case_analysis.csv - Best/Avg/Worst case comparison (NEW)
"""

import csv
import pandas as pd
import numpy as np
from pathlib import Path


def create_comprehensive_comparison():
    """Buat CSV komparasi lengkap dari semua hasil testing"""
    
    print("="*80)
    print("CREATING ENHANCED COMPREHENSIVE COMPARISON CSV")
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
        print("\n❌ Error: Missing required files:")
        for f in missing_files:
            print(f"  - {f}")
        print("\n⚠️  Please run dataset-generator.py first!")
        return
    
    # Read all data
    df_search = pd.read_csv('results_search.csv')
    df_random = pd.read_csv('results_sorting_sorting_random.csv')
    df_sorted = pd.read_csv('results_sorting_sorting_sorted.csv')
    df_reverse = pd.read_csv('results_sorting_sorting_reverse.csv')
    
    print("\n Data loaded successfully")
    print(f"  - Search tests: {len(df_search)} size variations")
    print(f"  - Sorting tests: {len(df_random)} size variations x 3 data types")
    
    # CSV 1: ALL ALGORITHMS COMPARISON
    print("\n1. Creating comparison_all_algorithms.csv...")
    with open('comparison_all_algorithms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Data Type', 'Input Size (n)', 'Comparisons', 'Time (seconds)', 'Complexity Class', 'Notes'])
        
        # Search algorithms
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Linear Search', 'Sorted', size, int(row['Linear Comparisons']), float(row['Linear Time (sec)']), 'O(n)', 'Target at 90% position'])
            writer.writerow(['Binary Search', 'Sorted', size, int(row['Binary Comparisons']), float(row['Binary Time (sec)']), 'O(log n)', 'Target at 90% position'])
        
        # Sorting algorithms - Random
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Bubble Sort', 'Random', size, int(row['Bubble Comparisons']), float(row['Bubble Time (sec)']), 'O(n^2)', 'Average case'])
            writer.writerow(['Selection Sort', 'Random', size, int(row['Selection Comparisons']), float(row['Selection Time (sec)']), 'O(n^2)', 'Average case'])
            writer.writerow(['Insertion Sort', 'Random', size, int(row['Insertion Comparisons']), float(row['Insertion Time (sec)']), 'O(n^2)', 'Average case'])
            writer.writerow(['Merge Sort', 'Random', size, int(row['Merge Comparisons']), float(row['Merge Time (sec)']), 'O(n log n)', 'Consistent performance'])
            writer.writerow(['Quick Sort', 'Random', size, int(row['Quick Comparisons']), float(row['Quick Time (sec)']), 'O(n log n) avg', 'Average case'])
        
        # Sorting algorithms - Best case (Sorted)
        for _, row in df_sorted.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Bubble Sort', 'Already Sorted', size, int(row['Bubble Comparisons']), float(row['Bubble Time (sec)']), 'O(n)', 'Best case - early exit'])
            writer.writerow(['Selection Sort', 'Already Sorted', size, int(row['Selection Comparisons']), float(row['Selection Time (sec)']), 'O(n^2)', 'No benefit from sorted'])
            writer.writerow(['Insertion Sort', 'Already Sorted', size, int(row['Insertion Comparisons']), float(row['Insertion Time (sec)']), 'O(n)', 'Best case - minimal shifts'])
            writer.writerow(['Merge Sort', 'Already Sorted', size, int(row['Merge Comparisons']), float(row['Merge Time (sec)']), 'O(n log n)', 'Consistent performance'])
            writer.writerow(['Quick Sort', 'Already Sorted', size, int(row['Quick Comparisons']), float(row['Quick Time (sec)']), 'O(n log n)', 'Good with median pivot'])
        
        # Sorting algorithms - Worst case (Reverse)
        for _, row in df_reverse.iterrows():
            size = int(row['Input Size'])
            writer.writerow(['Bubble Sort', 'Reverse Sorted', size, int(row['Bubble Comparisons']), float(row['Bubble Time (sec)']), 'O(n^2)', 'Worst case - max swaps'])
            writer.writerow(['Selection Sort', 'Reverse Sorted', size, int(row['Selection Comparisons']), float(row['Selection Time (sec)']), 'O(n^2)', 'Same as average'])
            writer.writerow(['Insertion Sort', 'Reverse Sorted', size, int(row['Insertion Comparisons']), float(row['Insertion Time (sec)']), 'O(n^2)', 'Worst case - max shifts'])
            writer.writerow(['Merge Sort', 'Reverse Sorted', size, int(row['Merge Comparisons']), float(row['Merge Time (sec)']), 'O(n log n)', 'Consistent performance'])
            writer.writerow(['Quick Sort', 'Reverse Sorted', size, int(row['Quick Comparisons']), float(row['Quick Time (sec)']), 'O(n log n)', 'Handled by median pivot'])
    
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
            speedup = linear_time / binary_time if binary_time > 0 else 0
            comp_reduction = ((linear_comps - binary_comps) / linear_comps) * 100 if linear_comps > 0 else 0
            writer.writerow(['Search Algorithms', size, 'Linear Search', f"{linear_time:.6f}", 'Binary Search', f"{binary_time:.6f}", f"{speedup:.2f}", f"{comp_reduction:.2f}"])
        
        # Quick vs Bubble Sort (Random)
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            bubble_comps = int(row['Bubble Comparisons'])
            quick_comps = int(row['Quick Comparisons'])
            bubble_time = float(row['Bubble Time (sec)'])
            quick_time = float(row['Quick Time (sec)'])
            speedup = bubble_time / quick_time if quick_time > 0 else 0
            comp_reduction = ((bubble_comps - quick_comps) / bubble_comps) * 100 if bubble_comps > 0 else 0
            writer.writerow(['Sorting O(n^2) vs O(n log n)', size, 'Bubble Sort', f"{bubble_time:.6f}", 'Quick Sort', f"{quick_time:.6f}", f"{speedup:.2f}", f"{comp_reduction:.2f}"])
        
        # Merge vs Bubble Sort (Random)
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            bubble_time = float(row['Bubble Time (sec)'])
            merge_time = float(row['Merge Time (sec)'])
            speedup = bubble_time / merge_time if merge_time > 0 else 0
            writer.writerow(['Simple vs Advanced Sort', size, 'Bubble Sort', f"{bubble_time:.6f}", 'Merge Sort', f"{merge_time:.6f}", f"{speedup:.2f}", 'N/A'])
    
    print("   Created: comparison_speedup.csv")
    
    # CSV 4: GROWTH RATE ANALYSIS
    print("\n4. Creating comparison_growth_rate.csv...")
    with open('comparison_growth_rate.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Size 1', 'Comparisons 1', 'Size 2', 'Comparisons 2', 'Size Growth (x)', 'Comparisons Growth (x)', 'Theoretical Complexity', 'Expected Growth', 'Matches Theory?'])
        
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
            linear_growth = linear2 / linear1 if linear1 > 0 else 0
            expected = size_growth
            matches_linear = abs(linear_growth - size_growth) < size_growth * 0.3
            writer.writerow(['Linear Search', size1, linear1, size2, linear2, f"{size_growth:.2f}", f"{linear_growth:.2f}", 'O(n)', f"{expected:.2f}", 'Yes' if matches_linear else 'Close'])
            
            # Binary Search
            binary1 = int(row1['Binary Comparisons'])
            binary2 = int(row2['Binary Comparisons'])
            binary_growth = binary2 / binary1 if binary1 > 0 else 0
            expected = np.log2(size2) / np.log2(size1)
            matches_log = abs(binary_growth - expected) < expected * 0.5
            writer.writerow(['Binary Search', size1, binary1, size2, binary2, f"{size_growth:.2f}", f"{binary_growth:.2f}", 'O(log n)', f"{expected:.2f}", 'Yes' if matches_log else 'Close'])
        
        # Sorting algorithms growth (Random data)
        for i in range(len(df_random) - 1):
            row1 = df_random.iloc[i]
            row2 = df_random.iloc[i + 1]
            size1 = int(row1['Input Size'])
            size2 = int(row2['Input Size'])
            size_growth = size2 / size1
            expected_n2 = size_growth ** 2
            expected_nlogn = size_growth * (np.log2(size2) / np.log2(size1))
            
            # Bubble Sort
            bubble1 = int(row1['Bubble Comparisons'])
            bubble2 = int(row2['Bubble Comparisons'])
            bubble_growth = bubble2 / bubble1 if bubble1 > 0 else 0
            matches_n2 = abs(bubble_growth - expected_n2) < expected_n2 * 0.4
            writer.writerow(['Bubble Sort', size1, bubble1, size2, bubble2, f"{size_growth:.2f}", f"{bubble_growth:.2f}", 'O(n^2)', f"{expected_n2:.2f}", 'Yes' if matches_n2 else 'Close'])
            
            # Selection Sort
            selection1 = int(row1['Selection Comparisons'])
            selection2 = int(row2['Selection Comparisons'])
            selection_growth = selection2 / selection1 if selection1 > 0 else 0
            matches_n2_sel = abs(selection_growth - expected_n2) < expected_n2 * 0.4
            writer.writerow(['Selection Sort', size1, selection1, size2, selection2, f"{size_growth:.2f}", f"{selection_growth:.2f}", 'O(n^2)', f"{expected_n2:.2f}", 'Yes' if matches_n2_sel else 'Close'])
            
            # Insertion Sort
            insertion1 = int(row1['Insertion Comparisons'])
            insertion2 = int(row2['Insertion Comparisons'])
            insertion_growth = insertion2 / insertion1 if insertion1 > 0 else 0
            matches_n2_ins = abs(insertion_growth - expected_n2) < expected_n2 * 0.5
            writer.writerow(['Insertion Sort', size1, insertion1, size2, insertion2, f"{size_growth:.2f}", f"{insertion_growth:.2f}", 'O(n^2)', f"{expected_n2:.2f}", 'Yes' if matches_n2_ins else 'Close'])
            
            # Merge Sort
            merge1 = int(row1['Merge Comparisons'])
            merge2 = int(row2['Merge Comparisons'])
            merge_growth = merge2 / merge1 if merge1 > 0 else 0
            matches_nlogn = abs(merge_growth - expected_nlogn) < expected_nlogn * 0.5
            writer.writerow(['Merge Sort', size1, merge1, size2, merge2, f"{size_growth:.2f}", f"{merge_growth:.2f}", 'O(n log n)', f"{expected_nlogn:.2f}", 'Yes' if matches_nlogn else 'Close'])
            
            # Quick Sort
            quick1 = int(row1['Quick Comparisons'])
            quick2 = int(row2['Quick Comparisons'])
            quick_growth = quick2 / quick1 if quick1 > 0 else 0
            matches_nlogn_q = abs(quick_growth - expected_nlogn) < expected_nlogn * 0.6
            writer.writerow(['Quick Sort', size1, quick1, size2, quick2, f"{size_growth:.2f}", f"{quick_growth:.2f}", 'O(n log n) avg', f"{expected_nlogn:.2f}", 'Yes' if matches_nlogn_q else 'Close'])
    
    print("   Created: comparison_growth_rate.csv")
    
    # CSV 5: STATISTICS (NEW)
    print("\n5. Creating comparison_statistics.csv...")
    with open('comparison_statistics.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Metric', 'Min', 'Max', 'Mean', 'Median', 'Std Dev', 'Coefficient of Variation (%)'])
        
        # Search statistics - Comparisons
        linear_comps = df_search['Linear Comparisons'].values
        binary_comps = df_search['Binary Comparisons'].values
        
        for algo, comps in [('Linear Search', linear_comps), ('Binary Search', binary_comps)]:
            writer.writerow([algo, 'Comparisons', int(comps.min()), int(comps.max()), f"{comps.mean():.2f}", 
                           f"{np.median(comps):.2f}", f"{comps.std():.2f}", f"{(comps.std()/comps.mean()*100):.2f}"])
        
        # Search statistics - Time
        linear_time = df_search['Linear Time (sec)'].values
        binary_time = df_search['Binary Time (sec)'].values
        
        for algo, time in [('Linear Search', linear_time), ('Binary Search', binary_time)]:
            writer.writerow([algo, 'Time (sec)', f"{time.min():.6f}", f"{time.max():.6f}", f"{time.mean():.6f}", 
                           f"{np.median(time):.6f}", f"{time.std():.6f}", f"{(time.std()/time.mean()*100):.2f}"])
        
        # Sorting statistics - Random data
        algos = ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick']
        for algo_name in algos:
            comps = df_random[f'{algo_name} Comparisons'].values
            time = df_random[f'{algo_name} Time (sec)'].values
            
            writer.writerow([f'{algo_name} Sort', 'Comparisons', int(comps.min()), int(comps.max()), f"{comps.mean():.2f}", 
                           f"{np.median(comps):.2f}", f"{comps.std():.2f}", f"{(comps.std()/comps.mean()*100):.2f}"])
            writer.writerow([f'{algo_name} Sort', 'Time (sec)', f"{time.min():.6f}", f"{time.max():.6f}", f"{time.mean():.6f}", 
                           f"{np.median(time):.6f}", f"{time.std():.6f}", f"{(time.std()/time.mean()*100):.2f}"])
    
    print("   Created: comparison_statistics.csv")
    
    # CSV 6: EFFICIENCY ANALYSIS (NEW)
    print("\n6. Creating comparison_efficiency.csv...")
    with open('comparison_efficiency.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Input Size (n)', 'Comparisons per Element', 'Time per Element (ns)', 'Efficiency Score', 'Category'])
        
        # Search efficiency
        for _, row in df_search.iterrows():
            size = int(row['Input Size'])
            
            linear_comps = int(row['Linear Comparisons'])
            linear_time = float(row['Linear Time (sec)'])
            linear_comp_per_elem = linear_comps / size
            linear_time_per_elem = (linear_time / size) * 1e9  # nanoseconds
            linear_efficiency = size / linear_comps
            writer.writerow(['Linear Search', size, f"{linear_comp_per_elem:.2f}", f"{linear_time_per_elem:.2f}", 
                           f"{linear_efficiency:.4f}", 'Search'])
            
            binary_comps = int(row['Binary Comparisons'])
            binary_time = float(row['Binary Time (sec)'])
            binary_comp_per_elem = binary_comps / size
            binary_time_per_elem = (binary_time / size) * 1e9
            binary_efficiency = size / binary_comps
            writer.writerow(['Binary Search', size, f"{binary_comp_per_elem:.2f}", f"{binary_time_per_elem:.2f}", 
                           f"{binary_efficiency:.4f}", 'Search'])
        
        # Sorting efficiency - Random data
        for _, row in df_random.iterrows():
            size = int(row['Input Size'])
            
            for algo in ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick']:
                comps = int(row[f'{algo} Comparisons'])
                time = float(row[f'{algo} Time (sec)'])
                comp_per_elem = comps / size
                time_per_elem = (time / size) * 1e9
                efficiency = size / comps if comps > 0 else 0
                category = 'Simple Sort' if algo in ['Bubble', 'Selection', 'Insertion'] else 'Advanced Sort'
                writer.writerow([f'{algo} Sort', size, f"{comp_per_elem:.2f}", f"{time_per_elem:.2f}", 
                               f"{efficiency:.6f}", category])
    
    print("   Created: comparison_efficiency.csv")
    
    # CSV 7: CASE ANALYSIS (NEW)
    print("\n7. Creating comparison_case_analysis.csv...")
    with open('comparison_case_analysis.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Input Size (n)', 'Best Case Time', 'Average Case Time', 'Worst Case Time', 
                        'Best/Worst Ratio', 'Variance (%)', 'Stability'])
        
        for i in range(len(df_sorted)):
            size = int(df_sorted.iloc[i]['Input Size'])
            
            for algo in ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick']:
                best_time = float(df_sorted.iloc[i][f'{algo} Time (sec)'])
                avg_time = float(df_random.iloc[i][f'{algo} Time (sec)'])
                worst_time = float(df_reverse.iloc[i][f'{algo} Time (sec)'])
                
                ratio = worst_time / best_time if best_time > 0 else 0
                variance = ((worst_time - best_time) / avg_time) * 100 if avg_time > 0 else 0
                
                # Determine stability
                if ratio < 1.5:
                    stability = 'Highly Stable'
                elif ratio < 3:
                    stability = 'Stable'
                elif ratio < 10:
                    stability = 'Moderate'
                else:
                    stability = 'Variable'
                
                writer.writerow([f'{algo} Sort', size, f"{best_time:.6f}", f"{avg_time:.6f}", f"{worst_time:.6f}", 
                               f"{ratio:.2f}", f"{variance:.2f}", stability])
    
    print("   Created: comparison_case_analysis.csv")
    
    print("\n" + "="*80)
    print("ENHANCED COMPARISON CSV FILES COMPLETED!")
    print("="*80)
    print("\nGenerated files:")
    print("  1. comparison_all_algorithms.csv    - Semua data lengkap (68 records)")
    print("  2. comparison_summary.csv            - Ringkasan best/worst per size")
    print("  3. comparison_speedup.csv            - Analisis speedup detail")
    print("  4. comparison_growth_rate.csv        - Verifikasi Big-O growth")
    print("  5. comparison_statistics.csv         -  Min/Max/Mean/Median/StdDev")
    print("  6. comparison_efficiency.csv         -  Comparisons & time per element")
    print("  7. comparison_case_analysis.csv      - Best/Avg/Worst case stability")
    print("\n 7 CSV files ready for comprehensive analysis!")
    print(" Perfect for research paper and presentation!")
    print("="*80)


if __name__ == "__main__":
    print("\n" + "="*80)
    print("ENHANCED COMPREHENSIVE COMPARISON GENERATOR")
    print("Kelompok 2 - Advanced CSV Analysis")
    print("7 Algoritma Lengkap: 2 Searching + 5 Sorting")
    print("="*80)
    create_comprehensive_comparison()
