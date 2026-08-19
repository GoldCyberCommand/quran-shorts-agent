# Editorial policy

The rules that govern what Bayān is allowed to say. These are not aspirations — most
are enforced in the pipeline as blocking checks (§10), and the rest are review criteria
a reviewer signs against.

> This is scripture. A software bug is embarrassing; getting this wrong misleads someone
> about their religion. The whole architecture is built around that asymmetry.

---

## 1. Traceability

Nothing reaches a reader that is not traceable to a named source with a locator.

- Every generated sentence in L1 (plain English), L2 (context) and L3 (scholarly views)
  carries ≥1 citation into a stored source passage.
- The `citation` field is **not nullable**. Content with an uncited span cannot reach
  `status = approved`. Enforced by the database, not by a prompt.
- A reviewer can see, for any sentence, the exact source text it came from.
- **If we cannot cite it, we do not say it.** No "scholars generally hold…" with nothing
  behind it. No plausible-sounding connective tissue.

## 2. The Arabic is never touched

The Qur'anic text is verbatim from Tanzil, checksum-verified at every build. No model
ever sees it in a writing context, only a reading one. A checksum mismatch fails the
build.

## 3. Translations are quoted, never paraphrased

An AI never rewords a translation. Translations are quoted byte-for-byte from the
licensed text, verified against the source at build time. Ṣaḥīḥ International is CC BY-ND
— no-derivatives means exactly this. Where a translation is quoted partially, the
truncation is marked.

## 4. We do not issue fatāwā

Bayān reports what scholars have held. It does not tell a reader what to do.

- Where an ayah bears on a practical ruling, we present the positions and their evidence.
- The pipeline flags any generated sentence in imperative or prescriptive voice on a
  fiqh matter for mandatory review.
- Passages touching rulings carry a standing note: practical questions need a qualified
  scholar who knows your circumstances.
- We never present one madhhab's ruling as *the* Islamic ruling.

## 5. Ikhtilāf is reported, not resolved

Where scholars genuinely differ, we show the difference.

- Never manufacture consensus for tidiness or brevity.
- Never hide a minority position held by a recognised authority.
- A claim of *ijmāʿ* is only made where a source explicitly asserts it — and then it is
  attributed to that source, not stated in Bayān's own voice.
- Where the mainstream reading is clear and a minority view is genuinely marginal, say
  both things: what most held, and what the minority held. Proportion is editorial, but
  omission is not.

## 6. Weak reports are labelled

Especially in asbāb al-nuzūl, where weak narrations circulate widely and confidently.

- Every asbāb report carries an authenticity grading from its source.
- Disputed reports are shown as disputed, with who disputed them.
- We do not silently drop weak reports — a reader who has heard one elsewhere is better
  served by seeing it labelled than by not finding it.

## 7. The reader always sees what is source and what is ours

- Quoted tafsīr and Bayān's own summary are visually and typographically distinct.
- Tier B material (Arabic originals rendered into English by Bayān) is labelled on every
  passage: *"rendered into English by Bayān from the Arabic original; not a published
  translation."* Never buried in settings.
- The L1 plain-English summary is clearly Bayān's own writing, grounded in cited
  sources — never presented as any scholar's words.

## 8. Register and reading level

L1 is for everyday folk. That is a measurable property, not a hope.

- Target reading level ≤ grade 9, measured in the pipeline and blocking above threshold.
- Plain English: no untranslated technical term without an inline gloss on first use.
- Transliterated Arabic terms are always glossed (*asbāb al-nuzūl* — the circumstances
  in which a passage was revealed).
- Warm and clear, never patronising. The reader is intelligent and simply not a specialist.

## 9. Accountability and corrections

- Every passage shows its content version and reviewed status.
- "Report an issue" on every passage, routed into the review queue.
- Corrections are versioned; a corrected passage records what changed and why.
- Errors will happen. The response to them is where the credibility actually lives.

## 10. Pipeline gates (all blocking)

Automated, run before any content can enter human review:

| Gate | Check |
|---|---|
| Citation completeness | every generated sentence maps to ≥1 resolvable citation |
| Translation fidelity | quoted translations match the licensed text byte-for-byte |
| Arabic integrity | Tanzil checksum matches |
| Prescriptive voice | no fiqh ruling in imperative voice → flag for mandatory review |
| Consensus claims | no *ijmāʿ* claim unless a source explicitly asserts it |
| Reading level | L1 ≤ grade 9 |
| Scholar identity | named scholars exist in the source register with matching era/school |
| Source integrity | source hash unchanged since the derived content was approved |

A failed gate blocks the passage. Gates are never disabled to hit a milestone.

## 11. Human review is mandatory

- No content reaches a reader without a recorded human approval.
- The reviewer sees the draft and its sources side by side, and approves, edits, or rejects.
- Approval is signed and recorded in `review_record` — reviewer, timestamp, verdict, notes.
- Tier B (Arabic-sourced) content requires a reviewer who reads classical Arabic. An
  English-only reviewer cannot approve Tier B, and the tool enforces that.
- Re-ingesting a source flips all derived content to `needs_re-review`.

## 11a. Every link is a claim

A cross-reference between two ayat is a claim about the text and is governed by rule 1
like any other.

- Every edge names the scholar or work that asserted it, with a locator.
- Links are extracted from what a mufassir actually cites while commenting — not
  generated by keyword or embedding similarity. An unattributed "related verses" list
  cannot ship.
- Edge *type* is part of the claim and is shown to the reader: an `explains` link and a
  `same-topic` link are different assertions and must not look alike.
- **Abrogation edges are shown as discussion, never as verdict.** *Naskh* is contested
  ground; Bayān reports which scholars argued what, and never presents a verse as
  settled-abrogated in its own voice.
- Edges are reviewed like any other content. They review fast in bulk, but they are
  reviewed.

---

## 12. What Bayān is not

- Not a fatwa service.
- Not a substitute for a teacher. The app says so, in the app.
- Not a position in an intra-Muslim polemic. **Sunni Islam only** — classical and
  modern — is the declared scope (see PLAN.md §3), stated plainly in-app so a reader
  always knows what tradition they are reading. Declared scope is honest; silent scope
  presented as neutrality is not. Within that scope the four madhāhib and the range of
  recognised Sunni positions are all represented; no one school speaks for the whole.
- Not a live AI chatbot over scripture. Content is drafted offline, reviewed by a human,
  and frozen. A reader and a scholar looking at the same ayah see the same words.
