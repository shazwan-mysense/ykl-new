# YKL Mac Fix — v2 (client reference-mockup design)

A second, complete design of the site, built to match the reference mockup the client supplied
(black utility bar → white header with dropdown nav → dark hero → trust bar → service cards →
device row → locations + why-choose → 5-step process). v1 (the Devix-derived design) is untouched
in the repo root so the two can be compared side by side.

Open `v2/index.html`. Assets: `v2/assets/css/v2.css`, `v2/assets/js/v2.js`, images shared from
`../assets/img/`.

## Pages (13)
index · services · devices · about · contact · blog
· mac-screen-repair · mac-battery-replacement · mac-logicboard-repair · mac-water-damage-repair
· blog-professional-mac-repair · blog-mac-battery-health · blog-water-damage-first-hour

## Tokens (sampled from the client's mockup PNG)
| role | value |
|---|---|
| utility bar / dark panels | `#1B2028` |
| primary blue | `#0171FD` (hover `#0159C9`, soft `#E8F1FF`) |
| WhatsApp green | `#01BA47` |
| hero / page-hero background | `#030505` |
| light band | `#F5F7F9` · alt band `#F2F7FA` |
| ink | `#101828` · secondary `#475467` · muted `#667085` |
| hairline | `#E4E9F0` · radius 14px · easing `cubic-bezier(.22,1,.36,1)` |
| type | Inter 400–800 (all UI) + Caveat (the handwritten accents) |

## Motion layer
- **Lenis** smooth scroll, `lerp .1`.
- `.mask` — clip reveal: a heading's inner `<span>` slides up from `translateY(105%)`. Used on every H1/H2.
- `.rv` — fade + 26px rise. Stagger with inline `style="--d:.06s"` (the reveal delay custom property).
- `.zoom` — image starts at `scale(1.14)` and settles to 1 as the card enters view.
- Hero: image parallax + scale on scroll, handwritten accent with a blue underline that draws in.
- `.proc` — the connector lines between the five process steps draw left to right in sequence.
- Count-ups on the stats strip (`fmt()` renders 1,190 and 1M).
- Thin blue scroll-progress bar fixed at the top of the viewport.
- Sticky header compacts from 74px to 64px and gains a shadow past 8px of scroll.
- Hovers: cards lift 6px, card images scale, arrows slide, buttons darken and lift.
- Everything is behind `prefers-reduced-motion: reduce` — all transforms/transitions are dropped
  and every element is marked `.in` immediately.

## Gotchas already handled
- `overflow-x:hidden` kills `position:sticky`; `html` uses `overflow-x:clip` instead.
- The hero photo is a JPEG on black. It is `mix-blend-mode:screen` **plus** a radial `mask-image`,
  otherwise it reads as a pasted rectangle against `#030505`.
- `.ticks` is deliberately NOT scoped to `.prose` — it is also used inside `.split-copy`.
- `.phero-script` sits in 38px of padding **above** the hero art, not over it: white handwriting on
  a light product photo was unreadable.

## Regenerating
`index.html` is hand-written and is the source of the shared header, footer and process section.
Every other page is generated:

```bash
cd v2 && python3 _build.py && python3 _build2.py
```

`_build.py` slices the header/footer/process blocks out of `index.html`, then writes services,
devices, about, contact and blog. `_build2.py` reuses its helpers for the four service detail pages
and the three blog articles. Edit the header or footer in `index.html`, re-run both, and every page
picks it up. Do not hand-edit the generated pages unless you also update the builders.
