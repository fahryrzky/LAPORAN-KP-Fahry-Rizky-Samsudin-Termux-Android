#!/usr/bin/env bash
# Script kompilasi LaTeX Laporan KP Fahry Rizky Samsudin
set -e

echo "=== Memulai Kompilasi LaTeX Laporan KP ==="

if command -v pdflatex >/dev/null 2>&1; then
    echo "1. Menjalankan pdflatex (Pass 1)..."
    pdflatex -interaction=nonstopmode main.tex
    
    if command -v bibtex >/dev/null 2>&1; then
        echo "2. Menjalankan bibtex..."
        bibtex main || true
    fi

    echo "3. Menjalankan pdflatex (Pass 2)..."
    pdflatex -interaction=nonstopmode main.tex

    echo "4. Menjalankan pdflatex (Pass 3 - Final)..."
    pdflatex -interaction=nonstopmode main.tex

    echo "Kompilasi selesai! Output PDF: main.pdf"
else
    echo "[INFO] pdflatex belum terpasang di Termux."
    echo "Anda dapat mengompilasi proyek ini di Overleaf, VS Code (LaTeX Workshop), atau menginstal texlive di Termux:"
    echo "  pkg install texlive-installer"
fi
