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
        self.ax.text(LM, 0.45, "Greek Deep Tech | Gerald Velas | dataset as of 2026-10-16", fontfamily=BF, fontsize=8, color=GREY)
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
    pg = Page(pdf, "Greek Deep Tech: Analysis", "What is crowded, what is missing, how it is funded, who is active. Based on the 63 mapped companies in the dataset.")
    pg.h("Read this first")
    pg.p("The dataset has 82 rows: 63 mapped (31 Include, 32 Borderline), 2 on Hold because nothing current could be found (PiDust, QUBITECH), and 17 excluded. "
         "Every number below comes from those rows or from the sources listed on page 3. The 63 companies were found by sweeping VC portfolios and news lists, "
         "so they are a sample of the ecosystem, not a census. Counts show where evidence was found, not market share.")
    pg.h("Shape of the map")
    gs = pg.fig.add_axes([0.24, 0.5, 0.26, 0.19])
    bar(gs, [("Robotics & Drones", 13), ("Health & Biotech", 13), ("AI & ML", 11), ("Space & Defense", 9),
             ("Energy & Climate", 7), ("Semiconductors", 5), ("Industrial & Mfg", 5), ("Quantum", 0)], PURPLE, "Companies by category")
    gs2 = pg.fig.add_axes([0.7, 0.5, 0.22, 0.19])
    bar(gs2, [("Pre-seed / seed", 29), ("Series A and later", 15), ("Stage not found", 14), ("Exited", 5)], BLUE, "Companies by stage")
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
    pg.p("Quantum: no verified venture-backed Greek company. PiDust (Patras, 2019) has only a 2020 source; QUBITECH is a single-source mention. Both are on Hold. Xatoms (AI and quantum chemistry, backed by Genesis Ventures) was checked and is a Toronto company with Slovak founders, so it is excluded. "
         "A vendor guide (Quantum Zeitgeist) says research bodies lead.", bullet="-", indent=0.2)
    pg.p("Space: only two Greek-headquartered space companies were found, Prisma Electronics (Alexandroupolis; company-reported revenue above EUR 10M, in talks with investment funds) and Attisat (Athens satellite antennas), and neither has disclosed venture funding. "
         "Demand exists: Greece announced a EUR 350M Hellas-Space 2.0 programme in August 2026, and Open Cosmos Aegean won a EUR 60M contract. "
         "But those flow to foreign-headquartered firms (Open Cosmos is UK-based; OroraTech, checked and excluded, is German).", bullet="-", indent=0.2)
    pg.p("Semiconductors and hardware: five names (Circuits Integrated Hellas, SolidWatts, Think Silicon, Navenio, Axelera AI). Circuits Integrated's round (Evercurious, 2026-09) rests on one aggregator and has no disclosed amount. "
         "Axelera AI, the largest round tied to the ecosystem (more than USD 250M, February 2026), is Borderline: its CTO and co-founder is Greek and it hires engineers remotely in Greece, but no Greek office was found and its CEO is Italian.", bullet="-", indent=0.2)
    pg.p("Energy and climate: seven names (WeatherXM, Better Origin, Centaur Analytics, PlugSecure, Pinepeak, ClearDrop, Neurohive); four are Genesis Ventures portfolio companies. Piq Energy, which appears in Marathon's 2026 round list, is San Francisco-based with no Greek link found, so it is not on the map.", bullet="-", indent=0.2)
    pg.p("The Series A bridge: of the 15 companies at Series A or later, only 3 list a Greek headquarters (WeatherXM, Delian Alliance Industries, DeepSea Technologies). "
         "At least 25 of the 63 mapped companies are headquartered outside Greece (for example Perceptual Robotics in the UK, TileDB in the US, Bota Systems in Switzerland). "
         "Greek capital seeds them; growth capital and headquarters tend to move abroad. HQ is unconfirmed for Causaly, Keragon and Achira AI.", bullet="-", indent=0.2)
    pg.h("Funding patterns")
    pg.p("Marathon Venture Capital data, reported by MoneyBuzz on 2026-10-11, counts USD 435M raised by Greek startups so far in 2026 across 38 rounds. "
         "Axelera AI's round is a large share of that (the article says about 57%). 25 rounds were seed (about USD 38M combined) and eight were Series A (about USD 50M combined).", bullet="-", indent=0.2)
    pg.p("Totals depend on the source. Athens Tech Circle counts about EUR 1.45B across 100 deals in 2025 including debt and grants; a vendor guide (Ellty) cites EUR 732M. "
         "Do not compare these without checking their scope.", bullet="-", indent=0.2)
    pg.p("In the dataset, most disclosed seed-stage rounds fall roughly between USD 1M and 8M (mixed currencies, approximate). "
         "Acumino's USD 11.7M seed (June 2026) is the high outlier; Robenso (EUR 500K) and Intelistyle (about EUR 534K, 2018) are at the low end. Series A rounds run from USD 7.7M (WeatherXM) to USD 22.5M (iCOMAT).", bullet="-", indent=0.2)
    pg.p("Public money matters: the EIB's EUR 20M debt to StiQ (excluded as foodtech), grants at Bitloops and Bioemtech, the NATO Innovation Fund as iCOMAT co-lead, "
         "and Evercurious VC, anchored by the Hellenic Development Bank of Investments.", bullet="-", indent=0.2)
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
    pg = Page(pdf, "Where I'd invest in 2027", "Thesis draft for Greek deep tech. An opinion built on the dataset, not a recommendation to buy anything.")
    pg.h("The view in one paragraph")
    pg.p("Greek seed funds are finding and backing technical teams; the thin part is the step after seed, and the demand side (defense, space, energy, health systems) is growing faster than local venture-backed supply. "
         "I would look for companies that sit where Greek capital, Greek engineering talent and a funded public or industrial buyer overlap, and that need a Series A rather than another seed.")
    pg.h("Three bets")
    pg.p("1. Physical AI and robot components (software and sensors, not whole robots).", size=10.2, gap=0.03)
    pg.p("Evidence: Acumino raised USD 11.7M seed (June 2026) and joined Google DeepMind's robotics accelerator; Progressive Robotics and Terra Robotics (laser weeding, about EUR 1.8M seed, Uni.Fund-led, 2025) in Thessaloniki, Bota Systems and Robenso are all seed stage; "
         "Gizelis Robotics is a local integrator with no external funding found. What would make it work: a Series A lead from outside Greece and an industrial pilot customer. Risk: most teams are one or two rounds old.", indent=0.2, size=9.3)
    pg.p("2. Dual-use and defense autonomy.", size=10.2, gap=0.03)
    pg.p("Evidence: Delian Alliance Industries (USD 14M Series A, July 2025, Air Street and Marathon); Mind The Hack (EUR 2.8M seed, Oct 2025); five drone makers with no disclosed venture round (EFA Group invests in two); EUR 350M Hellas-Space 2.0 as a sign of public demand. "
         "The opening is component and software suppliers to those drone makers, and a second Delian-type company. Risk: long procurement cycles (my assumption, not in the dataset).", indent=0.2, size=9.3)
    pg.p("3. Computational health and biotech tooling.", size=10.2, gap=0.03)
    pg.p("Evidence: Health & Biotech is level with Robotics as the largest box (13 names each): ORamaVR (USD 4.5M, Jan 2026), Intelligencia, Causaly, Brainomix, Anacalypsis (first Greek VC investment in homegrown drug discovery per Metavallon). "
         "New local capital (Kos, USD 123M, reported June 2026) should lift Series A options. Risk: wet-lab biotech is capital-heavy; I would favor software and instruments over therapeutics at this stage.", indent=0.2, size=9.3)
    pg.h("Where I would not rush")
    pg.p("Quantum: the dataset has no verified venture-backed Greek company. I would track university spinouts through Metavallon's Brain Gain fund and revisit, rather than force a thesis.", bullet="-", indent=0.2, size=9.3)
    pg.p("Pure application-layer AI: the AI box is full of seed-stage apps (Moveo.AI, Bitloops, Keragon). Differentiation is hard to see without product or revenue data this dataset does not hold.", bullet="-", indent=0.2, size=9.3)
    pg.h("What I would check next")
    for t in ["Confirm whether Axelera AI has any Greek team beyond its CTO and remote hires: if so, semiconductors is the strongest talent story; if not, the box stays thin.",
              "Find the Series A and B investors who actually follow Greek seed rounds (Air Street, Molten, 8VC appear) and map their criteria.",
              "Phase 2 tracker: hiring, funding news and GitHub activity for the 63 mapped names, starting with the robotics and defense groups."]:
        pg.p(t, bullet="-", indent=0.2, size=9.3)
    pg.footer(1, 1)
    pg.save()
print("done", TF, BF)
