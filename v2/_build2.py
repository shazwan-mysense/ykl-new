#!/usr/bin/env python3
"""Service detail + blog article pages. Reuses helpers from _build.py."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
g = {'__file__': os.path.join(HERE, '_build.py')}
exec(open('_build.py', encoding='utf-8').read(), g)
phero, sec_head, tiles, write, PROCESS, WA, ARROW = (
    g['phero'], g['sec_head'], g['tiles'], g['write'], g['PROCESS'], g['WA'], g['ARROW'])

def aside_block():
    return """<aside class="aside">
      <div class="abox abox--dark rv">
        <h4>Free diagnosis, then a price</h4>
        <p>Send a photo and describe the fault. Most quotes come back the same day.</p>
        <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">WhatsApp us</a>
      </div>
      <div class="abox rv" style="--d:.08s">
        <h4>What is included</h4>
        <ul>
          <li><b>Free</b><span>diagnostics and quote</span></li>
          <li><b>In-house</b><span>repaired at our own bench</span></li>
          <li><b>Up to 5 years</b><span>warranty on selected repairs</span></li>
          <li><b>Tested</b><span>full function check before collection</span></li>
        </ul>
      </div>
      <div class="abox rv" style="--d:.16s">
        <h4>Other repairs</h4>
        <ul style="gap:11px">
          <li><a href="mac-screen-repair.html">Screen replacement</a></li>
          <li><a href="mac-battery-replacement.html">Battery replacement</a></li>
          <li><a href="mac-logicboard-repair.html">Logic board repair</a></li>
          <li><a href="mac-water-damage-repair.html">Water damage recovery</a></li>
          <li><a href="services.html">All services</a></li>
        </ul>
      </div>
    </aside>""" % WA

PLUS = '<svg viewBox="0 0 24 24" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'

def detail(fname, crumb, h1, lead, art, script, symptoms, prose, title, desc, faq=None):
    b = phero(crumb, h1, lead, art=art, script=script)
    if symptoms:
        chips = ''.join('<span>%s</span>' % s for s in symptoms)
        b += '\n<section class="sec sec--tight" style="padding-bottom:0">\n  <div class="wrap">\n    ' \
             + sec_head('sound familiar?', 'Symptoms we see most', center=True, tier='sub') \
             + '\n    <div class="sym rv" style="justify-content:center">' + chips + '</div>\n  </div>\n</section>\n'
    b += '\n<section class="sec sec--airy sec--band">\n  <div class="wrap rich">\n    <div class="prose rv">' \
         + prose + '</div>\n    ' + aside_block() + '\n  </div>\n</section>\n'
    if faq:
        items = ''.join(
            '\n      <div class="faq-i"><button class="faq-q">%s%s</button><div class="faq-a"><p>%s</p></div></div>' % (q, PLUS, a)
            for q, a in faq)
        b += ('\n<section class="sec">\n  <div class="wrap">\n'
              '    <div class="faq-split">\n'
              '      <div class="faq-aside">\n'
              '        <h2 class="h2 mask"><span>Questions we get asked</span></h2>\n'
              '        <p class="rv" style="--d:.1s">The things people ask about this repair at the counter. '
              'Anything else, message the workshop and we will answer today.</p>\n'
              '        <a class="arrow-link rv" style="--d:.16s" href="%s" target="_blank" rel="noopener">Ask us directly %s</a>\n'
              '      </div>\n'
              '      <div class="faq rv">' % (WA, ARROW)) + items + '\n      </div>\n    </div>\n  </div>\n</section>\n'
    b += PROCESS
    write(fname, title, desc, b)

def article(fname, cat, read, h1, lead, img, prose, title, desc):
    b = phero('<a href="blog.html">Blog</a><span>/</span>' + cat, h1, lead, plain=True, cta=False)
    b += '\n<section class="sec sec--band">\n  <div class="wrap rich">\n    <div class="prose rv">\n' \
         + '      <img src="../assets/img/%s" alt="%s" loading="lazy" style="margin-top:0">\n' % (img, h1) \
         + '      <p style="font-size:12.5px;color:var(--ink-50);margin-bottom:18px">%s &middot; %s</p>\n' % (cat, read) \
         + prose + '\n    </div>\n    ' + aside_block() + '\n  </div>\n</section>\n'
    write(fname, title, desc, b)

# ---------------------------------------------------------------- screen
detail('mac-screen-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Screen replacement',
 'Mac and iPad screen replacement',
 'Cracked glass, flickering panels, dark screens and dead pixels. Most MacBook screens are done the same day, colour-matched and tested before you collect.',
 'ykl-work-1.jpg', 'same day,<br>most models',
 ['Cracked or shattered glass','Vertical or horizontal lines','Flickering backlight','Dark screen, machine still running',
  'Dead pixels or blotches','Stage light effect at the bottom','Lid will not stay on when opened','Ghosting or image retention'],
 """<h2>What we replace</h2>
<p>On a MacBook the display is a full assembly: panel, backlight, hinges, antennas and camera. On an iMac the panel is separate from the glass, and on an iPad the digitiser sits over the LCD. Which parts your repair needs depends on the fault, and we tell you that after the free diagnosis, not before.</p>
<ul class="ticks">
  <li>MacBook Air and MacBook Pro display assemblies, all sizes</li>
  <li>iMac 21.5&quot;, 24&quot; and 27&quot; panels</li>
  <li>iPad glass and digitiser, with LCD replacement where needed</li>
  <li>Backlight cable repair on the MacBook Pro models known for it</li>
</ul>
<h2>Why screens fail</h2>
<p>Impact is the obvious one. The rest are quieter. A hinge that has stiffened stresses the display cable every time you open the lid, and on some MacBook Pro models that cable is short enough to wear through on its own. It shows up first as an uneven glow along the bottom of the screen, then the backlight goes completely.</p>
<p>Lines and flicker usually mean the panel or its connector, but they can also come from the graphics side of the logic board. That difference matters, because replacing a perfectly good panel will not fix a board fault. We test both before quoting.</p>
<h2>How long it takes</h2>
<p>Most MacBook screen replacements are finished the same day, often while you wait, because we keep common panels in stock. iMac panels and less common models may take an extra working day. You get the timeline with your quote.</p>
<h2>After the repair</h2>
<p>We run a full function test: brightness across the range, True Tone where the model supports it, camera, Wi-Fi and hinge tension. Selected screen repairs carry up to 5 years warranty, stated on your invoice.</p>""",
 'Mac &amp; iPad Screen Replacement in PJ and Kuantan | YKL Mac Fix',
 'Cracked, flickering or dark MacBook, iMac and iPad screens replaced. Same-day on most models, free diagnostics, up to 5 years warranty.',
 faq=[('Will the replacement screen look the same?','Yes. We fit original-grade panels and check brightness and colour against the model spec before you collect. On models with True Tone we verify it still works.'),
      ('My glass is fine but there are lines. Is that the panel?','Sometimes. Lines can also come from the display cable or the graphics side of the logic board. The free diagnosis tells us which, so you are not paying for a panel you did not need.'),
      ('Can you replace just the glass on an iPad?','Often yes. If the LCD underneath is undamaged we replace the glass and digitiser only, which costs less. We confirm after testing.')])

# ---------------------------------------------------------------- battery
detail('mac-battery-replacement.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Battery replacement',
 'MacBook battery replacement',
 'Swollen packs, fast drain and the Service Recommended warning. Replaced with a tested cell, calibrated and checked, usually the same day.',
 'ykl-work-4.jpg', 'before it<br>swells further',
 ['Service Recommended in macOS','Trackpad stiff or lifting','Bottom case bulging','Shuts down at 30%',
  'Only runs plugged in','Very high cycle count','Hot while charging','Will not charge past a level'],
 """<h2>Stop using a swollen battery</h2>
<p>A swollen battery is the one fault we ask people not to wait on. The pack expands against the trackpad and the bottom case, which is why a stiff or lifting trackpad is usually the first sign. Left long enough it can crack the case, press on the logic board, or damage the display when the lid is closed.</p>
<p>If your Mac is visibly bulging, power it down, stop charging it and bring it in. Do not press on it, and do not carry it under pressure in a bag.</p>
<h2>What Service Recommended actually means</h2>
<p>macOS reports battery condition from cycle count and measured capacity. Service Recommended means the pack no longer holds enough charge to be considered healthy. It is not an emergency on its own, but it usually appears months before the physical swelling does, which makes it a good moment to book the replacement rather than wait for the trackpad to stop clicking.</p>
<h2>What we fit</h2>
<ul class="ticks">
  <li>Tested cells matched to your exact model, not a generic pack</li>
  <li>New adhesive strips and, where needed, replacement screws</li>
  <li>Battery health and charging behaviour verified before collection</li>
  <li>Old pack disposed of properly. We do not hand swollen cells back</li>
</ul>
<h2>Turnaround</h2>
<p>Most MacBook Air and MacBook Pro batteries are replaced the same day. Older models where the pack is glued into the top case take longer, because the old adhesive has to come out cleanly. Either way you get a timeline with the quote.</p>""",
 'MacBook Battery Replacement in PJ and Kuantan | YKL Mac Fix',
 'Swollen or worn MacBook batteries replaced the same day. Free diagnostics, tested cells, up to 5 years warranty on selected repairs.',
 faq=[('How do I know if my battery is swollen?','The trackpad stops clicking properly, the Mac rocks on a flat table, or you can see a gap between the bottom case and the frame. Any of those means stop charging it and bring it in.'),
      ('Will I lose my data?','No. A battery replacement does not touch your storage. We still recommend a backup before any repair, as a general habit.'),
      ('Can you replace an iPad or iPhone battery too?','Yes. Both use glued packs, so they take longer than a MacBook, but the process and the free diagnosis are the same.')])

# ---------------------------------------------------------------- logic board
detail('mac-logicboard-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Logic board repair',
 'Mac logic board repair',
 'Board-level diagnosis, micro-soldering and BGA reballing. If another shop told you the board is dead and quoted you a new machine, bring it here first.',
 'ykl-work-3.jpg', 'under the<br>microscope',
 ['No power at all','Fans spin, no display','Stuck on the Apple logo','Kernel panic loops',
  'No charge on any port','Very hot before it shuts down','Liquid damage on the board','Random restarts'],
 """<h2>Repair, not replace</h2>
<p>A logic board is a circuit board. When one fails it is almost always a specific component on it: a power management IC, a charging controller, a blown fuse, a cracked solder joint under a chip. Replacing the whole board is fast for the shop and expensive for you. Repairing the component is slower, and it is what we do.</p>
<p>That is the difference people mention in our reviews. Machines quoted as write-offs elsewhere often leave here working, for a fraction of a replacement.</p>
<h2>What board-level work involves</h2>
<ul class="ticks">
  <li>Schematic-led fault tracing, measuring rails to find where the power stops</li>
  <li>Micro-soldering of individual components under a stereo microscope</li>
  <li>BGA reballing for chips that have lost contact with the board</li>
  <li>Corrosion removal and pad rebuilding after liquid damage</li>
  <li>Thermal testing under load before the machine goes back together</li>
</ul>
<h2>Be honest about what happened</h2>
<p>Liquid, a bad charger, a power surge, a drop. Whatever it was, tell us. It narrows the search enormously, which means a faster diagnosis and a lower bill. Nobody here is going to judge a spilled coffee.</p>
<h2>How long it takes</h2>
<p>Board work is the one job we will not rush. Expect two to three working days for most cases, longer if a component has to come in. The device is tested under load afterwards, not just powered on once, because an intermittent fault that reappears a week later helps nobody.</p>
<h2>When it is not worth it</h2>
<p>Sometimes it is not. If the damage is spread across the board, or the cost of repair approaches the value of the machine, we will tell you that plainly at the quote stage. The diagnosis is still free.</p>""",
 'Mac Logic Board Repair &amp; Micro-Soldering | YKL Mac Fix',
 'Board-level Mac repair in Petaling Jaya and Kuantan. Micro-soldering, BGA reballing and liquid damage recovery. Free diagnostics before any quote.',
 faq=[('Another shop said the board cannot be repaired. Can you check?','Yes, and it costs nothing to look. Board-level repair is a different skill set from part swapping, so a board written off elsewhere is often repairable here.'),
      ('How long does board repair take?','Usually two to three working days. Fault tracing takes time, and we test under load afterwards rather than just powering the machine on once.'),
      ('Is my data safe during board repair?','Your storage is a separate component and is not touched by the board work itself. On Macs with soldered storage we take extra care, and we will tell you up front if a fault puts data at risk.')])

# ---------------------------------------------------------------- water
detail('mac-water-damage-repair.html',
 '<a href="services.html">Mac Repair</a><span>/</span>Water damage recovery',
 'Water damage recovery for Mac and iPad',
 'Spills spread. Ultrasonic cleaning, corrosion treatment and component-level repair, and the sooner it reaches our bench the more of it we save.',
 'ykl-work-2.jpg', 'faster is<br>cheaper',
 ['Spilled water, coffee or juice','Worked at first, then died','Screen went dark after a spill','Keys stopped responding',
  'Fans running constantly','Switches off randomly','Charges but will not boot','Burnt smell'],
 """<h2>The first hour matters</h2>
<p>Liquid does not stop working when the screen goes dark. Corrosion keeps eating the board for days, so a machine that still turns on today may not next week. Power it off, do not charge it, do not dry it with heat, and get it to us.</p>
<p>Rice does nothing useful. It absorbs a little surface moisture and leaves starch dust in the ports. The liquid that matters is already between the board and its components.</p>
<h2>What we do on the bench</h2>
<ul class="ticks">
  <li>Full disassembly and inspection under a microscope</li>
  <li>Ultrasonic cleaning of the board to lift residue from under the chips</li>
  <li>Corrosion removal, pad rebuilding and component replacement where tracks have been eaten</li>
  <li>Battery and trackpad checked separately, as both corrode quickly</li>
  <li>Extended testing before the machine goes back together</li>
</ul>
<h2>What we can and cannot promise</h2>
<p>Liquid damage is the one repair where no honest shop guarantees the outcome in advance. What we can promise is a free, thorough diagnosis and a straight answer. If the board is recoverable we will quote it. If it is not, we will say so, and we will still try to get your data off the storage.</p>
<h2>Sugar is worse than water</h2>
<p>Coffee, soft drinks and sweetened tea leave a conductive residue that keeps bridging contacts long after the liquid has dried. If that is what went in, treat it as urgent even if the machine still seems fine.</p>""",
 'MacBook Water Damage Repair in PJ and Kuantan | YKL Mac Fix',
 'Spilled on your Mac or iPad? Ultrasonic cleaning, corrosion treatment and board-level recovery. Free diagnostics and honest answers.',
 faq=[('It still works. Do I need to bring it in?','Yes, ideally today. Corrosion continues after the liquid dries, so machines that survive the spill often fail days or weeks later. Cleaning it now is far cheaper than board repair later.'),
      ('Should I put it in rice?','No. Rice only touches surface moisture and leaves dust in the ports. Power the device off, stop charging it, and bring it to us.'),
      ('Can you recover my files if the Mac is beyond repair?','We will try. On models where storage is a separate module it is usually straightforward. Where storage is soldered to the board it depends on the damage, and we will tell you honestly what the chances are.')])

# ---------------------------------------------------------------- articles
article('blog-professional-mac-repair.html', 'Guides', '8 min read',
 'Why board-level repair beats a replacement quote',
 'A dead logic board is not the end of a Mac. Here is what actually happens on our bench when a machine will not power on.',
 'ykl-work-3.jpg',
 """<h2>The quote that ends the conversation</h2>
<p>You bring in a MacBook that will not turn on. Someone opens it, looks at the board, and tells you the board is gone. The replacement costs most of what a new machine costs, so you buy a new machine. That conversation happens thousands of times a year in Malaysia, and most of the time it did not need to.</p>
<h2>A board is not one part</h2>
<p>A logic board carries hundreds of individual components. When a Mac loses power, the fault is usually one of them: a power management IC, a charging controller, a fuse the size of a grain of rice, or a solder joint under a chip that has cracked from heat cycling. The rest of the board is fine.</p>
<p>Replacing the whole board to fix one component is like replacing an engine because of a failed sensor. It works, it is fast, and it is the most expensive possible answer.</p>
<h2>How the diagnosis actually runs</h2>
<p>The board comes out and goes under a stereo microscope. We measure the power rails in sequence, following the schematic, to find the point where voltage stops arriving. That tells us which stage failed. Visual inspection catches the rest: corrosion from an old spill, a burnt component, a lifted pad.</p>
<p>From there it is soldering work. Components are replaced individually. Chips that have lost contact are reballed and reseated. Pads eaten away by corrosion are rebuilt so a trace can be reconnected.</p>
<h2>Then it gets tested properly</h2>
<p>Powering the machine on once proves very little. An intermittent fault that reappears in a week is a repair that failed. We test under load, with the board at working temperature, before anything goes back into the case.</p>
<h2>When replacement really is the answer</h2>
<p>Sometimes it is. If liquid has spread across the board, if several stages are damaged, or if the repair cost approaches the value of the machine, we say so. The difference is that you hear it after a real diagnosis rather than instead of one, and the diagnosis is free either way.</p>
<h2>What to ask any repair shop</h2>
<ul class="ticks">
  <li>Do you repair at board level, or only replace boards?</li>
  <li>Is the diagnosis free, and do I get the price before anything is opened?</li>
  <li>What warranty covers the work, and is it written on the invoice?</li>
  <li>Can you show me what failed?</li>
</ul>
<p>If the answers are vague, get a second opinion. It costs you nothing here.</p>""",
 'Why Board-Level Mac Repair Beats a Replacement Quote | YKL Mac Fix',
 'What really happens when a Mac will not power on, why most logic boards are repairable, and what to ask before accepting a replacement quote.')

article('blog-mac-battery-health.html', 'Maintenance', '5 min read',
 'Service Recommended: what your Mac battery is telling you',
 'macOS warns you long before the battery swells. What the warning means, and how long you can safely leave it.',
 'ykl-work-4.jpg',
 """<h2>Where the warning comes from</h2>
<p>macOS tracks two things about your battery: how many charge cycles it has been through, and how much charge it can still physically hold compared to when it was new. When the measured capacity drops far enough, the status changes from Normal to Service Recommended.</p>
<p>You can see it yourself. Hold Option and click the Apple menu, choose System Information, then Power. Cycle count and condition are both listed there.</p>
<h2>It is a warning, not an alarm</h2>
<p>Service Recommended on its own means the battery is worn, not dangerous. Plenty of Macs run for months in that state. What it does mean is that the pack has started its decline, and the decline is not linear. Capacity falls slowly, then swelling starts, and swelling is the part that damages other components.</p>
<h2>The signs that do need action today</h2>
<ul class="ticks">
  <li>The trackpad has gone stiff or will not click properly</li>
  <li>The Mac rocks when it sits on a flat table</li>
  <li>You can see a gap between the bottom case and the frame</li>
  <li>The lid no longer closes flush</li>
</ul>
<p>Any of those means the pack is expanding against the case. Power the Mac down, stop charging it, and bring it in. A swollen battery pressing upward will eventually crack the trackpad, and pressing against a closed lid can damage the display.</p>
<h2>Habits that slow the wear</h2>
<p>Batteries age from heat and from sitting at extremes of charge. Keeping the Mac off soft surfaces that block the vents helps more than most people expect. So does leaving Optimised Battery Charging on, and not leaving the machine plugged in at 100% for weeks at a time in a hot room.</p>
<p>None of this stops the wear. It is a consumable part, and it is meant to be replaced.</p>
<h2>What replacement involves</h2>
<p>On most MacBook Air and MacBook Pro models it is a same-day job. We fit a tested cell matched to your model, replace the adhesive, and check that the health reading and charging behaviour are correct before you collect. The old pack is disposed of properly.</p>""",
 'What Service Recommended Means for Your Mac Battery | YKL Mac Fix',
 'How macOS decides your battery needs service, which symptoms mean stop using it today, and what a MacBook battery replacement involves.')

article('blog-water-damage-first-hour.html', 'Emergency', '4 min read',
 'Spilled on your MacBook? The first hour matters most',
 'What to do, what never to do, and why rice is the worst advice on the internet.',
 'ykl-work-2.jpg',
 """<h2>Do this now</h2>
<ul class="ticks">
  <li>Shut it down immediately. Hold the power button if you have to</li>
  <li>Unplug the charger and leave it unplugged</li>
  <li>Stand the Mac upside down and open, like a tent, so liquid drains away from the board</li>
  <li>Wipe what you can reach with a dry cloth</li>
  <li>Get it to a repair bench the same day if you can</li>
</ul>
<h2>Do not do this</h2>
<ul class="ticks">
  <li>Do not turn it on to check whether it still works. Powering a wet board is how a recoverable spill becomes a dead one</li>
  <li>Do not charge it</li>
  <li>Do not use a hairdryer or leave it in the sun. Heat pushes liquid further in and warps components</li>
  <li>Do not put it in rice</li>
</ul>
<h2>Why not rice</h2>
<p>Rice absorbs a little humidity from the air around the device. It does nothing about the liquid already sitting between the logic board and its components, which is the liquid that matters. What it does do is leave starch dust in the ports and buy you two days of false confidence while corrosion spreads.</p>
<h2>What is actually happening inside</h2>
<p>Water conducts, so the immediate risk is a short circuit between contacts that were never meant to touch. That is why powering on is dangerous. The slower problem is corrosion: the residue keeps reacting with the board for days, eating through fine copper traces until a connection that survived the spill fails on its own a week later.</p>
<p>Sugary drinks are worse. Coffee, sweetened tea and soft drinks leave a sticky conductive film that keeps bridging contacts long after the liquid has dried.</p>
<h2>What we do when it arrives</h2>
<p>Full disassembly, then the board goes through an ultrasonic clean to lift residue from underneath the chips where no cloth can reach. Corrosion is removed, damaged pads are rebuilt, and any component that has been eaten through is replaced. The battery and trackpad are checked separately because both corrode fast.</p>
<h2>The honest part</h2>
<p>Nobody can promise a liquid damage recovery before looking at the board, and you should be suspicious of anyone who does. What you should get is a free diagnosis, a straight answer about what is recoverable, and an attempt at your data even if the machine is not worth saving.</p>""",
 'Spilled Water on Your MacBook? What To Do First | YKL Mac Fix',
 'The first hour after a spill decides whether your Mac survives. What to do, what to avoid, and why rice does not work.')

print('detail pages done')
