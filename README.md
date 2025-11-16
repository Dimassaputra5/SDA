# Dokumentasi Repository SDA - Analisis Kompleksitas Algoritma

## Ringkasan

Repository SDA ini berisi implementasi berbagai algoritma pencarian dan pengurutan (sorting) dalam Python, lengkap dengan sistem analisis Big O complexity berbasis pengukuran waktu eksekusi secara empiris.

## Struktur Repository
- **Main.py** — eksekusi utama analisis
- **BinarySearch.py** — algoritma Binary Search
- **LinearSearch.py** — algoritma Linear Search
- **InsertionSort.py** — algoritma Insertion Sort
- **BubbleSort.py** — algoritma Bubble Sort
- **MergeSort.py** — prosedur penggabungan dua array terurut
- **BigOcomplexity.py** — framework analisis kompleksitas Big O

---

## Penjelasan Algoritma & Langkah Manual

### Binary Search (Pencarian Biner)
**Deskripsi**: Mencari elemen di array terurut dengan divide-and-conquer.

**Kompleksitas**:
- Time: \( O(\log n) \)
- Space: \( O(1) \)

**Langkah Manual**
1. Inisialisasi `L=0`, `R=n-1`
2. Selama `L <= R`, ambil indeks tengah `m = L + floor((R-L)/2)`
3. Jika `A[m] < T`: geser kiri ke kanan, jika `A[m] > T` geser kanan ke kiri, else return indeks.

**Pseudocode**
```python
BINARY_SEARCH(A, n, T):
    L = 0
    R = n - 1
    while L <= R:
        m = L + (R - L) // 2
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m
    return -1
```

---

### Linear Search (Pencarian Linear)
**Deskripsi**: Mencari elemen di array dengan memeriksa satu per satu.

**Kompleksitas**:
- Time: \( O(n) \)
- Space: \( O(1) \)

**Pseudocode**
```python
LINEAR_SEARCH(A, n, T):
    for i in range(n):
        if A[i] == T:
            return i
    return -1
```

---

### Insertion Sort
**Deskripsi**: Pengurutan dengan menyisipkan tiap elemen ke posisi yang tepat.

**Kompleksitas**:
- Time: Best \( O(n) \), Worst/Average \( O(n^2) \)
- Space: \( O(1) \)

**Pseudocode**
```python
INSERTION_SORT(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A
```

---

### Bubble Sort
**Deskripsi**: Sorting dengan menukar elemen berulang-ulang hingga terurut.

**Kompleksitas**:
- Time: \( O(n^2) \)
- Space: \( O(1) \)

**Pseudocode**
```python
BUBBLE_SORT(A, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A
```

---

### Merge (Gabung Array Terurut)
**Deskripsi**: Menggabungkan 2 array terurut ke satu array baru.

**Kompleksitas**:
- Time: \( O(m + n) \)
- Space: \( O(m + n) \)

**Pseudocode**
```python
MERGE(A, m, B, n):
    result = []
    i, j = 0, 0
    while i < m and j < n:
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    result.extend(A[i:m])
    result.extend(B[j:n])
    return result
```

---

## Cara Menjalankan

### Persyaratan
- Python 3.8+
- Install dependency:

```bash
pip install numpy pandas
```

### Jalankan Analisis

Clone repository dan jalankan file utama:
```bash
git clone https://github.com/Dimassaputra5/SDA.git
cd SDA
python Main.py
```

Hasil analisis performa dan kompleksitas algoritma akan muncul langsung di terminal berupa ranking hasil fit Big O, statistik waktu eksekusi, dan pengukuran sample.

**Catatan:**
- Tidak perlu mengedit modul *.py, seluruh proses terotomatisasi lewat Main.py
- Minimal requirements: Python versi 3.8 atau lebih baru
- Jika error module, pastikan dependency terpasang dengan benar
- Untuk logika detail lihat README atau source masing-masing file.

---

## Ringkasan Kompleksitas
| Algoritma        | Time Complexity | Space Complexity | Keterangan                      |
|------------------|----------------|------------------|----------------------------------|
| Binary Search    | O(log n)       | O(1)             | Data terurut                     |
| Linear Search    | O(n)           | O(1)             | Data acak                        |
| Insertion Sort   | O(n^2)         | O(1)             | Efisien untuk data kecil         |
| Bubble Sort      | O(n^2)         | O(1)             | Sederhana, lambat untuk data besar|
| Merge (2 arrays) | O(m+n)         | O(m+n)           | Gabung dua array terurut         |

---

## Framework Analisis Big O
**BigOAnalyzer** akan secara otomatis menguji runtime empiris algoritma pada berbagai skala input, membandingkan against model teoritis (O(1), O(log n), O(n), O(n log n), O(n^2), O(n^3)) dan membandingkan kecocokan dengan menggunakan regresi linear dan skor R².

Outputnya berupa ranking kompleksitas terbaik beserta confidence score, hasil pengukuran, dan detail statistik pada console.
