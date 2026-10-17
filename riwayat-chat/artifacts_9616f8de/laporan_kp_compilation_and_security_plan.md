# Rencana Implementasi: Kompilasi Dokumen LaTeX Laporan KP & Analisis Keamanan Tanda Tangan

## Deskripsi Tujuan
Pengguna meminta untuk:
1. **Mengompilasi naskah LaTeX Laporan KP** menjadi berkas PDF agar dapat dilihat (*preview*) langsung di perangkat HP.
2. **Menganalisis aspek keamanan tanda tangan** (*signature security & privacy*): Menjawab apakah tanda tangan dan stempel resmi yang ada di dokumen tersebut aman, serta bagaimana cara mengamankannya agar tidak disalahgunakan.

---

## User Review Required

> [!IMPORTANT]
> **Analisis Keamanan Tanda Tangan & Stempel Resmi Kampus:**
> Di dalam folder [`Gambar/`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Gambar) terdapat 2 file otentikasi resmi yang diekstrak dari PDF:
> - `ttd_pembimbing.png` (Tanda tangan Dr. Moch Nurul Subkhi, M.Si)
> - `stempel_pengesahan.png` (Stempel resmi Jurusan Fisika / Fakultas Sains & Teknologi UIN SGD)
>
> **Apakah Aman?**
> 1. **Penyimpanan Lokal di HP (Termux):** **SANGAT AMAN**. File berada di memori internal privat Termux yang terisolasi dari aplikasi lain (*sandbox* Android).
> 2. **Jika Diunggah ke GitHub Publik:** **TIDAK AMAN**. Tanda tangan dosen dan stempel resmi universitas adalah data sensitif. Jika repositori dibuat *Public* di GitHub, tanda tangan ini bisa diunduh dan dipalsukan oleh pihak luar untuk dokumen akademik/keuangan lainnya.
>
> **Rekomendasi Proteksi Otomatis:**
> - Menambahkan `Gambar/ttd_*.png` dan `Gambar/stempel_*.png` ke dalam `.gitignore` agar tidak bisa terunggah ke repositori daring.
> - Menyediakan opsi konfigurasi di LaTeX: dokumen bisa dikompilasi dengan tanda tangan digital (untuk arsip pribadi) ATAU tanpa tanda tangan (kotak kosong untuk cetak tanda tangan basah resmi).

> [!NOTE]
> **Penyimpanan & Pemilihan Kompiler LaTeX:**
> Sisa memori internal perangkat adalah **1.6 GB**. Menginstal TeX Live penuh (~3–4 GB) sangat berisiko membuat memori HP penuh.
> Oleh karena itu, kita akan menggunakan **`tectonic`**:
> - Ukuran unduhan hanya **4.1 MB** (terpasang ~16 MB).
> - Mesin modern berbasis Rust & XeTeX yang mengunduh paket secara *on-demand* (hemat memori drastis).
> - Berkas PDF hasil kompilasi akan otomatis disalin ke folder [`storage/shared/proposal tugas akhir/`](file:///data/data/com.termux/files/home/storage/shared/proposal%20tugas%20akhir/) agar bisa langsung dibuka di aplikasi PDF viewer HP Anda.

---

## Open Questions
- Apakah Anda ingin tanda tangan dosen & stempel disematkan langsung di lembar persetujuan PDF hasil kompilasi, atau dibiarkan berupa garis kosong untuk tanda tangan basah?
  *(Rencana default: Disediakan tombol saklar / toggle di LaTeX, default menyematkan gambar untuk pratinjau lengkap).*

---

## Rencana Perubahan (Proposed Changes)

```
LAPORAN-KP-Fahry-Rizky-Samsudin/
├── .gitignore                  # [NEW] Memblokir file tanda tangan/stempel agar aman dari git
├── Header/persetujuan.tex      # [MODIFY] Menambahkan opsi penyematan gambar tanda tangan & stempel
├── compile.py / compile.sh     # [NEW] Skrip kompilasi otomatis berbasis Tectonic
└── output/
    └── Laporan_KP_Fahry_Compiled.pdf # [NEW] Salinan PDF hasil kompilasi untuk dilihat di HP
```

---

### Tahap 1: Pengamanan Berkas Tanda Tangan & Konfigurasi Proteksi
#### [NEW] `.gitignore`
* Memastikan berkas biner sensitif dilindungi:
  ```gitignore
  # Security: Protect official signatures and stamps
  Gambar/ttd_*.png
  Gambar/stempel_*.png
  *.aux
  *.log
  *.out
  ```

#### [MODIFY] `Header/persetujuan.tex`
* Menambahkan blok kondisional agar gambar tanda tangan dan stempel dapat ditampilkan secara presisi di atas nama pembimbing bila diinginkan, tanpa merusak tata letak teks bila dikosongkan.

---

### Tahap 2: Pemasangan Mesin Ringan Tectonic & Kompilasi
* Memasang paket `tectonic` melalui Termux package manager (`pkg install tectonic -y` / ukuran 4.1 MB).
* Menjalankan kompilasi naskah `main.tex`:
  ```bash
  tectonic -X compile main.tex
  ```
* Tectonic akan menyelesaikan pembuatan font, perataan bab, rumus kinematika, tabel, serta penomoran halaman secara otomatis.

---

### Tahap 3: Ekspor PDF ke Storage Bersama (Shared Storage)
* Menyalin PDF hasil kompilasi ke:
  `storage/shared/proposal tugas akhir/Laporan_KP_Fahry_Hasil_Kompilasi.pdf`
* Pengguna dapat langsung membuka file ini di aplikasi File Manager atau PDF Viewer Android (Google PDF Viewer, WPS, Adobe Acrobat, dsb.).

---

## Verification Plan

### Automated Tests
1. **Verifikasi Tectonic**:
   ```bash
   tectonic --version
   ```
2. **Verifikasi Kompilasi**:
   ```bash
   test -f /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/main.pdf
   ```
3. **Verifikasi Salinan PDF di Shared Storage**:
   ```bash
   ls -la "/data/data/com.termux/files/home/storage/shared/proposal tugas akhir/Laporan_KP_Fahry_Hasil_Kompilasi.pdf"
   ```

### Manual Verification
1. Buka file `Laporan_KP_Fahry_Hasil_Kompilasi.pdf` dari File Manager Android Anda.
2. Periksa kesesuaian halaman judul, lembar pengesahan, rumus kinematika di Bab III, diagram alir TikZ di Bab IV, grafik akurasi di Bab V, serta galeri gambar di Lampiran.
