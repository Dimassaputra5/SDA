# Dokumentasi Empiris BigOAnalyzer

## Deskripsi Singkat
BigOAnalyzer adalah class Python untuk **menghitung dan mengestimasi empiris kompleksitas waktu algoritma (Big O Notation)**. Tool ini melakukan eksperimen pada fungsi target dengan berbagai ukuran input dan membandingkan waktu eksekusinya ke model-model teoritis (O(1), O(log n), O(n), O(n log n), O(n²), O(n³)).

---

## Alur Algoritma Secara Detail

### 1. Inisialisasi dan Parameter
Saat objek dibuat:
- `min_n`: Ukuran input paling kecil untuk eksperimen
- `max_n`: Ukuran input paling besar
- `multiplier`: Pengali agar ukuran input naik eksponensial (n, 2n, 4n,...)
- `repeats`: Berapa kali pengukuran per ukuran agar hasil rata-rata

### 2. Pengumpulan Data (`collect_data`)
- Melakukan iterasi dari `min_n` hingga `max_n`.
- Untuk tiap ukuran input `n`, panggil fungsi target sebanyak `repeats` kali dan catat waktu eksekusi (dalam detik).
- Rata-ratakan waktu eksekusi untuk tiap `n`, simpan pasangan `(n, avg_time)` ke array measurements.
- Hasil akhirnya: array 2 kolom [n, avg_time] untuk dievaluasi ke tahap berikutnya.

#### Contoh Manual
Misal ingin analisis fungsi linear_search dengan input [100, 200, 400]:
- Generate data 100 elemen → uji fungsi 3x → ambil rata-rata waktu → simpan (100, avg1)
- Generate data 200 elemen → ulangi proses
- Generate data 400 elemen → ulangi proses

### 3. Pengukuran Waktu (
`_measure_time, _measure_time_with_args`)
- Mengukur waktu eksekusi aktual, memakai time.perf_counter untuk presisi.
- Jika fungsi target memerlukan single parameter, gunakan `_measure_time`.
- Jika multi-parameter, gunakan `_measure_time_with_args` (fungsi dan argumen tuple).

### 4. Fitting Model Teoritis (`_fit_model`)
- Setiap kelas Big O memiliki "teoritis x":
  - O(1): konstanta
  - O(log n): log(n)
  - O(n): n
  - O(n log n): n*log(n)
  - O(n²): n²
  - O(n³): n³
- Lakukan fitting regresi linear ke data `(teoritis value, empirical time)` → dapat slope, intercept, dan R² (coefficient of determination).
  - R² = seberapa kuat model memprediksi data nyata (semakin mendekati 1, fit semakin bagus)

### 5. Analisis Tiap Kelas Big O (`analyze_O1`, ...)
- Untuk setiap O-class, hitung teoritis value untuk semua n, fitting ke time values.
- Simpan class, r_squared ke hasil.

### 6. Pencarian Best-Fit dan Ranking (`analyze_all`)
- Jalankan semua analisis O-class.
- Urutkan berdasarkan R².
- Berikan hasil best-fit dan confidence score sekaligus ranking lengkap serta semua data pengukuran.

---

## Manual Step-by-Step Simulasi (dengan Contoh Sederhana)

Misal ingin menguji fungsi bubble_sort:
1. Pilih parameter eksperimen: min_n=100, max_n=400, multiplier=2, repeats=3.
2. Untuk n=100, n=200, n=400:
   - Generate random array ukuran n.
   - Jalankan bubble_sort, catat waktu eksekusi tiga kali, ambil rata-rata.
   - Simpan tuple (n, avg_time).
3. Untuk seluruh daftar hasil, uji ke semua model O-class.
4. Nilai fit terbaik (R² tertinggi) jadi output, misal O(n²) dengan confidence 0.997.

---

## Output dan Visualisasi
- Kelas/notation terbaik dan confidence ditampilkan.
- Tabel pengukuran raw beserta ranking seluruh kelas rata-rata.

---

## Kesimpulan
BigOAnalyzer memungkinkan analisis Big O algoritma berdasar eksperimen nyata dengan mudah, otomatis, dan confidence score yang informatif.

---

## Referensi Kode
Terinspirasi dan diadaptasi dari kode di attachment file: `BigOcomplexity.py`.
