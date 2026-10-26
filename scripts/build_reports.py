"""Render the analysis (3 pages) and the 2027 thesis (1 page) as PDFs."""
import sys, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle
from matplotlib import font_manager as fm

OUT = sys.argv[1]  # output directory

BG, PURPLE, BLUE, NAVY, GREY = "#faf8f3", "#7a5cc4", "#4aa3f0", "#273B7B", "#6b7089"

import os as _os
_fp = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "fonts", "RedHatMono-Regular.ttf")
if _os.path.exists(_fp):
    fm.fontManager.addfont(_fp)
    fm.fontManager.addfont(_fp.replace("Regular", "Bold"))

names = {f.name for f in fm.fontManager.ttflist}
TF = next((n for n in ("Red Hat Mono", "Consolas", "DejaVu Sans Mono") if n in names), "monospace")
BF = next((n for n in ("Segoe UI", "Arial", "DejaVu Sans") if n in names), "sans-serif")

W, H = 8.27, 11.69
LM, RM = 0.85, 0.85


class Page:
    def __init__(self, pdf, title, kicker):
        self.pdf = pdf
        self.fig = plt.figure(figsize=(W, H), facecolor=BG)
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, W); self.ax.set_ylim(0, H); self.ax.axis("off")
        self.ax.add_patch(Rectangle((0, H - 0.18), W, 0.18, color=PURPLE, lw=0))
        self.ax.add_patch(Rectangle((0, H - 0.18), W * 0.33, 0.18, color=BLUE, lw=0))
        self.ax.text(LM, H - 0.75, title, fontfamily=TF, fontsize=19, fontweight="bold", color=NAVY, va="center")
        self.ax.text(LM, H - 1.12, kicker, fontfamily=BF, fontsize=9.5, color=GREY, va="center")
        self.y = H - 1.6

    def h(self, text):
        self.y -= 0.12
        self.ax.text(LM, self.y, text, fontfamily=TF, fontsize=11.5, fontweight="bold", color=PURPLE, va="center")
        self.y -= 0.3

    def p(self, text, size=9.6, color=NAVY, indent=0.0, gap=0.1, bullet=None, width=None):
        cpl = width or int((W - LM - RM - indent) * 72 / (size * 0.5))
        lines = textwrap.wrap(text, cpl)
        if bullet:
            self.ax.text(LM + indent - 0.2, self.y, bullet, fontfamily=BF, fontsize=size, color=BLUE, va="top")
        for ln in lines:
            self.ax.text(LM + indent, self.y, ln, fontfamily=BF, fontsize=size, color=color, va="top")
            self.y -= size * 1.55 / 72
        self.y -= gap

    def footer(self, n, total):
        self.ax.text(LM, 0.45, "Greek Deep Tech | Gerald Velas | dataset as of October 2026", fontfamily=BF, fontsize=8, color=GREY)
        self.ax.text(W - RM, 0.45, f"{n}/{total}", fontfamily=BF, fontsize=8, color=GREY, ha="right")

    def save(self):
        self.pdf.savefig(self.fig, facecolor=BG)
        plt.close(self.fig)


def bar(ax, items, color, title):
    labels = [a for a, _ in items][::-1]
    vals = [b for _, b in items][::-1]
    ax.barh(labels, vals, color=color, height=0.62)
    for i, v in enumerate(vals):
        ax.text(v + 0.15, i, str(v), va="center", fontfamily=BF, fontsize=8.5, color=NAVY)
    ax.set_facecolor(BG)
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#c9ccd8")
    ax.tick_params(axis="y", labelsize=8.5, colors=NAVY, length=0)
    ax.set_xticks([])
    ax.set_xlim(0, max(vals) + 2)
    ax.set_title(title, loc="left", fontfamily=TF, fontsize=9.5, color=NAVY, fontweight="bold")
    for t in ax.get_yticklabels():
        t.set_fontfamily(BF)


# ---------------------------------------------------------------- analysis
with PdfPages(OUT + "/greek_deeptech_analysis.pdf") as pdf:
    TOTAL = 3
    pg = Page(pdf, "Greek Deep Tech: Analysis", "What is crowded, what is missing, how it is funded, who is active. Based on the 69 mapped companies in the dataset.")
    pg.h("Read this first")
    pg.p("The dataset has 88 rows: 69 mapped (36 Include, 33 Borderline), 2 on Hold because nothing current could be found (PiDust, QUBITECH), and 17 excluded. "
         "Every number below comes from those rows or from the sources listed on page 3. The 69 companies were found by sweeping VC portfolios, news lists and the ESA BIC Greece incubator, "
         "so they are a sample of the ecosystem, not a census. Counts show where evidence was found, not market share.")
    pg.h("Shape of the map")
    gs = pg.fig.add_axes([0.24, 0.5, 0.26, 0.19])
    bar(gs, [("Robotics & Drones", 13), ("Health & Biotech", 13), ("AI & ML", 11), ("Space & Defense", 11),
             ("Energy & Climate", 8), ("Semiconductors", 7), ("Industrial & Mfg", 5), ("Quantum", 1)], PURPLE, "Companies by category")
    gs2 = pg.fig.add_axes([0.7, 0.5, 0.22, 0.19])
    bar(gs2, [("Pre-seed / seed", 30), ("Series A and later", 16), ("No round found", 18), ("Exited", 5)], BLUE, "Companies by stage")
    pg.y = 0.48 * H - 0.0
    pg.p("Stage is read from the last round on record. Five exits sit on the map as context: Think Silicon (acquired by Applied Materials, 2020), "
         "MarineTraffic (Kpler, 2023), Augmenta (CNH Industrial, 2023, enterprise value USD 110M), Seervision (Q-SYS, announced 2023) and Code BGP (Cisco, undated).")
    pg.h("What is crowded")
    pg.p("Robotics & Drones (13 names) and Health & Biotech (13) are the most populated boxes, and both are mostly early. "
         "In robotics, 6 of 13 companies are seed stage (Acumino, Progressive Robotics, Velos Rotors, Robenso, Bota Systems, Terra Robotics), one is an exit (Augmenta) and five have no external round found (Gizelis, Altus LSA, SAS Technology, Aether Aeronautics, Ucandrone). "
         "Health is more varied (Intelligencia, Anodyne Nanotech, Brainomix and Causaly are Series A or later).", bullet="-", indent=0.2)
    pg.p("Defense and drones is where company count outruns venture capital. Altus LSA (Chania), SAS Technology (Athens), Aether Aeronautics (Chania), Ucandrone (Koropi) and Velos Rotors (Xylokastro) are all drone makers, "
         "yet only Velos Rotors (USD 2M seed, Marathon, 2023) has a disclosed venture round; EFA Group has made undisclosed strategic investments in Aether and Ucandrone. A Greek press study cited by To Vima counts nine defense and dual-use startups raising a combined EUR 19.21M.", bullet="-", indent=0.2)
    pg.p("AI is crowded with applications, not infrastructure. Moveo.AI, Bitloops, Keragon, Intryc, Pallma AI, Proxy Foods AI, Intelistyle and SquareDev are application-layer companies; "
         "TileDB / Tile.ai (data infrastructure, USD 34M Series B, 2023) is the one infrastructure name.", bullet="-", indent=0.2)
    pg.footer(1, TOTAL)
    pg.save()

    pg = Page(pdf, "Greek Deep Tech: Analysis", "Gaps and funding patterns")
    pg.h("What is missing")
    pg.p("Quantum: one company, QRBIT, a 2025 NTUA spin-off building photonic systems for satellite quantum communications, incubated at ESA BIC Greece with no venture round found. PiDust (Patras, 2019) has only a 2020 source and QUBITECH is a single-source mention; both are on Hold.", bullet="-", indent=0.2)
    pg.p("Space: three Greek-headquartered space companies are mapped, Prisma Electronics (revenue above EUR 10M, company-reported), Attisat (satellite antennas, since 1997) and EMTech Space (spacecraft simulators, prime contractor of the Hellenic Space Dawn CubeSat), and none has a disclosed venture round. ESA BIC Greece has incubated about 32 space startups, most still pre-funding. "
         "Demand exists: the EUR 350M Hellas-Space 2.0 programme (August 2026). "
         "The largest space rounds tied to Greece go to foreign-headquartered firms with Greek bases: Open Cosmos (UK) and OQ Technology (Luxembourg; EUR 25M EIB venture debt in 2026, Greek fund Phaistos co-led its Series A).", bullet="-", indent=0.2)
    pg.p("Semiconductors and hardware: seven names (Circuits Integrated Hellas, SolidWatts, Think Silicon, Navenio, Axelera AI, and two ESA BIC Greece incubatees, SolidKosmos and Trimsignal). Circuits Integrated's round (Evercurious, 2026-09) rests on one aggregator and has no disclosed amount. "
         "Axelera AI (more than USD 250M, February 2026) is Borderline: Greek co-founder and CTO, remote hires in Greece, no Greek office.", bullet="-", indent=0.2)
    pg.p("Energy and climate: eight names (WeatherXM, Better Origin, Centaur Analytics, PlugSecure, Pinepeak, ClearDrop, Neurohive, Solmeyea); four are Genesis Ventures portfolio companies and Solmeyea is mostly EU-grant funded. Piq Energy, which appears in Marathon's 2026 round list, is San Francisco-based with no Greek link found, so it is not on the map.", bullet="-", indent=0.2)
    pg.p("The Series A bridge: of the 16 companies at Series A or later, only 3 list a Greek headquarters (WeatherXM, Delian Alliance Industries, DeepSea Technologies). "
         "At least 26 of the 69 mapped companies are headquartered outside Greece (for example Perceptual Robotics in the UK, TileDB in the US, Bota Systems in Switzerland). "
         "Greek capital seeds them; growth capital and headquarters tend to move abroad. HQ is unconfirmed for Causaly, Keragon and Achira AI.", bullet="-", indent=0.2)
    pg.h("Funding patterns")
    pg.p("Marathon Venture Capital data, reported by MoneyBuzz on 2026-10-11, counts USD 435M raised by Greek startups so far in 2026 across 38 rounds. "
         "Axelera AI's round is a large share of that (the article says about 57%). 25 rounds were seed (about USD 38M combined) and eight were Series A (about USD 50M combined).", bullet="-", indent=0.2)
    pg.p("Totals depend on the source: Athens Tech Circle counts about EUR 1.45B across 100 deals in 2025 including debt and grants; a vendor guide (Ellty) cites EUR 732M.", bullet="-", indent=0.2)
    pg.p("In the dataset, most disclosed seed-stage rounds fall roughly between USD 1M and 8M (mixed currencies, approximate). "
         "Acumino's USD 11.7M seed (June 2026) is the high outlier; Robenso (EUR 500K) and Intelistyle (about EUR 534K, 2018) are at the low end. Series A rounds run from USD 7.7M (WeatherXM) to USD 22.5M (iCOMAT).", bullet="-", indent=0.2)
    pg.p("Public money matters: EIB debt (StiQ, OQ Technology), EU grants (Solmeyea, Bioemtech), the NATO Innovation Fund (iCOMAT) and HDBI-anchored Evercurious VC.", bullet="-", indent=0.2)
    pg.footer(2, TOTAL)
    pg.save()

    pg = Page(pdf, "Greek Deep Tech: Analysis", "Active investors, caveats and sources")
    pg.h("Most active investors in this dataset")
    rows = [("Marathon Venture Capital", "10", "Progressive Robotics, Velos Rotors, Augmenta, Delian, Hack The Box, Causaly, Bota Systems, Centaur, Code BGP, Pallma AI"),
            ("Big Pi Ventures", "7", "Acumino, TileDB, Intelligencia, ORamaVR, Anodyne Nanotech, Corsmed, Navenio"),
            ("Metavallon VC", "9", "Perceptual Robotics, Think Silicon, Anacalypsis, Better Origin, Bioemtech, Feel Therapeutics, Purposeful, Seervision, Intelistyle"),
            ("Genesis Ventures", "9", "Progressive Robotics, Feel Therapeutics, ClearDrop, Terra Robotics, Neurohive, PlugSecure, Pinepeak, Hoplon AI, Pleioflow"),
            ("Evercurious VC", "5", "SolidWatts, ORamaVR, Anodyne Nanotech, Circuits Integrated, Koios Care"),
            ("Uni.Fund (3), Eleven Ventures, Velocity Partners VC, Helidoni Group, EFA Group (2 each)", "2-3", "see dataset")]
    for a, n, c in rows:
        pg.ax.text(LM, pg.y, a, fontfamily=BF, fontsize=9.3, fontweight="bold", color=NAVY, va="top")
        pg.ax.text(W - RM - 0.15, pg.y, n, fontfamily=TF, fontsize=9.3, color=PURPLE, va="top", ha="right")
        pg.y -= 0.22
        pg.p(c, size=8.6, color=GREY, gap=0.0, width=100)
    pg.p("Caution: the sweep started from Marathon, Big Pi, Metavallon and Genesis portfolio pages, so those four are over-represented by construction. "
         "Athens Tech Circle's H1 2025 ranking (all sectors) puts Genesis Ventures first (7+ deals), then THETI (4), with Uni.fund, Evercurious VC, VentureFriends and SPOROS Platform at 3 each. "
         "Marathon says 27 funds took part in 2026's 38 rounds. Foreign leads appear at later stages: Air Street, Carlyle, 8VC and ICONIQ Growth.")
    pg.p("New fund capacity: Metavallon's EUR 5M Brain Gain fund (Jan 2026), Kos Biotechnology Partners' USD 123M life-sciences fund (June 2026, single source), "
         "Big Pi's EUR 130M growth fund first close, and Marathon's EUR 75M latest fund.")
    pg.h("Limits of this work")
    for t in ["2 rows are on Hold (PiDust, QUBITECH); 17 are excluded; some Greek links and amounts are still UNVERIFIED in the CSV. Aggregators were used for some rounds and are labelled.",
              "Funding currencies are kept as reported. Some figures and founding years differ between sources; the notes column records each conflict.",
              "EU-Startups and the Genesis portfolio were read in a browser. Sifted's 2022 deeptech list is paywalled and unreadable, and Tracxn and the full Big Pi and Marathon portfolio pages could not be read, so companies only on those lists may be missing."]:
        pg.p(t, bullet="-", indent=0.2, size=9.2)
    pg.h("Sources for aggregate figures")
    for t in ["moneybuzz.gr/greek-startups-funding-435-million-2026-axelera-ai (Marathon VC data, 2026-10-11)",
              "athenstechcircle.beehiiv.com/p/greek-startups-vcs-funding-report-from-jan-jun-2025-9 and .../the-greek-startup-ecosystem-in-2025-what-the-data-tells-us",
              "tovima.com/finance/greece-emerges-as-a-hub-for-defense-and-cybersecurity-startups",
              "advanced-television.com/2026/08/03/greece-invests-e350m-in-new-space-programme",
              "tech.eu/2026/01/22/metavallon-vc-launches-eur5m-brain-gain-fund-to-reverse-greeces-tech-talent-exodus",
              "biocentury.com/article/659803 (Kos fund); company-level sources are in the CSV source_link column"]:
        pg.p(t, size=8.2, color=GREY, gap=0.04, width=108)
    pg.footer(3, TOTAL)
    pg.save()

# ---------------------------------------------------------------- thesis
with PdfPages(OUT + "/greek_deeptech_thesis_2027.pdf") as pdf:
    pg = Page(pdf, "Where I'd invest in 2027", "My view after mapping 69 Greek deep tech startups. This is my own opinion and not investment advice.")
    pg.h("My view in short")
    pg.p(size=9.3, text="I spent the last few weeks building a map of Greek deep tech startups and one thing kept coming up. Greek seed funds are good at finding technical teams early, "
         "but very few of these companies raise a Series A while staying based in Greece. Out of the 16 companies on my map that reached Series A or later, only 3 have their headquarters here. "
         "At the same time the state and the EU are putting real money into defense, space and energy. So in 2027 I would look for teams that already have a Greek seed round, "
         "a paying public or industrial customer, and a good reason to keep growing in Greece.")
    pg.h("Where I would put money")
    pg.p("1. Robot software and sensors", size=10.2, gap=0.03)
    pg.p("Acumino raised $11.7M at seed in June 2026 and was picked for Google DeepMind's first European robotics accelerator. Progressive Robotics and Terra Robotics in Thessaloniki, "
         "Bota Systems and Robenso are all still at seed. I prefer software and sensors over full robots because they need less money. "
         "What could go wrong: most of these teams are young and they will probably need a foreign investor to lead their Series A.", indent=0.2, size=9.0)
    pg.p("2. Defense and dual use autonomy", size=10.2, gap=0.03)
    pg.p("Delian Alliance Industries raised a $14M Series A in July 2025 with Air Street and Marathon, and Mind The Hack raised €2.8M in October 2025. "
         "My map has at least five Greek drone makers with no disclosed venture round, and EFA Group has already invested in two of them. "
         "I would look at the companies that supply parts and software to these drone makers. "
         "What could go wrong: selling to governments takes a long time.", indent=0.2, size=9.0)
    pg.p("3. Health and biotech software", size=10.2, gap=0.03)
    pg.p("Health and biotech is one of the two biggest groups on my map with 13 companies, like ORamaVR ($4.5M in January 2026), Intelligencia, Causaly and Brainomix. "
         "Kos Biotechnology Partners reached $123M for its first life sciences fund (reported in June 2026). "
         "I would choose software and medical devices over new drugs, because developing a drug needs much more money than Greek funds can give.", indent=0.2, size=9.0)
    pg.h("Where I would wait")
    pg.p("Quantum. I found only one company, QRBIT, a 2025 spinout from NTUA, and no venture round yet. For now I would follow the university spinouts and the ESA BIC Greece incubator.", bullet="•", indent=0.2, size=9.0)
    pg.p("Space. Greece is spending €350M on its Hellas Space 2.0 program, but the biggest space deals so far went to foreign companies with Greek offices, like Open Cosmos and OQ Technology. "
         "I would wait for Greek teams like EMTech Space to raise real rounds first.", bullet="•", indent=0.2, size=9.0)
    pg.p("Simple AI apps. There are a lot of seed stage AI apps and without revenue numbers it is hard to tell which ones will last.", bullet="•", indent=0.2, size=9.0)
    pg.h("What I want to check next")
    for t in ["Whether Axelera AI has a real team in Greece beyond its Greek cofounder and CTO.",
              "Which foreign investors keep leading Greek Series A rounds (Air Street, Molten and 8VC show up in my data).",
              "Phase 2: a tracker for hiring, funding news and GitHub activity across these 69 companies."]:
        pg.p(t, bullet="•", indent=0.2, size=9.0)
    pg.footer(1, 1)
    pg.save()
print("done", TF, BF)
