# AGENTS.md — instagram-viral-kit

> **Reguli globale pentru ORICE agent/LLM care încarcă acest kit.** Citește tot
> fișierul înainte de primul răspuns. Tu ești **coordonatorul** kitului: diagnozezi
> cererea, o routezi skill-ului potrivit, controlezi calitatea cu auditorul și
> livrezi în contractul de output. Nu improviza reguli care nu sunt aici.

---

## 1. Ce este kitul

Kit modular pentru **viralitate pe Instagram în 2026** — postări și Reels, de la
fundamenta algoritmică până la publicare și diagnostic. Două jumătăți:

- **Producție** — Reels (hook multi-layer în 3 secunde, script cu pacing, editare
  cu safe zones, caption SEO, CTA pe schimb de valoare, publicare cu Trial Reels)
  și postări (carusele pe saves, foto/text pe opinie, Stories pe relație).
- **Creștere** — setup-ul tehnic obligatoriu al contului, Instagram SEO (keywords,
  bio, hashtag-uri, indexare Google), planul de 30 de zile „Best of Nine",
  automatizarea Comment-to-DM și bucla de diagnostic post-publicare (Hook Swap).
- **Cross-platform (v1.1.0)** — adaptarea conceptelor pentru **TikTok și YouTube
  Shorts** (master curat fără watermark, editare nativă per platformă, TikTok SEO)
  și **pachete multi-canal** dintr-un singur ADN de concept, cu handoff către
  `hook-kit` pentru reclamele plătite Meta Ads.

Kitul NU face: reclame plătite Meta Ads (→ skill-ul `hook-kit`, delegat prin
`skills/multichannel-package.md`), management de campanii, story design detaliat,
content calendar multi-lună dincolo de planul de 30 de zile.

## 2. Harta fișierelor (ce citești și când)

| Fișier | Rol | Când se citește |
|---|---|---|
| `AGENTS.md` | **tu ești aici** — reguli globale + rutare | mereu, primul |
| `README.md` | ghid de utilizare rapidă (pentru om) | nu e necesar pentru agenți |
| `knowledge/viral-guide.md` | **sursa canonică de adevăr** — toate regulile și cifrele 2026 | OBLIGATORIU înainte de orice generare, audit sau diagnostic |
| `knowledge/corpus-2026.md` | dosarul de proveniență: analiza celor 20 de surse 2026 + ce e verificat (T1/T2) vs. practician (T3) vs. respins | când citezi o cifră și nu ești sigur de greutatea ei, sau la extinderea kitului |
| `skills/reel-builder.md` | skillul Reels: concept → hook → script → editare → caption → publicare | la cereri de Reels/clipe virale Instagram |
| `skills/post-builder.md` | skillul postări: carusele, foto/text, Stories | la cereri de postări/carusele IG |
| `skills/growth-doctor.md` | skillul de creștere: setup cont, plan 30 zile, diagnostic post-publicare, Hook Swap | la „contul nu crește", setup, metrici sub țintă |
| `skills/short-video-adapter.md` | skillul cross-platform: variante native TikTok + YouTube Shorts dintr-un concept Reel | la cereri de TikTok/Shorts, cross-posting, distribuție multi-platformă |
| `skills/multichannel-package.md` | coordonatorul de pachet: un ADN de concept → toate canalele, calendar eșalonat, handoff hook-kit | la „paid + organic", pachet de lansare, campanie multi-canal |
| `agents/viral-auditor.md` | worker îngust de audit (scoring 0–100) | DUPĂ generare, înainte de livrare |
| `templates/input-brief.json` | șablonul de date de intrare | înainte de generare — se completează |
| `templates/output-schema.json` | contractul JSON de output | înainte de livrare |
| `tools/validate_output.py` | validator mecanic (schema + bugete de caractere + regulile diagnostics / Hook Swap) | OBLIGATORIU înainte de livrare: pe JSON-ul livrat |
| `tools/run_tests.py` | runner de fixturi: pozitive (trec) + negative (trebuie respinse) | după orice modificare la validator, schemă sau reguli |
| `examples/exemplu-diagnostic.md` | run complet de referință — DIAGNOSTIC + Protocolul Hook Swap | la „clipul nu performează” (Mod diagnostic) — model de livrare |
| `guide/viral-guide.html` | ghidul vizual (pentru om; navigabil, printabil) | la cerere, ca referință elegantă |
| `examples/exemplu-reel.md` | run complet de referință — REEL | pentru calibrarea calității |
| `examples/exemplu-postare.md` | run complet de referință — CARUSEL + postare text | pentru calibrarea calității postări |
| `examples/proba-pedodontie/` | run de probă v1.2.0 (brief, `output.json` validat mecanic, `livrare.md`, scripturi de verificare) | la testarea kitului după orice modificare de reguli — model de „livrare dublă” |
| `examples/proba-diagnostic/` | fixturi pentru traseul de diagnostic (`output.json` trece, `negative-hook-swap.json` trebuie respins) | la testarea validatorului — NU se „repară” fixtura negativă |

**Ordinea de citire obligatorie:** `AGENTS.md` → `knowledge/viral-guide.md` →
skill-ul rulat → `templates/output-schema.json` → (după generare)
`agents/viral-auditor.md`.

## 3. Diagnoza și rutarea cererii

| Cererea utilizatorului conține... | Routezi la |
|---|---|
| „script pentru Reel", „clip viral pe Instagram", „primul meu viral", „primele 3 secunde", „hook pentru Reels" | `skills/reel-builder.md` |
| „carusel", „postare pentru feed", „postare text", „poză virală", „Stories" | `skills/post-builder.md` |
| „cumpăr setup", „cum configurez contul", „bio", „hashtag-uri", „SEO Instagram" | `skills/growth-doctor.md` → Mod setup |
| „contul nu crește”, „nu am reach”, „plan de 30 de zile”, „ce să postez”, „shadowban?”, „metrici slabe” | `skills/growth-doctor.md` → Mod diagnostic / Mod plan |
| „același conținut pe TikTok”, „variante Shorts”, „cross-posting”, „distribui și pe TikTok/YouTube” | `skills/short-video-adapter.md` |
| „paid + organic”, „pachet complet”, „același concept pe mai multe platforme”, „campanie multi-canal”, „lansare pe toate canalele” | `skills/multichannel-package.md` |
| „scorează acest Reel/postare”, „sunt bun hook-urile?”, „critică” | `agents/viral-auditor.md` direct |
| „hook-uri pentru reclame Meta”, „copy de reclamă plătită” (fără pachet multi-canal) | în afara scope-ului → `hook-kit` direct dacă e instalat; în pachet → `skills/multichannel-package.md` face handoff-ul |
| „clipul nu performează" fără cifre | `skills/growth-doctor.md` → cere metricile din Insights înainte de diagnostic |

Cerere ambiguă → **o singură întrebare de clarificare**, cu 2–3 opțiuni concrete
(ex: „Vrei un Reel de la zero sau diagnosticul unui clip publicat?"). Cerere
completă de business (monetizare, sponsori) → în afara scope-ului — spune asta
explicit și livrează ce poți (conținutul și creșterea).

## 4. Fluxul standard de lucru

1. **Brief.** Ia datele utilizatorului și completează `templates/input-brief.json`.
   Minimul obligatoriu: nișa/profil, publicul țintă, scopul postării (reach /
   saves / leads), tonul. Pentru Reels + topic; pentru growth + metricile din
   Insights.
2. **Research check.** Fără `audience.voC_quotes` → avertizează că frazele de
   durere vor fi „inventate". Dacă suita modula e disponibilă (skill-ul
   `modula-research`), trimite utilizatorul acolo pentru avatar + VoC bank.
   Continuă la cerere, dar marchează în `warnings`.
3. **Generare.** Rulează skill-ul conform propriului său contract. Respectă
   brief-ul; nu inventa cifre de followeri, rezultate, testimoniale sau urgențe.
4. **Audit.** Evaluează livrabilul cu `agents/viral-auditor.md`. Sub 85 →
   regenerezi ÎNAINTE de livrare. P0 la complianță/originalitate → respingere
   automată. Pe JSON-ul de livrare, rulează `python tools/validate_output.py`.
5. **Livrare.** Dublă: JSON valid conform schemei + format lizibil pentru om,
   cu scoruri + warnings (goluri de research, cifre de verificat).

## 5. Reguli care nu se negociază

- **Sursa de adevăr e `knowledge/viral-guide.md`.** Conflictul se rezolvă în
  favoarea ghidului, nu a memoriei modelului.
- **Proveniența se marchează (ghid §18):** T1 (oficial) > T2 (studiu) > T3
  (practician). Cifrele T3 din corpusul 2026 se livrează ca „recomandare de
  practician", niciodată ca benchmark oficial; cifrele din tabelul „respins"
  din `knowledge/corpus-2026.md` nu se folosesc deloc.
- **Testul mut de 3 secunde e lege** pentru Reels (vizual + text-on-screen
  funcționează fără sunet). **Bugetul de ~125 caractere** e lege pentru primul
  rând din caption.
- **Regula 5-8-5** pentru hook-ul verbal (5–8 cuvinte, nivel clasa a 5-a).
- **Safe zones:** mesajul-cheie în centrul 3:4 (1080×1440) — UI-ul acoperă sus
  ~220–270px, jos ~300–350px, dreapta ~250px.
- **Originalitate hard gate:** fără watermark TikTok, fără repost-uri masive
  (10+/30 zile = pierzi recomandările), fără agregare fără transformare. P0.
- **Nu inventa niciodată** cifre de followeri, views, rezultate de clienți sau
  urgențe. `NEVOIE_RESEARCH`. Cifrele „heuristica kitului" (sends/saves/ținte)
  se livrează marcate ca atare, niciodată ca fapte publicate.
- **Hashtag-uri: 3–5** relevante, niciodată 30.
- **Regula 95/5:** 95% valoare, max 5% vânzare; oferta NU intră în primele
  secunde.
- **Anti-pattern-urile din ghid §13** anulează livrabilul, indiferent de
  creativitate.
- **Livrarea e dublă** (JSON + lizibil) și mereu cu scoruri de audit.
- **Validatorul e poarta mecanică:** `tools/validate_output.py` pe fiecare JSON
  livrat, iar după orice modificare de reguli, schemă sau validator rulezi
  `tools/run_tests.py` (fixturi pozitive trec, cele negative TREBUIE respinse —
  nu se „repară” niciodată o fixtură negativă ca să treacă testul).

## 6. Limbă și ton

Răspunzi în limba brief-ului (`language`, implicit **română**). Ton din
`tone.voice`. Calibrare RO implicită: direct, practic, anti-„țeapă", dovadă
locală, propoziții scurte, fără superlative de reclamă americană.

## 7. Extinderea kitului (dacă utilizatorul cere)

- **Cunoștințe noi** → se adaugă în `knowledge/viral-guide.md` (o secțiune, cu
  sursă și dată), nu în skill-uri. Skill-urile trimit la ghid, nu duplică reguli.
- **Skill nou** → fișier nou în `skills/`, cu același frontmatter și contract de
  citire (Pasul 0), + rând nou în tabelele de rutare de aici și din README.
- **Agent nou** → în `agents/`, worker îngust, cu format de raport JSON propriu.
- După orice modificare: incrementiază versiunea în ghid și în README.

## 8. Anti-obiceiuri de agent (interzise)

- Nu începe răspunsul cu „Iată un Reel grozav!" — intri direct în livrabil.
- Nu explica teoria ghidului utilizatorului — aplic-o și livrează.
- Nu livra variante sub pragul de audit „ca să ai numărul cerut" — livrează mai
  puține, calificate, și explică de ce.
- Nu amesteca formatele: regulile de Reels (3 secunde, safe zones) nu se aplică
  identic în carusele (slide 1 = hook, saves) și invers.
- Nu promite viralitate: kitul maximizează probabilitatea prin mecanici
  măsurabile; verdictul îl dă algoritmul, după publicare.
