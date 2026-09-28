#!/usr/bin/env python3
"""Round-2 pages: the five remaining service pages, and six area landing pages.
Reuses the helpers in _build.py / _build2.py. Run after both of those."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
g = {'__file__': os.path.join(HERE, '_build2.py')}
exec(open('_build2.py', encoding='utf-8').read(), g)
phero, sec_head, tiles, write = g['phero'], g['sec_head'], g['tiles'], g['write']
PROCESS, WA, ARROW, PLUS = g['PROCESS'], g['WA'], g['ARROW'], g['PLUS']
detail, aside_block = g['detail'], g['aside_block']

# ---------------------------------------------------------------- 5 service pages
detail('mac-keyboard-trackpad-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Keyboard &amp; trackpad',
 'MacBook keyboard and trackpad repair',
 'Sticky keys, letters that repeat themselves, a dead row, or a trackpad that has stopped clicking. All of it is fixable, and the diagnosis is free.',
 'ykl-work-5.jpg', 'keys that<br>actually work',
 ['Keys repeating themselves','A key or a whole row is dead','Sticky or mushy keys','Trackpad will not click',
  'Trackpad clicks on its own','Cursor jumping while typing','Keyboard backlight out','Caps Lock stuck on'],
 """<h2>Two faults that look like one</h2>
<p>A trackpad that has stopped clicking is usually not the trackpad. On most MacBooks the battery sits directly underneath it, and when that battery swells it presses upward until the click mechanism has nowhere left to travel. Replacing the trackpad on a machine with a swollen battery fixes nothing and the fault returns within weeks.</p>
<p>So we check the battery first on every trackpad job. If it is swollen, that is the repair, and it is usually cheaper than the part you came in expecting to buy.</p>
<h2>Keyboards</h2>
<p>Repeating characters, dead keys and sticky travel are the classic symptoms of the butterfly mechanism used on several MacBook generations, where a fragment of dust under a key is enough to stop it registering. On newer scissor-switch models the usual causes are liquid, a failed flex cable, or wear on a single switch.</p>
<ul class="ticks">
  <li>Individual key and keycap replacement where the mechanism is intact</li>
  <li>Full top-case keyboard replacement where it is not</li>
  <li>Backlight and flex cable repair</li>
  <li>Trackpad replacement, recalibration and Force Touch testing</li>
</ul>
<h2>If liquid got in</h2>
<p>A keyboard that started misbehaving after a spill is a liquid damage job, not a keyboard job. The keys are simply the first thing you notice. Bring it in quickly and read <a href="mac-water-damage-repair.html">what we do with a liquid-damaged Mac</a>, because the board underneath keeps corroding while the machine sits.</p>
<h2>How long it takes</h2>
<p>Single keys and trackpads are usually same-day. A full top-case replacement depends on the model and whether the part is in stock, and you get that timeline with the quote.</p>""",
 'MacBook Keyboard &amp; Trackpad Repair in PJ and Kuantan | YKL Mac Fix',
 'Sticky keys, repeating characters, dead rows and trackpads that will not click. Free diagnostics, most jobs same-day, up to 5 years warranty.',
 faq=[('My trackpad will not click. Is that the trackpad?','Usually not. On most MacBooks the battery sits under the trackpad, and a swollen battery presses on it until it cannot click. We check the battery first, and that is often the whole repair.'),
      ('Can you replace just one key?','Where the mechanism under the key is intact, yes. If the mechanism itself has failed, the key is part of the top case and that is a larger job. The free diagnosis tells us which.'),
      ('My keyboard went strange after a spill. Is that a keyboard repair?','No, treat it as liquid damage. The keys are just what you noticed first. Bring it in the same day if you can, because the board keeps corroding.')])

detail('mac-ssd-ram-upgrade.html',
 '<a href="services.html">Mac Repair</a><span>/</span>SSD &amp; RAM upgrade',
 'Mac SSD and RAM upgrades',
 'More storage and more memory for Macs that still have years left in them. Your data is migrated across before you collect the machine.',
 'r-ram-chip.jpg', 'faster than<br>buying new',
 ['Startup disk is almost full','Beachball on everything','Slow since the last macOS update','Cannot install updates',
  'Too many apps open is a problem','Photos library will not fit','Slow to boot','Swap file thrashing'],
 """<h2>What can actually be upgraded</h2>
<p>This is the first thing to establish, and it depends entirely on your model. Older Intel Macs often have socketed memory and a removable drive, and those are straightforward. From a certain generation onward Apple soldered both to the logic board, and on those machines no upgrade is possible at any price.</p>
<p>We will tell you which camp your Mac is in during the free diagnosis, before you spend anything. If it cannot be upgraded we will say so rather than sell you something else.</p>
<ul class="ticks">
  <li>SSD replacement and capacity upgrades on models with removable storage</li>
  <li>Memory upgrades on models with socketed RAM</li>
  <li>Fusion Drive to solid-state conversion on older iMacs</li>
  <li>Full data migration, so the machine comes back set up the way you left it</li>
</ul>
<h2>Why a slow Mac is often a storage problem</h2>
<p>macOS needs free space to work. When the startup disk fills up it starts writing swap to a drive that has nowhere left to write, and everything stalls. On an older iMac still running a mechanical Fusion Drive, moving to solid-state is the single biggest change you can make, and it costs a fraction of a new machine.</p>
<h2>Your data</h2>
<p>We clone the existing drive across, so you get the same desktop, the same apps and the same files. Back up first anyway if the machine still boots. If it does not boot, tell us at drop-off that the data matters and we will treat recovery as the priority.</p>
<h2>How long it takes</h2>
<p>Most upgrades are done within a working day. The variable is the migration: a nearly-full 2TB drive takes considerably longer to copy than a half-empty 256GB one, and we would rather it copied properly than quickly.</p>""",
 'Mac SSD &amp; RAM Upgrades in PJ and Kuantan | YKL Mac Fix',
 'Storage and memory upgrades for MacBook, iMac and Mac mini, with full data migration. Free diagnostics before you spend anything.',
 faq=[('Can every Mac be upgraded?','No. Newer Macs have storage and memory soldered to the logic board and cannot be changed. We check your exact model during the free diagnosis and tell you before you commit to anything.'),
      ('Will I lose my files?','No. We clone your existing drive across so the machine comes back as you left it. Back up first as a habit, and tell us if the data is the priority.'),
      ('My Mac is slow. Will more RAM fix it?','Sometimes, but a full startup disk is the more common cause. We test which one is actually holding your machine back rather than guessing.')])

detail('mac-speaker-audio-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Speaker &amp; audio',
 'Mac speaker and audio repair',
 'Crackling, muted or one-sided sound, microphones nobody can hear, and headphone jacks that only work if you hold the plug at an angle.',
 'ykl-work-6.jpg', 'sound, sorted',
 ['Crackling or distorted sound','Only one speaker works','No sound at all','Microphone not picking up',
  'Headphone jack is intermittent','Sound cuts out at volume','Rattle from the speaker grille','Stuck in headphone mode'],
 """<h2>Blown, or just wet</h2>
<p>Most failed Mac speakers were not played too loud. They were damaged by liquid, which corrodes the coil, or by a battery swelling against the speaker enclosure, which is why a distorted speaker sometimes arrives alongside a trackpad that will not click. Both are worth catching early.</p>
<p>Distortion that appears only above a certain volume usually means the driver itself. Distortion at every volume more often points at the audio circuitry on the board.</p>
<ul class="ticks">
  <li>Speaker replacement, left and right, on MacBook, iMac and iPad</li>
  <li>Microphone replacement and array testing</li>
  <li>Headphone jack repair, including the stuck-in-headphone-mode fault</li>
  <li>Board-level repair of the audio circuit where the speakers themselves are fine</li>
</ul>
<h2>Stuck in headphone mode</h2>
<p>If your Mac behaves as though headphones are plugged in when they are not, the switch inside the jack has usually failed or a fragment of debris is holding it open. It is a small repair and there is no reason to live with it.</p>
<h2>Before you book</h2>
<p>Try another audio source and check the output device in System Settings first. Software accounts for a fair share of the audio faults people bring in, and if that is all it is we will tell you and send you home without a bill.</p>""",
 'Mac Speaker, Microphone &amp; Audio Repair | YKL Mac Fix',
 'Crackling, muted or one-sided Mac speakers, failed microphones and headphone jack faults. Free diagnostics in Petaling Jaya and Kuantan.',
 faq=[('One speaker stopped working. Do both need replacing?','Not necessarily. We test each channel and replace what has actually failed. On some models the pair is a single assembly, and we will tell you if yours is one of them.'),
      ('My Mac thinks headphones are plugged in.','The switch inside the jack has failed or something is holding it open. It is a small repair, usually same-day.'),
      ('Could this be a software problem?','Often, yes. Check your output device in System Settings first. If that is all it is, we will say so and there is nothing to pay.')])

detail('mac-charging-port-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Charging &amp; ports',
 'Mac charging and port repair',
 'MagSafe and USB-C ports that will not charge, connectors that only work at an angle, and Macs that charge from one port but not another.',
 'r-iphone-mat.jpg', 'charge it<br>properly',
 ['Will not charge at all','Charges only at a certain angle','One port works, another does not','Charger gets very hot',
  'Charging light will not come on','Drops charge while plugged in','Port feels loose','No data over USB-C'],
 """<h2>Rule out the cheap causes first</h2>
<p>Before anything is opened we test with a known-good charger and cable, and we clean the port. A surprising number of will-not-charge Macs are a failed cable or a port packed with pocket lint, and neither is worth paying a repair bill for. If that is your fault, you will be told so.</p>
<h2>When it is the port</h2>
<p>A connector that only works at an angle has worn or cracked solder joints where it meets the board. That is a micro-soldering repair, not a part swap, and doing it properly means reflowing or replacing the connector rather than bending something back into place.</p>
<ul class="ticks">
  <li>MagSafe and USB-C connector replacement and reflow</li>
  <li>Charging IC and power circuit repair at board level</li>
  <li>Port cleaning and pin repair</li>
  <li>Data-line repair where a port charges but will not transfer</li>
</ul>
<h2>When it is the board</h2>
<p>If no port charges, the fault is usually further in: the charging controller, a blown fuse, or the power management circuit. That is <a href="mac-logicboard-repair.html">board-level work</a>, which we do here rather than sending it away, and it is why a Mac written off elsewhere as a charging fault often leaves here working.</p>
<h2>A note on chargers</h2>
<p>Cheap third-party chargers are behind a real share of the charging-circuit damage we see. If yours runs very hot or the cable has been repaired with tape, replace it before it takes the board with it.</p>""",
 'MacBook Charging Port &amp; MagSafe Repair | YKL Mac Fix',
 'MagSafe and USB-C ports that will not charge, loose connectors and charging circuit faults, repaired at board level. Free diagnostics.',
 faq=[('My Mac will not charge. Is it the port or the charger?','We test with a known-good charger and cable and clean the port before anything else. Often that is the whole answer, and there is nothing to pay.'),
      ('It only charges if I hold the cable at an angle.','The connector has worn or cracked solder joints where it meets the board. That is a micro-soldering repair and it is worth doing before it stops charging entirely.'),
      ('Can a cheap charger damage my Mac?','Yes, and it is behind a real share of the charging-circuit damage we see. If yours runs very hot, replace it.')])

detail('ipad-iphone-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>iPad &amp; iPhone',
 'iPad and iPhone repair',
 'The same bench, the same microscope and the same free diagnosis we give a Mac. Screens, batteries, charging ports, speakers and board-level work.',
 'ykl-work-7.jpg', 'small screens,<br>same standard',
 ['Cracked glass','Touch not responding in places','Battery drains by lunchtime','Will not charge',
  'No sound on calls','Stuck on the Apple logo','Water damage','Face ID stopped working'],
 """<h2>iPad</h2>
<p>On most iPads the glass and the digitiser are one part and the LCD underneath is another. If the LCD survived the drop we replace the glass only, which costs less. The free diagnosis is what tells us which, and it is worth having before you assume the worst.</p>
<ul class="ticks">
  <li>Glass and digitiser replacement, with LCD replacement where needed</li>
  <li>Battery replacement on iPad, Air, mini and Pro</li>
  <li>Charging port and connector repair</li>
  <li>Speaker, microphone and button repair</li>
  <li>Liquid damage recovery and board-level repair</li>
</ul>
<h2>iPhone</h2>
<p>Screens and batteries are the everyday jobs and most are same-day. Beyond those we do the work many shops send away: charging circuits, audio ICs, and reballing chips that have lost contact with the board.</p>
<h2>What to expect on Face ID and True Tone</h2>
<p>Some components on an iPhone are paired to the specific device at the factory. Where a repair affects one of those we will explain exactly what will and will not still work before you agree to anything, rather than after you collect it. That conversation happens at the quote, every time.</p>
<h2>Back up first</h2>
<p>If the device still powers on, back it up before you bring it in. Screen and battery work does not touch your data, but a backup costs you nothing and removes the only real risk in the whole process.</p>""",
 'iPad &amp; iPhone Repair in Petaling Jaya and Kuantan | YKL Mac Fix',
 'Screens, batteries, charging ports, speakers and board-level repair for iPad and iPhone. Free diagnostics, most jobs same-day.',
 faq=[('Can you replace just the glass on my iPad?','Often yes. If the LCD underneath is undamaged we replace the glass and digitiser only, which costs less. The free diagnosis confirms it.'),
      ('Will Face ID still work after a screen repair?','Some components are paired to the device at the factory. We explain exactly what will and will not still work before you agree to the repair, not after.'),
      ('Do you repair iPhones at board level?','Yes. Charging circuits, audio ICs and chip reballing are done here, which is work many shops send away.')])

print('five service pages written')

# ---------------------------------------------------------------- area landing pages
# NOTE: YKL has three branches (Petaling Jaya HQ + two in Kuantan). The other five
# areas below are SERVICE AREAS reached from the PJ workshop, not shopfronts, and the
# copy must never imply otherwise. See CONTENT-NOTES.md.
SERVICE_LINKS = [
    ('mac-screen-repair.html', 'Mac screen repair', 'Cracked glass, flickering panels and dead backlights on MacBook, iMac and iPad.'),
    ('mac-battery-replacement.html', 'MacBook Pro battery replacement', 'Swollen packs, fast drain and the Service Recommended warning in macOS.'),
    ('mac-logicboard-repair.html', 'Logic board repair', 'Board-level diagnosis, micro-soldering and reballing for Macs that will not power on.'),
    ('mac-water-damage-repair.html', 'Water damage recovery', 'Ultrasonic cleaning and corrosion treatment after a spill.'),
    ('mac-keyboard-trackpad-repair.html', 'Keyboard and trackpad repair', 'Sticky keys, repeating characters and trackpads that will not click.'),
    ('mac-ssd-ram-upgrade.html', 'SSD and RAM upgrades', 'More storage and memory for older Macs, with your data migrated across.'),
]

AREAS = [
    dict(art='ykl-work-1.jpg', slug='bangsar-south', name='Bangsar South', where='Kuala Lumpur',
         geo='Bangsar South sits just off the Federal Highway in Kerinchi, which puts it a short drive from our Section 14 workshop in Petaling Jaya.',
         branch=False),
    dict(art='ykl-work-6.jpg', slug='petaling-jaya', name='Petaling Jaya', where='Selangor',
         geo='This is where our head office and main workshop are. Walk in at No 16, 3rd &amp; 4th Floor, Jalan 14/20, Section 14, and hand the machine straight to the technician who will work on it.',
         branch=True),
    dict(art='ykl-work-4.jpg', slug='mont-kiara', name='Mont Kiara', where='Kuala Lumpur',
         geo='Mont Kiara is in north-west Kuala Lumpur, a straightforward run down to our Section 14 workshop in Petaling Jaya.',
         branch=False),
    dict(art='ykl-work-3.jpg', slug='kuala-lumpur', name='Kuala Lumpur', where='Malaysia',
         geo='We cover the whole of Kuala Lumpur from our workshop in Section 14, Petaling Jaya, which is minutes from the city boundary.',
         branch=False),
    dict(art='ykl-work-5.jpg', slug='publika', name='Publika', where='Solaris Dutamas, Kuala Lumpur',
         geo='Publika sits in Solaris Dutamas next to Mont Kiara. Our workshop is in Section 14, Petaling Jaya, an easy drive across.',
         branch=False),
    dict(art='ykl-work-2.jpg', slug='ampang', name='Ampang', where='Kuala Lumpur',
         geo='Ampang is east of the city centre. It is the far side of the Klang Valley from our Section 14 workshop, which is exactly what the free pickup is for.',
         branch=False),
]

def location(a):
    name, slug, where, geo = a['name'], a['slug'], a['where'], a['geo']
    fname = f'apple-repair-{slug}.html'
    lead = (f'Free diagnostics, a quote before anything is opened, and up to 5 years warranty. '
            f'Mac, iPad and iPhone repair for {name} and the rest of the Klang Valley.')
    b = phero(f'{name}', f'Apple repair in {name}', lead,
              art=a['art'], script='free pickup,<br>free diagnosis')

    svc = ''.join(
        f'''
      <article class="tile rv">
        <div class="tile-b" style="padding:0">
          <h3><a href="{href}">{title}</a></h3>
          <p>{desc}</p>
          <a class="arrow-link" href="{href}">Learn more {ARROW}</a>
        </div>
      </article>''' for href, title, desc in SERVICE_LINKS)

    if a['branch']:
        how = f'''<h2>Walk in, or send it to us</h2>
<p>{geo} No appointment is needed. Bring the device in during opening hours, describe what it is doing, and we will diagnose it free before quoting you.</p>
<p>If you would rather not make the trip, pickup is free across the Klang Valley on jobs above RM500. Message us a photo of the problem on WhatsApp and we will arrange it.</p>'''
    else:
        how = f'''<h2>How {name} customers reach us</h2>
<p>We do not have a shopfront in {name}. Our workshop is in Section 14, Petaling Jaya, and there are two ways to get your device onto that bench.</p>
<p>{geo} You are welcome to walk in during opening hours, no appointment needed. Or use the free pickup: it covers the whole Klang Valley on jobs above RM500, so send us a photo of the problem on WhatsApp and we will collect the device and bring it back to you.</p>'''

    body = b + f'''
<section class="sec sec--airy sec--band">
  <div class="wrap rich">
    <div class="prose rv">
      <h2>Looking for Apple repair near you in {name}?</h2>
      <p>YKL Mac Fix is a specialist Apple repair workshop serving {name}, {where} and the wider Klang Valley. Every device on our bench is an Apple device, which is why we recognise the same faults quickly instead of working them out from scratch.</p>
      <p>If you have been searching for MacBook repair near me, mac repair near me or apple repair near me and getting quotes that read like a price for a new machine, get a second opinion here first. The diagnosis costs nothing and the price is agreed before anything is opened.</p>
      {how}
      <h2>What we repair</h2>
      <p>Mac screen repair and MacBook screen repair, MacBook Pro battery replacement, logic board and water damage work, keyboards, trackpads, speakers, charging ports, and storage and memory upgrades. MacBook Air, MacBook Pro, iMac, Mac mini, Mac Pro, iPad and iPhone.</p>
      <p>Board-level repair is done in-house at our own bench, with micro-soldering and reballing under a stereo microscope. That is the reason Macs written off elsewhere often leave here working.</p>
      <h2>Why people in {name} use us</h2>
      <ul class="ticks">
        <li>Free diagnostics on every device, walk-in or collected</li>
        <li>A written quote before anything is opened</li>
        <li>Same-day service on most screen and battery jobs</li>
        <li>Up to 5 years warranty on selected repairs and upgrades</li>
        <li>Free pickup across the Klang Valley on jobs above RM500</li>
        <li>Interest-free instalments with SPay Later</li>
        <li>1,190+ Google reviews, rated Excellent</li>
      </ul>
    </div>
    {aside_block()}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head('what we fix', f'Mac repair services for {name}', 'Every one of these is diagnosed free before we quote you.', tier='sub')}
    <div class="tiles reveal-group" style="border-top:0;padding-top:0">{svc}
    </div>
  </div>
</section>

<section class="sec sec--tight sec--band2">
  <div class="wrap">
    {sec_head('good to know', f'Apple repair in {name}: questions', center=True, tier='sub')}
    <div class="faq rv">
      <div class="faq-i"><button class="faq-q">Where is the nearest Mac repair to {name}?{PLUS}</button><div class="faq-a"><p>Our workshop is at No 16, 3rd &amp; 4th Floor, Jalan 14/20, Section 14, 46100 Petaling Jaya. {geo}</p></div></div>
      <div class="faq-i"><button class="faq-q">Do you collect from {name}?{PLUS}</button><div class="faq-a"><p>Yes. Pickup is free across the Klang Valley on jobs above RM500. Send us a photo of the problem on WhatsApp with your location and we will arrange a time.</p></div></div>
      <div class="faq-i"><button class="faq-q">How much does a diagnosis cost?{PLUS}</button><div class="faq-a"><p>Nothing. We test the device, find the actual fault and give you a price. Nothing is opened until you approve the quote.</p></div></div>
      <div class="faq-i"><button class="faq-q">Can you do a MacBook Pro battery replacement the same day?{PLUS}</button><div class="faq-a"><p>Most MacBook Air and MacBook Pro batteries are replaced the same day. Older models where the pack is glued into the top case take longer, and you get the timeline with your quote.</p></div></div>
      <div class="faq-i"><button class="faq-q">Is macbook repair in Malaysia covered by a warranty here?{PLUS}</button><div class="faq-a"><p>Selected repairs and upgrades carry up to 5 years of warranty on the work and the parts we fitted. The exact term for your job is stated on your invoice.</p></div></div>
      <div class="faq-i"><button class="faq-q">Another shop said my Mac cannot be repaired. Can you check?{PLUS}</button><div class="faq-a"><p>Yes, and it costs nothing to look. Board-level repair is a different skill set from swapping parts, so a board written off elsewhere is often repairable here.</p></div></div>
    </div>
  </div>
</section>
'''
    write(fname,
          f'Apple Repair in {name} | MacBook &amp; Mac Repair Near You | YKL Mac Fix',
          f'Apple repair in {name}, {where}. MacBook, iMac, iPad and iPhone screen repair, battery replacement and board-level work. Free diagnostics and free Klang Valley pickup.',
          body)

for a in AREAS:
    location(a)
print('six area pages written')
