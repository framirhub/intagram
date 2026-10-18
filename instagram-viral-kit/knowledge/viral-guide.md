# Ghidul Canonic de Viralitate Instagram — instagram-viral-kit

> **Sursa de adevăr a kitului.** Orice skill, agent sau orchestrator care produce
> Reels, postări, setup de cont sau diagnostice Instagram trage cunoștințele
> EXCLUSIV de aici. Dacă un output contrazice acest ghid, outputul e greșit — nu
> ghidul.
>
> Surse primare: `context/brief-viral-instagram-v2.pdf` (brief strategic „Cum să
> devii viral pe Instagram", v2, analiză pe 40 resurse video — algoritm interest
> space, metrici critici, hook-uri, Trial Reels, plan 30 zile). Completări
> validate web (octombrie 2026): declarații Adam Mosseri (watch time, likes per
> reach, sends per reach), blog oficial Instagram Creators (distribuție în valuri,
> reguli de originalitate 2024→2026), Metricool Instagram Study 2026 (24,4M
> postări), Socialinsider Benchmarks 2026 (15M postări), Sprout Social 2025
> (timing), Buffer 2025 (frecvență), help.instagram.com (spec-uri, traduceri,
> Account Status, indexare Google din iulie 2025), ManyChat (API oficial Meta).
> Cifrele care NU au sursă publică sunt marcate explicit „heuristica kitului" sau
> „din brief, neconfirmat public".
>
> **v1.2.0:** regulile noi vin din corpusul de 20 de surse 2026 (10 articole +
> 10 clipuri) analizat în `knowledge/corpus-2026.md`, cu sistem de proveniență
> **T1 (oficial) / T2 (studiu cu metodologie) / T3 (practician) / R (respins)** —
> vezi §18. Orice cifră T3 se livrează marcată ca atare, niciodată ca benchmark
> oficial.
>
> **v1.2.1:** traseul de diagnostic e verificat mecanic — `tools/validate_output.py`
> controlează acum câmpurile obligatorii ale unui diagnostic și protocolul Hook
> Swap (minimum 3 hook-uri noi, fiecare în bugetul 5-8-5); fixturi pozitive +
> negative în `examples/proba-diagnostic/` și runner `tools/run_tests.py`.
>
> Version: 1.2.1 · Data: 2026-10-15 · Limbă implicită: RO (kitul funcționează în
> orice limbă — vezi §16 pentru calibrarea pe limbi și piețe)

---

## 1. Fundament: cum gândește algoritmul Instagram în 2026

### 1.1 Interest graph, nu social graph

Algoritmul **nu mai distribuie pe baza followerilor**. Fiecare postare e evaluată
individual și distribuită către **spații de interes** (Interest Space Algorithm /
interest graph): oamenii cărora le place subiectul tău, nu neapărat oamenii care te
urmăresc. Cont nou + zero followeri poate bate cont mare, dacă Reel-ul performează.

Consecințe operaționale:

- **Fiecare postare pleacă de la zero.** Un Reel slab nu e „salvat" de cont; un
  Reel bun nu e „frânat" de cont mic.
- **Nisa clară e obligatorie.** Algoritmul îți construiește un profil de interes
  din ce postezi; contul care sare de la gătit la crypto la fitness nu e
  clasificat, deci nu e distribuit eficient.
- **Cifrele de followeri din brief e o falsă siguranță.** Un cont de 50k cu
  engagement mort primește reach mai mic decât unul de 800 cu watch time bun.

### 1.2 Distribuția în valuri

Mecanismul oficial confirmat (blog Instagram Creators, apr. 2024, în vigoare 2026):
conținutul e arătat întâi unei **mici audiențe de test** (fără să conteze
followerii), apoi — dacă metricile de test trec — extins **în valuri succesive**
tot mai mari. Fiecare val e câștigat în primele secunde.

> ⚠️ Cifra „eșantion de test 100–500 utilizatori" circulă în materiale de
> practician, dar NU apare în nicio sursă oficială. Folosește conceptul (audiență
> mică de test → valuri), nu cifra.

**Modelul mental T3 al fazelor** (corpus 2026, S6 — cifre de practician, NU
oficiale; folosește-le ca ordine de citire a Insights-ului, nu ca praguri
contractuale):

1. **Follower test (0–60 min):** postarea e arătată unei fracțiuni din baza
   existentă (T3: 10–20% din followeri) + non-followerilor cu interese apropiate.
2. **Extindere (1–6 ore):** dacă retenția și sends-urile trec, conținutul intră
   în Explore / pagini de hashtag / audiențe similare.
3. **Push viral (6h+):** dacă rata de interacțiune se menține, valurile devin tot
   mai mari — aici se decide „viralul", nu la prima oră.

Consecință practică: **nu judeca un Reel la 30 de minute.** Fereastra de citire
corectă a testului e 24–72h (Metricool, T2: 65% din views-urile unui Reel și 61%
din interacțiuni se adună în primele 72 de ore).

### 1.3 „Views" e moneda unică

Din august 2024, **Views** e metrica primară unificată pe tot Instagram (Reels,
video, foto, carusele, Stories). Creșterea reach-ului = creșterea views-urilor.
Tot ce faci se măsoară la final în: views + cine le-a văzut (followeri vs
non-followeri — raportul arată dacă algoritmul te distribuie dincolo de baza ta).

### 1.4 Semnalele de ranking (declarații Adam Mosseri, confirmate 2025–2026)

Ierarhia semnalelor pentru Reels, în ordinea puterii:

1. **Watch time / Retention** — cât timp și ce procent din clip se vizionează.
   Metricool 2026: watch time mediu per Reel ≈ **8,5 secunde** (+117% față de
   2024) — dacă nu câștigi primele 8 secunde, nu câștigi nimic.
2. **Sends per reach (share-uri pe DM)** — semnalul suprem pentru distribuția
   către non-followeri. Un Reel trimis în DM-uri circulă în pâlnii private, pe
   care algoritmul le citește ca valoare maximă. Sentimentul care produce sends:
   „asta e pentru X pe care îl cunosc", „trebuie să văd asta și eu mai târziu".
3. **Likes per reach** — angajamentul cu followerii existenți; contează, dar nu
   deschide audiențe noi.
4. **Comentarii, saves, follows per reach** — validează interesul activ;
   comentariile alimentează și conversația în DM (rumoare).
5. **Skip rate (semnal negativ)** — procentul care trece peste Reel în primele
   secunde. Din 2026 apare în corpus ca semnal de ranking distinct (S10, T3) și
   e oricum metrică oficială în Insights (aug. 2025). Funcționează ca frână: un
   skip rate mare anulează retenția bună de după.

**Nuanța T1 (Mosseri) asupra likes vs. sends — context, nu ierarhie universală:**
cele trei semnale principale sunt watch time, likes și sends, dar **likes
cântăresc relativ mai mult pentru reach-ul conectat** (audiența care te
urmărește), iar **sends mai mult pentru reach-ul neconectat** (non-followeri).
Nu există „sends 3–5× likes" publicat oficial — afirmația circulă în surse de
practician (S1, S4) și se livrează marcată T3, ca orientare, nu ca multiplicator
cert (§18).

> **Heuristica kitului (din brief, neconfirmat public):** 1 send la 100–200 views
> e ținta de viralitate; saves țintă 1 la 50–100 views; comentarii 15–30+ la
> 1.000 de views. Nu există benchmarks publice oficiale — folosesc-le ca ținte de
> lucru, nu ca adevăruri absolute.

### 1.5 Regulile de originalitate (2026)

Confirmat oficial, extins în aprilie 2026 dincolo de Reels la **fotografii și
carusele**:

- Postarea conținutului altora de **10+ ori în 30 de zile** (fără transformare
  semnificativă) → contul devine **neeligibil pentru recomandări** (se repară prin
  Account Status, îndepărtând conținutul neoriginal).
- La conținut duplicat, doar **originalul** e recomandat; repost-urile primesc
  etichetă către creator. Agregatoarele sunt scoase din recomandări.
- **Watermark TikTok / alte platforme** → deprioritare în recomandări.
- Excepții tolerate: meme-uri, parodii, compilații cu transformație, reacții cu
  voiceover nou și comentariu propriu.

### 1.6 Ce NU mai contează (mituri 2026)

| Mit | Realitate 2026 |
|---|---|
| „Postez la ora X și devin viral" | Timing-ul are efect minor; în interest graph contează retenția și sends, nu ora. Ora optimă = când e activă audiența TA (vezi Insights), cu ferestre generale mar–mie 9–11 (Sprout Social 2025). |
| „30 de hashtag-uri = reach" | Hashtag-urile ajută la categorizare/căutare, NU la reach. Limita oficială recomandată: **max ~5** (din dec. 2025). 3–5 relevante e optimul. |
| „Followerii aduc viralitate" | Followerii dau baza inițială de vizionări; distribuția vine din metrici per reach, nu din mărimea contului. |
| „Meta Verified îți dă reach" | Promite vizibilitate în search, dar testele independente (Buffer 2025) nu arată boost real de reach. Legitimitate + suport, nu pârghie. |
| „Contul mare e protejat" | 10 repost-uri în 30 de zile → pierzi recomandările, indiferent de mărime. |

---

## 2. Metricile critice și țintele de lucru

### 2.1 Funnel-ul metricilor unui Reel

```
Impresii → Vizionări 3s (hook rate) → Retenție (watch time) → Completare
→ Interacțiuni (sends, comments, saves, likes) → Follows → Views noi (buclă)
```

Fiecare etapă filtrează pe cea următoare. Diagnosticul (§11) citează funnel-ul în
ordine și repară PRIMA etapă stricată, nu ultima.

### 2.2 Tabelul de ținte 2026

| Metrică | Ce măsoară | Țintă de lucru | Sursă |
|---|---|---|---|
| **Hook rate** (vizionări >3s / impresii) | hook-ul oprește scroll-ul | ≥ 25–35% sănătos; 40%+ elite | benchmark Meta Ads public (proxy); Instagram a adăugat metrica oficială „view rate / skip rate" în Insights (aug. 2025) |
| **Skip rate** | % care abandonează în 3s | complementar hook rate; NU „sub 20–30%" (claim din brief — nesustenat public; skip <70% e deja foarte bun) | insights oficiale |
| **Watch time mediu** | secunde vizionate | > 8,5s (media 2026); urcă retenția prin pacing | Metricool 2026 |
| **Completion rate** | % din clip vizionat | clipuri <30s: ≥65%; 30–60s: ≥50% (heuristica kitului, din brief); corpus 2026: ≥70% la clipuri <15s | heuristica + T3 (S6) |
| **Skip rate** (complementar hook rate) | % care abandonează în primele secunde | 20–35% = interval normal; **peste ~40% → repară intro-ul** (Hook Repair) | T3 (S10), metrică T1 în Insights |
| **Share rate** (shares/views) | cât de „de trimis" e conținutul | 0,5–2% (sub 0,5% = lipsă de valoare de identitate) | T3 (S6: >0,5%; S8: 1–2%) |
| **Save rate** (saves/views) | valoare de referință | 1–3% (peste 3% = material de referință validat) | T3 (S6: >1%; S8: 2–3%) |
| **Sends / views** | share-uri pe DM | 1 send / 100–200 views (heuristica kitului) | heuristica; semnal confirmat de Mosseri |
| **Saves / views** | salvări | 1 save / 50–100 views (heuristica kitului) | heuristica |
| **Comentarii / 1k views** | conversație | 15–30+ (heuristica kitului) | heuristica |
| **Engagement rate** | engagement/followers | media IG 2026 ≈ 0,45%; carusele 0,55% (top format); Reels 0,52%; imagini 0,37% | Socialinsider 2025–2026 |
| **Reach rate** (Reels) | views / followers | ~9,8% pe conturi mici = sănătos | clouted 2026 |

### 2.3 Regula de citire a raportului followeri / non-followeri

După fiecare postare: dacă **majoritatea views vin de la non-followeri**
(reach **neconectat**), algoritmul te distribuie activ (ești în jocul de
viralitate) — acolo lucrează hook-ul, sends-urile și shareability-ul. Dacă 90%+
views vin de la followeri (reach **conectat**), conținutul e doar „servit" bazei
existente — sau e neoriginal, sau hook-ul n-a deschis valul. Reziem conținutul:
câștig de top-funnel = zero.

**Cele două regimuri cer optimizări diferite** (T1 Mosseri + S9, T3):

| Regim | Cine vede | Semnal care te ridică | Ce optimizezi |
|---|---|---|---|
| **Reach conectat** | followerii tăi | likes per reach | comunitate, consecvență, identitate, serii |
| **Reach neconectat** | non-followeri (Explore/Reels) | sends per reach, hook, shareability | unghi de trimis în DM, teme universale, trenduri |

Pentru conturi mici/noi, kitul recomandă **ponderea efortului spre reach
neconectat** (T3, S9: ~70%) — acolo se câștigă următorii 1.000 de followeri.

### 2.4 Ce înseamnă „viral" pentru contul TĂU (definiție relativă)

Viralitatea nu se măsoară în views absolute (S4, T3) — pragul de 1M views e o
excepție, nu o definiție. Definiția de lucru a kitului, pe două repere:

- **Cont mic/mediu:** un Reel e viral când atinge **~7,5× numărul de followeri
  în reach** sau **~40× media lui de views** (ex: cont cu 1.000 de views medii →
  moment viral la ~40.000).
- **Cont mare:** pragul rămâne absolut (peste ~1M views în câteva zile), pentru
  că raportul la followeri devine imposibil de atins.

Ambele repere sunt T3 (practician) — folosește-le ca **sărbătoare măsurabilă și
ca obiectiv de plan**, nu ca promisiune. Cifrele absolute „absolute" din listele
de ore și de „boost-uri" NU intră în kit (§18, tabelul de respinse).

---

## 3. Setup-ul tehnic obligatoriu al contului

Setările pot bloca eligibilitatea de a deveni viral înainte de prima postare.
Checklist de audit (rulează în ordine; toate trebuie PASS înainte de a produce):

1. **Cont profesionist (Creator sau Business)** — obligatoriu pentru: insights
   complete, Trial Reels, indexare Google, apostrof de încredere. Gratuit.
2. **Calitate media:** Settings and activity → Media quality → **Upload at
   highest quality = ON** + date saver OFF. Re-upload-urile comprimate agresiv
   (1080p→720p) pierd din retenție percepută.
3. **Indexare în motoarele de căutare:** Settings → **Allow public photos and
   videos to appear in search engine results = ON**. Din **10 iulie 2025**,
   Instagram lasă Google/Bing să indexeze conținutul public al **conturilor
   profesionale** (posts, Reels, captions, alt text) — postările tale devin
   suprafață de căutare Google + material pentru motoare AI (ChatGPT, Gemini).
4. **Account Status:** Settings → Account Status. Verifică: conținut eliminat,
   conținut **neeligibil pentru recomandări** (aici apare shadowban-ul real), și
   „ce nu poate fi recomandat". Orice problemă → appeal direct din ecran. Contul
   „verde" aici = condiția zero pentru recomandări.
5. **Traduceri automate:** Settings → Language and translations → activare
   traduceri captions/comentarii. La publicare, opțiunea **„Translate voices
   with Meta AI"** (dubbing AI cu lip-sync, din aug. 2025: EN/ES, extins 2026
   cu JP/KO/FR/DE/IT; necesar 1.000+ followeri) — deschide audiențe
   internaționale fără refilmat.
6. **Bio optimizată SEO** (vezi §4.2): nume + keyword principal + propoziție de
   valoare + CTA/link.
7. **Nisa declarată în fapte:** ultimele 9 postări în aceeași temă (algoritmul
   clasifică după conținut, nu după intenții).

**Contul „verde" pe toate cele 7 = fundația. Orice Reel publicat pe un cont cu
restricții în Account Status aruncă producția pe o fundație blocată.**

---

## 4. Instagram SEO 2026

### 4.1 Unde trăiesc cuvintele-cheie

Căutarea Instagram e keyword-based. Algoritmul parsează, în ordinea impactului:

1. **Câmpul Name** (numele profilului, nu username-ul) — cel mai puternic spot de
   căutare internă: „Ana | Nutriție pentru mamă" bate „Ana" la căutarea „nutriție".
2. **Bio** — keyword-urile din bio te fac findable în search + Google.
3. **Caption** — keyword-urile naturale din primele 2 rânduri contează atât pentru
   search intern, cât și pentru indexare Google (din iulie 2025).
4. **Cuvintele rostite în Reel + text-on-screen** — Instagram transcrie și
   citește textul din Reels (declarație Mosseri: keywords în captions, cuvinte
   rostite, text-on-screen).
5. **Alt text** (opțional) — descrie pozele pentru accesibilitate + indexare.

### 4.2 Formula de bio

```
[Nume] | [Keyword-ul principal pe care vrei să-l găsească lumea]
[Ce primește followerul, concret — 1 linie]
[Prova/diferența — 1 linie, cifre dacă ai]
[CTA + link: "Ghid gratuit ↓" / DM "KIT"]
```

### 4.3 Hashtags — rolul corect

- **Max ~5 hashtag-uri** (recomandare oficială @creators, dec. 2025–ian. 2026;
  fostul maxim 30 e istorie).
- Rol: categorizare + căutare internă, NU reach. 3–5 specifice nișei + 1 broad.
- Zero hashtag-uri generice (#love #viral #fyp) — atrag agregatoare și zero
  relevanță.

### 4.4 SEO Google (nou, 2025–2026)

Conținutul public al conturilor profesionale e indexat de Google din 10 iulie
2025. Consecințe: scrie captions care au sens în afara Instagram (propoziții
completes, keyword-ul subiectului prezent), folosește alt text, și tratează
caption-ul ca pagină web: titlu (prima linie) + conținut cu keyword-uri + CTA.
Postările pot apărea în rezultate Google și pot fi citate de motoare AI.

---

## 5. Anatomia Reel-ului viral

### 5.1 Primele 3 secunde — Hook-ul multi-layer

Hook-ul are un singur scop: **oprirea scroll-ului + claritate instantanee** asupra
subiectului. Media watch time 2026 e 8,5s — totul se decide acolo.

**Triple Hook Layering — 3 straturi sincronizate pe ACEEAȘI idee:**

| Strat | Ce livrzi | Regulă |
|---|---|---|
| **Vizual** | cadru 0–3s (mișcare bruscă, recuzită, unghi, mid-motion start) | înțeles fără sunet |
| **Verbal** | replica rostită, **5–8 cuvinte** (Regula 5-8-5), nivel „clasa a 5-a", fără jargon | declarație, nu intro |
| **Text-on-screen** | 1–3 cuvinte de impact, mare, contrastant | lizibil în prima secundă |
| (+ **Auditiv**) | whoosh, pauză totală, schimbare de ritm | pattern interrupt |

**Reguli de aur:**
- **Fără delay (speed to value):** zero preambuluri („Bună guys, welcome back!").
  Subiectul e în secunda 1.
- **Tăieturi la 2 secunde:** schimbă unghi/zoom/cadru la fiecare 2–3,5s
  (Attention Reset).
- **Testul mut:** oprește sunetul — vizual + text-on-screen trebuie să transmită
  ideea singure (80%+ privesc fără sonor).
- Hook-ul verbal e o **promisiune** pe care corpul o plătește; clickbait fără
  plată ucide retenția la secunda 10 și îți distruge contul pe termen lung.

### 5.2 Durata 2026

- **Max oficial 3 minute** (din ian. 2025), dar Instagram NU recomandă >3 min
  audiențelor noi; boost-ul plătit funcționează doar ≤90s.
- **Sweet spot pe date 2025–2026:** 30–60s = cel mai mare reach rate (5,60%,
  Socialinsider); 45–60s = sweet spot engagement; **7–15s = completion maxim**
  (consens al corpusului 2026: S4, S5, S6, S8, S9, S10 — T3). Regula rămâne
  însă „durată = minimul promisiunii": 7–15s nu e o țintă, e intervalul în care
  completion-ul stă cel mai sus — dacă promisiunea are nevoie de 40s, o plătești
  în 40s (cu Attention Reset la 2–3,5s), nu o tai artificial.
- **Regulă kit:** durata = timpul minim în care plătești promisiunea hook-ului.
  Nu întinzi ca să „ajungă la 60s".

### 5.3 Timeline de pacing (șablon de producție, primele 15 secunde)

| Interval | Script vorbit | Schimbare vizuală | Audio / SFX |
|---|---|---|---|
| 0:00–0:03 | Hook verbal (5–8 cuvinte) | cadru strâns A-roll + text mare | whoosh / alertă |
| 0:03–0:06 | identificarea problemei | jump-zoom pe față | tăcere scurtă |
| 0:06–0:09 | agitare + open loop | b-roll / grafică | pop SFX |
| 0:09–0:12 | soluția 1 | revenire A-roll + subtitrare galbenă | muzică volum mic |
| 0:12–0:15 | soluția 2 | schimbare unghi / zoom out | SFX pe cuvânt-cheie |

Restul clipului: puncte de valoare cu Attention Reset la fiecare 2–3,5s, și
**Regula 95/5**: 95% valoare/poveste, max 5% vânzare. Oferta agresivă în primele
secunde prăbușește retenția.

### 5.4 Checklist de editare (Dead Air Removal)

- [ ] Pauze tăiate până când unda audio atinge propoziția următoare.
- [ ] Cuvinte parazit șterse („deci", „ăăă", repetiții).
- [ ] Subtitrări animate cuvânt-cuvânt, centrate, contrast mare (safe zone!).
- [ ] Mixaj 3 niveluri: voce 0 dB, muzică −20 dB, SFX la tranziții.
- [ ] Text cheie în **safe zone** (vezi 5.5).
- [ ] Cover cu titlu lizibil în miniatură (vezi 5.5).

### 5.5 Safe zones și cover (spec-uri 2026)

Pe 1080×1920 (9:16, MP4 H.264, min 30fps):

- **Sus:** evită text în primele ~220–270px (UI: header, audio).
- **Jos:** evită ultimele ~300–350px (caption + bară).
- **Dreapta:** bandă ~250px (butoane like/comment/share/send).
- **Zona sigură de mesaj: centrul 1080×1440 (3:4)** — exact ce se vede în grila
  de profil (grila e dreptunghiulară din 2025; thumbnail-ul tăie ~240px sus/jos).
- **Cover:** pune titlul în centrul 3:4, nu în 9:16 complet — altfel în grid apare
  tăiat.

### 5.6 Instrumente de producție 2026

**Edits** (aplicația Meta, lansată 22 aprilie 2025, gratuită): editare, captions
automat, cutout, AI background, tracking de trenduri — 130+ funcții în primul an;
2026: versiune desktop + asistent AI. Alternativă CapCut fără watermark-ul care
te penalizează.

---

## 6. Colecția de hook-uri Instagram (șabloane ready-to-use)

Fiecare șablon = formulă + psihologia din spate. Sursa: brief v2 (analiza 40
resurse) + structurile canonice din hook-kit.

| Categorie | Șablon (gata de copiat) | Psihologia |
|---|---|---|
| **Desire-Based (About Me / trecut)** | „Am luat o pauză de o lună de la postat și tot am crescut cu 11.000 de urmăritori. Iată exact ce am făcut." | rezultat dorit obținut fără efort exagerat — dovadă vie |
| **Desire-Based (If I / viitor)** | „Dacă ar trebui să o iau de la 0 pe Instagram, iată exact cele 3 etape prin care aș ajunge la 10k." | proiecție ipotetică accesibilă începătorului |
| **Desire-Based (To You / direct)** | „Dacă vrei să devii mai bun la crearea de conținut, acest truc simplu îți economisește 10 ore pe săptămână." | apel direct „tu" pe durerea privitorului |
| **Negative Hook (frică de greșeală)** | „Oprește-te din a mai folosi [Metoda X]! Îți distrugi acoperirea pe Reels fără să-ți dai seama." | loss aversion — frica de a pierde activează instant |
| **Curiosity Gap (open loop)** | „Acest truc pe Instagram pare ilegal de știut... dar îți dublează comentariile în 24 de ore." | buclă informațională pe care creierul vrea să o închidă |
| **Pattern Interrupt (contrast vizual)** | text de impact pe ecran + mișcare bruscă spre cameră / obiect așezat pe masă | disrupție a pilotului automat din scroll |

Extensii canonice (detalii în hook-kit, knowledge/hooks-guide.md §2, dacă e
instalat): Contrarian/Unpopular Opinion, Number-Led & Proof (cifre exacte >
cifre rotunde), Audience Callout („Dacă ești [avatar] și..."), Story Open (in
medias res), Industry Shock („90% din [nișă] te mint în legătura cu...").

**Reguli de redactare (obligatorii):**
- Regula **5-8-5**: 5–8 cuvinte, nivel clasa a 5-a, fără jargon.
- **O propoziție, un mesaj** — nu împacheta două idei.
- **Specific, nu gol:** cifre exacte, denumiri, mecanisme. Zero adjective de
  umplutură.
- Într-un pachet de 5 hook-uri: minimum 3 structuri diferite.
- **Testul „Prietenul de la Cafea":** dacă sună a robot sau a manual de
  marketing, se rescrie.

---

## 7. Caption-ul viral

### 7.1 Structura

```
[LINIA 1–2: hook-ul scris — ~125 caractere vizibile în feed înainte de „...more"]
[linia de reîncadrare — întărește promisiunea]
[valoare în buline / paragrafe scurte — plătește promisiunea]
[keyword-uri naturale integrate (SEO)]
[CTA unic + schimb de valoare: „Comentează KIT și trimitem ghidul în DM"]
[3–5 hashtag-uri]
```

- Bugetul vizibil: **~125 caractere** (variază 110–150 după device). Scrie-l ca
  să convertească și truncat.
- Limită totală: 2.200 de caractere. Textul lung e OK dacă îți permite —
  „dacă nimeni nu-ți spune că e prea lung, n-a fost suficient de lungă" —
  timpul petrecut pe postare e semnal de algoritm.
- **Întrebări pe tot textul**, nu doar la final.
- Caption-ul e și **suprafață Google** din iulie 2025 — propoziții complete,
  keyword-ul subiectului prezent.

### 7.2 CTA-ul care produce comentarii (motorul Comment-to-DM)

- CTA pe **schimb de valoare**, nu pe cerșit: „Comentează CUVÂNT și primești X
  în DM" > „Dă follow dacă ți-a plăcut".
- Stratificat pe 3 straturi: text-on-screen + mențiune verbală la final + detaliu
  în caption.
- **Opiniile creează tabere, faptele nu.** Subiectivismul moderat produce
  comentarii („ce e mai bun: X sau Y?"), tehnicile de engagement care SE SIMT le
  ucid.
- **Tehnica găurii:** omiterea intenționată a unui detaliu evident — audiența
  vine să corecteze (dwell time ↑, comentarii ↑).

---

## 8. Formatele care performează în 2026

### 8.1 Reels — motorul de top-funnel
Cea mai mare reach rate (~9,8% din followers pe conturi mici; 2,25× reach vs
imagine simplă). Rolul: audiențe noi. Vezi §5.

### 8.2 Caruselele — motorul de engagement și saves
- **Max 20 slide-uri** (în app), format 1080×1350 (4:5), ~30 MB/slide.
- Date 2025–2026: engagement rate **0,55%** — cel mai mare format (Socialinsider);
  +12% engagement total vs Reels; consumul silențios de seară e teritoriul lor.
- Structura canonică: Slide 1 = hook (titlu + promisiune), slide-uri 2–N = o
  idee/slide, design pentru **save** (checklist, ghid, „return here"), ultimul
  slide = CTA + keyword.
- Slide 1 trece testul de hook ca un Reel: title de impact, fără logo mare.
- > ⚠️ Claim-ul din brief „carusele au reach +89%" e **neconfirmat public**;
  datele reale: carusele câștigă engagement/saves, Reels câștigă reach. Folosește
  ambele pentru rolurile lor.

### 8.3 Stories — motorul de relație (nu de viralitate)
- 1080×1920, max 60s/card. Rol: retenție, comunitate, DM-uri, sondaje.
- Strategia: viralitatea se face pe Reels/carusele; Stories țin audiența caldă
  între postări (2–10/zi pentru conturi active).

### 8.4 Postările text / foto — motorul de opinie
- Hook-ul trăiește în prima linie + poză. Cele 6 tipuri de hook pentru text (vezi
  hook-kit §2.7): Poza, Ceva familiar, Contrastul, Întrebările, Setarea scenei,
  Știrea.
- Detalii concrete obligatorii (nume, localități, ani) — fără ele, povestea pare
  inventată.

### 8.5 Mixul de conținut (piramida)

```
        [Stories zilnice — relație]
      [Carusele 2–4/lună — saves, autoritate]
    [Reels 2–3/săptămână — reach, top-funnel]
  [Postare opinie/foto 1–2/lună — brand personal]
```

Frecvență: baseline Meta **3–5 postări feed/săptămână**; Buffer 2025 (2M postări):
mai multe postări = reach total mai mare, fără plafon de penalizare — dar
consistența bate maratonul. Conturi mici: calitate > volum; un Reel bun pe
săptămână bătut corect > 7 medii.

---

## 9. Hack-urile avansate 2026

### 9.1 Trial Reels (workflow CORECT)

Lansate dec. 2024, extinse iul. 2025 la toți creatorii publici cu 1.000+
followeri:

1. Publici cu opțiunea **Trial** — Reel-ul e arătat **doar non-followerilor**
   (followerii NU-l văd în faza de test).
2. **Insights în ~24 de ore** (views, likes, comments, shares).
3. Dacă performează, alegi **„Share to everyone"** — abia atunci apare pe profil
   și la followeri.

> ✅ Corecție v1.2.0 (T1, Creators blog): partajarea finală poate fi **manuală**
> („Share to everyone") **sau automată** — Instagram poate distribui singur
> Reel-ul către toți dacă îl consideră performant pe baza views-urilor din primele
> **72 de ore**. Fereastra de citire corectă a testului: 24–72h (insights în ~24h,
> decizia de escaladare se joacă până la 72h). Vechea notă „72h neconfirmat" din
> v1.1.x e retrasă: cifra e documentată oficial.
> ⚠️ Chiar și în Trial, o parte din followeri pot vedea Reel-ul prin DM sau prin
> paginile de audio/locație/filtru — testul nu e 100% orb pentru baza ta.

**Când folosești:** la fiecare conținut experimental sau fiecare format nou;
testezi fără să-ți „ardezi" feed-ul. La formatul care a validat deja — publici
normal.

### 9.2 Tehnica „Triple Double" (variante, nu duplicate)

Pentru testarea aceluiași concept de mai multe ori (inclusiv prin Trial Reels),
modifică la fiecare variantă: **oglindirea orizontală** (horizontal flip),
**viteza ±5%**, **textul primului cadru**.

> ⚠️ Complianță 2026: regulile de originalitate s-au extins la foto/carusele și
> agregatoarele sunt scoase din recomandări. Variantele trebuie să fie conținut
> TĂU re-interpretat, nu repost masiv — 10+ postări „duplicat" în 30 de zile =
> pierzi recomandările. Triple Double = variație, nu spam.

### 9.3 Automatizarea Comment-to-DM (ManyChat)

- **Mecanism:** commentezi cu **cuvânt-cheie** (ex. „KIT") → DM automat cu
  link/ghidul promis. Funcționează și pe story replies.
- **Complianță:** ManyChat e **Meta Business Partner** și folosește API-ul
  oficial Instagram — utilizarea e permisă (nu e robot third-party interzis).
  Plan Pro de la ~$10–15/lună.
- **Riscuri reale (nu automatizarea, ci abuzul):** valuri identice de comentarii
  + DM-uri repetate = semnale de spam. Best practices: rate-limiting/queue pe
  postările virale, primul DM = exact promisiunea din CTA, fără link-uri
  afiliate agresive, respectarea ferestrei de mesagerie de 24h.
- **De ce funcționează:** comentariile validează interesul activ pentru
  algoritm; efect secundar: lead-ii intră în DM = suprafată de conversie.
- Limite generale de acțiuni (neoficiale, raportate de tool-uri 2025–2026):
  ~500 acțiuni/24h, ~100 DM/zi către followers, 30–40 către non-followers,
  pacing ~10/oră.

### 9.4 Serii și binge sessions

- Open loop-urile deschid serii: „partea 2 mâine" → follow-ul vine din „vreau mai
  multe de la profilul ăsta".
- Formats dovedit → produce în loturi (binge sessions) pe același format, cu
  variază unghiul; algoritmul asociază profilul cu formatul și distribuie
  secvențial.
- 2026: funcția **Series** (hub episodic pe profil cu buton „Watch Next") e în
  rollout — dacă e activă pe contul tău, folosește-o pentru serii.

### 9.5 Collab posts și Blend

- **Collab post** (autor dublu): postarea apare la ambele audiențe — reach dublat
  pe același efort. Folosește-l cu conturi complementare din nișă.
- **Blend** (2025): feed partajat de Reels în DM-uri — Reel-urile trimise
  frecvent în Blend câștigă distribuție secundară.

---

### 9.6 Pârghiile secundare 2026 (toate T3 — corpus §4)

Acestea nu înlocuiesc fundația (hook, retenție, sends), dar dau procente:

- **Audio trending, folosit devreme** (S6, S8): publicarea în **24–72h** de la
  apariția trendului prinde distribuția maximă; mai târziu, sunetul e „ars".
  Atenție: trendurile audio migrează TikTok → Instagram în ~1–2 săptămâni (S9).
- **3–5 content pillars** (S7): pilonii sunt teme repetabile în care poți produce
  la nesfârșit fără să te plictisești — baza nisei clare (§1.1).
- **Mix de formate pentru business** (S4/S9): ~60% Reels / 25% carusele / 15%
  postări statice; mix de piloni 40% educație / 25% relatable / 20% behind-the-
  scenes / 15% promoțional. Puncte de plecare, se calibrează din Insights.
- **Regula 5-3-1 de interacțiune** (S5): zilnic, interacționezi real cu 5 conturi
  mici, 3 medii și 1 mare din nișă — construiește relația care produce
  colaborări și sends reciproce.
- **Batch production** (S6, S20): filmezi 2–3 ore într-o sesiune → 4–5 Reels;
  reduci frecarea de producție și crești consistența (singurul „hack" care
  funcționează invariabil).
- **Post-viral: nu taci** (S2, S4): după un Reel care sparge, publică următorul
  material în 1–2 zile — valul de vizibilitate se transferă pe postarea nouă.

> Regulile de mai sus vin din surse de practician (T3). Le folosești ca tactici,
> le citezi ca „recomandare de practician", niciodată ca „ce spune Instagram".

## 10. Complianță și anti-penalizare

1. **Originalitate** (§1.5) — hard gate: fără repost-uri, fără watermark TikTok,
   fără agregare fără transformare.
2. **Fără engagement pods** / grupuri de schimb de like-uri — semnalele
   artificiale diluează profilul de interes al contului.
3. **Limite de acțiuni** (§9.3) — follow/unfollow în masă = flag de spam.
4. **Conținut reglementat** (sănătate, finanțe) — fără promisiuni de rezultate
   garantate; dezvăluie condițiile.
5. **AI disclosure** — conținutul generat AI semnificativ se etichetează (C2PA,
   2026).
6. **Comunitate reală:** răspunde la primele comentarii în prima oră (ferestrea
   de test a algoritmului) — conversația inițială e semnal de valoare.

---

## 11. Bucla post-publicare: Diagnostic Metric & Hook Swap

Algoritmul decide după publicare — și verdictul lui e măsurabil în Insights
(view rate / skip rate + grafic de retenție, oficiale din aug. 2025). Când o
metrică e sub țintă, cauza e cunoscută și corecția e tactică:

| Metrică sub țintă | Diagnostic | Acțiune tactică |
|---|---|---|
| **Hook rate < 25%** (skip rate mare) | hook-ul n-a oprit scroll-ul | **Hook Swap**: taie primele 3 secunde, hook nou (Contrarian/Industry Shock), republiezi după 3 zile — NU șterge clipul dacă retenția de după e bună |
| **Retenție prăbușită la 3–10s** | promisiunea hook-ului nu se plătește | rescrie deschiderea corpului; taie dead air-ul |
| **Completion < țintă** (§2.2) | pacing lent, clip prea lung | taie pauzele, viteză 1,1×, scurtează la timpul minim al promisiunii |
| **Sends sub 1/200 views** | lipsă de identificare/valoare de statut | CTA bazat pe identitate („trimite-i lui [persoana care are nevoie]") + unghi cu valoare de salvat |
| **Saves sub 1/100 views** | conținut consumabil, nu de referință | transformă în material de revenit: checklist, ghid, carusel |
| **Comentarii sub 15/1k views** | fapt rece în loc de opinie | Tehnica găurii / opinie polarizantă moderată |
| **Views 90%+ de la followeri** | nu ești în distribuția de interes | nisa neclară sau conținut prea generic — verifică §1.1 și originalitatea |
| **Skip rate > 40%** | intro slab, hook prea lent la prima secundă | taie primele cadre, hook nou la 0–1,5s (Hook Swap dacă restul clipului ține) |
| **Repost rate ≈ 0** | conținut fără valoare de identitate | adaugă unghi „asta e pentru cineva pe care îl știi" / date memorabile de trimis în Story |

**Scorecard-ul pe 6 rate-uri (S19, T3)** — framework complementar funnel-ului,
folosit când media generală e OK dar o componentă e moartă. Citește, în ordine:
**skip rate** (oprește scroll-ul?), **share rate** (e de trimis?), **like rate**
(place?), **save rate** (e de revenit?), **repost rate** (e de arătat altora din
nume propriu?), **comment rate** (provoacă opinie?). Primul rate mort din listă
îți dă reparația, fără să te uiți la restul. Verdictul final rămâne pe funnel-ul
§2.1: reperezi PRIMA etapă stricată.

**Protocolul Hook Swap:** retenție bună după secunda 3, dar skip rate peste
~65% → NU ștergi clipul; schimbi doar primele 3 secunde (hook nou pe 4 straturi
+ test mut) și republiezi după 3 zile ca să nu cannibalizezi testul variantei
originale. Hook-ul e piesă replaceable; corpul de valoare, nu.

Cerința e **mecanică, nu de inspirație**: pachetul de Hook Swap conține minimum
**3 hook-uri noi**, pe **structuri diferite** (ghid §6), fiecare cu cele 4
straturi, testul mut trecut și **5–8 cuvinte** (Regula 5-8-5). Validatorul respinge
un `hook_swap` care nu îndeplinește condiția. Regula completă de diagnostic (funnel
în ordine, ramura alternativă, criteriul de succes la 72h) e ilustrată cap-coadă în
`examples/exemplu-diagnostic.md`; versiunea verificabilă mecanic:
`examples/proba-diagnostic/output.json`.

---

## 12. Planul de acțiune în 30 de zile („Best of Nine")

### Săptămâna 1 — Setare & Cercetare
- Setup tehnic complet (§3, toate cele 7 puncte PASS).
- **O singură nișă clară** (dacă ai nise multiple → separă conturile).
- Creează folderul **„Content Pool"** (Saved collection în Instagram) și salvează
  **20+ Reels virale (>1M views)** din nișa ta. Pentru fiecare, notează: structura
  hook-ului, durata, mecanismul de retenție, CTA-ul.
- Definește 3 **content pillars** (teme pe care le poți repeta fără să te plictisești).

### Săptămâna 2 — Testing: cele 9 formate
- Alege **3 formate dovedite** din Content Pool (ce a mers la alții din nișa ta).
- Recreează-le **în vocea ta** (nu copie — originalitate, §1.5) și postează-le
  **de 3 ori fiecare** (total 9 Reels), rotind hook-urile din §6.
- Folosește **Trial Reels** pentru variantele experimentale (§9.1).
- Publică la orele în care Insights arată audiența ta activă (baseline: mar–mie
  9–11 dimineața).

### Săptămânile 3–4 — Scale & Binge Sessions
- Analizează funnel-ul metricilor (§2.1) pentru toate cele 9.
- **Formatul câștigător** (cel mai mare watch time + sends): dublezi producția pe
  el — sesiuni de producție în loturi, variând hook-ul, nu formatul.
- Deschide o **serie** pe formatul câștigător (open loop-uri, §9.4) pentru
  follow-uri.
- Activează **Comment-to-DM** pe postările cu valoare de trimis (§9.3).

**Metrica de succes a lunii:** un Reel în valul 2+ de distribuție (majoritate
non-followeri) sau 1 format validat cu watch time > media 2026 (8,5s).

### Varianta scurtă — testarea în 10 zile (S20, T3)

Pentru conturi care vor un ciclu mai rapid decât 30 de zile (sau pentru testarea
unei singure idei de business):

1. **9 Reels în 10 zile** — 1 problemă reală de client, abordată în **3 formate**,
   fiecare postat de 3 ori (rotind hook-ul, nu formatul).
2. **3 revizuiri de date** (zilele 3, 6, 9) — te uiți la funnel-ul §2.1, nu la
   views brute.
3. **O singură ajustare per rundă** — altfel nu știi ce a produs diferența.

Traseul de conversie care se validează în paralel (S7, S20): **Reel → profil →
postări fixate (dovadă + ofertă) → CTA**. Dacă Reel-ul performează dar profilul
nu convertește, problema nu e conținutul, sunt primele 9 postări fixate.

---

## 13. Anti-pattern-uri (reject la audit)

| Anti-pattern | De ce e fatal | Reparație |
|---|---|---|
| Intro de teleshopping („Bună guys, welcome back!") | pierde secunda 1 | hook direct în secunda 0–1 |
| Hook verbal înțeles doar cu sunet | 80%+ privesc fără sonor | text-on-screen + vizual de impact |
| Watermark TikTok / CapCut | deprioritare în recomandări | Edits (Meta) sau export curat |
| Repost masiv / agregator | 10+/30 zile → pierzi recomandările | recrea în vocea ta (originalitate) |
| Clickbait fără plată | retenția prăbușită la sec. 10; trust pierdut | hook-ul = promisiunea pe care corpul o plătește |
| Text în afara safe zone-ului | UI-ul îl acoperă; cover tăiat în grid | mesaj în centrul 3:4 |
| 30 de hashtag-uri | semnal de spam; de ani de zile ineficient | 3–5 relevante |
| „Dă follow" ca singur CTA | cerșit = zero schimb de valoare | CTA pe schimb de valoare + keyword DM |
| Două idei într-un hook | mesaj diluat | o idee, un unghi |
| Nisa neclară (teme împrăștiate) | algoritmul nu te clasifică | o nișă, 3 piloni de conținut |
| Oferta în primele secunde | regula 95/5 încălcată; retenția moare | plasare la final sau în DM |
| Cifre inventate („+89% reach", „150–450 views/share") citate ca fapt | pierdere de credibilitate | cifre confirmate sau „heuristica" marcată |

---

## 14. Checklist-ul de calitate (criterii de audit)

Folosit de `agents/viral-auditor.md`. Scor 0–100, prag de livrare 85.

| Criteriu | Puncte | Test |
|---|---|---|
| **Hook & scroll-stop** | 25 | primele 3s pe 4 straturi (vizual + verbal 5–8 cuvinte + text-on-screen ≤3 cuvinte + audio); test mut trecut; fără intro; promisiune clară |
| **Retenție & structură** | 20 | corpul plătește promisiunea; attention reset la 2–3,5s; durată = timpul minim al promisiunii; regula 95/5 |
| **Discoverability (SEO)** | 20 | keyword în caption (primele 125 caractere), în bio/Name field (la cont), 3–5 hashtag-uri, text-on-screen cu keyword, alt text unde e cazul |
| **Complianță & originalitate** | 15 | fără watermark/repost, fără clickbait fără plată, fără cifre inventate, fără promisiuni garantate, AI disclosure unde trebuie |
| **CTA & buclă de creștere** | 20 | CTA pe schimb de valoare + stratificat (ecran/verbal/caption); producă de comentarii sau sends; open loop pentru serie unde are sens |

**Bareme:** ≥ 85 PASS · 70–84 REVISE (listează reparațiile) · < 70 REJECT
(regenerează).

---

## 15. TikTok & YouTube Shorts — adaptările cross-platform

Același conținut de bază poate lucra pe toate cele trei platforme short-video —
dar NU prin cross-postare identică. Regula de producție: **filmezi o dată,
exportezi master curat, editezi nativ per platformă.**

### 15.1 Regula de aur a cross-posting-ului

1. **Master curat fără watermark** — filmezi în Edits (Meta) sau camera nativă
   și exporți master-ul 1080×1920 fără logo (watermark-ul TikTok penalizează
   confirmat pe Instagram; pe TikTok și YouTube nu e confirmat oficial, dar
   semnalează conținut „reciclat").
2. **Editare nativă per platformă:** subtitrări/în stilul platformei, sunet
   trending unde e relevant (TikTok), titlu + metadata pe Shorts, caption +
   hashtag-uri per platformă (§4.3 / §15.3).
3. **Nu reposta identic:** algoritmul fiecaruie detectează duplicatul; YouTube
   demonetizează conținutul „mass-produced/repetitiv" (policy inauthentic
   content, iul. 2025).

### 15.2 TikTok în 2026

- **Semnale de ranking** (consens third-party, fără ierarhizare oficială):
  watch time, completion, **rewatch**, plus shares/saves/comentarii ca semnale
  de „passion". Mecanicile de retenție din §5 funcționează identic.
- **Lungimi:** top conținut rămâne **21–34s**; TikTok a împins long-form (teste
  până la 60 min din apr. 2025, pentru monetizare) — dar pentru reach de la
  zero, scurtul câștigă.
- **TikTok SEO e mai puternic decât pe Instagram:** 86% din Gen Z caută
  săptămânal pe TikTok; keyword-urile funcționează în caption, text-on-screen
  ȘI audio vorbit. Tratează fiecare clip ca o pagină de căutare.
- **Trenduri & sunete:** sunetul trending mai dă boost în FYP, dar algoritmul a
  trecut pe „niche content is king" — **remixezi** trendul prin nisa ta, nu-l
  copiezi identic.
- **Frecvență:** 2–5 postări/săptămână sweet spot (Socialinsider); randamente
  descrescătoare peste.
- **Audiența:** cea mai tânără (47%+ sub 30 de ani); ER/views ~4,2%; comentarii
  ~50/video (2,5× Reels) — formatul preferă opinia și conversația.

### 15.3 YouTube Shorts în 2026

- **Max 3 minute din 15 oct. 2024** (standardul era 60s). Distribution-driven
  de feed; evergreen/search e secundar.
- **Metrica-cheie: „Viewed vs. Swiped Away"** în YouTube Studio — țintă **70%+
  viewed** (echivalentul hook rate-ului de pe Instagram). La 40–50% swipe away,
  distribuția scade drastic.
- **75%+ din view-urile YouTube 2025 au fost Shorts** — domină discovery-ul;
  convertește în abonați mai slab decât long-form, deci folosești Shorts pentru
  top-funnel și canalul long pentru relație/monetizare.
- **Titlul contează** (nu există cover în sensul Reels): titlu + primele cadre
  fac click-ul; metadata SEO (titlu, descriere) e citită de YouTube.
- **Audiența:** cea mai largă (~2 mld. utilizatori), ER/views 5,91%, dar
  comentarii ~10/video — mai puțin conversație, mai mult volum.

### 15.4 Tabelul de adaptare per platformă

| Element | Instagram Reels | TikTok | YouTube Shorts |
|---|---|---|---|
| Lungime țintă | 30–60s (reach) | 21–34s | 20–60s (max 3 min) |
| Hook rate / prag | ≥25–35% viewed >3s | completion + rewatch | **70%+ viewed vs swiped** |
| SEO | keyword în caption + text | caption + text + audio vorbit | titlu + descriere + speech |
| Trenduri/sunete | secundar | **remix trend** prin nișă | secundar |
| Hashtag-uri | 3–5 | 3–5 (max ~5) | 2–3 (topic tags) |
| Frecvență | 2–3/săpt. | 2–5/săpt. | 3–5/săpt. posibil (feed lent) |
| Comentarii (rol) | mediu (20/video) | **mare (50/video)** — opinie | mic (10/video) — volum |
| CTA preferat | keyword DM (ManyChat) | comentariu + follow | abonare + playlist/serie |

> Cifrele de comentarii/ER per platformă: Socialinsider aug. 2026 — folosite ca
> orientare, nu ca ținte contractuale.

---

## 16. Limbi și piețe — calibrarea kitului

Kitul rulează în limba din `brief.language`. Regulile mecanice (bugete de
caractere, safe zones, durate) sunt independente de limbă; ce se calibrează
este **limbajul și piața**.

### 16.1 Matricea de calibrare

| Limbă / piață | Hook verbal (Regula 5-8-5) | Notă de piață |
|---|---|---|
| **RO (implicit)** | 5–8 cuvinte | Piață mică: temele universale de masă (Bula Mai Mare din hook-kit — Bani, Relații, Sănătate, Familie) sunt aproape obligatorii pentru reach mare; nișa pură plafonează la zeci de mii de views. Dovadă locală (localități, lei, contexte RO) crește credibilitatea. |
| **EN (global)** | 5–8 cuvinte | Poți fi mult mai nișat — piața suportă nișe pure cu milioane de views. VoC per piață (US ≠ UK ≠ AU): expresii diferite pentru aceeași durere. |
| **DE** | **4–6 cuvinte** (cuvinte compuse lungi) | Precizie și dovadă tehnică > hype; umorul uscat funcționează, superlativele americane resping. |
| **FR / IT / ES** | 5–8 cuvinte | Emoție și relațional > cifre seci; programul zilnic (prânz/seară) diferă de RO — calibrezi din Insights locale. |
| **Piețe asiatice (JP/KO)** | 3–6 cuvinte | Cortezie formală în hook, mai puțin „tu" direct; dubbing-ul Meta AI suportă JP/KO din 2026. |

### 16.2 Regulile de scriere multi-limbă

1. **Scrii nativ în limba țintă — NU traduci din RO.** Ordinea cuvintelor,
   expresiile și umorul nu se traduc; un hook tradus pierde testul „Prietenul
   de la Cafea".
2. **VoC per limbă.** Citațiile de durere din brief trebuie să existe în limba
   pieței țintă; fără ele → `NEVOIE_RESEARCH` (nu adaptezi VoC-ul românesc).
3. **Bugetele de caractere rămân:** ~125 caractere vizibile în caption (prag
   device-based, nu lingvistic); text-on-screen ≤3 cuvinte — la limbile cu
   cuvinte lungi (DE) folosești 1–2 cuvinte scurte.
4. **Pârghia de traducere 2026:** dubbing-ul Meta AI (1.000+ followeri) și
   traducerile automate de captions deschid audiențe externe FĂRĂ refilmat —
   dar sunt distribuție, nu înlocuitor pentru conținut nativ pe piața aia.

---

## 17. Surse

- `context/brief-viral-instagram-v2.pdf` — brief strategic v2 (40 resurse video):
  interest space, metrici critici, hook-uri, Trial Reels, plan 30 zile.
- Blog Instagram Creators (30.04.2024, actualizat 30.04.2026) — distribuție în
  valuri, reguli de originalitate (extinse la foto/carusele în 2026).
- Declarații Adam Mosseri 2024–2026 (raportate de presă: contentgrip, hookpoint,
  Socialsamosa) — watch time, likes per reach, sends per reach; views ca metrică
  unificată (07–08.08.2024).
- help.instagram.com — spec-uri Reels/Carusele/Stories, Media Quality, Account
  Status, traduceri + dubbing Meta AI (aug. 2025), indexare Google (10.07.2025),
  Trial Reels (10.12.2024; extindere 1k+ followeri iul. 2025 — thekeyword.co).
- Metricool Instagram Study 2026 (24,4M postări, 375k conturi) — watch time
  ~8,5s, publishing +35%, carusele +24% YoY.
- Socialinsider Benchmarks (feb. 2026, 15M postări) — ER 0,45%, carusele 0,55%,
  Reels reach rate 5,60% la 30–60s.
- Buffer (aug. 2025, 2M postări) — frecvență: mai multe postări → reach total
  mai mare; consistența.
- Sprout Social 2025 — timing: mar–mie 9–11 AM, L–V 9–16.
- ManyChat (feb. 2025) — Meta Business Partner, API oficial, planuri de preț.
- Rival IQ 2025, Dash Social 2026, Collabkit, Clouted, Biddyco/Billo (hook rate
  benchmarks), WERSM/Yahoo (metrici oficiale de retenție, aug. 2025).
- TikTok/Shorts (research web oct. 2026): Metricool TikTok study (sep. 2025) și
  TikTok SEO guide; Socialinsider benchmarks (oct. 2025, aug. 2026) — frecvență
  TikTok, comentarii/ER per platformă, audiențe; MakeUseOf/Videostew (Shorts 3
  min, 15.10.2024); ReelRise/Google Support („Viewed vs. Swiped Away" 70%+);
  Social Samosa / support.google.com (policy „inauthentic content", 15.07.2025);
  The Utopia/PhoneArena (TikTok long-form 60 min test, apr. 2025); Aspect
  Digital (86% Gen Z caută pe TikTok săptămânal); Clouted (top TikTok 21–34s).
- Cifre marcate „heuristica kitului" (ținte sends/saves/comments/completion) —
  din brief, neconfirmate public; folosesc-le ca ținte de lucru, nu ca fapte.
- **Corpusul 2026 (v1.2.0)** — 20 de surse analizate în `knowledge/corpus-2026.md`:
  10 articole (SocialPilot sep. 2026; Hootsuite iul. 2026; PostEverywhere feb.
  2026; Aurelius Media apr. 2026; Deftsoft mai 2026; Maya Digital Desk mar. 2026;
  Pictame ian. 2026; True Future Media feb. 2026; UseFastlane iul. 2026;
  ReelsMaker AI apr. 2026 — inaccesibil) + 10 clipuri YouTube (Robert Benjamin ×3,
  Tech Paradise, Build Your Tribe/Brock Johnson, Metricool, Jade Beason,
  Jagaltech, Enrico Incarnati, HubSpot Marketing). Din corpus au intrat în ghid:
  skip rate ca semnal negativ, țintele de share/save/completion, definiția
  relativă a viralității, scorecard-ul pe 6 rate-uri, fazele de distribuție,
  testarea în 10 zile, pârghiile secundare (§9.6).
- **Verificări T1 folosite la validare:** Mosseri (ierarhia semnalelor, connected
  vs. unconnected reach), Creators blog (Trial Reels — insights ~24h, partajare
  manuală sau automată pe baza primelor 72h), Creators blog (Reels ≤3 min
  eligibile pentru non-followeri, 21 ian. 2025), Social Media Today (plafon 5
  hashtag-uri, dec. 2025), Metricool Research Study 2026 (24.364.803 postări /
  375.118 conturi).

---

## 18. Proveniență și niveluri de încredere (corpus 2026)

Kitul nu tratează toate sursele la fel. Fiecare cifră livrată are un **tier**,
și tier-ul se vede în output:

| Tier | Ce e | Cum se livrează |
|---|---|---|
| **T1 — oficial** | Instagram/Meta (help center, Creators blog, anunțuri), Adam Mosseri | „Instagram spune că…" |
| **T2 — studiu public** | Metricool Research Study (24,36M postări), Socialinsider, Buffer, Sprout Social | „studiu Metricool 2026: …" |
| **T3 — practician** | bloguri de agenție/tool, creatori YouTube, materiale „data-backed" fără metodă | „recomandare de practician (corpus 2026)" — tactică, nu benchmark |
| **R — respins** | cifre fără metodă, ponderi de semnale „exacte", tabele de ore globale, boost-uri magice | nu intră în ghid |

**Regula de conflict:** T1 > T2 > T3. Două surse T3 care se contrazic nu se
„mediatează" — se păstrează fie regula cu mecanism explicabil, fie se elimină
cifra. Exemplu din corpus: „10+ postări/săptămână = randamente descrescătoare"
(S9, T3) a fost respins în favoarea T2 (Buffer 2025: volumul crește reach-ul
total, consistența bate maratonul).

**Ce nu se inventează niciodată:** un framework dintr-un clip YouTube fără
transcript verificabil (7 din 20 de surse au picat testul de acces), o pondere de
semnale, un „score" de originalitate cu nume propriu. Lipsa de sursă =
`NEVOIE_RESEARCH`, nu improvizație.

**Când se re-verifică:** la fiecare ciclu de research (≈trimestrial), se
re-rulează analiza pe surse noi și se incrementează versiunea ghidului. Regulile
mecanice (safe zones, bugete de caractere, 5-8-5) nu se schimbă cu moda
algoritmului; se schimbă doar tacticile și țintele.
