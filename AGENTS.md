# AGENTS.md — Panduan Sistem & Pengetahuan Proyek Laporan Kerja Mandiri Terpantau (KP)

Dokumen ini berisi identitas proyek, arsitektur naskah LaTeX, konvensi gambar, serta integrasi keterampilan (*skills*) dan alat (*scripts*) terhubung untuk agen kecerdasan buatan (*AI assistant*).

---

## 1. Identitas Proyek
- **Judul**: *Rancang Bangun Sistem Visi Komputer Tertanam Berbasis Raspberry Pi 5 untuk Kendali Robot 4-DOF: Teleoperasi Dobot Magician dan Pengenalan SIBI pada meArm*
- **Peneliti**: Fahry Rizky Samsudin (NIM: 1237030018)
- **Jurusan / Institusi**: Jurusan Fisika, Fakultas Sains dan Teknologi, Universitas Islam Negeri Sunan Gunung Djati Bandung
- **Lokasi Penelitian**: Laboratorium Program Studi Teknologi Mekatronika, Politeknik Enjinering Indorama (PEI), Purwakarta, Jawa Barat
- **Tahun**: 2026

---

## 2. Struktur Direktori Repositori

```
LAPORAN-KP-Fahry-Rizky-Samsudin/
├── main.tex                    # Berkas master LaTeX
├── references.bib              # Bibliografi BibTeX lengkap (18 entri)
├── build.sh                    # Skrip build otomatis pdflatex + bibtex
├── Header/                     # Halaman preliminer skripsi/laporan
│   ├── sampul.tex              # Halaman sampul utama
│   ├── Keaslian.tex            # Surat pernyataan keaslian bermaterai
│   ├── persetujuan.tex         # Lembar persetujuan pembimbing
│   ├── pengesahan.tex          # Lembar pengesahan sidang
│   ├── abstrak.tex             # Abstrak Bahasa Indonesia
│   ├── abstract.tex            # Abstract Bahasa Inggris
│   ├── prakata.tex             # Kata pengantar
│   ├── d_isi.tex               # Daftar isi
│   ├── d_gambar.tex            # Daftar gambar
│   └── d_tabel.tex             # Daftar tabel
├── Isi/                        # Naskah utama bab laporan
│   ├── Bab1_Pendahuluan.tex    # Bab I: Latar Belakang, Rumusan, Batasan, Tujuan, Manfaat, Waktu
│   ├── Bab2_Profil_Industri.tex # Bab II: Profil Politeknik Enjinering Indorama, Sejarah, Visi Misi, Roadmap
│   ├── Bab3_Tinjauan_Pustaka.tex # Bab III: Embedded CV, Raspberry Pi 5, SIBI DNN, MediaPipe, Kinematika 4-DOF
│   ├── Bab4_Metode_Penelitian.tex # Bab IV: Alat/Bahan, Diagram Alir TikZ, Hardware & Software Design
│   ├── Bab5_Hasil_dan_Pembahasan.tex # Bab V: Hasil Sistem TikZ, Akurasi SIBI, Teleoperasi Dobot, Kinematika meArm
│   ├── Bab6_Kesimpulan_dan_Saran.tex # Bab VI: Kesimpulan & Saran
│   └── Lampiran.tex            # Lampiran 1-4: Kode Python Tkinter, Teleoperasi Dobot, Firmware Arduino, Foto Lab
├── Gambar/                     # 33 Berkas gambar resolusi asli (XObject stream)
├── .agents/                    # [SYMLINK] Akses penuh ke 2.220+ skills & rules dari PROPOSAL-TA
├── scripts/                    # [SYMLINK] Akses skrip otomasi & utilitas dari PROPOSAL-TA
└── .superpowers/               # [SYMLINK] Alat bantu superpowers dari PROPOSAL-TA
```

---

## 3. Integrasi Shared Skills & Scripts
Repositori ini terhubung langsung (*symbolic link*) dengan repositori `PROPOSAL-TA-Fahry-RIzky-Samsudin`:
* **Skills**: Seluruh 2.220+ keterampilan agen di `.agents/skills` dapat dipanggil secara langsung.
* **Scripts**: Skrip pengunduh literatur, parser DOI, dan pembuat diagram dapat dieksekusi langsung dari folder `scripts/`.
