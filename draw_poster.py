#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news poster (1024x1024 PNG).

Newspaper-style poster, round 2: a dominant full-width lead story
(Huang returns as Nvidia CEO), then six stories in a two-by-three
grid, then a full-width strip for the eighth story. Every story was
checked against live reporting on 23 November 2026; the three
replaced stories (Grok lawsuits, Wall Street rally, Iran sanctions)
are all Monday 23 November actions, verified against primary
sources. Claims are labelled as claims and tolls use the lowest
figure several outlets agreed on that day. Run: python3 draw_poster.py
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (250, 248, 243)
NAVY = (20, 33, 61)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
GREY = (110, 110, 110)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, using PIL textlength."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


LEAD = ("TECH \u00b7 SANTA CLARA", (0, 120, 80),
        "Huang returns as Nvidia CEO",
        "Trump convinces the board to reinstate Jensen Huang as chief "
        "executive; shares jump 31%, adding a record $952 billion in a day.",
        "Reuters \u00b7 USA Today")

STORIES = [
    ("CLIMATE \u00b7 ANTALYA", (0, 128, 128),
     "COP31 collapses with no deal",
     "Talks collapse Sunday after record overtime; the EU and about 130 nations reject a text with no fossil fuels.",
     "CNN \u00b7 Reuters"),
    ("CONFLICT \u00b7 LIBYA", (178, 34, 34),
     "Russian warship sinks at Benghazi",
     "Ukraine confirms it sank corvette Merkury with seven sea drones; ten hurt.",
     "CNN \u00b7 WSJ"),
    ("USA \u00b7 WASHINGTON", (150, 90, 160),
     "Democrats take 258 House seats",
     "Ties the 1992 high of 258 seats. Hubbard beats Foxx by 330 votes in a North Carolina recount.",
     "AP \u00b7 Reuters"),
    ("TECH \u00b7 VIRGINIA", (120, 40, 140),
     "Two states sue SpaceX over Grok deepfakes",
     "Virginia and Oregon sue over Grok making sexual images of real people, including children.",
     "Reuters \u00b7 NY Post"),
    ("MARKETS \u00b7 NEW YORK", (160, 120, 0),
     "Wall Street posts best day since April 2025",
     "Dow gains 1,448 points, Nasdaq jumps 6.5% and the S&P 500 rises 4.7%.",
     "CNN \u00b7 WSJ"),
    ("MIDDLE EAST \u00b7 WASHINGTON", (160, 82, 45),
     "US hits Iran with sweeping new sanctions",
     "Treasury targets over two dozen firms in Iran's shadow banking network.",
     "Reuters"),
]

STRIP = ("UKRAINE \u00b7 DYMER", (0, 90, 160),
         "Strike on flats kills at least 11",
         "A Russian drone hits a five-storey block north of Kyiv; rescue ends Monday with the toll final at 11.",
         "Reuters")


def card(draw, x, y, w, h, num, tag, colour, head, body, src,
         head_size=25, body_size=18):
    """Draw one grid card. Headline up to 2 lines, body capped so it
    never reaches the source line."""
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255),
                   outline=(210, 205, 195), width=1)
    draw.rectangle([x, y, x + 6, y + h], fill=colour)
    cx, cy = x + w - 26, y + 22
    draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=colour)
    draw.text((cx, cy), str(num), font=font(SANS_B, 18),
              fill=(255, 255, 255), anchor="mm")
    tx = x + 18
    draw.text((tx, y + 10), tag, font=font(SANS_B, 15), fill=colour)
    lines = wrap(draw, head, font(SERIF_B, head_size), w - 56)
    hy = y + 34
    for ln in lines[:2]:
        draw.text((tx, hy), ln, font=font(SERIF_B, head_size), fill=INK)
        hy += head_size + 4
    blines = wrap(draw, body, font(SANS, body_size), w - 36)
    max_body = 2 if len(lines) > 1 else 3
    by = hy + 4
    for ln in blines[:max_body]:
        draw.text((tx, by), ln, font=font(SANS, body_size), fill=(60, 60, 60))
        by += body_size + 4
    draw.text((tx, y + h - 26), "Source: " + src, font=font(SANS, 14), fill=GREY)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 140], fill=NAVY)
    d.text((28, 14), "THE WORLD IN ONE DAY", font=font(SANS_B, 26), fill=GOLD)
    d.text((28, 44), "MONDAY 23 NOVEMBER 2026", font=font(SERIF_B, 44), fill=(255, 255, 255))
    d.text((28, 102), "Eight stories that defined the day \u2014 from Santa Clara to Antalya, Benghazi to Washington",
           font=font(SANS, 19), fill=(200, 205, 220))
    d.rectangle([0, 140, W, 146], fill=GOLD)
    margin, gap = 16, 12
    # Lead story: full width, dominant
    tag, colour, head, body, src = LEAD
    lx, ly, lw, lh = margin, 156, W - 2 * margin, 196
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=(255, 255, 255),
                outline=(210, 205, 195), width=1)
    d.rectangle([lx, ly, lx + 8, ly + lh], fill=GOLD)
    d.rectangle([lx + 8, ly, lx + lw, ly + 6], fill=colour)
    d.text((lx + 28, ly + 12), "THE DAY'S BIGGEST STORY", font=font(SANS_B, 15), fill=colour)
    d.text((lx + 28, ly + 36), tag, font=font(SANS_B, 15), fill=GREY)
    cx, cy = lx + lw - 34, ly + 34
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=colour)
    d.text((cx, cy), "1", font=font(SANS_B, 22), fill=(255, 255, 255), anchor="mm")
    lines = wrap(d, head, font(SERIF_B, 34), lw - 90)
    hy = ly + 62
    for ln in lines[:1]:
        d.text((lx + 28, hy), ln, font=font(SERIF_B, 34), fill=INK)
        hy += 42
    blines = wrap(d, body, font(SANS, 20), lw - 56)
    by = hy + 4
    for ln in blines[:2]:
        d.text((lx + 28, by), ln, font=font(SANS, 20), fill=(60, 60, 60))
        by += 26
    d.text((lx + 28, ly + lh - 26), "Source: " + src, font=font(SANS, 14), fill=GREY)
    # Grid: stories 2-7, 2 columns x 3 rows
    cell_w = (W - 2 * margin - gap) // 2
    cell_h = 168
    top = ly + lh + gap
    for i, (tag, colour, head, body, src) in enumerate(STORIES):
        r, c = divmod(i, 2)
        x = margin + c * (cell_w + gap)
        y = top + r * (cell_h + gap)
        card(d, x, y, cell_w, cell_h, i + 2, tag, colour, head, body, src)
    # Strip: story 8, full width
    tag, colour, head, body, src = STRIP
    sx, sy, sw, sh = margin, top + 3 * cell_h + 2 * gap + gap, W - 2 * margin, 72
    d.rectangle([sx, sy, sx + sw, sy + sh], fill=(255, 255, 255),
                outline=(210, 205, 195), width=1)
    d.rectangle([sx, sy, sx + 6, sy + sh], fill=colour)
    cx, cy = sx + sw - 26, sy + 22
    d.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=colour)
    d.text((cx, cy), "8", font=font(SANS_B, 18), fill=(255, 255, 255), anchor="mm")
    d.text((sx + 18, sy + 8), tag, font=font(SANS_B, 14), fill=colour)
    d.text((sx + 18, sy + 28), head, font=font(SERIF_B, 21), fill=INK)
    d.text((sx + 18, sy + 52), body, font=font(SANS, 15), fill=(60, 60, 60))
    # Footer
    fy = sy + sh + 8
    d.text((margin, fy), "Sources: AP \u00b7 Reuters \u00b7 CNN \u00b7 WSJ \u00b7 USA Today \u00b7 NY Post",
           font=font(SANS, 14), fill=GREY)
    d.text((margin, fy + 18), "All stories are events of Monday 23 November 2026, or first reported that day.",
           font=font(SANS, 14), fill=GREY)
    img.save("image.png", optimize=True)
    print("wrote image.png", img.size)


if __name__ == "__main__":
    main()
