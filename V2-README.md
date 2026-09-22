# YKL Mac Fix — the current site

Built to match the reference mockup the client supplied (black utility bar → white header with
dropdown nav → dark hero → trust bar → service cards → device row → locations + why-choose →
5-step process), then given a craft pass because the mockup was itself AI-generated.

**This design is now the site root.** Open `index.html`.
Assets: `assets/css/v2.css`, `assets/js/v2.js`, images in `assets/img/`.

The earlier Devix-derived design is preserved at **`v1/`** for comparison — it has its own
`assets/css/style.css` and `assets/js/main.js`, and its pages reference `../assets/`.
`v2/` now holds redirect stubs only, so links handed out while this design lived there still work.

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

## The craft layer (22 Sep 2026)

The client's reference mockup was itself AI-generated, so building it faithfully inherited its tells. The
bottom of `assets/css/v2.css` is a **craft layer**, loaded last, that keeps the approved layout, palette and typefaces and
changes how each section is composed. Ideas were taken from the Framer templates the client's agency picked as
reference — Spector, Lateral, Himon, Outline Studio, Kairn, ClearPath, Trev, Mira — all of which share one
lesson: **hairline rules and real photography, not wall-to-wall rounded cards.**

| Was | Is |
|---|---|
| eight identical section openers (script accent + H2 + lead) | a hairline rule under a larger heading; the handwriting is down to one or two per page |
| everything a bordered, rounded, hover-lifting card | services, locations, reviews and team set on rules with the photo leading; blog posts and tiles share the same system |
| six 180px service cards in one row | three across at 3:2, the native ratio of the client's photos, so nothing is cropped |
| dark rounded stats box with four count-ups | four editorial rows: tabular number, label, one line of context |
| circle-icon-in-a-disc process steps | markers on a single blue line that draws itself across the five steps |
| centred FAQ | heading left, questions right |
| synthetic blue radial glows on hero, page heroes and CTA | gone; the photography carries those sections |
| one H2 size for every section | `.h2` for load-bearing sections, `.h2--sub` for supporting ones |
| tracking assigned by tag | a ramp by optical size: negative on display, positive on small print |

**A rule the craft layer must follow:** it is loaded last, so any desktop rule it restates must restate the
small-screen override too. `.hero .wrap` was set to `1.18fr .82fr` without one and the hero stopped stacking on
phones. Sections 26 and 47 exist for exactly this.

## Robustness

Every hidden animation state is gated behind an `html.js` class set by an inline script in `<head>`. Without it,
`.rv{opacity:0}` on 55 elements meant one bad asset path rendered a blank page. Verified: with scripting
disabled, 0 of 63 animated elements are hidden.

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
- **Per-word headline reveal** (`.words`) and a **scroll-scrubbed statement** (`.say`) whose words ink up from
  `--ink-20` to `--ink` as you pass it. Both use `splitWords()`, which walks text nodes only so inline markup
  like `<span class="acc">` survives the split.
- **Hovering one item quiets its row.** Gated on `:has(:hover)` so it cannot fire while the pointer is merely
  crossing the gutters, with a `.72` floor so the quieted cards stay above the contrast minimum.
- `.reveal-group` stages its own children from their index; delays are no longer hand-typed into the markup.
- Everything is behind `prefers-reduced-motion: reduce` — all transforms/transitions are dropped
  and every element is marked `.in` immediately.

## Gotchas already handled
- `overflow-x:hidden` kills `position:sticky`; `html` uses `overflow-x:clip` instead.
- The hero photo is a JPEG on black. It is `mix-blend-mode:screen` **plus** a radial `mask-image`,
  otherwise it reads as a pasted rectangle against `#030505`.
- `.ticks` is deliberately NOT scoped to `.prose` — it is also used inside `.split-copy`.
- `.phero-script` sits in 38px of padding **above** the hero art, not over it: white handwriting on
  a light product photo was unreadable.
- **Client photography is never covered.** The handwritten note beside the bench photo sits under it, not on it.
- `.zoom.in img{transform:scale(1)}` is declared after the hover rules at equal specificity and wins, which had
  killed the hover zoom on every photo. The scale lives on a `--z` custom property so the two cannot fight.
- The `:focus-visible` outline must not set `border-radius` — it applies to the element and snaps a button's
  own corners. It uses `inherit`.
- The cache-buster is read out of `index.html` by `_build.py`, so bumping `?v=` there cannot leave the other
  twelve pages on a stale stylesheet.

## Regenerating
`index.html` is hand-written and is the source of the shared header, footer and process section.
Every other page is generated:

```bash
python3 _build.py && python3 _build2.py
```

`_build.py` slices the header/footer/process blocks out of `index.html`, then writes services,
devices, about, contact and blog. `_build2.py` reuses its helpers for the four service detail pages
and the three blog articles. Edit the header or footer in `index.html`, re-run both, and every page
picks it up. Do not hand-edit the generated pages unless you also update the builders.
