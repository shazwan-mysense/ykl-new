# Content notes — items to confirm with YKL before go-live

## Client photo pack (received 3 Sep 2026) — live on the site
Source: `MYS_YKL_Website Development_6 pages` (37 photos + logo). Processed copies live in `assets/img/`
as `ykl-work-*` (bench candids), `ykl-team-*` (staff portraits), `ykl-store-*` (storefront) and `ba-*`
(before/after). Originals are untouched in the client folder.

**One deliberate exception:** the "Four Simple Steps to a Fixed Mac" block keeps its original stock
imagery on every page it appears (homepage plus the four service-detail pages). The client photos were
tried there and rejected — the phone-shot look did not sit well in that particular layout. Everywhere
else on the site uses the real YKL photography.

- [ ] Team section (About) lists first names only — Chris, Shahid, Huang, Ah Wei, Terence, Ah Hong, Han.
      Confirm correct spellings, preferred names, and whether they want job titles shown.
- [ ] Three of the seven team portraits are not in YKL uniform (Ah Hong, Han, Terence) and the
      backdrops vary. Worth a reshoot in polos against one wall for a consistent grid.
- [ ] Before/after section uses 4 of the 8 supplied pairs (iPad, iMac 2, MacBook 3, iPhone). Skipped:
      iMac pair 3 and iMac pair 1 — their "before" frames look like working screens, so they read as
      "nothing was repaired". MacBook pairs 1 and 2 are held in reserve.
- [ ] Before/after captions describe the visible fault only. Confirm the actual repair performed on each
      device so the captions can be made precise.
- [ ] Storefront photos all appear to be the Petaling Jaya HQ. Need exteriors/interiors of both Kuantan
      branches before the location cards can each carry their own photo.
- [ ] Still missing, would upgrade the site further: a water-damage repair in progress, iPhone/iPad
      internals (all teardown shots supplied are MacBooks), a keyboard / top-case replacement (the
      Keyboard Replacement tile currently uses a general bench shot), a full team group photo, and a
      customer handover at the counter.
- [ ] Photo editing applied: white balance, shadow lift and mild sharpening on the bench/store/team
      photos (several were underexposed). Before/after pairs deliberately received NO exposure change —
      only identical mild white balance on both halves — so the comparison is not manipulated.
- [ ] A few stock photos remain where the client pack had no equivalent: water damage treatment, SSD
      upgrade, RAM upgrade, iPad repair and iPhone repair tiles, plus the dark iPhone showcase on the
      homepage. Replace when matching real photos exist.

- [ ] IMPORTANT: the mockup now positions YKL as Apple-only (per stakeholder direction, Aug 12 2026), but yklmacfix.com currently advertises "Smartphone repair — all brands" and their TikTok shows Samsung/POCO motherboard jobs. Confirm with the client whether non-Apple repair should be dropped from the site.

- [ ] Kuantan Parade street name: their footer prints "Kuantan He Abdul Rahman" (Wix typo). Mockup uses "Jalan Haji Abdul Rahman" — confirm.
- [ ] PJ hours differ between their footer (Mon–Fri 10:30–7:30, Sat–Sun 10:30–6:00) and their contact page (Mon–Fri 10:00–8:00, Sat 10:00–6:00). Mockup uses the footer version — confirm.
- [ ] Warranty: "up to 5 years" is their sitewide claim; per-service durations unknown. Chips say "Backed by warranty" only.
- [ ] Google review count: their widget shows 1,190 reviews / "EXCELLENT". Live number will drift.
- [ ] Testimonials: real reviewer names from their homepage widget (Asyraf Muslihudin, Kamale Mohd…, Ilyia Hasnul Hadi, Nur Falisah Mat…). Quotes reconstructed from truncated widget text — verify against Google before publishing.
- [ ] WhatsApp numbers: footer chips → PJ wa.me/60374959092, Pandan Damai wa.me/60199873386, Kuantan Parade wa.me/601126256581 — confirm which numbers actually run WhatsApp Business.
- [ ] Blog: first two posts are their real titles; the other four are invented mockup topics.
- [ ] Waze links are search-by-address (waze.com/ul?q=…), not their official venue links.
- [ ] Stock lifestyle photos (assets/img/c-*.jpg, av-*.jpg) are Unsplash placeholders; product shots (macbook-air, imac-yellow, iphones, mac-lineup, macbook-float) are Apple marketing images pulled from YKL's current Wix site — replace with licensed/own photos before go-live.
- [ ] The apple-*.png/jpg files (hero stacked MacBook Airs, "go places" duo, iPhone 17 Pro camera) are Apple's own marketing assets pulled from apple.com for this mockup — same category as the Wix ones above, must be reviewed/replaced before any public launch.

---

## v2 (client reference-mockup design) — 21 Sep 2026

The client asked for the whole design to be replaced with one matching a reference mockup image
they supplied. That mockup is a generic template and carried several **wrong** details, all of
which were replaced with YKL's verified data:

| In the client's mockup PNG | Used on v2 instead | Source |
|---|---|---|
| `+60 12-345 6789` | PJ `+60 3-7495 9092` · Pandan Damai `+60 19-987 3386` · Kuantan Parade `+60 11-2625 6581` | existing verified facts |
| 2 branches, one at "Publika KL" | **3 branches**, no Publika branch exists | existing verified facts |
| "Up to 3 Years Warranty" | **Up to 5 years warranty**, on selected repairs | existing verified facts |
| "No Fix, No Charge" | dropped. It is kissmymac's claim, not YKL's. Replaced with free diagnostics / quote-first | — |
| "9 Years in the Market" | dropped, unverified. Replaced with 1,190+ Google reviews · 1M+ TikTok views · 3 branches · up to 5 yrs warranty | existing verified facts |
| "MacBook Neo" | not an Apple product. Device row is MacBook Air, MacBook Pro, iMac, Mac mini, iPad, iPhone | — |
| Hours "Mon–Sat 10–7" | PJ Mon–Fri 10:30am–7:30pm, Sat–Sun 10:30am–6:00pm · both Kuantan branches Mon–Sat 11:00am–9:00pm | existing verified facts |

### BLOCKER before v2 goes anywhere near a live domain
- **The three testimonials on `index.html` are invented.** The quotes, the names (Sarah L., Adrian H.,
  Muhammad F.) and the locations were all written for the mockup. Publishing fabricated customer reviews on a
  real business's site is not a rough edge, it is a false statement about real people's experiences. Before
  launch, either paste three real reviews from the client's Google profile with the reviewers' actual display
  names, or cut the section down to the rating line and the "Read all reviews" link, which are true. Do not
  ship as-is.
  The star ratings were removed in the 22 Sep craft pass and the rating is now stated once as "Rated Excellent
  across 1,190+ Google reviews", which matches what the client has actually published.

### Still TODO-confirm on v2
- **Team roles** on `about.html` (Senior technician, Board-level specialist, Mac technician,
  Diagnostics, Workshop lead, Front of house) are assumed. Confirm each person's actual title.
- **The three blog articles** are original copy written for the mockup. They are factually
  conservative but have not been reviewed by the client.
- **Apple product renders** (`macbook-air.png`, `macbook-float-cut.png`, `imac-yellow-cut.png`,
  `dev-macmini.png`, `ipad-hero.png`, `dev-iphone.png`, `mac-lineup.png`, `mbp-hero.jpg`) come from
  Apple's own marketing/store imagery. Licensing must be cleared, or they must be re-shot, before
  this goes live.
- **"Apple only"** positioning carries over from v1 and is still unconfirmed against the live site,
  which advertises all brands.
- The booking form on `contact.html` is a mock. It validates and shows a confirmation but sends
  nothing.
- **`og:image` and `og:url` need the final domain.** The 22 Sep pass added Open Graph and theme-color tags, but
  `og:image` points at a relative path and there is no `og:url` or `<link rel="canonical">` because the
  production domain is not decided. Both need filling in at launch or link previews will be broken.
- **The favicon is the 1500x570 wordmark**, which renders as an illegible smear at 16px. A square mark needs
  exporting before launch.
- Service-page copy asserts specific workshop capabilities (ultrasonic cleaning, stereo-microscope bench,
  panels kept in stock, BGA reballing). Board-level repair and reball are confirmed; the rest were written to
  describe a normal Apple repair workflow and should be confirmed with the client before launch.
