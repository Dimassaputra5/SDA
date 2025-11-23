import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def plot_search_comparison():
    ...
    # (tidak diubah)
    ...
def plot_sorting_random():
    ...
    # (tidak diubah)
    ...
def plot_best_vs_worst_case():
    ...
    # (tidak diubah)
    ...
def plot_growth_rate_analysis():
    ...
    # (tidak diubah)
    ...
def plot_speedup_comparison():
    ...
    # (tidak diubah)
    ...

# === Tambahan visualisasi dari CSV baru ===
def plot_statistik():
    df = pd.read_csv('comparison_statistics.csv')
    subset = df[df['Metric'] == 'Time (sec)']
    plt.figure(figsize=(10, 6))
    plt.bar(subset['Algorithm'], subset['Mean'].astype(float), yerr=subset['Std Dev'].astype(float), color='#3498db')
    plt.title('Mean Execution Time & Std Dev (Random Data)')
    plt.ylabel('Mean Time (seconds)')
    plt.xlabel('Algorithm')
    plt.tight_layout()
    plt.savefig('grafik_statistik_algoritma.png', dpi=300)
    plt.close()
    print("Saved: grafik_statistik_algoritma.png")

def plot_efficiency():
    df = pd.read_csv('comparison_efficiency.csv')
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Input Size (n)'], subset['Time per Element (ns)'].astype(float), marker='o', label=algo)
    plt.title('Efficiency: Time per Element (ns)')
    plt.ylabel('Time per Element (nanoseconds)')
    plt.xlabel('Input Size')
    plt.legend()
    plt.tight_layout()
    plt.savefig('grafik_efficiency.png', dpi=300)
    plt.close()
    print("Saved: grafik_efficiency.png")

def plot_stability_case_analysis():
    df = pd.read_csv('comparison_case_analysis.csv')
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Input Size (n)'], subset['Best/Worst Ratio'].astype(float), marker='o', label=algo)
    plt.title('Best/Worst Time Ratio per Algorithm')
    plt.ylabel('Best/Worst Ratio')
    plt.xlabel('Input Size')
    plt.legend()
    plt.tight_layout()
    plt.savefig('grafik_stability_case.png', dpi=300)
    plt.close()
    print("Saved: grafik_stability_case.png")


def plot_all_new():
    plot_statistik()
    plot_efficiency()
    plot_stability_case_analysis()

if __name__ == "__main__":
    print("="*80)
    print("GENERATING VISUALIZATIONS FOR 7 ALGORITHMS")
    print("="*80)
    print("\nProcessing...")
    try:
        plot_search_comparison()
        plot_sorting_random()
        plot_best_vs_worst_case()
        plot_growth_rate_analysis()
        plot_speedup_comparison()
        plot_all_new()
        print("\nALL VISUALIZATIONS COMPLETED!")
        print("\nGenerated graphs:")
        print("  - grafik_search_algorithms.png")
        print("  - grafik_sorting_random.png")
        print("  - grafik_best_vs_worst.png")
        print("  - grafik_growth_rate.png")
        print("  - grafik_speedup.png")
        print("  - grafik_statistik_algoritma.png")
        print("  - grafik_efficiency.png")
        print("  - grafik_stability_case.png")
        print("All graphs saved in high resolution (300 DPI)")
        print("Ready for presentation!")
    except FileNotFoundError as e:
        print(f"\nError: CSV file not found: {e}")
        print("\nPlease run dataset-generator.py first.")
        print("="*80)
    except Exception as e:
        print(f"\nError: {e}")
        print("="*80)
