# Rencana Implementasi: Presentasi Laporan KP (Format Anti-Slop 100% Gaya Skripsi Gilang)

## Deskripsi Rencana
Merombak total seluruh rancangan dan script pembuat slide presentasi untuk seminar/sidang **Laporan Kerja Mandiri Terpantau (Laporan KP)** milik **Fahry Rizky Samsudin** (*NIM 1237030018*). 

Menjawab kritik pengguna (*"masih slop parah kocak, kamu malah bikin elemen baru untuk flowchart terus isinya slop seslopnya"*), perbaikan ini **membuang 100% teks generik AI dan diagram sintesis buatan matplotlib**, lalu menggantinya secara presisi dengan format akademik murni mengadopsi struktur slide skripsi **Gilang Pratama Putra Siswanto (`1227030017_skripsi.pdf`)**:
1. **Diagram Alir Asli (Zero Synthetic Graphics)**: Tidak lagi menggambar kotak-kotak buatan via matplotlib. Diagram alir dikompilasi langsung dari kode sumber TikZ naskah LaTeX (`Bab4` Gambar 4.1 dan `Bab5` Gambar 5.1) menggunakan `tectonic` dan diekspor ke PNG 300 DPI via `pdftoppm`.
2. **Latar Belakang Gaya Gilang (Causal Flow + Gap Research)**: Mengganti paragraf narasi generik dengan bagan rantai kausalitas 6 node berpanah emas berisi angka statistik riil dan sitasi formal `(Author, Year)` yang bermuara pada kotak emas **Gap Research**.
3. **Format Slide Image-First & Data-Heavy**: Setiap slide didominasi oleh grafik eksperimen riil, tabel data asli, skema mekanik, dan rumus fisis dengan caption resmi `Gambar X.` dan `Tabel Y.`. Teks pendukung dibatasi maksimal 2 baris ringkas berisi klaim kuantitatif.
4. **Output Ganda**: Berkas widescreen 16:9 `.pptx` dan `.pdf` disalin ke folder HP:
   👉 `/storage/emulated/0/Akademik/Laporan KP/`

---

## User Review Required

> [!IMPORTANT]
> **Audit Perubahan Paradigma (Slop vs Anti-Slop Gaya Gilang):**
> * **Elemen Flowchart**: Dilarang menggunakan matplotlib boxes. Seluruh diagram alir adalah diagram asli naskah TeX (`Gambar 4.1` Metodologi 6 Tahap dan `Gambar 5.1` Arsitektur Sistem RPi 5) yang dirender melalui kompilasi standalone TikZ beresolusi 300 DPI.
> * **Latar Belakang**: Slide 2 disusun persis seperti Slide 2 Gilang: 5 kotak ringkas terhubung panah emas berisi data angka/sitasi literatur $\to$ menuju kotak emas bertuliskan pertanyaan **Gap Research**.
> * **Dasar Teori**: Tidak ada paragraf panjang. Tiap konsep hanya memuat 2 bullet poin ringkas + rumus fisis + gambar asli naskah bertuliskan caption formal (`Gambar 3.1`, `Gambar 3.2`, `Gambar 3.3`, `Gambar 3.4a-b`).
> * **Hasil dan Pembahasan**: Judul slide adalah klaim kuantitatif singkat (misal: *"Akurasi Pengujian Real-Time SIBI Mencapai 96,73% dengan 22 dari 26 Abjad Sempurna"*), didampingi tabel data riil dan kurva/matriks konfusi asli naskah.

---

## Struktur 24 Slide Presentasi (Identik dengan Logika Slide Gilang)

```
[BAGIAN I: PRELIMINER & PENDAHULUAN]
Slide 01: Cover Resmi Akademik (Logo UIN & Fisika, Judul Lengkap, Peneliti NIM 1237030018, Pembimbing I & II)
Slide 02: Latar Belakang (Alur Berantai Kausalitas 6 Node: Craig 2018 -> Shi 2016 -> Satyanarayanan 2017 -> MediaPipe 2019 -> Gap Research Emas)
Slide 03: Rumusan Masalah (3 Butir Asli Bab 1) & Batasan Masalah (5 Butir Asli Bab 1)
Slide 04: Tujuan Penelitian (3 Butir Asli Bab 1) & Tempat/Waktu Penelitian (Jan-Feb 2026, Lab Mekatronika PEI Purwakarta)

[BAGIAN II: PROFIL MITRA INDUSTRI]
Slide 05: Profil Mitra: Politeknik Enjinering Indorama (PEI) Purwakarta, Sejarah PT Indorama Synthetics Tbk, & Roadmap Mekatronika

[BAGIAN III: DASAR TEORI (SELURUH MATERI BAB III BERBASIS GAMBAR ASLI & FORMULA)]
Slide 06: Dasar Teori: Sistem Visi Komputer Tertanam & Edge Computing Raspberry Pi 5 [Gambar 3.1 Antarmuka Dobot] (Szeliski, 2022; Satyanarayanan, 2017)
Slide 07: Dasar Teori: Ekstraksi Fitur Geometris & MediaPipe 21 Hand Landmarks (63 Koordinat) [Gambar 3.2 Topologi Landmark] (Lugaresi, 2019; Zhang, 2020)
Slide 08: Dasar Teori: Pengenalan SIBI Berbasis Deep Neural Networks (DNN) & Fungsi Aktivasi Softmax [Formula Matematika DNN] (Kosasih, 2012; Goodfellow, 2016)
Slide 09: Dasar Teori: Kinematika Lengan Robot Manipulator 4-DOF [Formula Forward & Inverse Kinematics (X,Y,Z & Theta 1..4)] (Craig, 2018; Lynch, 2017)
Slide 10: Dasar Teori: Karakteristik Perangkat Keras Manipulator [Gambar 3.3 Dobot Magician & Gambar 3.4a-b meArm 4-DOF] (Dobot, 2026; meArm, 2026)

[BAGIAN IV: METODE PENELITIAN & DIAGRAM ALIR ASLI (BAB IV)]
Slide 11: Metode Penelitian: Alat dan Bahan Penelitian [Tabel 4.1 Spesifikasi Lengkap 13 Komponen Asli]
Slide 12: Metode Penelitian: Diagram Alir Penelitian [Gambar 4.1 Render TikZ Asli 6 Tahapan Metodologi]
Slide 13: Metode Penelitian: Perancangan Perangkat Keras (Integrasi Jalur Daya 5V DC Terpisah, USB Serial Dobot, GPIO RPi 5) + Foto Fisik
Slide 14: Metode Penelitian: Arsitektur Sistem Tertanam Raspberry Pi 5 [Gambar 5.1 Render TikZ Asli Arsitektur Dual-Mode]
Slide 15: Metode Penelitian: Diagram Alir Logika Piranti Lunak (Alur SIBI 63 Fitur & Alur Filter Teleoperasi Alpha=0,2)

[BAGIAN V: HASIL DAN PEMBAHASAN (KLAIM KUANTITATIF + GAMBAR ASLI + TABEL RIIL)]
Slide 16: Hasil dan Pembahasan: Pelatihan Model DNN SIBI Konvergen pada 100 Epoch [Gambar 5.2a Akurasi vs Epoch & Gambar 5.2b Loss vs Epoch]
Slide 17: Hasil dan Pembahasan: Akurasi Pengujian Real-Time SIBI Mencapai 96,73% [Gambar 5.3 CM Validasi, Gambar 5.4 CM Real-Time, & Tabel 5.2 Rekapitulasi]
Slide 18: Hasil dan Pembahasan: Pengujian Respons Kinematik meArm terhadap Perintah SIBI [Gambar 5.5 Dokumentasi Uji meArm, Tabel 5.1 & Tabel 5.3]
Slide 19: Hasil dan Pembahasan: Evaluasi Pemetaan Koordinat Teleoperasi Dobot Magician 100% Valid [Gambar 5.6 Dokumentasi Uji Dobot & Tabel 5.4]
Slide 20: Hasil dan Pembahasan: Presisi Spasial Dobot Rata-rata 1,90 mm dan Waktu Respons 87,25 ms [Tabel 5.5 Data Galat Spasial & Formula Euclidean]
Slide 21: Hasil dan Pembahasan: Rangkuman Kinerja Sistem Keseluruhan [Tabel 5.6 Rekapitulasi Kinerja Dual-Mode & Tautan Google Drive Video Eksperimen]

[BAGIAN VI: DOKUMENTASI, KESIMPULAN, & PENUTUP]
Slide 22: Dokumentasi Implementasi Purwarupa & Stasiun Uji Eksperimen [Gambar 6.1 s.d. 6.19 Perakitan & Uji Fisik meArm/Dobot]
Slide 23: Kesimpulan (3 Poin Kuantitatif Asli Bab 6) & Saran (5 Poin Pengembangan Asli Bab 6)
Slide 24: Daftar Pustaka Utama (Sitasi Formal IEEE/APA Sesuai Naskah) & Terima Kasih (Sesi Tanya Jawab)
```

---

## Rencana Perubahan (Proposed Changes)

### 1. Ekstraksi dan Render Aset Resmi TikZ
* Mengompilasi kode TikZ langsung dari sumber LaTeX:
  - `fig4_1.tex` $\rightarrow$ `Gambar/Gambar4_1_diagram_alir_penelitian_asli.png` (via `tectonic` + `pdftoppm -r 300`).
  - `fig5_1.tex` $\rightarrow$ `Gambar/Gambar5_1_arsitektur_sistem_asli.png` (via `tectonic` + `pdftoppm -r 300`).
  - `fig_software_flow.tex` $\rightarrow$ `Gambar/Gambar4_2_diagram_alir_software_asli.png` (Alur logika SIBI & Teleoperasi).
* Tidak ada lagi penggunaan generator gambar sintetis `render_flowcharts.py`!

### 2. Rekonstruksi Script Generator (`scripts/generate_laporan_kp_deck_full.py`)
* Menulis ulang skrip dengan arsitektur **Anti-Slop Strict Enforcement**:
  - **Slide 2 (Latar Belakang)**:
    Render diagram rantai 6 kotak berpanah emas:
    * Kotak 1: *Urgensi HMI & Otomasi*: Interaksi nirsentuh (*contactless*) gantikan joystick konvensional (Craig, 2018; Rautaray & Agrawal, 2015).
    * Kotak 2: *Inklusi SIBI*: Komunikasi isyarat 26 abjad daktilologi ramah disabilitas (Kosasih, 2012).
    * Kotak 3: *Limitasi Cloud Konvensional*: Komputasi awan timbulkan latensi transmisi >200 ms & isu privasi (Shi et al., 2016).
    * Kotak 4: *Solusi Komputasi Tepi (Edge AI)*: RPi 5 SoC BCM2712 Cortex-A76 proses inferensi lokal mandiri 30 FPS (Satyanarayanan, 2017; Wang et al., 2020).
    * Kotak 5: *Ekstraksi Fitur Ringan*: MediaPipe 21 landmark 3D (63 fitur koordinat vektor padat) reduksi komputasi piksel (Lugaresi et al., 2019; Zhang et al., 2020).
    * Kotak 6 (Emas): **Gap Research**: *"Rancang bangun sistem visi tertanam RPi 5 untuk kendali dual-mode (teleoperasi kontinu Dobot presisi <2 mm & klasifikasi instruksional SIBI meArm akurasi >95%) secara mandiri dengan latensi <100 ms?"*
  - **Slide 3-5 (Bab I & Profil Industri)**:
    Format nomor urut ringkas dan formal, tanpa kalimat panjang generik.
  - **Slide 6-10 (Dasar Teori)**:
    Format 2 konsep per slide: Judul bold $\to$ 2 baris definisi/sitasi $\to$ Formula matematis $\to$ Gambar asli dengan caption `Gambar 3.X`.
  - **Slide 11-15 (Metode Penelitian)**:
    Tabel 4.1 komponen riil + Gambar 4.1 TikZ asli + Gambar 5.1 TikZ asli + Diagram alir software TikZ asli.
  - **Slide 16-21 (Hasil dan Pembahasan)**:
    Judul berupa klaim kuantitatif ilmiah + Gambar grafik kurva/CM + Tabel data riil side-by-side + Callout angka metrik.
  - **Slide 22-24 (Dokumentasi & Penutup)**:
    Grid foto purwarupa Lampiran + Kesimpulan kuantitatif Bab 6 + Referensi formal.

### 3. Eksekusi Kompilasi PPTX & PDF
* Menjalankan:
  ```bash
  cd ~/LAPORAN-KP-Fahry-Rizky-Samsudin
  python3 scripts/generate_laporan_kp_deck_full.py
  ```
* Menghasilkan berkas:
  - `Laporan_KP_Fahry_Rizky_Samsudin.pptx`
  - `Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf`

### 4. Sinkronisasi ke Penyimpanan HP
* Menyalin ke:
  `/storage/emulated/0/Akademik/Laporan KP/Laporan KP Fahry Rizky Samsudin.pptx`
  `/storage/emulated/0/Akademik/Laporan KP/Laporan KP Fahry Rizky Samsudin - Presentasi.pdf`

---

## Verification Plan

### Automated Tests
1. **Verifikasi Aset Gambar TikZ Asli**:
   ```bash
   test -f Gambar/Gambar4_1_diagram_alir_penelitian_asli.png
   test -f Gambar/Gambar5_1_arsitektur_sistem_asli.png
   ```
2. **Pemeriksaan PPTX (24 Slide)**:
   ```python
   from pptx import Presentation
   prs = Presentation('Laporan_KP_Fahry_Rizky_Samsudin.pptx')
   assert len(prs.slides) == 24
   print("PPTX Verification OK: 24 slides!")
   ```
3. **Pemeriksaan PDF (24 Halaman Widescreen)**:
   ```python
   import pypdf
   reader = pypdf.PdfReader('Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf')
   assert len(reader.pages) == 24
   print("PDF Verification OK: 24 pages!")
   ```
4. **Pemeriksaan File di Storage HP**:
   ```bash
   ls -lh "/storage/emulated/0/Akademik/Laporan KP/Laporan KP Fahry Rizky Samsudin.pptx"
   ls -lh "/storage/emulated/0/Akademik/Laporan KP/Laporan KP Fahry Rizky Samsudin - Presentasi.pdf"
   ```
