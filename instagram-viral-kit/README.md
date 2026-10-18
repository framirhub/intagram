# instagram-viral-kit

Kit modular și reutilizabil pentru **viralitate pe Instagram în 2026** — postări
și Reels, de la mecanica algoritmului până la publicare, diagnostic și creștere.
Construit pe tiparul suitei modula: **ghid vizual HTML + cunoștințe canonice +
skill-uri + orchestrator + auditor de calitate** (la fel ca
`facebook-hook-generator-kit`).

Orice agent/LLM care primește acest folder citește mai întâi [`AGENTS.md`](AGENTS.md) —
acolo sunt regulile globale și rutarea.

## Structura

```
instagram-viral-kit/
├── SKILL.md                   # intrarea ca skill global (frontmatter + încarcă AGENTS.md)
├── AGENTS.md                  # Reguli globale, roluri și orchestrare — INTRAREA agentului
├── README.md                  # acest ghid
├── guide/
│   └── viral-guide.html       # Ghidul vizual (deschide în browser; printabil A4)
├── knowledge/
│   ├── viral-guide.md         # Sursa canonică de cunoștințe (toate regulile + cifrele 2026)
│   └── corpus-2026.md         # Dosarul de proveniență: cele 20 de surse 2026, T1/T2/T3 vs. respinse
├── skills/
│   ├── reel-builder.md        # REELS: hook 3s multi-layer → script cu pacing → editare → caption SEO → publicare
│   ├── post-builder.md        # POSTĂRI: carusele (saves), foto/text (opinie), Stories
│   ├── growth-doctor.md       # CREȘTERE: setup cont, plan 30 zile, diagnostic post-publicare + Hook Swap
│   ├── short-video-adapter.md # CROSS-PLATFORM: variante native TikTok + YouTube Shorts dintr-un Reel (v1.1.0)
│   └── multichannel-package.md# MULTI-CANAL: un ADN de concept → toate canalele, calendar eșalonat, handoff hook-kit (v1.1.0)
├── agents/
│   └── viral-auditor.md       # Auditor de calitate: scoring 0–100, verdict PASS/REVISE/REJECT
├── templates/
│   ├── input-brief.json       # Brief-ul de intrare (nișă, audiență, scop, ton, metrici)
│   └── output-schema.json     # JSON Schema (reels, posts, account_setup, growth_plan, diagnostics)
├── tools/
│   ├── validate_output.py     # Validator mecanic: schema + bugetele de caractere + regulile diagnostics
│   └── run_tests.py           # Runner: fixturi pozitive (trec) + negative (trebuie respinse)
└── examples/
    ├── exemplu-reel.md        # Run complet de referință — REEL (de la concept la diagnostic)
    ├── exemplu-postare.md     # Run complet de referință — CARUSEL + postare text
    ├── exemplu-diagnostic.md  # Run complet de referință — DIAGNOSTIC + Protocolul Hook Swap
    ├── proba-pedodontie/      # Run de probă v1.2.0: brief + output.json validat + livrare.md
    │                          #   + genereaza_output.py / audita.py / render_livrare.py
    └── proba-diagnostic/      # Fixturi pentru traseul de diagnostic: output.json (trece)
                               #   + negative-hook-swap.json (TREBUIE să pice)
```

## Utilizare rapidă (3 pași)

1. **Brief.** Copiază `templates/input-brief.json`, completează câmpurile marcate
   în `_required` (nișă, public, scop, ton) + atât din optional cât poți (mai
   ales `voC_quotes` și metricile actuale din Insights — materia primă a
   diagnosticului).
2. **Generezi.** Deschide sesiunea de agent cu kitul încărcat și spune, de ex:
   - *„Script Reels pentru [subiect], brief-ul e în brief.json"* → `skills/reel-builder.md`
   - *„Carusel cu 8 slide-uri despre [temă]"* → `skills/post-builder.md`
   - *„Configurează contul ca să fie eligibil pentru viralitate"* → `skills/growth-doctor.md` (Mod setup)
   - *„Reel-ul meu are 400 de views din 50k followeri — ce e greșit?"* → `skills/growth-doctor.md` (Mod diagnostic)
   - *„Plan de 30 de zile ca să pornesc de la 0"* → `skills/growth-doctor.md` (Mod plan)
   - *„Adu acest concept și pe TikTok și Shorts"* → `skills/short-video-adapter.md`
   - *„Pachet complet de lansare: Reels + carusel + TikTok + reclame"* → `skills/multichannel-package.md`
   - *„Scorează acest Reel"* → `agents/viral-auditor.md`
3. **Primești.** Pachet dublu: JSON conform `output-schema.json` (pentru
   automatizări) + format lizibil (pentru tine), fiecare livrabil cu scor de
   audit. Sub 85/100 nu se livrează — varianta e regenerată automat.

## Cum se conectează ca skill (ZCode / Claude / orice agent cu skills)

Kitul e **self-contained** — funcționează și doar prin AGENTS.md, într-o sesiune
în care ai atașat folderul. Instalarea permanentă (tiparul suitei modula —
junction, o singură sursă de adevăr, zero duplicare):

```
cmd /c mklink /J "%USERPROFILE%\.agents\skills\instagram-kit" "D:\zaicode\projects\instagram-viral-modula\instagram-viral-kit"
```

- Skill-ul global se numește **`instagram-kit`** (orchestratorul din `SKILL.md`):
  îl invoci natural („instagram-kit, scrie-mi un Reel despre X") și el citește
  AGENTS.md → cunoștințe → skill-ul intern potrivit → audit → livrare.
- Toate căile din skill sunt relative, deci junctionul păstrează structura intactă.
- Dezinstalare: șterge junctionul (`rmdir` pe link — NU afectează kitul sursă).

## Ce reguli aplică kitul (rezumat)

- **Algoritmul 2026:** interest graph, distribuție în valuri (audiență de test →
  extindere), „views" ca monedă unică; semnalele Mosseri: watch time > sends per
  reach > likes per reach.
- **Testul mut de 3 secunde** pentru Reels: vizual + text-on-screen transmit
  ideea fără sunet; hook verbal 5–8 cuvinte (Regula 5-8-5), fără intro.
- **Setup tehnic obligatoriu** (7 puncte): cont profesionist, Upload at highest
  quality, indexare motoare de căutare, Account Status verde, traduceri + dubbing
  AI, bio SEO, nișă clară.
- **Instagram SEO 2026:** keywords în Name field/bio/caption/text rostit; Google
  indexează conturile profesionale din iulie 2025; hashtag-uri 3–5 (max oficial
  ~5).
- **Safe zones:** mesajul în centrul 3:4; cover cu titlu în miniatură.
- **Originalitate hard gate:** fără watermark TikTok, fără repost masiv
  (10+/30 zile = pierzi recomandările — reguli extinse la foto/carusele în 2026).
- **CTA pe schimb de valoare** („Comentează KIT → ghid în DM") + automatizare
  Comment-to-DM cu ManyChat (partener oficial Meta API).
- **Trial Reels** pentru testare doar pe non-followeri (insights ~24h; publicarea
  finală e decizia ta, nu automată).
- **Audit 0–100** pe 5 criterii (hook & scroll-stop, retenție & structură,
  discoverability, complianță & originalitate, CTA & buclă de creștere); prag de
  livrare: 85.
- **Bucla post-publicare:** metrică sub țintă → cauză cunoscută → acțiune tactică,
  inclusiv Protocolul Hook Swap (nu ștergi clipul — schimbi primele 3 secunde și
  republiezi după 3 zile). Din v1.2.1 bucla e și **verificată mecanic**: un
  `hook_swap` fără 3 hook-uri noi, în buget 5-8-5, nu trece validarea.
- **Cross-platform (v1.1.0):** TikTok (21–34s, SEO pe 3 canale, remix de trend)
  și YouTube Shorts (max 3 min, „Viewed vs. Swiped Away" ≥70%) dintr-un master
  curat — filmezi o dată, editezi nativ per platformă, niciodată repost identic.
- **Pachete multi-canal (v1.1.0):** un singur ADN de concept transpus pe toate
  canalele, calendar de lansare eșalonat, handoff către `hook-kit` (v1.3.0) pentru
  reclamele plătite Meta Ads — sau warning explicit dacă hook-kit lipsește.
- **Limbă și piețe (v1.1.0):** kitul rulează în limba brief-ului cu matrice de
  calibrare per piață (RO/EN/DE/FR-IT-ES/JP-KO) — bugete de cuvinte per hook,
  VoC în limba pieței, niciodată traduceri din RO (ghid §16).
- **Proveniență pe niveluri (v1.2.0):** T1 (oficial: Instagram/Meta/Mosseri) >
  T2 (studiu cu metodologie: Metricool) > T3 (practician: bloguri/creatori).
  Cifrele T3 se livrează ca „recomandare de practician", niciodată ca benchmark
  oficial; ce nu are sursă = `NEVOIE_RESEARCH`.
- **Metrici noi în diagnostic (v1.2.0):** skip rate ca semnal negativ (peste ~40%
  → repară intro-ul) plus scorecard-ul pe 6 rate-uri (skip / share / like / save /
  repost / comment) care localizează componenta moartă când media generală e OK.
- **Viralitate relativă (v1.2.0):** un Reel e viral pentru contul tău la ~7,5×
  reach față de followeri sau ~40× media de views (conturi mari: prag absolut
  ~1M); nu se promite viralitate, se măsoară.
- **Plan de 30 de zile „Best of Nine":** setup + Content Pool (20+ Reels virale)
  → testarea a 3 formate × 3 postări → scale pe formatul câștigător. Variantă
  scurtă: testarea în 10 zile (9 Reels, 3 revizuiri de date, o ajustare/rundă).

## Personalizare

- **Reguli noi / nișă nouă** → adaugă o secțiune în `knowledge/viral-guide.md`;
  skill-urile o moștenesc automat (ele citesc ghidul, nu duplică regulile).
- **Alt canal** (LinkedIn, X, Google Ads) → skill nou în `skills/`, cu contractul
  de citire din AGENTS.md §7. TikTok și YouTube Shorts există deja
  (`skills/short-video-adapter.md`).
- **Limbă** → kitul rulează implicit în română; setează `language` în brief pentru
  altă piață și urmează matricea de calibrare din ghid §16 (regulile mecanice
  rămân; bugetele de cuvinte și dovada locală se adaptează).

## Kituri-partener

Kiturile suitei modula sunt interoperabile. Relatie bilaterală cu
`facebook-hook-generator-kit` (v1.3.0): el livrează hook-urile și copy-ul de
reclame Meta Ads, acest kit livrează producția de platformă. Pachetele
multi-canal (`skills/multichannel-package.md`) fac handoff-ul automat: brief de
transfer către `hook-kit` pentru reclame, sau pachet organic + warning dacă
hook-kit nu e instalat.

## Surse

Cunoștințele consolidează: `context/brief-viral-instagram-v2.pdf` (brief strategic
v2, analiză pe 40 resurse video — algoritm interest-space, metrici critici,
hook-uri, Trial Reels, plan 30 zile) + research web validat octombrie 2026:
declarații Adam Mosseri (watch time, likes per reach, sends per reach), blog
oficial Instagram Creators (valuri, originalitate 2024→2026), help.instagram.com
(specs, Account Status, traduceri/dubbing AI, indexare Google din 10.07.2025),
Metricool IG Study 2026, Socialinsider Benchmarks 2026, Buffer 2025, Sprout
Social 2025, ManyChat (API oficial) + pentru cross-platform (v1.1.0): Metricool
TikTok study, Socialinsider aug. 2026 (audiențe per platformă), MakeUseOf
(Shorts 3 min, oct. 2024), YouTube „inauthentic content" policy (iul. 2025).
Cifrele fără sursă publică sunt marcate explicit „heuristica kitului".

**Corpusul 2026 (v1.2.0)** consolidează 20 de surse analizate separat — 10
articole (SocialPilot sep. 2026, Hootsuite iul. 2026, PostEverywhere feb. 2026,
Aurelius Media apr. 2026, Deftsoft mai 2026, Maya Digital Desk mar. 2026, Pictame
ian. 2026, True Future Media feb. 2026, UseFastlane iul. 2026, ReelsMaker AI apr.
2026) și 10 clipuri YouTube (Robert Benjamin, Tech Paradise, Build Your Tribe,
Metricool, Jade Beason, Jagaltech, Enrico Incarnati, HubSpot Marketing) — cu
verdict de verificare în [`knowledge/corpus-2026.md`](knowledge/corpus-2026.md):
7 surse nu au putut fi verificate (corp de text/transcript indisponibil), iar o
parte a cifrelor lor (ponderi exacte de semnale, boost-uri de audio, tabele de
ore) a fost respinsă explicit.

Version 1.2.1 · 2026-10-15 · changelog: v1.2.1 = traseul de diagnostic testat cap-coadă: exemplu complet (`examples/exemplu-diagnostic.md`) + fixturi pozitive/negative (`examples/proba-diagnostic/`) + `tools/run_tests.py` (asertă exit 0 pe fixturi valide și exit 1 pe cele invalide, cu gard că testul nu trece „pe gol”); `tools/validate_output.py` verifică acum câmpurile obligatorii ale unui diagnostic și protocolul Hook Swap (minimum 3 hook-uri, fiecare cu 5–8 cuvinte); regula scrisă explicit în ghid §11 (runul de probă pedodonție rămâne etichetat `kit_version: 1.2.0` — a fost generat sub regulile acelei versiuni și se păstrează ca artefact istoric) · v1.2.0 = corpusul 2026 analizat în `knowledge/corpus-2026.md` (20 de surse, grading T1/T2/T3/R) + capitolul nou §18 „Proveniență și niveluri de încredere" în ghid; skip rate ca semnal negativ (§1.4, §2.2, §11); ținte de practician pentru share rate (0,5–2%), save rate (1–3%) și completion (<15s: ≥70%); definiția relativă a viralității (§2.4); scorecard pe 6 rate-uri (skip/share/like/save/repost/comment) în diagnostic; separarea explicită reach conectat (likes) vs. neconectat (sends); corecția T1 la Trial Reels (partajare automată pe baza primelor 72h — nota veche „72h neconfirmat" retrasă); pârghiile secundare T3 (§9.6); testarea în 10 zile (§12); 7 surse neverificabile marcate ca atare; run de probă complet (`examples/proba-pedodontie/`: brief → 3 Reels + carusel + plan 30 zile → `validate_output.py` VALID → `audita.py` 0 probleme → `livrare.md`) · v1.1.1 = reparații P0 la verificarea mecanică: validatorul nu mai crapă pe Windows (UTF-8 reconfigure) nici pe hashtag-uri generice/hook_line lung (NameError `notes`); schema cere `content` doar la text/foto și obligă `slides` la carusel (un carusel corect nu mai pică validarea); `audit` e obligatoriu pe fiecare livrabil (reel, post, cross_channel) în schemă + eroare în validator — poarta 85/100 e acum mecanică · v1.1.0 = `skills/short-video-adapter.md`
(TikTok + Shorts, ghid §15) · `skills/multichannel-package.md` (pachet multi-canal
cu handoff hook-kit) · matricea de limbi și pieți (ghid §16) · bloc `cross_channel`
în schema + validator extins · pagina 8 în ghidul vizual · v1.0.0 = kitul inițial:
ghid canonic (17 secțiuni), 3 skill-uri (reel-builder, post-builder, growth-doctor),
auditor 0–100, template-uri + validator mecanic, 2 exemple de referință, ghid
vizual HTML, instalare ca skill global (`instagram-kit`).
