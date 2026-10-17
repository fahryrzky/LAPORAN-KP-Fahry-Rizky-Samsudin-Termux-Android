# Rencana Implementasi: Konfigurasi Otomatisasi Persetujuan (Auto-Approve) Antigravity CLI

## Deskripsi Tujuan
Mengonfigurasi lingkungan Antigravity CLI (`agy`) dan shell Termux agar asisten AI dapat melakukan pengeditan berkas dan menjalankan perintah terminal secara otonom tanpa memunculkan permintaan konfirmasi berulang (*pop-up accept/allow*):
1. Mengubah default `agentMode` pada `settings.json` menjadi `accept-edits`.
2. Menambahkan alias shell di `~/.bashrc` dengan flag `--dangerously-skip-permissions` dan `--mode accept-edits`.

---

## User Review Required

> [!IMPORTANT]
> **Dampak Perubahan Perilaku Asisten:**
> - **Perintah Terminal**: Flag `--dangerously-skip-permissions` akan membuat CLI mengizinkan (*auto-approve*) semua tool/perintah terminal tanpa jeda konfirmasi "Allow".
> - **Edit Berkas**: Mode `accept-edits` akan langsung menerapkan perubahan kode/berkas tanpa menunggu Anda menekan tombol "Accept".
> - Anda tetap memegang kendali penuh melalui riwayat interaksi dan dapat membatalkan atau mengembalikan mode kapan saja (misal via shortcut `Shift + Tab` atau menghapus alias).

---

## Open Questions
Tidak ada pertanyaan pemblokir. Perubahan terisolasi pada berkas konfigurasi lokal.

---

## Rencana Perubahan (Proposed Changes)

### 1. Konfigurasi Antigravity CLI
#### [MODIFY] [`~/.gemini/antigravity-cli/settings.json`](file:///data/data/com.termux/files/home/.gemini/antigravity-cli/settings.json)
* Mengubah nilai `agentMode` dari `"plan"` menjadi `"accept-edits"`:
  ```json
  "agentMode": "accept-edits"
  ```

### 2. Konfigurasi Shell Environment
#### [MODIFY] [`~/.bashrc`](file:///data/data/com.termux/files/home/.bashrc)
* Menambahkan alias `agy` agar setiap sesi baru berjalan tanpa prompt konfirmasi:
  ```bash
  alias agy="agy --dangerously-skip-permissions --mode accept-edits"
  ```

---

## Verification Plan

### Automated Tests
1. **Validasi Format JSON `settings.json`**:
   ```bash
   python3 -c "import json; d = json.load(open('/data/data/com.termux/files/home/.gemini/antigravity-cli/settings.json')); assert d['agentMode'] == 'accept-edits'; print('settings.json VALID: agentMode =', d['agentMode'])"
   ```
2. **Validasi Alias di `.bashrc`**:
   ```bash
   bash -c "source ~/.bashrc && alias agy"
   ```

### Manual Verification
1. Saat membuka sesi baru dengan mengetik `agy`, perhatikan status line di terminal akan menunjukkan mode `accept-edits`.
2. Saat AI menjalankan perintah shell atau mengedit berkas, proses akan langsung berjalan tanpa pop-up persetujuan.
