import csv, sys

U = "UNVERIFIED"
NF = "Not found"
COLS = ["company_id", "company", "category", "sub_sector", "what_they_do", "founded",
        "hq_greek_link", "stage", "last_round_amount", "last_round_date", "investors",
        "website", "source_link", "map_status", "verification_status", "notes",
        "last_verified", "github_org", "linkedin_url"]

R = []
def add(name, cat, sub, what, founded, hq, stage, amt, date, inv, site, src, status, ver, notes):
    R.append(dict(company=name, category=cat, sub_sector=sub, what_they_do=what, founded=founded,
                  hq_greek_link=hq, stage=stage, last_round_amount=amt, last_round_date=date,
                  investors=inv, website=site, source_link=src, map_status=status,
                  verification_status=ver, notes=notes, last_verified="2026-10-16",
                  github_org="", linkedin_url=""))

# ---------------- Robotics & Drones ----------------
add("Perceptual Robotics", "Robotics & Drones", "Inspection drones",
    "Autonomous drone inspection and analytics for wind turbines", "2016",
    "HQ Bristol UK; European base in Athens", "Growth round (label disputed)",
    "~GBP 4M (~USD 5.3M)", "2026-07",
    "Investing for Purpose; Loggerhead Ventures; One Planet Capital (+Innovate UK support). Earlier: TSP Ventures, Brookstreet Equity, Deeptech Labs, Metavallon VC",
    U, "https://www.bristol.ac.uk/news/2026/july/perceptual-robotics-secures-millions-to-expand-wind-turbine-technology.html | https://www.mishcon.com/news/client-spotlight-perceptual-robotics-limited | https://raising.fi/news/perceptual-robotics-undisclosed-july-2026",
    "Include", "Verified (round label conflict)",
    "Marathon VC data cites USD 5.4M Series A; no source found for that figure. Series A GBP 3.6M was 2023 per Mishcon. Founded date per therecursive/UKBAA coverage.")
add("Acumino", "Robotics & Drones", "Physical AI / robot intelligence",
    "General robotic intelligence platform letting connected robots do dexterous tasks in unstructured environments", U,
    "Described as Greek robotics startup; exact HQ not confirmed", "Seed", "USD 11.7M", "2026-06-24",
    "Reports conflict on lead (Metaplanet vs Radar Ventures). Named: Big Pi Ventures, Schaeffler, MegaChips, LDV Partners, Air Street Capital, LocalGlobe, BTG Ventures",
    U, "https://bigpi.vc/ | https://www.orrick.com/fr-FR/News/2026/07/Acumino-Raises-11-7-Million-Seed-Round-and-Joins-Google-DeepMinds-European-Robotics-Accelerator | https://letsdatascience.com/news/acumino-raises-117m-seed-to-scale-robotics-deployments-c63b06a0",
    "Include", "Round verified; lead investor and HQ UNVERIFIED",
    "Sole Greek participant in Google DeepMind European robotics accelerator per one source. Total raised reported as USD 19.2M in a founder post (single source).")
add("Progressive Robotics", "Robotics & Drones", "Industrial robot software",
    "No-code AI software to program and reconfigure industrial robots (palletising focus)", "2023",
    "Thessaloniki, Greece", "Seed", "EUR 1.55M", "2025-01",
    "Marathon Venture Capital; Genesis Ventures",
    U, "https://finder.techleap.nl/news/feed/progressive-robotics-raises-1-55m-seed-funding | https://www.vcbacked.co/company/progressive-robotics",
    "Include", "Verified", "Amount reported as EUR 1.55M-1.6M across sources; one item mentions EUR 2M total.")
add("Velos Rotors", "Robotics & Drones", "Unmanned helicopters",
    "Electric unmanned helicopter UAVs (Velos V3, V-Twin) for survey, cargo and defense", U,
    "Xylokastro, Greece (described as US company with Greek roots)", "Seed", "USD 2M", "2023-04",
    "Marathon Venture Capital", U,
    "https://tech.eu/2023/04/06/velos-rotors-snags-2-million-to-help-drone-helicopter-production-take-off | https://registry.elevategreece.gov.gr/company/velos-rotors",
    "Include", "Verified", "No later round found.")
add("Robenso", "Robotics & Drones", "Recycling robotics",
    "Robotics and machine learning for sorting recyclable waste", "2021",
    "Heraklion, Crete", "Seed", "EUR 500K", "UNVERIFIED (reported in Athens Tech Circle newsletter)",
    "Helidoni Group", U,
    "https://athenstechcircle.beehiiv.com/p/big-moves-in-startup-funding-500k-for-robenso-hdb-s-new-loan-fund-more | https://www.vcbacked.co/company/robenso",
    "Include", "Verified round; date and website UNVERIFIED", "Founding year from one profile only.")
add("Augmenta", "Robotics & Drones", "Agri-robotics / precision ag",
    "Retrofit computer-vision system that adjusts fertilizer and spray rates per field area", U,
    "Athens, Greece (also Austin, Texas); Greek and US offices kept after acquisition", "Exited (acquired by CNH Industrial)", "Acquisition, enterprise value USD 110M", "2023-03",
    "Acquirer: CNH Industrial (held ~10.5% before deal). Earlier investors: Hardware Club, Marathon Venture Capital (USD 2.5M seed, 2019)",
    U, "https://tech.eu/2023/03/13/cnh-industrial-acquires-augmenta-for-110-million/ | https://agfundernews.com/precision-ag-startup-augmenta-raises-2-5m-from-hardware-club-and-marathon-venture-capital",
    "Include", "Verified", "Shown as exit context. Marathon was a shareholder; its proceeds are not disclosed in sources found.")
add("Gizelis Robotics", "Robotics & Drones", "Industrial robot integration",
    "Industrial robot integrator: welding, palletizing and handling cells", "2018",
    "Schimatari, Greece", "Corporate-backed (parent group); no external round found", NF, NF,
    "No external investors found (Dealroom: none known; Elevate registry stage label conflicts)",
    "https://grobotics.eu/", "https://registry.elevategreece.gov.gr/company/gizelis-robotics-sa | https://www.cbinsights.com/company/gizelis-robotics",
    "Borderline", "Existence verified; funding NOT FOUND",
    "Integrator rather than product startup. ELPEN gave a startup prize per Greek press. Third-party revenue estimates ignored.")
add("Altus LSA", "Robotics & Drones", "Defense UAVs",
    "UAV maker (ATLAS and EDOMON surveillance and reconnaissance systems)", "2011",
    "Chania, Greece", "Established SME", NF, NF, "None found", U,
    "https://www.newgreektv.com/news-in-english-for-greeks/greece/item/39098-drones-made-in-greece-which-greek-companies-are-building-the-next-generation-of-the-defense-industry",
    "Borderline", "Existence verified; funding NOT FOUND", "Mature company, included as ecosystem context.")
add("SAS Technology", "Robotics & Drones", "Heavy multirotor UAVs",
    "Heavy multirotor UAVs (EMPUSA, SARISA), moving toward armed versions", U,
    U, "UNVERIFIED", NF, NF, "None found", U,
    "https://www.newgreektv.com/news-in-english-for-greeks/greece/item/39098-drones-made-in-greece-which-greek-companies-are-building-the-next-generation-of-the-defense-industry",
    "Hold", "Single source; location UNVERIFIED", "Need second source and Greek link confirmation.")
add("Aether Aeronautics", "Robotics & Drones", "Target drones",
    "Target drones used to train air defense systems", U, U, "UNVERIFIED", NF, NF, "None found", U,
    "https://www.newgreektv.com/news-in-english-for-greeks/greece/item/39098-drones-made-in-greece-which-greek-companies-are-building-the-next-generation-of-the-defense-industry",
    "Hold", "Single source; location UNVERIFIED", "Need second source and Greek link confirmation.")
add("Ucandrone", "Robotics & Drones", "UAS (mapping, surveillance, defense)",
    "UAS for mapping, surveillance and defense (AQUILA, MERA, BLACKBIRD); part of EFA Group", U,
    U, "Group subsidiary", NF, NF, "Parent: EFA Group", U,
    "https://www.newgreektv.com/news-in-english-for-greeks/greece/item/39098-drones-made-in-greece-which-greek-companies-are-building-the-next-generation-of-the-defense-industry",
    "Hold", "Single source; location UNVERIFIED", "EFA Group capital increase (EUR 80M, Motor Oil/IREON Ventures, EOS Capital Partners) seen only in a LinkedIn snippet; verify before use.")

# ---------------- AI & Machine Learning ----------------
add("Moveo.AI", "AI & Machine Learning", "Conversational AI (enterprise)",
    "Enterprise customer-experience AI agents built on proprietary LLMs", "2020",
    "Operates from USA, Greece and Brazil", "Seed", "USD 2.6M (EUR 2.3M)", "2024-08",
    "Eleven Ventures (lead); Uni.Fund; Charge.vc; earlier pre-seed investors",
    "https://moveo.ai/", "https://moveo.ai/blog-new/moveo-ai-secures-2-6m-in-new-funding | https://vestbee.com/insights/articles/moveo-ai-raises-2-3-m",
    "Include", "Verified", "Performance claims vs GPT-4 are company claims. No later round found.")
add("Bitloops", "AI & Machine Learning", "Developer tools",
    "AI tool that turns Figma designs into frontend code", "2021 or 2024 (sources conflict)",
    "Athens and Nicosia", "Pre-seed", "EUR 1M (USD 1.2M)", "2025-06",
    "Eleven Ventures (lead); Corallia Ventures; angels",
    U, "https://vestbee.com/insights/articles/bitloops-raises-1-m | https://finder.techleap.nl/news/feed/bitloops-secures-1-2m-pre-seed-funding",
    "Include", "Verified round; founding year conflict", "Earlier EUR 165K and ~EUR 55K grant reported by EU-Startups/The Recursive.")
add("Satori Analytics", "AI & Machine Learning", "Data and AI services",
    "Data and AI engineering firm (~125 engineers per Motor Oil announcement)", "2014",
    "Athens (London office)", "Strategic minority investment", "UNVERIFIED (Marathon VC data cites USD 5.9M Series A)", "2026",
    "Motor Oil Group (strategic minority stake)", U,
    "https://moneybuzz.gr/greek-startups-funding-435-million-2026-axelera-ai/ | https://gr.linkedin.com/in/marios-parthenios",
    "Borderline", "Existence verified; amount and round label UNVERIFIED",
    "Services-led; deep tech status debatable. Motor Oil release does not state amount.")
add("Keragon", "AI & Machine Learning", "Healthcare workflow automation",
    "AI-powered healthcare automation platform connecting 300+ tools and EHRs", U,
    "Described as Greek-founded by Vestbee only", "Seed", "USD 7.5M", "2025-02",
    "Upfront Ventures (lead); Afore Capital; Focal; 25m Health. Earlier USD 3M pre-seed",
    "https://keragon.com/", "https://keragon.com/blog/keragon-ai-powered-healthcare-automation-platform-secured-7-5m-seed-round | https://vestbee.com/blog/articles/keragon-raises-7-5-m",
    "Include", "Round verified; Greek link single-sourced",
    "Traction numbers are company-reported. Confirm Greek team/office before final publication.")
add("TileDB (rebranded Tile.ai)", "AI & Machine Learning", "Data infrastructure",
    "Multi-dimensional array and scientific data management engine", "2017",
    "HQ Cambridge MA; Greek-founded (Stavros Papadopoulos), Athens office", "Series B", "USD 34M (one source says USD 36M)", "2023-10",
    "AlleyCorp; Lockheed Martin; Intel Capital; Big Pi Ventures (reported); Amgen; Nexus Venture Partners; Verizon (participants vary by source). Strategic investment announced 2026-09-16",
    U, "https://therecursive.com/?p=32254 | https://bigpi.vc/",
    "Include", "Verified (investor list and amount vary)", "Rebrand to Tile.ai announced by Big Pi Ventures Sept 2026; strategic investment amount not stated.")
add("Proxy Foods AI", "AI & Machine Learning", "AI for food R&D",
    "AI platform for food and beverage recipe formulation and R&D", U,
    "HQ Washington DC; labs/offices in Greece; Greek-educated CEO Panos Kostopoulos", "Seed", "USD 6M", "2026-08",
    "Ted Leonsis (lead); Robert G. Hisaoka; SWaN & Legend Venture Partners",
    U, "https://pulse2.com/proxy-foods-ai-raises-6-million-seed-round-to-expand-ai-native-food-rd-platform/amp/ | https://www.endeavor.org.gr/entrepreneurs/panos-kostopoulos",
    "Borderline", "Round verified; Greek presence partly verified", "Earlier USD 2.3M seed in 2024.")
add("Intryc", "AI & Machine Learning", "Customer support AI",
    "AI customer support quality and automation tool (YC S24)", U,
    "Greek-founded per search summary; details UNVERIFIED", "Seed", "USD 3.1M", "2025-01",
    "General Catalyst (lead); Sequoia scouts; Episode 1; 500 Emerging Europe",
    U, "https://seedtable.com/companies/intryc/funding-rounds/seed-2025-01",
    "Hold", "Round verified; Greek link UNVERIFIED", "Need founder nationality/team location source.")
add("StiQ", "AI & Machine Learning", "AI-run cloud kitchens",
    "AI-powered cloud kitchen and food platform", U, "Greece", "Debt/quasi-equity", "EUR 35M total (EUR 20M EIB venture debt)", "2025-07",
    "European Investment Bank (EUR 20M); international family offices", U,
    "https://www.eib.org/en/press/all/2025-301-eib-supports-greek-foodtech-innovator-stiq-with-eur20-million-under-investeu-to-scale-up-ai-powered-cloud-kitchen-platform",
    "Exclude", "Verified", "Foodtech operator, not deep tech. Kept for funding-pattern analysis only.")

# ---------------- Semiconductors & Hardware ----------------
add("Axelera AI", "Semiconductors & Hardware", "AI accelerators",
    "AI inference chips and accelerator platform", "2021",
    "HQ Eindhoven, Netherlands", "Late stage", "More than USD 250M", "2026-02",
    "Innovation Industries (lead); BlackRock; Samsung Catalyst Fund (per MoneyBuzz article). Earlier Series B ~EUR 63.5M incl. Invest-NL",
    U, "https://moneybuzz.gr/greek-startups-funding-435-million-2026-axelera-ai/ | https://ioplus.nl/archive/en/selected/dutch-ai-semiconductor-start-up-axelera-ai-launches-with-a-12-million-seed-round/",
    "Hold", "Funding verified; GREEK LINK UNVERIFIED",
    "Counted as Greek-linked in Marathon VC ecosystem data, but no source found naming Greek founders or a Greek office. Resolve before including on the map as context.")
add("Think Silicon", "Semiconductors & Hardware", "Low-power GPU IP",
    "Ultra-low-power GPUs and display controllers for wearables and IoT", U,
    "Patras, Greece", "Exited (acquired by Applied Materials)", "Acquisition (terms undisclosed in sources)", "2020-05",
    "Metavallon VC (investor)", U,
    "https://thehellenicinitiative.org/thi-news/the-hellenic-initiatives-annual-venture-fair-winner-think-silicon-acquired-by-applied-materials/",
    "Include", "Verified", "Shown as exit context; described as the largest deep tech exit in Greece (Metavallon).")
add("SolidWatts", "Semiconductors & Hardware", "Solid-state RF heating",
    "Solid-state RF generators to electrify industrial heating", "2022",
    "HQ Pully, Switzerland; SolidWatts Hellas in Greece", "Seed", "~USD 1.8M (EUR 2.0M per tech.eu)", "2026-03",
    "Evercurious VC (lead); Kickfund; Uni.Fund; Axel Carbon Capital; others. Pre-seed EUR 850K Jan 2025",
    U, "https://raising.fi/news/solidwatts-undisclosed-march-2026 | https://funding.tech.eu/companies/E78CCAFC-97C1-4BD7-A917-A6AC4DB58914",
    "Borderline", "Round verified; Greek presence thin", "Greek link is a Greek subsidiary and Greek investors; totals vary by source.")

# ---------------- Energy & Climate Tech ----------------
add("WeatherXM", "Energy & Climate Tech", "Climate data hardware",
    "Decentralized weather station network with crypto-enabled hardware", "2021",
    "Athens, Greece", "Series A", "USD 7.7M", "2024-05",
    "Lightspeed Faction (lead); Protocol Labs; Borderless Capital; Placeholder VC; Metaplanet; Arca; others",
    U, "https://greekcitytimes.com/2024/05/23/greek-founded-weatherxm-secures-7-7m-series-a-funding-to-expand-decentralized-weather-network/ | https://www.theblock.co/post/295807/lightspeed-faction-leads-7-7-million-series-a-round-for-depin-weather-startup-weatherxm",
    "Include", "Verified", "Seed USD 5M June 2022. Founding year from Failory only.")

# ---------------- Health & Biotech ----------------
add("Intelligencia", "Health & Biotech", "AI drug development",
    "Machine-learning predictions of clinical trial success for drug developers", U,
    "HQ New York; Athens and Basel offices; Greek founders", "Series A", "EUR 10.2M (USD 12M)", "2021-08",
    "MTIP (lead); Big Pi Ventures; Synetro Group; ZS",
    U, "https://www.businesswire.com/news/home/20210810005501/en/Intelligencia-Raises-%2412M-to-Reduce-the-Risk-of-Clinical-Research-Improve-RD-Productivity-and-Accelerate-Scientific-Breakthroughs | https://www.mobihealthnews.com/news/emea/greek-ai-startup-intelligencia-scores-eu102m-series-round",
    "Include", "Verified (2021 data, later rounds UNVERIFIED)", "Check for post-2021 rounds before publishing.")
add("ORamaVR", "Health & Biotech", "Medical XR training",
    "XR and AI training software for medical device makers and surgical robots", U,
    "Geneva with office in Crete, Greece", "Late seed", "USD 4.5M", "2026-01-30",
    "Big Pi Ventures (lead); Evercurious VC (lead); Sofmedica Ventures; Lars Rasmussen; FORTH-ICS; Starttech Ventures",
    U, "https://athenstechcircle.beehiiv.com/p/oramavr-secures-4-5m-late-seed-funding | https://ggba.swiss/en/geneva-based-oramavr-raises-usd-4-5-million-to-scale-medical-xr-training-solutions/",
    "Include", "Verified", "Prior USD 4M seed Jan 2025 per CB Insights (single source). HQ described variously.")
add("Anodyne Nanotech", "Health & Biotech", "Drug delivery",
    "Microneedle patch for transdermal delivery of biologics", U,
    "Boston-based; Athens link per one source; Greek investors", "Series A", "USD 12.6M", "2026-06-24",
    "Velocity Partners VC (lead); Evercurious VC; Relativity Healthcare Partners. Seed investors incl. Big Pi Ventures",
    U, "https://www.drugdeliverybusiness.com/?p=67513 | https://statnano.com/news/69081/Burns-Levinson-Closes-42-Million-Seed-Financing-for-Anodyne-Nanotech",
    "Borderline", "Round verified; Greek presence UNVERIFIED", "Greek link may be investor-only. Seed USD 4.2M April 2021.")
add("Anacalypsis Therapeutics", "Health & Biotech", "Neurodegeneration drug discovery",
    "Medications and biomarkers for neurodegenerative disease (Parkinson's focus)", U,
    "Pikermi, Greece", "Pre-seed", "~USD 344K", "2026-09 (UNVERIFIED)",
    "Metavallon VC", U,
    "https://www.vcbacked.co/company/anacalypsis-therapeutics | https://fundediq.co/anacalypsis-therapeutics-anacalypsistherapeutics-com-funding/",
    "Include", "Amount and date UNVERIFIED (aggregators only)", "Marathon VC data lists USD 300K seed; conflicting. Metavallon LinkedIn post claims first Greek VC investment in homegrown drug-discovery biotech.")
add("Caristo Diagnostics", "Health & Biotech", "AI cardiac diagnostics",
    "AI analysis of cardiac CT to detect coronary inflammation", U,
    "Oxford, UK; Greek link UNVERIFIED", "Series A", "GBP 13M (USD 16.3M)", "2023-04",
    "Oxford Science Enterprises (lead); BGF; Longwall Venture Partners", U,
    "https://www.biospace.com/caristo-diagnostics-completes-series-a-financing-and-welcomes-new-ceo-to-advance-ground-breaking-ai-technology-for-cardiac-disease-detection",
    "Hold", "Round verified; Greek link UNVERIFIED", "Do not include until a source confirms Greek founders or team.")
add("Koios Care", "Health & Biotech", "Digital neurology",
    "Smartphone/smartwatch data for Parkinson's monitoring (Parkiwatch)", "2022",
    "Antwerp, Belgium; Greek investors", "Seed", "EUR 1M", "2025-06",
    "Evercurious VC (lead); Astylab Ventures; imec.istart; HeBAN angels",
    U, "https://siliconcanals.com/koios-care-lands-e1m-in-funding/",
    "Hold", "Round verified; Greek link UNVERIFIED", "Founders' nationality not sourced.")

# ---------------- Space & Defense ----------------
add("Delian Alliance Industries", "Space & Defense", "Autonomous defense systems",
    "AI-enabled autonomous drones and surveillance towers for border and coastal defense", "2021",
    "Athens, Greece (formerly Lambda Automata)", "Series A", "USD 14M", "2025-07",
    "Air Street Capital and Marathon Venture Capital (co-leads); 201 Ventures; HCVC; Entropy Industrial Capital; Nebular",
    U, "https://tech.eu/2025/07/29/greek-defence-tech-startup-founded-by-apple-roboticist-raised-14m/ | https://startuprise.co.uk/greek-defence-tech-startup-delian-alliance-industries-secures-14-million-in-series-a-round/",
    "Include", "Verified", "Largest disclosed Greek defense-tech round found.")
add("Hack The Box", "Space & Defense", "Cybersecurity training",
    "Gamified cybersecurity training and simulation platform", "2017",
    "HQ UK (sources conflict); offices in Greece and US; Greek co-founder Haris Pylarinos", "Series B", "USD 55M (EUR 61.6M)", "2023-01",
    "Carlyle (lead); Paladin Capital Group; Osage University Partners; Marathon Venture Capital; Brighteye Ventures; Endeavor Catalyst",
    "https://www.hackthebox.com/", "https://www.hackthebox.com/blog/htb-series-b-funding | https://www.endeavor.org.gr/blog/hack-the-box-starts-the-year-off-strong-with-an-investment-round-of-usd55",
    "Borderline", "Verified", "Cybersecurity software; included under defense/security. Series A USD 10.6M led by Paladin (2021).")
add("Sotiria Technology", "Space & Defense", "Underwater intelligence",
    "Underwater intelligence systems combining AI, sensors and software (Nereid, Dioptre)", "2021",
    "Greece (city UNVERIFIED)", "Grant stage", "USD 100K grant (Failory)", "UNVERIFIED", "Grant funding", U,
    "https://www.failory.com/startups/greece | https://www.newgreektv.com/news-in-english-for-greeks/greece/item/39098-drones-made-in-greece-which-greek-companies-are-building-the-next-generation-of-the-defense-industry",
    "Include", "Existence verified; funding UNVERIFIED", "Grant figure from Failory only.")
add("Prisma Electronics", "Space & Defense", "Nanosatellites",
    "Designs and builds nanosatellites (MICE 1) for maritime data communication", U,
    "Alexandroupolis, Greece", "UNVERIFIED", NF, NF, "Works with Democritus University of Thrace", U,
    "https://greekreporter.com/2025/11/06/first-private-greek-nanosatellite-launched/ | https://www.cnn.gr/oikonomia/epixeiriseis/story/503706/i-prisma-electronics-stelnei-sto-diastima-nanodoryforo-kai-proselkyei-ependytes",
    "Include", "Existence verified; funding NOT FOUND", "CNN Greece headline says it attracts investors; details not retrieved.")
add("Open Cosmos (Open Cosmos Aegean)", "Space & Defense", "Satellite manufacturing",
    "Small-satellite manufacturer and data provider; Greek entity builds satellites near Athens", "2015",
    "HQ UK; Greek entity Open Cosmos Aegean", "Late stage", "EUR 300M", "2026-09",
    "Lightrock; ETF Partners; Institut Catala de Finances; Entrepreneurs First; pension funds",
    U, "https://tech.eu/2026/09/14/open-cosmos-secures-eur300m-to-expand-satellite-intelligence-and-connectivity/ | https://www.uktech.news/space-tech/open-cosmos-greece-esa-contract-20240529/",
    "Borderline", "Funding verified; Greek link is subsidiary and EUR 60M government contract", "Context only; not Greek-founded.")

# ---------------- Quantum & Advanced Computing ----------------
add("PiDust", "Quantum & Advanced Computing", "Quantum chemistry simulation",
    "Quantum computing hardware to simulate drugs, chemicals and materials", "2019",
    "Patras, Greece", "UNVERIFIED", NF, NF, U, U,
    "https://thequantuminsider.com/2020/07/25/greek-startup-utilizing-quantum-computing-hardware-to-simulate-drugs-chemicals-materials-and-other-quantum-systems/",
    "Hold", "2020 source only; current status UNVERIFIED", "Check whether still active.")
add("QUBITECH", "Quantum & Advanced Computing", "Quantum photonics and security",
    "Quantum photonics and security venture of UBITECH", U, "Greece (city UNVERIFIED)", "Corporate venture", NF, NF, "Parent: UBITECH", U,
    "https://quantumzeitgeist.com/greece-quantum-computing-companies/",
    "Hold", "Single source; UNVERIFIED", "Quantum category is thin; flagged as a finding in the analysis.")

# ---------------- Industrial & Manufacturing Tech ----------------
add("DeepSea Technologies", "Industrial & Manufacturing Tech", "Maritime AI",
    "AI tools to optimize vessel performance and cut fuel use and emissions", "2017",
    "Athens, Greece", "Growth (label varies by source)", "EUR 5M", "2021-07",
    "Nabtesco Technology Ventures (lead); The Signal Group; ETF Partners",
    "https://www.deepsea.ai/", "https://www.deepsea.ai/post/deepsea-technologies-secures-5-million-funding | https://thedigitalship.com/news/electronics-navigation/deepsea-technologies-secures-eur-5m-funding",
    "Include", "Verified (2021 data, later rounds UNVERIFIED)", "EUR 3M from ETF Partners in April 2020. Check for newer rounds.")


# ---------------- Second research pass ----------------
add("Corsmed", "Health & Biotech", "MRI simulation",
    "MRI simulation software and training tools", "2016 or 2019 (sources conflict)",
    "Stockholm; Greek link via Big Pi Ventures and Endeavor Greece Scale Up listing", "Seed", "~USD 3.5M (EUR 3.3M)", "2024-12",
    "Luminar Ventures and Big Pi Ventures (co-leads)", U,
    "https://vestbee.com/insights/articles/corsmed-raises-3-5-m | https://funding.tech.eu/companies/FBD96CAB-1946-4709-A1DD-C4C06BE3E8D1",
    "Borderline", "Round verified; Greek founders UNVERIFIED", "Co-founder Christos Xanthis has a Greek name; nationality not sourced.")
add("Better Origin", "Energy & Climate Tech", "Insect farming automation",
    "AI-driven insect mini-farms in containers turning food waste into feed", "2015 or 2019 (sources conflict)",
    "Cambridge, UK; Greek CEO and co-founder Fotis Fotiadis", "Series A", "USD 16M (EUR 14.6M)", "2022-04",
    "Balderton Capital (lead); Fly Ventures; Metavallon VC", U,
    "https://agfundernews.com/better-origin-banks-16m-series-a-for-its-ai-powered-insect-mini-farms | https://feednavigator.com/Article/2022/04/07/Better-Origin-raises-16m-to-expand-reach-of-its-AI-powered-mini-insect-farms",
    "Borderline", "Verified (2022 data, later rounds UNVERIFIED)", "No Greek office confirmed; Greek link is founder and investor.")
add("Bioemtech", "Health & Biotech", "Preclinical CRO",
    "Preclinical contract research and imaging services", U,
    "Greece (city UNVERIFIED)", "Pre-seed (follow-on)", "EUR 200K (2021) after EUR 400K (2019)", "2021",
    "Metavallon VC", U,
    "https://www.fi-compass.eu/sites/default/files/publications/Fireside%20chat%20Boosting%20investment%20into%20innovation.pdf",
    "Include", "Verified from company presentation (2024); newer rounds not found", "Also up to EUR 3M EU and national grants and a Seal of Excellence per the deck.")
add("Feel Therapeutics", "Health & Biotech", "Digital mental health",
    "Wearable and smartphone data for objective mental-health diagnosis and care", U,
    "HQ San Francisco; Greek founders; ~90% of workforce in Greece per Dealroom", "Seed / convertible notes", "USD 4M (May 2022)", "2022-05 (later notes through 2024)",
    "Metavallon VC; Genesis Ventures; Anthemis; Felicis; SOSV; Satori Neuro; SeedToB Capital",
    U, "https://greekanalyst.substack.com/p/reinventing-mental-health | https://www.cbinsights.com/company/feel-therapeutics/financials",
    "Include", "Verified; totals conflict (USD 7.5M vs 22.5M)", "Workforce share from Dealroom only. Founder names not retrieved.")
add("Brainomix", "Health & Biotech", "AI medical imaging",
    "AI imaging software for stroke and lung fibrosis (Brainomix 360)", U,
    "Oxford, UK spinout; Greek-founded per trade press; CEO Michalis Papadakis", "Series C", "GBP 14M (USD 18M), later extended to GBP 18.8M (USD 25.4M)", "2025-03",
    "UNVERIFIED (not captured in search results)", U,
    "https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15740447/brainomix-completes-18m-funding-round-plans-us-expansion | https://www.auntminnie.com/imaging-informatics/artificial-intelligence/news/15818048/brainomix-raises-series-c-financing-to-254m",
    "Borderline", "Round verified; investors and Greek office UNVERIFIED", "Fetch AuntMinnie pages for investor list.")
add("Achira AI", "Health & Biotech", "AI drug development",
    "AI-enabled drug development", U,
    "Described as Greek startup; HQ UNVERIFIED", "UNVERIFIED", "USD 33M", "2025-04",
    "Dimension; Nvidia; Amplify; Compound", U,
    "https://finder.techleap.nl/news/feed/achira-ai-secures-33m-in-funding",
    "Include", "Round verified; Greek link and stage UNVERIFIED", "Need primary announcement for stage and HQ.")
add("Causaly", "Health & Biotech", "Biomedical AI",
    "Biomedical evidence search and discovery platform for researchers", U,
    "Greek founder Ioannis Kiachopoulos; HQ UNVERIFIED", "Series B", "USD 60M (total USD 86M)", "2024-07 (UNVERIFIED day)",
    "ICONIQ Growth (lead); Index Ventures; Marathon Venture Capital; EBRD; Pentech", U,
    "https://www.powergame.gr/start-ups-digital/479740/causaly-ependysi-60-ekat-dolarion-apo-tin-iconiq-capital/ | https://www.businesswire.com/news/home/20240715471754/en",
    "Borderline", "Round verified; HQ and Greek presence UNVERIFIED", "Month inferred from Business Wire URL; confirm.")
add("Circuits Integrated Hellas", "Semiconductors & Hardware", "RF / mmWave ICs",
    "Analog, RF and mmWave IC design; CI-ONE chip for Ka-band flat-panel antennas", "2018",
    "Athens, Greece", "Pre-seed / seed", "Not disclosed", "2026-09-15 (UNVERIFIED, aggregator)",
    "Evercurious VC", U,
    "https://app.fundz.net/fundings/circuits-integrated-hellas-funding-round-seed-003f07 | https://athenstechcircle.beehiiv.com/p/evercurious-vc-launches-early-stage-deep-tech-fund-piney-raises-1-2m-for-expansion",
    "Include", "Single aggregator for round; no second source", "Product target: CI-ONE availability Q4 2026 (company claim).")
add("Bota Systems", "Robotics & Drones", "Robot sensors",
    "Force-torque sensors with built-in electronics and AI for robot arms", U,
    "Zurich; described as Greek-founded by one profile; co-founders Klajd Lika, Ilias Patsiaouras", "Seed", "USD 2.5M (EUR 2.4M)", "2023-10-02",
    "Marathon Venture Capital (lead); angels", U,
    "https://www.startupticker.ch/en/news/bota-systems-raises-2-5-million-in-seed-round | https://www.walderwyss.com/en/news/2023-10-03_bota-systems-ag-announces-the-completion-of-usd-2-5m-seed-round",
    "Borderline", "Round verified; Greek link single-sourced", "Earlier USD 0.2M seed (2020) and EUR 150K Venture Kick grant.")
add("Centaur Analytics", "Energy & Climate Tech", "AgTech IoT",
    "Post-harvest crop monitoring sensors and analytics", U,
    "Volos, Greece per Elevate Greece registry (also California)", "Seed", "USD 3M (earlier USD 1.3M in 2016)", "UNVERIFIED (2016 for first round)",
    "Marathon Venture Capital (lead); Detia Degesch; OurCrowd", U,
    "https://agfundernews.com/centaur-analytics-raises-3m-seed-round-for-post-harvest-crop-monitoring | https://registry.elevategreece.gov.gr/company/centaur-technologies-p-c",
    "Include", "Rounds verified; dates and later funding UNVERIFIED", "Registry lists USD 5M total (company-reported).")
add("Code BGP", "Industrial & Manufacturing Tech", "Network security software",
    "BGP routing management software; spin-off of ITE", U,
    "Greece", "Seed", "EUR 1.2M (New Money says USD 1.5M)", "UNVERIFIED",
    "Marathon Venture Capital", U,
    "https://www.cnn.gr/tech/story/271143/xrimatodotisi-1-2-ekat-eyro-gia-tin-code-bgp",
    "Borderline", "Round verified; date UNVERIFIED", "Software, deep tech status debatable.")
add("iCOMAT", "Industrial & Manufacturing Tech", "Advanced composites",
    "Rapid Tow Shearing fibre steering for lighter composite parts", "2019 (University of Bristol spinout)",
    "Bristol, UK; Greek-founded (CEO Evangelos Zympeloudis)", "Series A", "USD 22.5M (about GBP 17.6M)", "2024-06",
    "8VC (lead); NATO Innovation Fund (co-lead); Syensqo Ventures; Velocity Partners VC", U,
    "https://greekcitytimes.com/2024/06/06/greek-founded-icomat-secures-22-5m-series-a-funding-to-revolutionize-advanced-composite-manufacturing | https://www.setsquared.co.uk/icomat-raises-22-5m-to-automate-advanced-composite-manufacturing-for-sustainable-transport/",
    "Borderline", "Verified; Greek team presence UNVERIFIED", "Factory under construction in Gloucester, UK.")
add("MarineTraffic", "Industrial & Manufacturing Tech", "Maritime data",
    "Ship-tracking data and maritime analytics", "2007",
    "Athens, Greece", "Exited (acquired by Kpler)", "Undisclosed", "2023-03-07 (closing)",
    "Acquirer: Kpler", U,
    "https://www.kpler.com/blog/kpler-acquires-marinetraffic-and-fleetmon-for-maritime-sector-expansion | https://gcaptain.com/kpler-acquires-marinetraffic-and-fleetmon/",
    "Include", "Verified", "Exit context for maritime tech cluster.")
add("Core Innovation and Technology", "Industrial & Manufacturing Tech", "Industrial AI",
    "Machine learning for factory and warehouse operations", U,
    "Chalkis, Greece", "UNVERIFIED", NF, NF, "None found", U,
    "https://portal.effra.eu/organisation/8321 | https://sifted.eu/articles/greek-deeptech-startups-to-watch-according-to-investors",
    "Include", "Existence verified; funding NOT FOUND", "Sifted calls it one of the best-funded Greek deeptech startups (article about 2022); no round data found.")

# ---------------- Held after second pass ----------------
add("PolyModels Hub", "Health & Biotech", "Computational biology",
    "ModelFlow platform linking scientific data, physics-based and AI models", "2023",
    "London; Greek link is Marathon VC only", "Series A", "GBP 7M (EUR 7.8M per The Recursive)", "2025-11-20",
    "Molten Ventures (lead); Marathon Venture Capital", U,
    "https://tech.eu/2025/11/20/polymodels-hub-secures-ps7m-investment-led-by-molten-ventures-and-marathon-vc/",
    "Hold", "Round verified; Greek link UNVERIFIED", "Founders Antonio Benedetti, Harry Christodoulou, Antonio Yankey; nationality not sourced.")
add("NOFire AI", "AI & Machine Learning", "Infrastructure reliability",
    "AI incident resolution platform for engineering teams", U,
    "Greek link UNVERIFIED (Marathon-backed)", "Seed", "USD 2.5M (aggregator)", "2026-05-28",
    "Marathon Venture Capital; a16z Scout Fund; angels", U,
    "https://www.caplight.com/company/nofire",
    "Hold", "Aggregator only; not deep tech", "Founders Spiros Economakis, Panagiotis Moustafellos.")
add("Juisci", "AI & Machine Learning", "SaaS (business UNVERIFIED)",
    "Business UNVERIFIED; classified as SaaS by Seedtable", U,
    "Greek link UNVERIFIED (Big Pi II holding)", "Seed", "USD 6.5M (Seedtable)", "2025-09-19",
    "Big Pi Ventures (lead)", U,
    "https://www.cnn.gr/oikonomia/epixeiriseis/story/526571/big-pi-ventures-oi-epomenes-kiniseis-kai-to-stoixima-ton-ependyseon-se-scale-ups-etaireies",
    "Hold", "Single aggregator; business UNVERIFIED", "Not deep tech as described.")
add("Straion", "AI & Machine Learning", "Developer tools",
    "Developer tools (details UNVERIFIED)", U, "Greek link UNVERIFIED (Marathon-backed)", "Seed", "USD 1.3M (CB Insights)", "2026-02-23",
    "Marathon Venture Capital", U, "https://www.cbinsights.com/investor/marathon-venture-capital",
    "Hold", "Aggregator only", "Not deep tech as described.")
add("Pallma AI", "AI & Machine Learning", "UNVERIFIED",
    "Details UNVERIFIED", U, "Greek link UNVERIFIED (Marathon-backed)", "Pre-seed", "USD 1.6M (CB Insights)", "2026-01-28",
    "Marathon Venture Capital", U, "https://www.cbinsights.com/investor/marathon-venture-capital",
    "Hold", "Aggregator only", "Needs a primary source.")
add("ClearDrop", "Industrial & Manufacturing Tech", "Acoustic surface cleaning",
    "Vibration-based cleaning of optical surfaces (rain, dust, frost)", U,
    "Greek link UNVERIFIED; CEO Nikos Christopoulos", "UNVERIFIED", NF, NF, NF, U,
    "https://athenstechcircle.beehiiv.com/p/never-marry-your-ideas-or-assumptions-nikos-christopoulos-ceo-cleardrop",
    "Hold", "Funding NOT FOUND; Genesis Ventures backing UNVERIFIED", "Origins in a Lille research lab.")
add("Nutropy", "Health & Biotech", "Precision fermentation",
    "Animal-free casein via precision fermentation", U, "France; Big Pi co-led", "Seed", "EUR 7M", "2025-10",
    "Big Pi Ventures and Zero Carbon Capital (co-leads)", U,
    "https://vegconomist.com/?p=154460",
    "Exclude", "Verified; not Greek", "French company with a Greek lead investor. Keep for investor-activity analysis only.")
add("Purposeful", "Industrial & Manufacturing Tech", "UNVERIFIED",
    "Details UNVERIFIED", U, "Greek link UNVERIFIED", "Exited (acquired by PharOS per Greek press)", NF, NF, "Metavallon VC (investor)", U,
    "https://athenstechcircle.beehiiv.com/p/brain-gain-fund-by-metavallon-vc",
    "Hold", "Exit mentioned only", "Need company profile and acquisition details.")

# ---------------- Held for Greek-link or deep-tech check ----------------
add("Butler POS", "Industrial & Manufacturing Tech", "Restaurant POS software",
    "Cloud point-of-sale for restaurants with terminal hardware", U,
    "Greece, Cyprus, Ireland (availability)", "UNVERIFIED", NF, NF, NF, U,
    "https://www.capterra.co.uk/software/1097176/Butler-POS",
    "Exclude", "Funding NOT FOUND; not clearly deep tech", "On your known-company list. Only product listings found. Decide whether to keep as non-deep-tech context.")
add("Edra", "AI & Machine Learning", "Enterprise AI",
    "AI that turns operational data into living knowledge", "2024",
    "New York; Greek link UNVERIFIED", "Series A", "USD 30M", "2026-03-18",
    "Sequoia (lead); 8VC; HubSpot Ventures; A*", U,
    "https://www.wsgr.com/en/insights/wilson-sonsini-advises-edra-on-dollar30-million-series-a-financing.html",
    "Hold", "Round verified; Greek link UNVERIFIED", "Founders Eugen Alpeza and Yannis Karamanlakis; nationality not sourced. Do not assume.")
add("Astrato Analytics", "AI & Machine Learning", "Business intelligence",
    "Cloud-native BI platform", "2023", "London, UK; Greek link UNVERIFIED", "Seed", "USD 5M (GBP 3.7M)", "2025-04-29",
    "Big Pi Ventures (lead); Propelling Tech Ventures; 30+ angels", U,
    "https://businesscloud.co.uk/news/astrato-raises-3-7m-seed-round-after-5-fold-revenue-jump/",
    "Hold", "Round verified; Greek link UNVERIFIED", "Listed as Greek deeptech in a Greek funding report; founder Martin Mahler.")
add("Navenio", "Semiconductors & Hardware", "Indoor positioning",
    "Indoor positioning software using phone sensors", U, "UK; Greek link UNVERIFIED", "Series A", "GBP 9.5M (date UNVERIFIED)", U,
    "Oxford Science Enterprises (lead); Big Pi Ventures (participant)", U,
    "https://businesscloud.co.uk/news/indoor-gps-scaleup-navenio-navigates-to-9-5m/",
    "Hold", "Greek link UNVERIFIED", "Big Pi is an investor; need Greek founders/team source.")


# ---------------- Third research pass: resolutions of Hold rows ----------------
def upd(name, **kw):
    for r in R:
        if r["company"] == name:
            r.update(kw)
            return
    raise KeyError(name)

upd("Axelera AI", map_status="Borderline",
    hq_greek_link="HQ Eindhoven; Greek co-founder and CTO Evangelos Eleftheriou; remote engineering hires in Greece; no Athens office found",
    verification_status="Funding verified; Greek link partly verified (leadership, not an office)",
    source_link="https://moneybuzz.gr/greek-startups-funding-435-million-2026-axelera-ai/ | https://www.endeavor.org.gr/podcasts/evangelos-eleftheriou-axelera-ai-from-scientific-excellence-to-europes-most | https://www.newmoney.gr/roh/palmos-oikonomias/epixeiriseis/ellinikes-startups-pos-anevasan-tachitita-i-chrimatodotisis-pies-eteries-sikosan-ta-megalitera-posa-pics/amp/",
    notes="CEO Fabrizio Del Maffeo is Italian. Shown as late-stage context. Counted by Marathon VC as Greek-linked.")
upd("Intryc", map_status="Borderline",
    hq_greek_link="San Francisco-based; Greek co-founders Alex Marantelos (CEO) and Dimitrios Ilias (CTO) per profile pages",
    verification_status="Round verified; Greek link from profile pages only",
    source_link="https://seedtable.com/companies/intryc/funding-rounds/seed-2025-01 | https://yespress.io/alex-marantelos.md | https://www.panathenea.org/panathenea-2025/speakers/dimitrios-ilias/")
upd("Navenio", map_status="Borderline",
    hq_greek_link="Oxford, UK; co-founder and CTO Niki Trigoni is Greek (born in Chalcis); no Athens office found",
    founded="2015",
    verification_status="Greek founder verified; round date and investors UNVERIFIED",
    source_link="https://businesscloud.co.uk/news/indoor-gps-scaleup-navenio-navigates-to-9-5m/ | https://en.wikipedia.org/wiki/Niki_Trigoni | https://crunchbase.com/organization/navenio",
    notes="Funding totals conflict across sources (USD 6.3M to 40.9M); only the GBP 9.5M round is used.")
upd("SAS Technology", map_status="Borderline",
    hq_greek_link="Glyka Nera, Athens, Greece (member of Spirit World Group)",
    verification_status="Existence and location verified; funding NOT FOUND",
    source_link="https://sas-tech.gr/ | https://sas-tech.gr/dl/SAS_Brochure.pdf | https://greekreporter.com/2025/02/16/greek-drone-sarisa-rocket-combat-ready/",
    stage="Group-owned SME; no external round found", notes="SARISA II armed trials Feb 2025 (Litochoro range). Company site lists ESPA funding badge.")
upd("Aether Aeronautics", map_status="Borderline",
    hq_greek_link="Chania, Crete (Elevate Greece registry)",
    verification_status="Existence and location verified; funding NOT FOUND",
    source_link="https://registry.elevategreece.gov.gr/company/aether-aeronautics-pc | https://www.parapolitika.gr/zoi/article/1111770/stratigiki-sunergasia-tou-omilou-efa-group-me-tin-elliniki-aether-aeronautics-pc-gia-tin-anaptuxi-enaerion-stohon/app/",
    stage="No external round found", notes="NAMFI suitability certification reported for PNS-1 and NMS-2 targets (Greek-language report). EFA Group partnership.")
upd("Ucandrone", map_status="Borderline",
    hq_greek_link="Koropi, Attica; part of EFA Group",
    founded="2015 (sole proprietorship since 2009)",
    verification_status="Existence and location verified; funding NOT FOUND",
    source_link="https://registry.elevategreece.gov.gr/company/ucandrone-sa/ | https://www.euro2day.gr/en/article/2358851/efa-group-demonstration-of-advanced-defense-techno",
    stage="Group subsidiary; no external round found", notes="Took part in Trojan Horse 26 exercise (June 2026) per EFA-related posts.")
upd("Altus LSA", hq_greek_link="Chania, Crete",
    source_link="https://www.newgreektv.com/news-in-english-for-greeks/greece/item/39098-drones-made-in-greece-which-greek-companies-are-building-the-next-generation-of-the-defense-industry | https://registry.elevategreece.gov.gr/company/aether-aeronautics-pc")
upd("Pallma AI", map_status="Borderline", category="AI & Machine Learning", sub_sector="AI agent security",
    what_they_do="Security layer for autonomous enterprise AI agents (prompt injection, data leakage, unsupervised execution)",
    founded="2025", hq_greek_link="London; Greek-founded (Pavlos Mitsoulis, Dionysis Varelas); teams in London and Athens",
    stage="Pre-seed", last_round_amount="EUR 1.36M (USD 1.6M)", last_round_date="2026-02-02 (announcement)",
    investors="Marathon Venture Capital (lead); senior tech leaders from AWS, Meta, Google, Hack The Box, Workable",
    verification_status="Verified (aggregator figures vary: USD 1.58M to 2.0M)",
    source_link="https://theaiinsider.tech/2026/02/02/pallma-ai-raises-e1-36m-pre-seed-to-secure-autonomous-ai-agents-for-the-enterprise/ | https://finder.techleap.nl/news/feed/pallma-ai-raises-1-6m-to-secure-enterprise-ai-agents-from-threats-1",
    notes="Do not confuse with Palma.ai (separate company).")
upd("Purposeful", map_status="Borderline", category="Health & Biotech", sub_sector="AI drug repurposing",
    what_they_do="AI to find new uses for existing drugs, focused on rare diseases", founded="2018",
    hq_greek_link="Greece (Greek law firm advised the founders; city UNVERIFIED)",
    stage="Strategic investment (PharOS) with secondary purchase from Metavallon", last_round_amount=NF, last_round_date=U,
    investors="PharOS (strategic); Metavallon VC (sold shares)",
    verification_status="Deal verified; value and date NOT FOUND",
    source_link="https://www.zeya.com/news/zepos-yannopoulos-advised-purposeful-strategic-collaboration-pharos | https://ceelegalmatters.com/greece/23608-zepos-yannopoulos-advises-purposeful-on-pharos-partnership",
    notes="Not a full acquisition per sources, though Metavallon lists it among exits. Founders: George Drakakis, Charalampos Chomenidis, Georgia Tsiliki, Aristidis Dokoumetzidis.")
upd("Caristo Diagnostics", map_status="Exclude", verification_status="Round verified; Greek link NOT FOUND after targeted search",
    notes="Oxford spinout; sources give no Greek or Cypriot link for founders. Reopen only with a biographical source.")
upd("Edra", map_status="Exclude", verification_status="Round verified; Greek link NOT FOUND after targeted search",
    notes="Targeted search returned nothing on founders' nationality. Reopen only with a primary source.")
upd("Astrato Analytics", map_status="Exclude", verification_status="Round verified; Greek link NOT FOUND",
    hq_greek_link="London, UK; PitchBook lists it as formerly Vizlib",
    notes="Counted as Greek deeptech in a funding report, but no Greek office or founder found. Big Pi is an investor only.")
upd("Juisci", map_status="Exclude", hq_greek_link="Paris, France (Seedtable); Big Pi Ventures lead",
    last_round_amount="USD 6.5M (Seedtable) or USD 5.5M (F4 Fund)", sub_sector="SaaS",
    verification_status="Not Greek-headquartered; product not described in sources",
    source_link="https://seedtable.com/investors/big-pi-ventures/portfolio | https://f4.fund/firms/big-pi-ventures",
    notes="Kept for investor-activity analysis only.")
upd("Straion", map_status="Exclude", hq_greek_link="Linz, Austria; Marathon Venture Capital lead", founded=U,
    what_they_do="Rules and context layer for AI coding tools", stage="Seed", last_round_amount="EUR 1.1M (~USD 1.3M)",
    verification_status="Round verified; no Greek founders found",
    source_link="https://nordic9.com/news/straion-raised-11m-with-marathon-venture-capital/ | https://seedtable.com/companies/straion/funding-rounds/seed-2026-02",
    notes="Greek link is the lead investor only.")
upd("NOFire AI", verification_status="Round verified; HQ listed as New Jersey or Dover (US); Greek link UNVERIFIED",
    source_link="https://www.hipeac.net/news/7151/nofire-ai-raises-25-million-seed-funding-software-reliability-platform/ | https://www.caplight.com/company/nofire",
    notes="Team: Spiros Economakis (CEO), Panagiotis Moustafellos (CTO), Antonios Chalkiopoulos (COO), Anastassios Nanos (chief scientist). Nationality and Athens office not sourced. Stays on Hold.")
upd("PiDust", verification_status="2020 source only; searched again, no 2025-26 activity or funding found. Stays on Hold",
    notes="Founders: Vasilis Armaos (CEO), Dimitris Badounas, Paraskevas Deligiannis. Check G.E.MI. registry for current status.")
upd("QUBITECH", verification_status="Only a vendor guide names it; no products, funding or location found. Stays on Hold")
upd("PolyModels Hub", verification_status="Round verified; searches found no Greek founder or Athens link. Stays on Hold")
upd("Koios Care", verification_status="Round verified; searches found no founder nationality. Stays on Hold")
upd("ClearDrop", verification_status="Athens Tech Circle interview only; no funding, location or Greek link stated. Stays on Hold")


# ---------------- Websites confirmed by fetching the page (2026-10-16) ----------------
WEB = {
 "Acumino": "https://acumino.ai/", "Perceptual Robotics": "https://www.perceptual-robotics.com/",
 "Progressive Robotics": "https://progressive-robotics.com/", "Gizelis Robotics": "https://grobotics.eu/",
 "Altus LSA": "https://altus-lsa.com/", "SAS Technology": "https://sas-tech.gr/", "Ucandrone": "https://ucandrone.com/",
 "Aether Aeronautics": "https://www.aether-aero.com/", "Bota Systems": "https://botasys.com/", "Moveo.AI": "https://moveo.ai/",
 "Bitloops": "https://bitloops.com/", "Satori Analytics": "https://satorianalytics.com/", "Keragon": "https://www.keragon.com/",
 "TileDB (rebranded Tile.ai)": "https://www.tile.ai/", "Proxy Foods AI": "https://proxyfoods.ai/", "Intryc": "https://www.intryc.com/",
 "Pallma AI": "https://pallma.ai/ (redirects to vernolabs.ai)", "Axelera AI": "https://axelera.ai/", "SolidWatts": "https://www.solidwatts.ch/",
 "Circuits Integrated Hellas": "https://www.circuitsintegrated.com/", "Navenio": "https://navenio.com/", "WeatherXM": "https://weatherxm.com/",
 "Centaur Analytics": "https://centaur.ag/", "Intelligencia": "https://www.intelligencia.ai/", "ORamaVR": "https://oramavr.com/",
 "Anacalypsis Therapeutics": "https://anacalypsistherapeutics.com/", "Corsmed": "https://www.corsmed.com/", "Bioemtech": "https://bioemtech.com/",
 "Feel Therapeutics": "https://feeltherapeutics.com/", "Brainomix": "https://www.brainomix.com/", "Achira AI": "https://achira.ai/",
 "Causaly": "https://www.causaly.com/", "Hack The Box": "https://www.hackthebox.com/", "Sotiria Technology": "https://www.sotiria.gr/",
 "Prisma Electronics": "https://prismael.com/", "Open Cosmos (Open Cosmos Aegean)": "https://open-cosmos.com/", "DeepSea Technologies": "https://www.deepsea.ai/",
 "Code BGP": "https://www.codebgp.com/", "iCOMAT": "https://www.icomat.co.uk/", "MarineTraffic": "https://www.marinetraffic.com/",
 "Core Innovation and Technology": "https://www.core-innovation.com/ (UNVERIFIED: same entity as Greek Core Innovation and Technology OE)",
}
for _n, _w in WEB.items():
    for _r in R:
        if _r["company"] == _n and _r["website"] == U:
            _r["website"] = _w
upd("Pallma AI", notes="Do not confuse with Palma.ai. pallma.ai now redirects to Verno Labs, whose footer reads Pallma AI Ltd (rebrand not confirmed by a press source).")


# ---------------- Fourth research pass: completeness ----------------
# Corrections to existing rows
upd("Acumino", investors="Radar Ventures (lead, per company announcement); Schaeffler; Big Pi Ventures; MegaChips; LDV Partners; Bulent Celebi",
    verification_status="Round verified; lead = Radar Ventures per company post and Caplight; HQ UNVERIFIED",
    source_link="https://bigpi.vc/ | https://www.trysignalbase.com/news/funding/acumino-secures-117 | https://www.caplight.com/investor/radarventures | https://www.orrick.com/fr-FR/News/2026/07/Acumino-Raises-11-7-Million-Seed-Round-and-Joins-Google-DeepMinds-European-Robotics-Accelerator",
    notes="One outlet (Logicity) names Metaplanet as lead; it conflicts with the company post and is not used. One of 15 startups in Google DeepMind's first European robotics accelerator (Orrick).")
upd("Brainomix", investors="Parkwalk Advisors and Boehringer Ingelheim Venture Fund (co-leads); Hostplus via IP Group Hostplus Innovation Fund (new); LifeSci Capital supported",
    verification_status="Round and investors verified (company release 2025-03-18); Greek office UNVERIFIED",
    source_link="https://www.brainomix.com/news/brainomix-series-c/ | https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15740447/brainomix-completes-18m-funding-round-plans-us-expansion",
    notes="Series C extended to GBP 18.8M (USD 25.4M) per AuntMinnie. Greek-founded per trade press; CEO Michalis Papadakis.")
upd("Achira AI", stage="Seed", investors="Dimension (lead); Amplify Partners; Compound; NVentures (Nvidia)", last_round_date="2025-02 to 2025-04 (sources differ)",
    what_they_do="AI plus physics-based simulation (geometric deep learning, quantum chemistry) for drug discovery",
    hq_greek_link="HQ UNVERIFIED; Greek co-founder Theofanis Karaletsos (also John Chodera, CEO; Zavain Dar)",
    verification_status="Round verified; HQ and Greek presence UNVERIFIED",
    source_link="https://finder.techleap.nl/news/feed/achira-ai-secures-33m-in-funding | https://www.thenationalherald.com/greek-startup-achira-ai-gets-33-million-in-investor-funding/",
    notes="Round exceeded a USD 15M target. Dealroom dates it Feb 2025; press Apr 2025.")
upd("Prisma Electronics", stage="Profitable SME; in talks with investment funds", last_round_amount="No external round found (company-reported 2024 revenue above EUR 10M, 145+ staff)",
    investors="None found; CEO said talks with funds under way",
    verification_status="Existence verified; no external funding found",
    source_link="https://www.cnn.gr/oikonomia/epixeiriseis/story/503706/i-prisma-electronics-stelnei-sto-diastima-nanodoryforo-kai-proselkyei-ependytes | https://greekreporter.com/2025/11/06/first-private-greek-nanosatellite-launched/",
    notes="MICE-1 launch reported for Nov 2025 on Falcon 9; outcome not confirmed here. Revenue and headcount are company-reported via Greek press.")
upd("Sotiria Technology", stage="Seed (registry label); DIANA grant", last_round_amount="USD 100K grant (DIANA)", last_round_date="2023-11",
    investors="Angels (unnamed); DIANA (NATO innovation programme) grant", hq_greek_link="Athens, Greece (Elevate Greece registry)",
    verification_status="Existence and location verified; investors not named",
    source_link="https://registry.elevategreece.gov.gr/company/sotiria-technology | https://bouncewatch.com/company/sotiria-technology | https://www.powergame.gr/start-ups-digital/1350165/sotiria-technology-vazei-made-in-greece-lyseis-stin-ypothalassia-amyna-tis-evropis/",
    notes="Managing Director Angelos Tsereklas Zafeirakis. DIANA and MIT Innovators Under 35 claims come from speaker bios and are not independently verified.")
upd("Core Innovation and Technology", stage="Grant-funded R&D organisation (CORE Innovation Centre is a non-profit subsidiary)",
    last_round_amount="More than EUR 30M in grants (leader's statement, single source)", investors="Public and EU grants",
    hq_greek_link="Chalkida (Halkida), Greece", verification_status="Existence verified; funding figure UNVERIFIED",
    source_link="https://portal.effra.eu/organisation/12520 | https://cordis.europa.eu/project/id/101079180 | https://www.core-innovation.com/",
    notes="Site core-innovation.com describes itself as the first smart manufacturing hub in Greece; assumed to be the same group.")
upd("Aether Aeronautics", stage="Strategic investment (EFA Group)", investors="EFA Group (strategic partnership and investment; terms not disclosed)",
    last_round_amount="Not disclosed", last_round_date=U,
    source_link="https://www.parapolitika.gr/zoi/article/1111770/stratigiki-sunergasia-tou-omilou-efa-group-me-tin-elliniki-aether-aeronautics-pc-gia-tin-anaptuxi-enaerion-stohon/app/ | https://registry.elevategreece.gov.gr/company/aether-aeronautics-pc")
upd("Ucandrone", stage="Strategic investment (EFA Group)", investors="EFA Group (strategic partnership through investment; terms not disclosed)",
    last_round_amount="Not disclosed", last_round_date=U,
    source_link="https://registry.elevategreece.gov.gr/company/ucandrone-sa/ | https://www.euro2day.gr/en/article/2358851/efa-group-demonstration-of-advanced-defense-techno")
upd("Altus LSA", stage="Established SME; strategic partner Shield AI (2026)",
    notes="Signed a strategic agreement with Shield AI (2026) to integrate KMB Hunter and M3NTOR with V-BAT and Hivemind. No shareholder round found; robotics.press lists USD 880K (third-party card, not used).",
    source_link="https://www.naftemporiki.gr/english/2143605/greek-defence-firm-altus-lsa-us-shield-ai-sign-strategic-drone-partnership/ | https://registry.elevategreece.gov.gr/company/aether-aeronautics-pc")
upd("ClearDrop", map_status="Borderline", category="Energy & Climate Tech", sub_sector="Self-cleaning solar panels",
    what_they_do="Vibration-based technology that turns solar panels into self-cleaning devices (acoustic-wave cleaning from a Lille research lab)",
    hq_greek_link="Greek link: listed by Genesis Ventures (Greek fund) as Deeptech; CEO Nikos Christopoulos; HQ UNVERIFIED",
    investors="Genesis Ventures (portfolio listing; round not disclosed)",
    verification_status="Genesis portfolio listing verified; funding and HQ NOT FOUND",
    source_link="https://www.genesis-ventures.vc/our-portfolio | https://athenstechcircle.beehiiv.com/p/never-marry-your-ideas-or-assumptions-nikos-christopoulos-ceo-cleardrop")

# New companies from this pass
add("Terra Robotics", "Robotics & Drones", "Agri-robotics (laser weeding)",
    "TerraWeeder laser weeding robot for ultra-precise, soil-free organic weeding", U,
    "Thessaloniki, Greece (Elevate Greece registry)", "Seed", "~EUR 1.8M (USD 2.1M)", "2025-09 to 2025-10",
    "Uni.Fund (lead); Genesis Ventures; Helidoni Group; HeBAN; Argyris Kaninis. Earlier EUR 345K pre-seed (2024, Genesis)", U,
    "https://finder.techleap.nl/news/feed/terra-robotics-raises-2-1m-for-laser-weeding | https://www.fertilizerdaily.com/20251014-terra-robotics-raises-e1-8-million-to-bring-laser-weeding-technology-to-market/ | https://registry.elevategreece.gov.gr/company/terra-robotics-p-c",
    "Include", "Verified", "CEO Konstantinos Kandylas. Aggregators list USD 3.1M total seed; EUR 1.8M is the most consistent figure.")
add("Neurohive", "Energy & Climate Tech", "Agri-tech (livestock sensing)",
    "Wearable sensors, cloud and AI for monitoring sheep and goat herds", "2023",
    "Thessaloniki, Greece (PremierAlts listing)", "Pre-seed (inferred from total)", "USD 160K total (aggregator)", U,
    "Genesis Ventures (portfolio listing; round not disclosed)", U,
    "https://www.genesis-ventures.vc/our-portfolio | https://www.premieralts.com/companies/neurohive",
    "Include", "Genesis listing verified; amounts UNVERIFIED (aggregator)", "Selected for the Wageningen Hub per a LinkedIn post (not verified).")
add("PlugSecure", "Energy & Climate Tech", "Energy infrastructure cybersecurity",
    "Security-as-a-service for EV charging, solar, battery and wind infrastructure (OT security)", "2024",
    "Athens, Greece (Elevate Greece registry)", "Pre-seed", "EUR 720K (~USD 780K)", "2025-03 to 2025-04 (sources differ)",
    "Apeiron VC (lead); Genesis Ventures; Alexander Caravitis", U,
    "https://nordic9.com/news/plugsecure-in-a-720k-pre-seed-deal-led-by-apeiron-vc-joined-by-genesis-ventures/ | https://registry.elevategreece.gov.gr/company/plugsecure/ | https://www.eu-startups.com/2026/02/from-athens-to-thessaloniki-10-of-the-most-promising-greek-startups-to-keep-an-eye-on-in-2026/",
    "Include", "Verified; round date and label vary", "CEO Eleftherios Karabatsakis.")
add("Pinepeak", "Energy & Climate Tech", "Wildfire risk forecasting",
    "High-resolution wildfire probability forecasts down to individual homes (Cambridge and Imperial College research)", "2023-12",
    "UK-based; two founders are Greek per The Next Web; HQ UNVERIFIED", "Pre-seed (inferred)", "USD 580K total (aggregator)", U,
    "Genesis Ventures (portfolio listing; round not disclosed)", U,
    "https://thenextweb.com/news/pinepeak-wildfire-simulator-predicts-fire-risks | https://www.genesis-ventures.vc/our-portfolio | https://www.premieralts.com/companies/pinepeak",
    "Borderline", "Greek founders from one article; funding UNVERIFIED", "Genesis lists it as Deeptech.")
add("Mind The Hack", "Space & Defense", "Cybersecurity (automated pen-testing)",
    "Automated, attacker-driven security testing platform for enterprises", "2022 or 2023 (sources differ)",
    "Attica, Greece", "Seed", "EUR 2.8M", "2025-10-07",
    "Deep Capital Group (lead)", U,
    "https://startuprise.co.uk/greek-cybersecurity-startup-mind-the-hack-secures-e2-8m-funding/ | https://app.dealroom.co/news/feed/mindthehack-raises-2-8m-for-cybersecurity-innovation | https://www.eu-startups.com/2026/02/from-athens-to-thessaloniki-10-of-the-most-promising-greek-startups-to-keep-an-eye-on-in-2026/",
    "Include", "Verified", "Founders reported as Stavros Kirykos (CEO) and Giorgos Rakitzi (CTO); spellings vary. Aggregators list USD 3.3M to 4.5M.")
add("Hoplon AI", "Space & Defense", "Cybersecurity (AI agents)",
    "Autonomous AI agents acting as a virtual cybersecurity team for SMEs", U,
    "London-based; Greek co-founder Yannis Kostakis", "Seed", "USD 1M", "2026-01 to 2026-05 (sources differ)",
    "Haatch (lead per press); Genesis Ventures; angels", U,
    "https://athenstechcircle.beehiiv.com/p/plugsecure-secures-funding-to-protect-ev-charging-from-cyber-attacks-bdfd | https://www.vcbacked.co/company/hoplonai | https://www.caplight.com/company/hoplonai",
    "Borderline", "Round verified (aggregators); Greek team presence UNVERIFIED", "Caplight lists Genesis as co-lead; press says Haatch led.")
add("Satways", "Space & Defense", "Geospatial command and control",
    "Geospatial command-and-control software for public safety, civil protection and defense", "2006",
    "Athens, Greece (Neo Irakleio, Attica)", "Private SME", NF, NF, "None found", U,
    "https://www.datanyze.com/companies/satways/348633223 | https://www.netlaw.bg/en/a/satways-olokliromenes-lyseis-asfaleias-kai-amynas-idiotiki-epicheirisi-parochis-ypiresion-asfaleias-iepya-etaireia-periorismenis-efthynis-greece",
    "Borderline", "Existence and location verified; funding NOT FOUND", "Named as a Greek partner in the OroraTech wildfire contract. Established firm, shown for context.")
add("Attisat", "Space & Defense", "Satellite antennas",
    "Satellite antenna and communications equipment; ESA ARTES partner", U,
    "Athens, Greece", "Private SME", NF, NF, "None found", U,
    "https://artes.esa.int/contractors/attisat | https://esa.int/Applications/Connectivity_and_Secure_Communications/Invisible_satellite_dishes_to_preserve_Athens_skyline",
    "Borderline", "Existence verified; founding year and funding NOT FOUND", "Greek partner in the OroraTech wildfire contract per Tech.eu.")
add("Seervision", "AI & Machine Learning", "Computer vision (camera automation)",
    "AI-driven camera automation software (ETH Zurich spin-off)", U,
    "Zurich with offices in Athens; CEO Nikos Kariotoglou", "Exited (acquired by Q-SYS)", "Undisclosed", "2023-06",
    "Acquirer: Q-SYS (QSC). Metavallon VC listed as an investor by Tracxn", U,
    "https://www.businesswire.com/news/home/20230612005152/en | https://startupticker.ch/en/news/california-based-company-acquires-seervision",
    "Borderline", "Acquisition announced (closing not confirmed); Metavallon stake single-sourced", "19 staff per Startupticker at the time.")
add("Intelistyle", "AI & Machine Learning", "AI fashion styling",
    "AI-based outfit recommendation engine for fashion retailers", U,
    "London; Greek registry lists Maroussi, Athens entity", "Seed", "~EUR 534K (USD 600K)", "2018-11",
    "Metavallon VC (lead); Techstars Montreal AI Accelerator; Innovate UK; Plug and Play", U,
    "https://www.eu-startups.com/2018/11/intelistyle-raises-seed-round/ | https://registry.elevategreece.gov.gr/company/intelistyle-ltd",
    "Borderline", "Round verified (2018, stale); founders' nationality NOT FOUND", "Applied AI in retail; deep tech status debatable.")
add("Pleioflow", "Health & Biotech", "Cardiovascular medical devices",
    "Percutaneous flow-assist devices for cardiogenic shock and kidney protection", U,
    "UK with Greek subsidiary Pleioflow Hellas (Nea Kifissia)", "UNVERIFIED", "USD 1.74M (PitchBook, undated)", U,
    "Genesis Ventures (portfolio listing); Olympic Investments (PitchBook)", U,
    "https://www.genesis-ventures.vc/our-portfolio | https://registry.elevategreece.gov.gr/company/pleioflow-hellas-sa/ | https://pitchbook.com/profiles/company/538044-67",
    "Borderline", "Greek subsidiary verified; funding from an aggregator", "Registry figures (EUR 4.5M, USD 30M valuation) are self-reported and not used.")

# Newly checked and excluded or held
add("Krotos", "Industrial & Manufacturing Tech", "Audio software", "Sound-effects software for film, TV and games", "2013",
    "Edinburgh, Scotland; Greek founder Orfeas Mpoteas", "Seed", "Seven figures (amount undisclosed)", "2022-02",
    "Metavallon VC (lead); Old College Capital", U,
    "https://en.wikipedia.org/wiki/Krotos_Ltd | https://www.powergame.gr/start-ups-digital/208118/krotos-i-elliniki-startup-pou-kanei-thoryvo-sto-choligount/",
    "Exclude", "Verified; not deep tech", "Creative software.")
add("Dataphoria", "AI & Machine Learning", "ESG analytics SaaS", "ESG analytics platform", U,
    "Athens, Greece", "Seed", "EUR 335K (USD 390K)", "2026-09-18", "Investing for Purpose (lead); angels", U,
    "https://app.fundz.net/fundings/dataphoria-funding-round-dc8466 | https://www.cbinsights.com/company/dataphoria",
    "Exclude", "Round verified (aggregators); not deep tech", "SaaS analytics.")
add("Mobito", "AI & Machine Learning", "Mobility data marketplace", "Aggregated connected-vehicle data platform", U,
    "Brussels, Belgium; CEO George Cambanis", "Seed", "EUR 1M", "2025-06",
    "Loggerhead Ventures; Sporos Platform; Moro Global; imec.istart", U,
    "https://athenstechcircle.beehiiv.com/p/mobito-raises-1m-to-scale-its-tech-infrastructure-and-expand-across-europe-58c7 | https://finder.techleap.nl/news/feed/mobito-secures-1m-for-european-growth",
    "Exclude", "Round verified; not deep tech", "Data marketplace.")
add("NeuroVirt", "Health & Biotech", "VR rehabilitation", "XR-based movement rehabilitation for stroke", U,
    "London; founder Eve Gregoriou is Cypriot per Cypriot press", "Seed", "USD 1.5M (aggregator)", U, "Genesis Ventures; Conception X; Innovate UK", U,
    "https://www.trysignalbase.com/news/funding/neurovirt-secures-15m-in-seed-funding-to-revolutionize-vr-powered-rehabilitation-care | https://en.politis.com.cy/portraits/portraits-personae/950839/rewiring-recovery-dr-eve-gregorious-new-era-of-stroke-rehabilitation",
    "Exclude", "Greek link NOT FOUND (Cypriot founder)", "The Recursive calls it Greek-founded; not confirmed.")
add("Electryone AI", "Energy & Climate Tech", "Energy AI", "AI platform for energy suppliers and storage", "2023",
    "Cyprus-linked; founders described as Cypriot", "Seed", "EUR 400K (33East)", "2025-01", "33East Venture Capital; Genesis Ventures; others", U,
    "https://fastforward.com.cy/tech/how-local-funding-gave-electryone-ai-reason-return | https://finder.techleap.nl/news/feed/electryone-ai-secures-400k-funding",
    "Exclude", "Not Greek (Cypriot founders)", "Genesis is a minor investor.")
add("Xatoms", "Quantum & Advanced Computing", "AI and quantum chemistry for materials", "Light-activated materials for water purification", "2024",
    "Toronto, Canada; Slovak founders", "Pre-seed", "USD 3M", "2025-06", "Quantacet (lead); Genesis Ventures; BDC Thrive Lab", U,
    "https://thequantuminsider.com/2025/06/19/xatoms-secures-3-million-in-pre-seed-funding-to-combine-ai-and-quantum-chemistry-for-water-purification-technology/",
    "Exclude", "Not Greek", "Greek fund is a minor investor; kept only as a checked candidate for the empty Quantum box.")
add("Averywell", "Health & Biotech", "Liquid biopsy", "miRNA-based liquid biopsy for early lung cancer detection", U,
    "Manchester, UK; no Greek link found", "Pre-seed", "Not disclosed", "2024-04", "Genesis Ventures (pre-seed); Barclays Eagle Labs", U,
    "https://www.caplight.com/company/averywell | https://www.genesis-ventures.vc/our-portfolio",
    "Exclude", "Greek link NOT FOUND", "Greek fund is the only link.")
add("SquareDev", "AI & Machine Learning", "Enterprise AI assistants", "AI assistants for internal business search and customer support", U,
    "Greek link UNVERIFIED (appears in an Athens Exchange filing as SquareDev BV)", "Seed", NF, U, NF, U,
    "https://athexgroup.gr/sites/default/files/hermes/2025-03/f4c3d366-7604-4ae4-94cb-b10ec7440ba2/826_2030_2025_Greek_1.pdf | https://athenstechcircle.beehiiv.com/p/greek-startups-vcs-funding-report-from-jan-jun-2025-9",
    "Hold", "Seed listed in Athens Tech Circle report; amount, investors and ownership NOT FOUND", "Filing is from a listed Greek company; relationship not established.")


# ---------------- Fifth research pass ----------------
upd("Koios Care", map_status="Borderline", website="https://www.koios.care/",
    what_they_do="Parkiwatch: Class IIa medical-device software that turns smartwatch movement into kinematic measures for Parkinson's care",
    hq_greek_link="Antwerp, Belgium; Greek lead investor (Evercurious VC) and HeBAN angels; team page lists CEO Konstantinos Kyritsis and CTO Dimitris Iakovakis (nationality not stated)",
    verification_status="Round and company verified on its own site; Greek link rests on investors, not on a stated nationality",
    source_link="https://www.koios.care/ | https://www.koios.care/about | https://siliconcanals.com/koios-care-lands-e1m-in-funding/",
    notes="Backed by imec.istart and VLAIO per the site. Greek names on the team are not treated as proof of nationality.")
upd("SquareDev", map_status="Borderline", website="https://squaredev.io/", founded="2018 (Built In)",
    hq_greek_link="Majority owned by Greek group Quality & Reliability (QnR) since 2025; Athens project roles; CB Insights lists Brussels",
    stage="Majority stake acquired by QnR", last_round_amount="EUR 1M investment (Athens Tech Circle); USD 1.18M for a majority stake (CB Insights)",
    last_round_date="2025-03", investors="Quality & Reliability S.A. (QnR)",
    verification_status="Ownership by a Greek group reported by two sources; founders not named",
    source_link="https://athenstechcircle.beehiiv.com/p/growing-faster-together-collaboration-the-key-to-business-success | https://www.cbinsights.com/company/squaredev | https://builtindublin.ie/company/squaredev",
    notes="Appears as SquareDev BV in an Athens Exchange filing. About 19 staff per Built In.")
upd("NOFire AI", map_status="Exclude", verification_status="Round verified; US-listed devops software with no Greek HQ found",
    notes="Team names look Greek but nationality is not stated and the site gives no location. DevOps software, not deep tech.")
upd("PolyModels Hub", map_status="Exclude", verification_status="Round verified; Greek link is the investor only",
    notes="London company. One outlet mentions a Greek co-founder, which is not confirmed. Site unreachable.")
upd("Code BGP", stage="Exited (acquired by Cisco, ThousandEyes)", last_round_amount="Acquisition, terms undisclosed", last_round_date="UNVERIFIED (Cisco ThousandEyes post undated in the page text)",
    investors="Acquirer: Cisco. Earlier: Marathon Venture Capital", map_status="Include",
    verification_status="Acquisition verified by Cisco ThousandEyes blog; date UNVERIFIED",
    source_link="https://www.thousandeyes.com/blog/cisco-announces-acquisition-of-codebgp | https://www.cnn.gr/tech/story/271143/xrimatodotisi-1-2-ekat-eyro-gia-tin-code-bgp",
    notes="Described by Cisco as a privately held BGP monitoring company based in Greece. codebgp.com now redirects to the Cisco post.")
upd("Aether Aeronautics", website=U,
    notes="aether-aero.com belongs to a different company (Aether Aerospace, eVTOL) and is not used. NAMFI suitability certification reported for PNS-1 and NMS-2 targets (Greek-language report). EFA Group partnership.")
upd("Think Silicon", website="https://think-silicon.com/ (redirects to Applied Materials)")
upd("Seervision", notes="19 staff per Startupticker at the time. seervision.com now redirects to Q-SYS.")


# ---------------- Sixth pass: fixes from the source re-check (2026-10-16) ----------------
upd("Progressive Robotics",
    source_link="https://www.eu-startups.com/2026/02/from-athens-to-thessaloniki-10-of-the-most-promising-greek-startups-to-keep-an-eye-on-in-2026/ | https://finder.techleap.nl/news/feed/progressive-robotics-raises-1-55m-seed-funding | https://www.vcbacked.co/company/progressive-robotics",
    verification_status="Verified (EU-Startups page read in a browser: Thessaloniki, founded 2023, EUR 1.55M)")
upd("Intelligencia",
    source_link="https://www.mobihealthnews.com/news/emea/greek-ai-startup-intelligencia-scores-eu102m-series-round | https://www.businesswire.com/news/home/20210810005501/en/Intelligencia-Raises-%2412M-to-Reduce-the-Risk-of-Clinical-Research-Improve-RD-Productivity-and-Accelerate-Scientific-Breakthroughs",
    verification_status="Verified (MobiHealthNews, 2021-08-19, read in a browser; later rounds UNVERIFIED)")
upd("Purposeful", last_round_date="2023-06-20", stage="Strategic investment by PharOS with share purchase from Metavallon",
    verification_status="Deal verified (Zepos & Yannopoulos, 2023-06-20, read in a browser); value NOT FOUND",
    source_link="https://www.zeya.com/news/zepos-yannopoulos-advised-purposeful-strategic-collaboration-pharos | https://ceelegalmatters.com/greece/23608-zepos-yannopoulos-advises-purposeful-on-pharos-partnership")
upd("TileDB (rebranded Tile.ai)",
    investors="AlleyCorp (lead); Two Bear Capital; Nexus Venture Partners; Intel Capital; Lockheed Martin Ventures; Amgen Ventures; Verizon Ventures; Big Pi Ventures (listed as a Series B investor by PitchBook)",
    source_link="https://www.businesswire.com/news/home/20231010796451/en/TileDB-closes-34M-Series-B-to-advance-the-vision-of-the-%E2%80%98modern-database%E2%80%99-as-an-alternative-to-the-%E2%80%98modern-data-stack%E2%80%99 | https://siliconangle.com/2023/10/10/multimodal-database-startup-tiledb-raises-34m-series-b-funding/ | https://therecursive.com/?p=32254 | https://bigpi.vc/",
    last_round_date="2023-10-10",
    verification_status="Round verified against the company release (lead and participants); Big Pi's participation from PitchBook")
upd("Bioemtech",
    verification_status="Not re-verified: figures come from a 2024 company presentation (PDF) that could not be opened automatically")
upd("Neurohive", last_round_amount="UNVERIFIED (an aggregator lists USD 160K total; page not machine-readable)",
    verification_status="Genesis portfolio listing verified; amount UNVERIFIED")
upd("Pinepeak", last_round_amount="UNVERIFIED (an aggregator lists USD 580K total; not re-confirmed)",
    verification_status="Genesis portfolio listing and Greek founders (one article) found; amount UNVERIFIED")
upd("Pleioflow", last_round_amount="UNVERIFIED (PitchBook lists USD 1.74M, undated; not re-confirmed)",
    verification_status="Greek subsidiary and Genesis portfolio listing verified; amount UNVERIFIED")


# ---------------- Seventh pass: founding years, websites, dates (2026-10-21) ----------------
upd("Acumino", founded="2021 (CB Insights, Endeavor, Preqin; one outlet says 2023)",
    hq_greek_link="Washington state per CB Insights and Preqin; Endeavor Greece lists the company with offices in the USA, Greece and New Zealand; founders Minas Liarokapis (CEO), Tom White, Patrick Jarvis",
    source_link="https://bigpi.vc/ | https://www.endeavor.org.gr/companies/acumino | https://www.cbinsights.com/company/acumino | https://www.trysignalbase.com/news/funding/acumino-secures-117 | https://www.caplight.com/investor/radarventures | https://www.orrick.com/fr-FR/News/2026/07/Acumino-Raises-11-7-Million-Seed-Round-and-Joins-Google-DeepMinds-European-Robotics-Accelerator")
upd("Augmenta", founded="2016 (Elevate Greece registry) or 2017 (Dealroom)",
    hq_greek_link="Athens, Greece (also Austin, Texas); founders George Varvarelis and Dimitris Evangelopoulos; early work in Volos per Endeavor; offices kept after the acquisition",
    notes="Shown as exit context. Marathon was a shareholder; its proceeds are not disclosed in sources found. Founding year differs between registry and Dealroom.")
upd("SAS Technology", founded="2020 (July, company site and Army Recognition; research since 2015)",
    hq_greek_link="Piraeus HQ with engineering facilities in Glyka Nera, Athens; subsidiary of Spirit World Group (founded 2004)",
    source_link="https://sas-tech.gr/about.html | https://sas-tech.gr/dl/SAS_Brochure.pdf | https://greekreporter.com/2025/02/16/greek-drone-sarisa-rocket-combat-ready/")
upd("Keragon", founded="2022 (CB Insights, PitchBook) or 2024 (The Recursive)",
    hq_greek_link="New York (PitchBook, The Recursive) or Boston (CB Insights); described as Greek-founded by The Recursive and Vestbee; founders Conno Christou, George Makkoulis, Panos Papageorgiou, George Eracleous (earlier co-founded Avocarrot)",
    verification_status="Round verified; Greek link from two outlets (The Recursive, Vestbee)",
    source_link="https://keragon.com/blog/keragon-ai-powered-healthcare-automation-platform-secured-7-5m-seed-round | https://vestbee.com/blog/articles/keragon-raises-7-5-m | https://therecursive.com/?p=39354 | https://www.cbinsights.com/company/keragon")
upd("Proxy Foods AI", founded="2022 (Georgetown alumni page, Endeavor)",
    source_link="https://pulse2.com/proxy-foods-ai-raises-6-million-seed-round-to-expand-ai-native-food-rd-platform/amp/ | https://www.endeavor.org.gr/entrepreneurs/panos-kostopoulos | https://biotechnology.georgetown.edu/alumni-entrepreneurs/proxy-foods/")
upd("Intryc", founded="2024 (inferred from Y Combinator S24; not stated)")
upd("Think Silicon", founded="2007 (founders George Sidiropoulos and Iakovos Stamoulis)",
    source_link="https://thehellenicinitiative.org/thi-news/the-hellenic-initiatives-annual-venture-fair-winner-think-silicon-acquired-by-applied-materials/ | https://endeavor.org.gr/think-silicon-from-patras-greece-to-its-acquisition-by-applied-materials/ | https://www.jonpeddie.com/techwatch/think-silicon-secures-investment-round-2/")
upd("Intelligencia", founded="2017 (most sources; newmoney.gr says 2018); co-founders Dimitrios Skaltsas and Vangelis Vergetis")
upd("ORamaVR", founded="2016 (FORTH spin-off in Heraklion; formerly Ovid VR)",
    hq_greek_link="Geneva (HQ) with a Greek entity in Heraklion, Crete (Elevate Greece registry); FORTH-ICS is an investor",
    source_link="https://athenstechcircle.beehiiv.com/p/oramavr-secures-4-5m-late-seed-funding | https://ggba.swiss/en/geneva-based-oramavr-raises-usd-4-5-million-to-scale-medical-xr-training-solutions/ | https://registry.elevategreece.gov.gr/company/oramavr-%CE%BC%CE%BF%CE%BD%CE%BF%CF%80%CF%81%CF%8C%CF%83%CF%89%CF%80%CE%B7-%CE%B1-%CE%B5/")
upd("Anodyne Nanotech", founded="2019 (Boston Globe, Endeavor, Built In Boston); founders Hojat Rezaei Nejad, Konstantinos Tzortzakis, Jake Lombardo",
    hq_greek_link="Boston; listed by Endeavor Greece, which profiles co-founder and chief business officer Konstantinos Tzortzakis; Greek VCs invested",
    website="https://www.theheropatch.com/")
upd("Anacalypsis Therapeutics", founded="2019 (single source)",
    last_round_amount="EUR 300K (Athens LifeTech Park post, Brain Gain Fund); aggregators list USD 340-344K")
upd("Prisma Electronics", founded="1991 (Alexandroupolis; several company profiles)")
upd("Bioemtech", founded="2013 (one profile; company is BioEmission Technology Solutions IKE)",
    hq_greek_link="Athens, Greece (NCSR Demokritos Technology Park, Pallini; Elevate Greece registry)")
upd("Feel Therapeutics", founded="2015 (formerly Sentio Solutions and Myfeel)",
    hq_greek_link="HQ San Francisco; about 30 staff in Athens, mainly R&D (Hellenic Initiative); co-founders George Eleftheriou (CEO) and Haris Tsirmpas (CTO); listed in the Elevate Greece registry",
    verification_status="Verified (Greek R&D base confirmed by the Hellenic Initiative); totals conflict (USD 7.5M vs 22.5M)",
    source_link="https://thehellenicinitiative.org/feel-therapeutics-brings-objective-measurements-to-mental-health-diagnosis-and-treatment | https://greekanalyst.substack.com/p/reinventing-mental-health | https://registry.elevategreece.gov.gr/company/sentio-solutions/ | https://www.cbinsights.com/company/feel-therapeutics/financials",
    map_status="Include")
upd("Brainomix", founded="2010 (University of Oxford spin-out; co-founder and CEO Michalis Papadakis)",
    hq_greek_link="Oxford, UK; profiled by Endeavor Greece (founder Michalis Papadakis); nationality and a Greek office not stated",
    source_link="https://www.brainomix.com/news/brainomix-series-c/ | https://www.endeavor.org.gr/companies/brainomix | https://www.ox.ac.uk/news/2024-02-06-oxford-spinout-brainomix-is-revolutionising-stroke-care-through-ai | https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15740447/brainomix-completes-18m-funding-round-plans-us-expansion")
upd("Achira AI", founded="2023 (one article) or 2024 (Startup-Seeker, Built In)",
    hq_greek_link="San Francisco per Built In (hybrid SF/New York); Greek co-founder Theofanis Karaletsos; described as having Greek roots by FastForward",
    source_link="https://finder.techleap.nl/news/feed/achira-ai-secures-33m-in-funding | https://www.thenationalherald.com/greek-startup-achira-ai-gets-33-million-in-investor-funding/ | https://fastforward.com.cy/breakthrough/achira-biotech-startup-greek-roots-nvidia | https://builtin.com/company/achira/teams")
upd("Causaly", founded="2018 (incorporated 2018-05-17, Companies House)",
    hq_greek_link="London, UK (Companies House); Greek founder Ioannis Kiachopoulos per Greek press; no Athens office found")
upd("Bota Systems", founded="2020 (ETH Zurich spin-off, independent from 2020)",
    hq_greek_link="Zurich; CEO Klajd Lika grew up in Greece and studied in Athens (profile), co-founder Ilias Patsiaouras; Marathon-led; covered by Greek press",
    source_link="https://www.startupticker.ch/en/news/bota-systems-raises-2-5-million-in-seed-round | https://www.walderwyss.com/en/news/2023-10-03_bota-systems-ag-announces-the-completion-of-usd-2-5m-seed-round | https://www.powergame.gr/start-ups-digital/520909/bota-systems-ependyei-25-dis-dol-gia-ta-robot/")
upd("Centaur Analytics", founded="2014 (Elevate Greece registry; Endeavor data field says 2016); co-founders Sotiris Bantas and Vasilis Sotiroudas",
    last_round_date="2018-10 (USD 3M round, ImpactAlpha 2018-10-11); first seed 2016-09",
    source_link="https://agfundernews.com/centaur-analytics-raises-3m-seed-round-for-post-harvest-crop-monitoring | https://impactalpha.com/centaur-analytics-secures-3-million-to-cut-food-waste-using-sensors | https://registry.elevategreece.gov.gr/company/centaur-technologies-p-c | https://www.endeavor.org.gr/companies/centaur-analytics")
upd("Code BGP", founded="2021 (FORTH spin-off announced 2021-06-23)",
    last_round_date="2023-08 (acquisition by Cisco)",
    hq_greek_link="Heraklion, Crete (Elevate Greece registry); Delaware parent with a Greek subsidiary; FORTH-ICS spin-off; founders Xenofontas Dimitropoulos, Vasileios Kotronis, Lefteris Manassakis",
    verification_status="Acquisition verified (Cisco ThousandEyes, FORTH, GSRI); August 2023 per FORTH news item",
    source_link="https://www.thousandeyes.com/blog/cisco-announces-acquisition-of-codebgp | https://www.forth.gr/en/news/show/&tid=3011 | https://gsri.gov.gr/en/forth-ics-spin-off-company-code-bgp-acquired-by-cisco/ | https://forth.gr/en/news/show/&tid=1940 | https://registry.elevategreece.gov.gr/company/code-bgp")
upd("Terra Robotics", founded="2020 (CB Insights, single source)")
upd("Hoplon AI", founded="2023 (one report)")
upd("Attisat", founded="UNVERIFIED (active with ESA by 2003)", website="https://attisat.gr/ (listed by ESA ARTES; the site fails a certificate check)")
upd("Seervision", founded="2016 (ETH Zurich spin-off; founders Nikos Kariotoglou, Reto Hofmann, Conrad von Grebel)",
    website="https://www.seervision.com/ (redirects to Q-SYS)")
upd("Intelistyle", founded="2017 (launched December 2017) or 2018 (Startups 100)", website="https://intelistyle.com/")
upd("Pleioflow", founded="2018 (CB Insights, PitchBook)",
    hq_greek_link="Burton-on-Trent, UK with offices in Germany and Greece (2024 conference talk); Greek subsidiary Pleioflow Hellas SA (Nea Kifissia); listed by Genesis Ventures",
    website="https://pleioflow.com/")
# websites confirmed by fetching the page in the logo step
upd("Velos Rotors", website="https://velos-rotors.com/")
upd("Robenso", website="https://robenso.gr/")
upd("ClearDrop", website="https://cleardrop.tech/")
upd("Neurohive", website="https://neurohive.eu/")
upd("PlugSecure", website="https://plugsecure.com/")
upd("Mind The Hack", website="https://mindthehack.ai/")
upd("Hoplon AI", website="https://hoplonai.com/")
upd("Satways", website="https://www.satways.net/")


# ---------------- Eighth pass: remaining gaps (2026-10-21) ----------------
upd("Velos Rotors", founded="2011 (design work began; first product Velos 880 in 2014, per company About page)",
    hq_greek_link="Xylokastro, Greece (Velos Rotors SA; Elevate Greece registry describes it as Greek-founded)",
    source_link="https://tech.eu/2023/04/06/velos-rotors-snags-2-million-to-help-drone-helicopter-production-take-off | https://registry.elevategreece.gov.gr/company/velos-rotors | https://velos-rotors.com/about-us/")
upd("Aether Aeronautics", founded="2018 (company About page: established in Chania, Crete)", website="https://www.aether-aeronautics.com/",
    source_link="https://www.aether-aeronautics.com/about-us | https://www.parapolitika.gr/zoi/article/1111770/stratigiki-sunergasia-tou-omilou-efa-group-me-tin-elliniki-aether-aeronautics-pc-gia-tin-anaptuxi-enaerion-stohon/app/ | https://registry.elevategreece.gov.gr/company/aether-aeronautics-pc",
    notes="Aether Aeronautic S.A.; aether-aero.com is an unrelated eVTOL company. NAMFI suitability certification reported for PNS-1 and NMS-2 targets (Greek-language report). EFA Group partnership.")
upd("Core Innovation and Technology", founded="2016 (company About page; CORE Innovation Centre founded 2020)",
    hq_greek_link="Offices in south Athens (about 70 people per the company); CORE Innovation Centre in Chalkida",
    what_they_do="Industry 4.0 engineering and AI: COREbeat predictive-maintenance platform, Greek Smart Factory testbed",
    source_link="https://www.core-innovation.com/about | https://portal.effra.eu/organisation/12520 | https://cordis.europa.eu/project/id/101079180",
    notes="Identity now confirmed by the company's own About page (CORE Innovation Group, COREbeat, Greek Smart Factory).")
upd("Attisat", founded="1997 (Greek Space Ecosystem Catalogue)",
    hq_greek_link="Attica, Greece (ATTISAT Attica Satellite Antennas S.A.; Moschato/Kallithea listings)",
    source_link="https://www.space-ecosystem.gr/organisations/attisat/ | https://artes.esa.int/contractors/attisat | https://esa.int/Applications/Connectivity_and_Secure_Communications/Invisible_satellite_dishes_to_preserve_Athens_skyline")
upd("ClearDrop", last_round_amount="USD 700K (Signalbase, aggregator)", last_round_date="2026-06",
    stage="Seed (label UNVERIFIED)", website="https://cleardrop.tech/",
    investors="Genesis Ventures (portfolio listing); Obratori (portfolio listing per Signalbase)",
    hq_greek_link="Technology developed with IEMN, University of Lille and CNRS (company site); Greek link: Genesis Ventures portfolio and CEO Nikos Christopoulos (nationality not stated); HQ UNVERIFIED",
    source_link="https://www.genesis-ventures.vc/our-portfolio | https://cleardrop.tech/ | https://www.trysignalbase.com/news/funding/cleardrop-raises-700k-funding | https://athenstechcircle.beehiiv.com/p/never-marry-your-ideas-or-assumptions-nikos-christopoulos-ceo-cleardrop",
    verification_status="Genesis listing and site verified; round from one aggregator; founding year NOT FOUND")
upd("Augmenta", website="https://www.augmenta.ag/ (redirects to the Raven Industries product page)")
upd("Delian Alliance Industries", website="https://delian.ai/")
upd("Better Origin", website="https://betterorigin.co.uk/")
upd("Purposeful", website="https://purposeful.eu/",
    hq_greek_link="Greece; listed in the Elevate Greece registry as PURPOSEFUL IKE; described as a Greek startup by Zepos & Yannopoulos")
upd("Terra Robotics", website="https://terrarobotics.io/", hq_greek_link="Thessaloniki, Greece (Ptolemeon 29A; Elevate Greece registry)")
upd("Pinepeak", website="https://www.pinepeak.co.uk/",
    hq_greek_link="Cambridge, UK (University of Cambridge Founders portfolio); two founders are Greek per The Next Web",
    source_link="https://thenextweb.com/news/pinepeak-wildfire-simulator-predicts-fire-risks | https://www.genesis-ventures.vc/our-portfolio | https://founders.cam.ac.uk/portfolio/pinepeak/ | https://www.premieralts.com/companies/pinepeak")


# ---------------- Ninth pass: round dates ----------------
upd("Navenio", last_round_date="2020 or 2021 (sources differ: Global Venturing May 2020, CB Insights Dec 2021)",
    investors="Oxford Science Enterprises (lead); QBN Capital; Big Pi Ventures; Future Planet Capital; University of Oxford",
    source_link="https://businesscloud.co.uk/news/indoor-gps-scaleup-navenio-navigates-to-9-5m/ | https://en.wikipedia.org/wiki/Niki_Trigoni | https://www.cbinsights.com/company/navenio/financials")
upd("Robenso", last_round_date="2025-02 (VCBacked, aggregator)")


# ---------------- Tenth pass: ESA BIC Greece and space additions (2026-10-21) ----------------
ESA_BIC = "https://www.athenarc.gr/en/news/esa-bic-greece-five-years-32-startups-and-greeces-growing-role-new-space-economy"
add("QRBIT", "Quantum & Advanced Computing", "Quantum satellite communications",
    "Photonic hardware and software for optical ground stations and satellite quantum key distribution (QKD)",
    "2025 (spin-off approved by NTUA and ICCS in 2025)",
    "Athens; spin-off of the NTUA Photonics Communications Research Laboratory (ICCS); founders Ioannis Giannoulis (CEO), Aristeidis Stathis, Argyrios Danos",
    "Incubated (ESA BIC Greece); university spin-off", "Not disclosed", U,
    "NTUA and ICCS (equity stakes); ESA BIC Greece", "https://qrbit.gr/",
    "https://photonics.ntua.gr/pcrl-members-found-the-spin-off-company-qrbit | https://www.iccs.gr/?p=15488 | https://esa-bic.gr/qrbit/",
    "Include", "Verified (university announcements and ESA BIC Greece page)",
    "First company in the Quantum box. Dealroom lists a EUR 50K angel entry (not verified). No venture round found.")
add("SolidKosmos", "Semiconductors & Hardware", "Radiation testing for electronics",
    "SK-RAFT tool that emulates radiation-induced faults to qualify off-the-shelf electronics for space, defense and automotive",
    "2024 (directory; ESA BIC Greece incubation 2024-2026)",
    "Piraeus, Greece; spin-off of the University of Piraeus Research Centre; founders Dimitris Agiakatsikas (CEO), Mihalis Psarakis (CTO), Vassilis Vlagkoulis",
    "Incubated (ESA BIC Greece); university spin-off", "Not disclosed", U,
    "ESA BIC Greece", "https://solidkosmos.gr/",
    "https://esa-bic.gr/solidkosmos/ | https://commercialisation.esa.int/?p=11652 | https://app.beta.dealroom.co/companies/solidkosmos_s_a_",
    "Include", "Verified (ESA pages); founding year from a directory", "")
add("Trimsignal", "Semiconductors & Hardware", "Chip design IP",
    "Patented dynamic frequency boosting and a digital design approach that raise processor performance and cut power use",
    "2021 (ESA BIC Greece page)",
    "Greece (Greek and US entities); CEO and co-founder Nikolaos Zompakis, co-founder Georgios Pappas",
    "Incubated (ESA BIC Greece)", "Not disclosed", U,
    "ESA BIC Greece", "https://www.trimsignal.com/",
    "https://esa-bic.gr/trimsignal/ | https://www.iefimerida.gr/tehnologia/trimsignal-epexergastes-allazoyn-tahytita | https://www.trimsignal.com/",
    "Include", "Verified (ESA BIC page, Greek press, company site)",
    "Company-reported gains: 35-60% performance, 15-40% lower power (Greek press). Site lists a HICOOL 2024 prize.")
add("EMTech Space", "Space & Defense", "Spacecraft simulators and CubeSats",
    "Spacecraft simulators and validation facilities; prime contractor of the Hellenic Space Dawn CubeSat mission",
    "2009 or earlier (spacecraft simulator work since 2009, EMTECH group)",
    "Athens, Greece; presence in Germany and Cyprus; founder and CEO Nikolaos-Antonios Livanos",
    "Established SME; national CubeSat programme contracts (ESA-managed)", NF, NF,
    "None found (Greek national CubeSat programme, funded by the EU Recovery and Resilience Facility)", "https://emtech.space/",
    "https://www.esa.int/Applications/Connectivity_and_Secure_Communications/ESA_backs_Greek_firms_and_universities_CubeSats | https://www.powergame.gr/start-ups-digital/466684/nanodoryforoi-made-in-greece-sto-diastima-to-2024 | https://emtech.space/",
    "Include", "Existence and role verified; no external funding found",
    "Spun out Odes Space (simulation software), an ESA BIC Greece incubatee.")
add("OQ Technology", "Space & Defense", "5G satellite IoT and direct-to-device",
    "Low-orbit satellite operator for 5G IoT and satellite-to-smartphone connectivity", "2016 (founder Omar Qaise)",
    "HQ Luxembourg; Greek subsidiary OQ Technology Hellas (Corallia, Athens) as technology and production hub; Greek fund Phaistos co-led the Series A",
    "Venture debt (after Series A)", "EUR 25M EIB venture debt (EUR 13M Series A in 2022-09)", "2026-02-25",
    "European Investment Bank (venture debt). Series A co-led by Wa'ed Ventures (Aramco) and Phaistos Investment Fund (Greece)",
    "https://www.oqtechnology.com/",
    "https://www.eib.org/en/press/all/2026-x072-european-financing-for-luxembourgish-satellite-to-smartphone-connectivity-pioneer-oq-technology | https://www.wamda.com/en/2022/09/aramco-waed-ventures-invests-13-million-series-round-oq-technology | https://www.powergame.gr/start-ups-digital/298934/oq-technology-me-technologia-apo-to-diastima-idryei-thygatriki-stin-ellada/",
    "Borderline", "Verified (EIB press release, Wamda); Greek link is the subsidiary and investor",
    "Not Greek-founded; shown like Open Cosmos as a foreign firm with a Greek base.")
add("Solmeyea", "Energy & Climate Tech", "CO2-to-protein (microalgae)",
    "Hybrid vertical microalgae farming that turns industrial CO2 into protein (MEY), cosmetic ingredients and fuels",
    "2019 (CB Insights)", "Pallini, Greece (SOLMEGIA IKE); founder and CEO Vasilis Stenos",
    "Grant-funded", "USD 3.2M-3.3M total, mostly EU grants (aggregators)", U,
    "EIC Accelerator; Circular Bio-based Europe JU; EIT Food; ESA BIC Greece", "https://www.solmeyea.com/",
    "https://cordis.europa.eu/project/id/101188544 | https://esa-bic.gr/solmeyea/ | https://bioenergyinternational.com/cycleo-solmeyea-biotech-to-convert-co2-into-food-protein/ | https://www.cbinsights.com/company/solmeyea/financials",
    "Include", "Company and EU project verified; totals from aggregators", "Pilot with CycleO to convert 100 t CO2 into 15 t protein a year.")

for i, r in enumerate(R, 1):
    r["company_id"] = "GRDT-%03d" % i

out = sys.argv[1]
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    w.writerows(R)

from collections import Counter
print(len(R), Counter(r["map_status"] for r in R))
