#!/usr/bin/env python3
"""Generates the v2 inner pages from index.html's shared header/footer + per-page bodies.
Run from inside v2/:  python3 _build.py
Re-running regenerates every page EXCEPT index.html."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
idx = open('index.html', encoding='utf-8').read()

# The cache-buster is whatever index.html is currently stamped with, so the 12 generated
# pages can never drift onto a stale stylesheet after index.html is bumped by hand.
VER = re.search(r'v2\.css\?v=([0-9a-z]+)', idx).group(1)

def between(a, b):
    i = idx.index(a); j = idx.index(b)
    return idx[i:j]

HEADER = between('<!-- ============ UTILITY BAR ============ -->', '<!-- ============ HERO ============ -->')
PROCESS = between('<!-- ============ PROCESS ============ -->', '<!-- ============ STATS + REVIEWS ============ -->')
FOOTER  = idx[idx.index('<!-- ============ FOOTER ============ -->'):]

HEAD = '''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<script>document.documentElement.className="js"</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0171FD">
<meta property="og:type" content="website">
<meta property="og:site_name" content="YKL Mac Fix">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="../assets/img/ykl-work-3.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/img/ykl-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/v2.css?v={ver}">
</head>
<body>

'''

ART_ALT = {
 'ykl-work-6.jpg':'YKL technician running diagnostics on a MacBook',
 'mac-lineup.png':'The Apple Mac line-up: MacBook, iMac, Mac mini and Mac Pro',
 'ykl-work-8.jpg':'YKL Mac Fix technician at the repair bench',
 'ykl-work-1.jpg':'YKL technician replacing a MacBook display',
 'ykl-work-4.jpg':'YKL technician removing a MacBook battery',
 'ykl-work-3.jpg':'YKL technician inspecting a logic board under a microscope',
 'ykl-work-2.jpg':'YKL technician cleaning a liquid-damaged Mac board',
}

ARROW = '<svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
WA = 'https://wa.me/60374959092'

def phero(crumb, h1, lead, art=None, script=None, plain=False, cta=True):
    c = ' phero--plain' if plain else ''
    s = f'''<section class="phero{c}">
  <div class="wrap">
    <div>
      <p class="crumb rv"><a href="index.html">Home</a><span>/</span>{crumb}</p>
      <h1 class="mask"><span>{h1}</span></h1>
      <p class="lead rv" style="--d:.14s">{lead}</p>'''
    if cta:
        s += f'''
      <div class="hero-cta rv" style="--d:.24s">
        <a class="btn btn--wa" href="{WA}" target="_blank" rel="noopener">Get a free quote</a>
        <a class="btn btn--ghost" href="contact.html">Find a branch</a>
      </div>'''
    s += '\n    </div>'
    if art:
        sc = f'<p class="script phero-script rv">{script}</p>' if script else ''
        alt = ART_ALT.get(art, '')
        s += f'''
    <div class="phero-art rv" style="--d:.2s">{sc}
      <img src="../assets/img/{art}" alt="{alt}" loading="eager">
    </div>'''
    s += '\n  </div>\n</section>\n'
    return s

def sec_head(script, h2, lead=None, link=None, center=False, tier='main'):
    """`script` is kept in the signature for the existing call sites but is no longer
    rendered: one handwritten accent per page reads as a signature, eight reads as a
    template. Section openers are separated by a hairline rule instead (see the craft
    layer in v2.css)."""
    cls = 'sec-head sec-head--center' if center else 'sec-head'
    h2cls = 'h2 h2--sub mask' if tier == 'sub' else 'h2 mask'
    s = f'''<div class="{cls}">
      <div>
        <h2 class="{h2cls}"><span>{h2}</span></h2>'''
    if lead:
        s += f'\n        <p class="lead rv" style="--d:.1s;max-width:58ch;margin-top:12px">{lead}</p>'
    s += '\n      </div>'
    if link:
        href, label = link
        s += f'\n      <a class="arrow-link rv" href="{href}">{label} {ARROW}</a>'
    s += '\n    </div>'
    return s

def tiles(items, cols=3, contain=False):
    cls = {2: 'tiles tiles--2', 3: 'tiles', 4: 'tiles tiles--4'}[cols]
    out = [f'<div class="{cls} reveal-group">']
    for i, (img, alt, title, body, href) in enumerate(items):
        d = f' style="--d:{i*0.06:.2f}s"' if i else ''
        ic = ' tile-img--contain' if contain else ''
        link = f'\n        <a class="arrow-link" href="{href}">Learn more {ARROW}</a>' if href else ''
        out.append(f'''  <article class="tile rv"{d}>
    <div class="tile-img{ic} zoom"><img src="../assets/img/{img}" alt="{alt}" loading="lazy"></div>
    <div class="tile-b"><h3>{title}</h3><p>{body}</p>{link}</div>
  </article>''')
    out.append('</div>')
    return '\n'.join(out)

CTA = '''<!-- CTA -->
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="cta rv">
      <div>
        <h2 class="h2">Send us a photo. <span class="acc">Get a price today.</span></h2>
        <p>Free diagnostics at all three branches. Tell us the symptom and we will tell you what it takes to fix it.</p>
      </div>
      <div class="cta-btns">
        <a class="btn btn--wa" href="''' + WA + '''" target="_blank" rel="noopener">WhatsApp us</a>
        <a class="btn btn--ghost" href="contact.html">Book a repair</a>
      </div>
    </div>
  </div>
</section>

'''

def write(name, title, desc, body):
    html = HEAD.format(title=title, desc=desc, ver=VER) + HEADER + body + CTA + FOOTER
    open(name, 'w', encoding='utf-8').write(html)
    print('wrote', name, len(html), 'bytes')

# ============================================================ SERVICES
SERVICES = [
 ('ykl-work-1.jpg','Technician working on an open MacBook display','Screen replacement',
  'Cracked glass, flickering panels, dead pixels and backlight failure on MacBook, iMac and iPad.','mac-screen-repair.html'),
 ('ykl-work-4.jpg','Technician removing a MacBook battery','Battery replacement',
  'Swollen packs pushing the trackpad up, fast drain, or the Service Recommended warning in macOS.','mac-battery-replacement.html'),
 ('ykl-work-3.jpg','Technician inspecting a logic board under a microscope','Logic board repair',
  'Board-level fault finding, micro-soldering and BGA reballing for Macs that will not power on or boot.','mac-logicboard-repair.html'),
 ('ykl-work-2.jpg','Technician cleaning a Mac board at the bench','Water damage recovery',
  'Ultrasonic cleaning, corrosion treatment and component replacement after a spill. Bring it in fast.','mac-water-damage-repair.html'),
 ('ykl-work-5.jpg','Technician servicing a MacBook keyboard','Keyboard &amp; trackpad',
  'Sticky or repeating keys, dead rows, and trackpads that will not click or register gestures.',None),
 ('r-ram-chip.jpg','Memory module ready for a Mac upgrade','SSD &amp; RAM upgrade',
  'More storage and memory for older Intel Macs, with your data migrated across before you collect.',None),
 ('ykl-work-6.jpg','Technician running diagnostics on a MacBook','Speaker &amp; audio repair',
  'Crackling, muted or one-sided speakers, failed microphones and headphone jack faults.',None),
 ('r-iphone-mat.jpg','Charging port repair on the bench','Charging &amp; port repair',
  'MagSafe and USB-C ports that will not charge, loose connectors and charging IC faults.',None),
 ('ykl-work-7.jpg','Technician handling a tablet display','iPad &amp; iPhone repair',
  'Screens, batteries, charging ports, speakers, logic boards and water damage on iPad and iPhone.',None),
]

body = phero('Mac Repair', 'Every Apple repair, under one roof',
  'Screens, batteries, boards and spills. Diagnosed free at our own bench, quoted before anything is opened, and covered by up to 5 years warranty.',
  art='ykl-work-6.jpg', script='we open it,<br>we own it')
body += f'''
<section class="sec sec--band">
  <div class="wrap">
    {sec_head('what we fix', 'Mac repair services', 'Nine of the jobs we handle most. If your symptom is not listed, message us and describe it.')}
    {tiles(SERVICES, 3)}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head('common symptoms', 'Tell us what it is doing', 'Most people describe a symptom, not a part. That is exactly how we take it in.', tier='sub')}
    <div class="sym rv">
      <span>Will not turn on</span><span>Black screen but the fan runs</span><span>Battery swollen</span>
      <span>Trackpad will not click</span><span>Keys repeating</span><span>Spilled water or coffee</span>
      <span>Stuck on the Apple logo</span><span>Overheating and loud fans</span><span>No charge on MagSafe</span>
      <span>Screen flickering or lines</span><span>Storage full</span><span>Random shutdowns</span>
      <span>Crackling speakers</span><span>Wi-Fi keeps dropping</span><span>Very slow since the last update</span>
    </div>
  </div>
</section>

{PROCESS}'''
write('services.html', 'Mac Repair Services | YKL Mac Fix',
      'Screen, battery, logic board, water damage, keyboard, SSD and RAM repairs for Mac, iPad and iPhone in Petaling Jaya and Kuantan.', body)

# ============================================================ DEVICES
DEVICES = [
 ('macbook-air.png','MacBook Air','MacBook Air','macbook-air',
  'M1 through the latest M-series, plus the older Intel bodies. Screens, batteries, keyboards, boards and spills.'),
 ('macbook-float-cut.png','MacBook Pro','MacBook Pro','macbook-pro',
  '13&quot;, 14&quot;, 15&quot;, 16&quot; and the Touch Bar models. Display assemblies, flexgate, board-level faults and thermal work.'),
 ('imac-yellow-cut.png','iMac','iMac','imac',
  '21.5&quot;, 24&quot; and 27&quot;. Panel replacement, fusion drive and SSD upgrades, power supply and board repair.'),
 ('dev-macmini.png','Mac mini','Mac mini','mac-mini',
  'Will not power on after a surge, no display output, storage upgrades and port repair.'),
 ('ipad-hero.png','iPad','iPad','ipad',
  'iPad, Air, mini and Pro. Glass and digitiser, batteries, charging ports, speakers and water damage.'),
 ('dev-iphone.png','iPhone','iPhone','iphone',
  'Screens, batteries, charging ports, rear glass and motherboard-level repair including reball.'),
]
dev_tiles = []
for img, alt, title, anchor, body_txt in DEVICES:
    dev_tiles.append((img, alt, title, body_txt, 'contact.html'))

body = phero('Devices', 'Apple devices we repair',
  'Mac, iPad and iPhone. If it has an Apple logo on it, our bench has seen it before.',
  art='mac-lineup.png', script='every model,<br>every year')
body += f'''
<section class="sec sec--band">
  <div class="wrap">
    {sec_head('the full line-up', 'Pick your device', 'Every one of these is diagnosed free before we quote you.', tier='sub')}
    <div class="tiles reveal-group">'''
for i, (img, alt, title, anchor, txt) in enumerate(DEVICES):
    d = f' style="--d:{i*0.06:.2f}s"' if i else ''
    body += f'''
      <article class="tile rv" id="{anchor}"{d}>
        <div class="tile-img tile-img--contain zoom" style="background:#fff"><img src="../assets/img/{img}" alt="{alt}" loading="lazy"></div>
        <div class="tile-b"><h3>{title}</h3><p>{txt}</p>
          <a class="arrow-link" href="{WA}" target="_blank" rel="noopener">Get a free quote {ARROW}</a></div>
      </article>'''
body += f'''
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="split-media rv"><img src="../assets/img/ykl-work-3.jpg" alt="YKL technician working on a logic board under a microscope" loading="lazy"></div>
    <div class="split-copy">
      <p class="script rv" style="font-size:24px;color:var(--blue)">not a parts shop</p>
      <h2 class="h2 mask"><span>We repair boards, not just swap parts</span></h2>
      <p class="rv" style="--d:.1s">Plenty of shops will tell you a logic board is dead and quote you for a new one. We put it under the microscope first. Micro-soldering, component replacement and BGA reballing are done here, at our own bench, which is why Macs written off elsewhere often leave here working.</p>
      <ul class="ticks rv" style="--d:.16s">
        <li>Board-level diagnosis on every no-power case</li>
        <li>Original-grade parts, with the warranty stated on your invoice</li>
        <li>Full function test before you collect</li>
      </ul>
      <a class="btn rv" style="--d:.22s" href="mac-logicboard-repair.html">About logic board repair</a>
    </div>
  </div>
</section>
'''
write('devices.html', 'Apple Devices We Repair | YKL Mac Fix',
      'MacBook Air, MacBook Pro, iMac, Mac mini, iPad and iPhone repair in Petaling Jaya and Kuantan. Free diagnostics, up to 5 years warranty.', body)

# ============================================================ ABOUT
TEAM = [
 ('ykl-team-chris.jpg','Chris','Senior technician'),
 ('ykl-team-shahid.jpg','Shahid','Board-level specialist'),
 ('ykl-team-huang.jpg','Huang','Mac technician'),
 ('ykl-team-ah-wei.jpg','Ah Wei','Mac technician'),
 ('ykl-team-terence.jpg','Terence','Diagnostics'),
 ('ykl-team-ah-hong.jpg','Ah Hong','Workshop lead'),
 ('ykl-team-han.jpg','Han','Front of house'),
]
team_html = '<div class="team-grid reveal-group">'
for i,(img,name,role) in enumerate(TEAM):
    d = f' style="--d:{i*0.05:.2f}s"' if i else ''
    team_html += f'''
      <div class="team-card rv"{d}><div class="ph"><img src="../assets/img/{img}" alt="{name}, {role} at YKL Mac Fix" loading="lazy"></div><b>{name}</b><small>{role}</small></div>'''
team_html += '\n    </div>'

STORES = [
 ('ykl-store-6.jpg','YKL Mac Fix entrance','Petaling Jaya','Our head office and main workshop, on the 3rd and 4th floor in Section 14.',None),
 ('ykl-store-1.jpg','Parts store at YKL Mac Fix','Our parts store','Screens, batteries, flex cables and board components kept in stock so most jobs do not wait on an order.',None),
 ('ykl-store-3.jpg','The YKL Mac Fix service counter','The service counter','Bring your Mac in, describe the symptom and we take it from there. No appointment needed.',None),
]

body = phero('About Us', 'Mac specialists, not a general phone shop',
  'Three branches, one bench standard. We diagnose free, quote before we open anything, and back selected repairs with up to 5 years warranty.',
  art='ykl-work-8.jpg', script='three branches,<br>one standard')
body += f'''
<section class="sec sec--band">
  <div class="wrap">
    <div class="rows reveal-group" id="stats">
      <div class="rows-i rv"><span class="rows-n n" data-count="1190" data-suffix="+">0</span><div class="rows-b"><b>Google reviews</b><span>Rated Excellent by customers across all three branches.</span></div></div>
      <div class="rows-i rv" style="--d:.06s"><span class="rows-n n" data-count="1000000" data-suffix="+">0</span><div class="rows-b"><b>Views on TikTok</b><span>People watch us take Macs apart at <a href="https://www.tiktok.com/@yklmacfix" target="_blank" rel="noopener">@yklmacfix</a>.</span></div></div>
      <div class="rows-i rv" style="--d:.12s"><span class="rows-n n" data-count="3" data-suffix="">0</span><div class="rows-b"><b>Branches in Malaysia</b><span>Petaling Jaya and two in Kuantan, all with the same bench standard.</span></div></div>
      <div class="rows-i rv" style="--d:.18s"><span class="rows-n n" data-count="5" data-suffix="">0</span><div class="rows-b"><b>Years of warranty, up to</b><span>On selected repairs and upgrades, stated on your invoice.</span></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split split--flip">
    <div class="split-media rv"><img src="../assets/img/ykl-work-2.jpg" alt="YKL Mac Fix technician at the repair bench" loading="lazy"></div>
    <div class="split-copy">
      <p class="script rv" style="font-size:24px;color:var(--blue)">who we are</p>
      <h2 class="h2 mask"><span>YKL One Hour Service Trading</span></h2>
      <p class="rv" style="--d:.1s">YKL Mac Fix started as a walk-in repair counter and grew into three branches across Petaling Jaya and Kuantan. We chose to specialise. Everything on our bench is an Apple device, which means our technicians see the same faults often enough to recognise them quickly.</p>
      <p class="rv" style="--d:.14s">That is also why we can repair at board level instead of reselling you a machine. More than 1,190 Google reviews and a million views on TikTok come from people watching us do exactly that.</p>
      <ul class="ticks rv" style="--d:.2s">
        <li>Free diagnostics on every device, walk-in or sent to us</li>
        <li>A written quote before anything is opened</li>
        <li>Up to 5 years warranty on selected repairs and upgrades</li>
        <li>Interest-free instalments with SPay Later</li>
      </ul>
    </div>
  </div>
</section>

<section class="sec sec--band2">
  <div class="wrap">
    {sec_head('the people on the bench', 'Meet the team', 'The same faces you will hand your Mac to.', tier='sub')}
    {team_html}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head('inside the shop', 'Our workshop', tier='sub')}
    {tiles(STORES, 3)}
  </div>
</section>

{PROCESS}'''
write('about.html', 'About YKL Mac Fix | Apple Repair Specialists in Malaysia',
      'YKL One Hour Service Trading, trading as YKL Mac Fix. Three branches, board-level Apple repair, free diagnostics and up to 5 years warranty.', body)

# ============================================================ CONTACT
BRANCHES = [
 ('pj','Petaling Jaya (HQ)','ykl-store-3.jpg','No 16, 3rd &amp; 4th Floor, Jalan 14/20, Section 14, 46100 Petaling Jaya, Selangor',
  'Mon&ndash;Fri 10:30am&ndash;7:30pm &middot; Sat&ndash;Sun 10:30am&ndash;6:00pm','+60 3-7495 9092','+60374959092','60374959092'),
 ('pandan-damai','Kuantan @ Pandan Damai','ykl-store-2.jpg','No A3, Jalan Pandan Damai 2/2, Perumahan Pandan Damai, 25150 Kuantan, Pahang',
  'Mon&ndash;Sat 11:00am&ndash;9:00pm','+60 19-987 3386','+60199873386','60199873386'),
 ('kuantan-parade','Kuantan Parade','ykl-store-5.jpg','Lot F22, 1st Floor, Kuantan Parade, Jalan Haji Abdul Rahman, 25000 Kuantan, Pahang',
  'Mon&ndash;Sat 11:00am&ndash;9:00pm','+60 11-2625 6581','+601126256581','601126256581'),
]
CLOCK = '<svg viewBox="0 0 24 24" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" stroke-linecap="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
PIN = '<svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'

branch_cards = '<div class="tiles reveal-group">'
for i,(anchor,name,img,addr,hours,tel_disp,tel,wa) in enumerate(BRANCHES):
    d = f' style="--d:{i*0.07:.2f}s"' if i else ''
    q = re.sub(r'&amp;|&ndash;|&middot;','',addr).replace(' ','+')
    branch_cards += f'''
      <article class="tile rv" id="{anchor}"{d}>
        <div class="tile-img zoom"><img src="../assets/img/{img}" alt="{name} branch" loading="lazy"></div>
        <div class="tile-b">
          <h3>{name}</h3>
          <p class="loc-row">{PIN}<span>{addr}</span></p>
          <p class="loc-row">{CLOCK}<span>{hours}</span></p>
          <p class="loc-row">{PHONE}<a href="tel:{tel}">{tel_disp}</a></p>
          <div style="display:flex;gap:9px;flex-wrap:wrap;margin-top:12px">
            <a class="btn btn--wa" href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp</a>
            <a class="btn btn--line" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">Directions</a>
          </div>
        </div>
      </article>'''
branch_cards += '\n    </div>'

body = phero('Contact', 'Talk to us about your Mac',
  'Message us on WhatsApp with a photo of the problem, call the branch nearest you, or fill in the form and we will come back to you.',
  plain=True, cta=False)
body += f'''
<section class="sec sec--band">
  <div class="wrap rich">
    <div>
      <p class="script rv" style="font-size:24px;color:var(--blue)">tell us what happened</p>
      <h2 class="h2 mask" style="margin-bottom:18px"><span>Book a repair</span></h2>
      <form class="form rv" id="bookForm" novalidate>
        <div class="fgrid">
          <div class="f"><label for="n">Your name</label><input id="n" name="name" type="text" required placeholder="Full name"></div>
          <div class="f"><label for="p">Phone / WhatsApp</label><input id="p" name="phone" type="tel" required placeholder="01x xxx xxxx"></div>
          <div class="f"><label for="e">Email</label><input id="e" name="email" type="email" placeholder="you@example.com"></div>
          <div class="f"><label for="d">Device</label>
            <select id="d" name="device">
              <option>MacBook Air</option><option>MacBook Pro</option><option>iMac</option>
              <option>Mac mini</option><option>Mac Pro</option><option>iPad</option><option>iPhone</option><option>Something else</option>
            </select></div>
          <div class="f"><label for="b">Branch</label>
            <select id="b" name="branch">
              <option>Petaling Jaya (HQ)</option><option>Kuantan @ Pandan Damai</option><option>Kuantan Parade</option><option>Arrange a pickup</option>
            </select></div>
          <div class="f"><label for="s">Service needed</label>
            <select id="s" name="service">
              <option>Screen replacement</option><option>Battery replacement</option><option>Logic board repair</option>
              <option>Water damage recovery</option><option>Keyboard or trackpad</option><option>SSD or RAM upgrade</option><option>Not sure yet</option>
            </select></div>
          <div class="f f--full"><label for="m">What is it doing?</label><textarea id="m" name="message" placeholder="Describe the symptom in your own words. When did it start?"></textarea></div>
        </div>
        <button class="btn" type="submit">Send my request</button>
        <p class="fnote">This is a demo form on a mockup. Nothing is sent yet.</p>
        <div class="fdone" id="formDone">Thanks. In the live version this would reach the branch you picked. For now, message us on WhatsApp and we will reply today.</div>
      </form>
    </div>
    <aside class="aside">
      <div class="abox abox--dark rv">
        <h4>Fastest way to a price</h4>
        <p>Send a photo of the device and describe the fault. You usually get an answer the same day.</p>
        <a class="btn btn--wa" href="{WA}" target="_blank" rel="noopener">WhatsApp the workshop</a>
      </div>
      <div class="abox rv" style="--d:.08s">
        <h4>Good to know</h4>
        <ul>
          <li><b>Free</b><span>diagnostics on every device</span></li>
          <li><b>Quote first</b><span>nothing is opened until you approve</span></li>
          <li><b>Up to 5 years</b><span>warranty on selected repairs</span></li>
          <li><b>Free pickup</b><span>Klang Valley, jobs above RM500</span></li>
          <li><b>SPay Later</b><span>interest-free instalments</span></li>
        </ul>
      </div>
    </aside>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head('three branches', 'Where to find us', 'Walk in during opening hours. No appointment needed.', tier='sub')}
    {branch_cards}
  </div>
</section>
'''
write('contact.html', 'Contact &amp; Locations | YKL Mac Fix',
      'Three YKL Mac Fix branches: Petaling Jaya HQ, Kuantan @ Pandan Damai and Kuantan Parade. Phone numbers, opening hours and a booking form.', body)

# ============================================================ BLOG
POSTS = [
 ('blog-professional-mac-repair.html','ykl-work-3.jpg','Why board-level repair beats a replacement quote',
  'Guides','8 min read','A dead logic board is not the end of a Mac. Here is what actually happens on our bench when a machine will not power on.'),
 ('blog-mac-battery-health.html','ykl-work-4.jpg','Service Recommended: what your Mac battery is telling you',
  'Maintenance','5 min read','macOS warns you long before the battery swells. What the warning means, and how long you can safely leave it.'),
 ('blog-water-damage-first-hour.html','ykl-work-2.jpg','Spilled on your MacBook? The first hour matters most',
  'Emergency','4 min read','What to do, what never to do, and why rice is the worst advice on the internet.'),
]
post_html = '<div class="post-grid reveal-group">'
for i,(href,img,title,cat,read,ex) in enumerate(POSTS):
    d = f' style="--d:{i*0.07:.2f}s"' if i else ''
    post_html += f'''
      <a class="post rv" href="{href}"{d}>
        <div class="ph zoom"><img src="../assets/img/{img}" alt="{title}" loading="lazy"></div>
        <div class="post-b"><p class="meta">{cat} &middot; {read}</p><h3>{title}</h3><p>{ex}</p>
        <span class="arrow-link">Read article {ARROW}</span></div>
      </a>'''
post_html += '\n    </div>'

body = phero('Blog', 'Notes from the bench',
  'Plain-English guides to the faults we see every week, written by the people who repair them.',
  plain=True, cta=False)
body += f'''
<section class="sec sec--band">
  <div class="wrap">
    {sec_head('latest', 'Articles', tier='sub')}
    {post_html}
  </div>
</section>
'''
write('blog.html', 'Mac Repair Guides &amp; Advice | YKL Mac Fix Blog',
      'Guides on Mac battery health, water damage, logic board repair and keeping your Apple devices alive longer.', body)

print('done')
