# Car Dealer Website — Demo Build Plan

A showcase demo for a local car dealership. Built like a real client project, shown before the client is involved. Keep this file in the repo root and paste it at the start of every Antigravity session.

---

## 1. Goal and positioning

**Goal:** a fast, good-looking, mobile-first website that shows the dealer what they could have: browse inventory, filter, view a car, and send an enquiry or book a test drive.

**Demo rules (important, since the dealer is not involved yet):**
- Use a **placeholder brand name** (for example "Marlow Motors") so the demo is reusable. Swapping in the real name later is a 10-minute change if it is stored in one config file.
- Do **not** use the dealer's logo, photos or copy without permission. Use your own photos, free-licence photos (Unsplash/Pexels, check the licence) or clearly labelled sample images.
- Mark inventory as **sample data**. Never show fake prices as if they are real offers.
- Real phone numbers and WhatsApp links point to **your** number or a dummy one until the dealer agrees.

---

## 2. Scope

### In scope (MVP)
| Area | What it includes |
|---|---|
| Home | Hero, featured cars, brand strip, why-us section, how-it-works, contact strip |
| Inventory | Grid listing, filters (brand, price, year, fuel, transmission, km), sort, pagination, empty state |
| Car detail | Gallery, key specs, description, features list, price, EMI estimate, enquiry form, call/WhatsApp buttons, similar cars |
| Enquiry and test drive | Forms with validation, stored in DB, visible in admin, confirmation page |
| Sell / trade-in | One simple form (car details + contact) |
| About and contact | Story, location map link, hours, contact form |
| Admin | Django admin customised so a non-technical owner can add and edit cars with multiple photos |
| Basics | 404/500 pages, SEO meta, sitemap, favicon, responsive on 360px+ screens |

### Out of scope for the demo (mention as "phase 2" to the dealer)
- Online payments (a booking-amount flow can be added later; practise with Razorpay **test mode** separately)
- User accounts, wishlists, comparison tool
- Live chat, WhatsApp API automation
- Multi-language
- Real inventory sync

---

## 3. Tech stack (all free)

- **Backend:** Django (Python), SQLite locally, Postgres when deployed
- **Frontend:** Django templates + Tailwind CSS + vanilla JS modules. **GSAP + ScrollTrigger** for scroll animation, **Lenis** for smooth scroll, **three.js** for the 3D hero car (or a canvas image sequence, see phase 1b). No SPA framework needed.
- **Images:** Pillow for resizing/thumbnails, WebP output
- **Forms:** Django forms with server-side validation, honeypot field for spam
- **Hosting (free):** Render or PythonAnywhere free tier for the demo link; WhiteNoise for static files
- **Tools:** Git + GitHub, VS Code/Antigravity, Lighthouse in Chrome DevTools

---

## 4. Design direction: dark, cinematic, scroll-driven (Apple/Samsung style)

**Personality:** premium product launch page. Dark, quiet, lots of space, one hero object (the car) that moves as the user scrolls.

**Colour (dark theme, one accent):**
| Role | Value |
|---|---|
| Background | Near-black `#07080A` |
| Surface / cards | `#101216` |
| Border | `rgba(255,255,255,0.08)` |
| Text | `#EDEEF0` |
| Muted text | `#8A8F98` |
| Accent | Arctic blue `#7DB8FF` (used for buttons, links, price highlights, one soft glow behind the car) |

Rules: no rainbow gradients. A single soft spotlight behind the car is allowed. Text contrast must stay AA (check muted text on surfaces).

**Typography (two families):**
- Headings: **Archivo** variable font, expanded width (`font-stretch: 125%`), weight 600 to 800, tight letter-spacing. Wide and confident, very automotive.
- Body/UI: **Hanken Grotesk** (clean, slightly warmer than Inter)
- Specs and prices: tabular numbers
- Big, sparse headlines (64 to 120px on desktop), short lines, lots of empty space. Do not use Inter, Space Grotesk or serif fonts.

**Motion system (this is the signature):**
- Smooth scrolling with **Lenis**, scroll-linked animation with **GSAP ScrollTrigger** (both free).
- Home hero is a **pinned scroll sequence**: the car rotates/zooms as you scroll while short text panels fade in and out (design, performance, comfort, price).
- Elsewhere motion is subtle: fade-up on reveal, image parallax, hover states. No bouncing, no confetti.
- Respect `prefers-reduced-motion`: show static images instead.
- Mobile gets a lighter version (fewer frames or a static hero) to stay fast.

**Imagery:** dark-studio style photos, consistent crop, cars lit on dark backgrounds. Cutout PNG/WebP with soft floor reflection looks most premium.

**Copy:** short, confident, specific. Good: "120-point inspection. 6-month warranty." Bad: "Welcome to the future of car buying."

**Avoid (AI-template giveaways):**
- Emoji as icons (use Lucide)
- Three identical rounded cards with icons and filler text
- Purple/blue gradient blobs
- "Unlock", "seamless", "elevate" style wording
- Every section centred with the same layout

---

## 5. Data model

```
Brand        name, slug, logo(optional)
Car          title, slug, brand(FK), model, variant, year, price, km_driven,
             fuel, transmission, owners, colour, registration_state,
             description, is_featured, is_sold, status(draft/published), created_at
CarImage     car(FK), image, alt_text, order, is_cover
CarFeature   car(FK), name            (or a simple M2M to a Feature table)
Enquiry      car(FK, nullable), name, phone, email, message, type
             (enquiry/test_drive/callback), preferred_date, status, created_at
SellRequest  name, phone, brand, model, year, km, expected_price, photos, created_at
SiteSettings dealership name, phone, WhatsApp, address, hours, social links
```

Keep the dealership name, phone and address in `SiteSettings`, so rebranding for the real dealer is a data change, not a code change.

---

## 6. Project structure

```
project/
├── config/            settings split: base.py, dev.py, prod.py
├── apps/
│   ├── core/          home, about, contact, SiteSettings
│   ├── inventory/     Brand, Car, CarImage, listing, detail, filters
│   └── leads/         Enquiry, SellRequest, forms
├── templates/         base.html, partials/ (card, navbar, footer, filters)
├── static/            css, js, fonts, images
├── media/             uploads (git-ignored)
├── plan.md
├── .env.example
└── requirements.txt
```

---

## 7. Build phases

Each phase ends with a commit and a checklist. Do not start the next phase until the checklist passes.

### Phase 0 — Setup (half a day)
- Create repo, virtual env, Django project, split settings, `.env` for secrets
- Add `.gitignore`, `requirements.txt`, `.env.example`
- **Done when:** the site runs locally and the first commit is pushed

### Phase 1 — Design system (1 day)
- Install Tailwind, load Archivo + Hanken Grotesk, define the dark colour tokens and type scale
- Build base template, navbar (transparent over hero, blurred dark when scrolled), footer, buttons, inputs, card, badge, section wrapper
- Make a single `/style-guide/` page showing every component on the dark theme
- **Done when:** the style guide feels like a premium dark product site at 360px and 1440px

### Phase 1b — Scroll hero (2 days)
- Get a free car model (glTF/GLB, check the licence and credit the author) or render frames from it in Blender
- **Option A (recommended):** three.js scene, GSAP ScrollTrigger pins the section and ties car rotation, camera zoom and text panels to scroll progress
- **Option B:** 120 to 180 WebP frames drawn on a `<canvas>` by scroll progress (the classic Apple technique), heavier to load
- Compress the model (gltf-transform + Draco), target under 5 MB, lazy-load it
- Add a static fallback for mobile and reduced-motion users
- **Done when:** scrolling feels smooth at 60fps on a mid-range phone and the page loads fast

### Phase 2 — Data and admin (1 day)
- Models, migrations, customised admin (list filters, search, inline image upload)
- Seed command that loads 15 to 20 sample cars with images
- **Done when:** you can add a car with 6 photos from admin in under 2 minutes

### Phase 3 — Inventory (2 days)
- Listing with filters, sorting, pagination, URL-based filter state
- Detail page with gallery, specs, EMI calculator, similar cars
- **Done when:** filters work together, empty state exists, page loads fast

### Phase 4 — Leads (1 day)
- Enquiry, test drive, callback and sell forms
- Validation, spam protection, thank-you page, admin view of leads
- **Done when:** a submitted form appears in admin with the right car attached

### Phase 5 — Home and content pages (1 day)
- Home, About, Contact, and policy pages
- Write real, specific copy; no lorem ipsum anywhere
- **Done when:** the homepage tells the dealer's story in five seconds

### Phase 6 — Production hardening (1 day)
- `DEBUG=False` settings, `ALLOWED_HOSTS`, secure cookies, CSRF check
- Image compression and lazy loading, caching headers, WhiteNoise
- Meta tags, Open Graph image, sitemap.xml, robots.txt, structured data (schema.org `Car`/`Vehicle`)
- Custom 404 and 500 pages
- **Done when:** Lighthouse scores 90+ on mobile for Performance, Accessibility, Best Practices, SEO

### Phase 7 — Deploy and demo prep (half a day)
- Deploy to free hosting, test on a real phone over mobile data
- Prepare a 3-minute demo script and 5 screenshots
- **Done when:** a public link opens fast on any phone

---

## 8. Working with Antigravity (vibe coding that stays professional)

**Do**
- Start every session by pasting this `plan.md` and saying which phase and task you are on.
- Give **one small task per prompt**, for example "build the filter sidebar partial", not "build the inventory app".
- Read every diff before accepting. If you cannot explain it, ask the AI to explain it.
- Commit after every working step with a clear message.
- Ask for the design tokens to be used everywhere: "use only the CSS variables from `base.css`".
- Test each feature yourself in the browser, including on a phone-sized viewport.
- Ask the AI to review its own code: security, N+1 queries, accessibility.

**Do not**
- Ask for "the whole website" in one prompt
- Accept a new library without asking why it is needed
- Let it invent colours, fonts or spacing outside the design system
- Leave secrets, API keys or `SECRET_KEY` in code
- Keep placeholder text, broken links or dead buttons in the demo
- Skip mobile testing, since most car buyers browse on phones

**Prompt template**
```
Context: Django car dealer demo, phase [N]. Follow plan.md and the design tokens.
Task: [one specific thing]
Constraints: use existing components, no new dependencies, mobile-first.
Output: changed files only, and explain anything non-obvious.
```

---

## 9. Quality checklist before showing anyone

**Design**
- [ ] Only the defined colours, two fonts, consistent spacing
- [ ] Consistent photo crops, no stretched images
- [ ] No lorem ipsum, no emoji icons, no generic marketing filler

**Function**
- [ ] Every link and button works
- [ ] Forms validate and show helpful errors
- [ ] Filters combine correctly and can be cleared
- [ ] Admin is usable by a non-technical person

**Technical**
- [ ] `DEBUG=False` in production, secrets in environment variables
- [ ] Images are WebP, resized, lazy-loaded
- [ ] No console errors, no 404 assets
- [ ] Works at 360px, 768px and 1440px

**Content**
- [ ] Sample data clearly marked
- [ ] Placeholder brand used consistently
- [ ] Contact details point to you or dummy values

---

## 10. Demo day

1. Open on a phone, not a laptop, to show the mobile experience first.
2. Walk through: home, filter a car, open a detail page, send an enquiry.
3. Show the admin: add a car live in under two minutes. This is what sells it.
4. Close with the phase 2 list (payments, finance calculator, WhatsApp automation) and a rough timeline, not a price.

---

## 11. What to learn along the way

- Django ORM query optimisation (`select_related`, `prefetch_related`)
- Responsive design with Tailwind
- Image handling and web performance
- Basic SEO and structured data
- Deployment, environment config and security basics
- Writing a clear project plan and commit history, which you can show future clients
