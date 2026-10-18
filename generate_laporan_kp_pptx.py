#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Presentasi Laporan Kerja Mandiri Terpantau (KP) - Standar Referensi Gilang
Peneliti : Fahry Rizky Samsudin (NIM: 1237030018)
Jurusan  : Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
Lokasi   : Laboratorium Teknologi Mekatronika, Politeknik Enjinering Indorama (PEI)
Output   :
  1. Laporan_KP_Fahry_Rizky_Samsudin.pptx (17 Slide Widescreen 16:9)
  2. Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf (17 Halaman Widescreen 16:9 Identik)
"""

import os
import sys
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = "/storage/emulated/0/Projek/LAPORAN-KP-Fahry-Rizky-Samsudin-Termux-Android"
GAMBAR_DIR = os.path.join(BASE_DIR, "Gambar")
EQ_DIR = os.path.join(GAMBAR_DIR, "equations")

OUTPUT_PPTX = os.path.join(BASE_DIR, "Laporan_KP_Fahry_Rizky_Samsudin.pptx")
OUTPUT_PDF = os.path.join(BASE_DIR, "Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf")

# Palet Warna Khas Referensi Gilang (Navy Pekat, Emas/Amber, Biru Akademik, Putih Bersih)
C_BG_SLIDE    = RGBColor(244, 247, 251)  # #F4F7FB
C_NAVY_DARK   = RGBColor(15, 30, 68)     # #0F1E44 (Header Banner & Kartu Teori Gelap)
C_NAVY_CARD   = RGBColor(23, 43, 92)     # #172B5C (Kartu Konten Navy)
C_NAVY_MID    = RGBColor(30, 58, 138)    # #1E3A8A
C_BLUE_ACCENT = RGBColor(2, 132, 199)    # #0284C7
C_GOLD_ACCENT = RGBColor(245, 158, 11)   # #F59E0B (Aksen Emas/Kuning Khas Gilang)
C_GOLD_LIGHT  = RGBColor(254, 243, 199)  # #FEF3C7
C_EMERALD     = RGBColor(5, 150, 105)    # #059669
C_EMR_LIGHT   = RGBColor(209, 250, 229)  # #D1FAE5
C_WHITE       = RGBColor(255, 255, 255)
C_SLATE_LIGHT = RGBColor(241, 245, 249)  # #F1F5F9
C_BORDER      = RGBColor(203, 213, 225)  # #CBD5E1
C_TEXT_DARK   = RGBColor(15, 23, 42)     # #0F172A
C_TEXT_BODY   = RGBColor(51, 65, 85)     # #334155
C_TEXT_MUTED  = RGBColor(100, 116, 139)  # #64748B

FONT_MAIN = "Arial"
TOTAL_SLIDES = 17


class GilangStyleDeck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]

    def add_slide(self, dark_bg=False):
        s = self.prs.slides.add_slide(self.blank_layout)
        bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_NAVY_DARK if dark_bg else C_BG_SLIDE
        bg.line.fill.background()
        return s

    def add_gilang_header(self, s, banner_title, page_num, subtitle_claim=None):
        """
        Header bergaya PPTX Gilang:
        - Pita panjang biru dongker (dark navy) di bagian atas dengan teks judul bab/bagian putih tebal
        - Badge nomor halaman kuning/emas di sebelah kanan
        - Opsional: Baris klaim kuantitatif / subjudul di bawah pita header
        """
        # Banner utama
        banner = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.45), Inches(0.22), Inches(11.65), Inches(0.62)
        )
        banner.fill.solid()
        banner.fill.fore_color.rgb = C_NAVY_DARK
        banner.line.color.rgb = C_GOLD_ACCENT
        banner.line.width = Pt(1.5)

        tf = banner.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.85)
        tf.margin_top = Inches(0.05)
        tf.margin_bottom = Inches(0.05)
        p = tf.paragraphs[0]
        p.text = banner_title.upper()
        p.font.name = FONT_MAIN
        title_len = len(banner_title)
        if title_len > 60:
            p.font.size = Pt(15.0)
            p.line_spacing = 1.1
        elif title_len > 40:
            p.font.size = Pt(17.0)
            p.line_spacing = 1.15
        else:
            p.font.size = Pt(20.0)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

        # Badge Nomor Slide di Kanan Atas
        badge = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(12.22), Inches(0.22), Inches(0.66), Inches(0.62)
        )
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_GOLD_ACCENT
        badge.line.color.rgb = C_NAVY_DARK
        badge.line.width = Pt(1.5)

        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = f"{page_num:02d}"
        p_b.font.name = FONT_MAIN
        p_b.font.size = Pt(18)
        p_b.font.bold = True
        p_b.font.color.rgb = C_NAVY_DARK
        p_b.alignment = PP_ALIGN.CENTER

        # Jika ada kalimat klaim kuantitatif di atas konten (khas slide Hasil & Pembahasan Gilang)
        if subtitle_claim:
            claim_box = s.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.45), Inches(0.92), Inches(12.43), Inches(0.48)
            )
            claim_box.fill.solid()
            claim_box.fill.fore_color.rgb = C_GOLD_LIGHT
            claim_box.line.color.rgb = C_GOLD_ACCENT
            claim_box.line.width = Pt(1.2)

            tf_c = claim_box.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = Inches(0.15)
            tf_c.margin_right = Inches(0.15)
            tf_c.margin_top = Inches(0.04)
            tf_c.margin_bottom = Inches(0.04)
            p_c = tf_c.paragraphs[0]
            p_c.text = subtitle_claim
            p_c.font.name = FONT_MAIN
            p_c.font.size = Pt(11.5)
            p_c.font.bold = True
            p_c.font.color.rgb = C_NAVY_DARK
            p_c.alignment = PP_ALIGN.LEFT

    def add_footer(self, s, page_num):
        line = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.45), Inches(7.12), Inches(12.43), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = C_BORDER
        line.line.fill.background()

        tb = s.shapes.add_textbox(Inches(0.45), Inches(7.15), Inches(10.5), Inches(0.28))
        p = tb.text_frame.paragraphs[0]
        p.text = "Seminar Kerja Praktik | Fahry Rizky Samsudin (1237030018) | Fisika FST UIN Sunan Gunung Djati Bandung"
        p.font.name = FONT_MAIN
        p.font.size = Pt(9.0)
        p.font.color.rgb = C_TEXT_MUTED

        tb_r = s.shapes.add_textbox(Inches(11.0), Inches(7.15), Inches(1.88), Inches(0.28))
        pr = tb_r.text_frame.paragraphs[0]
        pr.text = f"Slide {page_num} / {TOTAL_SLIDES}"
        pr.font.name = FONT_MAIN
        pr.font.size = Pt(9.0)
        pr.font.bold = True
        pr.font.color.rgb = C_NAVY_MID
        pr.alignment = PP_ALIGN.RIGHT

    def add_card(self, s, left, top, width, height, bg=C_WHITE, border=C_BORDER, lw=1.2):
        c = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        c.fill.solid()
        c.fill.fore_color.rgb = bg
        if border:
            c.line.color.rgb = border
            c.line.width = Pt(lw)
        else:
            c.line.fill.background()
        return c

    def add_header_card(self, s, left, top, width, height, title_text, header_bg=C_NAVY_DARK, header_fg=C_WHITE, card_bg=C_WHITE, border=C_NAVY_MID):
        """Kartu dengan pita judul di bagian atas (khas kartu Gilang)."""
        card = self.add_card(s, left, top, width, height, bg=card_bg, border=border, lw=1.5)
        hbar = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.44))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = header_bg
        hbar.line.color.rgb = border
        hbar.line.width = Pt(1.2)
        p = hbar.text_frame.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_MAIN
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = header_fg
        p.alignment = PP_ALIGN.CENTER
        return card

    def add_picture_fit(self, s, img_path, left, top, max_w, max_h, caption=None, cap_color=C_TEXT_DARK, border=False):
        if not os.path.exists(img_path):
            print(f"[WARN] Gambar tidak ditemukan: {img_path}")
            return None
        im = Image.open(img_path)
        iw, ih = im.size
        aspect = iw / float(ih)

        cap_h = Inches(0.28) if caption else Inches(0)
        avail_h = max_h - cap_h

        def _to_in(val):
            return val.inches if hasattr(val, 'inches') else float(val) / 914400.0

        bw = _to_in(max_w)
        bh = _to_in(avail_h)

        if (bw / bh) > aspect:
            ch = bh
            cw = ch * aspect
        else:
            cw = bw
            ch = cw / aspect

        fx = _to_in(left) + (bw - cw) / 2.0
        fy = _to_in(top) + (bh - ch) / 2.0

        if border:
            self.add_card(s, Inches(fx - 0.04), Inches(fy - 0.04), Inches(cw + 0.08), Inches(ch + 0.08), bg=C_WHITE, border=C_BORDER, lw=1.0)

        pic = s.shapes.add_picture(img_path, Inches(fx), Inches(fy), Inches(cw), Inches(ch))

        if caption:
            tb = s.shapes.add_textbox(left, Inches(fy + ch + 0.02), max_w, Inches(0.28))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
            p = tf.paragraphs[0]
            p.text = caption
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.0)
            p.font.bold = True
            p.font.color.rgb = cap_color
            p.alignment = PP_ALIGN.CENTER
        return pic

    def add_bullet(self, tf, bold_lead, body_text, pt=11.0, fg=C_TEXT_DARK, lead_fg=C_NAVY_MID, space_after=4):
        p = tf.paragraphs[0] if len(tf.paragraphs[0].text) == 0 else tf.add_paragraph()
        p.space_after = Pt(space_after)
        p.line_spacing = 1.15

        r0 = p.add_run()
        r0.text = "• "
        r0.font.name = FONT_MAIN
        r0.font.size = Pt(pt)
        r0.font.bold = True
        r0.font.color.rgb = C_GOLD_ACCENT

        if bold_lead:
            r1 = p.add_run()
            r1.text = bold_lead + " "
            r1.font.name = FONT_MAIN
            r1.font.size = Pt(pt)
            r1.font.bold = True
            r1.font.color.rgb = lead_fg

        r2 = p.add_run()
        r2.text = body_text
        r2.font.name = FONT_MAIN
        r2.font.size = Pt(pt)
        r2.font.color.rgb = fg

    def add_styled_table(self, s, left, top, width, height, headers, rows, col_widths=None, font_size=9.5, highlight_last=False):
        r_cnt = len(rows) + 1
        c_cnt = len(headers)
        t_shape = s.shapes.add_table(r_cnt, c_cnt, left, top, width, height)
        tbl = t_shape.table

        if col_widths and len(col_widths) == c_cnt:
            for i, w in enumerate(col_widths):
                tbl.columns[i].width = w

        for ci, h_text in enumerate(headers):
            cell = tbl.cell(0, ci)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_NAVY_DARK
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.text = h_text
            p.font.name = FONT_MAIN
            p.font.size = Pt(font_size)
            p.font.bold = True
            p.font.color.rgb = C_WHITE
            p.alignment = PP_ALIGN.CENTER

        for ri, r_data in enumerate(rows):
            is_last = (ri == len(rows) - 1) and highlight_last
            for ci, val in enumerate(r_data):
                cell = tbl.cell(ri + 1, ci)
                cell.fill.solid()
                if is_last:
                    cell.fill.fore_color.rgb = C_GOLD_LIGHT
                else:
                    cell.fill.fore_color.rgb = C_WHITE if ri % 2 == 0 else C_SLATE_LIGHT
                cell.vertical_anchor = MSO_ANCHOR.MIDDLE
                p = cell.text_frame.paragraphs[0]
                p.text = str(val)
                p.font.name = FONT_MAIN
                p.font.size = Pt(font_size - 0.3)
                p.font.bold = is_last or (ci == 0)
                p.font.color.rgb = C_NAVY_DARK if is_last else C_TEXT_DARK
                p.alignment = PP_ALIGN.CENTER if (ci == 0 or ci >= c_cnt - 2) else PP_ALIGN.LEFT
        return t_shape


def build_kp_pptx():
    deck = GilangStyleDeck()

    # =========================================================================
    # SLIDE 1: COVER SEMINAR KP (GAYA SLIDE_REF_1 GILANG)
    # =========================================================================
    s1 = deck.add_slide(dark_bg=True)
    bg_cover = os.path.join(GAMBAR_DIR, "cover_bg_kp.png")
    if os.path.exists(bg_cover):
        s1.shapes.add_picture(bg_cover, 0, 0, Inches(13.333), Inches(7.5))

    # Kiri Atas: Lokasi & Tahun
    tb_date = s1.shapes.add_textbox(Inches(0.6), Inches(0.42), Inches(3.8), Inches(0.45))
    p = tb_date.text_frame.paragraphs[0]
    p.text = "Bandung, 2026"
    p.font.name = FONT_MAIN
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    # Tengah Atas: Pill Putih Logo UIN + Fisika
    pill_logo = os.path.join(GAMBAR_DIR, "logo_uin_fisika_pill.png")
    if os.path.exists(pill_logo):
        deck.add_picture_fit(s1, pill_logo, Inches(4.9), Inches(0.25), Inches(3.533), Inches(1.15))

    # Kanan Atas: Jenis Sidang
    tb_sem = s1.shapes.add_textbox(Inches(8.8), Inches(0.42), Inches(3.9), Inches(0.45))
    p = tb_sem.text_frame.paragraphs[0]
    p.text = "Seminar Kerja Praktik"
    p.font.name = FONT_MAIN
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_ACCENT
    p.alignment = PP_ALIGN.RIGHT

    # Kotak Judul Tengah Beraksen Emas-Navy (Persis Slide 1 Gilang)
    title_card = deck.add_card(
        s1, Inches(0.85), Inches(1.65), Inches(11.633), Inches(2.15),
        bg=RGBColor(15, 30, 68), border=C_GOLD_ACCENT, lw=2.8
    )
    tb_t = s1.shapes.add_textbox(Inches(1.1), Inches(1.78), Inches(11.133), Inches(1.9))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    p.text = "RANCANG BANGUN SISTEM VISI KOMPUTER TERTANAM BERBASIS RASPBERRY PI 5 UNTUK KENDALI ROBOT 4-DOF: TELEOPERASI DOBOT MAGICIAN DAN PENGENALAN SIBI PADA MEARM"
    p.font.name = FONT_MAIN
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER
    p.line_spacing = 1.22

    # Nama & NIM di Tengah
    tb_auth = s1.shapes.add_textbox(Inches(3.0), Inches(3.98), Inches(7.333), Inches(0.85))
    tf_a = tb_auth.text_frame
    tf_a.word_wrap = True
    p1 = tf_a.paragraphs[0]
    p1.text = "Fahry Rizky Samsudin"
    p1.font.name = FONT_MAIN
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = C_GOLD_ACCENT
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf_a.add_paragraph()
    p2.text = "NIM. 1237030018"
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.alignment = PP_ALIGN.CENTER

    # 2 Kolom Dosen Pembimbing I & II
    # Kiri: Dosen Pembimbing I
    deck.add_card(s1, Inches(1.2), Inches(4.95), Inches(5.1), Inches(1.35), bg=RGBColor(23, 43, 92), border=C_BORDER, lw=1.2)
    tb_d1 = s1.shapes.add_textbox(Inches(1.35), Inches(5.05), Inches(4.8), Inches(1.15))
    tf_d1 = tb_d1.text_frame
    tf_d1.word_wrap = True
    p = tf_d1.paragraphs[0]
    p.text = "DOSEN PEMBIMBING I"
    p.font.name = FONT_MAIN
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p2 = tf_d1.add_paragraph()
    p2.text = "Dr. Moch Nurul Subkhi, M.Si."
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.alignment = PP_ALIGN.CENTER
    p3 = tf_d1.add_paragraph()
    p3.text = "NIP. 19810201 200912 1003 (UIN SGD Bandung)"
    p3.font.name = FONT_MAIN
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = C_SLATE_LIGHT
    p3.alignment = PP_ALIGN.CENTER

    # Kanan: Dosen Pembimbing II
    deck.add_card(s1, Inches(7.033), Inches(4.95), Inches(5.1), Inches(1.35), bg=RGBColor(23, 43, 92), border=C_BORDER, lw=1.2)
    tb_d2 = s1.shapes.add_textbox(Inches(7.183), Inches(5.05), Inches(4.8), Inches(1.15))
    tf_d2 = tb_d2.text_frame
    tf_d2.word_wrap = True
    p = tf_d2.paragraphs[0]
    p.text = "PEMBIMBING II (MITRA INDUSTRI)"
    p.font.name = FONT_MAIN
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p2 = tf_d2.add_paragraph()
    p2.text = "Dr. Emmanuel Agung N, S.T, M.T."
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.alignment = PP_ALIGN.CENTER
    p3 = tf_d2.add_paragraph()
    p3.text = "NIDN. 0407047801 (Politeknik Enjinering Indorama)"
    p3.font.name = FONT_MAIN
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = C_SLATE_LIGHT
    p3.alignment = PP_ALIGN.CENTER

    # Footer Institusi di Bawah
    tb_inst = s1.shapes.add_textbox(Inches(0.8), Inches(6.52), Inches(11.733), Inches(0.75))
    tf_i = tb_inst.text_frame
    tf_i.word_wrap = True
    p = tf_i.paragraphs[0]
    p.text = "JURUSAN FISIKA | FAKULTAS SAINS DAN TEKNOLOGI\nUNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI BANDUNG"
    p.font.name = FONT_MAIN
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 2: LATAR BELAKANG (ALUR CITRA + INFO FOOTER + GAP RESEARCH)
    # =========================================================================
    s2 = deck.add_slide()
    deck.add_gilang_header(s2, "Latar Belakang", 2)
    deck.add_footer(s2, 2)

    lb_img = os.path.join(GAMBAR_DIR, "Gambar1_1_latar_belakang_flowchart_asli.png")
    deck.add_picture_fit(s2, lb_img, Inches(0.42), Inches(0.92), Inches(12.49), Inches(6.12))

    # =========================================================================
    # SLIDE 3: RUMUSAN MASALAH & TUJUAN PENELITIAN (1 SLIDE 2 KOLOM SEJAJAR)
    # =========================================================================
    s3 = deck.add_slide()
    deck.add_gilang_header(s3, "Rumusan Masalah dan Tujuan Penelitian", 3)
    deck.add_footer(s3, 3)

    # Kolom Kiri: RUMUSAN MASALAH
    deck.add_header_card(
        s3, Inches(0.45), Inches(0.98), Inches(6.05), Inches(4.55),
        "RUMUSAN MASALAH", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT, card_bg=C_WHITE, border=C_NAVY_DARK
    )
    rm_items = [
        ("1.", "Bagaimana merancang dan mengimplementasikan sistem visi komputer tertanam (embedded computer vision) menggunakan Raspberry Pi 5 untuk kendali lengan robot 4-DOF?"),
        ("2.", "Bagaimana menerjemahkan sistem pengenalan Sistem Isyarat Bahasa Indonesia (SIBI) menjadi sinyal kendali mekanik pada lengan robot meArm?"),
        ("3.", "Bagaimana memetakan ekstraksi hand landmark dari MediaPipe menjadi pergerakan teleoperasi yang kontinu berdasarkan sistem koordinat spasial (X, Y, Z) pada lengan robot Dobot Magician?")
    ]
    for idx, (num, txt) in enumerate(rm_items):
        y_pos = Inches(1.55 + idx * 1.28)
        badge = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), y_pos, Inches(0.46), Inches(0.46))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_GOLD_ACCENT
        badge.line.fill.background()
        pb = badge.text_frame.paragraphs[0]
        pb.text = num
        pb.font.name = FONT_MAIN
        pb.font.size = Pt(13)
        pb.font.bold = True
        pb.font.color.rgb = C_NAVY_DARK
        pb.alignment = PP_ALIGN.CENTER

        tb = s3.shapes.add_textbox(Inches(1.20), y_pos - Inches(0.05), Inches(5.15), Inches(1.18))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = txt
        p.font.name = FONT_MAIN
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK
        p.line_spacing = 1.18

    # Kolom Kanan: TUJUAN PENELITIAN
    deck.add_header_card(
        s3, Inches(6.83), Inches(0.98), Inches(6.05), Inches(4.55),
        "TUJUAN PENELITIAN", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT, card_bg=C_WHITE, border=C_NAVY_DARK
    )
    tj_items = [
        ("1.", "Merancang bangun sistem antarmuka nirsentuh (contactless) untuk mengontrol manipulator robot 4-DOF melalui pemanfaatan visi komputer berbasis sistem tertanam Raspberry Pi 5."),
        ("2.", "Menguji dan menganalisis tingkat keberhasilan integrasi pengenalan SIBI sebagai metode instruksi kendali diskret pada manipulator meArm."),
        ("3.", "Mengimplementasikan dan mengevaluasi respons kinematis Dobot Magician saat dikendalikan secara real-time melalui sistem teleoperasi pelacakan tangan (hand tracking).")
    ]
    for idx, (num, txt) in enumerate(tj_items):
        y_pos = Inches(1.55 + idx * 1.28)
        badge = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.03), y_pos, Inches(0.46), Inches(0.46))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_EMERALD
        badge.line.fill.background()
        pb = badge.text_frame.paragraphs[0]
        pb.text = num
        pb.font.name = FONT_MAIN
        pb.font.size = Pt(13)
        pb.font.bold = True
        pb.font.color.rgb = C_WHITE
        pb.alignment = PP_ALIGN.CENTER

        tb = s3.shapes.add_textbox(Inches(7.58), y_pos - Inches(0.05), Inches(5.15), Inches(1.18))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = txt
        p.font.name = FONT_MAIN
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK
        p.line_spacing = 1.18

    # Bagian Bawah: BATASAN MASALAH (5 Poin Bab 1.3)
    deck.add_header_card(
        s3, Inches(0.45), Inches(5.68), Inches(12.43), Inches(1.32),
        "BATASAN MASALAH PENELITIAN (BAB 1.3)", header_bg=C_NAVY_MID, header_fg=C_WHITE, card_bg=C_SLATE_LIGHT, border=C_NAVY_MID
    )
    tb_bm = s3.shapes.add_textbox(Inches(0.62), Inches(6.14), Inches(12.1), Inches(0.82))
    tf_bm = tb_bm.text_frame
    tf_bm.word_wrap = True
    p = tf_bm.paragraphs[0]
    p.text = (
        "1. Komputasi lokal sepenuhnya pada Raspberry Pi 5 (tanpa cloud)   |   "
        "2. Pemrograman antarmuka & kinematika berbasis Python 3.9   |   "
        "3. Objek uji: manipulator 4-DOF meArm (mode SIBI) & Dobot Magician (mode teleoperasi)\n"
        "4. Ekstraksi 21 titik persendian tangan menggunakan framework MediaPipe   |   "
        "5. Pergerakan robot difokuskan pada penyelesaian Forward & Inverse Kinematics 3D (X, Y, Z)."
    )
    p.font.name = FONT_MAIN
    p.font.size = Pt(10.2)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.line_spacing = 1.22

    # =========================================================================
    # SLIDE 4: LANDASAN TEORI (1/3) - SUB-BAB 3.1, 3.2, DAN 3.7 LENGKAP
    # =========================================================================
    s4 = deck.add_slide()
    deck.add_gilang_header(
        s4, "Landasan Teori (1/3): Visi Tertanam, Edge Computing RPi 5, & Python 3.9", 4,
        "Mencakup Sub-Bab 3.1 Embedded Computer Vision, Sub-Bab 3.2 Edge Computing Raspberry Pi 5, dan Sub-Bab 3.7 Python 3.9"
    )
    deck.add_footer(s4, 4)

    # Kartu 1 (Kiri): Sub-Bab 3.1 Sistem Visi Komputer Tertanam + Gambar 3.1
    deck.add_header_card(
        s4, Inches(0.45), Inches(1.50), Inches(4.25), Inches(5.48),
        "3.1 Sistem Visi Komputer Tertanam", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s4, os.path.join(GAMBAR_DIR, "Gambar3_1_antarmuka_dobot.jpg"),
        Inches(0.60), Inches(2.02), Inches(3.95), Inches(2.35),
        caption="Gambar 3.1 Antarmuka Visi Tertanam Dobot"
    )
    tb = s4.shapes.add_textbox(Inches(0.58), Inches(4.42), Inches(3.98), Inches(2.45))
    tf = tb.text_frame
    tf.word_wrap = True
    deck.add_bullet(tf, "Inferensi Langsung di Lokasi:", "Memadukan sistem tertanam dengan algoritma visi komputer untuk memproses citra secara mandiri tanpa peladen awan (Szeliski, 2022).", pt=10.5)
    deck.add_bullet(tf, "Eliminasi Delay Transmisi:", "Menghilangkan ketergantungan jaringan eksternal dan memangkas transmission delay pada kendali robot real-time (Li et al., 2018).", pt=10.5)
    deck.add_bullet(tf, "Efisiensi Beban & Daya:", "Dimensi mikrokomputer mereduksi payload mekanis dan konsumsi daya dibanding PC konvensional (Shi et al., 2016).", pt=10.5)

    # Kartu 2 (Tengah): Sub-Bab 3.2 Komputasi Tepi (Edge Computing) Raspberry Pi 5
    deck.add_header_card(
        s4, Inches(4.82), Inches(1.50), Inches(4.05), Inches(5.48),
        "3.2 Edge Computing Raspberry Pi 5", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    tb2 = s4.shapes.add_textbox(Inches(4.96), Inches(2.02), Inches(3.78), Inches(4.85))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    deck.add_bullet(tf2, "Paradigma Dekat Sensor:", "Mendistribusikan beban komputasi sedekat mungkin dengan sensor kamera guna menghindari disipasi bandwidth dan latensi fluktuatif (Satyanarayanan, 2017).", pt=10.8, space_after=6)
    deck.add_bullet(tf2, "Hard Real-Time Constraints:", "Menarik analitik AI langsung ke lapisan perangkat fisik (device layer) agar waktu respons robot berada dalam batas waktu nyata.", pt=10.8, space_after=6)
    deck.add_bullet(tf2, "SoC Broadcom BCM2712:", "Ditenagai prosesor ARM Cortex-A76 quad-core dengan lonjakan kinerja single-thread untuk inferensi DNN & pelacakan 3D tanpa dedicated GPU (Raspberry Pi Ltd, 2023).", pt=10.8, space_after=6)
    deck.add_bullet(tf2, "Antarmuka Berkecepatan Tinggi:", "Dilengkapi jalur PCIe 2.0 dan bandwidth memori tinggi untuk aplikasi Edge AI robotika industri & edukasi (Wang et al., 2020).", pt=10.8, space_after=4)

    # Kartu 3 (Kanan): Sub-Bab 3.7 Python 3.9 & NumPy
    deck.add_header_card(
        s4, Inches(8.99), Inches(1.50), Inches(3.89), Inches(5.48),
        "3.7 Python 3.9 & Pustaka NumPy", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    tb3 = s4.shapes.add_textbox(Inches(9.13), Inches(2.02), Inches(3.62), Inches(4.85))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    deck.add_bullet(tf3, "Bahasa Utama Sistem (Python 3.9):", "Sintaks ringkas dan dukungan ekosistem luas untuk pembacaan kamera (OpenCV), ekstraksi MediaPipe, klasifikasi DNN (TensorFlow/Keras), GUI Tkinter, dan komunikasi serial (Python Software Foundation, 2020).", pt=10.8, space_after=6)
    deck.add_bullet(tf3, "Komputasi Matriks NumPy:", "Mengelola struktur array multidimensi secara efisien untuk transformasi koordinat, normalisasi vektor 63 fitur terhadap wrist, serta penyelesaian trigonometri matriks kinematika (Harris et al., 2020).", pt=10.8, space_after=6)
    deck.add_bullet(tf3, "Komunikasi Perangkat Keras:", "Integrasi PySerial dan pydobotplus menjamin pengiriman paket sudut/koordinat bebas packet loss ke mikrokontroler robot.", pt=10.8, space_after=4)

    # =========================================================================
    # SLIDE 5: LANDASAN TEORI (2/3) - SUB-BAB 3.3, 3.5, DAN 3.4 LENGKAP
    # =========================================================================
    s5 = deck.add_slide()
    deck.add_gilang_header(
        s5, "Landasan Teori (2/3): Ekstraksi Geometri, MediaPipe, & SIBI DNN", 5,
        "Mencakup Sub-Bab 3.3 Ekstraksi Fitur Geometris, Sub-Bab 3.5 MediaPipe Hand Tracking, dan Sub-Bab 3.4 SIBI Berbasis DNN"
    )
    deck.add_footer(s5, 5)

    # Kolom Kiri: Sub-Bab 3.3 & 3.5 (Landmark Extraction & MediaPipe Hand Tracking + Gambar 3.2)
    deck.add_header_card(
        s5, Inches(0.45), Inches(1.50), Inches(6.10), Inches(5.48),
        "3.3 Ekstraksi Geometri & 3.5 MediaPipe Hand Tracking", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s5, os.path.join(GAMBAR_DIR, "Gambar3_2_mediapipe_landmarks.png"),
        Inches(0.62), Inches(2.02), Inches(5.76), Inches(2.05),
        caption="Gambar 3.2 Topologi 21 Titik Persendian Tangan (Hand Landmarks) MediaPipe"
    )
    tb_l5 = s5.shapes.add_textbox(Inches(0.60), Inches(4.12), Inches(5.80), Inches(1.92))
    tf_l5 = tb_l5.text_frame
    tf_l5.word_wrap = True
    deck.add_bullet(tf_l5, "Efisiensi Landmark vs Piksel Mentah (Sub-Bab 3.3):", "Mereduksi matriks citra RGB menjadi vektor numerik 1D (dense feature vector) persendian tangan agar ringan bagi SBC (Rautaray & Agrawal, 2015; Zhang et al., 2020).", pt=10.2, space_after=3)
    deck.add_bullet(tf_l5, "Arsitektur 2 Tahap MediaPipe (Sub-Bab 3.5):", "(1) Palm Detector melokalisasi bounding box telapak tangan; (2) Hand Landmark memprediksi 21 titik 3D (x,y,z) dari 0: WRIST (origin) s.d. 20: PINKY_TIP = 63 fitur skalar (Lugaresi et al., 2019; Zhang et al., 2020).", pt=10.2, space_after=3)

    deck.add_picture_fit(
        s5, os.path.join(EQ_DIR, "eq_norm_landmark.png"),
        Inches(0.62), Inches(6.02), Inches(5.76), Inches(0.82), border=True
    )

    # Kolom Kanan: Sub-Bab 3.4 Pengenalan SIBI Berbasis DNN
    deck.add_header_card(
        s5, Inches(6.78), Inches(1.50), Inches(6.10), Inches(5.48),
        "3.4 Pengenalan SIBI Berbasis Deep Neural Networks (DNN)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    tb_r5 = s5.shapes.add_textbox(Inches(6.95), Inches(2.02), Inches(5.76), Inches(3.85))
    tf_r5 = tb_r5.text_frame
    tf_r5.word_wrap = True
    deck.add_bullet(tf_r5, "Karakteristik Daktilologi SIBI:", "Sistem Isyarat Bahasa Indonesia (SIBI) memanfaatkan artikulasi jari-jemari dan orientasi telapak tangan spesifik untuk merepresentasikan 26 abjad alfabet A–Z (Kosasih, 2012).", pt=10.8, space_after=6)
    deck.add_bullet(tf_r5, "Pustaka Instruksi Kendali Diskret:", "Variabilitas formasi jari dijadikan pustaka perintah mandiri (command library) dengan pemetaan satu-ke-satu (one-to-one mapping) terhadap aksi titik kerja dan gripper robot meArm.", pt=10.8, space_after=6)
    deck.add_bullet(tf_r5, "Keunggulan DNN Vektor 63 Fitur vs CNN:", "Tanpa operasi konvolusi citra CNN yang berat, vektor 63 skalar (x,y,z) diumpankan maju (feed-forward) ke jaringan DNN fully-connected berlapis tersembunyi non-linear (Goodfellow et al., 2016).", pt=10.8, space_after=6)
    deck.add_bullet(tf_r5, "Klasifikasi Probabilitas Softmax:", "Lapisan akhir DNN memprediksi probabilitas tertinggi dari 26 kelas abjad dengan ambang keyakinan (confidence score > 0,80) sebelum instruksi dikirim ke aktuator.", pt=10.8, space_after=4)

    deck.add_picture_fit(
        s5, os.path.join(EQ_DIR, "eq_dnn_softmax.png"),
        Inches(6.95), Inches(5.92), Inches(5.76), Inches(0.92), border=True
    )

    # =========================================================================
    # SLIDE 6: LANDASAN TEORI (3/3) - SUB-BAB 3.6.1, 3.6.2, DAN 3.6.3 LENGKAP
    # =========================================================================
    s6 = deck.add_slide()
    deck.add_gilang_header(
        s6, "Landasan Teori (3/3): Kinematika 4-DOF & Perangkat Keras Manipulator", 6,
        "Mencakup Sub-Bab 3.6.1 Forward Kinematics (Pers. 3.1–3.3), 3.6.2 Inverse Kinematics (Pers. 3.4–3.8), & 3.6.3 Dobot vs meArm"
    )
    deck.add_footer(s6, 6)

    # Kolom Kiri: Sub-Bab 3.6.1 Forward & 3.6.2 Inverse Kinematics (Seluruh Persamaan 3.1 s.d. 3.8)
    deck.add_header_card(
        s6, Inches(0.45), Inches(1.50), Inches(6.35), Inches(5.48),
        "3.6.1 Forward & 3.6.2 Inverse Kinematics 4-DOF (Craig, 2018)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    tb_k6 = s6.shapes.add_textbox(Inches(0.60), Inches(1.98), Inches(6.05), Inches(0.85))
    tf_k6 = tb_k6.text_frame
    tf_k6.word_wrap = True
    deck.add_bullet(tf_k6, "Kinematika Maju (Pers. 3.1–3.3):", "Menghitung posisi Cartesian (X,Y,Z) & pitch (phi) dari sudut sendi (theta_1..theta_4) dengan panjang tautan L1, L2, L3 & tinggi basis d1 (Lynch & Park, 2017).", pt=9.8, space_after=2)
    deck.add_bullet(tf_k6, "Kinematika Balikan (Pers. 3.4–3.8):", "Menghitung sudut sendi (theta_1..theta_4) dari target (X,Y,Z) via wrist center (rw, zw) dan Hukum Kosinus (Craig, 2018).", pt=9.8, space_after=2)

    deck.add_picture_fit(s6, os.path.join(EQ_DIR, "eq_3_1_fk.png"), Inches(0.60), Inches(2.90), Inches(6.05), Inches(1.25), border=True)
    deck.add_picture_fit(s6, os.path.join(EQ_DIR, "eq_3_2_ik_1.png"), Inches(0.60), Inches(4.25), Inches(6.05), Inches(1.35), border=True)
    deck.add_picture_fit(s6, os.path.join(EQ_DIR, "eq_3_3_ik_2.png"), Inches(0.60), Inches(5.70), Inches(6.05), Inches(1.15), border=True)

    # Kolom Kanan: Sub-Bab 3.6.3 Implementasi Dobot Magician (Gambar 3.3) & meArm (Gambar 3.4a & 3.4b)
    deck.add_header_card(
        s6, Inches(6.98), Inches(1.50), Inches(5.90), Inches(5.48),
        "3.6.3 Implementasi Perangkat Keras 4-DOF: Dobot & meArm", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    # Gambar 3.3 Dobot Magician (Kiri Atas dalam kartu kanan)
    deck.add_picture_fit(
        s6, os.path.join(GAMBAR_DIR, "Gambar3_3_dobot_magician.jpg"),
        Inches(7.12), Inches(2.02), Inches(2.65), Inches(2.25),
        caption="Gambar 3.3 Dobot Magician", border=True
    )
    # Gambar 3.4a & 3.4b meArm (Kanan Atas dalam kartu kanan)
    deck.add_picture_fit(
        s6, os.path.join(GAMBAR_DIR, "Gambar3_4a_mearm_depan.jpg"),
        Inches(9.88), Inches(2.02), Inches(1.42), Inches(2.25),
        caption="Gambar 3.4a Depan", border=True
    )
    deck.add_picture_fit(
        s6, os.path.join(GAMBAR_DIR, "Gambar3_4b_mearm_samping.jpg"),
        Inches(11.36), Inches(2.02), Inches(1.40), Inches(2.25),
        caption="Gambar 3.4b Samping", border=True
    )

    tb_r6 = s6.shapes.add_textbox(Inches(7.12), Inches(4.38), Inches(5.62), Inches(2.50))
    tf_r6 = tb_r6.text_frame
    tf_r6.word_wrap = True
    deck.add_bullet(tf_r6, "1. Dobot Magician (Mode Teleoperasi Kontinu):", "Manipulator edukasi-industri berpenggerak motor stepper presisi tinggi dengan efektor penyedot vakum (suction cup). Menyelesaikan Pers. (3.4)–(3.8) secara real-time untuk mereplikasi koordinat tangan operator (Dobot, 2022; Dobot, 2026).", pt=10.3, space_after=6)
    deck.add_bullet(tf_r6, "2. Purwarupa meArm 4-DOF (Mode Pengenalan SIBI):", "Manipulator berskala desktop berbahan akrilik yang digerakkan 4 motor servo standar untuk kendali diskret dari posisi home menuju koordinat kerja setelah abjad SIBI tervalidasi (MeArm Robotics, 2026).", pt=10.3, space_after=4)

    # =========================================================================
    # SLIDE 7: METODE PENELITIAN (1/3) - TEMPAT/WAKTU + ALAT/BAHAN + HARDWARE (ALA SLIDE 7 GILANG)
    # =========================================================================
    s7 = deck.add_slide()
    deck.add_gilang_header(s7, "Metode Penelitian (1/3): Lokasi, Alat & Bahan, serta Perancangan Hardware", 7)
    deck.add_footer(s7, 7)

    # Baris Atas: TEMPAT DAN WAKTU PENELITIAN (Bab 4.1 & Bab 2)
    deck.add_header_card(
        s7, Inches(0.45), Inches(0.95), Inches(12.43), Inches(0.95),
        "TEMPAT DAN WAKTU PELAKSANAAN PENELITIAN (BAB 4.1 & PROFIL MITRA BAB II)",
        header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT, card_bg=C_WHITE
    )
    tb_tw = s7.shapes.add_textbox(Inches(0.60), Inches(1.41), Inches(12.15), Inches(0.46))
    p_tw = tb_tw.text_frame.paragraphs[0]
    p_tw.text = "Waktu: Januari – Februari 2026   |   Lokasi: Laboratorium Program Studi Teknologi Mekatronika, Politeknik Enjinering Indorama (PEI), Kembangkuning, Jatiluhur, Kabupaten Purwakarta, Jawa Barat."
    p_tw.font.name = FONT_MAIN
    p_tw.font.size = Pt(10.8)
    p_tw.font.bold = True
    p_tw.font.color.rgb = C_TEXT_DARK
    p_tw.alignment = PP_ALIGN.CENTER

    # Kiri Bawah: TABEL 4.1 ALAT DAN BAHAN LENGKAP
    deck.add_header_card(
        s7, Inches(0.45), Inches(2.00), Inches(6.25), Inches(5.00),
        "ALAT DAN BAHAN PENELITIAN (TABEL 4.1 NASKAH)", header_bg=C_NAVY_DARK, header_fg=C_WHITE
    )
    ab_headers = ["No.", "Alat dan Bahan (Perangkat Keras & Lunak)", "Jumlah"]
    ab_rows = [
        ["1–2", "Laptop & Single Board Computer Raspberry Pi 5", "Masing-masing 1"],
        ["3–4", "Lengan Robot Dobot Magician & Lengan Robot meArm (4-DOF)", "Masing-masing 1"],
        ["5", "Kamera Web (Webcam) Logitech C270/HD (640x480 piksel, 30 FPS)", "1 buah"],
        ["6–7", "Monitor Raspberry Pi & Adaptor Daya (Power Supply) RPi 5", "Masing-masing 1"],
        ["8", "Power Supply 5V DC Eksternal (catu daya terpisah servo meArm)", "1 buah"],
        ["9–11", "Breadboard, Kabel Jumper (M-M / M-F), & Kabel USB Serial", "1 set lengkap"],
        ["12", "Lingkungan Pemrograman Utama: Software Python 3.9", "Lisensi Terbuka"],
        ["13", "Pustaka: OpenCV v4.9.0.80, MediaPipe v0.9.0.1, TensorFlow/Keras, NumPy v1.23.5, Protobuf v3.20.3, Pydobotplus, PySerial, Tkinter, PIL", "Paket Lengkap"]
    ]
    deck.add_styled_table(
        s7, Inches(0.58), Inches(2.50), Inches(5.98), Inches(4.35),
        ab_headers, ab_rows, col_widths=[Inches(0.65), Inches(4.18), Inches(1.15)], font_size=8.8
    )

    # Kanan Bawah: PERANCANGAN PERANGKAT KERAS & ARSITEKTUR SISTEM (GAMBAR 5.1)
    deck.add_header_card(
        s7, Inches(6.88), Inches(2.00), Inches(6.00), Inches(5.00),
        "PERANCANGAN PERANGKAT KERAS & ARSITEKTUR (BAB 4.3.2 & 5.1)", header_bg=C_NAVY_DARK, header_fg=C_WHITE
    )
    deck.add_picture_fit(
        s7, os.path.join(GAMBAR_DIR, "Gambar5_1_arsitektur_sistem_asli.png"),
        Inches(7.02), Inches(2.50), Inches(5.72), Inches(2.85),
        caption="Gambar 5.1 Hasil Rancangan Arsitektur Sistem Tertanam Berbasis Raspberry Pi 5", border=True
    )
    tb_hw = s7.shapes.add_textbox(Inches(7.02), Inches(5.42), Inches(5.72), Inches(1.48))
    tf_hw = tb_hw.text_frame
    tf_hw.word_wrap = True
    deck.add_bullet(tf_hw, "Isolasi Catu Daya Ganda:", "Adaptor khusus menyuplai Raspberry Pi 5 (mencegah under-voltage), sedangkan PSU 5V DC terpisah menyuplai servo meArm guna mengeliminasi noise induksi motor.", pt=9.8, space_after=3)
    deck.add_bullet(tf_hw, "Transmisi Serial Stabil:", "Kabel USB Serial menghubungkan port USB RPi 5 ke kontroler internal Dobot Magician & mikrokontroler servo meArm.", pt=9.8, space_after=2)

    # =========================================================================
    # SLIDE 8: METODE PENELITIAN (2/3) - DIAGRAM ALIR PENELITIAN & PERANGKAT LUNAK (ALA SLIDE 8 GILANG)
    # =========================================================================
    s8 = deck.add_slide()
    deck.add_gilang_header(
        s8, "Metode Penelitian (2/3): Diagram Alir Penelitian & Piranti Lunak", 8,
        "Menampilkan Diagram Alir Tahapan Penelitian (Gambar 4.1) & Alur Logika Piranti Lunak Mode SIBI vs Teleoperasi (Gambar 4.2)"
    )
    deck.add_footer(s8, 8)

    # Kiri: Gambar 4.1 Diagram Alir Penelitian
    deck.add_header_card(
        s8, Inches(0.45), Inches(1.50), Inches(4.55), Inches(5.48),
        "DIAGRAM ALIR PENELITIAN (BAB 4.3)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s8, os.path.join(GAMBAR_DIR, "Gambar4_1_diagram_alir_penelitian_asli.png"),
        Inches(0.60), Inches(2.02), Inches(4.25), Inches(4.82),
        caption="Gambar 4.1 Diagram Alir Tahapan Penelitian"
    )

    # Kanan: Gambar 4.2 Diagram Alir Perangkat Lunak (Mode SIBI & Teleoperasi)
    deck.add_header_card(
        s8, Inches(5.15), Inches(1.50), Inches(7.73), Inches(5.48),
        "PERANCANGAN PIRANTI LUNAK: MODE SIBI & TELEOPERASI (BAB 4.3.3)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s8, os.path.join(GAMBAR_DIR, "Gambar4_2_diagram_alir_software_asli.png"),
        Inches(5.28), Inches(2.02), Inches(7.46), Inches(4.82),
        caption="Gambar 4.2 Diagram Alir Piranti Lunak: (a) Mode SIBI meArm & (b) Mode Teleoperasi Dobot"
    )

    # =========================================================================
    # SLIDE 9: METODE PENELITIAN (3/3) - PEMETAAN PERINTAH SIBI & PARAMETER TELEOPERASI
    # =========================================================================
    s9 = deck.add_slide()
    deck.add_gilang_header(
        s9, "Metode Penelitian (3/3): Skema Pemetaan SIBI & Parameter Teleoperasi", 9,
        "Konfigurasi Pemetaan Karakter SIBI pada meArm (Tabel 5.1) serta Kalibrasi Spasial & Penapisan Jitter pada Dobot Magician"
    )
    deck.add_footer(s9, 9)

    # Kiri: Tabel 5.1 Pemetaan Isyarat Abjad SIBI terhadap Respons Kendali meArm
    deck.add_header_card(
        s9, Inches(0.45), Inches(1.50), Inches(6.15), Inches(5.48),
        "PEMETAAN ISYARAT SIBI KE MEARM (TABEL 5.1)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    t51_headers = ["No.", "Karakter", "Klasifikasi Formasi Isyarat", "Respons Kinematika meArm"]
    t51_rows = [
        ["1", "'A'", "Kepalan tangan, ibu jari tegak ke atas", "Maju ke target posisi kerja XYZ(80, 0, 40) mm"],
        ["2", "'B'", "Empat jari tegak rapat, ibu jari ditekuk", "Rotasi basis ke posisi kerja XYZ(60, 60, 30) mm"],
        ["3", "'C'", "Jari-jemari melengkung membentuk kurva C", "Menutup capit gripper (sudut servo 90 derajat)"],
        ["4", "'D'", "Jari telunjuk tegak vertikal ke atas", "Membuka capit gripper (sudut servo 180 derajat)"],
        ["5", "'E'", "Empat jari menekuk rapat ke telapak", "Kembali ke posisi parkir awal (Home Position)"]
    ]
    deck.add_styled_table(
        s9, Inches(0.60), Inches(2.05), Inches(5.85), Inches(3.35),
        t51_headers, t51_rows, col_widths=[Inches(0.55), Inches(0.85), Inches(2.15), Inches(2.30)], font_size=9.5
    )
    tb_s9l = s9.shapes.add_textbox(Inches(0.60), Inches(5.50), Inches(5.85), Inches(1.35))
    tf_s9l = tb_s9l.text_frame
    tf_s9l.word_wrap = True
    deck.add_bullet(tf_s9l, "Validasi Confidence Score > 0,80:", "Instruksi hanya dikirim melalui komunikasi serial apabila probabilitas keluaran Softmax DNN melampaui ambang batas 0,80.", pt=10.2, space_after=3)
    deck.add_bullet(tf_s9l, "Smooth Stepping Firmware:", "Pergerakan motor servo diatur dengan jeda bertahap agar transisi koordinat bebas hentakan mekanis.", pt=10.2, space_after=2)

    # Kanan: Parameter Teleoperasi Spasial & Filter Anti-Jitter Dobot Magician
    deck.add_header_card(
        s9, Inches(6.78), Inches(1.50), Inches(6.10), Inches(5.48),
        "PARAMETER TELEOPERASI & FILTER ANTI-JITTER DOBOT", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    tb_s9r = s9.shapes.add_textbox(Inches(6.95), Inches(2.02), Inches(5.76), Inches(3.75))
    tf_s9r = tb_s9r.text_frame
    tf_s9r.word_wrap = True
    deck.add_bullet(tf_s9r, "Titik Acuan Pelacakan Spasial:", "Memetakan pergeseran koordinat titik pergelangan (WRIST, indeks 0) dan ujung telunjuk (INDEX_FINGER_TIP, indeks 8) ke ruang kerja fisik Dobot Magician.", pt=10.5, space_after=6)
    deck.add_bullet(tf_s9r, "Pemetaan 3 Sumbu & Efektor Vakum:", "Gerak horizontal citra -> Sumbu Y (kiri/kanan); gerak vertikal citra -> Sumbu Z (naik/turun); skala kedalaman tangan -> Sumbu X (maju); jarak jepit ibu jari–telunjuk < 30 piksel -> Suction Cup ON.", pt=10.5, space_after=6)
    deck.add_bullet(tf_s9r, "Filter Exponential Smoothing (alpha = 0,2):", "Meredam fluktuasi koordinat frekuensi tinggi dari sensor kamera sebelum dihitung melalui persamaan Inverse Kinematics.", pt=10.5, space_after=6)
    deck.add_bullet(tf_s9r, "Ambang Pergeseran (Deadband 5,0 mm):", "Perintah Point-to-Point (PTP) via pydobotplus & PySerial hanya dieksekusi jika selisih jarak target melampaui 5,0 mm, mengeliminasi getaran mikro (jitter).", pt=10.5, space_after=4)

    deck.add_picture_fit(
        s9, os.path.join(EQ_DIR, "eq_ema_filter.png"),
        Inches(6.95), Inches(5.88), Inches(5.76), Inches(0.92), border=True
    )

    # =========================================================================
    # SLIDE 10: HASIL & PEMBAHASAN (1/5) - PELATIHAN & VALIDASI MODEL DNN SIBI
    # =========================================================================
    s10 = deck.add_slide()
    deck.add_gilang_header(
        s10, "Hasil dan Pembahasan (1/5): Pelatihan & Validasi Model DNN SIBI", 10,
        "Model DNN 63 fitur konvergen stabil pada 100 epoch (Training Acc 96,0%–98,5%, Validation Acc 98,0%–100,0%, Loss < 0,10) tanpa overfitting."
    )
    deck.add_footer(s10, 10)

    # Kiri: Kurva Akurasi (Gambar 5.2a) & Loss (Gambar 5.2b)
    deck.add_header_card(
        s10, Inches(0.45), Inches(1.50), Inches(6.35), Inches(5.48),
        "KURVA EVALUASI PELATIHAN MODEL DNN (SESI 25 JANUARI 2026)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s10, os.path.join(GAMBAR_DIR, "Gambar5_2a_akurasi_sibi.png"),
        Inches(0.58), Inches(2.02), Inches(3.00), Inches(2.55),
        caption="Gambar 5.2(a) Accuracy vs Epoch", border=True
    )
    deck.add_picture_fit(
        s10, os.path.join(GAMBAR_DIR, "Gambar5_2b_loss_sibi.png"),
        Inches(3.68), Inches(2.02), Inches(3.00), Inches(2.55),
        caption="Gambar 5.2(b) Loss vs Epoch", border=True
    )
    tb_s10l = s10.shapes.add_textbox(Inches(0.58), Inches(4.68), Inches(6.08), Inches(2.20))
    tf_s10l = tb_s10l.text_frame
    tf_s10l.word_wrap = True
    deck.add_bullet(tf_s10l, "Lonjakan Konvergensi Cepat:", "Training Accuracy melonjak dari 21,3% ke >90,0% pada 20 epoch pertama, lalu stabil di 96,0%–98,5% (Validation Accuracy 98,0%–100,0%).", pt=10.2, space_after=4)
    deck.add_bullet(tf_s10l, "Peluruhan Eksponensial Loss:", "Training & Validation Loss meluruh tajam dari ~3,08 hingga menyusut di bawah 0,10 dengan kurva saling berimpit (bebas overfitting).", pt=10.2, space_after=3)

    # Kanan: Confusion Matrix Validasi Awal (Gambar 5.3) + Rumus Akurasi (Pers. 5.1)
    deck.add_header_card(
        s10, Inches(6.95), Inches(1.50), Inches(5.93), Inches(5.48),
        "MATRIKS KEBINGUNGAN VALIDASI AWAL (106 SAMPEL UJI)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s10, os.path.join(GAMBAR_DIR, "Gambar5_3_cm_validasi.png"),
        Inches(7.12), Inches(2.00), Inches(5.58), Inches(3.65),
        caption="Gambar 5.3 Confusion Matrix Validasi Awal (106 Sampel, Off-Diagonal = 0)", border=True
    )
    deck.add_picture_fit(
        s10, os.path.join(EQ_DIR, "eq_5_1_akurasi.png"),
        Inches(7.12), Inches(5.78), Inches(5.58), Inches(1.05), border=True
    )

    # =========================================================================
    # SLIDE 11: HASIL & PEMBAHASAN (2/5) - KLASIFIKASI SIBI REAL-TIME (96,73%)
    # =========================================================================
    s11 = deck.add_slide()
    deck.add_gilang_header(
        s11, "Hasil dan Pembahasan (2/5): Pengujian Klasifikasi SIBI Real-Time", 11,
        "Pengujian real-time pada Raspberry Pi 5 terhadap 520 data uji (26 abjad × 20 uji) mencapai akurasi 96,73% (503/520 benar; 22 abjad sempurna 100%)."
    )
    deck.add_footer(s11, 11)

    # Kiri: Gambar 5.4 Confusion Matrix Real-Time (520 Data Uji)
    deck.add_header_card(
        s11, Inches(0.45), Inches(1.50), Inches(6.15), Inches(5.48),
        "CONFUSION MATRIX PENGUJIAN REAL-TIME (SESI 18 FEBRUARI 2026)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s11, os.path.join(GAMBAR_DIR, "Gambar5_4_cm_realtime.png"),
        Inches(0.60), Inches(2.00), Inches(5.85), Inches(4.85),
        caption="Gambar 5.4 Confusion Matrix Real-Time SIBI (20 Percobaan per Abjad = 520 Sampel)", border=True
    )

    # Kanan: Tabel 5.2 Rekapitulasi Kinerja SIBI + Analisis Deviasi
    deck.add_header_card(
        s11, Inches(6.78), Inches(1.50), Inches(6.10), Inches(5.48),
        "REKAPITULASI KINERJA PENGUJIAN SIBI (TABEL 5.2)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    t52_headers = ["No.", "Kelompok Isyarat Abjad", "Data Uji", "Benar", "Akurasi (%)"]
    t52_rows = [
        ["1", "Isyarat Perintah Utama (A–E)", "100", "100", "100,00%"],
        ["2", "Isyarat Sekunder (F–J)", "100", "92", "92,00%"],
        ["3", "Isyarat Lanjutan 1 (K–R)", "160", "154", "96,25%"],
        ["4", "Isyarat Lanjutan 2 (S–Z)", "160", "157", "98,13%"],
        ["Total", "Kinerja Keseluruhan (26 Abjad)", "520", "503", "96,73%"]
    ]
    deck.add_styled_table(
        s11, Inches(6.92), Inches(2.02), Inches(5.82), Inches(2.55),
        t52_headers, t52_rows,
        col_widths=[Inches(0.65), Inches(2.45), Inches(0.85), Inches(0.85), Inches(1.02)],
        font_size=9.5, highlight_last=True
    )

    tb_s11r = s11.shapes.add_textbox(Inches(6.92), Inches(4.68), Inches(5.82), Inches(2.20))
    tf_s11r = tb_s11r.text_frame
    tf_s11r.word_wrap = True
    deck.add_bullet(tf_s11r, "Keunggulan Perintah Utama (A–E = 100,0%):", "Kelima abjad instruksi kendali robot meArm (A, B, C, D, E) dikenali 100% akurat tanpa satu pun kesalahan klasifikasi.", pt=10.2, space_after=4)
    deck.add_bullet(tf_s11r, "22 dari 26 Kelas Abjad Mencapai 100%:", "Normalisasi koordinat terhadap titik WRIST terbukti invarian terhadap pergeseran posisi tangan di depan kamera.", pt=10.2, space_after=4)
    deck.add_bullet(tf_s11r, "Analisis Galat Minor (J, M, N, Y):", "Deviasi terbatas pada huruf J (gestur dinamis), M & N (kemiripan lipatan ibu jari tertutup 3 jari), serta Y (rotasi pergelangan).", pt=10.2, space_after=2)

    # =========================================================================
    # SLIDE 12: HASIL & PEMBAHASAN (3/5) - ANALISIS PERGERAKAN KINEMATIS MEARM
    # =========================================================================
    s12 = deck.add_slide()
    deck.add_gilang_header(
        s12, "Hasil dan Pembahasan (3/5): Respons Kinematis Manipulator meArm", 12,
        "Seluruh 5 perintah utama SIBI (A, B, C, D, E) berhasil dieksekusi 100% (5/5 Berhasil) menjadi gerakan translasi dan penjepitan objek pada meArm."
    )
    deck.add_footer(s12, 12)

    # Kiri: Gambar 5.5 Pengujian meArm & Gambar 6.10 Manuver IK meArm
    deck.add_header_card(
        s12, Inches(0.45), Inches(1.50), Inches(5.85), Inches(5.48),
        "DOKUMENTASI PENGUJIAN RESPONS KINEMATIK MEARM (GAMBAR 5.5)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s12, os.path.join(GAMBAR_DIR, "Gambar5_5_uji_mearm_sibi.png"),
        Inches(0.60), Inches(2.00), Inches(5.55), Inches(2.65),
        caption="Gambar 5.5 Pengujian Interaksi Langsung meArm Berbasis Deteksi Gestur SIBI", border=True
    )
    deck.add_picture_fit(
        s12, os.path.join(GAMBAR_DIR, "Gambar6_12_pengujian_jangkauan_capit.jpg"),
        Inches(0.60), Inches(4.72), Inches(2.70), Inches(2.12),
        caption="Gambar 6.12 Uji Jangkauan Capit", border=True
    )
    deck.add_picture_fit(
        s12, os.path.join(GAMBAR_DIR, "Gambar6_13_pengujian_respons_gerak_sibi.jpg"),
        Inches(3.45), Inches(4.72), Inches(2.70), Inches(2.12),
        caption="Gambar 6.13 Respons Gerak SIBI", border=True
    )

    # Kanan: Tabel 5.3 Pengujian Respons Kinematik meArm terhadap Perintah SIBI
    deck.add_header_card(
        s12, Inches(6.48), Inches(1.50), Inches(6.40), Inches(5.48),
        "HASIL PENGUJIAN RESPONS KINEMATIK MEARM (TABEL 5.3)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    t53_headers = ["No.", "Isyarat", "Perintah Aksi", "Respons Fisik Aktual meArm", "Status"]
    t53_rows = [
        ["1", "'A'", "Maju ke posisi kerja", "Lengan bergerak maju ke XYZ(80, 0, 40) mm", "Berhasil"],
        ["2", "'B'", "Rotasi ke samping", "Basis berputar ke koordinat XYZ(60, 60, 30) mm", "Berhasil"],
        ["3", "'C'", "Menutup gripper", "Capit menutup rapat menjepit silinder uji", "Berhasil"],
        ["4", "'D'", "Membuka gripper", "Capit membuka penuh melepas silinder uji", "Berhasil"],
        ["5", "'E'", "Kembali ke Home", "Seluruh servo kembali ke posisi parkir awal", "Berhasil"]
    ]
    deck.add_styled_table(
        s12, Inches(6.62), Inches(2.02), Inches(6.12), Inches(2.95),
        t53_headers, t53_rows,
        col_widths=[Inches(0.50), Inches(0.72), Inches(1.45), Inches(2.50), Inches(0.95)],
        font_size=9.3
    )

    tb_s12r = s12.shapes.add_textbox(Inches(6.62), Inches(5.08), Inches(6.12), Inches(1.80))
    tf_s12r = tb_s12r.text_frame
    tf_s12r.word_wrap = True
    deck.add_bullet(tf_s12r, "Kestabilan Gerak Servo (Smooth Stepping):", "Implementasi jeda bertahap pada firmware berhasil mencegah lonjakan torsi mendadak saat meArm bermanuver menjepit objek silinder.", pt=10.2, space_after=4)
    deck.add_bullet(tf_s12r, "Evaluasi Batas Ruang Kerja Mekanis:", "Rentang kerja fisik purwarupa akrilik meArm memiliki batas jangkauan diagonal <= 180 mm, sehingga waypoint dibatasi dalam zona aman.", pt=10.2, space_after=2)

    # =========================================================================
    # SLIDE 13: HASIL & PEMBAHASAN (4/5) - TELEOPERASI, PRESISI SPASIAL & LATENSI DOBOT
    # =========================================================================
    s13 = deck.add_slide()
    deck.add_gilang_header(
        s13, "Hasil dan Pembahasan (4/5): Teleoperasi, Presisi Spasial, & Latensi Dobot", 13,
        "Pemetaan 6 arah spasial valid 100% (6/6), galat spasial Euclidean rata-rata 1,90 mm (terendah 1,28 mm), dan waktu respons 87,25 ms (near real-time)."
    )
    deck.add_footer(s13, 13)

    # Kiri: Gambar 5.6 + Tabel 5.4 Evaluasi Pemetaan 6 Arah Spasial
    deck.add_header_card(
        s13, Inches(0.45), Inches(1.50), Inches(6.15), Inches(5.48),
        "EVALUASI PEMETAAN ARAH TELEOPERASI DOBOT (TABEL 5.4)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    deck.add_picture_fit(
        s13, os.path.join(GAMBAR_DIR, "Gambar5_6_uji_teleoperasi_dobot.png"),
        Inches(0.60), Inches(1.98), Inches(5.85), Inches(2.22),
        caption="Gambar 5.6 Pengujian Teleoperasi Dobot Magician via Hand Tracking MediaPipe", border=True
    )
    t54_headers = ["No.", "Arah Gerak Tangan Operator", "Respons Dobot Magician", "Status"]
    t54_rows = [
        ["1", "Geser Kanan (X > 0,5)", "Translasi sumbu Y+ (kanan)", "Sesuai (Valid)"],
        ["2", "Geser Kiri (X < 0,5)", "Translasi sumbu Y- (kiri)", "Sesuai (Valid)"],
        ["3", "Angkat Tangan (Y < 0,5)", "Translasi sumbu Z+ (naik)", "Sesuai (Valid)"],
        ["4", "Turun Tangan (Y > 0,5)", "Translasi sumbu Z- (turun)", "Sesuai (Valid)"],
        ["5", "Mendekati Kamera (Skala > 0,2)", "Jangkauan sumbu X+ (maju)", "Sesuai (Valid)"],
        ["6", "Jepit Telunjuk–Ibu Jari (< 30 px)", "Penyedot Vakum (Suction ON)", "Sesuai (Valid)"]
    ]
    deck.add_styled_table(
        s13, Inches(0.60), Inches(4.26), Inches(5.85), Inches(2.58),
        t54_headers, t54_rows,
        col_widths=[Inches(0.50), Inches(2.15), Inches(2.05), Inches(1.15)],
        font_size=8.8
    )

    # Kanan: Tabel 5.5 Presisi Spasial & Waktu Respons + Rumus Galat Euclidean (Pers. 5.2)
    deck.add_header_card(
        s13, Inches(6.78), Inches(1.50), Inches(6.10), Inches(5.48),
        "PRESISI SPASIAL & WAKTU RESPONS DOBOT (TABEL 5.5)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    t55_headers = ["No.", "Target (X, Y, Z) mm", "Aktual Enkoder (mm)", "Galat (mm)", "Respons (ms)"]
    t55_rows = [
        ["1", "(200,0; 0,0; 0,0)", "(198,8; 0,4; -0,2)", "1,28", "82"],
        ["2", "(220,0; 50,0; 30,0)", "(218,6; 49,2; 29,5)", "1,68", "88"],
        ["3", "(250,0; -60,0; 50,0)", "(247,8; -58,7; 50,8)", "2,68", "94"],
        ["4", "(190,0; 80,0; -20,0)", "(188,5; 78,9; -19,4)", "1,95", "85"],
        ["Rerata", "Evaluasi 4 Kuadran Kerja", "Umpan Balik Enkoder Optik", "1,90 mm", "87,25 ms"]
    ]
    deck.add_styled_table(
        s13, Inches(6.92), Inches(2.02), Inches(5.82), Inches(2.45),
        t55_headers, t55_rows,
        col_widths=[Inches(0.68), Inches(1.62), Inches(1.68), Inches(0.92), Inches(0.92)],
        font_size=9.2, highlight_last=True
    )

    deck.add_picture_fit(
        s13, os.path.join(EQ_DIR, "eq_5_2_euclidean.png"),
        Inches(6.92), Inches(4.58), Inches(5.82), Inches(0.90), border=True
    )

    tb_s13r = s13.shapes.add_textbox(Inches(6.92), Inches(5.55), Inches(5.82), Inches(1.35))
    tf_s13r = tb_s13r.text_frame
    tf_s13r.word_wrap = True
    deck.add_bullet(tf_s13r, "Ketelitian Spasial Milimeter (1,90 mm):", "Selisih antara target algoritma dan pembacaan enkoder optik internal via pydobotplus sangat kecil (terendah 1,28 mm).", pt=10.0, space_after=3)
    deck.add_bullet(tf_s13r, "Respons di Bawah Ambang Visual (< 100 ms):", "Latensi rata-rata 87,25 ms memastikan replikasi gerak tangan terasa instan disertai penapisan jitter (alpha = 0,2).", pt=10.0, space_after=2)

    # =========================================================================
    # SLIDE 14: HASIL & PEMBAHASAN (5/5) - RANGKUMAN KINERJA SISTEM & VIDEO DARING
    # =========================================================================
    s14 = deck.add_slide()
    deck.add_gilang_header(
        s14, "Hasil dan Pembahasan (5/5): Evaluasi Sistem Keseluruhan & Video Uji", 14,
        "Satu perangkat komputasi tepi Raspberry Pi 5 berhasil menjalankan kedua skenario kendali manipulator 4-DOF secara stabil pada 30 FPS."
    )
    deck.add_footer(s14, 14)

    # Atas: Tabel 5.6 Rangkuman Kinerja Sistem Keseluruhan
    deck.add_header_card(
        s14, Inches(0.45), Inches(1.50), Inches(12.43), Inches(3.38),
        "RANGKUMAN KINERJA SISTEM KESELURUHAN (TABEL 5.6 NASKAH)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    t56_headers = ["No.", "Parameter Kinerja Evaluasi Sistem", "Mode Pengenalan SIBI (meArm 4-DOF)", "Mode Teleoperasi (Dobot Magician 4-DOF)"]
    t56_rows = [
        ["1", "Akurasi Klasifikasi Isyarat Visual", "96,73% (503 / 520 Data Uji Valid; 22 Abjad 100%)", "N/A (Pelacakan Koordinat Spasial Kontinu)"],
        ["2", "Kesesuaian Pemetaan Arah Spasial", "N/A (Kendali Diskret Waypoint)", "6 / 6 Arah Gerak & Gestur Valid (100% Sinkron)"],
        ["3", "Galat Spasial Rata-rata (Euclidean 3D)", "-- (Dibatasi Toleransi Servo Standar)", "1,90 mm (Galat Terendah 1,28 mm)"],
        ["4", "Waktu Respons Rata-rata Sistem (Latensi)", "--", "87,25 ms (Responsif Near Real-Time < 100 ms)"],
        ["5", "Keberhasilan Respons Perintah Kinematik", "5 / 5 Perintah Utama Berhasil (100%)", "4 / 4 Target Kuadran Posisi Berhasil (100%)"],
        ["6", "Stabilitas Pipeline Visi Raspberry Pi 5", "Stabil (30 FPS Lokal Tanpa Cloud)", "Stabil (Bebas Jitter dengan Filter alpha = 0,2)"]
    ]
    deck.add_styled_table(
        s14, Inches(0.60), Inches(2.00), Inches(12.13), Inches(2.75),
        t56_headers, t56_rows,
        col_widths=[Inches(0.65), Inches(3.88), Inches(3.80), Inches(3.80)],
        font_size=9.5
    )

    # Bawah Kiri: Kotak Tautan Video Pengujian Daring (Bab 5.4.1)
    deck.add_header_card(
        s14, Inches(0.45), Inches(5.00), Inches(7.75), Inches(1.98),
        "AKSES REPOSITORI & REKAMAN VIDEO PENGUJIAN DARING (BAB 5.4.1)",
        header_bg=C_NAVY_MID, header_fg=C_GOLD_ACCENT, card_bg=C_GOLD_LIGHT, border=C_GOLD_ACCENT
    )
    tb_vid = s14.shapes.add_textbox(Inches(0.62), Inches(5.48), Inches(7.40), Inches(1.42))
    tf_vid = tb_vid.text_frame
    tf_vid.word_wrap = True
    p = tf_vid.paragraphs[0]
    p.text = "Tautan Google Drive: https://drive.google.com/drive/folders/1tkqb4tbg0jelGM6Wm1YSTbDkor_XJfIM?usp=sharing"
    p.font.name = FONT_MAIN
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    p.space_after = Pt(4)

    deck.add_bullet(tf_vid, "Video 1 (Teleoperasi Dobot Magician):", "Demonstrasi pelacakan tangan 3D real-time dan aktivasi vakum (suction cup) memindahkan objek kubus.", pt=9.8, space_after=2)
    deck.add_bullet(tf_vid, "Video 2 (Pengenalan SIBI meArm):", "Demonstrasi klasifikasi abjad SIBI di depan kamera dan eksekusi gerak servo meArm menjepit silinder.", pt=9.8, space_after=2)

    # Bawah Kanan: 2 Foto Stasiun Kerja
    deck.add_picture_fit(
        s14, os.path.join(GAMBAR_DIR, "Gambar6_15_stasiun_teleoperasi_dobot1.jpg"),
        Inches(8.35), Inches(5.00), Inches(2.20), Inches(1.98),
        caption="Stasiun Uji Dobot", border=True
    )
    deck.add_picture_fit(
        s14, os.path.join(GAMBAR_DIR, "Gambar6_9_integrasi_sistem_mearm.jpg"),
        Inches(10.68), Inches(5.00), Inches(2.20), Inches(1.98),
        caption="Stasiun Uji meArm", border=True
    )

    # =========================================================================
    # SLIDE 15: KESIMPULAN DAN SARAN (BAB VI NASKAH ASLI, GAYA SLIDE 24 GILANG)
    # =========================================================================
    s15 = deck.add_slide()
    deck.add_gilang_header(s15, "Kesimpulan dan Saran", 15)
    deck.add_footer(s15, 15)

    # Kolom Kiri: KESIMPULAN (Menjawab 1:1 Rumusan Masalah 1–3)
    deck.add_header_card(
        s15, Inches(0.45), Inches(0.98), Inches(6.25), Inches(6.00),
        "KESIMPULAN PENELITIAN (BAB 6.1)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    ks_items = [
        ("1.", "Implementasi Visi Tertanam Raspberry Pi 5 Mandiri:",
         "Sistem tertanam berbasis Raspberry Pi 5 berhasil dirancang dan diimplementasikan sebagai pusat komputasi tepi (edge computer) yang mengintegrasikan kamera Logitech, MediaPipe, Python 3.9, serta dua manipulator 4-DOF (meArm & Dobot Magician) secara lokal dan stabil (30 FPS) tanpa komputasi awan."),
        ("2.", "Akurasi Pengenalan SIBI 96,73% pada Manipulator meArm:",
         "Mode pengenalan SIBI pada meArm berhasil mengklasifikasikan 26 abjad dengan akurasi keseluruhan 96,73% (503 prediksi benar dari 520 percobaan). Model DNN berbasis 63 fitur koordinat spasial mengenali 22 dari 26 kelas abjad dengan akurasi sempurna (100,0%) dan mengeksekusi 5/5 perintah mekanis meArm."),
        ("3.", "Presisi 1,90 mm & Respons 87,25 ms pada Teleoperasi Dobot:",
         "Mode teleoperasi Dobot Magician berhasil memetakan gerak tangan dengan kesesuaian 6/6 arah valid (100%), galat spasial rata-rata 1,90 mm (terendah 1,28 mm), dan waktu respons rata-rata 87,25 ms. Filter exponential smoothing (alpha = 0,2) dan ambang gerak 5,0 mm sukses mengeliminasi jitter.")
    ]
    for idx, (num, title_k, body_k) in enumerate(ks_items):
        y_pos = Inches(1.55 + idx * 1.78)
        badge = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.62), y_pos, Inches(0.45), Inches(0.45))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_GOLD_ACCENT
        badge.line.fill.background()
        pb = badge.text_frame.paragraphs[0]
        pb.text = num
        pb.font.name = FONT_MAIN
        pb.font.size = Pt(13)
        pb.font.bold = True
        pb.font.color.rgb = C_NAVY_DARK
        pb.alignment = PP_ALIGN.CENTER

        tb = s15.shapes.add_textbox(Inches(1.15), y_pos - Inches(0.06), Inches(5.42), Inches(1.68))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_k
        p.font.name = FONT_MAIN
        p.font.size = Pt(11.2)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_MID
        p.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = body_k
        p2.font.name = FONT_MAIN
        p2.font.size = Pt(10.2)
        p2.font.color.rgb = C_TEXT_DARK
        p2.line_spacing = 1.15

    # Kolom Kanan: SARAN PENGEMBANGAN (5 Poin Bab 6.2)
    deck.add_header_card(
        s15, Inches(6.88), Inches(0.98), Inches(6.00), Inches(6.00),
        "SARAN PENGEMBANGAN LANJUTAN (BAB 6.2)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    sr_items = [
        ("1. Variasi Dataset Multi-Pengguna:", "Menambah jumlah kelas dinamis dan variasi data SIBI dari berbagai ukuran tangan pengguna agar model lebih tangguh terhadap variasi anatomi."),
        ("2. Eksplorasi Algoritma Klasifikasi Ringan:", "Mengeksplorasi metode klasifikasi pembanding seperti Support Vector Machine (SVM), Random Forest, atau arsitektur jaringan saraf ringan pada Raspberry Pi 5."),
        ("3. Filter Temporal Lanjutan:", "Menambahkan filter temporal adaptif (seperti Kalman Filter / One-Euro Filter) pada sinyal landmark tangan agar pergerakan manipulator semakin halus."),
        ("4. Kalibrasi Ruang Kerja Multi-Kamera:", "Melakukan kalibrasi transformasi ruang kerja 3D yang lebih presisi antara bidang pandang kamera dan ruang kerja fisik Dobot Magician."),
        ("5. Antarmuka Pencatatan Data Otomatis:", "Mengembangkan fitur GUI untuk pemilihan mode terpadu, pemantauan metrik real-time, serta penyimpanan log pengujian otomatis.")
    ]
    tb_sr = s15.shapes.add_textbox(Inches(7.05), Inches(1.55), Inches(5.66), Inches(5.30))
    tf_sr = tb_sr.text_frame
    tf_sr.word_wrap = True
    for h_s, b_s in sr_items:
        deck.add_bullet(tf_sr, h_s, b_s, pt=10.5, space_after=8)

    # =========================================================================
    # SLIDE 16: DAFTAR PUSTAKA LENGKAP & GALERI DOKUMENTASI LAMPIRAN
    # =========================================================================
    s16 = deck.add_slide()
    deck.add_gilang_header(s16, "Daftar Pustaka dan Lampiran Dokumentasi Penelitian", 16)
    deck.add_footer(s16, 16)

    # Kiri: Daftar Pustaka Lengkap (18 Entri references.bib)
    deck.add_header_card(
        s16, Inches(0.45), Inches(0.98), Inches(6.35), Inches(6.00),
        "DAFTAR PUSTAKA LENGKAP (18 REFERENSI NASKAH)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    bib_entries = [
        "1. Craig, J. J. (2018). Introduction to Robotics: Mechanics and Control (4th ed.). Pearson.",
        "2. DOBOT. (2022). Dobot Magician User Guide. Shenzhen Yuejiang Technology Co., Ltd.",
        "3. DOBOT. (2026). Dobot Magician Desktop Robotic Arm Documentation and Specifications.",
        "4. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.",
        "5. Harris, C. R., et al. (2020). Array programming with NumPy. Nature, 585, 357–362.",
        "6. Kosasih, E. (2012). Pendidikan Anak Tunarungu (Sistem Isyarat Bahasa Indonesia). Yrama Widya.",
        "7. Li, E., Zeng, L., Zhou, Z., & Chen, X. (2018). Deep learning for edge computing applications: A state-of-the-art survey. IEEE Access, 6, 58322–58336.",
        "8. Lugaresi, C., et al. (2019). MediaPipe: A framework for building perception pipelines. arXiv:1906.08172.",
        "9. Lynch, K. M., & Park, F. C. (2017). Modern Robotics: Mechanics, Planning, and Control. Cambridge University Press.",
        "10. MeArm Robotics. (2026). meArm Robot Arm Documentation.",
        "11. Python Software Foundation. (2020). Python 3.9 Documentation.",
        "12. Raspberry Pi Ltd. (2023). Raspberry Pi 5 Product Brief.",
        "13. Rautaray, S. S., & Agrawal, A. (2015). Vision based hand gesture recognition for human computer interaction: A survey. Artificial Intelligence Review, 43, 1–54.",
        "14. Satyanarayanan, M. (2017). The emergence of edge computing. Computer, 50(1), 30–39.",
        "15. Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge computing: Vision and challenges. IEEE Internet of Things Journal, 3(5), 637–646.",
        "16. Szeliski, R. (2022). Computer Vision: Algorithms and Applications (2nd ed.). Springer.",
        "17. Wang, X., et al. (2020). Convergence of edge computing and deep learning: A comprehensive survey. IEEE Communications Surveys & Tutorials, 22(2), 869–904.",
        "18. Zhang, F., et al. (2020). MediaPipe Hands: On-device real-time hand tracking. arXiv:2006.10214."
    ]
    tb_bib = s16.shapes.add_textbox(Inches(0.58), Inches(1.48), Inches(6.10), Inches(5.42))
    tf_bib = tb_bib.text_frame
    tf_bib.word_wrap = True
    for b_line in bib_entries:
        p = tf_bib.paragraphs[0] if len(tf_bib.paragraphs[0].text) == 0 else tf_bib.add_paragraph()
        p.text = b_line
        p.font.name = FONT_MAIN
        p.font.size = Pt(8.0)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(1.8)

    # Kanan: Galeri 6 Foto Dokumentasi Laboratorium (Lampiran 4)
    deck.add_header_card(
        s16, Inches(6.95), Inches(0.98), Inches(5.93), Inches(6.00),
        "DOKUMENTASI IMPLEMENTASI & PENGUJIAN (LAMPIRAN)", header_bg=C_NAVY_DARK, header_fg=C_GOLD_ACCENT
    )
    gallery = [
        ("Gambar6_1_mearm_tampak_depan.jpg", "Gambar 6.1 Purwarupa meArm"),
        ("Gambar6_2_mearm_dan_mikrokontroler.jpg", "Gambar 6.2 Integrasi Mikrokontroler"),
        ("Gambar6_5_perakitan_rangka_akrilik.jpg", "Gambar 6.5 Perakitan Rangka"),
        ("Gambar6_10_pengujian_manuver_ik_sesi1.jpg", "Gambar 6.10 Uji Manuver IK meArm"),
        ("Gambar6_14_antarmuka_pelacakan_dobot.jpg", "Gambar 6.14 Antarmuka Pelacakan"),
        ("Gambar6_17_manipulator_dobot_suction1.jpg", "Gambar 6.17 Dobot & Suction Cup")
    ]
    gx_list = [Inches(7.08), Inches(9.98)]
    gy_list = [Inches(1.52), Inches(3.32), Inches(5.12)]
    for idx, (g_fn, g_cap) in enumerate(gallery):
        col = idx % 2
        row = idx // 2
        deck.add_picture_fit(
            s16, os.path.join(GAMBAR_DIR, g_fn),
            gx_list[col], gy_list[row], Inches(2.75), Inches(1.70),
            caption=g_cap, border=True
        )

    # =========================================================================
    # SLIDE 17: PENUTUP - TERIMA KASIH (SELARAS COVER SLIDE 1)
    # =========================================================================
    s17 = deck.add_slide(dark_bg=True)
    if os.path.exists(bg_cover):
        s17.shapes.add_picture(bg_cover, 0, 0, Inches(13.333), Inches(7.5))

    if os.path.exists(pill_logo):
        deck.add_picture_fit(s17, pill_logo, Inches(4.9), Inches(0.45), Inches(3.533), Inches(1.15))

    deck.add_card(
        s17, Inches(1.5), Inches(1.95), Inches(10.333), Inches(3.65),
        bg=RGBColor(15, 30, 68), border=C_GOLD_ACCENT, lw=3.0
    )
    tb_end = s17.shapes.add_textbox(Inches(1.8), Inches(2.15), Inches(9.733), Inches(3.25))
    tf_e = tb_end.text_frame
    tf_e.word_wrap = True

    p = tf_e.paragraphs[0]
    p.text = "TERIMA KASIH"
    p.font.name = FONT_MAIN
    p.font.size = Pt(42)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_ACCENT
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(10)

    p2 = tf_e.add_paragraph()
    p2.text = "Mohon Arahan, Masukan, dan Saran pada Sesi Tanya Jawab Seminar Kerja Praktik"
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(14)

    p3 = tf_e.add_paragraph()
    p3.text = (
        "Fahry Rizky Samsudin (NIM. 1237030018)\n"
        "Pembimbing I: Dr. Moch Nurul Subkhi, M.Si.  |  Pembimbing II: Dr. Emmanuel Agung N, S.T, M.T.\n"
        "Jurusan Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung (2026)"
    )
    p3.font.name = FONT_MAIN
    p3.font.size = Pt(11.5)
    p3.font.color.rgb = C_SLATE_LIGHT
    p3.alignment = PP_ALIGN.CENTER
    p3.line_spacing = 1.3

    deck.prs.save(OUTPUT_PPTX)
    print(f"[SUKSES] PPTX Laporan KP berhasil disimpan: {OUTPUT_PPTX} ({len(deck.prs.slides)} slides)")


if __name__ == "__main__":
    build_kp_pptx()
