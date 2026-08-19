# Source register

Every text Bayān uses, what it costs us legally, and whether it can ship.

**This file is the release gate.** No source ships in a public build until its
**Public release** column is ✅. Personal builds may use anything marked 🟡.

Legend — **Public release:** ✅ clear · 🟡 personal use only, permission needed · ❌ blocked
**Tier:** A = published English translation exists · B = Arabic only, Bayān renders into English

---

## 1. Qur'anic text

| Source | Licence | Public release | Notes |
|---|---|---|---|
| Tanzil Uthmānī text | CC BY 3.0 | ✅ | Verbatim only, no modification. Attribution + link to tanzil.net required. Checksum-verified at every build. |
| Tanzil Simple/Clean text | CC BY 3.0 | ✅ | For search indexing and transliteration base. |

**Verify before Phase 1:** Tanzil's own docs state CC BY 3.0; some downstream projects
describe the corpus as CC BY-ND. Read `tanzil.net/docs/text_license` directly and record
the exact terms here. Either way we only ever use it verbatim, so both work.

---

## 2. English translations (L0)

| Translation | Translator | Licence | Public release | Notes |
|---|---|---|---|---|
| The Meaning of the Glorious Koran | Pickthall (1930) | Public domain | ✅ | Dated register but free and complete. |
| The Holy Qur'an | Yusuf Ali (1934) | Public domain (orig.) | ✅ | Original edition only — later revised editions are separately copyrighted. |
| Ṣaḥīḥ International | — | CC BY-ND via Tanzil | ✅ verbatim | No-derivatives: quote exactly, never paraphrase or excerpt mid-sentence. |
| The Clear Qur'an | Mustafa Khattab | Licensed | 🟡 | Most readable modern English; the natural default for L0. Permission required. |
| The Qur'an | M.A.S. Abdel Haleem | © OUP | 🟡 | Excellent prose. OUP licensing likely expensive. |

**Default plan:** ship Ṣaḥīḥ International as the licence-clear default, with The Clear
Qur'an as the preferred default if permission is obtained.

---

## 3. Context of revelation (L2)

| Source | Author / translator | Licence | Public release | Notes |
|---|---|---|---|---|
| Asbāb al-Nuzūl | al-Wāḥidī, tr. Mokrane Guezzou | Royal Aal al-Bayt, free access | 🟡 | The primary asbāb source. Free to read at altafsir.com; **redistribution permission still required**. Ask — a non-profit institute publishing for free is the most likely yes on this list. |
| Asbāb reports within tafsīr | Ibn Kathīr, Jalālayn | see below | — | Used to cross-check and grade. |

**Editorial requirement:** asbāb reports vary widely in authenticity and are frequently
circulated uncritically. Every report shown carries a grading, and disputed ones say so.
See `EDITORIAL-POLICY.md` §6.

---

## 4. Tafsīr — Tier A (published English translation exists)

| Work | Author | d. | School | Translator | Licence | Public release |
|---|---|---|---|---|---|---|
| Tafsīr al-Jalālayn | al-Maḥallī & al-Suyūṭī | 864/911 AH | Shāfiʿī | Feras Hamza | Royal Aal al-Bayt | 🟡 |
| Tanwīr al-Miqbās | attr. Ibn ʿAbbās | — | — | Mokrane Guezzou | Royal Aal al-Bayt | 🟡 |
| Tafsīr al-Tustarī | Sahl al-Tustarī | 283 AH | Sufi | Annabel Keeler | Royal Aal al-Bayt | 🟡 |
| Anwār al-Tanzīl | al-Bayḍāwī | 685 AH | Shāfiʿī | partial | Royal Aal al-Bayt | 🟡 |
| Tafsīr Ibn Kathīr (abridged) | Ibn Kathīr | 774 AH | Shāfiʿī/Atharī | Darussalam, ed. al-Mubārakpūrī | © Maktaba Dar-us-Salam 2003, all rights reserved | 🟡 |
| Maʿārif al-Qurʾān | Mufti Muhammad Shafi | 1976 CE | Ḥanafī | Muhammad Shamim | Copyrighted | 🟡 |
| Tafhīm al-Qurʾān | Abul Aʿla Mawdūdī | 1979 CE | — | Zafar Ansari | Copyrighted | 🟡 |
| Taysīr al-Karīm al-Raḥmān | ʿAbd al-Raḥmān al-Saʿdī | 1376 AH | Ḥanbalī/Salafī | various | Copyrighted | 🟡 |

**Note on the Ibn Kathīr abridgement:** it is a *tahdhīb* — weak narrations were pruned
by the Darussalam editors. Where a passage turns on material the abridgement omits, say
so rather than treating the abridgement as the complete work.

---

## 5. Tafsīr — Tier B (Arabic only; Bayān renders into English)

These carry most of the depth the app promises, and none has a complete English
translation. Every rendering is labelled *"rendered into English by Bayān from the
Arabic original; not a published translation."*

| Work | Author | d. | School | Why it matters |
|---|---|---|---|---|
| Jāmiʿ al-Bayān | al-Ṭabarī | 310 AH | — | The foundational tafsīr bi'l-ma'thūr. Reports the early ikhtilāf with chains — the single richest source for "what scholars said". |
| al-Jāmiʿ li-Aḥkām al-Qurʾān | al-Qurṭubī | 671 AH | Mālikī | The great legal tafsīr; indispensable for āyāt al-aḥkām. |
| Mafātīḥ al-Ghayb | Fakhr al-Dīn al-Rāzī | 606 AH | Shāfiʿī/Ashʿarī | Theological and rational depth. |
| Maʿālim al-Tanzīl | al-Baghawī | 516 AH | Shāfiʿī | Sound, concise, mainstream. |
| al-Muḥarrar al-Wajīz | Ibn ʿAṭiyyah | 542 AH | Mālikī | Superb on linguistic and grammatical difference. |
| al-Taḥrīr wa'l-Tanwīr | Ibn ʿĀshūr | 1393 AH | Mālikī | The outstanding modern Arabic tafsīr; rhetoric and coherence. |

**Blocking prerequisite:** an Arabic-competent reviewer. Tier B does not enter the
pipeline until one is secured. Arabic source texts themselves are pre-modern and out of
copyright; specific printed editions may carry editorial copyright — prefer public
manuscript-derived digital texts (altafsir.com, Shamela) and record the edition used.

---

## 6. Arabic scripts, fonts and mushaf layouts

### Text editions (flowing mode)

| Edition | Source | Licence | Public release |
|---|---|---|---|
| Uthmani (KFGQPC Ḥafṣ) | Tanzil / QUL | CC BY (Tanzil) | ✅ |
| Uthmani simple | Tanzil | CC BY | ✅ |
| IndoPak | QUL | per-resource; verify | 🟡 |
| Imlaei | Tanzil | CC BY | ✅ |

### Fonts

| Font | For | Notes |
|---|---|---|
| Amiri | Flowing Arabic | Open (OFL). A naskh revival; the safe default. |
| Scheherazade New | Flowing Arabic | Open (OFL). Good diacritic clarity. |
| Noto Naskh Arabic | Flowing Arabic | Open (OFL). |
| KFGQPC Uthmanic Ḥafṣ | Flowing Arabic | King Fahd Complex. Free to use; confirm redistribution terms. |
| **QCF v1 / v2 / v4** | **Page view only** | **604 files — one per mushaf page**, each glyph a whole word. Page-perfect and non-reflowing. Confirm King Fahd Complex terms before shipping. |
| Digital Khatt | Either | Newer open rendering engine; worth evaluating. |

### Mushaf layouts (page view) — all from QUL

Madinah V1 (1405H, 604pp, 15 lines) · Madinah V2 (1421H, 604pp, 15 lines) · QCF v4
(1441H) · IndoPak 15-line (610pp) · IndoPak 16-line (548pp, nastaʿlīq) · Digital Khatt.
QUL lists twelve layouts in total.

### Word-by-word

Word-level Arabic, translation and transliteration (~78,000 words) from QUL, plus tajwīd
data. Licence varies by contributed resource — check each. **QAAM already renders
word-by-word tajwīd-coloured text**; reuse that work rather than rebuilding it.

---

## 7. Recitations

**Route:** per-ayah MP3s named `SSSAAA.mp3` (`002255.mp3` = 2:255), as distributed by
everyayah.com (~44 reciters, mostly 128 kbps) and addressable through the Quran
Foundation API's recitation endpoints. Per-ayah files are what make single-ayah playback
exact.

| Reciter | Style | Segment timestamps | Public release |
|---|---|---|---|
| Maḥmūd Khalīl al-Ḥuṣarī | Murattal / muʿallim | some sets | 🟡 |
| ʿAbd al-Bāsit ʿAbd al-Ṣamad | Murattal & mujawwad | partial | 🟡 |
| Muḥammad Ṣiddīq al-Minshāwī | Murattal & mujawwad | partial | 🟡 |
| ʿAbd al-Raḥmān al-Sudais | Murattal | partial | 🟡 |
| Saʿūd al-Shuraim | Murattal | partial | 🟡 |
| Mishary Rāshid al-ʿAfāsy | Murattal | yes | 🟡 |
| Muḥammad Ayyūb | Murattal | partial | 🟡 |
| Yāsir al-Dussarī | Murattal | partial | 🟡 |

**Rights position.** everyayah.com's own guidance is to verify usage rights before
redistributing. So the shipped position is: **the app fetches audio from the licensed
source onto the reader's own machine for personal use. It never bundles audio in the
installer and never re-serves it.** That is legal to build and ship today, and it
becomes a switch — not a rewrite — if a reciter's rights are later cleared.

**Storage.** A complete reciter at 128 kbps is roughly 800 MB–1.2 GB; a juz is ~25–40 MB.
Packs download per juz, with size shown before the download and per-juz delete after.

**Segment timestamps** (word-level highlighting) exist for some reciters and not others.
The UI must degrade honestly: ayah-level highlighting where word timings are missing,
never guessed timings.

---

## 8. Acquisition routes

| Route | What it gives | Ayah-aligned? | Notes |
|---|---|---|---|
| **Quran Foundation / Quran.com API v4** | Translations + several English tafsirs, e.g. `/resources/tafsirs`, `/tafsirs/{id}/by_ayah/{key}` | ✅ Yes | Fastest route to Tier A. Requires API credentials. Alignment already solved — significant saved effort. |
| **QUL — Quranic Universal Library** (Tarteel) | Bulk SQLite/JSON: translations, tafsirs, word-by-word, mushaf layouts | ✅ Mostly | Best bulk-download route. QUL states licences vary per resource — check each before use. |
| **altafsir.com** (Royal Aal al-Bayt) | The commissioned English translations + Arabic originals for Tier B | ❌ No | Requires scraping and alignment. The Wāḥidī Asbāb is a direct PDF. |
| **spa5k/tafsir_api** | 122 tafsirs as JSON over jsDelivr | ✅ Yes | Convenient for Phase 0 prototyping. **Verify provenance before trusting** — a redistributed copy is not a licence. |

---

## 9. Permission conversations to open in Phase 1

| Counterparty | Asking for | Assessment |
|---|---|---|
| **Royal Aal al-Bayt Institute** | Redistribution of their commissioned English translations (Jalālayn, Ibn ʿAbbās, Wāḥidī, Tustarī, Bayḍāwī) | **Best prospect.** A non-profit whose stated mission is free global access. Ask first. |
| **Darussalam** | Ibn Kathīr abridged, English | Commercial publisher, actively selling the 10-volume set. Expect a licence fee or a no. |
| **Maktaba Maʿārif al-Qurʾān** | Maʿārif al-Qurʾān, English | Worth asking; often permissive for non-commercial da'wah use. |
| **Book of Signs Foundation** | The Clear Qur'an (Khattab) | Widely licensed to apps already; a known path exists. |

Approach each with a clear statement of purpose, non-commercial intent (if that's the
plan), and exactly how attribution will appear in the app.

---

## 10. Attribution requirements (must appear in-app)

- Tanzil: source credit + link to tanzil.net on the About/Sources screen.
- Every tafsīr and translation: author, translator, publisher, edition, and — where
  applicable — "used by permission".
- Tier B renderings: the "not a published translation" label on every passage, not
  buried in a settings screen.
