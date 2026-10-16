"""Re-fetch every source link in the dataset and test whether the company name, funding amount
and lead investor appear in the page text. Writes data/verification_report.csv.
Run: python -I scripts/verify_sources.py   (needs network; takes several minutes)
"""
import csv, re, sys, urllib.request, html
from concurrent.futures import ThreadPoolExecutor

CSV_IN = "data/greek_deeptech_dataset.csv"
CSV_OUT = "data/verification_report.csv"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept-Language": "en,el;q=0.8"}
cache = {}


def fetch(url):
    if url in cache:
        return cache[url]
    txt = None
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=12)
        data = r.read(3_000_000)
        txt = html.unescape(re.sub(r"<[^>]+>", " ", data.decode("utf-8", "ignore"))).lower()
        txt = re.sub(r"\s+", " ", txt)
    except Exception:
        txt = None
    cache[url] = txt
    return txt


def aliases(name):
    parts = re.split(r"[()/]", name)
    out = []
    for p in parts:
        p = p.strip().lower().replace("rebranded", "").strip()
        if len(p) >= 3:
            out.append(p)
            out.append(p.replace(" ", ""))
            if " " in p:
                out.append(p.split()[0])
    return [a for a in dict.fromkeys(out) if len(a) >= 4]


def amounts(s):
    if not s or re.search(r"not found|unverified|not disclosed|undisclosed|none", s, re.I):
        return []
    nums = re.findall(r"(\d+(?:[.,]\d+)?)\s*(?:m\b|k\b|million|b\b)?", s.lower())
    keep = []
    for n in nums:
        n = n.replace(",", ".")
        if n in ("2025", "2026", "2024", "2023", "2022", "2021", "2020", "2019", "2018"):
            continue
        keep.append(n)
    return keep[:3]


def lead(inv):
    if not inv or re.search(r"none|unverified|not found", inv, re.I):
        return None
    first = re.split(r"[;(]", inv)[0].strip().lower()
    first = re.sub(r"\b(lead|co-lead|acquirer:?)\b", "", first).strip(" :,")
    return first if len(first) >= 4 else None


def check(row):
    urls = [u.strip() for u in row["source_link"].split("|") if u.strip().startswith("http")]
    texts = [(u, fetch(u)) for u in urls]
    ok = [(u, t) for u, t in texts if t]
    al = aliases(row["company"])
    am = amounts(row["last_round_amount"])
    ld = lead(row["investors"])
    name_hit = [u for u, t in ok if any(a in t for a in al)]
    amt_hit = [u for u, t in ok if any(re.search(r"(?<![\d.])" + re.escape(a) + r"(?![\d])", t) for a in am)] if am else []
    inv_hit = [u for u, t in ok if ld and ld in t]
    if not urls:
        status = "NO SOURCE"
    elif not ok:
        status = "UNREADABLE"
    elif not name_hit:
        status = "NAME NOT FOUND"
    elif am and not amt_hit:
        status = "AMOUNT NOT CONFIRMED"
    else:
        status = "CONFIRMED"
    return {"company_id": row["company_id"], "company": row["company"], "map_status": row["map_status"], "check": status,
            "urls": len(urls), "readable": len(ok), "name_hit": len(name_hit), "amount_checked": "|".join(am),
            "amount_hit": len(amt_hit), "lead_checked": ld or "", "lead_hit": len(inv_hit),
            "claimed_amount": row["last_round_amount"], "claimed_date": row["last_round_date"]}


rows = list(csv.DictReader(open(CSV_IN, encoding="utf-8-sig")))
# prefetch all URLs in parallel
allurls = sorted({u.strip() for r in rows for u in r["source_link"].split("|") if u.strip().startswith("http")})
print(len(allurls), "urls", file=sys.stderr)
with ThreadPoolExecutor(max_workers=16) as ex:
    list(ex.map(fetch, allurls))
res = [check(r) for r in rows]
with open(CSV_OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
    w.writeheader()
    w.writerows(res)
from collections import Counter
print(Counter(r["check"] for r in res))
print("readable urls:", sum(1 for t in cache.values() if t), "of", len(cache))
