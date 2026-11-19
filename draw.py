#!/usr/bin/env python3
"""Render the make.fun news-image-20261119 entry.

Draws a clean, legible 1024x1024 infographic of Thursday 19 November 2026's
world news: a dark-navy page, a header naming the day, five numbered
colour-accented story cards, and a footer sources line. Deterministic:
fixed fonts, fixed colours, no timestamps, no randomness, so repeated runs
produce byte-identical output.

Usage: python3 draw.py [output-path]  (default: entry.png next to this file)
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

NAVY = (10, 25, 41)          # page background
CARD = (18, 38, 61)          # story card background
WHITE = (255, 255, 255)
BODY = (199, 211, 224)       # body text
MUTED = (122, 143, 166)      # footer text
GOLD = (245, 166, 35)        # header accent

ACCENTS = [
    (245, 166, 35),   # 1 summit: amber
    (46, 204, 113),   # 2 IPO: green
    (155, 89, 182),   # 3 GTA VI: purple
    (231, 76, 60),    # 4 Gaza/Crimea: red
    (52, 152, 219),   # 5 EU loan: blue
]

STORIES = [
    (
        "Trump, Xi & Putin Meet in Shenzhen",
        "Donald Trump, Xi Jinping and Vladimir Putin hold a trilateral "
        "summit in Shenzhen on the sidelines of the APEC meeting.",
    ),
    (
        "Anthropic's Record $81.3B IPO",
        "Priced at $83 a share, the 980-million-share offering raises "
        "$81.3 billion \u2014 the largest IPO ever. Trading starts on the "
        "Nasdaq as ANT.",
    ),
    (
        "GTA VI Rolls Out Worldwide",
        "The midnight launch begins in New Zealand on PS5 and Xbox "
        "Series X|S, after about 15.9 million preorders worth $1.5 billion.",
    ),
    (
        "Gaza Ground Op, Crimea Bridge Hit",
        "Israeli troops launch a ground operation in central Gaza, and "
        "the Crimea bridge is attacked again, suspending traffic.",
    ),
    (
        "EU Proposes \u20ac45B Loan for Ukraine",
        "Brussels proposes a \u20ac45 billion loan for Kyiv, to be repaid "
        "after Russia pays reparations for the war.",
    ),
]

FOOTER = "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u2014 19 November 2026"


def load_font(bold, size):
    """Load Noto Sans, falling back to DejaVu Sans if it is missing."""
    candidates = [
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if os.path.isfile(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    """Split text into lines that fit max_width pixels."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=font) <= max_width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png"
    )

    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)

    font_date = load_font(True, 30)
    font_title = load_font(True, 46)
    font_card_title = load_font(True, 28)
    font_body = load_font(False, 22)
    font_footer = load_font(False, 17)
    font_num = load_font(True, 28)

    # Header.
    draw.text((48, 36), "THURSDAY, 19 NOVEMBER 2026", font=font_date, fill=GOLD)
    draw.text((48, 74), "World News in One Image", font=font_title, fill=WHITE)
    draw.rectangle([48, 142, W - 48, 146], fill=GOLD)

    # Story cards.
    card_x, card_w = 48, W - 96
    card_h, gap = 138, 14
    y = 168
    for i, (title, body) in enumerate(STORIES):
        accent = ACCENTS[i]
        # Card body with rounded corners and a left accent bar.
        draw.rounded_rectangle(
            [card_x, y, card_x + card_w, y + card_h], radius=16, fill=CARD
        )
        draw.rounded_rectangle(
            [card_x, y, card_x + 8, y + card_h], radius=4, fill=accent
        )
        # Number circle.
        cx, cy, r = card_x + 52, y + card_h // 2, 28
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent)
        num = str(i + 1)
        nw = draw.textlength(num, font=font_num)
        nh = font_num.size
        draw.text((cx - nw / 2, cy - nh / 2 - 2), num, font=font_num, fill=WHITE)
        # Title and body.
        tx = card_x + 104
        tw = card_x + card_w - 24 - tx
        draw.text((tx, y + 16), title, font=font_card_title, fill=WHITE)
        lines = wrap_text(draw, body, font_body, tw)
        by = y + 56
        for line in lines[:2]:
            draw.text((tx, by), line, font=font_body, fill=BODY)
            by += 30
        y += card_h + gap

    # Footer.
    fw = draw.textlength(FOOTER, font=font_footer)
    draw.text(((W - fw) / 2, 952), FOOTER, font=font_footer, fill=MUTED)

    img.save(out_path, format="PNG")
    print("wrote %s (%d bytes)" % (out_path, os.path.getsize(out_path)))


if __name__ == "__main__":
    main()
