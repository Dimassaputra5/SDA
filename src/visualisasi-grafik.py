import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


def plot_search_comparison():
    """Grafik perbandingan Linear vs Binary Search"""
    
    # Baca data
    df = pd.read_csv('results_search.csv')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot 1: Comparisons
    ax1.plot(df['Input Size'], df['Linear Comparisons'], 
             marker='o', linewidth=2, markersize=8, label='Linear Search O(n)', color='#e74c3c')
    ax1.plot(df['Input Size'], df['Binary Comparisons'], 
             marker='s', linewidth=2, markersize=8, label='Binary Search O(log n)', color='#27ae60')
    
    ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Comparisons', fontsize=12, fontweight='bold')
    ax1.set_title('Search Algorithms: Comparisons vs Input Size', 
                  fontsize=14, fontweight='bold', pad=20)
    ax1.legend(fontsize=11, loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')  # Log scale untuk better visualization
    
    # Tambah annotations
    max_idx = df['Input Size'].idxmax()
    ax1.annotate(f"{df.loc[max_idx, 'Linear Comparisons']:,.0f} comparisons", 
                xy=(df.loc[max_idx, 'Input Size'], df.loc[max_idx, 'Linear Comparisons']),
                xytext=(20, 20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    # Plot 2: Execution Time
    ax2.plot(df['Input Size'], df['Linear Time (sec)'], 
             marker='o', linewidth=2, markersize=8, label='Linear Search', color='#e74c3c')
    ax2.plot(df['Input Size'], df['Binary Time (sec)'], 
             marker='s', linewidth=2, markersize=8, label='Binary Search', color='#27ae60')
    
    ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Execution Time (seconds)', fontsize=12, fontweight='bold')
    ax2.set_title('Search Algorithms: Execution Time vs Input Size', 
                  fontsize=14, fontweight='bold', pad=20)
    ax2.legend(fontsize=11, loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('grafik_search_algorithms.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_search_algorithms.png")
    plt.close()



def plot_sorting_random():
    """Grafik sorting algorithms dengan random data"""
    
    # Baca data
    df = pd.read_csv('results_sorting_sorting_random.csv')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot 1: Comparisons
    ax1.plot(df['Input Size'], df['Bubble Comparisons'], 
             marker='o', linewidth=2, markersize=8, label='Bubble Sort O(n²)', color='#e74c3c')
    ax1.plot(df['Input Size'], df['Insertion Comparisons'], 
             marker='s', linewidth=2, markersize=8, label='Insertion Sort O(n²)', color='#f39c12')
    ax1.plot(df['Input Size'], df['Merge Comparisons'], 
             marker='^', linewidth=2, markersize=8, label='Merge Sort O(n log n)', color='#27ae60')
    
    ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Comparisons', fontsize=12, fontweight='bold')
    ax1.set_title('Sorting Algorithms: Comparisons (Random Data)', 
                  fontsize=14, fontweight='bold', pad=20)
    ax1.legend(fontsize=11, loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    # Plot 2: Execution Time
    ax2.plot(df['Input Size'], df['Bubble Time (sec)'], 
             marker='o', linewidth=2, markersize=8, label='Bubble Sort', color='#e74c3c')
    ax2.plot(df['Input Size'], df['Insertion Time (sec)'], 
             marker='s', linewidth=2, markersize=8, label='Insertion Sort', color='#f39c12')
    ax2.plot(df['Input Size'], df['Merge Time (sec)'], 
             marker='^', linewidth=2, markersize=8, label='Merge Sort', color='#27ae60')
    
    ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Execution Time (seconds)', fontsize=12, fontweight='bold')
    ax2.set_title('Sorting Algorithms: Execution Time (Random Data)', 
                  fontsize=14, fontweight='bold', pad=20)
    ax2.legend(fontsize=11, loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    # Annotation untuk perbedaan dramatis
    max_idx = len(df) - 1
    ax2.annotate(f"Bubble: {df.loc[max_idx, 'Bubble Time (sec)']:.2f}s\nMerge: {df.loc[max_idx, 'Merge Time (sec)']:.4f}s", 
                xy=(df.loc[max_idx, 'Input Size'], df.loc[max_idx, 'Bubble Time (sec)']),
                xytext=(20, -40), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    plt.tight_layout()
    plt.savefig('grafik_sorting_random.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_sorting_random.png")
    plt.close()


# ============================================================
# GRAFIK 3: BEST VS WORST CASE COMPARISON
# ============================================================

def plot_best_vs_worst_case():
    """Perbandingan best case vs worst case untuk sorting"""
    
    # Baca data
    df_best = pd.read_csv('results_sorting_sorting_sorted.csv')
    df_worst = pd.read_csv('results_sorting_sorting_reverse.csv')
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Bubble Sort - Best vs Worst
    ax1 = axes[0, 0]
    ax1.plot(df_best['Input Size'], df_best['Bubble Time (sec)'], 
             marker='o', linewidth=2, markersize=8, label='Best Case (Sorted)', color='#27ae60')
    ax1.plot(df_worst['Input Size'], df_worst['Bubble Time (sec)'], 
             marker='s', linewidth=2, markersize=8, label='Worst Case (Reverse)', color='#e74c3c')
    ax1.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Execution Time (seconds)', fontsize=11, fontweight='bold')
    ax1.set_title('Bubble Sort: Best vs Worst Case', fontsize=13, fontweight='bold', pad=15)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    # Insertion Sort - Best vs Worst
    ax2 = axes[0, 1]
    ax2.plot(df_best['Input Size'], df_best['Insertion Time (sec)'], 
             marker='o', linewidth=2, markersize=8, label='Best Case (Sorted)', color='#27ae60')
    ax2.plot(df_worst['Input Size'], df_worst['Insertion Time (sec)'], 
             marker='s', linewidth=2, markersize=8, label='Worst Case (Reverse)', color='#e74c3c')
    ax2.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Execution Time (seconds)', fontsize=11, fontweight='bold')
    ax2.set_title('Insertion Sort: Best vs Worst Case', fontsize=13, fontweight='bold', pad=15)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    # Merge Sort - Consistent Performance
    ax3 = axes[1, 0]
    ax3.plot(df_best['Input Size'], df_best['Merge Time (sec)'], 
             marker='o', linewidth=2, markersize=8, label='Best Case', color='#3498db')
    ax3.plot(df_worst['Input Size'], df_worst['Merge Time (sec)'], 
             marker='s', linewidth=2, markersize=8, label='Worst Case', color='#9b59b6')
    ax3.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Execution Time (seconds)', fontsize=11, fontweight='bold')
    ax3.set_title('Merge Sort: Consistent O(n log n)', fontsize=13, fontweight='bold', pad=15)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    # Summary: All algorithms worst case
    ax4 = axes[1, 1]
    ax4.plot(df_worst['Input Size'], df_worst['Bubble Time (sec)'], 
             marker='o', linewidth=2, markersize=8, label='Bubble O(n²)', color='#e74c3c')
    ax4.plot(df_worst['Input Size'], df_worst['Insertion Time (sec)'], 
             marker='s', linewidth=2, markersize=8, label='Insertion O(n²)', color='#f39c12')
    ax4.plot(df_worst['Input Size'], df_worst['Merge Time (sec)'], 
             marker='^', linewidth=2, markersize=8, label='Merge O(n log n)', color='#27ae60')
    ax4.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Execution Time (seconds)', fontsize=11, fontweight='bold')
    ax4.set_title('Worst Case Comparison: All Algorithms', fontsize=13, fontweight='bold', pad=15)
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('grafik_best_vs_worst.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_best_vs_worst.png")
    plt.close()



def plot_growth_rate_analysis():
    """Analisis growth rate untuk membuktikan Big-O"""
    
    # Baca data
    df_search = pd.read_csv('results_search.csv')
    df_sort = pd.read_csv('results_sorting_sorting_random.csv')
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Theoretical curves
    n_search = np.array(df_search['Input Size'])
    n_sort = np.array(df_sort['Input Size'])
    
    # Search: Linear O(n)
    ax1 = axes[0, 0]
    ax1.scatter(df_search['Input Size'], df_search['Linear Comparisons'], 
                s=100, alpha=0.7, label='Actual', color='#e74c3c', zorder=3)
    # Theoretical O(n)
    theoretical_linear = n_search
    ax1.plot(n_search, theoretical_linear, '--', linewidth=2, 
             label='Theoretical O(n)', color='#34495e', alpha=0.7)
    ax1.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    ax1.set_title('Linear Search: Actual vs Theoretical O(n)', 
                  fontsize=13, fontweight='bold', pad=15)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Search: Binary O(log n)
    ax2 = axes[0, 1]
    ax2.scatter(df_search['Input Size'], df_search['Binary Comparisons'], 
                s=100, alpha=0.7, label='Actual', color='#27ae60', zorder=3)
    # Theoretical O(log n)
    theoretical_log = np.log2(n_search)
    ax2.plot(n_search, theoretical_log, '--', linewidth=2, 
             label='Theoretical O(log n)', color='#34495e', alpha=0.7)
    ax2.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    ax2.set_title('Binary Search: Actual vs Theoretical O(log n)', 
                  fontsize=13, fontweight='bold', pad=15)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # Sorting: Bubble O(n²)
    ax3 = axes[1, 0]
    ax3.scatter(df_sort['Input Size'], df_sort['Bubble Comparisons'], 
                s=100, alpha=0.7, label='Actual', color='#e74c3c', zorder=3)
    # Theoretical O(n²)
    theoretical_n2 = (n_sort ** 2) / 2  # n²/2 untuk bubble sort
    ax3.plot(n_sort, theoretical_n2, '--', linewidth=2, 
             label='Theoretical O(n²)', color='#34495e', alpha=0.7)
    ax3.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    ax3.set_title('Bubble Sort: Actual vs Theoretical O(n²)', 
                  fontsize=13, fontweight='bold', pad=15)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    # Sorting: Merge O(n log n)
    ax4 = axes[1, 1]
    ax4.scatter(df_sort['Input Size'], df_sort['Merge Comparisons'], 
                s=100, alpha=0.7, label='Actual', color='#27ae60', zorder=3)
    # Theoretical O(n log n)
    theoretical_nlogn = n_sort * np.log2(n_sort)
    ax4.plot(n_sort, theoretical_nlogn, '--', linewidth=2, 
             label='Theoretical O(n log n)', color='#34495e', alpha=0.7)
    ax4.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Comparisons', fontsize=11, fontweight='bold')
    ax4.set_title('Merge Sort: Actual vs Theoretical O(n log n)', 
                  fontsize=13, fontweight='bold', pad=15)
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('grafik_growth_rate.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_growth_rate.png")
    plt.close()



def plot_speedup_comparison():
    """Grafik speedup untuk menunjukkan perbedaan performa"""
    
    df_search = pd.read_csv('results_search.csv')
    df_sort = pd.read_csv('results_sorting_sorting_random.csv')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Search Speedup
    speedup_search = df_search['Linear Comparisons'] / df_search['Binary Comparisons']
    ax1.bar(range(len(df_search)), speedup_search, color='#3498db', alpha=0.7, edgecolor='black')
    ax1.set_xticks(range(len(df_search)))
    ax1.set_xticklabels([f"{n:,}" for n in df_search['Input Size']], rotation=45)
    ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Speedup Factor (Linear / Binary)', fontsize=12, fontweight='bold')
    ax1.set_title('Binary Search Speedup over Linear Search', 
                  fontsize=14, fontweight='bold', pad=20)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, v in enumerate(speedup_search):
        ax1.text(i, v + max(speedup_search)*0.02, f'{v:.0f}x', 
                ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # Sorting Speedup (Merge vs Bubble)
    speedup_sort = df_sort['Bubble Time (sec)'] / df_sort['Merge Time (sec)']
    ax2.bar(range(len(df_sort)), speedup_sort, color='#e74c3c', alpha=0.7, edgecolor='black')
    ax2.set_xticks(range(len(df_sort)))
    ax2.set_xticklabels([f"{n:,}" for n in df_sort['Input Size']], rotation=45)
    ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Speedup Factor (Bubble / Merge)', fontsize=12, fontweight='bold')
    ax2.set_title('Merge Sort Speedup over Bubble Sort', 
                  fontsize=14, fontweight='bold', pad=20)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, v in enumerate(speedup_sort):
        ax2.text(i, v + max(speedup_sort)*0.02, f'{v:.0f}x', 
                ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('grafik_speedup.png', dpi=300, bbox_inches='tight')
    print("Saved: grafik_speedup.png")
    plt.close()



if __name__ == "__main__":   
    print("Generating visualizations...\n")
    
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
        print("  1. grafik_search_algorithms.png")
        print("  2. grafik_sorting_random.png")
        print("  3. grafik_best_vs_worst.png")
        print("  4. grafik_growth_rate.png")
        print("  5. grafik_speedup.png")
        print("\n All graphs saved in high resolution (300 DPI)")
        print(" Ready for presentation!")
        print("="*80)
        
    except FileNotFoundError as e:
        print(f"\nError: CSV file not found!")
        print(f"   {e}")
        print("\nPlease run dataset-generator.py first to generate CSV files.")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure all required CSV files are present:")
        print("  - results_search.csv")
        print("  - results_sorting_sorting_random.csv")
        print("  - results_sorting_sorting_sorted.csv")
        print("  - results_sorting_sorting_reverse.csv")
