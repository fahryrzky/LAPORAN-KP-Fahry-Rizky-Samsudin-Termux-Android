# Laporan Kerja Mandiri Terpantau (LaTeX)
**Fahry Rizky Samsudin (1237030018)**  
*Jurusan Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung*

---

## Judul Laporan
> **Rancang Bangun Sistem Visi Komputer Tertanam Berbasis Raspberry Pi 5 untuk Kendali Robot 4-DOF: Teleoperasi Dobot Magician dan Pengenalan SIBI pada meArm**

## Ringkasan Proyek
Repositori ini merupakan naskah lengkap modular LaTeX hasil migrasi dari naskah PDF asli Laporan KP (68 halaman). Berkas ini mencakup:
1. **Bab I s.d. VI**: Seluruh naskah lengkap, rumus kinematika maju/balikan, tabel pengujian, dan analisis kinerja.
2. **Gambar Vektor & Resolusi Asli**: Diagram alir (Gambar 4.1) dan arsitektur sistem (Gambar 5.1) direkonstruksi dalam **LaTeX TikZ murni**. Seluruh 33 gambar foto dan grafik diekstrak dalam resolusi penuh tanpa pemotongan margin.
3. **Lampiran Lengkap**: Kode program Python pengenalan SIBI, kode program Python teleoperasi Dobot Magician, firmware Arduino C++, dan 19 dokumentasi foto eksperimental.
4. **Shared Skills & Scripts**: Terhubung secara symlink ke folder `PROPOSAL-TA` untuk kemudahan akses utilitas bersama.

## Cara Kompilasi
Untuk mengompilasi naskah menjadi PDF:
```bash
./build.sh
```
Atau unggah seluruh folder ini ke platform [Overleaf](https://www.overleaf.com/) dengan memilih `main.tex` sebagai *root document*.
