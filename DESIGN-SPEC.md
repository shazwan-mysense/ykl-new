# YKL Mac Fix — Devix-style rebuild. Design spec (canonical)

Reference template: https://devix.framer.website/ (structure + look cloned faithfully, content re-directed to YKL Mac Fix, Malaysia).

## Tokens
- bg page: #F2F1ED (warm bone) · cards/panels: #FFFFFF · footer band: #ECEAE5
- ink: #141414 · secondary text: rgba(20,20,20,.6) · faint: rgba(20,20,20,.4)
- hairline: rgba(20,20,20,.08) · accent blue: #1667D9 (hover #0F55C4)
- radius: cards 14px, images 10px, buttons pill (100px), icon tile 12px
- fonts: "Host Grotesk" 400/500 (all headings + body), "IBM Plex Mono" 400/500 (eyebrows, chips, dates, column headers, copyright)
- headings weight 400, letter-spacing -0.03em, line-height 1.08. Body 18px lh 1.45. Card body 15.5px.
- H1 hero ~clamp(46px→88px), section H2 ~clamp(34px→54px)

## Recurring components (classes in assets/css/style.css)
- `.eyebrow` — inline icon (14px stroke SVG) + IBM Plex Mono 12.5px uppercase ls .08em, blue. Section openers.
- `.chip-row` / `.chip` — mono 11.5px uppercase meta chips with tiny icon (clock, shield): e.g. "SAME-DAY AVAILABLE", "BACKED BY WARRANTY". Grey ink60.
- `.btn` (blue pill, white text) / `.btn--ghost` (1px blue-tint border, blue text; fills blue on hover). Sizes: default 12px 26px.
- `.link-arrow` — blue text link + → , used for "View All", "Get Directions".
- `.card` — white, radius 14, 1px hairline border, soft shadow; hover lifts 4px.
- `.media-card` — image (aspect 4:3ish, radius 10) + title below + one-line grey sub. Used: What We Repair, Devices grid, About values.
- `.service-card` — white card: blue icon → title → grey desc → chip row → footer (ghost "Learn More" pill + right-aligned note e.g. "Free diagnostics").
- `.feature` — centered: blue stroke icon, mono blue label, 22px title, grey desc. 3-col ×2 rows.
- `.stat` — centered: icon, ~56px number (JS count-up), grey label.
- `.t-quote` / `.t-photo` — testimonial 4-col row alternating photo cards and white quote cards (quote mark, bold title, body, initial-circle avatar + name).
- `.faq-grid` — two-col static Q&A, question 18px ink, answer grey, hairline under each pair.
- `.cta-panel` — big white rounded card: eyebrow "TAKE ACTION", huge H2 left, right col short text + blue pill; full-width photo (radius 10) inside card bottom.
- `.post-card` — white card: mono date, 22px title, grey desc, image flush at bottom.
- `.reveal` — scroll-in: opacity 0 / translateY(28px) → shown via `.in` (IntersectionObserver). Stagger siblings with `.reveal-group`.

## Page furniture (copy EXACTLY from index.html)
- Nav (fixed, transparent → bg+hairline after 40px scroll): logo img left · center links Services / Devices / About / Blog · right tel link "+60 3-7495 9092" + blue pill "Contact Us" → contact.html. Mobile ≤860px: hamburger → full-screen bone overlay, staggered big links.
- Footer: centered logo + blurb, then 4 link columns (mono caps headers MENU/COMPANY/CONTACT/FOLLOW), then 3 location blocks (name, address, hours, tel + WhatsApp ghost pills, Waze link), mono copyright "© 2026 YKL ONE HOUR SERVICE TRADING. ALL RIGHTS RESERVED."

## Motion
- Lenis smooth scroll (assets/js/lenis.min.js), lerp .1.
- Hero elements rise+fade on load, staggered 90ms.
- Sections: `.reveal` on scroll (700ms cubic-bezier(.22,1,.36,1)).
- Stats count up once in view.
- Hovers: nav links fade to ink60; buttons darken/fill; cards lift; card images scale 1.04 (parent overflow hidden). Everything transitioned 200-350ms — hovers must feel premium (client complaint: old site hovers are bad).
- NO marquees (mobile overflow risk). Brand strip is static.

## Second reference: kissmymac.my (competitor)
Borrow its CONVERSION patterns, keep Devix visuals:
- Trust chips under hero CTAs (free consultation / same-day / warranty / reviews)
- Stats band with count-ups right under hero (`.stats-band`)
- "How it works" 4-step strip on home (`.step-card`, Free Diagnosis → Clear Quote → Expert Repair → Test & Collect)
- "No hidden fees, final quote before we open anything" messaging
- WhatsApp-first CTAs + floating WhatsApp button (`.float-wa`, include on every page before scripts)
- Symptom-led copy on device cards (e.g. "Mac mini won't power on after a power trip?")

## Real client photography (Sep 2026)
Client-supplied photos replace stock wherever a genuine equivalent exists. Two components were added for them:
- `.ba-grid` / `.ba-card` — before/after proof. Two stacked `<img>` crossfade inside `.ba-media`; `.show-after`
  swaps image + badge. Controlled by the `.ba-switch` Before/After buttons, by clicking the image, and by hover
  on fine-pointer devices (hover stops once the user clicks a switch). Wired in `main.js`.
- `.team-grid` / `.team-card` — 4:5 staff portraits, name + mono label. 4 cols → 3 → 2.
Naming: `ykl-work-N.jpg` (bench candids, 3:2) and `-p` variants (4:5), `ykl-team-<name>.jpg`,
`ykl-store-N.jpg`, `ba-<device>-<n>-<before|after>.jpg`.
Rule: an image must depict what its section claims. Never put a product render or an unrelated stock scene
under copy that says "our team", "our workshop" or names a specific repair.

## Pages
index.html (canonical, hand-written) · services.html · devices.html · about.html · contact.html · blog.html · mac-screen-repair.html · mac-battery-replacement.html · mac-water-damage-repair.html · mac-logicboard-repair.html · blog-mac-running-slow.html
All flat in root; assets at assets/…. Every page: same <head> (Google Fonts Host Grotesk + IBM Plex Mono, style.css), same nav/footer, scripts lenis.min.js + main.js before </body>.

## Facts (do not invent beyond these; see CONTENT-NOTES.md for TODOs)
- Brand: YKL Mac Fix (YKL One Hour Service Trading). Mac specialists: MacBook Air/Pro, iMac, Mac mini, Mac Pro + iPad + smartphones all brands.
- USPs: up to 5 years warranty (selected repairs/upgrades) · same-day service for most Mac screen & battery jobs · interest-free installments via SPay Later · free pickup in Klang Valley for jobs RM500+ · free consultation/diagnostics · 1,190+ Google reviews, rated Excellent · 1M+ views on TikTok (@yklmacfix).
- Services: Mac water damage, battery, screen, keyboard, speaker, logicboard repair; SSD & RAM upgrades; iPad repair (screen, battery, charging port, logicboard, speaker, water damage); smartphone repair all brands (motherboard-level incl. reball).
- Locations:
  1. Petaling Jaya (HQ) — No 16, 3rd & 4th Floor, Jalan 14/20, Section 14, 46100 Petaling Jaya, Selangor · Mon–Fri 10:30 AM–7:30 PM, Sat–Sun 10:30 AM–6:00 PM · +60 3-7495 9092
  2. Kuantan @ Pandan Damai — No A3, Jalan Pandan Damai 2/2, Perumahan Pandan Damai, 25150 Kuantan, Pahang · Mon–Sat 11:00 AM–9:00 PM · +60 19-987 3386
  3. Kuantan Parade — Lot F22 (1st Floor), Kuantan Parade, Jalan Haji Abdul Rahman, 25000 Kuantan, Pahang · Mon–Sat 11:00 AM–9:00 PM · +60 11-2625 6581
- Socials: tiktok.com/@yklmacfix · instagram.com/yklmacfix · youtube.com/@yklmacfix
- WhatsApp links: wa.me/60374959092 (HQ) · wa.me/60199873386 · wa.me/601126256581
- No prices anywhere (site has none). Use "Free diagnostics" / "Free quote" instead of "From $X".
- Copy style: no em-dash clauses in headlines/subtext; short dash-free sentences.
