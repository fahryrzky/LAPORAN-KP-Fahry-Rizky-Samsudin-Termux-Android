# Rencana Implementasi: Kompilasi LaTeX Laporan KP ke `/storage/emulated/0/laporan kp`

## Deskripsi Tujuan
Mengompilasi naskah modular LaTeX Laporan KP Fahry Rizky Samsudin (68 halaman) menjadi berkas PDF utuh menggunakan kompiler ringan **Tectonic**, menyematkan tanda tangan pembimbing dan stempel resmi secara proporsional di Lembar Persetujuan, membuat direktori baru `/storage/emulated/0/laporan kp` di penyimpanan internal HP, serta menyalin berkas PDF hasil kompilasi ke folder tersebut agar dapat langsung dibuka dan dilihat oleh pengguna.

---

## User Review Required

> [!IMPORTANT]
> **Penyematan Dua Tanda Tangan Pembimbing Resmi:**
> Dikonfirmasi terdapat **2 tanda tangan pembimbing** pada Lembar Persetujuan:
> 1. **Pembimbing I**: Dr. Moch Nurul Subkhi, M.Si (`ttd_pembimbing1_subkhi.png`)
> 2. **Pembimbing II**: Dr. Emmanuel Agung N, S.T, M.T. (`ttd_pembimbing2_agung.png`)
>
> Keduanya akan disematkan secara proporsional dan sejajar di atas nama masing-masing pembimbing pada `Header/persetujuan.tex`.
>
> Untuk menjaga **keamanan**, seluruh berkas tanda tangan (`Gambar/ttd_*.png`) dimasukkan ke dalam `.gitignore` agar tidak bisa terunggah ke repositori publik daring.

> [!NOTE]
> **Lokasi Penyimpanan PDF Hasil Kompilasi:**
> Direktori target di penyimpanan internal HP:
> - Path Android: `/storage/emulated/0/laporan kp/`
> - Path Termux: [`/data/data/com.termux/files/home/storage/shared/laporan kp/`](file:///data/data/com.termux/files/home/storage/shared)
> - Nama file output: `Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf`

---

## Open Questions
Tidak ada pertanyaan pemblokir (*blocking questions*). Tectonic sudah terverifikasi siap pakai dan jalur penyimpanan bersama telah dipetakan.

---

## Rencana Perubahan (Proposed Changes)

```
LAPORAN-KP-Fahry-Rizky-Samsudin/
├── .gitignore                  # [NEW] Mengamankan tanda tangan dan stempel dari Git
├── Header/persetujuan.tex      # [MODIFY] Menyematkan tanda tangan pembimbing & cap stempel
├── compile.sh                  # [NEW] Skrip eksekusi kompilasi otomatis berbasis Tectonic
└── /storage/emulated/0/laporan kp/
    └── Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf # [NEW] Berkas PDF akhir di HP
```

---

### Tahap 1: Pengamanan Git & Pembaruan Lembar Persetujuan
#### [NEW] `.gitignore`
* Menambahkan aturan proteksi data sensitif:
  ```gitignore
  Gambar/ttd_*.png
  Gambar/stempel_*.png
  *.aux
  *.log
  *.out
  ```

#### [MODIFY] `Header/persetujuan.tex`
* Menyematkan objek tanda tangan `ttd_pembimbing.png` dan `stempel_pengesahan.png` di atas kolom Pembimbing I (Dr. Moch Nurul Subkhi, M.Si) menggunakan layer koordinat TikZ agar proporsinya rapi dan tidak menggeser kolom Pembimbing II.

---

### Tahap 2: Eksekusi Kompilasi LaTeX via Tectonic
* Menjalankan perintah:
  ```bash
  cd /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin
  tectonic -c minimal main.tex
  ```
* Tectonic akan memproses seluruh bab (Bab I–VI), me-resolve sitasi `references.bib`, merender diagram alir TikZ, tabel, dan persamaan kinematika menjadi `main.pdf`.

---

### Tahap 3: Pembuatan Folder & Penyalinan PDF ke Shared Storage
* Membuat direktori tujuan jika belum ada:
  ```bash
  mkdir -p "/storage/emulated/0/laporan kp"
  ```
* Menyalin PDF hasil kompilasi:
  ```bash
  cp main.pdf "/storage/emulated/0/laporan kp/Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf"
  ```

---

## Verification Plan

### Automated Tests
1. **Verifikasi Keberadaan PDF Hasil Kompilasi**:
   ```bash
   test -f /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/main.pdf
   ```
2. **Verifikasi Salinan di Shared Storage**:
   ```bash
   ls -la "/storage/emulated/0/laporan kp/Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf"
   ```
3. **Verifikasi Jumlah Halaman & Ukuran Berkas**:
   - Memastikan PDF memiliki jumlah halaman lengkap (68 halaman) dan ukuran berkas wajar ($> 2$ MB).

### Manual Verification
1. Buka aplikasi **File Manager** bawaan HP Android atau aplikasi pembaca PDF (Google PDF Viewer, WPS, dll.).
2. Masuk ke folder **Penyimpanan Internal > `laporan kp`**.
3. Buka berkas `Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf` dan periksa:
   - Halaman judul (Cover)
   - Lembar Persetujuan (apakah tanda tangan dan cap stempel terlihat rapi)
   - Diagram alir Bab IV dan Bab V
   - Lampiran kode program dan foto eksperimen.
