"""Draw a 1024x1024 newspaper front page summing up 20 November 2026.

Standard library + Pillow only. No photos, no network, no third-party
artwork: every mark on the page is a drawn shape or DejaVu text.
Run:  python3 render.py   -> writes entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 62, 110)
GREY = (96, 90, 80)
LIGHT = (232, 226, 212)
RULE = (60, 56, 48)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    """Draw wrapped paragraph; return y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def headline(draw, x, y, text, fnt, max_w, leading):
    """Draw a wrapped headline; return y just below it."""
    return para(draw, x, y, text, fnt, max_w, leading)


def kicker(draw, x, y, text, color=RED):
    f = font(SANS_B, 15)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return y + 21


def rule(draw, x, y, w, width=2, fill=RULE):
    draw.line([(x, y), (x + w, y)], fill=fill, width=width)
    return y + width


def story_box(draw, x, y, w, h, kick, head, body, head_size=25,
              body_size=15, kick_color=RED):
    """One boxed story: kicker, headline, body. Returns bottom y."""
    draw.rectangle([x, y, x + w, y + h], outline=RULE, width=1)
    pad = 12
    cx, cy = x + pad, y + pad
    cw = w - 2 * pad
    cy = kicker(draw, cx, cy, kick, kick_color)
    hf = font(SERIF_B, head_size)
    lead = head_size + 4
    cy = headline(draw, cx, cy, head, hf, cw, lead)
    cy += 4
    bf = font(SANS, body_size)
    para(draw, cx, cy, body, bf, cw, body_size + 5)
    return y + h


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 36  # page margin
    cw = W - 2 * m

    # ---- Masthead -------------------------------------------------
    d.text((m, 26), "THE WORLD IN ONE PAGE", font=font(SERIF_B, 52), fill=INK)
    d.text((m, 92), "FRIDAY, 20 NOVEMBER 2026", font=font(SANS_B, 17), fill=RED)
    d.text((W - m - 348, 92), "ONE IMAGE  •  ALL THE NEWS", font=font(SANS_B, 17), fill=INK)
    rule(d, m, 122, cw, 3)
    rule(d, m, 128, cw, 1)

    # ---- Lead story: Iran -----------------------------------------
    y = 140
    lh = 204
    d.rectangle([m, y, m + cw, y + lh], fill=(255, 253, 246), outline=RULE, width=2)
    cx = m + 16
    cy = y + 12
    cy = kicker(d, cx, cy, "Lead story — Washington / Tehran")
    cy = headline(d, cx, cy, "TRUMP PUSHES IRAN DECISION TO 2027",
                  font(SERIF_B, 40), cw - 32, 46)
    cy += 2
    cy = para(d, cx, cy,
              "\u201cWe\u2019ll see what happens after January 1,\u201d the president said, "
              "putting off any call on renewed strikes until next year. The war "
              "has already cost the US more than $48bn.",
              font(SANS, 16), cw - 32, 21)
    # stat strip inside the lead box
    sy = y + lh - 30
    d.line([(m + 16, sy), (m + cw - 16, sy)], fill=GREY, width=1)
    d.text((m + 16, sy + 6), "WAR COST: $48bn  •  SENATE VOTE: 48\u201351  •  \u201cI\u2019m not rushing\u201d",
           font=font(SANS_B, 14), fill=BLUE)

    # ---- Row 2: summit + ICJ --------------------------------------
    y = 360
    rh = 168
    story_box(d, m, y, 466, rh, "Shenzhen, China",
              "THREE NUCLEAR POWERS, ONE TABLE",
              "Trump, Xi and Putin held their first-ever three-way summit at "
              "APEC in Shenzhen. Nuclear arms control topped the agenda after "
              "New START expired in February; no deal was expected.",
              head_size=24, body_size=15)
    story_box(d, m + 486, y, 466, rh, "The Hague",
              "ICJ: MYANMAR COMMITTED GENOCIDE",
              "The UN\u2019s top court ruled 9\u20136 that Myanmar\u2019s 2017 crackdown on "
              "the Rohingya was genocide \u2014 the first time the court has held "
              "a state responsible for the crime.",
              head_size=24, body_size=15, kick_color=BLUE)

    # ---- Row 3: Voyager / Cyclone / GTA 6 --------------------------
    y = 536
    rh = 196
    col = 306
    gap = 17
    story_box(d, m, y, col, rh, "Space",
              "VOYAGER 1: ONE LIGHT-DAY AWAY",
              "NASA confirmed the probe, launched in 1977, is now a full light-"
              "day from Earth \u2014 16bn miles. A radio signal takes 24 hours "
              "to reach home. The first human object ever that far away.",
              head_size=21, body_size=14)
    story_box(d, m + col + gap, y, col, rh, "India",
              "CYCLONE AKVAN: 300,000 FLEE",
              "About 300,000 people were evacuated in Odisha as Severe Cyclone "
              "Akvan bore down on the coast near Gopalpur, with winds of "
              "90\u2013100 km/h and 9,341 shelters readied.",
              head_size=21, body_size=14, kick_color=BLUE)
    story_box(d, m + 2 * (col + gap), y, col, rh, "Culture",
              "GTA 6 BEATS THE ODYSSEY",
              "Grand Theft Auto VI took an estimated $1.84bn on launch day \u2014 "
              "passing the entire $1.805bn global box-office run of Christopher "
              "Nolan\u2019s The Odyssey. The biggest launch in game history.",
              head_size=21, body_size=14)

    # ---- Row 4: Europe talks + Hayabusa2 ---------------------------
    y = 748
    rh = 152
    story_box(d, m, y, 466, rh, "Berlin",
              "EUROPE READY TO TALK TO RUSSIA",
              "At the Coalition of the Willing summit in Berlin, European "
              "leaders said they are ready for negotiations with Russia to end "
              "the war in Ukraine.",
              head_size=23, body_size=15, kick_color=BLUE)
    story_box(d, m + 486, y, 466, rh, "Space — Japan",
              "HAYABUSA2 LOSES ITS LANDING",
              "Engine trouble has forced JAXA to scrap Hayabusa2\u2019s planned "
              "2031 landing on asteroid 1998 KY26. The probe will instead fly "
              "past a smaller asteroid in April 2028.",
              head_size=23, body_size=15)

    # ---- Also in the news ------------------------------------------
    y = 912
    d.rectangle([m, y, m + cw, y + 62], fill=LIGHT, outline=RULE, width=1)
    d.text((m + 12, y + 7), "ALSO IN THE NEWS", font=font(SANS_B, 14), fill=RED)
    para(d, m + 12, y + 27,
         "Seoul: top court overturns ex-PM Han Duck-soo\u2019s conviction  •  "
         "Riyadh: Houthi attack damages Saudi wealth-fund tower  •  "
         "US and Venezuela restore military ties  •  North Korea expands "
         "uranium enrichment at Yongbyon  •  Fiji declares drought disaster.",
         font(SANS, 13), cw - 24, 17)

    # ---- Footer ----------------------------------------------------
    d.text((m, 986), "Sources: Reuters, BBC, NASA, JAXA, IMD, The Hindu, Sensor Tower.",
           font=font(SANS, 12), fill=GREY)
    d.text((W - m - 118, 986), "20 NOV 2026", font=font(SANS_B, 12), fill=GREY)

    img.save("entry.png")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
