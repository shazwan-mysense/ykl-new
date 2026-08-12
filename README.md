# YKL Mac Fix — website mockup

A complete redesign concept for [yklmacfix.com](https://www.yklmacfix.com/), built as a static site.
Design direction: the Devix Framer template's visual system (Host Grotesk + IBM Plex Mono, bone/cobalt palette, smooth Lenis scrolling, scroll reveals) combined with conversion patterns from kissmymac.my (trust chips, stats band, process steps, WhatsApp-first CTAs).

## Pages

- `index.html` — home
- `services.html` — all 10 services
- `devices.html` — supported devices, symptom-led
- `about.html` — story, numbers, values, testimonials
- `contact.html` — contact methods, hours, 3 store locations, enquiry form (mock)
- `blog.html` + `blog-professional-mac-repair.html` — blog index and sample article
- `mac-screen-repair.html`, `mac-battery-replacement.html`, `mac-water-damage-repair.html`, `mac-logicboard-repair.html` — service detail pages

## Run it

No build step. Serve the folder with any static server, e.g.:

```bash
python3 -m http.server 8080
```

## Before go-live

See `CONTENT-NOTES.md` — facts to confirm with the client (addresses, hours, warranty terms, testimonials) and stock photos to replace. `DESIGN-SPEC.md` documents the design system.
