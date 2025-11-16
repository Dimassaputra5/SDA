# Dokumentasi Repository SDA - Analisis Kompleksitas Algoritma

## Ringkasan

Repository SDA ini berisi implementasi berbagai algoritma pencarian dan pengurutan (sorting) dalam Python, dilengkapi dengan sistem analisis empiris untuk menghitung Big O complexity secara otomatis. Repository ini menggunakan pendekatan pengukuran waktu eksekusi untuk memverifikasi kompleksitas teoretis dari setiap algoritma.

## Struktur Repository

Repository ini terdiri dari 7 file Python utama:

1. **Main.py** - File utama untuk menjalankan semua analisis
2. **BinarySearch.py** - Implementasi algoritma Binary Search
3. **LinearSearch.py** - Implementasi algoritma Linear Search
4. **InsertionSort.py** - Implementasi algoritma Insertion Sort
5. **BubbleSort.py** - Implementasi algoritma Bubble Sort
6. **MergeSort.py** - Implementasi algoritma Merge (penggabungan dua array terurut)
7. **BigOcomplexity.py** - Framework analisis kompleksitas algoritma

---

## Penjelasan Detail Setiap Algoritma

### 1. Binary Search (Pencarian Biner)

#### Deskripsi
Binary Search adalah algoritma pencarian yang efisien untuk mencari elemen dalam array yang sudah terurut. Algoritma ini menggunakan strategi divide-and-conquer dengan membagi ruang pencarian menjadi dua bagian pada setiap iterasi.

#### Kompleksitas
- **Time Complexity**: \(O(\log n)\)
- **Space Complexity**: \(O(1)\)

#### Langkah-Langkah Manual

**Input**: Array terurut `A = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67]`, Target `T = 23`

**Langkah 1**: Inisialisasi pointer
- `L = 0` (pointer kiri)
- `R = 9` (pointer kanan, n-1)
- `n = 10` (ukuran array)

**Langkah 2**: Iterasi 1
- Hitung index tengah: \(m = L + \lfloor\frac{R-L}{2}\rfloor = 0 + \lfloor\frac{9-0}{2}\rfloor = 4\)
- Nilai tengah: `A[4] = 16`
- Perbandingan: `16 < 23`, maka target ada di sebelah kanan
- Update: `L = m + 1 = 5`

**Langkah 3**: Iterasi 2
- `L = 5, R = 9`
- Hitung index tengah: \(m = 5 + \lfloor\frac{9-5}{2}\rfloor = 7\)
- Nilai tengah: `A[7] = 45`
- Perbandingan: `45 > 23`, maka target ada di sebelah kiri
- Update: `R = m - 1 = 6`

**Langkah 4**: Iterasi 3
- `L = 5, R = 6`
- Hitung index tengah: \(m = 5 + \lfloor\frac{6-5}{2}\rfloor = 5\)
- Nilai tengah: `A[5] = 23`
- Perbandingan: `A[5] == 23`, **DITEMUKAN!**
- Return: `m = 5`

**Hasil**: Elemen 23 ditemukan pada index 5

#### Pseudocode
```
BINARY_SEARCH(A, n, T)
    L ← 0
    R ← n - 1
    
    WHILE L ≤ R DO
        m ← L + floor((R - L) / 2)
        
        IF A[m] < T THEN
            L ← m + 1
        ELSE IF A[m] > T THEN
            R ← m - 1
        ELSE
            RETURN m
    END WHILE
    
    RETURN -1  // tidak ditemukan
```

---

### 2. Linear Search (Pencarian Linear)

#### Deskripsi
Linear Search adalah algoritma pencarian paling sederhana yang memeriksa setiap elemen dalam array secara berurutan dari awal hingga akhir sampai menemukan target atau mencapai akhir array.

#### Kompleksitas
- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)

#### Langkah-Langkah Manual

**Input**: Array `A = [34, 7, 23, 32, 5, 62, 23, 14]`, Target `T = 23`

**Langkah 1**: Inisialisasi
- `n = 8` (ukuran array)
- `i = 0` (index mulai dari 0)

**Langkah 2**: Iterasi 1
- Periksa `A[0] = 34`
- Perbandingan: `34 == 23`? **TIDAK**
- Lanjut ke index berikutnya: `i = 1`

**Langkah 3**: Iterasi 2
- Periksa `A[1] = 7`
- Perbandingan: `7 == 23`? **TIDAK**
- Lanjut: `i = 2`

**Langkah 4**: Iterasi 3
- Periksa `A[2] = 23`
- Perbandingan: `23 == 23`? **YA!**
- Return: `i = 2`

**Hasil**: Elemen 23 ditemukan pada index 2

#### Pseudocode
```
LINEAR_SEARCH(A, n, T)
    FOR i ← 0 TO n-1 DO
        IF A[i] == T THEN
            RETURN i
    END FOR
    
    RETURN -1  // tidak ditemukan
```

---

### 3. Insertion Sort (Pengurutan Sisipan)

#### Deskripsi
Insertion Sort adalah algoritma sorting yang membangun array terurut secara bertahap dengan menyisipkan satu elemen pada satu waktu ke posisi yang tepat. Mirip seperti cara kita mengurutkan kartu di tangan.

#### Kompleksitas
- **Time Complexity**: 
  - Best Case: \(O(n)\) - sudah terurut
  - Average/Worst Case: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)

#### Langkah-Langkah Manual

**Input**: Array `A = [12, 11, 13, 5, 6]`

**Langkah 1**: Mulai dari index 1
- Array: `[12, 11, 13, 5, 6]`
- `key = A[1] = 11`
- `j = 0`
- Bandingkan: `A[0] = 12 > 11`? **YA**
- Geser 12 ke kanan: `A[1] = 12`
- Sisipkan key: `A[0] = 11`
- Hasil: `[11, 12, 13, 5, 6]`

**Langkah 2**: Index 2
- `key = A[2] = 13`
- `j = 1`
- Bandingkan: `A[1] = 12 > 13`? **TIDAK**
- 13 sudah di posisi yang benar
- Hasil: `[11, 12, 13, 5, 6]`

**Langkah 3**: Index 3
- `key = A[3] = 5`
- `j = 2`
- Bandingkan: `A[2] = 13 > 5`? **YA** → Geser: `A[3] = 13`
- `j = 1`
- Bandingkan: `A[1] = 12 > 5`? **YA** → Geser: `A[2] = 12`
- `j = 0`
- Bandingkan: `A[0] = 11 > 5`? **YA** → Geser: `A[1] = 11`
- `j = -1` (berhenti)
- Sisipkan key: `A[0] = 5`
- Hasil: `[5, 11, 12, 13, 6]`

**Langkah 4**: Index 4
- `key = A[4] = 6`
- Proses serupa, geser 13, 12, 11
- Sisipkan 6 setelah 5
- Hasil: `[5, 6, 11, 12, 13]` ✓

#### Pseudocode
```
INSERTION_SORT(A, n)
    FOR i ← 1 TO n-1 DO
        key ← A[i]
        j ← i - 1
        
        WHILE j ≥ 0 AND A[j] > key DO
            A[j + 1] ← A[j]
            j ← j - 1
        END WHILE
        
        A[j + 1] ← key
    END FOR
    
    RETURN A
```

---

### 4. Bubble Sort (Pengurutan Gelembung)

#### Deskripsi
Bubble Sort adalah algoritma sorting sederhana yang bekerja dengan menukar elemen-elemen yang bersebelahan jika urutannya salah. Proses ini diulang hingga tidak ada lagi pertukaran yang diperlukan.

#### Kompleksitas
- **Time Complexity**: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)

#### Langkah-Langkah Manual

**Input**: Array `A = [64, 34, 25, 12, 22]`

**Pass 1** (i=0):
- Bandingkan `64` dan `34`: 64 > 34 → **TUKAR** → `[34, 64, 25, 12, 22]`
- Bandingkan `64` dan `25`: 64 > 25 → **TUKAR** → `[34, 25, 64, 12, 22]`
- Bandingkan `64` dan `12`: 64 > 12 → **TUKAR** → `[34, 25, 12, 64, 22]`
- Bandingkan `64` dan `22`: 64 > 22 → **TUKAR** → `[34, 25, 12, 22, 64]`
- Elemen terbesar (64) sudah di posisi akhir

**Pass 2** (i=1):
- Bandingkan `34` dan `25`: 34 > 25 → **TUKAR** → `[25, 34, 12, 22, 64]`
- Bandingkan `34` dan `12`: 34 > 12 → **TUKAR** → `[25, 12, 34, 22, 64]`
- Bandingkan `34` dan `22`: 34 > 22 → **TUKAR** → `[25, 12, 22, 34, 64]`
- Elemen terbesar kedua (34) sudah di posisi

**Pass 3** (i=2):
- Bandingkan `25` dan `12`: 25 > 12 → **TUKAR** → `[12, 25, 22, 34, 64]`
- Bandingkan `25` dan `22`: 25 > 22 → **TUKAR** → `[12, 22, 25, 34, 64]`

**Pass 4** (i=3):
- Bandingkan `12` dan `22`: 12 < 22 → **TIDAK TUKAR** → `[12, 22, 25, 34, 64]`

**Hasil**: Array terurut `[12, 22, 25, 34, 64]` ✓

#### Pseudocode
```
BUBBLE_SORT(A, n)
    FOR i ← 0 TO n-1 DO
        FOR j ← 0 TO n-i-2 DO
            IF A[j] > A[j+1] THEN
                SWAP(A[j], A[j+1])
            END IF
        END FOR
    END FOR
    
    RETURN A
```

---

### 5. Merge Sort (Penggabungan Array Terurut)

#### Deskripsi
Implementasi ini adalah operasi Merge dari algoritma Merge Sort - menggabungkan dua array yang sudah terurut menjadi satu array terurut. Ini adalah bagian "Combine" dari strategi divide-and-conquer.

#### Kompleksitas
- **Time Complexity**: \(O(m + n)\) dimana m dan n adalah ukuran kedua array
- **Space Complexity**: \(O(m + n)\)

#### Langkah-Langkah Manual

**Input**: 
- Array A (terurut): `[1, 3, 5, 7]` dengan `m = 4`
- Array B (terurut): `[2, 4, 6, 8]` dengan `n = 4`

**Inisialisasi**:
- `result = []` (array hasil)
- `i = 0` (pointer untuk A)
- `j = 0` (pointer untuk B)

**Langkah 1**: Bandingkan A[0] dan B[0]
- `A[0] = 1` vs `B[0] = 2`
- `1 ≤ 2` → Ambil dari A
- `result = [1]`, `i = 1`, `j = 0`

**Langkah 2**: Bandingkan A[1] dan B[0]
- `A[1] = 3` vs `B[0] = 2`
- `3 > 2` → Ambil dari B
- `result = [1, 2]`, `i = 1`, `j = 1`

**Langkah 3**: Bandingkan A[1] dan B[1]
- `A[1] = 3` vs `B[1] = 4`
- `3 ≤ 4` → Ambil dari A
- `result = [1, 2, 3]`, `i = 2`, `j = 1`

**Langkah 4**: Bandingkan A[2] dan B[1]
- `A[2] = 5` vs `B[1] = 4`
- `5 > 4` → Ambil dari B
- `result = [1, 2, 3, 4]`, `i = 2`, `j = 2`

**Langkah 5**: Bandingkan A[2] dan B[2]
- `A[2] = 5` vs `B[2] = 6`
- `5 ≤ 6` → Ambil dari A
- `result = [1, 2, 3, 4, 5]`, `i = 3`, `j = 2`

**Langkah 6**: Bandingkan A[3] dan B[2]
- `A[3] = 7` vs `B[2] = 6`
- `7 > 6` → Ambil dari B
- `result = [1, 2, 3, 4, 5, 6]`, `i = 3`, `j = 3`

**Langkah 7**: Bandingkan A[3] dan B[3]
- `A[3] = 7` vs `B[3] = 8`
- `7 ≤ 8` → Ambil dari A
- `result = [1, 2, 3, 4, 5, 6, 7]`, `i = 4`, `j = 3`

**Langkah 8**: Array A habis (i = m)
- Tambahkan sisa B: `B[3] = 8`
- `result = [1, 2, 3, 4, 5, 6, 7, 8]`

**Hasil**: Array gabungan terurut `[1, 2, 3, 4, 5, 6, 7, 8]` ✓

#### Pseudocode
```
MERGE(A, m, B, n)
    result ← []
    i ← 0
    j ← 0
    
    WHILE i < m AND j < n DO
        IF A[i] ≤ B[j] THEN
            APPEND A[i] TO result
            i ← i + 1
        ELSE
            APPEND B[j] TO result
            j ← j + 1
        END IF
    END WHILE
    
    // Tambahkan sisa elemen dari A atau B
    APPEND A[i:m] TO result
    APPEND B[j:n] TO result
    
    RETURN result
```

---

## Framework Analisis Big O (BigOcomplexity.py)

### Deskripsi
`BigOAnalyzer` adalah framework untuk menganalisis kompleksitas algoritma secara empiris dengan mengukur waktu eksekusi pada berbagai ukuran input dan mencocokkannya dengan fungsi kompleksitas teoretis.

### Metode Analisis

Framework ini menguji 6 kelas kompleksitas:

1. **O(1)** - Constant Time
2. **O(log n)** - Logarithmic
3. **O(n)** - Linear
4. **O(n log n)** - Linearithmic
5. **O(n²)** - Quadratic
6. **O(n³)** - Cubic

### Cara Kerja

#### Langkah 1: Pengumpulan Data
```python
n_values = [100, 200, 400, 800, 1600, 3200, 6400]
```
Untuk setiap nilai n:
- Generate data uji sebanyak `repeats` kali (default 3-5)
- Ukur waktu eksekusi
- Hitung rata-rata waktu

#### Langkah 2: Fitting Model
Untuk setiap kelas kompleksitas, hitung:

\[
\text{time} = a \times f(n) + b
\]

Dimana:
- \(f(n)\) adalah fungsi teoretis (contoh: \(n^2\) untuk O(n²))
- \(a\) dan \(b\) adalah koefisien yang di-fit menggunakan regresi linear
- Hitung \(R^2\) (coefficient of determination) untuk mengukur kecocokan

#### Langkah 3: Ranking
Urutkan hasil berdasarkan nilai \(R^2\) tertinggi. \(R^2\) mendekati 1.0 menunjukkan kecocokan yang sangat baik.

### Contoh Output
```
======================================================================
ANALYZING: BinarySearch(A, n, T)
======================================================================

[BEST FIT]: O(log n)
[CONFIDENCE (R^2)]: 0.987654

[RANKING]:
----------------------------------------------------------------------
[1] O(log n)    [####################################------] 0.9877
[2] O(1)        [#####################-----------------] 0.5234
[3] O(n)        [##########----------------------------] 0.2512
[4] O(n log n)  [#####---------------------------------] 0.1234
[5] O(n^2)      [##------------------------------------] 0.0456
[6] O(n^3)      [--------------------------------------] 0.0012

[MEASUREMENTS]:
----------------------------------------------------------------------
n          Time (us)      
100        0.0012         
200        0.0014         
400        0.0016         
800        0.0018         
1600       0.0020         
======================================================================
```

---

## Cara Menjalankan

### Persyaratan
```bash
pip install numpy pandas
```

### Eksekusi
```bash
python Main.py
```
Program akan secara otomatis:
1. Menjalankan analisis untuk Binary Search
2. Menjalankan analisis untuk Linear Search
3. Menjalankan analisis untuk Insertion Sort
4. Menjalankan analisis untuk Bubble Sort
5. Menjalankan analisis untuk Merge Sort

Setiap analisis akan menampilkan:
- Kelas kompleksitas terbaik yang cocok
- Confidence score (R²)
- Ranking semua kelas kompleksitas
- Sample measurements

---

## Ringkasan Kompleksitas

| Algoritma | Time Complexity | Space Complexity | Keterangan |
|-----------|----------------|------------------|------------|
| Binary Search | \(O(\log n)\) | \(O(1)\) | Memerlukan array terurut |
| Linear Search | \(O(n)\) | \(O(1)\) | Bekerja pada array tidak terurut |
| Insertion Sort | \(O(n^2)\) | \(O(1)\) | Efisien untuk data kecil/hampir terurut |
| Bubble Sort | \(O(n^2)\) | \(O(1)\) | Sederhana namun tidak efisien |
| Merge (2 arrays) | \(O(m+n)\) | \(O(m+n)\) | Menggabungkan 2 array terurut |

---

## Konsep Penting

### Big O Notation
Big O menggambarkan batas atas pertumbuhan waktu eksekusi algoritma relatif terhadap ukuran input. Ini membantu kita memahami bagaimana performa algoritma akan berubah ketika data bertambah besar.

### Empirical Analysis
Pendekatan empiris mengukur waktu eksekusi aktual dan mencocokkannya dengan fungsi teoretis menggunakan regresi linear dan \(R^2\) score untuk validasi.

### Trade-offs
- **Binary Search** cepat tapi butuh data terurut
- **Linear Search** lambat tapi bekerja pada data tidak terurut
- **Insertion Sort** baik untuk data kecil/hampir terurut
- **Bubble Sort** sederhana tapi sangat lambat untuk data besar
