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

Two things have to be true at once for that to work. The content has to be
comprehensive and honestly sourced (§4–§8). And the app has to be **easy to move
through** — clean enough that nothing distracts from the text, and connected enough
that you can follow an explanation from one verse to another without losing your place
(§2). Navigation is not polish here; it is half the product.

Scope is **Sunni Islam only** — classical and modern, stated plainly so a reader always
knows what tradition they are reading (see §3 and §8 rule 10).

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
data, which means the pipeline has to extract them (stage 4b, see §7).

**Where links come from — and why that matters.** The valuable links are the ones
*scholars themselves assert*. When Ibn Kathīr explains 2:2 by citing 41:44, that is a
scholar-asserted link: it is meaningful, it is citable, and it is reviewable. Keyword
similarity and embedding proximity produce plausible-looking links that no scholar ever
drew — they are unciteable, and under §8 rule 1 they cannot ship. So:

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
- **Source and summary always visually distinct** (§8 rule 7) — the one place where a
  visual boundary is non-negotiable.
- **No engagement furniture.** No streaks, badges, popups, or nudges. The reader came to
  read.

**Ruled out by the above:** a tab bar of eight tafsīr works across the top; verse cards
in a scrolling feed; L3 rendered as an undifferentiated wall of text; anything that
requires horizontal scrolling; modal dialogs in the reading path.

### 2.5 What this adds to the build

Navigation as a first-class objective is not free. It adds, concretely:

- a `cross_reference` table and the extraction stage that populates it (§6, §7);
- reviewer workload — every extracted edge is content and needs approving, though edges
  review fast in bulk since each is one assertion with one citation;
- peek-card rendering, trail state, and command-palette search in the app;
- a topic taxonomy, which is genuinely editorial work and should start small — perhaps
  60–100 threads for the pilot rather than an exhaustive ontology.

Sequenced in §10: links are extracted from Phase 1 so the pilot corpus has a real graph
inside Juz ʿAmma, and the graph gets denser with every juz added.

---

## 3. Decisions taken

| Decision | Choice |
|---|---|
| **Tradition** | **Sunni Islam only.** Not comparative religion, not intra-Muslim polemic. Declared openly in-app so a reader knows what they're reading. |
| **Scholarly scope** | Sunni classical + modern. Ṭabarī, Ibn Kathīr, Qurṭubī, Jalālayn, Baghawī, Rāzī, Bayḍāwī, Ibn ʿAṭiyyah + modern (Maʿārif al-Qurʾān, Tafhīm al-Qurʾān, al-Saʿdī). One coherent editorial voice. |
| **How L1/L2/L3 get written** | AI-drafted strictly from cited source passages → **human review** → frozen as fixed content. No unreviewed text reaches a reader. No live generation. |
| **Licensing posture** | Build the full corpus for **personal use now**; clear redistribution rights before any public release. Architecture keeps licensed and open content separable so this stays a switch, not a rewrite. |
| **Audience** | Layman *and* student, served by one content set through a persistent **reading depth** setting that changes defaults, never availability (§2.1). |
| **Verse linking** | A cross-reference graph built from **scholar-asserted** links extracted from the tafsīr itself. No unattributed similarity-search "related verses" (§2.2). |
| **Stack** | TypeScript/React UI → **Tauri 2** desktop first → same UI as web app → Capacitor for iOS/Android. Content pipeline in Python. |

---

## 4. The finding that reshapes the plan

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

## 5. Source register

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

## 6. Content architecture

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

## 7. The content pipeline

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
- No fiqh ruling stated in imperative voice (flagged for review — see §8)
- No claim of consensus (*ijmāʿ*) unless a source explicitly asserts it
- Reading level of L1 ≤ grade 9 (it is for everyday folk; measure it, don't hope)
- Named scholars appear in the source register with matching era/school

**Model tiering** — cost control without cutting corners where it counts:
- ALIGN, EXTRACT: cheaper fast model, high volume, mechanical
- CLUSTER, DRAFT: strongest model — this is where judgement lives
- VERIFY: deterministic code wherever possible, model only for the fuzzy checks

---

## 8. Editorial policy

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

## 9. Application architecture

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

## 10. Phasing

| Phase | Weeks | Deliverable | Gate to next phase |
|---|---|---|---|
| **0 — Corpus spike** | 1–2 | Ingest Tanzil + Jalālayn + Wāḥidī + one API tafsīr for al-Fātiḥa and al-Baqara 1–20. Prove alignment works. | Alignment accurate on a hand-checked sample |
| **1 — Pipeline + review tool** | 3–8 | Full 10-stage pipeline incl. link extraction. Review tool. **Pilot corpus: al-Fātiḥa + Juz ʿAmma** (38 surahs, 601 ayat) with its cross-reference graph and ~60–100 topic threads. | Pilot corpus and its edges fully human-reviewed |
| **2 — Desktop reader v1** | 9–14 | Tauri app over the pilot corpus. Reader with depth modes, ⌘K palette, peek cards + trail, threads, search, notes, sources. | You use it daily and want to keep using it |
| **3 — Scale to full Qur'an** | 15–40+ | Pipeline across all 114 surahs. Review juz by juz, longest surahs last. | Review throughput sustained; §11 is the real constraint |
| **4 — Licensing + web** | parallel from wk 20 | Clear redistribution rights. Web app. | Green rows in `SOURCES.md` |
| **5 — Mobile** | after 4 | iOS/Android via Capacitor. | — |
| **Tier B (Arabic sources)** | from wk 20 | Ṭabarī, Qurṭubī, Rāzī et al., surah by surah | Arabic-competent reviewer secured |

**Why Juz ʿAmma as the pilot:** 38 short surahs, ~601 ayat, the passages most Muslims
actually read and memorise, rich in both narrative and legal-theological content, and
small enough to review completely. It exercises every part of the system on content
that is immediately useful to you.

---

## 11. The real constraint: review capacity

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

## 12. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Getting religious content wrong** | Critical | Every safeguard in §8. Human review is mandatory, never optional. Corrections path is first-class. This risk is why we don't ship live-generated text. |
| **Review capacity below plan** | High | Ship per-juz. Optimise the review tool relentlessly. Pay for reviewer time. |
| **Licensing blocks public release** | High | Licensed content in a separable DB from day one. Open-licensed core is a complete product on its own. Start permission conversations in Phase 1, not Phase 4. |
| **Tier B needs Arabic-competent review** | High | Tier A is a complete product. Tier B is strictly additive, per-surah, and clearly labelled. Never blocks a release. |
| **Alignment of unaligned prose is harder than expected** | Medium | Phase 0 exists to find this out in two weeks, not six months. Prefer pre-aligned API sources where they exist. |
| **Scope creep** (audio, word-by-word, tajwīd, Arabic UI) | Medium | Explicitly out of scope for v1. The list lives in §13 and stays there. |
| **Sole-maintainer bus factor** | Medium | Content DB is a plain SQLite file with an open schema. Pipeline is deterministic and re-runnable. Nothing is locked in a service. |

---

## 13. Explicitly out of scope for v1

Recorded so they stop being open questions: audio recitation and playback; word-by-word
Arabic morphology; tajwīd colouring; Arabic-language UI; memorisation/ḥifẓ tools;
prayer times; social or sharing features; user accounts and sync; languages other than
English. Several are good ideas. None of them are v1.

On navigation specifically, also out of scope for v1: a visual graph explorer of the
cross-reference network (looks impressive, helps nobody read); AI chat over the corpus
(violates §8 rule 1); and an exhaustive topic ontology — the pilot gets 60–100 threads
that earn their place, not a taxonomy of everything.

---

## 14. Immediate next steps

1. **Confirm the pilot corpus** — al-Fātiḥa + Juz ʿAmma, or a different starting set.
2. **Identify the reviewer.** Who signs off content? If it's you, be honest about
   hours/week. If it's a scholar you'll engage, start that conversation now — §11 says
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
