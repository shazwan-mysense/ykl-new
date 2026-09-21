/* YKL Mac Fix — v2 interactions */
(function () {
  'use strict';
  var motionOK = !window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- smooth scroll ---------- */
  var lenis = null;
  if (motionOK && window.Lenis) {
    lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 1 });
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
  }
  function scrollTo(el) {
    if (lenis) lenis.scrollTo(el, { offset: -90 });
    else el.scrollIntoView({ behavior: motionOK ? 'smooth' : 'auto' });
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute('href');
    if (id.length < 2) return;
    var t = document.querySelector(id);
    if (!t) return;
    e.preventDefault();
    closeDrawer();
    scrollTo(t);
  });

  /* ---------- header ---------- */
  var hdr = document.getElementById('hdr');
  var prog = document.createElement('div');
  prog.className = 'sprog';
  document.body.appendChild(prog);

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop || 0;
    if (hdr) hdr.classList.toggle('stuck', y > 8);
    var h = document.documentElement.scrollHeight - window.innerHeight;
    prog.style.transform = 'scaleX(' + (h > 0 ? Math.min(y / h, 1) : 0) + ')';
    parallax(y);
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- hero parallax ---------- */
  var heroImg = document.getElementById('heroImg');
  var heroSec = heroImg && heroImg.closest('.hero');
  function parallax(y) {
    if (!heroImg || !heroSec || !motionOK) return;
    var h = heroSec.offsetHeight || 1;
    if (y > h) return;
    heroImg.style.transform = 'translate3d(0,' + (y * 0.085).toFixed(2) + 'px,0) scale(' + (1 + y / h * 0.045).toFixed(4) + ')';
  }

  /* ---------- mobile drawer ---------- */
  var burger = document.getElementById('burger');
  var drawer = document.getElementById('drawer');
  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('open');
    if (burger) { burger.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
    document.body.classList.remove('locked');
    if (lenis) lenis.start();
  }
  if (burger && drawer) {
    burger.addEventListener('click', function () {
      var open = !drawer.classList.contains('open');
      drawer.classList.toggle('open', open);
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('locked', open);
      if (lenis) { open ? lenis.stop() : lenis.start(); }
    });
    drawer.addEventListener('click', function (e) { if (e.target.tagName === 'A') closeDrawer(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDrawer(); });
  }
  window.addEventListener('resize', function () { if (window.innerWidth > 980) closeDrawer(); });

  /* ---------- scroll reveals ---------- */
  var targets = document.querySelectorAll('.rv, .mask, .zoom, .proc, .hero-script');
  if (!motionOK || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(targets, function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        io.unobserve(en.target);
        if (en.target.id === 'stats') countUp(en.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    Array.prototype.forEach.call(targets, function (el) { io.observe(el); });
    // anything already above the fold when the observer is late
    setTimeout(function () {
      Array.prototype.forEach.call(targets, function (el) {
        var r = el.getBoundingClientRect();
        var vh = window.innerHeight || document.documentElement.clientHeight || 800;
        if (r.top < vh * 0.92 && r.bottom > 0) el.classList.add('in');
      });
    }, 220);
  }

  /* ---------- count-ups ---------- */
  function fmt(n) {
    if (n >= 1000000) {
      var m = n / 1000000;
      return (m >= 10 ? Math.round(m) : Math.round(m * 10) / 10) + 'M';
    }
    return Math.round(n).toLocaleString('en-US');
  }
  var counted = false;
  function countUp(root) {
    if (counted) return; counted = true;
    Array.prototype.forEach.call(root.querySelectorAll('[data-count]'), function (el) {
      var to = parseFloat(el.getAttribute('data-count')) || 0;
      var sfx = el.getAttribute('data-suffix') || '';
      if (!motionOK) { el.textContent = fmt(to) + sfx; return; }
      var t0 = null, dur = 1500;
      requestAnimationFrame(function step(t) {
        if (t0 === null) t0 = t;
        var p = Math.min((t - t0) / dur, 1);
        el.textContent = fmt(to * (1 - Math.pow(1 - p, 3))) + sfx;
        if (p < 1) requestAnimationFrame(step); else el.textContent = fmt(to) + sfx;
      });
    });
  }
  var statsEl = document.getElementById('stats');
  if (statsEl && (!motionOK || !('IntersectionObserver' in window))) countUp(statsEl);

  /* ---------- FAQ ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.faq-q'), function (btn) {
    var item = btn.parentNode, panel = btn.nextElementSibling;
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', function () {
      var open = !item.classList.contains('open');
      // close siblings
      Array.prototype.forEach.call(item.parentNode.querySelectorAll('.faq-i.open'), function (o) {
        if (o === item) return;
        o.classList.remove('open');
        o.querySelector('.faq-a').style.height = '0px';
        o.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      });
      item.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
      panel.style.height = open ? panel.scrollHeight + 'px' : '0px';
      if (lenis) setTimeout(function () { lenis.resize(); }, 360);
    });
  });
  window.addEventListener('resize', function () {
    Array.prototype.forEach.call(document.querySelectorAll('.faq-i.open .faq-a'), function (p) {
      p.style.height = p.scrollHeight + 'px';
    });
  });

  /* ---------- mark current nav item ---------- */
  var here = location.pathname.split('/').pop() || 'index.html';
  Array.prototype.forEach.call(document.querySelectorAll('.nav > li > a'), function (a) {
    if (a.getAttribute('href') === here) a.parentNode.classList.add('on');
  });

  /* ---------- mock booking form ---------- */
  var form = document.getElementById('bookForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (el) {
        if (!el.value.trim()) { ok = false; el.style.borderColor = '#E5484D'; }
        else { el.style.borderColor = ''; }
      });
      if (!ok) return;
      var done = document.getElementById('formDone');
      if (done) done.classList.add('on');
      form.querySelector('button[type=submit]').textContent = 'Request received';
      if (lenis) setTimeout(function () { lenis.resize(); }, 300);
    });
  }

  onScroll();
})();
