/* YKL Mac Fix — shared behaviour */
(function () {
  // Lenis smooth scroll
  var lenis = null;
  if (window.Lenis && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    lenis = new Lenis({
      lerp: 0.1,
      wheelMultiplier: 1,
      // let horizontal tracks keep their own wheel/trackpad events
      prevent: function (node) {
        return !!(node && node.classList && node.classList.contains('slider-track'));
      }
    });
    function raf(t) { lenis.raf(t); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
  }

  // Nav background on scroll
  var nav = document.querySelector('.nav');
  function onScroll() {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var burger = document.querySelector('.nav-burger');
  var menu = document.querySelector('.mobile-menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.classList.toggle('open', open);
      document.body.classList.toggle('menu-locked', open);
      if (lenis) open ? lenis.stop() : lenis.start();
      // stagger links
      menu.querySelectorAll('.mm-link').forEach(function (a, i) {
        a.style.transitionDelay = open ? (0.06 + i * 0.055) + 's' : '0s';
      });
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('open');
        burger.classList.remove('open');
        document.body.classList.remove('menu-locked');
        if (lenis) lenis.start();
      });
    });
  }

  // Scroll reveals (single observer; stagger inside .reveal-group)
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      io.unobserve(e.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

  document.querySelectorAll('.reveal-group').forEach(function (g) {
    Array.prototype.forEach.call(g.children, function (child, i) {
      child.classList.add('reveal');
      child.style.transitionDelay = (i * 0.08) + 's';
    });
  });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  // Count-up stats: <span class="num" data-count="1190" data-suffix="+">0</span>
  var nio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      nio.unobserve(e.target);
      var el = e.target;
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      var dur = 1600, t0 = null;
      function fmt(n) { return n.toLocaleString('en-US'); }
      function tick(t) {
        if (!t0) t0 = t;
        var p = Math.min((t - t0) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 4);
        el.textContent = fmt(Math.round(target * eased)) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.num[data-count]').forEach(function (el) { nio.observe(el); });

  // Hero: mouse parallax on [data-depth] layers (desktop, motion-safe)
  var heroEl = document.querySelector('.hero');
  var motionOK = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var layers = heroEl ? heroEl.querySelectorAll('[data-depth]') : [];
  if (layers.length && motionOK && window.matchMedia('(pointer: fine)').matches) {
    var tx = 0, ty = 0, cx = 0, cy = 0, raf2 = null;
    heroEl.addEventListener('mousemove', function (e) {
      var r = heroEl.getBoundingClientRect();
      tx = (e.clientX - (r.left + r.width / 2)) / r.width;
      ty = (e.clientY - (r.top + r.height / 2)) / r.height;
      if (!raf2) raf2 = requestAnimationFrame(drift);
    });
    function drift() {
      cx += (tx - cx) * 0.06;
      cy += (ty - cy) * 0.06;
      layers.forEach(function (el) {
        var d = parseFloat(el.getAttribute('data-depth') || '0');
        el.style.translate = (-cx * d) + 'px ' + (-cy * d) + 'px';
      });
      if (Math.abs(tx - cx) + Math.abs(ty - cy) > 0.001) {
        raf2 = requestAnimationFrame(drift);
      } else { raf2 = null; }
    }
  }

  // Rotating headline word: <span class="word" data-rotate='["A","B"]'>A</span>
  document.querySelectorAll('.word[data-rotate]').forEach(function (el) {
    var phrases;
    try { phrases = JSON.parse(el.getAttribute('data-rotate')); } catch (e) { return; }
    if (!phrases || phrases.length < 2 || !motionOK) return;
    var i = 0;
    setInterval(function () {
      el.classList.add('word-out');
      setTimeout(function () {
        i = (i + 1) % phrases.length;
        el.textContent = phrases[i];
        el.classList.remove('word-out');
        el.classList.add('word-in');
        setTimeout(function () { el.classList.remove('word-in'); }, 520);
      }, 380);
    }, 3000);
  });

  // Before / after cards: switch buttons, click-to-toggle, hover preview on desktop
  var fine = window.matchMedia('(pointer: fine)').matches;
  document.querySelectorAll('.ba-card').forEach(function (card) {
    var media = card.querySelector('.ba-media');
    var btns = card.querySelectorAll('.ba-switch button');
    if (!media) return;
    function set(after) {
      media.classList.toggle('show-after', after);
      btns.forEach(function (b) {
        b.classList.toggle('on', (b.getAttribute('data-state') === 'after') === after);
      });
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function () { set(b.getAttribute('data-state') === 'after'); });
    });
    media.addEventListener('click', function () { set(!media.classList.contains('show-after')); });
    if (fine) {
      var sticky = false;
      btns.forEach(function (b) { b.addEventListener('click', function () { sticky = true; }); });
      media.addEventListener('mouseenter', function () { if (!sticky) set(true); });
      media.addEventListener('mouseleave', function () { if (!sticky) set(false); });
      media.addEventListener('click', function () { sticky = true; });
    }
  });

  // Before/after rows: depth cue as the next row slides over the previous one
  var baRows = Array.prototype.slice.call(document.querySelectorAll('.ba-row'));
  if (baRows.length > 1 && motionOK) {
    var stackQuery = window.matchMedia('(min-width: 901px)');
    var stackTicking = false;
    function paintStack() {
      stackTicking = false;
      if (!stackQuery.matches) {
        baRows.forEach(function (r) { r.style.transform = ''; r.style.opacity = ''; });
        return;
      }
      for (var i = 0; i < baRows.length - 1; i++) {
        var cur = baRows[i], next = baRows[i + 1];
        var gap = next.getBoundingClientRect().top - cur.getBoundingClientRect().top;
        var covered = 1 - Math.min(Math.max(gap / Math.max(cur.offsetHeight, 1), 0), 1);
        cur.style.transform = 'scale(' + (1 - 0.03 * covered).toFixed(4) + ')';
        cur.style.opacity = (1 - 0.3 * covered).toFixed(3);
      }
    }
    function onStackScroll() {
      if (!stackTicking) { stackTicking = true; requestAnimationFrame(paintStack); }
    }
    window.addEventListener('scroll', onStackScroll, { passive: true });
    window.addEventListener('resize', onStackScroll);
    paintStack();
  }

  // Sliders: arrows, drag-to-scroll, snap, progress rail
  document.querySelectorAll('.slider').forEach(function (sl) {
    var track = sl.querySelector('.slider-track');
    if (!track) return;
    var prev = sl.querySelector('[data-slide="prev"]');
    var next = sl.querySelector('[data-slide="next"]');
    var bar  = sl.querySelector('.slider-bar');

    function pageStep() {
      var item = track.querySelector('.slider-item');
      if (!item) return track.clientWidth;
      var gap = parseFloat(getComputedStyle(track).columnGap || '24') || 24;
      var per = Math.max(1, Math.floor(track.clientWidth / (item.offsetWidth + gap)));
      return per * (item.offsetWidth + gap);
    }
    function update() {
      var max = track.scrollWidth - track.clientWidth;
      var p = max > 1 ? track.scrollLeft / max : 0;
      if (bar) {
        var frac = Math.min(1, track.clientWidth / Math.max(track.scrollWidth, 1));
        bar.style.width = (frac * 100).toFixed(2) + '%';
        bar.style.marginLeft = (p * (100 - frac * 100)).toFixed(2) + '%';
      }
      if (prev) prev.disabled = track.scrollLeft <= 2;
      if (next) next.disabled = track.scrollLeft >= max - 2;
    }
    function animateTo(target, ms) {
      var max = Math.max(0, track.scrollWidth - track.clientWidth);
      target = Math.max(0, Math.min(max, target));
      var from = track.scrollLeft, dist = target - from;
      if (Math.abs(dist) < 1) return;
      var snap = track.style.scrollSnapType;
      track.style.scrollSnapType = 'none';   // mandatory snap cancels programmatic scrolling
      var settled = false;
      function finish() {
        if (settled) return;
        settled = true;
        track.scrollLeft = target;
        track.style.scrollSnapType = snap;
        update();
      }
      if (!motionOK) { finish(); return; }
      var t0 = null, dur = ms || 430;
      requestAnimationFrame(function frame(t) {
        if (settled) return;
        if (t0 === null) t0 = t;
        var p = Math.min((t - t0) / dur, 1);
        track.scrollLeft = from + dist * (1 - Math.pow(1 - p, 3));
        if (p < 1) requestAnimationFrame(frame); else finish();
      });
      setTimeout(finish, dur + 160);         // land anyway if rAF is throttled
    }
    if (prev) prev.addEventListener('click', function () { nudged(); animateTo(track.scrollLeft - pageStep()); });
    if (next) next.addEventListener('click', function () { nudged(); animateTo(track.scrollLeft + pageStep()); });
    track.addEventListener('scroll', function () {
      if (!track._t) track._t = requestAnimationFrame(function () { track._t = null; update(); });
    }, { passive: true });
    window.addEventListener('resize', update);

    // pointer drag (mouse only; touch already scrolls natively)
    var down = false, startX = 0, startLeft = 0, moved = 0;
    track.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse') return;
      down = true; moved = 0; startX = e.clientX; startLeft = track.scrollLeft; nudged();
      track.classList.add('dragging');
    });
    track.addEventListener('pointermove', function (e) {
      if (!down) return;
      var dx = e.clientX - startX;
      moved = Math.max(moved, Math.abs(dx));
      track.scrollLeft = startLeft - dx;
    });
    function endDrag() {
      if (!down) return;
      down = false;
      track.classList.remove('dragging');
      update();
    }
    track.addEventListener('pointerup', endDrag);
    track.addEventListener('pointerleave', endDrag);
    track.addEventListener('pointercancel', endDrag);
    // swallow the click that ends a drag so cards don't navigate
    track.addEventListener('click', function (e) {
      if (moved > 6) { e.preventDefault(); e.stopPropagation(); moved = 0; }
    }, true);

    update();

    // ---- autoplay -------------------------------------------------------
    // Advances one page at a time. Pauses on hover, on focus, while the tab
    // or section is out of view, and for a cooldown after any manual input.
    var AUTO_MS = parseInt(sl.getAttribute('data-autoplay') || '4800', 10);
    var hovered = false, quietUntil = 0;

    function nudged() { quietUntil = Date.now() + 9000; }

    function onScreen() {
      var r = sl.getBoundingClientRect();
      var vh = window.innerHeight || document.documentElement.clientHeight || 0;
      return r.bottom > 0 && r.top < vh;
    }
    function mayAdvance() {
      return motionOK && !hovered && !document.hidden &&
             Date.now() >= quietUntil && onScreen() &&
             track.scrollWidth > track.clientWidth + 2;
    }
    function advance() {
      if (!mayAdvance()) return;
      var max = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= max - 4) animateTo(0, 760);   // gentle rewind
      else animateTo(track.scrollLeft + pageStep());
    }

    sl.addEventListener('mouseenter', function () { hovered = true; });
    sl.addEventListener('mouseleave', function () { hovered = false; });
    sl.addEventListener('focusin',  function () { hovered = true; });
    sl.addEventListener('focusout', function () { hovered = false; });
    track.addEventListener('touchstart', nudged, { passive: true });

    if (motionOK) setInterval(advance, AUTO_MS);
  });

  // Mock form
  var form = document.querySelector('form[data-mock]');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.textContent = 'Message sent. We will reply shortly.'; btn.disabled = true; btn.style.opacity = '.75'; }
    });
  }

  // Current-page nav highlight
  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    if (a.getAttribute('href') === here) a.classList.add('active');
  });
})();
