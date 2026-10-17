# Walkthrough: Presentasi Laporan KP (Format Anti-Slop 100% Gaya Skripsi Gilang)

Slide presentasi untuk seminar/sidang **Laporan Kerja Mandiri Terpantau (Laporan KP)** milik **Fahry Rizky Samsudin** (*NIM 1237030018*) telah direkonstruksi total, membuang seluruh elemen AI-slop dan diagram buatan matplotlib, serta mengadopsi 100% struktur ilmiah murni dari slide skripsi **Gilang Pratama Putra Siswanto (`1227030017_skripsi.pdf`)**.

Berkas telah selesai dikompilasi ke format **PPTX** dan **PDF Widescreen 16:9** dan tersimpan langsung di folder penyimpanan internal smartphone Android:
👉 `/storage/emulated/0/Akademik/Laporan KP/`

---

## 1. Verifikasi Berkas Akhir di Penyimpanan HP Android

```
📂 /storage/emulated/0/Akademik/Laporan KP/
├── 📊 Laporan KP Fahry Rizky Samsudin.pptx              # [9.3 MB | 24 Slide Widescreen 16:9]
├── 📑 Laporan KP Fahry Rizky Samsudin - Presentasi.pdf  # [9.4 MB | 24 Halaman Widescreen 16:9]
└── 📄 Laporan KP Fahry Rizky Samsudin.pdf               # [16.0 MB | 69 Halaman Naskah Lengkap]
```

*Status Verifikasi Otomatis:*
* `PPTX Verified: 24 slides (Aspect Ratio 16:9)`
* `PDF Verified: 24 pages (Widescreen 13.333 x 7.5 inch)`
* `Diagram TikZ Asli: 300 DPI Vector-Rendered (Zero Matplotlib Artifacts)`

---

## 2. Bedah Transformasi Anti-Slop (Perbandingan Format)

| Bagian | Versi Sebelumnya (AI-Slop) | Versi Baru (Format Akademik Gilang Pratama) |
| :--- | :--- | :--- |
| **Diagram Alir (Flowchart)** | Menggunakan matplotlib boxes buatan baru dengan badge warna-warni sintetis. | **100% TikZ Asli Naskah LaTeX**: Dikompilasi via `tectonic` + `pdftoppm -r 300` langsung dari kode sumber TeX (`Gambar 4.1` Metodologi 6 Tahap, `Gambar 5.1` Arsitektur RPi 5, dan `Gambar 4.2` Alur Software). |
| **Slide 2 (Latar Belakang)** | Paragraf narasi teks generik AI ("Kebutuhan kendali jarak jauh... ramah disabilitas..."). | **Bagan Rantai Kausalitas (6 Node)**: Menghubungkan fakta statistik, batasan konvensional (latensi cloud >200 ms), solusi edge computing RPi 5, fitur 21 landmark MediaPipe, dengan panah emas bermuara ke **Gap Research Emas** ber-sitasi formal. |
| **Dasar Teori (Slide 6--10)** | Kartu teks panjang penjelasan generik. | **Image-First & Math Layout**: Hanya judul, 2 baris poin definisi + sitasi resmi, formula fisis fungsional, dan **Gambar Asli Naskah** dengan caption formal (`Gambar 3.1`, `Gambar 3.2`, `Gambar 3.3`, `Gambar 3.4`). |
| **Metode Penelitian (Slide 11--15)** | Diagram alir buatan baru & ringkasan umum. | **Data Lengkap Naskah**: Tabel 4.1 lengkap 13 komponen dan versi pustaka, Gambar 4.1 TikZ asli, Gambar 5.1 TikZ asli, skema daya terpisah 5V DC meArm, dan foto riil stasiun kerja. |
| **Hasil & Pembahasan (Slide 16--21)** | Paragraf naratif bertele-tele. | **Klaim Kuantitatif Singkat + Data Asli**: Judul berupa klaim terukur, kurva konvergensi Gambar 5.2a-b, Matriks Konfusi Gambar 5.4, Tabel 5.2 (520 data uji, akurasi 96,73%), Tabel 5.3 respons meArm, Tabel 5.4 pemetaan Dobot, Tabel 5.5 galat presisi 1,90 mm & respons 87,25 ms, serta tautan video Google Drive. |
| **Kesimpulan (Slide 23)** | Poin-poin umum AI. | **3 Kesimpulan Kuantitatif Asli Bab 6**: Menyebut akurasi 96,73%, galat 1,90 mm, respons 87,25 ms, dan filter eksponensial $\alpha = 0,2$. |

---

## 3. Rincian Struktur 24 Slide Presentasi

```
[BAGIAN I: PRELIMINER & PENDAHULUAN]
Slide 01: Cover Resmi Akademik (Logo UIN SGD & Fisika, Judul Lengkap, Peneliti NIM 1237030018, Pembimbing I & II)
Slide 02: Latar Belakang (Alur Berantai Kausalitas TikZ: Craig 2018 -> Shi 2016 -> Satyanarayanan 2017 -> MediaPipe -> Gap Research Emas)
Slide 03: Rumusan Masalah (3 Butir Verbatim Bab 1) & Batasan Masalah (5 Butir Verbatim Bab 1)
Slide 04: Tujuan Penelitian (3 Butir Verbatim Bab 1) & Tempat/Waktu (Jan-Feb 2026, Lab Mekatronika PEI Purwakarta)

[BAGIAN II: PROFIL MITRA INDUSTRI]
Slide 05: Profil Mitra: Politeknik Enjinering Indorama (PEI) Purwakarta, Sejarah PT Indorama Synthetics Tbk, & Roadmap Mekatronika

[BAGIAN III: DASAR TEORI (SELURUH MATERI BAB III BERBASIS GAMBAR ASLI & FORMULA)]
Slide 06: Dasar Teori: Sistem Visi Komputer Tertanam & Edge Computing RPi 5 [Gambar 3.1 Antarmuka Dobot] (Szeliski 2022; Satyanarayanan 2017)
Slide 07: Dasar Teori: Ekstraksi Fitur Geometris & MediaPipe 21 Landmarks (63 Koordinat) [Gambar 3.2 Topologi Landmark] (Lugaresi 2019; Zhang 2020)
Slide 08: Dasar Teori: Pengenalan SIBI Berbasis Deep Neural Networks (DNN) [Formulasi Matematis Lapisan ReLU, Softmax, & Cross-Entropy] (Goodfellow 2016)
Slide 09: Dasar Teori: Kinematika Manipulator 4-DOF [Formula Lengkap Forward & Inverse Kinematics X,Y,Z & Theta 1..4] (Craig 2018; Lynch 2017)
Slide 10: Dasar Teori: Karakteristik Perangkat Keras Manipulator [Gambar 3.3 Dobot Magician & Gambar 3.4a meArm 4-DOF] (Dobot 2026; meArm 2026)

[BAGIAN IV: METODE PENELITIAN & DIAGRAM ALIR ASLI (BAB IV)]
Slide 11: Metode Penelitian: Alat dan Bahan Penelitian [Tabel 4.1 Spesifikasi Lengkap 13 Komponen Asli]
Slide 12: Metode Penelitian: Diagram Alir Penelitian [Gambar 4.1 TikZ Asli 6 Tahapan Metodologi]
Slide 13: Metode Penelitian: Perancangan Perangkat Keras (Isolasi Daya 5V DC meArm, USB Serial Dobot, GPIO RPi 5) + Foto Fisik
Slide 14: Metode Penelitian: Arsitektur Sistem Tertanam Raspberry Pi 5 [Gambar 5.1 TikZ Asli Arsitektur Dual-Mode]
Slide 15: Metode Penelitian: Diagram Alir Logika Piranti Lunak [Gambar 4.2 TikZ Asli Dual-Pipeline Mode SIBI & Teleoperasi]

[BAGIAN V: HASIL DAN PEMBAHASAN (KLAIM KUANTITATIF + GAMBAR ASLI + TABEL RIIL)]
Slide 16: Hasil dan Pembahasan: Pelatihan Model DNN SIBI Konvergen pada 100 Epoch [Gambar 5.2a Akurasi vs Epoch & Gambar 5.2b Loss vs Epoch]
Slide 17: Hasil dan Pembahasan: Pengujian Real-Time SIBI Menghasilkan Akurasi 96,73% [Gambar 5.4 CM Real-Time & Tabel 5.2 Rekapitulasi 520 Uji]
Slide 18: Hasil dan Pembahasan: Seluruh 5 Perintah SIBI Berhasil Diterjemahkan ke Respons Fisik meArm [Gambar 5.5 & Tabel 5.3 Respons Servo]
Slide 19: Hasil dan Pembahasan: Evaluasi Pemetaan 6 Arah Spasial Teleoperasi Dobot 100% Valid [Gambar 5.6 & Tabel 5.4 Pemetaan Arah]
Slide 20: Hasil dan Pembahasan: Presisi Spasial Rata-rata 1,90 mm dan Waktu Respons 87,25 ms pada Dobot [Tabel 5.5 & Formula Galat Euclidean]
Slide 21: Hasil dan Pembahasan: Rangkuman Kinerja Sistem Keseluruhan [Tabel 5.6 Rekapitulasi & Tautan Google Drive Video Daring]

[BAGIAN VI: DOKUMENTASI, KESIMPULAN, & PENUTUP]
Slide 22: Dokumentasi Implementasi Purwarupa & Stasiun Uji Eksperimen [Galeri Gambar 6.1, 6.2, 6.5, 6.9, 6.15, 6.17 dari Lampiran]
Slide 23: Kesimpulan Penelitian (3 Butir Kuantitatif Asli Bab 6) & Saran Pengembangan Lanjutan (5 Butir Asli Bab 6)
Slide 24: Daftar Pustaka Utama (Format Resmi APA/IEEE Craig 2018, Lugaresi 2019, Shi 2016, dll.) & Sesi Tanya Jawab (Q&A)
```

---

## 4. Lokasi Master dan Script Pembangun

* **Script Generator**: [`~/LAPORAN-KP-Fahry-Rizky-Samsudin/scripts/generate_laporan_kp_deck_full.py`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/scripts/generate_laporan_kp_deck_full.py)
* **Master PPTX**: [`~/LAPORAN-KP-Fahry-Rizky-Samsudin/Laporan_KP_Fahry_Rizky_Samsudin.pptx`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Laporan_KP_Fahry_Rizky_Samsudin.pptx)
* **Master PDF**: [`~/LAPORAN-KP-Fahry-Rizky-Samsudin/Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf`](file:///data/data/com.termux/files/home/LAPORAN-KP-Fahry-Rizky-Samsudin/Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf)
* **Folder HP**: `/storage/emulated/0/Akademik/Laporan KP/`
