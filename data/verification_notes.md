# Verification notes (2026-10-16)

`verification_report.csv` is produced by `scripts/verify_sources.py`. For each company it re-fetches every `source_link` and tests whether the company name, the funding amount and the lead investor appear in the page text.

Result for the 63 mapped companies: 60 confirmed (name and amount on at least one source page), 2 unreadable by the script, 1 name not found. Lead investor found on a page for 48 of 56 rows where one was checked.

What "confirmed" means: the name and the number appear on a page the dataset cites. It does not prove that the page attributes the number to that round. Treat it as a consistency check, not an audit.

Checked by hand in a browser instead, because the script could not read the page:
- Intelligencia: MobiHealthNews, 2021-08-19 (EUR 10.2M Series A, MTIP lead, Big Pi Ventures, Synetro, ZS)
- Purposeful: Zepos & Yannopoulos, 2023-06-20 (PharOS investment and share purchase from Metavallon)
- Progressive Robotics: EU-Startups, 2026-02-03 (Thessaloniki, founded 2023, EUR 1.55M)
- Koios Care: company site team and about pages
- Genesis Ventures portfolio page (Terra Robotics, Neurohive, ClearDrop, Pinepeak, Pleioflow, PlugSecure, Hoplon AI, Feel Therapeutics, Progressive Robotics)

Not re-verified: Bioemtech (figures come from a PDF presentation the script could not read).

Fixes made during this check: three aggregator amounts (Neurohive, Pinepeak, Pleioflow) were downgraded to UNVERIFIED; TileDB's investor list was corrected to the company release; Purposeful's deal date was added.

Known gaps in the mapped rows: founding year missing for 30 of 63, website missing for 20, last-round date missing for 17, last-round amount missing or unverified for 11.
