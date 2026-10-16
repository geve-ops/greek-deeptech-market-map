"""Render the market map PNG and PDF from the Include/Borderline rows of the dataset."""
import csv, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib import font_manager as fm

CSV, OUT = sys.argv[1], sys.argv[2]  # OUT without extension

BG, PURPLE, BLUE, NAVY = "#faf8f3", "#7a5cc4", "#4aa3f0", "#273B7B"
GREY, LIGHT = "#8a8fa3", "#ece8f5"


import os as _os
_fp = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "fonts", "RedHatMono[wght].ttf")
if _os.path.exists(_fp):
    fm.fontManager.addfont(_fp)

names = {f.name for f in fm.fontManager.ttflist}
TITLE_FONT = next((n for n in ("Red Hat Mono", "Consolas", "DejaVu Sans Mono") if n in names), "monospace")
BODY_FONT = next((n for n in ("Segoe UI", "Arial", "DejaVu Sans") if n in names), "sans-serif")

SHORT = {
    "TileDB (rebranded Tile.ai)": "TileDB / Tile.ai",
    "Open Cosmos (Open Cosmos Aegean)": "Open Cosmos Aegean",
    "Core Innovation and Technology": "Core Innovation",
    "Circuits Integrated Hellas": "Circuits Integrated",
}

rows = [r for r in csv.DictReader(open(CSV, encoding="utf-8-sig"))
        if r["map_status"] in ("Include", "Borderline")]

def bucket(r):
    st = r["stage"].lower()
    if "exited" in st:
        return "exit"
    if any(k in st for k in ("series", "late stage", "growth")):
        return "growth"
    if any(k in st for k in ("seed", "pre-seed")):
        return "early"
    return "other"

COL = {"early": BLUE, "growth": PURPLE, "exit": NAVY, "other": "#c9ccd8"}

layout = [
    ["Robotics & Drones", "AI & Machine Learning", "Health & Biotech", "Space & Defense"],
    ["Semiconductors & Hardware", "Energy & Climate Tech", "Quantum & Advanced Computing", "Industrial & Manufacturing Tech"],
]

fig = plt.figure(figsize=(16, 10.5), facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 160); ax.set_ylim(0, 105); ax.axis("off"); ax.set_facecolor(BG)

ax.add_patch(Rectangle((0, 100.2), 160, 0.8, color=PURPLE, lw=0))
ax.add_patch(Rectangle((0, 100.2), 55, 0.8, color=BLUE, lw=0))
ax.text(5, 94.5, "Greek Deep Tech Market Map", fontfamily=TITLE_FONT, fontsize=30, fontweight="bold", color=NAVY, va="center")
ax.text(5, 89.3, f"{len(rows)} companies founded in Greece or by Greeks with a Greek presence  |  data as of 2026-10-16  |  sources in dataset",
        fontfamily=BODY_FONT, fontsize=12, color=GREY, va="center")

margin, gap = 5, 2.5
cw = (160 - 2 * margin - 3 * gap) / 4
row_h = [52, 23]
top = 85
ys = [top - row_h[0], top - row_h[0] - gap - row_h[1]]

for ri, cats in enumerate(layout):
    for ci, cat in enumerate(cats):
        x = margin + ci * (cw + gap)
        y, h = ys[ri], row_h[ri]
        ax.add_patch(FancyBboxPatch((x, y), cw, h, boxstyle="round,pad=0,rounding_size=1.2",
                                    fc="white", ec=PURPLE if ri == 0 else BLUE, lw=1.6))
        ax.add_patch(Rectangle((x, y + h - 4.6), cw, 4.6, color=NAVY, lw=0))
        ax.text(x + 1.5, y + h - 2.3, cat.upper(), fontfamily=TITLE_FONT, fontsize=10.5,
                fontweight="bold", color="white", va="center")
        items = sorted([r for r in rows if r["category"] == cat],
                       key=lambda r: (r["map_status"] != "Include", r["company"].lower()))
        ty = y + h - 7.6
        if not items:
            ax.text(x + 1.8, ty, "No verified venture-backed\ncompany yet. White space:\nsee thesis.", fontfamily=BODY_FONT,
                    fontsize=10.5, color=PURPLE, va="top", style="italic", linespacing=1.5)
            continue
        for r in items:
            nm = SHORT.get(r["company"], r["company"])
            border = r["map_status"] == "Borderline"
            ax.add_patch(Rectangle((x + 1.6, ty - 0.45), 0.9, 0.9, color=COL[bucket(r)], lw=0))
            ax.text(x + 3.4, ty, nm + (" *" if border else ""), fontfamily=BODY_FONT, fontsize=11.5,
                    color=GREY if border else NAVY, va="center", fontweight="normal" if border else "semibold")
            ty -= 3.8

ly = 5.2
ax.text(5, ly, "Stage:", fontfamily=BODY_FONT, fontsize=10.5, color=NAVY, va="center", fontweight="bold")
lx = 13
for key, label in (("early", "Pre-seed / seed"), ("growth", "Series A and later"), ("exit", "Exited"), ("other", "Stage or funding not found")):
    ax.add_patch(Rectangle((lx, ly - 0.45), 0.9, 0.9, color=COL[key], lw=0))
    ax.text(lx + 1.6, ly, label, fontfamily=BODY_FONT, fontsize=10.5, color=NAVY, va="center")
    lx += 8 + len(label) * 0.95
ax.text(5, 2.4, "* Borderline: Greek link or deep-tech fit not fully confirmed (grey text). Held-out names (for example Axelera AI) are in the dataset but not on the map. "
        "Company names shown as text only.", fontfamily=BODY_FONT, fontsize=9, color=GREY, va="center")

fig.savefig(OUT + ".png", dpi=200, facecolor=BG)
fig.savefig(OUT + ".pdf", facecolor=BG)
print(len(rows), "companies;", TITLE_FONT, "/", BODY_FONT)
