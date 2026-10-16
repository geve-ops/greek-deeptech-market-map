"""Consulting-style market map with logos. Run: python scripts/build_map_v2.py <csv> <out_without_ext>

Reads logos/choices.json: {company: {"file": "<prepared png in logos/prep>", "mode": "wide|icon", "invert": false}}
Companies without a chosen logo get a text wordmark.
"""
import csv, json, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CSV, OUT = sys.argv[1], sys.argv[2]

for f in ("RedHatMono-Regular.ttf", "RedHatMono-Bold.ttf"):
    fp = os.path.join(ROOT, "fonts", f)
    if os.path.exists(fp):
        fm.fontManager.addfont(fp)
names = {f.name for f in fm.fontManager.ttflist}
TF = "Red Hat Mono" if "Red Hat Mono" in names else "Consolas"
BF = next((n for n in ("Segoe UI", "Arial", "DejaVu Sans") if n in names), "sans-serif")

BG, PURPLE, BLUE, NAVY, GREY, LINE = "#faf8f3", "#7a5cc4", "#4aa3f0", "#273B7B", "#8a8fa3", "#d9d6e6"

SHORT = {"TileDB (rebranded Tile.ai)": "TileDB / Tile.ai", "Open Cosmos (Open Cosmos Aegean)": "Open Cosmos Aegean",
         "Core Innovation and Technology": "Core Innovation", "Circuits Integrated Hellas": "Circuits Integrated"}

# category -> ordered sub-boxes -> companies (CSV names)
STRUCT = [
    ("Robotics & Drones", [
        ("Physical AI & robot components", ["Acumino", "Progressive Robotics", "Bota Systems", "Gizelis Robotics"]),
        ("Inspection & agri robotics", ["Perceptual Robotics", "Augmenta", "Robenso"]),
        ("Drones & unmanned systems", ["Velos Rotors", "Altus LSA", "SAS Technology", "Aether Aeronautics", "Ucandrone"]),
    ]),
    ("Semiconductors & Hardware", [
        ("Chips, sensing & hardware", ["Axelera AI", "Think Silicon", "Circuits Integrated Hellas", "SolidWatts", "Navenio"]),
    ]),
    ("AI & Machine Learning", [
        ("Enterprise & applied AI", ["Moveo.AI", "Keragon", "Intryc", "Pallma AI", "Satori Analytics"]),
        ("Data & developer infrastructure", ["TileDB (rebranded Tile.ai)", "Bitloops", "Proxy Foods AI"]),
    ]),
    ("Health & Biotech", [
        ("AI drug discovery & diagnostics", ["Intelligencia", "Achira AI", "Causaly", "Purposeful", "Brainomix", "Anacalypsis Therapeutics"]),
        ("Medtech & digital health", ["ORamaVR", "Corsmed", "Anodyne Nanotech", "Feel Therapeutics", "Bioemtech"]),
    ]),
    ("Space & Defense", [
        ("Space", ["Prisma Electronics", "Open Cosmos (Open Cosmos Aegean)"]),
        ("Defense & security", ["Delian Alliance Industries", "Hack The Box", "Sotiria Technology"]),
    ]),
    ("Energy & Climate Tech", [
        ("Climate data, agri & circular", ["WeatherXM", "Better Origin", "Centaur Analytics"]),
    ]),
    ("Industrial & Manufacturing Tech", [
        ("Maritime, materials & industrial AI", ["DeepSea Technologies", "MarineTraffic", "iCOMAT", "Core Innovation and Technology", "Code BGP"]),
    ]),
    ("Quantum & Advanced Computing", []),
]
COLUMNS = [[0, 1], [2, 3], [4, 5, 6, 7]]  # indexes into STRUCT per page column

rows = {r["company"]: r for r in csv.DictReader(open(CSV, encoding="utf-8-sig"))}
mapped = {k for k, r in rows.items() if r["map_status"] in ("Include", "Borderline")}
placed = {c for _, subs in STRUCT for _, cs in subs for c in cs}
assert placed == mapped, (placed ^ mapped)

choices = {}
cp = os.path.join(ROOT, "logos", "choices.json")
if os.path.exists(cp):
    choices = json.load(open(cp))


def bucket(r):
    st = r["stage"].lower()
    if "exited" in st: return "exit"
    if any(k in st for k in ("series", "late stage", "growth")): return "growth"
    if any(k in st for k in ("seed", "pre-seed")): return "early"
    return "other"

SC = {"early": BLUE, "growth": PURPLE, "exit": NAVY, "other": "#c3c6d4"}

W, H = 22.0, 16.0
fig = plt.figure(figsize=(W, H), facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# header
ax.add_patch(Rectangle((0, H - 0.22), W, 0.22, color=PURPLE, lw=0))
ax.add_patch(Rectangle((0, H - 0.22), W * 0.3, 0.22, color=BLUE, lw=0))
ax.text(0.6, H - 0.95, "GREEK DEEP TECH MARKET MAP", fontfamily=TF, fontsize=34, fontweight="bold", color=NAVY, va="center")
n = len(mapped)
ax.text(0.6, H - 1.6, f"{n} companies founded in Greece, or by Greeks with a Greek presence  |  pre-seed to late stage  |  data as of 16 Oct 2026",
        fontfamily=BF, fontsize=14, color=GREY, va="center")

PAD, GAP = 0.6, 0.45
colw = (W - 2 * PAD - 2 * GAP) / 3
CELL_COLS = 3
cellw = colw / CELL_COLS
cellh = 0.98
HEAD = 0.42
CAT = 0.5
top = H - 2.1
bottom_limit = 1.55


def draw_logo(cx, cy, w, h, company, border):
    ch = choices.get(company)
    alpha = 1.0
    name = SHORT.get(company, company)
    if ch:
        p = os.path.join(ROOT, "logos", "prep", ch["file"])
        im = Image.open(p).convert("RGBA")
        if ch.get("invert"):
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (r.point(lambda v: 255 - v), g.point(lambda v: 255 - v), b.point(lambda v: 255 - v), a))
        iw, ih = im.size
        mode = ch.get("mode", "wide")
        if mode == "icon":
            # icon at left, name text at right
            side = min(h * 0.62, 0.62)
            sc = min(side / ih, side / iw)
            tw, th = iw * sc, ih * sc
            x0 = cx - w * 0.5 + 0.1
            ax.imshow(im, extent=(x0, x0 + tw, cy - th / 2, cy + th / 2), alpha=alpha, zorder=3, aspect="auto")
            ax.text(x0 + tw + 0.08, cy, name, fontfamily=BF, fontsize=9.2, fontweight="bold", color=NAVY, alpha=alpha,
                    va="center", ha="left", zorder=3)
        else:
            maxw, maxh = w * 0.78, h * 0.5
            sc = min(maxw / iw, maxh / ih)
            tw, th = iw * sc, ih * sc
            if ch.get("dark_bg"):
                ax.add_patch(FancyBboxPatch((cx - tw / 2 - 0.08, cy - th / 2 - 0.07), tw + 0.16, th + 0.14,
                             boxstyle="round,pad=0,rounding_size=0.05", fc=NAVY, ec="none", alpha=alpha, zorder=2))
            ax.imshow(im, extent=(cx - tw / 2, cx + tw / 2, cy - th / 2, cy + th / 2), alpha=alpha, zorder=3, aspect="auto")
    else:
        ax.text(cx, cy, name, fontfamily=BF, fontsize=10.5, fontweight="bold", color=NAVY, alpha=alpha, ha="center", va="center", zorder=3)


def box_height(nco):
    r = (nco + CELL_COLS - 1) // CELL_COLS
    return HEAD + r * cellh + 0.12


for ci, cats in enumerate(COLUMNS):
    x0 = PAD + ci * (colw + GAP)
    y = top
    for si in cats:
        cat, subs = STRUCT[si]
        ax.add_patch(Rectangle((x0, y - CAT), colw, CAT, color=NAVY, lw=0, zorder=2))
        ax.text(x0 + 0.18, y - CAT / 2, cat.upper(), fontfamily=TF, fontsize=12.5, fontweight="bold", color="white", va="center", zorder=3)
        y -= CAT + 0.1
        if not subs:
            hh = 1.15
            ax.add_patch(FancyBboxPatch((x0, y - hh), colw, hh, boxstyle="round,pad=0,rounding_size=0.06", fc="white", ec=PURPLE, lw=1.4, ls=(0, (4, 3))))
            ax.text(x0 + colw / 2, y - hh / 2, "White space: no verified venture-backed\nGreek company found yet", fontfamily=BF, fontsize=11,
                    style="italic", color=PURPLE, ha="center", va="center", linespacing=1.5)
            y -= hh + 0.3
            continue
        for sub, cos in subs:
            bh = box_height(len(cos))
            ax.add_patch(FancyBboxPatch((x0, y - bh), colw, bh, boxstyle="round,pad=0,rounding_size=0.06", fc="white", ec=NAVY, lw=1.2, zorder=1))
            ax.add_patch(Rectangle((x0, y - HEAD), colw, HEAD, color=PURPLE, lw=0, zorder=2))
            ax.text(x0 + colw / 2, y - HEAD / 2, sub, fontfamily=BF, fontsize=11, fontweight="bold", color="white", ha="center", va="center", zorder=3)
            for i, c in enumerate(cos):
                r, col = divmod(i, CELL_COLS)
                n_row = min(CELL_COLS, len(cos) - r * CELL_COLS)
                # center partial rows
                off = (CELL_COLS - n_row) * cellw / 2
                cx = x0 + off + col * cellw + cellw / 2
                cy = y - HEAD - 0.06 - r * cellh - cellh / 2
                row = rows[c]
                border = row["map_status"] == "Borderline"
                draw_logo(cx, cy + 0.04, cellw, cellh, c, border)
                bk = bucket(row)
                ax.add_patch(Rectangle((cx - cellw * 0.3, cy - cellh / 2 + 0.06), cellw * 0.6, 0.05, color=SC[bk], lw=0, zorder=3))
                if border:
                    ax.text(cx + cellw * 0.36, cy + cellh / 2 - 0.12, "*", fontfamily=BF, fontsize=11, color=GREY, ha="center", va="center", zorder=4)
            y -= bh + 0.22
        y -= 0.1

# legend and footer
ly = 1.0
ax.add_patch(Rectangle((PAD, 0.45), W - 2 * PAD, 0.95, fc="#ece8f5", ec="none", zorder=0))
ax.text(PAD + 0.25, ly + 0.15, "STAGE (underline)", fontfamily=TF, fontsize=9.5, fontweight="bold", color=NAVY, va="center")
lx = PAD + 2.7
for key, label in (("early", "Pre-seed / seed"), ("growth", "Series A and later"), ("exit", "Exited"), ("other", "Stage or funding not found")):
    ax.add_patch(Rectangle((lx, ly + 0.1), 0.4, 0.07, color=SC[key], lw=0))
    ax.text(lx + 0.5, ly + 0.15, label, fontfamily=BF, fontsize=10.5, color=NAVY, va="center")
    lx += 0.9 + len(label) * 0.115
ax.text(lx + 0.3, ly + 0.15, "*  Greek link or deep-tech fit not fully confirmed", fontfamily=BF, fontsize=10.5, color=GREY, va="center")
ax.text(PAD + 0.25, ly - 0.25, "Logos are trademarks of their respective owners and are shown for identification only. Sources and funding data: see dataset (source_link per company). "
        "Created by Gerald Velas.", fontfamily=BF, fontsize=9, color=GREY, va="center")

fig.savefig(OUT + ".png", dpi=200, facecolor=BG)
fig.savefig(OUT + ".pdf", facecolor=BG)
print("rendered", n, "companies;", len(choices), "logos chosen")
