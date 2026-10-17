# Rencana Implementasi: Kompilasi Final & Ekspor PDF Laporan KP ke Penyimpanan HP

## Deskripsi Tujuan
Melanjutkan dan menyelesaikan rencana eksekusi terakhir dari sesi sebelumnya untuk **Laporan Kerja Mandiri Terpantau (Laporan KP)** milik Fahry Rizky Samsudin:
1. Memastikan seluruh pembaruan naskah LaTeX modular (perbaikan spasi [sampul.tex](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Header/sampul.tex), penyematan 2 tanda tangan pembimbing di [persetujuan.tex](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Header/persetujuan.tex), dan pembersihan *smart quotes*) telah terintegrasi dengan sempurna.
2. Melakukan kompilasi penuh menggunakan kompiler **Tectonic**.
3. Membuat direktori `/storage/emulated/0/laporan kp/` di memori internal HP Android.
4. Menyalin berkas PDF hasil kompilasi akhir ke direktori tersebut dengan nama `Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf` agar dapat langsung diakses dan dibaca melalui File Manager HP.

---

## User Review Required

> [!IMPORTANT]
> **Status Integrasi Tanda Tangan & Format Halaman:**
> - **Dua Tanda Tangan Pembimbing**: Telah disematkan berdampingan pada [persetujuan.tex](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Header/persetujuan.tex):
>   1. **Pembimbing I**: Dr. Moch Nurul Subkhi, M.Si (`Gambar/ttd_pembimbing1_subkhi.png`)
>   2. **Pembimbing II**: Dr. Emmanuel Agung N, S.T, M.T. (`Gambar/ttd_pembimbing2_agung.png`)
> - **Sampul (Cover)**: Spasi telah diperbaiki agar presisi 1 halaman penuh tanpa bergeser ke halaman berikutnya.
> - **Proteksi Keamanan**: Berkas tanda tangan sudah dilindungi oleh [.gitignore](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/.gitignore).

> [!NOTE]
> **Target Lokasi Berkas PDF:**
> - Jalur penyimpanan Android: `/storage/emulated/0/laporan kp/`
> - Berkas output: `Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf`

---

## Open Questions
Tidak ada pertanyaan pemblokir (*blocking questions*). Seluruh berkas aset gambar, konfigurasi TeX, dan kompiler Tectonic telah terverifikasi siap dieksekusi.

---

## Rencana Perubahan & Langkah Kerja (Proposed Changes)

### 1. Kompilasi Ulang Berkas Master LaTeX
* Menjalankan proses kompilasi dokumen master menggunakan Tectonic:
  ```bash
  cd /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin
  tectonic -c minimal main.tex
  ```
* Tectonic akan memproses seluruh naskah (Preliminer, Bab I s.d. Bab VI, Daftar Pustaka BibTeX, serta Lampiran) menghasilkan `main.pdf`.

### 2. Pembuatan Direktori Shared Storage Android
* Membuat folder baru di penyimpanan internal perangkat:
  ```bash
  mkdir -p "/storage/emulated/0/laporan kp"
  ```

### 3. Ekspor & Penyalinan PDF
* Menyalin PDF hasil kompilasi ke folder penyimpanan bersama:
  ```bash
  cp /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/main.pdf \
     "/storage/emulated/0/laporan kp/Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf"
  ```

---

## Verification Plan

### Automated Tests
1. **Verifikasi Keberhasilan Kompilasi**:
   ```bash
   test -f /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/main.pdf && echo "Compile OK"
   ```
2. **Inspeksi Metadata & Jumlah Halaman PDF**:
   - Memeriksa jumlah halaman dan struktur PDF dengan script Python `pypdf`:
     - Memastikan total halaman konsisten (68 halaman).
     - Memastikan halaman 1 adalah Sampul tunggal.
     - Memastikan halaman 3 memuat Lembar Persetujuan dengan 2 objek gambar tanda tangan.
3. **Verifikasi Keberadaan Berkas di Shared Storage**:
   ```bash
   ls -la "/storage/emulated/0/laporan kp/Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf"
   ```

### Manual Verification
1. Buka aplikasi **File Manager** / Pengelola File di HP Android Anda.
2. Masuk ke folder **Penyimpanan Internal > `laporan kp`**.
3. Buka berkas `Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf` dan tinjau:
   - Sampul (1 halaman penuh rapi).
   - Lembar Persetujuan (kedua tanda tangan pembimbing muncul rapi).
   - Diagram alir penelitian (Bab IV) dan rancangan sistem (Bab V).
