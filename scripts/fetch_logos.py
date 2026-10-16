"""Find official sites and download candidate logo files into logos/raw/<slug>/.

Files are saved as data only; nothing downloaded is executed. A manifest is written to logos/manifest.json
so every logo's source URL is on record. Run:  python -I scripts/fetch_logos.py
"""
import json, os, re, sys, urllib.request, urllib.parse
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW = os.path.join(ROOT, "logos", "raw")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
MAX_BYTES = 1_500_000

# company -> (slug, name keyword to confirm page, candidate domains)
C = {
 "Acumino": ("acumino", "acumino", ["acumino.ai", "acumino.com"]),
 "Perceptual Robotics": ("perceptual-robotics", "perceptual", ["perceptual-robotics.com", "perceptualrobotics.com"]),
 "Progressive Robotics": ("progressive-robotics", "progressive", ["progressiverobotics.com", "progressive-robotics.com", "progressiverobotics.eu"]),
 "Velos Rotors": ("velos-rotors", "velos", ["velosrotors.com"]),
 "Robenso": ("robenso", "robenso", ["robenso.gr"]),
 "Augmenta": ("augmenta", "augmenta", ["augmenta.ag", "augmenta-ag.com"]),
 "Gizelis Robotics": ("gizelis-robotics", "gizelis", ["grobotics.eu"]),
 "Altus LSA": ("altus-lsa", "altus", ["altus-lsa.gr", "altuslsa.com"]),
 "SAS Technology": ("sas-technology", "sas", ["sas-tech.gr"]),
 "Aether Aeronautics": ("aether-aeronautics", "aether", ["aether-aero.com", "aetheraeronautics.com", "aether-aeronautics.com"]),
 "Ucandrone": ("ucandrone", "ucandrone", ["ucandrone.com", "ucandrone.gr"]),
 "Bota Systems": ("bota-systems", "bota", ["botasys.com"]),
 "Moveo.AI": ("moveo-ai", "moveo", ["moveo.ai"]),
 "Bitloops": ("bitloops", "bitloops", ["bitloops.com", "bitloops.ai"]),
 "Satori Analytics": ("satori-analytics", "satori", ["satorianalytics.com"]),
 "Keragon": ("keragon", "keragon", ["keragon.com"]),
 "TileDB (rebranded Tile.ai)": ("tiledb", "tile", ["tile.ai", "tiledb.com"]),
 "Proxy Foods AI": ("proxy-foods", "proxy", ["proxyfoods.ai", "proxyfoods.com"]),
 "Intryc": ("intryc", "intryc", ["intryc.com"]),
 "Pallma AI": ("pallma", "pallma", ["pallma.ai"]),
 "Axelera AI": ("axelera", "axelera", ["axelera.ai"]),
 "Think Silicon": ("think-silicon", "think", ["think-silicon.com"]),
 "SolidWatts": ("solidwatts", "solidwatts", ["solidwatts.com", "solidwatts.ch"]),
 "Circuits Integrated Hellas": ("circuits-integrated", "circuits", ["circuits-integrated.com", "circuitsintegrated.com"]),
 "Navenio": ("navenio", "navenio", ["navenio.com"]),
 "WeatherXM": ("weatherxm", "weatherxm", ["weatherxm.com"]),
 "Better Origin": ("better-origin", "better origin", ["betterorigin.com", "betterorigin.co"]),
 "Centaur Analytics": ("centaur-analytics", "centaur", ["centaur.ag", "centaur-analytics.com"]),
 "Intelligencia": ("intelligencia", "intelligencia", ["intelligencia.ai"]),
 "ORamaVR": ("oramavr", "orama", ["oramavr.com"]),
 "Anodyne Nanotech": ("anodyne-nanotech", "hero", ["theheropatch.com"]),
 "Anacalypsis Therapeutics": ("anacalypsis", "anacalypsis", ["anacalypsis.com", "anacalypsistherapeutics.com"]),
 "Corsmed": ("corsmed", "corsmed", ["corsmed.com"]),
 "Bioemtech": ("bioemtech", "bioemtech", ["bioemtech.com"]),
 "Feel Therapeutics": ("feel-therapeutics", "feel", ["feeltherapeutics.com"]),
 "Brainomix": ("brainomix", "brainomix", ["brainomix.com"]),
 "Achira AI": ("achira", "achira", ["achira.ai"]),
 "Causaly": ("causaly", "causaly", ["causaly.com"]),
 "Purposeful": ("purposeful", "purposeful", ["purposeful.ai", "purposeful.gr", "purposeful.bio"]),
 "Delian Alliance Industries": ("delian", "delian", ["delianalliance.com", "delian.io", "delian-alliance.com"]),
 "Hack The Box": ("hack-the-box", "hack", ["hackthebox.com"]),
 "Sotiria Technology": ("sotiria", "sotiria", ["sotiria-tech.com", "sotiriatechnology.com", "sotiria.gr"]),
 "Prisma Electronics": ("prisma-electronics", "prisma", ["prisma-electronics.gr", "prismael.com"]),
 "Open Cosmos (Open Cosmos Aegean)": ("open-cosmos", "open cosmos", ["open-cosmos.com"]),
 "DeepSea Technologies": ("deepsea", "deepsea", ["deepsea.ai"]),
 "Code BGP": ("code-bgp", "code", ["codebgp.com"]),
 "iCOMAT": ("icomat", "icomat", ["icomat.co.uk", "icomat.com"]),
 "MarineTraffic": ("marinetraffic", "marinetraffic", ["marinetraffic.com"]),
 "Core Innovation and Technology": ("core-innovation", "core", ["core-innovation.gr", "coreinnovation.gr", "core-innovation.eu"]),
 "Terra Robotics": ("terra-robotics", "terra", ["terra-robotics.com", "terrarobotics.gr", "terra-robotics.gr"]),
 "Neurohive": ("neurohive", "neurohive", ["neurohive.eu", "neurohive.gr", "neurohive.io", "neurohive.com"]),
 "PlugSecure": ("plugsecure", "plugsecure", ["plugsecure.com", "plugsecure.io", "plugsecure.eu"]),
 "Pinepeak": ("pinepeak", "pinepeak", ["pinepeak.co", "pinepeak.io", "pinepeak.com", "pinepeak.earth"]),
 "Mind The Hack": ("mind-the-hack", "mind", ["mindthehack.com", "mindthehack.io", "mindthehack.eu"]),
 "Hoplon AI": ("hoplon-ai", "hoplon", ["hoplon.ai", "hoplonai.com"]),
 "Satways": ("satways", "satways", ["satways.net", "satways.com"]),
 "Attisat": ("attisat", "attisat", ["attisat.gr", "attisat.com"]),
 "Seervision": ("seervision", "seervision", ["seervision.com"]),
 "Intelistyle": ("intelistyle", "intelistyle", ["intelistyle.com"]),
 "Pleioflow": ("pleioflow", "pleioflow", ["pleioflow.com"]),
 "ClearDrop": ("cleardrop", "cleardrop", ["cleardrop.tech", "cleardrop.eu", "cleardrop.io", "cleardrop.gr", "cleardrop.com"]),
 "Velos Rotors": ("velos-rotors", "velos", ["velosrotors.com", "velos-rotors.com", "velosrotors.gr"]),
 "Think Silicon": ("think-silicon", "think", ["think-silicon.com"]),
 "Better Origin": ("better-origin", "better origin", ["betterorigin.com"]),
 "Delian Alliance Industries": ("delian", "delian", ["delianalliance.com", "delian-alliance.com", "delian.io", "delian.ai", "delianai.com"]),
}


def get(url, maxb=MAX_BYTES, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read(maxb + 1)
        if len(data) > maxb:
            raise ValueError("too large")
        return r.geturl(), r.headers.get("Content-Type", ""), data


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs, self.icons, self.title, self._t = [], [], "", False

    def handle_starttag(self, tag, a):
        a = {k: (v or "") for k, v in a}
        if tag == "title":
            self._t = True
        if tag == "img":
            blob = " ".join([a.get("class", ""), a.get("id", ""), a.get("alt", ""), a.get("src", ""), a.get("data-src", "")]).lower()
            src = a.get("src") or a.get("data-src") or ""
            if "logo" in blob and src and not src.startswith("data:"):
                self.imgs.append(src)
        if tag == "link" and "icon" in a.get("rel", "").lower() and a.get("href"):
            self.icons.append((a.get("rel", ""), a.get("sizes", ""), a["href"]))
        if tag == "meta" and a.get("property") == "og:image" and a.get("content"):
            self.icons.append(("og", "", a["content"]))

    def handle_endtag(self, tag):
        if tag == "title":
            self._t = False

    def handle_data(self, d):
        if self._t:
            self.title += d


def ext_of(url, ctype):
    path = urllib.parse.urlparse(url).path.lower()
    for e in (".svg", ".png", ".webp", ".jpg", ".jpeg", ".ico", ".gif"):
        if path.endswith(e):
            return e
    if "svg" in ctype: return ".svg"
    if "png" in ctype: return ".png"
    if "webp" in ctype: return ".webp"
    if "jpeg" in ctype: return ".jpg"
    return ".bin"


manifest = {}
only = set(sys.argv[1:])
for name, (slug, kw, domains) in C.items():
    if only and name not in only and slug not in only:
        continue
    found = None
    for d in domains:
        for pre in ("https://", "https://www."):
            try:
                final, ct, html = get(pre + d + "/", maxb=8_000_000)
                text = html.decode("utf-8", "ignore")
                if kw in text.lower():
                    found = (final, text)
                    break
            except Exception:
                continue
        if found:
            break
    if not found:
        manifest[name] = {"status": "site not found", "tried": domains}
        print("NO SITE ", name)
        continue
    final, text = found
    p = P()
    try:
        p.feed(text)
    except Exception:
        pass
    cands = [("logo-img", urllib.parse.urljoin(final, s)) for s in p.imgs[:4]]
    icons = sorted(p.icons, key=lambda t: (("apple" not in t[0]), ("svg" not in t[2]), t[0] == "og"))
    cands += [("icon:" + r, urllib.parse.urljoin(final, h)) for r, _, h in icons[:3]]
    out = os.path.join(RAW, slug)
    os.makedirs(out, exist_ok=True)
    saved = []
    for i, (kind, u) in enumerate(cands):
        try:
            _, ct, data = get(u)
            if len(data) < 200 or b"<html" in data[:300].lower():
                continue
            fn = f"{i}_{kind.split(':')[0]}{ext_of(u, ct)}"
            open(os.path.join(out, fn), "wb").write(data)
            saved.append({"file": fn, "url": u, "kind": kind, "bytes": len(data), "type": ct})
        except Exception:
            continue
    manifest[name] = {"status": "ok" if saved else "no logo file", "site": final, "files": saved}
    print("OK " if saved else "NOLOGO ", name, final, len(saved))

mp = os.path.join(ROOT, "logos", "manifest.json")
old = json.load(open(mp)) if os.path.exists(mp) else {}
old.update(manifest)
json.dump(old, open(mp, "w"), indent=1)
