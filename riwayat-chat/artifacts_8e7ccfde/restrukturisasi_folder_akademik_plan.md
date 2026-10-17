# Rencana Implementasi: Restrukturisasi Folder Akademik di Penyimpanan Internal HP

## Deskripsi Tujuan
Merapikan tata kelola direktori berkas akademik pada penyimpanan internal perangkat Android (`/storage/emulated/0/`) agar rapi, tertata, dan mudah ditemukan pada File Manager HP, dengan mengelompokkan dokumen ke dalam folder induk **`Akademik`**, serta menstandarkan nama berkas hasil akhir menjadi bersih tanpa akhiran `Compiled` dan tanpa tanda garis bawah `_`:
* `/storage/emulated/0/Akademik/Laporan KP/`
* `/storage/emulated/0/Akademik/Proposal Tugas Akhir/`

---

## User Review Required

> [!IMPORTANT]
> **Standarisasi Nama Berkas & Skema Migrasi:**
> - Berkas Laporan KP hasil kompilasi diubah namanya dari `Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf` menjadi:
>   👉 **`Laporan KP Fahry Rizky Samsudin.pdf`** *(tanpa kata compiled dan tanpa underscore)*.
> - Berkas Proposal Tugas Akhir sudah dalam format rapi:
>   👉 **`Proposal Fahry Rizky Samsudin.pdf`**.
> - Seluruh isi dari direktori lama:
>   1. `/storage/emulated/0/laporan kp/` $\rightarrow$ dipindahkan dan diganti nama ke `/storage/emulated/0/Akademik/Laporan KP/`
>   2. `/storage/emulated/0/proposal tugas akhir/` $\rightarrow$ dipindahkan ke `/storage/emulated/0/Akademik/Proposal Tugas Akhir/`
> - Direktori lama yang sudah kosong dibersihkan agar penyimpanan internal tetap bersih.

---

## Open Questions
Tidak ada pertanyaan pemblokir. Format nama berkas dan hierarki folder telah disesuaikan dengan instruksi pengguna.

---

## Rencana Perubahan (Proposed Changes)

```
/storage/emulated/0/
├── [DELETE] laporan kp/
├── [DELETE] proposal tugas akhir/
└── [NEW] Akademik/
    ├── [NEW] Laporan KP/
    │   └── Laporan KP Fahry Rizky Samsudin.pdf   # [RENAME] Bersih tanpa underscore & tanpa 'Compiled'
    └── [NEW] Proposal Tugas Akhir/
        ├── Proposal Fahry Rizky Samsudin.pdf
        ├── Proposal_TA_Fahry_Rizky_Samsudin.pptx
        ├── Laporan KP - Fahry Rizky Samsudin (1237030018)-signed (2).pdf
        └── Desain & Dokumentasi Mekatronik (8 file gambar)
```

---

### Tahap 1: Pembuatan Struktur Direktori Baru
```bash
mkdir -p "/storage/emulated/0/Akademik/Laporan KP"
mkdir -p "/storage/emulated/0/Akademik/Proposal Tugas Akhir"
```

### Tahap 2: Pemindahan & Penggantian Nama Berkas
```bash
# Pindahkan berkas Laporan KP dan ubah nama tanpa _ serta tanpa Compiled
mv "/storage/emulated/0/laporan kp/Laporan_KP_Fahry_Rizky_Samsudin_Compiled.pdf" \
   "/storage/emulated/0/Akademik/Laporan KP/Laporan KP Fahry Rizky Samsudin.pdf"

# Pindahkan seluruh berkas Proposal Tugas Akhir
mv /storage/emulated/0/proposal\ tugas\ akhir/* "/storage/emulated/0/Akademik/Proposal Tugas Akhir/"
```

### Tahap 3: Pembersihan Folder Lama
```bash
rmdir "/storage/emulated/0/laporan kp"
rmdir "/storage/emulated/0/proposal tugas akhir"
```

### Tahap 4: Pembaruan Dokumentasi Riwayat
Memperbarui catatan path ekspor di [`MEMORI_RIWAYAT_PENELITIAN.md`](file:///data/data/com.termux/files/home/PROPOSAL-TA-Fahry-RIzky-Samsudin/MEMORI_RIWAYAT_PENELITIAN.md) agar selaras dengan path baru `/storage/emulated/0/Akademik/Proposal Tugas Akhir/`.

---

## Verification Plan

### Automated Tests
1. **Verifikasi Keberadaan Folder Induk & Subfolder:**
   ```bash
   test -d "/storage/emulated/0/Akademik/Laporan KP" && test -d "/storage/emulated/0/Akademik/Proposal Tugas Akhir"
   ```
2. **Verifikasi Keberadaan & Nama Berkas Laporan KP:**
   ```bash
   ls -la "/storage/emulated/0/Akademik/Laporan KP/Laporan KP Fahry Rizky Samsudin.pdf"
   ```
3. **Verifikasi Berkas Proposal & Aset Gambar:**
   ```bash
   ls -la "/storage/emulated/0/Akademik/Proposal Tugas Akhir/Proposal Fahry Rizky Samsudin.pdf"
   ```
4. **Verifikasi Penghapusan Folder Lama:**
   ```bash
   test ! -d "/storage/emulated/0/laporan kp" && test ! -d "/storage/emulated/0/proposal tugas akhir"
   ```

### Manual Verification
1. Buka aplikasi **File Manager** / Pengelola File di HP Android.
2. Masuk ke **Penyimpanan Internal > `Akademik`**.
3. Periksa subfolder:
   - **`Laporan KP`**: Berisi file `Laporan KP Fahry Rizky Samsudin.pdf`.
   - **`Proposal Tugas Akhir`**: Berisi `Proposal Fahry Rizky Samsudin.pdf`, slide PPTX, dan gambar dokumentasi.
