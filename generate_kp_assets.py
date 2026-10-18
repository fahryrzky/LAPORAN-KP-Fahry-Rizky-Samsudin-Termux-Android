#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Aset Visual Resolusi Tinggi (300 DPI) untuk Presentasi Laporan KP
Fahry Rizky Samsudin (NIM: 1237030018) - Fisika FST UIN Sunan Gunung Djati Bandung
Mencakup:
1. Latar Belakang Cover Kolase Foto Lab KP (cover_bg_kp.png) + Pill Logo UIN-Fisika
2. Gambar 1.1 Alur Latar Belakang Berbasis Citra + Info Footer + Panah Kuning + Gap Research
3. Gambar 4.2 Diagram Alir Perangkat Lunak (Mode SIBI & Teleoperasi) Bebas Tabrakan
4. Persamaan Matematika Bab III (3.1 s.d. 3.8) & Bab V (5.1 s.d. 5.2) 300 DPI
"""

import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

BASE_DIR = "/storage/emulated/0/Projek/LAPORAN-KP-Fahry-Rizky-Samsudin-Termux-Android"
PROPOSAL_DIR = "/storage/emulated/0/Projek/PROPOSAL-TA-Fahry-Rizky-Samsudin-Termux-Android"
GAMBAR_DIR = os.path.join(BASE_DIR, "Gambar")
EQ_DIR = os.path.join(GAMBAR_DIR, "equations")
os.makedirs(EQ_DIR, exist_ok=True)

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'


def prepare_cover_and_logos():
    """Menyiapkan logo pill UIN-Fisika dan latar kolase foto lab KP gelap ala slide_ref_1 Gilang."""
    src_pill = os.path.join(PROPOSAL_DIR, "Gambar", "Logo", "logo_uin_fisika_pill.png")
    dst_pill = os.path.join(GAMBAR_DIR, "logo_uin_fisika_pill.png")
    if os.path.exists(src_pill):
        shutil.copy2(src_pill, dst_pill)
        print(f"[OK] Logo pill disalin ke: {dst_pill}")

    # Buat kolase 2x2 dari 4 foto dokumentasi lab KP asli
    target_w, target_h = 2560, 1440
    canvas_img = Image.new("RGBA", (target_w, target_h), (8, 18, 38, 255))
    quad_photos = [
        os.path.join(GAMBAR_DIR, "Gambar6_15_stasiun_teleoperasi_dobot1.jpg"),
        os.path.join(GAMBAR_DIR, "Gambar6_9_integrasi_sistem_mearm.jpg"),
        os.path.join(GAMBAR_DIR, "Gambar6_1_mearm_tampak_depan.jpg"),
        os.path.join(GAMBAR_DIR, "Gambar6_17_manipulator_dobot_suction1.jpg"),
    ]
    qw, qh = target_w // 2, target_h // 2
    positions = [(0, 0), (qw, 0), (0, qh), (qw, qh)]
    for pos, p_path in zip(positions, quad_photos):
        if os.path.exists(p_path):
            im = Image.open(p_path).convert("RGBA")
            im = ImageOps.fit(im, (qw, qh), method=Image.Resampling.LANCZOS)
            canvas_img.paste(im, pos)

    # Gelapkan & beri sedikit blur serta overlay biru dongker pekat (#09152B)
    canvas_img = ImageEnhance.Brightness(canvas_img).enhance(0.42)
    canvas_img = canvas_img.filter(ImageFilter.GaussianBlur(radius=3))
    overlay = Image.new("RGBA", (target_w, target_h), (9, 21, 43, int(255 * 0.78)))
    comp = Image.alpha_composite(canvas_img, overlay).convert("RGB")
    out_cover = os.path.join(GAMBAR_DIR, "cover_bg_kp.png")
    comp.save(out_cover, "PNG", quality=95)
    print(f"[OK] Cover background KP dibuat: {out_cover}")


def render_equations():
    """Merender seluruh persamaan matematika Bab III (3.1-3.8) dan Bab V (5.1-5.2) pada 300 DPI."""
    equations = [
        (
            "eq_3_1_fk.png",
            r"$\phi = \theta_2 + \theta_3 + \theta_4, \qquad r = L_1\cos\theta_2 + L_2\cos(\theta_2+\theta_3) + L_3\cos\phi$" + "\n" +
            r"$X = r\cos\theta_1, \qquad Y = r\sin\theta_1, \qquad Z = d_1 + L_1\sin\theta_2 + L_2\sin(\theta_2+\theta_3) + L_3\sin\phi$",
            (8.2, 1.25), 14.5
        ),
        (
            "eq_3_2_ik_1.png",
            r"$\theta_1 = \mathrm{atan2}(Y, X), \quad r = \sqrt{X^2 + Y^2}, \quad r_w = r - L_3\cos\phi, \quad z_w = Z - d_1 - L_3\sin\phi$" + "\n" +
            r"$c_3 = \frac{r_w^2 + z_w^2 - L_1^2 - L_2^2}{2L_1L_2}, \qquad \theta_3 = \mathrm{atan2}\!\left(\pm\sqrt{1 - c_3^2},\; c_3\right)$",
            (8.2, 1.35), 14.0
        ),
        (
            "eq_3_3_ik_2.png",
            r"$\alpha = \mathrm{atan2}(z_w, r_w), \qquad \beta = \mathrm{atan2}\!\left(L_2\sin\theta_3,\; L_1 + L_2\cos\theta_3\right)$" + "\n" +
            r"$\theta_2 = \alpha - \beta, \qquad \theta_4 = \phi - \theta_2 - \theta_3$",
            (8.2, 1.15), 14.5
        ),
        (
            "eq_norm_landmark.png",
            r"$\Delta x_i = x_i - x_0, \quad \Delta y_i = y_i - y_0, \quad \Delta z_i = z_i - z_0 \quad (i = 0, 1, \dots, 20) \;\Longrightarrow\; \mathbf{v} \in \mathbb{R}^{63}$",
            (7.8, 0.75), 14.5
        ),
        (
            "eq_dnn_softmax.png",
            r"$P(y = k \mid \mathbf{v}) = \frac{\exp(z_k)}{\sum_{j=1}^{26} \exp(z_j)}, \qquad \mathcal{L}_{\mathrm{CE}} = -\sum_{k=1}^{26} y_k \ln P(y = k \mid \mathbf{v})$",
            (7.8, 0.85), 14.5
        ),
        (
            "eq_ema_filter.png",
            r"$\mathbf{P}_t = \alpha\,\mathbf{X}_t + (1 - \alpha)\,\mathbf{P}_{t-1} \quad (\alpha = 0{,}2), \qquad \|\mathbf{P}_t - \mathbf{P}_{t-1}\|_2 > 5{,}0\;\mathrm{mm}$",
            (7.6, 0.75), 14.5
        ),
        (
            "eq_5_1_akurasi.png",
            r"$\mathrm{Akurasi} = \frac{\mathrm{Jumlah\;Prediksi\;Benar}}{\mathrm{Jumlah\;Seluruh\;Data\;Uji}} \times 100\% = \frac{503}{520} \times 100\% = 96{,}73\%$",
            (7.8, 0.85), 15.0
        ),
        (
            "eq_5_2_euclidean.png",
            r"$e = \sqrt{(X_{\mathrm{target}} - X_{\mathrm{aktual}})^2 + (Y_{\mathrm{target}} - Y_{\mathrm{aktual}})^2 + (Z_{\mathrm{target}} - Z_{\mathrm{aktual}})^2}, \qquad \bar{e} = 1{,}90\;\mathrm{mm}$",
            (8.0, 0.85), 14.5
        ),
    ]

    for fname, tex, fsize, pt in equations:
        out_p = os.path.join(EQ_DIR, fname)
        fig, ax = plt.subplots(figsize=fsize, dpi=300)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        ax.axis('off')
        ax.text(0.5, 0.5, tex, fontsize=pt, ha='center', va='center', color='#0F1E4A', linespacing=1.45)
        plt.savefig(out_p, dpi=300, bbox_inches='tight', pad_inches=0.06, facecolor='white')
        plt.close(fig)
        print(f"[OK] Equation dirender: {out_p}")


def crop_and_round_image(img_path, target_size=(520, 270), radius=18):
    """Membuka citra, melakukan center-crop sesuai rasio, dan memberi sudut membulat."""
    im = Image.open(img_path).convert("RGBA")
    im = ImageOps.fit(im, target_size, method=Image.Resampling.LANCZOS)
    mask = Image.new("L", target_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, target_size[0], target_size[1]), radius=radius, fill=255)
    out = Image.new("RGBA", target_size, (255, 255, 255, 0))
    out.paste(im, (0, 0), mask)
    return out


def contain_and_round_image(img_path, target_size=(520, 270), radius=18, bg=(255, 255, 255, 255)):
    """Menampilkan citra utuh (letterbox) tanpa crop, cocok untuk diagram/ilustrasi berlabel."""
    im = Image.open(img_path).convert("RGBA")
    im = ImageOps.contain(im, target_size, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", target_size, bg)
    canvas.paste(im, ((target_size[0] - im.width) // 2, (target_size[1] - im.height) // 2), im)
    mask = Image.new("L", target_size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, target_size[0], target_size[1]), radius=radius, fill=255)
    out = Image.new("RGBA", target_size, (255, 255, 255, 0))
    out.paste(canvas, (0, 0), mask)
    return out


def make_dual_robot_image(path1, path2, target_size=(520, 270), radius=18):
    """Menggabungkan citra Dobot Magician (kiri) dan meArm (kanan) berdampingan."""
    w, h = target_size
    half_w = (w - 8) // 2
    canvas = Image.new("RGBA", target_size, (248, 250, 252, 255))
    im1 = ImageOps.fit(Image.open(path1).convert("RGBA"), (half_w, h), method=Image.Resampling.LANCZOS)
    im2 = ImageOps.fit(Image.open(path2).convert("RGBA"), (half_w, h), method=Image.Resampling.LANCZOS)
    canvas.paste(im1, (0, 0))
    canvas.paste(im2, (half_w + 8, 0))
    mask = Image.new("L", target_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, w, h), radius=radius, fill=255)
    out = Image.new("RGBA", target_size, (255, 255, 255, 0))
    out.paste(canvas, (0, 0), mask)
    return out


def generate_latar_belakang_image_flow():
    """
    Membangun Gambar 1.1 Alur Latar Belakang Berbasis Citra (Visual Image-Flow)
    Sesuai slide_ref_2.png Gilang:
    - 5 Kartu Citra Nyata + Info Footer Singkat Bersitasi di bawah setiap gambar
    - Panah Lengkung Kuning/Emas (Curved Arrows) menghubungkan 1 -> 2 -> 3 -> 4 -> 5 -> GAP RESEARCH
    """
    canvas_w, canvas_h = 2400, 1120
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (244, 247, 251, 255))
    draw = ImageDraw.Draw(canvas)

    from PIL import ImageFont
    font_bold_path = "/system/fonts/Roboto-Bold.ttf"
    font_reg_path = "/system/fonts/Roboto-Regular.ttf"
    font_italic_path = "/system/fonts/Roboto-Italic.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
        font_reg_path = "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans.ttf"
        font_italic_path = font_reg_path

    f_badge = ImageFont.truetype(font_bold_path, 23)
    f_foot_b = ImageFont.truetype(font_bold_path, 22)
    f_foot_r = ImageFont.truetype(font_reg_path, 20)
    f_cite = ImageFont.truetype(font_bold_path, 19)
    f_gap_title = ImageFont.truetype(font_bold_path, 34)
    f_gap_body = ImageFont.truetype(font_reg_path, 22)
    f_gap_bold = ImageFont.truetype(font_bold_path, 22)

    # Ukuran kartu (3 kolom x 2 baris)
    # Baris Atas: Node 1 (Kiri), Node 2 (Tengah), Node 3 (Kanan)
    # Baris Bawah: Node 4 (Kiri), Node 5 (Tengah), Node 6 = GAP RESEARCH (Kanan)
    card_w, card_h = 710, 500
    xs = [45, 845, 1645]
    ys = [25, 585]

    img_w, img_h = 670, 315

    # Siapkan 5 citra untuk Node 1..5
    im_node1 = make_dual_robot_image(
        os.path.join(GAMBAR_DIR, "Gambar3_3_dobot_magician.jpg"),
        os.path.join(GAMBAR_DIR, "Gambar3_4a_mearm_depan.jpg"),
        target_size=(img_w, img_h)
    )
    # Node 2: ambil hanya bagian kerangka tangan (kiri ~39%) agar bebas daftar teks
    lm_src = Image.open(os.path.join(GAMBAR_DIR, "Gambar3_2_mediapipe_landmarks.png")).convert("RGBA")
    lm_hand = lm_src.crop((0, 0, int(lm_src.width * 0.39), lm_src.height))
    lm_hand = ImageOps.contain(lm_hand, (img_w - 40, img_h - 70), method=Image.Resampling.LANCZOS)
    lm_canvas = Image.new("RGBA", (img_w, img_h), (255, 255, 255, 255))
    lm_canvas.paste(lm_hand, ((img_w - lm_hand.width) // 2, img_h - lm_hand.height - 8), lm_hand)
    lm_mask = Image.new("L", (img_w, img_h), 0)
    ImageDraw.Draw(lm_mask).rounded_rectangle((0, 0, img_w, img_h), radius=18, fill=255)
    im_node2 = Image.new("RGBA", (img_w, img_h), (255, 255, 255, 0))
    im_node2.paste(lm_canvas, (0, 0), lm_mask)
    im_node3 = crop_and_round_image(
        os.path.join(GAMBAR_DIR, "latar_belakang_gemini_concept.png"),
        target_size=(img_w, img_h)
    )
    im_node4 = crop_and_round_image(
        os.path.join(GAMBAR_DIR, "Gambar5_5_uji_mearm_sibi.png"),
        target_size=(img_w, img_h)
    )
    im_node5 = crop_and_round_image(
        os.path.join(GAMBAR_DIR, "Gambar5_6_uji_teleoperasi_dobot.png"),
        target_size=(img_w, img_h)
    )

    nodes = [
        {
            "col": 0, "row": 0,
            "img": im_node1,
            "badge": "1. Manipulator 4-DOF & Limitasi HMI",
            "badge_col": (18, 43, 89),
            "line1": "Manipulator 4-DOF vital bagi otomasi presisi, namun HMI",
            "line2": "joystick/pendant kaku & membatasi intuisi alami operator.",
            "cite": "(Craig, 2018; Rautaray & Agrawal, 2015)"
        },
        {
            "col": 1, "row": 0,
            "img": im_node2,
            "badge": "2. Visi Nirsentuh 21 Hand Landmarks",
            "badge_col": (2, 132, 199),
            "line1": "Ekstraksi 21 titik sendi tangan 3D (x, y, z) MediaPipe",
            "line2": "secara real-time tanpa beban komputasi piksel mentah.",
            "cite": "(Lugaresi et al., 2019; Zhang et al., 2020)"
        },
        {
            "col": 2, "row": 0,
            "img": im_node3,
            "badge": "3. Edge Computing Raspberry Pi 5",
            "badge_col": (5, 150, 105),
            "line1": "Inferensi AI dijalankan lokal pada SBC Raspberry Pi 5",
            "line2": "(30 FPS), memangkas latensi cloud & hemat daya.",
            "cite": "(Shi et al., 2016; Satyanarayanan, 2017)"
        },
        {
            "col": 0, "row": 1,
            "img": im_node4,
            "badge": "4. Kendali Diskret SIBI (meArm 4-DOF)",
            "badge_col": (124, 58, 237),
            "line1": "Klasifikasi 26 abjad SIBI (63 fitur geometri) via DNN",
            "line2": "sebagai instruksi aksi diskret pada manipulator meArm.",
            "cite": "(Kosasih, 2012; Goodfellow et al., 2016)"
        },
        {
            "col": 1, "row": 1,
            "img": im_node5,
            "badge": "5. Teleoperasi Kontinu 3D (Dobot)",
            "badge_col": (217, 119, 6),
            "line1": "Translasi koordinat tangan ke ruang kerja (X, Y, Z) via",
            "line2": "Inverse Kinematics & filter anti-jitter pada Dobot.",
            "cite": "(Craig, 2018; Lynch & Park, 2017)"
        },
    ]

    for nd in nodes:
        x = xs[nd["col"]]
        y = ys[nd["row"]]
        # Bayangan halus
        draw.rounded_rectangle((x + 5, y + 6, x + card_w + 5, y + card_h + 6), radius=24, fill=(203, 213, 225, 140))
        # Kartu putih dengan border navy/slate
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=24, fill=(255, 255, 255, 255), outline=(148, 163, 184, 255), width=3)

        # Tempel citra utama
        canvas.paste(nd["img"], (x + 20, y + 18), nd["img"])

        # Badge label di pojok kiri atas citra
        bw = draw.textlength(nd["badge"], font=f_badge) + 34
        draw.rounded_rectangle((x + 32, y + 30, x + 32 + bw, y + 74), radius=14, fill=nd["badge_col"] + (235,), outline=(255, 255, 255, 220), width=2)
        draw.text((x + 49, y + 38), nd["badge"], font=f_badge, fill=(255, 255, 255, 255))

        # Area Footer Info di bawah citra
        fy = y + 344
        draw.rounded_rectangle((x + 16, fy, x + card_w - 16, y + card_h - 14), radius=16, fill=(241, 245, 249, 255), outline=(203, 213, 225, 255), width=2)
        draw.text((x + 30, fy + 12), nd["line1"], font=f_foot_r, fill=(15, 23, 42, 255))
        draw.text((x + 30, fy + 40), nd["line2"], font=f_foot_r, fill=(15, 23, 42, 255))
        draw.text((x + 30, fy + 74), nd["cite"], font=f_cite, fill=nd["badge_col"] + (255,))

    # Kotak ke-6: GAP RESEARCH (Kanan Bawah: col=2, row=1) ala Gilang
    gx, gy = xs[2], ys[1]
    draw.rounded_rectangle((gx + 5, gy + 6, gx + card_w + 5, gy + card_h + 6), radius=24, fill=(203, 213, 225, 160))
    draw.rounded_rectangle((gx, gy, gx + card_w, gy + card_h), radius=24, fill=(15, 30, 68, 255), outline=(245, 158, 11, 255), width=5)

    # Header Pill GAP RESEARCH
    draw.rounded_rectangle((gx + 28, gy + 24, gx + card_w - 28, gy + 88), radius=16, fill=(245, 158, 11, 255))
    gt_w = draw.textlength("GAP RESEARCH", font=f_gap_title)
    draw.text((gx + (card_w - gt_w) / 2, gy + 36), "GAP RESEARCH", font=f_gap_title, fill=(15, 23, 42, 255))

    gap_lines = [
        ("Belum terdapat sistem ", "visi komputer tertanam"),
        ("mandiri pada ", "Raspberry Pi 5"),
        (" yang menyatukan", ""),
        ("dua paradigma kendali manipulator ", "4-DOF:"),
        ("1. Kendali Diskret: ", "Klasifikasi 26 abjad SIBI"),
        ("    (DNN 63 fitur) pada robot ", "meArm."),
        ("2. Kendali Kontinu: ", "Teleoperasi spasial 3D"),
        ("    (X, Y, Z) real-time pada ", "Dobot Magician"),
        ("    dengan evaluasi ", "akurasi, galat (mm), & latensi.")
    ]
    curr_y = gy + 112
    for regular_part, bold_part in gap_lines:
        cx = gx + 34
        if regular_part:
            draw.text((cx, curr_y), regular_part, font=f_gap_body, fill=(241, 245, 249, 255))
            cx += draw.textlength(regular_part, font=f_gap_body)
        if bold_part:
            draw.text((cx, curr_y), bold_part, font=f_gap_bold, fill=(251, 191, 36, 255))
        curr_y += 40

    # Gambar Panah Kuning/Emas Tebal antar kartu:
    # 1 -> 2 (Atas Kiri ke Atas Tengah)
    # 2 -> 3 (Atas Tengah ke Atas Kanan)
    # 3 -> 4 (Dari Atas Kanan mengarah ke Bawah Kiri / atau 3 turun ke bawah dan 1->2->3 lalu ke 4->5->GAP)
    # Agar sangat intuitif dibaca:
    # Panah 1 -> 2 (horizontal atas)
    # Panah 2 -> 3 (horizontal atas)
    # Panah 1/3 -> 4 & 5 -> GAP RESEARCH
    def draw_thick_arrow(p1, p2, color=(245, 158, 11, 255), width=12):
        draw.line([p1, p2], fill=color, width=width)
        # Kepala panah segitiga di p2
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = max((dx**2 + dy**2) ** 0.5, 1.0)
        ux, uy = dx / length, dy / length
        px, py = -uy, ux
        head_len = 28
        head_w = 18
        tip = p2
        b1 = (p2[0] - ux * head_len + px * head_w, p2[1] - uy * head_len + py * head_w)
        b2 = (p2[0] - ux * head_len - px * head_w, p2[1] - uy * head_len - py * head_w)
        draw.polygon([tip, b1, b2], fill=color, outline=(180, 83, 9, 255))

    # Panah 1 -> 2
    draw_thick_arrow((xs[0] + card_w + 6, ys[0] + card_h // 2), (xs[1] - 6, ys[0] + card_h // 2))
    # Panah 2 -> 3
    draw_thick_arrow((xs[1] + card_w + 6, ys[0] + card_h // 2), (xs[2] - 6, ys[0] + card_h // 2))
    # Panah konektor baris atas ke baris bawah (dari tengah bawah baris atas ke baris bawah)
    draw_thick_arrow((xs[0] + card_w // 2, ys[0] + card_h + 6), (xs[0] + card_w // 2, ys[1] - 6))
    draw_thick_arrow((xs[1] + card_w // 2, ys[0] + card_h + 6), (xs[1] + card_w // 2, ys[1] - 6))
    draw_thick_arrow((xs[2] + card_w // 2, ys[0] + card_h + 6), (xs[2] + card_w // 2, ys[1] - 6))
    # Panah 4 -> 5
    draw_thick_arrow((xs[0] + card_w + 6, ys[1] + card_h // 2), (xs[1] - 6, ys[1] + card_h // 2))
    # Panah 5 -> GAP RESEARCH
    draw_thick_arrow((xs[1] + card_w + 6, ys[1] + card_h // 2), (xs[2] - 6, ys[1] + card_h // 2))

    out_path1 = os.path.join(GAMBAR_DIR, "Gambar1_1_latar_belakang_flowchart_asli.png")
    out_path2 = os.path.join(GAMBAR_DIR, "latar_belakang_visual_flow.png")
    canvas.convert("RGB").save(out_path1, "PNG", quality=95)
    canvas.convert("RGB").save(out_path2, "PNG", quality=95)
    print(f"[OK] Gambar 1.1 Visual Image-Flow berhasil dibuat: {out_path1}")


def generate_clean_software_flowchart():
    """
    Memperbaiki Gambar4_2_diagram_alir_software_asli.png yang sebelumnya bertabrakan.
    Menampilkan (a) Alur Perangkat Lunak Mode SIBI (meArm) di kiri dan
    (b) Alur Perangkat Lunak Teleoperasi (Dobot Magician) di kanan dengan jarak presisi.
    """
    fig, ax = plt.subplots(figsize=(14.0, 7.2), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 14.0)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    def draw_box(cx, cy, w, h, text, bg='#E0E7FF', border='#1E3A8A', fg='#0F172A', fontsize=10.5, bold=False):
        rect = patches.FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.04,rounding_size=0.14",
            facecolor=bg, edgecolor=border, linewidth=1.8, zorder=3
        )
        ax.add_patch(rect)
        ax.text(
            cx, cy, text, ha='center', va='center',
            fontsize=fontsize, fontweight='bold' if bold else 'normal',
            color=fg, linespacing=1.25, zorder=4
        )

    def draw_diamond(cx, cy, w, h, text, bg='#FEF3C7', border='#D97706', fg='#0F172A', fontsize=10.0):
        pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
        poly = patches.Polygon(pts, closed=True, facecolor=bg, edgecolor=border, linewidth=1.8, zorder=3)
        ax.add_patch(poly)
        ax.text(
            cx, cy, text, ha='center', va='center',
            fontsize=fontsize, fontweight='bold', color=fg, linespacing=1.2, zorder=4
        )

    def draw_arrow(p1, p2, label=None, label_pos=None):
        arr = patches.FancyArrowPatch(
            p1, p2, arrowstyle='-|>,head_length=0.25,head_width=0.16',
            color='#0F172A', lw=1.8, zorder=5
        )
        ax.add_patch(arr)
        if label and label_pos:
            ax.text(label_pos[0], label_pos[1], label, fontsize=9.5, fontweight='bold', color='#1E3A8A', ha='center', va='center', zorder=6)

    # Judul Kolom Kiri & Kanan (Bebas Tabrakan!)
    ax.text(3.4, 6.82, "(a) Alur Perangkat Lunak Mode SIBI (meArm)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0F1E4A')
    ax.text(10.6, 6.82, "(b) Alur Perangkat Lunak Teleoperasi (Dobot)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0F1E4A')

    # Garis pemisah tengah tipis
    ax.plot([7.0, 7.0], [0.25, 6.95], color='#CBD5E1', linestyle='--', linewidth=1.3, zorder=1)

    # --- KOLOM KIRI: MODE SIBI (meArm) ---
    lx = 3.6
    bw, bh = 4.6, 0.68
    s_ys = [6.10, 5.10, 4.10, 3.10, 1.85, 0.60]

    draw_box(lx, s_ys[0], bw, bh, "Akuisisi Citra Video Kamera\n(OpenCV 640x480, 30 FPS)")
    draw_box(lx, s_ys[1], bw, bh, "Ekstraksi 21 Persendian Tangan\n(MediaPipe Hands 3D)")
    draw_box(lx, s_ys[2], bw, bh, "Normalisasi 63 Koordinat Fitur\nterhadap Titik Acuan Wrist (0,0,0)")
    draw_box(lx, s_ys[3], bw, bh, "Inferensi Model Klasifikasi\nDeep Neural Networks (DNN)")
    draw_diamond(lx, s_ys[4], 4.3, 1.05, "Skor Keyakinan\nConfidence > 0,80?")
    draw_box(lx, s_ys[5], bw, bh, "Pemetaan Titik Aksi Waypoint &\nTransmisi Serial ke meArm 4-DOF", bg='#DCFCE7', border='#059669', bold=True)

    draw_arrow((lx, s_ys[0] - bh / 2), (lx, s_ys[1] + bh / 2))
    draw_arrow((lx, s_ys[1] - bh / 2), (lx, s_ys[2] + bh / 2))
    draw_arrow((lx, s_ys[2] - bh / 2), (lx, s_ys[3] + bh / 2))
    draw_arrow((lx, s_ys[3] - bh / 2), (lx, s_ys[4] + 1.05 / 2))
    draw_arrow((lx, s_ys[4] - 1.05 / 2), (lx, s_ys[5] + bh / 2), label="Ya", label_pos=(lx + 0.32, 1.12))

    # Loop balik "Tidak (Abaikan)" di sisi kiri
    loop_lx = 0.65
    ax.plot([lx - 4.3 / 2, loop_lx, loop_lx], [s_ys[4], s_ys[4], s_ys[0]], color='#B45309', lw=1.8, zorder=4)
    arr_l = patches.FancyArrowPatch((loop_lx, s_ys[0]), (lx - bw / 2, s_ys[0]), arrowstyle='-|>,head_length=0.25,head_width=0.16', color='#B45309', lw=1.8, zorder=5)
    ax.add_patch(arr_l)
    ax.text(loop_lx, 4.0, "Tidak\n(Abaikan)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#B45309',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FEF3C7', edgecolor='#F59E0B', lw=1))

    # --- KOLOM KANAN: MODE TELEOPERASI (Dobot Magician) ---
    rx = 10.4
    t_ys = [6.10, 5.10, 4.10, 2.85, 1.60, 0.60]

    draw_box(rx, t_ys[0], bw, bh, "Akuisisi Citra & Deteksi Tangan\n(MediaPipe Hands 30 FPS)")
    draw_box(rx, t_ys[1], bw, bh, "Ekstraksi Koordinat Spasial\nTitik Wrist & Index Finger Tip")
    draw_box(rx, t_ys[2], bw, bh, "Filter Exponential Smoothing\n(alpha = 0,2 Penapis Jitter)")
    draw_diamond(rx, t_ys[3], 4.3, 1.05, "Pergeseran Jarak\nDelta d > 5,0 mm?")
    draw_box(rx, t_ys[4], bw, bh, "Penyelesaian Inverse Kinematics 3D\nTarget Spasial (X, Y, Z) & Suction")
    draw_box(rx, t_ys[5], bw, bh, "Transmisi USB Serial PTP\nke Dobot Magician (pydobotplus)", bg='#DCFCE7', border='#059669', bold=True)

    draw_arrow((rx, t_ys[0] - bh / 2), (rx, t_ys[1] + bh / 2))
    draw_arrow((rx, t_ys[1] - bh / 2), (rx, t_ys[2] + bh / 2))
    draw_arrow((rx, t_ys[2] - bh / 2), (rx, t_ys[3] + 1.05 / 2))
    draw_arrow((rx, t_ys[3] - 1.05 / 2), (rx, t_ys[4] + bh / 2), label="Ya", label_pos=(rx + 0.32, 2.12))
    draw_arrow((rx, t_ys[4] - bh / 2), (rx, t_ys[5] + bh / 2))

    # Loop balik "Tidak (Filter Jitter)" di sisi kanan
    loop_rx = 13.35
    ax.plot([rx + 4.3 / 2, loop_rx, loop_rx], [t_ys[3], t_ys[3], t_ys[0]], color='#B45309', lw=1.8, zorder=4)
    arr_r = patches.FancyArrowPatch((loop_rx, t_ys[0]), (rx + bw / 2, t_ys[0]), arrowstyle='-|>,head_length=0.25,head_width=0.16', color='#B45309', lw=1.8, zorder=5)
    ax.add_patch(arr_r)
    ax.text(loop_rx, 4.5, "Tidak\n(Filter\nJitter)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#B45309',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FEF3C7', edgecolor='#F59E0B', lw=1))

    out_sw = os.path.join(GAMBAR_DIR, "Gambar4_2_diagram_alir_software_asli.png")
    plt.tight_layout(pad=0.15)
    plt.savefig(out_sw, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"[OK] Gambar 4.2 Flowchart Software (Zero-Collision) dibuat: {out_sw}")


if __name__ == "__main__":
    prepare_cover_and_logos()
    render_equations()
    generate_latar_belakang_image_flow()
    generate_clean_software_flowchart()
    print("[SELESAI] Seluruh aset visual 300 DPI berhasil dibuat.")
