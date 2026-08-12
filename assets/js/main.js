/* YKL Mac Fix — shared behaviour */
(function () {
  // Lenis smooth scroll
  var lenis = null;
  if (window.Lenis && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 1 });
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

  // Hero stage: mouse parallax (desktop, motion-safe)
  var stage = document.querySelector('.hero-stage');
  var motionOK = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (stage && motionOK && window.matchMedia('(pointer: fine)').matches) {
    var layers = stage.querySelectorAll('.fl');
    var tx = 0, ty = 0, cx = 0, cy = 0, raf2 = null;
    document.querySelector('.hero').addEventListener('mousemove', function (e) {
      var r = stage.getBoundingClientRect();
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

  // Diagnostic ticker: type each phrase, hold, then next
  var diag = document.querySelector('.diag-text');
  if (diag) {
    var phrases;
    try { phrases = JSON.parse(diag.getAttribute('data-diag')); } catch (e) { phrases = null; }
    if (phrases && phrases.length && motionOK) {
      var pi = 0;
      function typePhrase() {
        var text = phrases[pi];
        var ci = 0;
        diag.textContent = '';
        (function typeChar() {
          if (ci <= text.length) {
            diag.textContent = text.slice(0, ci);
            ci++;
            setTimeout(typeChar, 42);
          } else {
            setTimeout(function () {
              pi = (pi + 1) % phrases.length;
              typePhrase();
            }, pi === 0 ? 2600 : 1700);
          }
        })();
      }
      typePhrase();
    }
  }

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
