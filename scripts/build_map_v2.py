"""Clean market map with logos and company names underneath.
Run: python scripts/build_map_v2.py <csv> <out_without_ext> [text]   (add "text" for the names-only version)

Reads logos/choices.json: {company: {"file": "<prepared png in logos/prep>", "mode": "wide|icon", "dark_bg": false}}
Companies without a chosen logo are shown as a bold text name.
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

BG, PURPLE, BLUE, NAVY, GREY, LINE = "#faf8f3", "#7a5cc4", "#4aa3f0", "#273B7B", "#6b7089", "#dcd8e8"

SHORT = {"TileDB (rebranded Tile.ai)": "TileDB (Tile.ai)", "Open Cosmos (Open Cosmos Aegean)": "Open Cosmos",
         "Core Innovation and Technology": "Core Innovation", "Circuits Integrated Hellas": "Circuits Integrated",
         "Anacalypsis Therapeutics": "Anacalypsis", "Mind The Hack": "Mind The Hack", "Delian Alliance Industries": "Delian Alliance",
         "DeepSea Technologies": "DeepSea", "Sotiria Technology": "Sotiria"}

STRUCT = [
    ("Robotics & Drones", [
        ("Physical AI & robot components", ["Acumino", "Progressive Robotics", "Bota Systems", "Gizelis Robotics"]),
        ("Inspection & agri robotics", ["Perceptual Robotics", "Augmenta", "Robenso", "Terra Robotics"]),
        ("Drones & unmanned systems", ["Velos Rotors", "Altus LSA", "SAS Technology", "Aether Aeronautics", "Ucandrone"]),
    ]),
    ("Semiconductors & Hardware", [
        ("Chips, sensing & hardware", ["Axelera AI", "Think Silicon", "Circuits Integrated Hellas", "SolidWatts", "Navenio"]),
    ]),
    ("AI & Machine Learning", [
        ("Enterprise & applied AI", ["Moveo.AI", "Keragon", "Intryc", "Pallma AI", "Satori Analytics", "Seervision", "Intelistyle"]),
        ("Data & developer infrastructure", ["TileDB (rebranded Tile.ai)", "Bitloops", "Proxy Foods AI"]),
    ]),
    ("Health & Biotech", [
        ("AI drug discovery & diagnostics", ["Intelligencia", "Achira AI", "Causaly", "Purposeful", "Brainomix", "Anacalypsis Therapeutics"]),
        ("Medtech & digital health", ["ORamaVR", "Corsmed", "Anodyne Nanotech", "Feel Therapeutics", "Bioemtech", "Pleioflow"]),
    ]),
    ("Space & Defense", [
        ("Space", ["Prisma Electronics", "Open Cosmos (Open Cosmos Aegean)", "Attisat"]),
        ("Defense & security", ["Delian Alliance Industries", "Hack The Box", "Sotiria Technology", "Mind The Hack", "Hoplon AI", "Satways"]),
    ]),
    ("Energy & Climate Tech", [
        ("Climate, energy & agri tech", ["WeatherXM", "Better Origin", "Centaur Analytics", "PlugSecure", "Pinepeak", "ClearDrop", "Neurohive"]),
    ]),
    ("Industrial & Manufacturing Tech", [
        ("Maritime, materials & industrial AI", ["DeepSea Technologies", "MarineTraffic", "iCOMAT", "Core Innovation and Technology", "Code BGP"]),
    ]),
    ("Quantum & Advanced Computing", []),
]
COLUMNS = [[0, 7], [1, 2], [3, 6], [4, 5]]

rows = {r["company"]: r for r in csv.DictReader(open(CSV, encoding="utf-8-sig"))}
mapped = {k for k, r in rows.items() if r["map_status"] in ("Include", "Borderline")}
placed = {c for _, subs in STRUCT for _, cs in subs for c in cs}
assert placed == mapped, (placed ^ mapped)

TEXT_ONLY = len(sys.argv) > 3 and sys.argv[3] == "text"
choices = {}
cp = os.path.join(ROOT, "logos", "choices.json")
if os.path.exists(cp) and not TEXT_ONLY:
    choices = json.load(open(cp))

W, H = 26.0, 15.7
fig = plt.figure(figsize=(W, H), facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

ax.add_patch(Rectangle((0, H - 0.22), W, 0.22, color=PURPLE, lw=0))
ax.add_patch(Rectangle((0, H - 0.22), W * 0.3, 0.22, color=BLUE, lw=0))
ax.text(0.7, H - 1.0, "Greek Deep Tech Market Map", fontfamily=TF, fontsize=36, fontweight="bold", color=NAVY, va="center")
ax.text(0.7, H - 1.7, f"{len(mapped)} startups founded in Greece, or by Greeks with a Greek presence  |  pre-seed to late stage  |  October 2026",
        fontfamily=BF, fontsize=15, color=GREY, va="center")

PAD, GAP = 0.7, 0.6
colw = (W - 2 * PAD - 3 * GAP) / 4
CELL_COLS = 3
cellw = colw / CELL_COLS
cellh = 1.15
HEAD = 0.5
CAT = 0.55
top = H - 2.35


def draw_company(cx, cy, company):
    """Logo in the upper part of the cell and the plain name underneath."""
    name = SHORT.get(company, company)
    ch = choices.get(company)
    ly = cy + 0.17
    ny = cy - 0.4
    if ch:
        im = Image.open(os.path.join(ROOT, "logos", "prep", ch["file"])).convert("RGBA")
        iw, ih = im.size
        if ch.get("mode") == "icon":
            maxw, maxh = 0.62, 0.62
        else:
            maxw, maxh = cellw * 0.72, 0.5
        sc = min(maxw / iw, maxh / ih)
        tw, th = iw * sc, ih * sc
        if ch.get("dark_bg"):
            ax.add_patch(FancyBboxPatch((cx - tw / 2 - 0.1, ly - th / 2 - 0.08), tw + 0.2, th + 0.16,
                                        boxstyle="round,pad=0,rounding_size=0.05", fc=NAVY, ec="none", zorder=2))
        ax.imshow(im, extent=(cx - tw / 2, cx + tw / 2, ly - th / 2, ly + th / 2), zorder=3, aspect="auto")
        ax.text(cx, ny, name, fontfamily=BF, fontsize=11, color=NAVY, ha="center", va="center", zorder=3)
    else:
        ax.text(cx, cy - 0.02, name, fontfamily=BF, fontsize=13, fontweight="bold", color=NAVY, ha="center", va="center", zorder=3)


def box_height(n):
    return HEAD + ((n + CELL_COLS - 1) // CELL_COLS) * cellh + 0.1


for ci, cats in enumerate(COLUMNS):
    x0 = PAD + ci * (colw + GAP)
    y = top
    for si in cats:
        cat, subs = STRUCT[si]
        ax.add_patch(Rectangle((x0, y - CAT), colw, CAT, color=NAVY, lw=0, zorder=2))
        ax.text(x0 + 0.2, y - CAT / 2, cat.upper(), fontfamily=TF, fontsize=13.5, fontweight="bold", color="white", va="center", zorder=3)
        y -= CAT + 0.12
        if not subs:
            hh = 1.2
            ax.add_patch(FancyBboxPatch((x0, y - hh), colw, hh, boxstyle="round,pad=0,rounding_size=0.06", fc="white", ec=PURPLE, lw=1.3, ls=(0, (4, 3))))
            ax.text(x0 + colw / 2, y - hh / 2, "No verified venture-backed Greek company found yet", fontfamily=BF,
                    fontsize=12, style="italic", color=PURPLE, ha="center", va="center")
            y -= hh + 0.3
            continue
        for sub, cos in subs:
            bh = box_height(len(cos))
            ax.add_patch(FancyBboxPatch((x0, y - bh), colw, bh, boxstyle="round,pad=0,rounding_size=0.06", fc="white", ec=LINE, lw=1.2, zorder=1))
            ax.text(x0 + 0.2, y - HEAD / 2 - 0.02, sub, fontfamily=BF, fontsize=12.5, fontweight="bold", color=PURPLE, va="center", zorder=3)
            ax.plot([x0 + 0.2, x0 + colw - 0.2], [y - HEAD, y - HEAD], color=LINE, lw=1, zorder=2)
            for i, c in enumerate(cos):
                r, col = divmod(i, CELL_COLS)
                n_row = min(CELL_COLS, len(cos) - r * CELL_COLS)
                off = (CELL_COLS - n_row) * cellw / 2
                cx = x0 + off + col * cellw + cellw / 2
                cy = y - HEAD - 0.05 - r * cellh - cellh / 2
                draw_company(cx, cy, c)
            y -= bh + 0.25
        y -= 0.12

foot = ("Sources and funding data are in the dataset.  Created by Gerald Velas." if TEXT_ONLY else
        "Logos are trademarks of their respective owners and are shown for identification only.  Sources and funding data are in the dataset.  Created by Gerald Velas.")
ax.text(PAD, 0.5, foot, fontfamily=BF, fontsize=10, color=GREY, va="center")

fig.savefig(OUT + ".png", dpi=200, facecolor=BG)
fig.savefig(OUT + ".pdf", facecolor=BG)
print("rendered", len(mapped), "companies;", len(choices), "logos")
