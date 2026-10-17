# Walkthrough: Migrasi PDF Laporan KP ke Format Modular LaTeX

Telah selesai dilakukan konversi dan rekonstruksi naskah **Laporan Kerja Mandiri Terpantau (Laporan KP)** milik Fahry Rizky Samsudin dari dokumen PDF asli (68 halaman) menjadi format **LaTeX modular** di folder mandiri baru dengan integrasi penuh ke pustaka *skills* dan *scripts*.

---

## 1. Lokasi & Struktur Repositori Baru

Direktori target:
👉 [`/data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin)

```
LAPORAN-KP-Fahry-Rizky-Samsudin/
├── main.tex                    # Berkas master LaTeX (standard UIN Sunan Gunung Djati Bandung)
├── references.bib              # Bibliografi BibTeX (18 entri lengkap)
├── build.sh                    # Skrip shell kompilasi otomatis
├── AGENTS.md                   # Spesifikasi sistem AI untuk repositori ini
├── README.md                   # Dokumentasi umum proyek
├── Header/                     # Halaman Preliminer
│   ├── sampul.tex              # Halaman judul & logo
│   ├── Keaslian.tex            # Surat pernyataan keaslian
│   ├── persetujuan.tex         # Lembar persetujuan pembimbing
│   ├── pengesahan.tex          # Lembar pengesahan penguji
│   ├── abstrak.tex             # Abstrak Bahasa Indonesia
│   ├── abstract.tex            # Abstract Bahasa Inggris
│   ├── prakata.tex             # Kata pengantar
│   ├── d_isi.tex               # Daftar isi
│   ├── d_gambar.tex            # Daftar gambar
│   └── d_tabel.tex             # Daftar tabel
├── Isi/                        # Naskah Utama Bab & Lampiran
│   ├── Bab1_Pendahuluan.tex    # Bab I: Latar belakang s.d. waktu & tempat
│   ├── Bab2_Profil_Industri.tex # Bab II: Politeknik Enjinering Indorama
│   ├── Bab3_Tinjauan_Pustaka.tex # Bab III: Embedded CV, MediaPipe, Kinematika 4-DOF
│   ├── Bab4_Metode_Penelitian.tex # Bab IV: Tabel 4.1 Alat/Bahan & Diagram Alir TikZ Gambar 4.1
│   ├── Bab5_Hasil_dan_Pembahasan.tex # Bab V: TikZ Gambar 5.1, Tabel 5.1-5.6, Grafik DNN, Evaluasi Real-Time
│   ├── Bab6_Kesimpulan_dan_Saran.tex # Bab VI: Kesimpulan & Saran
│   └── Lampiran.tex            # Lampiran 1-3 (Program Python & Arduino) + Galeri 19 Foto Eksperimen
├── Gambar/                     # 33 Berkas Gambar Resolusi Penuh Asli
├── .agents/                    # [SYMLINK] Akses 2.220+ skills & rules dari PROPOSAL-TA
├── scripts/                    # [SYMLINK] Akses skrip otomasi dari PROPOSAL-TA
└── .superpowers/               # [SYMLINK] Alat bantu superpowers dari PROPOSAL-TA
```

---

## 2. Aset Gambar & Diagram yang Direkonstruksi

1. **33 Gambar Biner Resolusi Asli**:
   - Diekstrak langsung dari objek biner PDF (*raw XObject stream*) tanpa terpotong (*no crop loss*), mencakup foto beresolusi kamera $4000 \times 3000$ piksel (12 MP) dan plot evaluasi PNG *lossless*.
   - Gambar tanda tangan dan stempel (`.jp2`) dikonversi secara transparan ke format `.png` standar.
2. **Rekonstruksi Diagram Vektor TikZ Murni**:
   - **Gambar 4.1 (Diagram Alir Penelitian)**: Ditulis langsung menggunakan sintaks `\begin{tikzpicture}` dengan blok alur proses dan panah terarah.
   - **Gambar 5.1 (Hasil Rancangan Arsitektur Sistem Raspberry Pi 5)**: Ditulis langsung menggunakan TikZ blok komputasi tepi dengan percabangan mode SIBI dan teleoperasi.

---

## 3. Hasil Pengujian Verifikasi Otomatis

| Pengujian | Status | Rincian |
| :--- | :---: | :--- |
| **Integritas Symlink** | PASSED | `.agents`, `scripts`, dan `.superpowers` terhubung valid ke `PROPOSAL-TA` |
| **Aset Gambar** | PASSED | 33 file gambar ada di `Gambar/` dengan ukuran valid ($>0$ byte) |
| **Kelengkapan TeX & Bib** | PASSED | 19 file `.tex` dan `.bib` lengkap dan terisi |
| **Keseimbangan Sintaks LaTeX** | PASSED | Seluruh `\begin{...}` dan `\end{...}` seimbang sempurna |

---

## 4. Cara Penggunaan & Kompilasi

* Untuk mengompilasi langsung di terminal (bila `texlive` terpasang):
  ```bash
  cd ~/LAPORAN-KP-Fahry-Rizky-Samsudin
  ./build.sh
  ```
* Untuk mengedit atau mengompilasi di **Overleaf**:
  Cukup unggah seluruh isi folder [`LAPORAN-KP-Fahry-Rizky-Samsudin`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin) ke proyek baru di Overleaf, dan pastikan file utama yang dipilih adalah [`main.tex`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/main.tex).
