import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


def plot_search_comparison():
    """Grafik perbandingan Linear vs Binary Search"""
    df = pd.read_csv('results_search.csv')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    ax1.plot(df['Input Size'], df['Linear Comparisons'], marker='o', linewidth=2, markersize=8, label='Linear Search O(n)', color='#e74c3c')
    ax1.plot(df['Input Size'], df['Binary Comparisons'], marker='s', linewidth=2, markersize=8, label='Binary Search O(log n)', color='#27ae60')
    ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Comparisons', fontsize=12, fontweight='bold')
    ax1.set_title('Search Algorithms: Comparisons vs Input Size', fontsize=14, fontweight='bold', pad=20)
    ax1.legend(fontsize=11, loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    ax2.plot(df['Input Size'], df['Linear Time (sec)'], marker='o', linewidth=2, markersize=8, label='Linear Search', color='#e74c3c')
    ax2.plot(df['Input Size'], df['Binary Time (sec)'], marker='s', linewidth=2, markersize=8, label='Binary Search', color='#27ae60')
    ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Execution Time (seconds)', fontsize=12, fontweight='bold')
    ax2.set_title('Search Algorithms: Execution Time vs Input Size', fontsize=14, fontweight='bold', pad=20)
    ax2.legend(fontsize=11, loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('grafik_search_algorithms.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_search_algorithms.png")
    plt.close()


def plot_sorting_random():
    """Grafik sorting algorithms dengan random data"""
    df = pd.read_csv('results_sorting_sorting_random.csv')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    ax1.plot(df['Input Size'], df['Bubble Comparisons'], marker='o', linewidth=2, markersize=8, label='Bubble Sort O(n²)', color='#e74c3c')
    ax1.plot(df['Input Size'], df['Selection Comparisons'], marker='d', linewidth=2, markersize=8, label='Selection Sort O(n²)', color='#e67e22')
    ax1.plot(df['Input Size'], df['Insertion Comparisons'], marker='s', linewidth=2, markersize=8, label='Insertion Sort O(n²)', color='#f39c12')
    ax1.plot(df['Input Size'], df['Merge Comparisons'], marker='^', linewidth=2, markersize=8, label='Merge Sort O(n log n)', color='#27ae60')
    ax1.plot(df['Input Size'], df['Quick Comparisons'], marker='v', linewidth=2, markersize=8, label='Quick Sort O(n log n)', color='#3498db')
    ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Comparisons', fontsize=12, fontweight='bold')
    ax1.set_title('Sorting Algorithms: Comparisons (Random Data)', fontsize=14, fontweight='bold', pad=20)
    ax1.legend(fontsize=10, loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    ax2.plot(df['Input Size'], df['Bubble Time (sec)'], marker='o', linewidth=2, markersize=8, label='Bubble Sort', color='#e74c3c')
    ax2.plot(df['Input Size'], df['Selection Time (sec)'], marker='d', linewidth=2, markersize=8, label='Selection Sort', color='#e67e22')
    ax2.plot(df['Input Size'], df['Insertion Time (sec)'], marker='s', linewidth=2, markersize=8, label='Insertion Sort', color='#f39c12')
    ax2.plot(df['Input Size'], df['Merge Time (sec)'], marker='^', linewidth=2, markersize=8, label='Merge Sort', color='#27ae60')
    ax2.plot(df['Input Size'], df['Quick Time (sec)'], marker='v', linewidth=2, markersize=8, label='Quick Sort', color='#3498db')
    ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Execution Time (seconds)', fontsize=12, fontweight='bold')
    ax2.set_title('Sorting Algorithms: Execution Time (Random Data)', fontsize=14, fontweight='bold', pad=20)
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('grafik_sorting_random.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_sorting_random.png")
    plt.close()


def plot_best_vs_worst_case():
    """Perbandingan best case vs worst case untuk sorting"""
    df_best = pd.read_csv('results_sorting_sorting_sorted.csv')
    df_worst = pd.read_csv('results_sorting_sorting_reverse.csv')
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    
    # Bubble Sort
    axes[0, 0].plot(df_best['Input Size'], df_best['Bubble Time (sec)'], marker='o', linewidth=2, markersize=8, label='Best Case', color='#27ae60')
    axes[0, 0].plot(df_worst['Input Size'], df_worst['Bubble Time (sec)'], marker='s', linewidth=2, markersize=8, label='Worst Case', color='#e74c3c')
    axes[0, 0].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 0].set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
    axes[0, 0].set_title('Bubble Sort: Best vs Worst', fontsize=13, fontweight='bold')
    axes[0, 0].legend(fontsize=10)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_yscale('log')
    
    # Selection Sort
    axes[0, 1].plot(df_best['Input Size'], df_best['Selection Time (sec)'], marker='o', linewidth=2, markersize=8, label='Best Case', color='#27ae60')
    axes[0, 1].plot(df_worst['Input Size'], df_worst['Selection Time (sec)'], marker='s', linewidth=2, markersize=8, label='Worst Case', color='#e74c3c')
    axes[0, 1].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 1].set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
    axes[0, 1].set_title('Selection Sort: Best vs Worst', fontsize=13, fontweight='bold')
    axes[0, 1].legend(fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_yscale('log')
    
    # Insertion Sort
    axes[0, 2].plot(df_best['Input Size'], df_best['Insertion Time (sec)'], marker='o', linewidth=2, markersize=8, label='Best Case', color='#27ae60')
    axes[0, 2].plot(df_worst['Input Size'], df_worst['Insertion Time (sec)'], marker='s', linewidth=2, markersize=8, label='Worst Case', color='#e74c3c')
    axes[0, 2].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 2].set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
    axes[0, 2].set_title('Insertion Sort: Best vs Worst', fontsize=13, fontweight='bold')
    axes[0, 2].legend(fontsize=10)
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].set_yscale('log')
    
    # Merge Sort
    axes[1, 0].plot(df_best['Input Size'], df_best['Merge Time (sec)'], marker='o', linewidth=2, markersize=8, label='Best Case', color='#3498db')
    axes[1, 0].plot(df_worst['Input Size'], df_worst['Merge Time (sec)'], marker='s', linewidth=2, markersize=8, label='Worst Case', color='#9b59b6')
    axes[1, 0].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 0].set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
    axes[1, 0].set_title('Merge Sort: Consistent O(n log n)', fontsize=13, fontweight='bold')
    axes[1, 0].legend(fontsize=10)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Quick Sort
    axes[1, 1].plot(df_best['Input Size'], df_best['Quick Time (sec)'], marker='o', linewidth=2, markersize=8, label='Best Case', color='#3498db')
    axes[1, 1].plot(df_worst['Input Size'], df_worst['Quick Time (sec)'], marker='s', linewidth=2, markersize=8, label='Worst Case', color='#9b59b6')
    axes[1, 1].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Quick Sort: Variable Performance', fontsize=13, fontweight='bold')
    axes[1, 1].legend(fontsize=10)
    axes[1, 1].grid(True, alpha=0.3)
    
    # All algorithms worst case
    axes[1, 2].plot(df_worst['Input Size'], df_worst['Bubble Time (sec)'], marker='o', linewidth=2, markersize=8, label='Bubble', color='#e74c3c')
    axes[1, 2].plot(df_worst['Input Size'], df_worst['Selection Time (sec)'], marker='d', linewidth=2, markersize=8, label='Selection', color='#e67e22')
    axes[1, 2].plot(df_worst['Input Size'], df_worst['Insertion Time (sec)'], marker='s', linewidth=2, markersize=8, label='Insertion', color='#f39c12')
    axes[1, 2].plot(df_worst['Input Size'], df_worst['Merge Time (sec)'], marker='^', linewidth=2, markersize=8, label='Merge', color='#27ae60')
    axes[1, 2].plot(df_worst['Input Size'], df_worst['Quick Time (sec)'], marker='v', linewidth=2, markersize=8, label='Quick', color='#3498db')
    axes[1, 2].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 2].set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
    axes[1, 2].set_title('Worst Case: All Algorithms', fontsize=13, fontweight='bold')
    axes[1, 2].legend(fontsize=9)
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('grafik_best_vs_worst.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_best_vs_worst.png")
    plt.close()


def plot_growth_rate_analysis():
    """Analisis growth rate untuk membuktikan Big-O"""
    df_search = pd.read_csv('results_search.csv')
    df_sort = pd.read_csv('results_sorting_sorting_random.csv')
    fig, axes = plt.subplots(2, 4, figsize=(24, 12))
    
    n_search = np.array(df_search['Input Size'])
    n_sort = np.array(df_sort['Input Size'])
    
    # Linear Search
    axes[0, 0].scatter(df_search['Input Size'], df_search['Linear Comparisons'], s=100, alpha=0.7, label='Actual', color='#e74c3c', zorder=3)
    axes[0, 0].plot(n_search, n_search, '--', linewidth=2, label='Theoretical O(n)', color='#34495e', alpha=0.7)
    axes[0, 0].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 0].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[0, 0].set_title('Linear Search: O(n)', fontsize=13, fontweight='bold')
    axes[0, 0].legend(fontsize=10)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Binary Search
    axes[0, 1].scatter(df_search['Input Size'], df_search['Binary Comparisons'], s=100, alpha=0.7, label='Actual', color='#27ae60', zorder=3)
    axes[0, 1].plot(n_search, np.log2(n_search), '--', linewidth=2, label='Theoretical O(log n)', color='#34495e', alpha=0.7)
    axes[0, 1].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 1].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[0, 1].set_title('Binary Search: O(log n)', fontsize=13, fontweight='bold')
    axes[0, 1].legend(fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Bubble Sort
    axes[0, 2].scatter(df_sort['Input Size'], df_sort['Bubble Comparisons'], s=100, alpha=0.7, label='Actual', color='#e74c3c', zorder=3)
    axes[0, 2].plot(n_sort, (n_sort ** 2) / 2, '--', linewidth=2, label='Theoretical O(n²)', color='#34495e', alpha=0.7)
    axes[0, 2].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 2].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[0, 2].set_title('Bubble Sort: O(n²)', fontsize=13, fontweight='bold')
    axes[0, 2].legend(fontsize=10)
    axes[0, 2].grid(True, alpha=0.3)
    
    # Selection Sort
    axes[0, 3].scatter(df_sort['Input Size'], df_sort['Selection Comparisons'], s=100, alpha=0.7, label='Actual', color='#e67e22', zorder=3)
    axes[0, 3].plot(n_sort, (n_sort ** 2) / 2, '--', linewidth=2, label='Theoretical O(n²)', color='#34495e', alpha=0.7)
    axes[0, 3].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0, 3].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[0, 3].set_title('Selection Sort: O(n²)', fontsize=13, fontweight='bold')
    axes[0, 3].legend(fontsize=10)
    axes[0, 3].grid(True, alpha=0.3)
    
    # Insertion Sort
    axes[1, 0].scatter(df_sort['Input Size'], df_sort['Insertion Comparisons'], s=100, alpha=0.7, label='Actual', color='#f39c12', zorder=3)
    axes[1, 0].plot(n_sort, (n_sort ** 2) / 4, '--', linewidth=2, label='Theoretical O(n²)', color='#34495e', alpha=0.7)
    axes[1, 0].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 0].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[1, 0].set_title('Insertion Sort: O(n²)', fontsize=13, fontweight='bold')
    axes[1, 0].legend(fontsize=10)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Merge Sort
    axes[1, 1].scatter(df_sort['Input Size'], df_sort['Merge Comparisons'], s=100, alpha=0.7, label='Actual', color='#27ae60', zorder=3)
    axes[1, 1].plot(n_sort, n_sort * np.log2(n_sort), '--', linewidth=2, label='Theoretical O(n log n)', color='#34495e', alpha=0.7)
    axes[1, 1].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Merge Sort: O(n log n)', fontsize=13, fontweight='bold')
    axes[1, 1].legend(fontsize=10)
    axes[1, 1].grid(True, alpha=0.3)
    
    # Quick Sort
    axes[1, 2].scatter(df_sort['Input Size'], df_sort['Quick Comparisons'], s=100, alpha=0.7, label='Actual', color='#3498db', zorder=3)
    axes[1, 2].plot(n_sort, n_sort * np.log2(n_sort), '--', linewidth=2, label='Theoretical O(n log n)', color='#34495e', alpha=0.7)
    axes[1, 2].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 2].set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    axes[1, 2].set_title('Quick Sort: O(n log n)', fontsize=13, fontweight='bold')
    axes[1, 2].legend(fontsize=10)
    axes[1, 2].grid(True, alpha=0.3)
    
    # Complexity Comparison - All Algorithms
    axes[1, 3].plot(n_search, n_search, '-', linewidth=2, label='Linear O(n)', color='#e74c3c', alpha=0.7)
    axes[1, 3].plot(n_search, np.log2(n_search) * 100, '-', linewidth=2, label='Binary O(log n)', color='#27ae60', alpha=0.7)
    axes[1, 3].plot(n_sort, (n_sort ** 2) / 1000, '-', linewidth=2, label='Bubble/Selection O(n²)', color='#e67e22', alpha=0.7)
    axes[1, 3].plot(n_sort, n_sort * np.log2(n_sort) / 10, '-', linewidth=2, label='Merge/Quick O(n log n)', color='#3498db', alpha=0.7)
    axes[1, 3].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1, 3].set_ylabel('Operations (scaled)', fontsize=11, fontweight='bold')
    axes[1, 3].set_title('Complexity Classes Comparison', fontsize=13, fontweight='bold')
    axes[1, 3].legend(fontsize=9)
    axes[1, 3].grid(True, alpha=0.3)
    axes[1, 3].set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('grafik_growth_rate.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_growth_rate.png")
    plt.close()


def plot_speedup_comparison():
    """Grafik speedup untuk menunjukkan perbedaan performa"""
    df_search = pd.read_csv('results_search.csv')
    df_sort = pd.read_csv('results_sorting_sorting_random.csv')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    speedup_search = df_search['Linear Comparisons'] / df_search['Binary Comparisons']
    ax1.bar(range(len(df_search)), speedup_search, color='#3498db', alpha=0.7, edgecolor='black')
    ax1.set_xticks(range(len(df_search)))
    ax1.set_xticklabels([f"{n:,}" for n in df_search['Input Size']], rotation=45)
    ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Speedup Factor', fontsize=12, fontweight='bold')
    ax1.set_title('Binary Search Speedup over Linear Search', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    for i, v in enumerate(speedup_search):
        ax1.text(i, v + max(speedup_search)*0.02, f'{v:.0f}x', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    speedup_sort = df_sort['Bubble Time (sec)'] / df_sort['Quick Time (sec)']
    ax2.bar(range(len(df_sort)), speedup_sort, color='#e74c3c', alpha=0.7, edgecolor='black')
    ax2.set_xticks(range(len(df_sort)))
    ax2.set_xticklabels([f"{n:,}" for n in df_sort['Input Size']], rotation=45)
    ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Speedup Factor', fontsize=12, fontweight='bold')
    ax2.set_title('Quick Sort Speedup over Bubble Sort', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    for i, v in enumerate(speedup_sort):
        ax2.text(i, v + max(speedup_sort)*0.02, f'{v:.0f}x', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('grafik_speedup.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_speedup.png")
    plt.close()


if __name__ == "__main__":
    print("="*80)
    print("GENERATING VISUALIZATIONS FOR 7 ALGORITHMS")
    print("="*80)
    print("\nSearching Algorithms (2):")
    print("  1. Linear Search")
    print("  2. Binary Search")
    print("\nSorting - Simple (3):")
    print("  3. Bubble Sort")
    print("  4. Selection Sort")
    print("  5. Insertion Sort")
    print("\nSorting - Advanced (2):")
    print("  6. Merge Sort")
    print("  7. Quick Sort")
    print("\n" + "="*80)
    print("Processing...\n")
    
    try:
        plot_search_comparison()
        plot_sorting_random()
        plot_best_vs_worst_case()
        plot_growth_rate_analysis()
        plot_speedup_comparison()
        
        print("\n" + "="*80)
        print("ALL VISUALIZATIONS COMPLETED!")
        print("="*80)
        print("\nGenerated graphs:")
        print("  1. grafik_search_algorithms.png       - Linear & Binary Search")
        print("  2. grafik_sorting_random.png          - All 5 Sorting Algorithms")
        print("  3. grafik_best_vs_worst.png           - Best vs Worst Case Analysis")
        print("  4. grafik_growth_rate.png             - Big-O Growth Rate Proof")
        print("  5. grafik_speedup.png                 - Performance Speedup")
        print("\nAll graphs saved in high resolution (300 DPI)")
        print("Ready for presentation!")
        print("="*80)
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: CSV file not found: {e}")
        print("\n⚠️  Please run dataset-generator.py first.")
        print("="*80)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("="*80)
