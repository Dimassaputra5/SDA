# 📊 Analisis Kompleksitas Algoritma - Struktur Data & Algoritma

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/Dimassaputra5/SDA)

> Implementasi dan analisis empiris kompleksitas Big-O untuk algoritma pencarian dan pengurutan

## 🎯 Tujuan Repository

Repository ini berisi:
1. **Implementasi 5 algoritma** (Linear Search, Binary Search, Bubble Sort, Insertion Sort, Merge Sort)
2. **Dataset generator** untuk testing dengan berbagai ukuran input (100 - 1 juta elemen)
3. **Analisis empiris Big-O** dengan perhitungan comparisons, time, dan speedup
4. **Visualisasi grafik** perbandingan performa algoritma
5. **Jupyter Notebook interaktif** untuk eksplorasi data hasil testing

**Tujuan Utama:**
- Membuktikan kompleksitas Big-O secara empiris melalui testing
- Membandingkan performa algoritma O(n), O(log n), O(n²), dan O(n log n)
- Menganalisis growth rate untuk verifikasi teori kompleksitas
- Menyediakan data dan visualisasi untuk presentasi/laporan

---

## 📁 Struktur Repository

```
SDA/
├── src/
│   ├── dataset-generator-fixed.py       # Generate dataset & testing
│   ├── create-comparison-csv.py         # Buat CSV komparasi
│   ├── visualisasi-grafik.py           # Generate grafik
│   ├── algorithm-complexity-complete.py # Semua algoritma lengkap
│   └── analysis-kompleksitas-algoritma.ipynb  # Jupyter Notebook analisis
├── results/
│   ├── results_search.csv               # Hasil testing search
│   ├── results_sorting_sorting_random.csv   # Hasil sorting random
│   ├── results_sorting_sorting_sorted.csv   # Hasil sorting best case
│   ├── results_sorting_sorting_reverse.csv  # Hasil sorting worst case
│   ├── comparison_all_algorithms.csv    # Komparasi lengkap
│   ├── comparison_summary.csv           # Summary best/worst
│   ├── comparison_speedup.csv           # Analisis speedup
│   └── comparison_growth_rate.csv       # Verifikasi Big-O
├── graphs/
│   ├── grafik_search_algorithms.png
│   ├── grafik_sorting_random.png
│   ├── grafik_best_vs_worst.png
│   ├── grafik_growth_rate.png
│   └── grafik_speedup.png
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 atau lebih baru
python --version

# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter
```

### Clone Repository

```bash
git clone https://github.com/Dimassaputra5/SDA.git
cd SDA
```

---

## 📊 Cara Menggunakan

### 1️⃣ Generate Dataset & Testing

**Generate dataset dan jalankan testing untuk semua algoritma:**

```bash
cd src
python dataset-generator-fixed.py
```

**Output:**
- `results_search.csv` - Hasil testing Linear vs Binary Search (7 ukuran: 1K - 1M elemen)
- `results_sorting_sorting_random.csv` - Sorting dengan random data (6 ukuran: 100 - 10K)
- `results_sorting_sorting_sorted.csv` - Sorting dengan data already sorted (best case)
- `results_sorting_sorting_reverse.csv` - Sorting dengan data reverse (worst case)

**Data yang dikumpulkan:**
- Jumlah comparisons (operasi perbandingan)
- Execution time (detik)
- Input size (n)

---

### 2️⃣ Generate CSV Komparasi

**Buat 4 CSV file komparasi lengkap:**

```bash
python create-comparison-csv.py
```

**Output:**
1. **`comparison_all_algorithms.csv`** - Semua data dalam satu file
   - Columns: Algorithm, Data Type, Input Size, Comparisons, Time, Complexity Class, Notes

2. **`comparison_summary.csv`** - Ringkasan best vs worst performers
   - Columns: Category, Input Size, Fastest Algorithm, Slowest Algorithm, Speed Difference

3. **`comparison_speedup.csv`** - Analisis speedup & comparison reduction
   - Columns: Comparison, Input Size, Algorithm A/B, Time A/B, Speedup, Comparison Reduction %

4. **`comparison_growth_rate.csv`** - Verifikasi empiris Big-O
   - Columns: Algorithm, Size 1/2, Comparisons 1/2, Size Growth, Comparisons Growth, Matches Theory?

---

### 3️⃣ Generate Grafik Visualisasi

**Buat 5 grafik high-resolution (300 DPI):**

```bash
python visualisasi-grafik.py
```

**Output:**
1. `grafik_search_algorithms.png` - Linear vs Binary search (comparisons + time)
2. `grafik_sorting_random.png` - Bubble vs Insertion vs Merge (random data)
3. `grafik_best_vs_worst.png` - Best case vs worst case comparison (4 subplots)
4. `grafik_growth_rate.png` - Actual vs theoretical Big-O verification (4 subplots)
5. `grafik_speedup.png` - Bar charts speedup comparison

**Fitur grafik:**
- Log scale untuk better visualization
- Annotations & value labels
- Professional styling (seaborn)
- Ready untuk presentasi

---

### 4️⃣ Analisis Interaktif dengan Jupyter Notebook

**Buka notebook untuk analisis mendalam:**

```bash
jupyter notebook analysis-kompleksitas-algoritma.ipynb
```

**Isi Notebook:**

1. **Section 1: Data Lengkap** - Load & preview semua data, statistik deskriptif
2. **Section 2: Summary** - Best vs worst performers, speed difference analysis
3. **Section 3: Speedup Analysis** - Detail speedup trends & comparison reduction
4. **Section 4: Growth Rate** - Verifikasi Big-O dengan empirical data
5. **Section 5: Key Insights** - Automatic summary generation
6. **Section 6: Export** - Generate `analysis_summary.txt`

**Cara pakai:**
- Run cell by cell untuk melihat hasil
- Semua visualizations ditampilkan inline
- Export summary untuk presentasi

---

## 📈 Hasil Analisis

### Key Findings

#### Search Algorithms

**Binary Search vs Linear Search (n = 1,000,000):**
- Linear Search: 900,001 comparisons, 0.197 seconds
- Binary Search: 19 comparisons, 0.00002 seconds
- **Speedup: 8,647x lebih cepat!** 💨
- Comparison reduction: **99.998%**

✅ **Kesimpulan:** Binary Search (O(log n)) DRAMATICALLY faster untuk data besar

#### Sorting Algorithms (Random Data)

**Perbandingan (n = 10,000):**
- Bubble Sort: 49,993,230 comparisons, 10.35 seconds
- Insertion Sort: 25,039,111 comparisons, 4.38 seconds
- Merge Sort: 120,552 comparisons, 0.04 seconds

**Speedup Merge vs Bubble: 277x lebih cepat!** 🚀

✅ **Kesimpulan:** Merge Sort (O(n log n)) mendominasi untuk data besar

#### Best Case vs Worst Case

**Already Sorted (n = 50,000):**
- Bubble Sort: 0.008 seconds (O(n) dengan early exit)
- Insertion Sort: 0.012 seconds (O(n) optimal)
- Merge Sort: 0.135 seconds (tetap O(n log n))

✅ **Kesimpulan:** Bubble/Insertion excellent untuk nearly sorted data

**Reverse Sorted (n = 5,000):**
- Bubble Sort: 3.16 seconds
- Insertion Sort: 2.23 seconds
- Merge Sort: 0.01 seconds (unaffected!)

✅ **Kesimpulan:** Merge Sort KONSISTEN regardless of data order

---

## 📊 Complexity Summary

| Algorithm | Best Case | Average Case | Worst Case | Space | Notes |
|-----------|-----------|--------------|------------|----------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) | Unsorted data OK |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) | Requires sorted data |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Good for nearly sorted |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Adaptive, stable |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Consistent, stable |

---

## 🎯 Practical Recommendations

### Kapan Menggunakan Algoritma Tertentu?

**Small Data (n < 100):**
- ✅ Any algorithm works
- Pilih yang paling simple (Bubble/Insertion)

**Medium Data (100 < n < 1,000):**
- ✅ Insertion Sort reasonable
- ❌ Avoid Bubble Sort

**Large Data (n > 1,000):**
- ✅ **ALWAYS use O(n log n) algorithms** (Merge Sort, Quick Sort, Heap Sort)
- ❌ NEVER use O(n²) algorithms (Bubble, Insertion)

**Sorted/Nearly Sorted Data:**
- ✅ Insertion Sort optimal (O(n) with early exit)
- Alternative: Timsort (Python's default)

**Search in Sorted Data:**
- ✅ **ALWAYS use Binary Search**
- Linear Search hanya untuk unsorted data

**Unknown Data Distribution:**
- ✅ Default to Merge Sort (consistent O(n log n))
- No worst-case surprises

---

## 🔬 Growth Rate Verification

**Empirical validation bahwa actual growth matches theoretical Big-O:**

| Algorithm | Theoretical | Empirical Match | Verified |
|-----------|------------|----------------|----------|
| Linear Search | O(n) | Growth ≈ n | ✅ Yes |
| Binary Search | O(log n) | Growth ≈ log₂(n) | ✅ Yes |
| Bubble Sort | O(n²) | Growth ≈ n² | ✅ Yes |
| Insertion Sort | O(n²) | Growth ≈ n² | ✅ Yes |
| Merge Sort | O(n log n) | Growth ≈ n log n | ✅ Yes |

**Method:** Mengukur ratio pertumbuhan operasi ketika input size naik 2x, 5x, 10x dan membandingkan dengan expected theoretical growth.

---

## 📚 File Documentation

### Python Scripts

**`dataset-generator-fixed.py`**
- Generate datasets dalam 4 tipe: random, sorted, reverse, nearly sorted
- Test 5 algoritma dengan berbagai ukuran input
- Export results ke 4 CSV files
- Runtime: ~3-5 menit (tergantung hardware)

**`create-comparison-csv.py`**
- Baca 4 CSV results
- Generate 4 CSV komparasi dengan metrics berbeda
- Automatic calculation: speedup, reduction %, growth rate
- Includes theoretical vs actual comparison

**`visualisasi-grafik.py`**
- Generate 5 professional graphs (300 DPI)
- Matplotlib + Seaborn styling
- Log scale visualization
- Annotations & value labels

**`algorithm-complexity-complete.py`**
- Standalone script dengan semua 5 algoritma
- Include docstrings & type hints
- Benchmark functions
- Demo program

### CSV Files

**Results Files (dari testing):**
- Raw data: comparisons, time, input size
- Different data types: random, sorted, reverse

**Comparison Files (processed):**
- Aggregated analysis
- Speedup calculations
- Growth rate verification
- Summary statistics

### Jupyter Notebook

**`analysis-kompleksitas-algoritma.ipynb`**
- 6 sections dengan 12+ visualizations
- Interactive data exploration
- Pandas aggregations & statistics
- Export capability ke text file
- Ready untuk presentasi

---

## 🎓 Penggunaan untuk Akademik

### Presentasi Kelompok

**Materials yang tersedia:**
1. ✅ High-res graphs (300 DPI) - ready untuk slides
2. ✅ CSV data - import ke Excel/Google Sheets
3. ✅ Summary statistics - key insights untuk narasi
4. ✅ Jupyter Notebook - live demo
5. ✅ Growth rate verification - proof empiris Big-O

**Recommended Flow:**
1. Intro: Tujuan & algoritma yang dianalisis
2. Methodology: Cara testing & metrics yang diukur
3. Results: Tunjukkan grafik comparisons & time
4. Analysis: Speedup, comparison reduction, growth rate
5. Conclusion: Practical recommendations

### Laporan Tertulis

**Section yang bisa dimasukkan:**
- Abstract: Key findings summary
- Methodology: Dataset generation & testing procedure
- Results: Tables & graphs dari CSV
- Discussion: Analysis speedup & growth rate
- Conclusion: Practical recommendations
- Appendix: Source code & raw data

**Tables untuk laporan:**
- Complexity summary table
- Results comparison table (dari CSV)
- Growth rate verification table
- Speedup analysis table

---

## 🛠️ Troubleshooting

**Error: Module not found**
```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter
```

**Error: Unicode encoding (Windows)**
- Sudah fixed di `dataset-generator-fixed.py`
- Menggunakan ASCII characters instead of box drawing

**Grafik tidak muncul di Jupyter**
```python
# Add ini di cell pertama
%matplotlib inline
```

**CSV file not found saat visualisasi**
```bash
# Pastikan menjalankan dataset-generator dulu
python dataset-generator-fixed.py
```

**Memory error untuk dataset besar**
- Reduce ukuran dataset di `dataset-generator-fixed.py`
- Comment out largest sizes (500K, 1M)

---

## 📝 License

MIT License - Free untuk digunakan untuk keperluan akademik dan penelitian.

---

## 👤 Author

**Dimas Saputra**
- GitHub: [@Dimassaputra5](https://github.com/Dimassaputra5)
- Repository: [SDA - Algorithm Complexity Analysis](https://github.com/Dimassaputra5/SDA)

---

## 🙏 Acknowledgments

- Mata kuliah Struktur Data & Algoritma
- Python community untuk libraries yang powerful
- Contributors yang memberikan feedback

---

## 📮 Contact & Support

Jika ada pertanyaan atau issue:
1. Buka [GitHub Issues](https://github.com/Dimassaputra5/SDA/issues)
2. Email: dimassaputrq96@gmail.com

---

**⭐ Star repository ini jika bermanfaat untuk project kalian!**

---

*Last Updated: November 22, 2025*