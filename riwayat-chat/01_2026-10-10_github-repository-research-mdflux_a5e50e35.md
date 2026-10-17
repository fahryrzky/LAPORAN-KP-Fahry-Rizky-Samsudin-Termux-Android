# GitHub Repository Research Mdflux
- **ID Percakapan**: `a5e50e35-283e-4903-9d32-71a64c540862`
- **Waktu Terakhir Aktif**: `2026-10-10 12:22:24`
- **Total Langkah**: `54`

---

## 👤 User (2026-10-10T12:14:43Z)

https://github.com/ibrahimqureshae/mdflux.git tolomg kamu meluncur ke repo ini dan riset terkait apa isinya

## 🤖 Assistant (2026-10-10T12:19:35Z)

Hasil riset mendalam mengenai repositori [ibrahimqureshae/mdflux](https://github.com/ibrahimqureshae/mdflux):

---

### 1. Apa itu MDFlux?
**MDFlux** adalah aplikasi desktop *local-first* (berjalan sepenuhnya di komputer lokal secara offline) berbasis open source (lisensi MIT) yang dirancang untuk **mengonversi berbagai jenis dokumen menjadi format Markdown bersih dan terstruktur yang siap dikonsumsi oleh AI / LLM (*AI-ready Markdown*)**.

Aplikasi ini dibangun di atas engine konversi [Microsoft MarkItDown](https://github.com/microsoft/markitdown), namun dibungkus dengan antarmuka desktop modern, engine OCR on-device, pemrosesan batch, dan modul pembersih (*cleanup*) teks.

---

### 2. Masalah yang Diselesaikan & Keunggulannya
- **Hemat Token & Biaya**: Mengirim dokumen langsung sebagai gambar ke *vision model* memakan ribuan token per halaman. MDFlux mengubah dokumen ke Markdown yang jauh lebih ringkas, menghasilkan penghematan token **2× hingga 6× lipat**.
- **Membaca PDF Hasil Scan (Scanned PDF)**: Ekstraktor teks biasa sering menghasilkan teks kosong pada PDF hasil scan. MDFlux dilengkapi OCR lokal untuk mengekstrak teksnya secara akurat.
- **Privasi Penuh (Local-First)**: Pemrosesan terjadi langsung di perangkat Anda tanpa mengirim dokumen sensitif (seperti kontrak atau data rahasia) ke cloud.
- **Batch Processing**: Mampu mengonversi satu folder penuh berisi aneka format file hanya dengan sekali *drag-and-drop*.

---

### 3. Format Dokumen yang Didukung
- **Dokumen Teks & Kantor**: PDF, Word (`.docx`), PowerPoint (`.pptx`), Excel (`.xlsx`, `.xls`), EPUB, HTML, CSV, JSON, XML, TXT, MD.
- **Citra / Scan**: Gambar berbasis teks via OCR.
- **Audio**: Transkripsi audio lokal ke teks.

---

### 4. Fitur-Fitur Kunci
1. **Mode Pembersihan (*Cleanup Modes*)**:
   - *Off*: Konversi standar apa adanya.
   - *Rule-based*: Membersihkan karakter sampah, layout patah, dan spasi berulang tanpa AI.
   - *AI Cleanup*: Merapikan teks menggunakan model AI lokal (Ollama / LM Studio) atau API cloud (OpenAI, DeepSeek, Groq, Ope
<truncated 367 bytes>
*Lite**: Ukuran arsip sangat kecil (~5 MB), memasang dependensi Python secara otomatis saat pertama kali dibuka.
   - **Full**: Dilengkapi *bundled immutable runtime* siap pakai sepenuhnya offline tanpa unduhan tambahan.

---

### 5. Arsitektur & Tech Stack
- **Desktop Shell**: [Tauri v2](https://tauri.app/) (berbasis **Rust**) untuk performa tinggi dan konsumsi memori rendah.
- **Frontend UI**: [Svelte 5](https://svelte.dev/) + Vite + TypeScript.
- **Backend / Sidecar Engine**: Subproses Python yang mengendalikan:
  - `markitdown` (inti parser dokumen).
  - `RapidOCR`, `onnxruntime`, dan `pypdfium2` (mesin OCR lokal).
  - `faster-whisper` (transkripsi audio).
  - `httpx` & `openai` SDK (AI cleanup).
- **Proses IPC**: Tauri berkomunikasi dengan skrip worker Python (`worker.py`) menggunakan *stream JSON lines* (stdin/stdout) dengan pemantauan progres dan *heartbeat*.

---

### 6. Struktur Direktori Repositori
```text
mdflux/
├── app/
│   ├── src/                  # Frontend Svelte 5 (UI, tema, routing, tampilan Markdown)
│   ├── src-tauri/            # Tauri 2 (Rust) core, manajemen IPC, platform launcher
│   │   └── resources/sidecar/# Skrip Python (worker.py) dan requirements lockfiles
├── docs/                     # Dokumentasi cross-platform & panduan setup
├── tools/                    # Tool verifikasi dependensi, roda wheel, dan release
├── scripts/                  # Skrip automasi build
├── tests/                    # Fixture pengujian dokumen
└── ROADMAP.md                # Rencana fitur masa depan
```

---

### 7. Roadmap Mendatang
- **MCP Server (Model Context Protocol)**: Agar asisten AI (seperti Claude Code, Cursor, dll.) dapat langsung memanggil MDFlux untuk mengonversi dokumen.
- **Mode CLI Headless (`mdflux convert`)**: Konversi via terminal untuk kebutuhan scripting dan pipeline CI/CD.
- **Dukungan macOS**: Build native untuk Apple Silicon dan Intel.
- **Sertifikasi Kode (*Code Signing*)**: Menghilangkan peringatan Windows SmartScreen.

## 👤 User (2026-10-10T12:21:27Z)

bolej deh kita install ini dikita tapi aku mau ngibah pdf ke format latex bisa nggak

## 🤖 Assistant (2026-10-10T12:22:12Z)

Secara singkat: **MDFlux sendiri tidak bisa langsung mengubah PDF ke LaTeX**, dan ada dua alasan teknis utama:

---

### 1. Keterbatasan MDFlux untuk Kebutuhan Ini
1. **Format Output Hanya Markdown**:
   MDFlux secara spesifik dirancang untuk menghasilkan file **Markdown (`.md`)**. Repositori ini tidak memiliki fitur untuk mengekspor atau menyusun sintaks dokumen LaTeX (`.tex`).
2. **Lingkungan Sistem (Termux Android / ARM64)**:
   Perangkat yang sedang kita gunakan saat ini berjalan di atas **Android `aarch64` (Termux)**. MDFlux adalah aplikasi GUI Desktop berbasis **Tauri 2 (Rust) + WebKitGTK** yang hanya mendukung desktop x64 (Windows/Linux glibc). Pengembangnya bahkan secara eksplisit menyatakan di `ROADMAP.md` bahwa arsitektur `ARM64` berada di luar jangkauan (*out of scope*).

---

### 2. Cara Alternatif untuk Mengubah PDF ke LaTeX

Tergantung pada jenis isi dokumen PDF Anda, berikut solusi yang jauh lebih cocok dan bisa kita jalankan langsung di Termux:

#### Opsi A: Menggunakan AI / LLM Multimodal (Sangat Direkomendasikan)
> **Paling ideal jika PDF berisi rumus matematika, simbol ilmiah, atau tabel akademik.**
- Converter biasa umumnya gagal mengenali rumus matematika dan hanya membaca simbolnya secara berantakan.
- Model AI (seperti Gemini API atau OpenAI) dapat membaca halaman PDF dan langsung merekonstruksinya menjadi dokumen LaTeX utuh yang rapi (menggunakan `\documentclass`, package `amsmath`, format persamaan `\begin{equation}`, dll.).
- **Solusi**: Kita bisa membuatkan **skrip Python sederhana di Termux** yang membaca file PDF Anda, mengirimkannya ke API, lalu menyimpan hasilnya sebagai file `.tex`.

#### Opsi B: Pipeline CLI Lokal via Pandoc (`PDF -> Markdown -> LaTeX`)
> **Cocok jika PDF didominasi teks biasa (buku, novel, artikel naratif tanpa rumus rumit).**
- Kita bisa pasang `pandoc` dan library PDF di Termux:
  ```bash
  pkg install pandoc poppler
  ```
- Ekstrak teks/markdown dari PDF terlebih dahulu, lalu konversi ke LaTeX menggunakan Pandoc:
  ```bash
  pandoc dokumen.md -o dokumen.tex
  ```

---

### Rekomendasi Selanjutnya
Bolehkah tahu **seperti apa karakteristik file PDF yang ingin Anda ubah**?
1. Apakah dokumen ilmiah/akademik yang memuat **banyak rumus matematika dan tabel**?
2. Atau dokumen **teks bacaan umum**?

Jika Anda mau, saya bisa buatkan skrip Python langsung di workspace ini untuk mengonversi PDF Anda ke `.tex`!
