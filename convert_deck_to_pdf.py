#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konverter Presisi Tinggi: PPTX Laporan KP -> PDF 16:9 Widescreen (17 Halaman)
Menggunakan python-pptx dan reportlab dengan font Roboto tersemat penuh.
"""

import os
import sys
import io
import html
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import PP_ALIGN

from reportlab.lib.colors import Color, HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Registrasi Font TrueType Roboto agar embedding 100% sempurna tanpa issue kerning
FONT_REGULAR = "Roboto"
FONT_BOLD = "Roboto-Bold"

if os.path.exists("/system/fonts/Roboto-Regular.ttf") and os.path.exists("/system/fonts/Roboto-Bold.ttf"):
    pdfmetrics.registerFont(TTFont("Roboto", "/system/fonts/Roboto-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Roboto-Bold", "/system/fonts/Roboto-Bold.ttf"))
elif os.path.exists("/system/fonts/DroidSans.ttf") and os.path.exists("/system/fonts/DroidSans-Bold.ttf"):
    pdfmetrics.registerFont(TTFont("Roboto", "/system/fonts/DroidSans.ttf"))
    pdfmetrics.registerFont(TTFont("Roboto-Bold", "/system/fonts/DroidSans-Bold.ttf"))
else:
    FONT_REGULAR = "Helvetica"
    FONT_BOLD = "Helvetica-Bold"

BASE_DIR = "/storage/emulated/0/Projek/LAPORAN-KP-Fahry-Rizky-Samsudin-Termux-Android"
PPTX_FILE = os.path.join(BASE_DIR, "Laporan_KP_Fahry_Rizky_Samsudin.pptx")
PDF_FILE = os.path.join(BASE_DIR, "Laporan_KP_Fahry_Rizky_Samsudin_Presentasi.pdf")

def emu_to_pt(emu):
    if emu is None:
        return 0.0
    return float(emu) / 914400.0 * 72.0

def get_rgb_color(color_format):
    try:
        rgb = color_format.rgb
        return Color(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
    except:
        return None

def get_hex_color(color_format):
    try:
        rgb = color_format.rgb
        return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    except:
        return None

def convert_pptx_to_pdf(input_pptx=PPTX_FILE, output_pdf=PDF_FILE):
    print(f"[INFO] Membaca PPTX: {input_pptx}")
    prs = Presentation(input_pptx)
    pw = emu_to_pt(prs.slide_width)
    ph = emu_to_pt(prs.slide_height)

    c = canvas.Canvas(output_pdf, pagesize=(pw, ph))

    align_map = {
        PP_ALIGN.LEFT: TA_LEFT,
        PP_ALIGN.CENTER: TA_CENTER,
        PP_ALIGN.RIGHT: TA_RIGHT,
        PP_ALIGN.JUSTIFY: TA_JUSTIFY,
        None: TA_LEFT
    }

    total_slides = len(prs.slides)
    print(f"[INFO] Total slide ditemukan: {total_slides}")

    for slide_idx, slide in enumerate(prs.slides, start=1):
        # Background default slide
        c.saveState()
        if slide_idx == 1:
            c.setFillColor(HexColor('#0F1E44'))
        else:
            c.setFillColor(HexColor('#F4F7FB'))
        c.rect(0, 0, pw, ph, fill=1, stroke=0)
        c.restoreState()

        for shape in slide.shapes:
            sx = emu_to_pt(shape.left)
            sw = emu_to_pt(shape.width)
            sh = emu_to_pt(shape.height)
            sy = ph - emu_to_pt(shape.top) - sh

            # -------------------------------------------------------------
            # 1. GAMBAR / PICTURE
            # -------------------------------------------------------------
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                try:
                    img_bytes = shape.image.blob
                    ir = ImageReader(io.BytesIO(img_bytes))
                    c.drawImage(ir, sx, sy, width=sw, height=sh, mask='auto')
                except Exception as e:
                    print(f"  [WARN] Slide {slide_idx}: Gagal merender gambar: {e}")

            # -------------------------------------------------------------
            # 2. AUTOSHAPE (KARTU, BANNER, RECTANGLE)
            # -------------------------------------------------------------
            elif shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
                fill_c = None
                try:
                    if shape.fill.type == 1:
                        fill_c = get_rgb_color(shape.fill.fore_color)
                except:
                    pass

                stroke_c = None
                stroke_w = 0.5
                try:
                    if shape.line.fill.type == 1:
                        stroke_c = get_rgb_color(shape.line.color)
                        stroke_w = emu_to_pt(shape.line.width) if shape.line.width else 1.0
                except:
                    pass

                if fill_c or stroke_c:
                    c.saveState()
                    if fill_c:
                        c.setFillColor(fill_c)
                    if stroke_c:
                        c.setStrokeColor(stroke_c)
                        c.setLineWidth(stroke_w)

                    is_round = ('rounded' in shape.name.lower() or 'card' in shape.name.lower())
                    if is_round:
                        c.roundRect(sx, sy, sw, sh, 5, fill=1 if fill_c else 0, stroke=1 if stroke_c else 0)
                    else:
                        c.rect(sx, sy, sw, sh, fill=1 if fill_c else 0, stroke=1 if stroke_c else 0)
                    c.restoreState()

            # -------------------------------------------------------------
            # 3. TABEL / TABLE
            # -------------------------------------------------------------
            elif shape.shape_type == MSO_SHAPE_TYPE.TABLE:
                tbl = shape.table
                cur_y = ph - emu_to_pt(shape.top)
                col_w_pts = [emu_to_pt(col.width) for col in tbl.columns]
                
                for r_idx, row in enumerate(tbl.rows):
                    rh = emu_to_pt(row.height)
                    cur_y -= rh
                    cur_x = sx

                    for c_idx, cell in enumerate(row.cells):
                        cw = col_w_pts[c_idx]
                        
                        c_fill = None
                        try:
                            if cell.fill.type == 1:
                                c_fill = get_rgb_color(cell.fill.fore_color)
                        except:
                            pass

                        c.saveState()
                        if c_fill:
                            c.setFillColor(c_fill)
                        else:
                            c.setFillColor(HexColor('#FFFFFF') if r_idx % 2 == 0 else HexColor('#F1F5F9'))
                        c.setStrokeColor(HexColor('#CBD5E1'))
                        c.setLineWidth(0.6)
                        c.rect(cur_x, cur_y, cw, rh, fill=1, stroke=1)
                        c.restoreState()

                        txt = cell.text.strip()
                        if txt:
                            p_elem = cell.text_frame.paragraphs[0]
                            font_sz = emu_to_pt(p_elem.font.size) if p_elem.font.size else 8.5
                            is_b = p_elem.font.bold or (r_idx == 0)
                            tc_hex = get_hex_color(p_elem.font.color) or ('#FFFFFF' if r_idx == 0 else '#0F172A')
                            
                            align_style = TA_CENTER if (c_idx == 0 or r_idx == 0) else TA_LEFT
                            cell_style = ParagraphStyle(
                                f'Cell_{slide_idx}_{r_idx}_{c_idx}',
                                fontName=FONT_BOLD if is_b else FONT_REGULAR,
                                fontSize=font_sz,
                                leading=font_sz * 1.25,
                                alignment=align_style,
                                textColor=HexColor(tc_hex)
                            )
                            p_obj = Paragraph(html.escape(txt), cell_style)
                            w_u, h_u = p_obj.wrap(cw - 8, rh - 4)
                            draw_y = cur_y + (rh - h_u) / 2.0
                            p_obj.drawOn(c, cur_x + 4, draw_y)

                        cur_x += cw

            # -------------------------------------------------------------
            # 4. TEKS PADA TEXT_BOX ATAU AUTOSHAPE DENGAN TEXT
            # -------------------------------------------------------------
            if shape.has_text_frame and shape.shape_type != MSO_SHAPE_TYPE.TABLE:
                tf = shape.text_frame
                if tf.text.strip():
                    pad_x = emu_to_pt(tf.margin_left) if tf.margin_left else 3.0
                    pad_y = emu_to_pt(tf.margin_top) if tf.margin_top else 3.0
                    
                    avail_w = max(10, sw - (pad_x * 2.0))
                    avail_h = max(10, sh - (pad_y * 2.0))

                    curr_text_y = sy + sh - pad_y

                    for p_idx, p in enumerate(tf.paragraphs):
                        raw_text = p.text
                        if not raw_text.strip():
                            curr_text_y -= 4.0
                            continue

                        runs_html = []
                        p_font_sz = emu_to_pt(p.font.size) if p.font.size else 11.0
                        p_is_b = bool(p.font.bold)
                        p_color_hex = get_hex_color(p.font.color) or '#0F172A'

                        if p.runs:
                            for r in p.runs:
                                r_text = html.escape(r.text)
                                r_sz = emu_to_pt(r.font.size) if r.font.size else p_font_sz
                                r_bold = r.font.bold if r.font.bold is not None else p_is_b
                                r_color = get_hex_color(r.font.color) or p_color_hex
                                
                                formatted_run = r_text
                                if r_bold:
                                    formatted_run = f"<b>{formatted_run}</b>"
                                formatted_run = f'<font size="{r_sz:.1f}" color="{r_color}">{formatted_run}</font>'
                                runs_html.append(formatted_run)
                            p_content = "".join(runs_html)
                        else:
                            p_content = html.escape(raw_text)
                            if p_is_b:
                                p_content = f"<b>{p_content}</b>"
                            p_content = f'<font size="{p_font_sz:.1f}" color="{p_color_hex}">{p_content}</font>'

                        rep_align = align_map.get(p.alignment, TA_LEFT)
                        line_spacing = p.line_spacing if p.line_spacing else 1.22
                        if isinstance(line_spacing, (int, float)):
                            leading_pt = p_font_sz * float(line_spacing)
                        else:
                            leading_pt = emu_to_pt(line_spacing)

                        p_style = ParagraphStyle(
                            f'P_{slide_idx}_{shape.shape_id}_{p_idx}',
                            fontName=FONT_BOLD if p_is_b else FONT_REGULAR,
                            fontSize=p_font_sz,
                            leading=leading_pt,
                            alignment=rep_align,
                            spaceBefore=emu_to_pt(p.space_before) if p.space_before else 0,
                            spaceAfter=emu_to_pt(p.space_after) if p.space_after else 1.5
                        )

                        p_obj = Paragraph(p_content, p_style)
                        w_used, h_used = p_obj.wrap(avail_w, avail_h)
                        curr_text_y -= h_used
                        p_obj.drawOn(c, sx + pad_x, curr_text_y)
                        curr_text_y -= (emu_to_pt(p.space_after) if p.space_after else 1.5)

        c.showPage()
        print(f"  [OK] Halaman {slide_idx} / {total_slides} selesai dirender.")

    c.save()
    print(f"[SUKSES] PDF presentasi 16:9 berhasil disimpan ke: {output_pdf}")

if __name__ == "__main__":
    convert_pptx_to_pdf()
