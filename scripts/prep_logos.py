"""Convert every downloaded candidate file to a trimmed PNG and build a contact sheet for review.

Run (no -I, needs matplotlib/Pillow):  python scripts/prep_logos.py
Outputs: logos/prep/<slug>__<file>.png and logos/contact_<n>.png
"""
import glob, io, os, sys
import pymupdf
from PIL import Image, ImageChops
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW, PREP = os.path.join(ROOT, "logos", "raw"), os.path.join(ROOT, "logos", "prep")
os.makedirs(PREP, exist_ok=True)


def load(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".svg":
        doc = pymupdf.open(path)
        pg = doc[0]
        z = 800 / max(pg.rect.width, 1)
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), alpha=True)
        return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGBA")
    return Image.open(path).convert("RGBA")


def trim(im):
    bg = Image.new("RGBA", im.size, (0, 0, 0, 0))
    bbox = im.getchannel("A").getbbox()
    if bbox is None:
        return im
    # also trim near-white borders on opaque images
    a = im.getchannel("A")
    if a.getextrema()[0] == 255:
        white = Image.new("RGBA", im.size, (255, 255, 255, 255))
        diff = ImageChops.difference(im.convert("RGB"), white.convert("RGB")).convert("L").point(lambda v: 255 if v > 18 else 0)
        b2 = diff.getbbox()
        if b2:
            bbox = b2
    return im.crop(bbox)


items = []
for d in sorted(glob.glob(os.path.join(RAW, "*"))):
    slug = os.path.basename(d)
    for f in sorted(glob.glob(os.path.join(d, "*"))):
        try:
            im = trim(load(f))
            if im.width < 8 or im.height < 8:
                continue
            out = os.path.join(PREP, f"{slug}__{os.path.splitext(os.path.basename(f))[0]}.png")
            im.save(out)
            items.append((slug, os.path.basename(f), out, im.size))
        except Exception as e:
            print("skip", f, type(e).__name__)

per = 30
for n in range(0, len(items), per):
    chunk = items[n:n + per]
    fig, axes = plt.subplots(6, 5, figsize=(15, 11), facecolor="#dcdce6")
    for ax in axes.ravel():
        ax.axis("off")
    for ax, (slug, fn, out, size) in zip(axes.ravel(), chunk):
        ax.imshow(Image.open(out))
        ax.set_title(f"{slug} / {fn} {size[0]}x{size[1]}", fontsize=7)
    fig.savefig(os.path.join(ROOT, "logos", f"contact_{n // per + 1}.png"), dpi=70)
    plt.close(fig)
print(len(items), "images")
