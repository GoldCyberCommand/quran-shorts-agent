# Bayān — a comprehensive English Qur'an commentary app

**Working name:** Bayān (بيان — "clear explanation"). Placeholder; rename freely.

**Status:** Planning. Nothing built yet.
**Owner:** Gold Cyber Command Limited
**Last updated:** 2026-08-19

---

## 1. What we are building

**The objective:** bring the depth and richness of the Sunni tafsīr tradition within
reach of both the layman and the serious student — in one app, on one screen, without
either of them being handed a lesser version.

Three things have to be true at once for that to work. The content has to be
comprehensive and honestly sourced (§5–§9). The app has to be **easy to move through** —
clean enough that nothing distracts from the text, and connected enough that you can
follow an explanation from one verse to another without losing your place (§2). And the
text has to **look and sound the way the reader wants it to** — their script, their
colours, their reciter (§3). Navigation and presentation are not polish here; between
them they are half the product.

Scope is **Sunni Islam only** — classical and modern, stated plainly so a reader always
knows what tradition they are reading (see §4 and §9 rule 10).

For **every ayah of the Qur'an**, four layers of understanding, stacked so a reader
can stop at whatever depth they came for:

| Layer | Name | Length | Who it's for |
|---|---|---|---|
| **L0** | Arabic text + English translation(s) | verbatim | everyone |
| **L1** | **Plain English** — the executive summary | 60–150 words | everyday reader; the default view |
| **L2** | **Context** — what this passage is about, where it sits in the surah, the setting of its revelation | 150–400 words | the curious reader |
| **L3** | **Scholarly views** — what the mufassirūn actually said, where they agree, where they differ, each attributed | unbounded | the student |

The product thesis is **L1 is the front door and L3 is the foundation.** Most Qur'an
apps give you a translation and a wall of tafsir text. Bayān gives you one honest
paragraph in ordinary English, and then lets you pull the thread all the way down to
al-Ṭabarī if you want to — with every sentence traceable to a named source.

### The differentiator

Existing apps (Quran.com, Muslim Pro, Tafsir apps) present tafsir works **side by
side**: pick Ibn Kathīr, read Ibn Kathīr. The reader is left to synthesise.

Bayān synthesises. For each passage we extract the *positions* scholars hold, cluster
equivalent positions across works, and present:

- **Where they agree** — the settled mainstream reading
- **Where they differ (ikhtilāf)** — each position, who holds it, on what evidence
- **The full source text** — always one tap away, verbatim, attributed

And it **connects**. Where a scholar explains one verse by reaching for another, that
link is in the data and you can follow it — with a peek first, and a trail back (§2.2).
The Qur'an explaining the Qur'an is the oldest method in tafsīr; almost no app makes it
navigable.

Synthesis and navigable linking are the two things nothing else does well.

---

## 2. Navigation is the product

The app's purpose is to let a layman and a serious student stand in front of the same
rich tafsīr tradition and both get something real from it. That is not achieved by
having more content than everyone else. It is achieved by **navigation** — how fast you
get to the right place, and how easily you follow a thought once you're there.

Treat this as a primary objective with the same weight as content accuracy, not as
polish applied at the end.

### 2.1 One app, two audiences: reading depth

Do not build a "simple mode" and an "advanced mode" with different content. That splits
the product and quietly tells the layman there's a better version they aren't getting.

Instead, a single **reading depth** setting that persists and changes only what is
*expanded by default* — never what is available:

| Depth | Opens showing | For |
|---|---|---|
| **Plain** | L0 + L1. One translation, one paragraph. | Someone who wants to understand what they just read |
| **Study** | L0 + L1 + L2, with L3 headings visible and collapsed | Someone reading through with intent |
| **Scholar** | L0 + L2 + L3 expanded, source panel open, multiple translations | Someone working a passage properly |

Every reader can reach every layer at every depth — one tap away. The setting is a
starting position, not a permission level. A layman who gets curious about 2:106
expands the scholarly views and finds them written to be followed, not to be impressive.

**This is the bridge.** The plain paragraph is what a layman reads and what a scholar
skips; the ikhtilāf section is what a scholar reads and what a layman *can* read. Same
screen, same content, different entry point.

### 2.2 Verse-to-verse: the cross-reference graph

*"Jump from verse to verse wherever there is a linked explanation."*

This is a **content** feature before it is a UI feature. The links have to exist in the
data, which means the pipeline has to extract them (stage 4b, see §8).

**Where links come from — and why that matters.** The valuable links are the ones
*scholars themselves assert*. When Ibn Kathīr explains 2:2 by citing 41:44, that is a
scholar-asserted link: it is meaningful, it is citable, and it is reviewable. Keyword
similarity and embedding proximity produce plausible-looking links that no scholar ever
drew — they are unciteable, and under §9 rule 1 they cannot ship. So:

- **Primary source of links:** every ayah a mufassir cites while commenting on a passage,
  extracted during stage 4 with the citing source recorded on the edge.
- **Secondary:** structural links that are matters of fact, not interpretation — the
  same story told elsewhere, verbatim or near-verbatim parallel wording, the passages a
  work discusses together.
- **Never:** an unattributed "related verses" list generated by similarity search.

**Link types**, each rendered differently so the reader knows what kind of connection
they're following:

| Type | Meaning | Example |
|---|---|---|
| `explains` | The Qur'an explaining the Qur'an — a mufassir cites B to clarify A | 2:2 → 41:44 |
| `parallel` | Same event or wording elsewhere | the Mūsā narratives across surahs |
| `general/specific` | One passage qualifies another (*ʿāmm/khāṣṣ*, *muṭlaq/muqayyad*) | frequent in āyāt al-aḥkām |
| `abrogation-discussed` | Scholars discuss a *naskh* relationship — **always shown as a discussion, never as a settled verdict** | 2:106 and its cluster |
| `same-topic` | A concept thread across the Qur'an | patience, orphans, the Sabbath |
| `cited-as-evidence` | A mufassir uses B as evidence for a position on A | throughout L3 |

Every edge carries: type, direction, the source that asserts it, and a locator. An edge
with no asserting source does not exist.

**Peek before you leap.** The failure mode of a linked corpus is losing your place. So a
link never navigates on first touch:

1. Hover (desktop) or tap (touch) → a **peek card**: the linked ayah, its translation,
   its one-line plain summary, and why it's linked ("Ibn Kathīr cites this here").
2. Only a second, deliberate action navigates.
3. Navigating pushes onto a **trail** — a visible breadcrumb of your hops, each one
   clickable, with proper back/forward. You can wander four verses deep and get home in
   one click.

Most link-following ends at the peek card. That is the design working, not failing.

### 2.3 Getting anywhere fast

- **The ayah address is the route.** `2:255` is the canonical identifier everywhere —
  URL, deep link, search input, share target, keyboard entry.
- **Command palette** (`⌘K` / `Ctrl-K`) as the primary navigation. One box accepting
  `2:255`, `al-baqarah 255`, `ayat al-kursi`, `throne verse`, or free text across
  translations and summaries. Typing an address and pressing enter is the fastest path
  to any of 6,236 places and needs no menus.
- **Three indexes**, because people hold the Qur'an in their head three ways: by surah,
  by juz (for readers and memorisers), and by topic thread.
- **Topic threads** — a concept followed across the whole Qur'an in revelation or mushaf
  order, assembled from `same-topic` edges. This is how a layman actually asks a
  question: "what does the Qur'an say about *X*."
- **Keyboard throughout on desktop.** `j`/`k` by ayah, `[`/`]` by passage, `⌘K` to jump,
  `Esc` to close a peek. A student working a passage should barely touch the mouse.

### 2.4 What "clean" means here

Clean is a set of constraints, not a mood:

- **One reading column.** No sidebars competing with the text on first load. The source
  panel is summonable, not permanent.
- **Structure carried by typography and space**, not by boxes, borders and cards. A
  screen full of bordered panels reads as an admin dashboard.
- **Progressive disclosure everywhere.** The default view is short. Depth is available
  in one gesture and invisible until asked for.
- **The Arabic gets real typographic care** — proper mushaf-style face, correct line
  height for diacritics, never cramped to fit an English layout.
- **Source and summary always visually distinct** (§9 rule 7) — the one place where a
  visual boundary is non-negotiable.
- **No engagement furniture.** No streaks, badges, popups, or nudges. The reader came to
  read.

**Ruled out by the above:** a tab bar of eight tafsīr works across the top; verse cards
in a scrolling feed; L3 rendered as an undifferentiated wall of text; anything that
requires horizontal scrolling; modal dialogs in the reading path.

### 2.5 What this adds to the build

Navigation as a first-class objective is not free. It adds, concretely:

- a `cross_reference` table and the extraction stage that populates it (§7, §8);
- reviewer workload — every extracted edge is content and needs approving, though edges
  review fast in bulk since each is one assertion with one citation;
- peek-card rendering, trail state, and command-palette search in the app;
- a topic taxonomy, which is genuinely editorial work and should start small — perhaps
  60–100 threads for the pilot rather than an exhaustive ontology.

Sequenced in §11: links are extracted from Phase 1 so the pilot corpus has a real graph
inside Juz ʿAmma, and the graph gets denser with every juz added.

---

## 3. Presentation: script, theme, and sound

The text has to look right, feel right to sit with, and be able to speak. All three are
reader-facing settings, and all three share one rule: **they never change what the
content says, only how it is presented.**

### 3.1 Two Arabic modes, and they are genuinely different

This is the fact that shapes the feature. There are two ways to put the Qur'an on a
screen, and they are not two settings on the same view:

| | **Flowing text** *(default)* | **Page-faithful mushaf** |
|---|---|---|
| How | A Unicode text edition in a webfont | QCF page fonts — one font file per mushaf page |
| Reflows? | Yes — any width, any font size | No. Fixed 15 lines, fixed page |
| Searchable / selectable | Yes | Effectively no (each glyph is a whole word) |
| Cost | One font | **604 font files** plus page-layout data |
| Right for | Reading tafsīr | Memorisers who hold page positions visually |

The Madinah mushaf's page-perfect rendering works by giving every one of the 604 pages
its own font, in which each glyph is an entire word. That is how apps reproduce the
printed page exactly — and it is why that mode cannot reflow, cannot resize freely, and
cannot be searched as text.

**Recommendation: flowing text is the reading column. The mushaf page is a separate
view.** Bayān is a tafsīr reader — its column has a plain-English paragraph, disclosures
and inline cross-references beside the Arabic, and none of that survives a fixed 15-line
page. Offer the page view as its own screen (`Mushaf`), for readers who want it, rather
than bending the reading column into a shape it cannot hold.

**Text editions** (flowing mode, user-selectable):

| Edition | Notes |
|---|---|
| **Uthmani (KFGQPC Ḥafṣ)** | The default. What most readers expect. |
| Uthmani simple | Lighter diacritics; also the search index |
| **IndoPak** | Expected by South Asian readers; different orthographic conventions, not a font choice |
| Imlaei | Modern standard orthography |

**Mushaf layouts** (page view), all available from QUL: Madinah V1 (1405H, 604pp,
15 lines) · Madinah V2 (1421H, 604pp) · QCF v4 (1441H) · IndoPak 15-line (610pp) ·
IndoPak 16-line (548pp, nastaʿlīq) · Digital Khatt.

**Arabic faces** for flowing mode — chosen independently of the English face: Amiri,
Scheherazade New, Noto Naskh Arabic, KFGQPC Uthmanic Ḥafṣ, Digital Khatt.

### 3.2 Word-by-word is a layer, not a script

Word-by-word sits *over* flowing mode: each Arabic word carries its translation and
transliteration beneath it, from QUL's word-level data (~78,000 words). Once that layer
exists it also unlocks per-word audio highlighting and tajwīd colouring.

**QAAM already renders word-by-word tajwīd-coloured mushaf text.** That work — the
colouring rules, the word alignment — should be reused here rather than rebuilt.

### 3.3 Themes: one engine, two axes

Eight accent colours and "as clean as possible" pull against each other if you
hand-design eight skins. So don't. **One engine, two independent axes:**

- **Ground** — Paper · Sepia · Night · Black (true black for OLED)
- **Accent** — Green · Blue · Purple · Red · Gold · Pink · Brown · Grey, plus a free hue

Accents are generated in **OKLCH from a single hue value**, with lightness and chroma
fixed per role and per ground. That means every accent is legible on every ground *by
construction*, not by luck: 4 × 8 = 32 combinations out of about 14 tokens, with no skin
files to maintain and no combination that was never checked.

**The accent never touches the Qur'anic text.** Arabic and translation stay
maximum-contrast ink on ground at every setting. The accent lives in chrome, links, the
summary rule, selection and focus. A "purple theme" must never mean purple scripture —
that is both ugly and a violation of §9 rule 7, which requires source and summary to
stay visually distinct.

**Customisable for real:** a hue slider produces any accent, not only the eight presets;
themes can be named, saved, and exported as a small JSON blob to share or restore.

**Reading comfort belongs here too:** Arabic size, English size, line height, column
width, and per-script font choice. These are the settings people actually change.

**Contrast is validated, not eyeballed.** A build check asserts every token pair on every
ground clears the contrast threshold. A theme that fails does not ship.

### 3.4 Recitation

Three asks: offline MP3s of well-known reciters, single-ayah playback, and audio that
follows you to the next ayah.

**Per-ayah files are the unit.** Recitations are distributed as one file per ayah
(`XXXYYY.mp3` — `002255.mp3` is 2:255), which makes "play this ayah only" native: no
seeking inside a surah-length file, no drift, no cut-off endings.

**Reciter packs download per juz, not whole-Qur'an.** A complete reciter at 128 kbps is
roughly 800 MB–1.2 GB; a single juz is ~25–40 MB. Show the size before the download,
show what is on disk, and allow deleting a juz without deleting the reciter.

**Playback modes:**

| Mode | Behaviour |
|---|---|
| Single ayah | Plays once and stops. The default. |
| Through the passage | Continues to the end of the current passage |
| Through the surah | Continues to the end of the surah |
| **Repeat ×N** | Repeats one ayah a set number of times — the memorisation mode |
| Follow along | Audio drives the scroll; word highlighting where the reciter has segment timestamps (not all do) |

**Auto-advance is off by default.** Audio starting by itself is the fastest way to
embarrass a reader in a quiet room. It is one toggle away, and once set it is remembered.

**Reciters** — Ḥuṣarī, ʿAbd al-Bāsit, Minshāwī, Sudais, Shuraim, Alafasy, Ayyūb,
ad-Dussarī and others; per-reciter availability, quality and rights tracked in
`SOURCES.md`.

**We fetch; we do not redistribute.** Until rights are cleared, the app downloads audio
from the licensed source onto the reader's own machine for their personal use. It never
ships audio in the installer and never re-serves it. Same discipline as the tafsīr texts
(§6), and the same switch later if rights are granted.

### 3.5 What this adds to the build — and what it doesn't

Adds: an `audio` catalogue and a downloads manifest (in the **user** DB, never the
content DB); a download manager with resume, integrity check and per-juz delete — fiddly,
budget for it properly; 604 QCF page fonts (~20–40 MB) and page-layout data if the mushaf
view ships; word-level data and its rendering; the theme engine and its contrast validator.

**Does not add:** a single hour of scholarly review. None of this touches the content
pipeline or the reviewer's queue. It is app work, it lands in Phase 2, and it does not
move the constraint in §12. That is worth knowing before it feels like scope creep — it
is the one part of the project that can be made as rich as you like without slowing the
content down.

---

## 4. Decisions taken

| Decision | Choice |
|---|---|
| **Tradition** | **Sunni Islam only.** Not comparative religion, not intra-Muslim polemic. Declared openly in-app so a reader knows what they're reading. |
| **Scholarly scope** | Sunni classical + modern. Ṭabarī, Ibn Kathīr, Qurṭubī, Jalālayn, Baghawī, Rāzī, Bayḍāwī, Ibn ʿAṭiyyah + modern (Maʿārif al-Qurʾān, Tafhīm al-Qurʾān, al-Saʿdī). One coherent editorial voice. |
| **How L1/L2/L3 get written** | AI-drafted strictly from cited source passages → **human review** → frozen as fixed content. No unreviewed text reaches a reader. No live generation. |
| **Licensing posture** | Build the full corpus for **personal use now**; clear redistribution rights before any public release. Architecture keeps licensed and open content separable so this stays a switch, not a rewrite. |
| **Audience** | Layman *and* student, served by one content set through a persistent **reading depth** setting that changes defaults, never availability (§2.1). |
| **Verse linking** | A cross-reference graph built from **scholar-asserted** links extracted from the tafsīr itself. No unattributed similarity-search "related verses" (§2.2). |
| **Arabic script** | Flowing Unicode text is the reading column (Uthmani default, IndoPak / Imlaei / Uthmani-simple selectable). Page-faithful QCF mushaf is a **separate view**, not a setting on the reading column (§3.1). |
| **Themes** | One engine, two axes: 4 grounds × 8 accents generated in OKLCH from a single hue, plus a free hue slider. The accent never colours the Qur'anic text (§3.3). |
| **Recitation** | Per-ayah MP3s; single-ayah play is the default; auto-advance ships **off**. Reciter packs download per juz. We fetch from the licensed source, never redistribute (§3.4). |
| **Stack** | TypeScript/React UI → **Tauri 2** desktop first → same UI as web app → Capacitor for iOS/Android. Content pipeline in Python. |

---

## 5. The finding that reshapes the plan

**Most of the great Sunni tafsīrs do not exist in complete English translation.**

This is the single most important fact for scoping. The brief was "all the tafsir
available in English" — that set is much smaller than it appears:

| Work | Complete English translation? |
|---|---|
| Tafsīr al-Jalālayn | ✅ Yes (Feras Hamza, Royal Aal al-Bayt) |
| Tanwīr al-Miqbās (attr. Ibn ʿAbbās) | ✅ Yes (Guezzou, Royal Aal al-Bayt) |
| Asbāb al-Nuzūl, al-Wāḥidī | ✅ Yes (Guezzou, Royal Aal al-Bayt) |
| Tafsīr al-Tustarī | ✅ Yes (Keeler, Royal Aal al-Bayt) |
| Tafsīr Ibn Kathīr (abridged) | ✅ Yes (Darussalam, 10 vols) — **copyrighted** |
| Maʿārif al-Qurʾān | ✅ Yes (8 vols) — **copyrighted** |
| Tafhīm al-Qurʾān | ✅ Yes — **copyrighted** |
| Tafsīr al-Saʿdī | ✅ Yes — **copyrighted** |
| **Tafsīr al-Ṭabarī** | ❌ Partial only (Cooper, vol. 1 — abandoned) |
| **Tafsīr al-Qurṭubī** | ❌ Partial only |
| **Mafātīḥ al-Ghayb (al-Rāzī)** | ❌ No |
| **Maʿālim al-Tanzīl (al-Baghawī)** | ❌ No |
| **al-Muḥarrar al-Wajīz (Ibn ʿAṭiyyah)** | ❌ No |
| **al-Taḥrīr wa'l-Tanwīr (Ibn ʿĀshūr)** | ❌ No |

So "full scholarly views" splits into two tiers:

- **Tier A — existing English.** Ingest, align, cite. Straightforward engineering.
- **Tier B — Arabic originals we render into English ourselves.** This is where
  Ṭabarī, Qurṭubī, Rāzī, Baghawī, Ibn ʿAṭiyyah and Ibn ʿĀshūr live — i.e. most of
  the depth. It is a translation-and-summarisation task, and it **requires a reviewer
  who reads classical Arabic.** It cannot be signed off by an English-only reader.

**Recommendation:** ship Tier A first as a complete, honest product. Add Tier B
sources surah by surah as Arabic-competent review capacity allows, with every Tier B
passage clearly labelled *"rendered into English by Bayān from the Arabic original;
not a published translation."* Never let a Tier B rendering be mistaken for a
published translation.

This does not shrink the ambition. It sequences it so that what ships is always true.

---

## 6. Source register

Full detail, per source, in [`SOURCES.md`](SOURCES.md). Summary:

### Qur'anic text
- **Tanzil** Uthmānī text, CC BY — verbatim, checksum-verified, never AI-touched.

### Translations (L0)
- Open/permissive: Pickthall, Yusuf Ali (public domain), Ṣaḥīḥ International (via Tanzil, CC BY-ND — verbatim only).
- Licensed: The Clear Qur'an (Khattab), Abdel Haleem (OUP). Personal-use now; clear before release.

### Context of revelation (L2)
- **Asbāb al-Nuzūl of al-Wāḥidī**, tr. Guezzou — the primary source.
- Cross-checked against Ibn Kathīr and Jalālayn, with authenticity grading noted.
- Where a report is weak or disputed, we say so rather than omitting it.

### Tafsīr (L3)
- **Tier A (English exists):** Jalālayn, Ibn ʿAbbās, Tustarī, Bayḍāwī (partial), Ibn Kathīr, Maʿārif al-Qurʾān, Tafhīm, al-Saʿdī.
- **Tier B (Arabic → our rendering):** Ṭabarī, Qurṭubī, Rāzī, Baghawī, Ibn ʿAṭiyyah, Ibn ʿĀshūr.

### Practical acquisition routes
- **Quran Foundation / Quran.com API v4** (`/resources/tafsirs`, `/tafsirs/{id}/by_ayah/{key}`) — already ayah-aligned; the fastest route to Tier A.
- **QUL (Quranic Universal Library, Tarteel)** — SQLite/JSON bulk downloads of translations, tafsirs, word-by-word data.
- **altafsir.com (Royal Aal al-Bayt)** — the commissioned English translations; also the Arabic originals for Tier B.
- **spa5k/tafsir_api** — 122 tafsirs as JSON over CDN; useful for prototyping, verify provenance before trusting.

> ⚠️ Every one of these has its own terms. `SOURCES.md` tracks licence status per
> source and is the gate for public release. Nothing ships publicly until its row is green.

---

## 7. Content architecture

### The key modelling insight

**The ayah is not the unit of meaning.** Tafsīr works comment on *passages* — a few
ayat that form one argument or one narrative beat. Ibn Kathīr will cover 2:1–5 in one
block. If the data model is ayah-only, we end up either duplicating the same
commentary five times or chopping it into nonsense.

So the model carries **both**: ayat for addressing and search, passages for meaning.

```
source            — a work: author, era, school, language, licence, tier (A/B)
surah             — 114
ayah              — 6,236; arabic text, transliteration, ordinal position
passage           — contiguous ayah range + theme; the unit L1/L2/L3 attach to
translation_text  — (translation_source, ayah) → verbatim text
tafsir_segment    — (source, ayah_range) → raw commentary text + provenance hash
summary           — (passage) → L1 plain-English text, status, reviewer, version
context_note      — (passage) → L2: setting, placement in surah, asbab + grading
scholarly_view    — (passage) → one position: statement, evidence, holders[], citations[]
ikhtilaf_group    — (passage) → clusters scholarly_views into agreement / divergence
cross_reference   — (from_ayah_range → to_ayah_range) typed edge: relation, direction,
                    asserting source + locator, note. NO EDGE WITHOUT A SOURCE.
topic             — a concept thread (patience, orphans, naskh, the Sabbath)
topic_membership  — (topic, passage) → ordered position in the thread
citation          — (any generated text span) → source + locator. NOT NULLABLE.
review_record     — who reviewed what, when, verdict, notes

  presentation — content DB, but carries no review burden
script_edition    — Uthmani | Uthmani-simple | IndoPak | Imlaei → text per ayah
mushaf_layout     — layout id → page / line / word placement for the page view
word              — (ayah, position) → arabic, translation, transliteration, tajwid
reciter           — id, name, style, bitrate, has_segment_timestamps, licence
ayah_audio        — (reciter, ayah) → file locator, duration, byte size
audio_segment     — (reciter, ayah, word) → start/end ms, where timestamps exist

  user DB — never the content DB
theme_pref        — ground, accent hue, sizes, line height, column width, fonts
audio_download    — (reciter, juz) → state, bytes on disk, checksum
```

Two constraints do most of the safety work:

1. **`citation` is not nullable.** Every generated sentence in L1/L2/L3 carries at
   least one citation into a `tafsir_segment`. Content with an uncited span cannot
   reach `status = approved`. This is enforced in the database, not in a prompt.
2. **Raw source text is immutable and hashed.** If a source is re-ingested and the
   hash changes, every derived summary flips to `needs_re-review`.
3. **`cross_reference` requires an asserting source.** Every edge names the scholar or
   work that drew the connection, so a link is a citation like any other claim. This is
   what keeps the graph trustworthy rather than merely dense (§2.2).

### Storage

- **Content DB** — SQLite, read-only, shipped with the app. FTS5 for full-text search
  across translations, summaries and tafsīr.
- **User DB** — separate SQLite: bookmarks, notes, reading position, highlights.
  Separate file so content updates never risk user data.
- **Licensed content** — separate attachable DB file. Personal build attaches it;
  a future public build does not. Licensing becomes a build flag.

---

## 8. The content pipeline

A Python pipeline, run offline, producing the frozen content DB. Ten stages:

```
1. INGEST     fetch source texts → normalise → store raw + provenance hash
2. ALIGN      map each work's commentary blocks onto ayah ranges
3. SEGMENT    define passages (ruku' boundaries + thematic review)
4. EXTRACT    LLM pulls candidate positions + evidence, each with a verbatim
              quote span back into the source text
4b. LINK      pull every ayah a mufassir cites while commenting → typed
              cross_reference edges, each carrying its asserting source
5. CLUSTER    group equivalent positions across works → agreement vs. ikhtilaf
6. DRAFT      generate L1 summary + L2 context, constrained to clustered material
7. VERIFY     automated gates (see below)
8. REVIEW     human queue: approve / edit / reject, signed and recorded
9. FREEZE     approved content versioned, content-addressed, built into the DB
```

**Stage 4b (LINK) is what makes verse-to-verse navigation possible.** It is cheap to
run alongside EXTRACT — the mufassir's citations of other ayat are already in the text
being read — and it is the difference between a corpus and a connected one. Edges are
reviewed in bulk (each is one assertion with one citation) rather than passage by passage.

**Stage 2 (ALIGN) is the hard engineering problem.** Tier A sources from the
Quran.com API arrive pre-aligned. Everything else — PDFs, scraped pages, Arabic
originals — is unaligned prose that mentions ayat inline. Expect this to be the
largest single engineering effort, and expect it to need a human spot-check pass.

**Stage 7 (VERIFY) — automated gates, all blocking:**

- Every generated sentence maps to ≥1 citation with a resolvable source locator
- Every quoted translation matches the licensed text byte-for-byte
- Arabic text unchanged from Tanzil (checksum)
- No fiqh ruling stated in imperative voice (flagged for review — see §9)
- No claim of consensus (*ijmāʿ*) unless a source explicitly asserts it
- Reading level of L1 ≤ grade 9 (it is for everyday folk; measure it, don't hope)
- Named scholars appear in the source register with matching era/school

**Model tiering** — cost control without cutting corners where it counts:
- ALIGN, EXTRACT: cheaper fast model, high volume, mechanical
- CLUSTER, DRAFT: strongest model — this is where judgement lives
- VERIFY: deterministic code wherever possible, model only for the fuzzy checks

---

## 9. Editorial policy

Full text in [`EDITORIAL-POLICY.md`](EDITORIAL-POLICY.md). The non-negotiables:

1. **Traceability.** Nothing reaches a reader that isn't traceable to a named source
   with a locator. If we can't cite it, we don't say it.
2. **The Arabic is never touched.** Verbatim from Tanzil, checksum-verified at build.
3. **Translations are quoted, never paraphrased.** An AI never rewords a translation.
4. **We do not issue fatāwā.** Where an ayah bears on a ruling, we report what
   scholars held and say plainly that practical rulings need a qualified scholar who
   knows your circumstances.
5. **Ikhtilāf is reported, not resolved.** Where scholars genuinely differ, we show
   the difference. We never manufacture a consensus for tidiness, and we never hide a
   minority position held by a recognised authority.
6. **Weak reports are labelled.** Especially in asbāb al-nuzūl, where weak narrations
   circulate widely. Grading is shown, not silently dropped.
7. **The reader always sees what is source and what is ours.** Visual and typographic
   distinction between quoted tafsīr and Bayān's own summary. No blurred line.
8. **Accountability is visible.** Every passage shows its content version and that it
   was reviewed. A reader can see who stands behind the words.
9. **Corrections are first-class.** In-app "report an issue" on every passage, routed
   to the review queue. Errors will happen; the response to them is the credibility.
10. **The tradition is declared, not assumed.** Bayān presents Sunni classical and
    modern scholarship. That is stated plainly in-app so a reader always knows what
    they are reading — not smuggled in as neutrality, and not a position in an
    intra-Muslim polemic.
11. **Every link is a claim.** A cross-reference names the scholar or work that drew
    it. No unattributed "related verses" (§2.2).

---

## 10. Application architecture

### Desktop (Phase 2 — first shipped target)

```
Tauri 2 shell (Rust)
└── React 18 + TypeScript + Tailwind
    ├── Reader        L0→L3 progressive disclosure at the chosen reading depth
    ├── Palette       ⌘K jump-to-anything: address, surah name, epithet, free text
    ├── PeekCard      hover/tap preview of a linked ayah — no navigation on first touch
    ├── Trail         breadcrumb of hops + back/forward history
    ├── Threads       topic threads across the Qur'an, from same-topic edges
    ├── Search        FTS5 across translation, summary, tafsir
    ├── Compare       side-by-side translations / side-by-side mufassirun
    ├── Notes         personal notes + bookmarks (user DB)
    ├── Mushaf        page-faithful QCF view — its own screen, not a reader setting
    ├── Appearance    ground × accent, script edition, fonts, sizes, saved themes
    ├── Player        per-ayah audio: single / passage / surah / repeat ×N / follow
    ├── Downloads     reciter packs by juz — size, progress, resume, delete
    └── Sources       the register: who each scholar was, era, school, licence
└── SQLite: content.db (read-only) + user.db (read-write)
```

**Routing is the ayah address.** `/2:255` is the canonical route, deep link and share
target; the trail is browser history, so back works exactly as a reader expects. This
falls out for free on web and mobile later, and it is why the address is the route
rather than an internal id.

Tauri over Electron: ~10 MB binary vs ~150 MB, native SQLite, and the React layer
ports unchanged to web and mobile. The Rust surface stays thin — file access, DB
handle, window chrome — so it doesn't become a second thing to maintain.

### The reading experience

At **Plain** depth the screen opens at L0 + L1: the ayah, a translation, and one plain
paragraph. That is the whole default view. No wall of text.

Below it, three collapsed disclosures — *Context* · *What scholars said* ·
*Full tafsīr texts*. Each expands in place. Reading depth (§2.1) sets which of these
start open; it never removes one. Passage-level content renders once, at the head of
its ayah range, with the range marked — never repeated per ayah.

Linked ayat appear inline in the text as quiet references. Hover or tap gives a peek
card; a second, deliberate action navigates and pushes onto the trail (§2.2). The
common case — a reader glancing at what Ibn Kathīr is pointing to and carrying on —
costs no navigation at all.

### Review tool (built before the reader app)

Reviewers need a tool in Phase 1, long before the reader app exists. A local
FastAPI + React app over the same content DB: queue, side-by-side draft vs. sources,
inline edit, approve/reject with notes. Sharing React components with the reader app
means this is largely reused, not thrown away.

### Web and mobile (Phases 4–5)

- **Web:** same React build. Either a small read API, or ship SQLite to the browser
  via WASM + OPFS for a fully offline web app. Decide when we get there.
- **Mobile:** Capacitor wrapping the same React. Content DB bundled for offline —
  the app must work on a plane and in a masjid with no signal.

---

## 11. Phasing

| Phase | Weeks | Deliverable | Gate to next phase |
|---|---|---|---|
| **0 — Corpus spike** | 1–2 | Ingest Tanzil + Jalālayn + Wāḥidī + one API tafsīr for al-Fātiḥa and al-Baqara 1–20. Prove alignment works. | Alignment accurate on a hand-checked sample |
| **1 — Pipeline + review tool** | 3–8 | Full 10-stage pipeline incl. link extraction. Review tool. **Pilot corpus: al-Fātiḥa + Juz ʿAmma** (38 surahs, 601 ayat) with its cross-reference graph and ~60–100 topic threads. | Pilot corpus and its edges fully human-reviewed |
| **2 — Desktop reader v1** | 9–16 | Tauri app over the pilot corpus. Reader with depth modes, ⌘K palette, peek cards + trail, threads, search, notes, sources — **plus** the theme engine, script switching, and per-ayah audio with downloads. | You use it daily and want to keep using it |
| **2b — Mushaf page view** | after 2 | QCF page fonts + layout data as a separate screen. Deferrable without blocking anything else. | — |
| **3 — Scale to full Qur'an** | 15–40+ | Pipeline across all 114 surahs. Review juz by juz, longest surahs last. | Review throughput sustained; §12 is the real constraint |
| **4 — Licensing + web** | parallel from wk 20 | Clear redistribution rights. Web app. | Green rows in `SOURCES.md` |
| **5 — Mobile** | after 4 | iOS/Android via Capacitor. | — |
| **Tier B (Arabic sources)** | from wk 20 | Ṭabarī, Qurṭubī, Rāzī et al., surah by surah | Arabic-competent reviewer secured |

**Why Juz ʿAmma as the pilot:** 38 short surahs, ~601 ayat, the passages most Muslims
actually read and memorise, rich in both narrative and legal-theological content, and
small enough to review completely. It exercises every part of the system on content
that is immediately useful to you.

---

## 12. The real constraint: review capacity

Be clear-eyed about this. Engineering is not the bottleneck.

- Working at passage level, the Qur'an is roughly **1,500–2,000 passages**, plus the
  cross-reference edges — which review far faster, in bulk, since each is a single
  assertion with a single citation. Budget them at roughly 10% on top, not double.
- Qualified review of a drafted passage — reading the sources, checking the citations,
  correcting the summary — is realistically **15–30 minutes**.
- That is **400–1,000 hours** of qualified scholarly review for full coverage.

At 10 hours/week that is 1–2 years. At 30 hours/week, 4–8 months. This is the number
that determines the project's timeline — not the code.

**Implications for the plan:**
- Ship by juz, not big-bang. Juz ʿAmma alone is a genuinely useful product.
- Design the review tool for throughput from day one — it is the critical path tool.
- Budget for paid reviewer time; treat it as the main line item, not an afterthought.
- Anything that lets a reviewer approve a passage 5 minutes faster is worth more
  engineering effort than almost any reader-facing feature.

**LLM cost** is comparatively minor: with model tiering, a full pass over ~1,750
passages lands in the **low thousands of pounds**, and reruns cost the same again —
so freeze aggressively and don't rerun approved content without cause.

---

## 13. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Getting religious content wrong** | Critical | Every safeguard in §9. Human review is mandatory, never optional. Corrections path is first-class. This risk is why we don't ship live-generated text. |
| **Review capacity below plan** | High | Ship per-juz. Optimise the review tool relentlessly. Pay for reviewer time. |
| **Licensing blocks public release** | High | Licensed content in a separable DB from day one. Open-licensed core is a complete product on its own. Start permission conversations in Phase 1, not Phase 4. |
| **Tier B needs Arabic-competent review** | High | Tier A is a complete product. Tier B is strictly additive, per-surah, and clearly labelled. Never blocks a release. |
| **Alignment of unaligned prose is harder than expected** | Medium | Phase 0 exists to find this out in two weeks, not six months. Prefer pre-aligned API sources where they exist. |
| **Audio rights and storage** | Medium | Fetch from the licensed source to the reader's own disk; never bundle or re-serve. Per-juz packs keep disk use in the reader's hands. Per-reciter rights tracked in `SOURCES.md` like everything else. |
| **Presentation outgrowing the content** | Medium | Themes, scripts and audio add no reviewer hours (§3.5) — but they can absorb unlimited engineering. Phase 2 ships one solid pass; the mushaf page view is explicitly Phase 2b. |
| **Scope creep** | Medium | What is out stays out, and the list lives in §14. What comes in gets costed there and then, as audio and word-by-word were. |
| **Sole-maintainer bus factor** | Medium | Content DB is a plain SQLite file with an open schema. Pipeline is deterministic and re-runnable. Nothing is locked in a service. |

---

## 14. Explicitly out of scope for v1

**Moved in.** Audio recitation, word-by-word and tajwīd colouring were on this list.
They are now in scope (§3) at your request. They cost engineering, not review hours.

Still out, recorded so they stop being open questions: Arabic-language UI;
memorisation/ḥifẓ *tracking* (the repeat-×N playback mode covers the practical need
without the bookkeeping); prayer times; social or sharing features; user accounts and
cloud sync; languages other than English. Several are good ideas. None of them are v1.

On navigation specifically, also out of scope for v1: a visual graph explorer of the
cross-reference network (looks impressive, helps nobody read); AI chat over the corpus
(violates §9 rule 1); and an exhaustive topic ontology — the pilot gets 60–100 threads
that earn their place, not a taxonomy of everything.

---

## 15. Immediate next steps

1. **Confirm the pilot corpus** — al-Fātiḥa + Juz ʿAmma, or a different starting set.
2. **Identify the reviewer.** Who signs off content? If it's you, be honest about
   hours/week. If it's a scholar you'll engage, start that conversation now — §12 says
   it's the critical path and everything else is downstream of it.
3. **Move this to its own repository.** `quran-shorts-agent` is a video tool; this is
   a different product with a different lifetime. Suggest `GoldCyberCommand/bayan`.
4. **Start Phase 0.** Two weeks, one question: does alignment work? Concretely — pull
   al-Fātiḥa and al-Baqara 1–20 from the Quran.com API and altafsir.com, align them,
   and hand-check the result.
5. **Open the licensing conversations** — Darussalam (Ibn Kathīr), Maktaba Maʿārif
   al-Qurʾān, Royal Aal al-Bayt (their English translations). These take months, so
   they start now and run in the background.

---

## Appendix: relationship to existing projects

- **quran-shorts-agent** (this repo) — cuts recitation videos into YouTube Shorts.
- **QAAM** — renders recitation videos with word-by-word tajwīd-coloured mushaf text.
- **Bayān** (this plan) — the commentary app.

They share a domain and an audience, not a codebase. One future link worth noting:
Bayān's L1 plain-English summaries are exactly the right caption text for Shorts
produced by the other two. Worth revisiting once the corpus exists — not a v1 concern.
