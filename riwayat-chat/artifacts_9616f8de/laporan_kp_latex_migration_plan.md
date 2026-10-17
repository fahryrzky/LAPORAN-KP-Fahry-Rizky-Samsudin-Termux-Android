# Rencana Implementasi: Konversi PDF Laporan KP Fahry ke Format LaTeX Modular (Opsi 2)

## Deskripsi Tujuan
Mengonversi dokumen PDF **Laporan Kerja Mandiri Terpantau (Laporan KP)** milik Fahry Rizky Samsudin (68 halaman) dari:
- Sumber: [`storage/shared/proposal tugas akhir/Laporan KP - Fahry Rizky Samsudin (1237030018)-signed (2).pdf`](file:///data/data/com.termux/files/home/storage/shared/proposal%20tugas%20akhir/Laporan%20KP%20-%20Fahry%20Rizky%20Samsudin%20(1237030018)-signed%20(2).pdf)
ke dalam folder baru yang terisolasi dan mandiri:
- Target: [`/data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin)

Sesuai permintaan pengguna, folder baru ini akan dihubungkan (*symlinked*) ke folder [`PROPOSAL-TA-Fahry-RIzky-Samsudin`](file:///data/data/com.termux/files/home/PROPOSAL-TA-Fahry-RIzky-Samsudin) agar seluruh **2.220+ skills**, **rules**, dan **scripts** otomatis dapat diakses dan digunakan di dalam folder Laporan KP tanpa menduplikasi data atau merusak naskah Proposal TA.

---

## User Review Required
> [!IMPORTANT]
> **Integrasi Berbagi Resources (*Skills & Scripts*):**
> Folder Laporan KP akan menggunakan *symbolic link* (symlink) Linux ke folder `PROPOSAL-TA`:
> - `.agents` $\rightarrow$ `../PROPOSAL-TA-Fahry-RIzky-Samsudin/.agents` (menyediakan akses instan ke 2.220+ skill dan aturan)
> - `scripts` $\rightarrow$ `../PROPOSAL-TA-Fahry-RIzky-Samsudin/scripts` (seluruh script utilitas, bibtex parser, pengunduh DOI, dll.)
> - `.superpowers` $\rightarrow$ `../PROPOSAL-TA-Fahry-RIzky-Samsudin/.superpowers`
>
> Hal ini memastikan nol redudansi penyimpanan di memori Android/Termux dan sinkronisasi otomatis bila ada script yang diperbarui.

> [!NOTE]
> Mengenai repositori `mdflux`: Folder `mdflux` (40MB) yang sempat di-clone untuk inspeksi akan dihapus agar menghemat ruang penyimpanan di Termux, karena tidak diperlukan dan tidak cocok untuk tugas ini.

---

## Open Questions
Tidak ada pertanyaan pemblokir (*blocking questions*). Seluruh data pada naskah PDF (68 halaman, 33 gambar, 18+ referensi) telah berhasil dipindai dan terbaca 100% secara digital.

---

## Rencana Perubahan (Proposed Changes)

```
LAPORAN-KP-Fahry-Rizky-Samsudin/
├── .agents/                    -> symlink ke PROPOSAL-TA/.agents
├── scripts/                    -> symlink ke PROPOSAL-TA/scripts
├── .superpowers/               -> symlink ke PROPOSAL-TA/.superpowers
├── AGENTS.md                   # Panduan AI spesifik topik Laporan KP (Robotika 4-DOF & CV)
├── main.tex                    # Dokumen master LaTeX (konfigurasi paket, geometri, urutan input)
├── references.bib              # Database BibTeX lengkap dari Daftar Pustaka
├── Header/                     # Bagian preliminer
│   ├── sampul.tex              # Halaman judul Laporan KP
│   ├── Keaslian.tex            # Surat pernyataan keaslian
│   ├── persetujuan.tex         # Lembar persetujuan pembimbing
│   ├── pengesahan.tex          # Lembar pengesahan penguji
│   ├── abstrak.tex             # Abstrak Bahasa Indonesia
│   ├── abstract.tex            # Abstract Bahasa Inggris
│   ├── prakata.tex             # Kata Pengantar
│   ├── d_isi.tex               # Daftar Isi
│   ├── d_gambar.tex            # Daftar Gambar
│   └── d_tabel.tex             # Daftar Tabel
├── Isi/                        # Naskah utama bab
│   ├── Bab1_Pendahuluan.tex    # Bab I: Latar Belakang, Rumusan, Batasan, Tujuan, Manfaat, Waktu
│   ├── Bab2_Profil_Industri.tex # Bab II: Politeknik Enjinering Indorama, Sejarah, Visi Misi, Roadmap
│   ├── Bab3_Tinjauan_Pustaka.tex # Bab III: Embedded CV, RPi 5, SIBI DNN, MediaPipe, Kinematika 4-DOF
│   ├── Bab4_Metode_Penelitian.tex # Bab IV: Alat/Bahan, Diagram Alir, Desain Hardware & Software
│   ├── Bab5_Hasil_dan_Pembahasan.tex # Bab V: Hasil Sistem, Akurasi SIBI, Teleoperasi Dobot, Kinematika meArm
│   ├── Bab6_Kesimpulan_dan_Saran.tex # Bab VI: Kesimpulan & Saran
│   └── Lampiran.tex            # Lampiran 1-4: Program Python, Firmware Arduino, Foto Dokumentasi
└── Gambar/                     # 33 Gambar/Diagram hasil ekstraksi resolusi tinggi
    ├── Logo/                   # Logo UIN SGD
    ├── Bab2/                   # Dokumentasi industri
    ├── Bab3/                   # Ilustrasi arsitektur sistem, MediaPipe, Dobot, meArm
    ├── Bab4/                   # Diagram alir penelitian & skematik
    ├── Bab5/                   # Confusion matrix, grafik akurasi, grafik respons
    └── Lampiran/               # Foto perakitan rangka, robot meArm, dan Dobot Magician
```

---

### Tahap 1: Inisialisasi Struktur Folder & Symlink
#### [NEW] `/data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin`
* Membuat direktori target berserta subfolder: `Header/`, `Isi/`, `Gambar/`, `output/`.
* Membuat symlink:
  * `.agents` $\rightarrow$ `/data/data/com.termux/files/home/PROPOSAL-TA-Fahry-RIzky-Samsudin/.agents`
  * `scripts` $\rightarrow$ `/data/data/com.termux/files/home/PROPOSAL-TA-Fahry-RIzky-Samsudin/scripts`
  * `.superpowers` $\rightarrow$ `/data/data/com.termux/files/home/PROPOSAL-TA-Fahry-RIzky-Samsudin/.superpowers`
* Menghapus folder sementara `~/mdflux`.

---

### Tahap 2: Ekstraksi Otomatis Gambar & Rekonstruksi Diagram TikZ
#### [NEW] `Gambar/` (33 File Gambar Asli)
* **Ekstraksi Biner (*Raw XObject Stream*)**:
  Mengambil langsung file biner asli gambar yang tertanam di PDF (bukan screenshot layar), sehingga **tidak ada bagian yang terpotong margin**:
  - Foto kamera meArm & Dobot (4000x3000 piksel / 12 MP & 1600x1200 piksel)
  - Confusion matrix & kurva akurasi/loss (PNG lossless tajam)
  - Logo UIN (PNG resolusi 1915x2744 piksel)
  - Konversi otomatis stempel/tanda tangan pembimbing dari format JPEG2000 (`.jp2`) ke `.png` agar 100% kompatibel dengan compiler LaTeX.
* **Rekonstruksi Diagram Vektor TikZ (Gambar 4.1 & 5.1)**:
  - **Gambar 4.1 (Diagram Alir Penelitian)** dan **Gambar 5.1 (Arsitektur Sistem Tertanam Raspberry Pi 5)** di PDF aslinya bukan file bitmap, melainkan digambar langsung menggunakan paket LaTeX `tikz`.
  - Kita merekonstruksi kembali kode blok `\begin{tikzpicture}` aslinya secara presisi, sehingga hasilnya adalah vektor tajam yang tidak akan pecah di level zoom mana pun.
* **Mitigasi Kualitas Gambar (Bila Kurang Sempurna)**:
  1. *Fallback ke Foto Asli*: Jika ada foto dokumentasi yang diinginkan versi mentahnya, kita dapat menautkan langsung ke foto kamera asli yang tersimpan di folder `proposal tugas akhir` (seperti `IMG_20261001_172001.jpg`, `Tampak depan.jpg`).
  2. *Skrip Verifikasi Gambar*: Menyediakan skrip verifikasi untuk memeriksa dimensi, resolusi, dan integritas seluruh file gambar yang diekstrak.

---

### Tahap 3: Penyusunan Berkas Master dan Header LaTeX
#### [NEW] `main.tex`
* Menyiapkan konfigurasi `\documentclass[12pt,a4paper]{report}` dengan margin 4-3-4-3 cm (standar UIN Sunan Gunung Djati Bandung).
* Mengaktifkan paket: `geometry`, `setspace`, `graphicx`, `amsmath`, `tikz`, `listings`, `hyperref`, `longtable`, `tocloft`, `titlesec`.
* Mendefinisikan format bab dan penomoran (Romawi untuk bab, Arab untuk subbab, gambar, dan tabel).
* Menyusun blok `\include` / `\input` terstruktur.

#### [NEW] `Header/*.tex`
* `Header/sampul.tex`: Judul lengkap, nama, NIM, logo, jurusan Fisika UIN SGD.
* `Header/Keaslian.tex`: Naskah surat pernyataan keaslian bebas plagiarisme.
* `Header/persetujuan.tex`: Pengesahan oleh Pembimbing I: Dr. Moch Nurul Subkhi, M.Si (NIP. 198007202008011007).
* `Header/pengesahan.tex`: Format lembar pengesahan seminar/sidang KP.
* `Header/abstrak.tex` & `Header/abstract.tex`: Teks abstrak bilingual lengkap kata kunci (*keywords*).
* `Header/prakata.tex`: Kata pengantar lengkap ucapan terima kasih kepada pimpinan jurusan, pembimbing, keluarga, dan pihak industri.
* `Header/d_isi.tex`, `Header/d_gambar.tex`, `Header/d_tabel.tex`: Pemanggilan daftar isi, gambar, tabel otomatis.

---

### Tahap 4: Penyusunan Bab Utama & Lampiran
#### [NEW] `Isi/Bab1_Pendahuluan.tex` s.d. `Isi/Bab6_Kesimpulan_dan_Saran.tex`
* Mengonversi teks dari PDF halaman 14 sampai 48:
  * **Bab 1:** Latar belakang visi komputer tertanam, teleoperasi 4-DOF, rumusan masalah, batasan masalah, tujuan, manfaat, lokasi Politeknik Enjinering Indorama Purwakarta.
  * **Bab 2:** Profil Politeknik Enjinering Indorama, sejarah Yayasan Pendidikan Indorama, visi misi mekatronika, roadmap riset.
  * **Bab 3:** Tinjauan pustaka embedded vision, Raspberry Pi 5 Broadcom BCM2712, MediaPipe Hands 21 landmarks, klasifikasi DNN SIBI, kinematika maju & balikan (Denavit-Hartenberg & geometrik trigonometri) manipulator 4-DOF, Dobot Magician, meArm.
  * **Bab 4:** Metodologi perancangan mekatronik, integrasi motor servo SG90, mikrokontroler Arduino Uno, diagram alir sistem, akuisisi dataset isyarat SIBI.
  * **Bab 5:** Hasil pengujian komputasi tepi, akurasi model DNN (confusion matrix), latensi FPS di Raspberry Pi 5, waktu respon teleoperasi Dobot Magician, manuver presisi meArm.
  * **Bab 6:** Kesimpulan pencapaian dan saran perbaikan pengembangan masa depan.

#### [NEW] `Isi/Lampiran.tex`
* Lampiran 1: Kode Python akuisisi OpenCV & MediaPipe Hands + inferensi Tkinter GUI.
* Lampiran 2: Script Python teleoperasi dinamik Dobot Magician via antarmuka serial/USB.
* Lampiran 3: Firmware Arduino C++ kendali sudut servo meArm berbasis kinematika balikan.
* Lampiran 4: Galeri foto eksperimen lengkap (Gambar 6.1 s.d 6.18) dengan lingkungan `figure` dan `caption`.

#### [NEW] `references.bib`
* Menyusun seluruh 18+ sitasi bibliografi dalam format standar BibTeX (`@book`, `@article`, `@manual`, `@misc`).

---

### Tahap 5: Dokumentasi Proyek AI & Build Tool
#### [NEW] `AGENTS.md` & `README.md`
* Menjelaskan identitas proyek Laporan KP, arsitektur folder, tata cara kompilasi, serta cara menggunakan skrip-skrip dari `scripts/` untuk memperbarui sitasi atau mengekspor presentasi.
#### [NEW] `build.sh`
* Script shell Termux untuk otomatisasi build LaTeX (`pdflatex` / `xelatex` + `bibtex`) jika sewaktu-waktu pengguna menginstal TeXLive di Termux atau menjalankan di Overleaf/VS Code.

---

## Verification Plan

### Automated Tests
1. **Verifikasi Integritas File & Symlink**:
   ```bash
   ls -la /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin
   # Memastikan .agents, scripts, dan .superpowers terhubung valid ke PROPOSAL-TA
   test -L /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/.agents
   test -d /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/.agents/skills
   ```
2. **Verifikasi Ekstraksi Gambar**:
   ```bash
   ls -1 /data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Gambar | wc -l
   # Memastikan seluruh 33 file gambar berhasil diekstrak dan memiliki ukuran non-nol
   ```
3. **Verifikasi Validitas Sintaks LaTeX**:
   - Memeriksa kelengkapan pasangan `\begin{...}` dan `\end{...}`, `\input{...}` path, kurung kurawal, dan sitasi `\cite{...}` terhadap `references.bib`.

### Manual Verification
1. Meninjau file [main.tex](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/main.tex) dan memastikan struktur bab sesuai dengan Daftar Isi Laporan KP asli.
2. Memeriksa ketersediaan gambar dan keterbacaan kode program pada [Lampiran.tex](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Isi/Lampiran.tex).
