# Run de probă — pedodonție (instagram-viral-kit v1.2.0)

> Livrabil de referință generat pe regulile kitului v1.2.0, ca probă de funcționare
> cap-coadă: brief → generare → audit → validare mecanică → livrare lizibilă.

- **Brief:** `examples/proba-pedodontie/brief.json` (cont fictiv `@zambetul.mic`, 1.850 followeri)
- **Nișă:** pedodonție — dentist pentru copii 0–12 ani
- **Livrat:** 3 Reels + 1 carusel + plan de 30 zile + audit de setup
- **Validare mecanică:** `python tools/validate_output.py output.json` → VALID
- **Audit suplimentar:** `python audita.py` → 0 probleme

## 1. Scoruri de audit (viral-auditor, prag 85/100)

| Livrabil | Hook | Retenție | Discoverability | Complianță | CTA | Total | Verdict |
|---|---|---|---|---|---|---|---|
| R1 — Frica de dentist se învață acasă, nu la cabinet | 23/25 | 19/20 | 18/20 | 15/15 | 19/20 | **94** | **PASS** |
| R2 — 3 greșeli în ziua vizitei la dentist | 22/25 | 18/20 | 18/20 | 15/15 | 17/20 | **90** | **PASS** |
| R3 — Sub 6 ani: ce se întâmplă (și ce nu) la prima vizită | 21/25 | 18/20 | 18/20 | 15/15 | 17/20 | **89** | **PASS** |
| P1 — Prima vizită la dentist: 7 zile de pregătire (carusel) | 22/25 | 19/20 | 18/20 | 15/15 | 16/20 | **90** | **PASS** |
| | | | | | | **medie 90.8** | 4 PASS / 0 REVISE / 0 REJECT |

Probleme rămase (toate P2 — nu blochează livrarea):
- **R1** [P2] Text-on-screen „GREȘEALA PĂRINȚILOR” are 20 caractere — la 3:4 rămâne lizibil, dar mai slab contrastant pe fundal deschis. → Adaugă o bandă semi-transparentă în spatele textului.
- **R2** [P2] Textul de ecran „SALVEAZĂ” apare abia în ultimele 4 secunde (0:41–0:45) — CTA-ul nu e vizibil pentru cine abandonează la 0:35. → Avansează textul „SALVEAZĂ” la 0:35, suprapus peste ultimul punct, sau ridică salvarea în textul de la 0:32.
- **R3** [P2] Sunetul ambiental de cabinet poate conține voci de copii identificabile. → Folosește doar înregistrări cu acord scris sau înlocuiește cu ambianță neutră.
- **P1** [P2] Caruselul cere două acțiuni (salvează + comentează) — risc de diluare a CTA-ului. → Ține salvarea pe slide 10 și keyword-ul în ultima linie din caption, ca acum; nu adăuga al treilea CTA.

## 2. Reels

### R1 — Frica de dentist se învață acasă, nu la cabinet

- **Structură hook:** `negative_warning` · **Pilon:** prima vizită fără frică · **Scop:** reach · **Durată:** 32s

**Hook (primele 3 secunde, 4 straturi sincronizate):**

```text
[vizual]        0–1s mid-motion: mâna părintelui închide brusc ușa cabinetului, în fundal scaunul dentar gol
[verbal]        „Frica de dentist se învață acasă, nu aici.” (8 cuvinte)
[text-on-screen] GREȘEALA PĂRINȚILOR
[audio]         whoosh + tăcere totală 1 secundă, apoi voce fără muzică
Test mut: PASS
```

**Script (Attention Reset la fiecare ≤4s, marcat):**

```text
0:00–0:01  [vizual] mid-motion — mâna închide ușa cabinetului      [reset: whoosh]
0:01–0:03  „Frica de dentist se învață acasă, nu aici.”            [reset: jump-zoom pe față]
0:03–0:06  „Trei lucruri care o construiesc în casa voastră.”      [reset: b-roll scaun gol]
0:06–0:09  „1. Nu-i spune «nu doare».”                              [reset: text pe ecran „1”]
0:09–0:12  „Când doare, nu te mai crede.”                           [reset: cadru apropiat]
0:12–0:15  „2. Nu promite cadouri.”                                [reset: schimbare unghi]
0:15–0:18  „Vizita devine negociere, nu rutină.”                    [reset: pop SFX]
0:18–0:21  „3. Nu-l duce când are deja durere.”                     [reset: text pe ecran „3”]
0:21–0:24  „Prima amintire rămâne cea rea.”                         [reset: zoom out]
0:24–0:27  „Du-l o dată doar să salutăm.”                           [reset: cadru larg cabinet]
0:27–0:30  „Fără tratament, fără surprize.”                         [reset: revenire pe față]
0:30–0:32  CTA verbal + text mare „GHIDUL”                          [reset: text mare „GHIDUL”]
```

**Editare:**

- [x] Dead air tăiat; nicio pauză mai lungă de 0,4s între propoziții.
- [x] Subtitrări cuvânt-cuvânt, centrate, galben pe negru (testul mut).
- [x] Mixaj: voce 0 dB, muzică −20 dB, whoosh doar la reset-uri.
- [x] Text cheie în centrul 3:4 (1080×1440) — nimic sub 350px jos sau 250px dreapta.
- [x] Cover: „FRICA SE ÎNVAȚĂ ACASĂ” lizibil în grila 3:4.
- [x] Export 1080×1920, MP4 H.264, 30fps, fără watermark.

**Caption:**

```text
Prima vizită la dentist pentru copii: frica se construiește acasă, în 3 propoziții.
(83 caractere vizibile — buget ~125)

Cele trei propoziții care fac prima vizită un coșmar:
1. „Nu doare, promit.” → când doare, copilul nu mai crede nimic.
2. „Dacă ești cuminte, îți iau ceva.” → vizita devine negociere.
3. Prima vizită se face când apare durerea. → prima amintire rămâne cea rea.

Ce funcționează în schimb: o vizită scurtă, „doar salutăm”, fără tratament,
cu părintele lângă scaun. Copilul memorabil nu ce i-ai spus, ci cum te-a văzut pe tine.

Care dintre cele trei propoziții ți-a scăpat și ție? Scrie în comentarii. 👇

Comentează GHID și îți trimit lista de 7 zile de pregătire (1 pagină) în DM.

#pedodontie #dentistpentrucopii #primavizita #parinti #sănătateadintară
```

**Publicare:** `trial_reels` · Format nou pentru cont → Trial Reels; ora din Insights (baseline mar–mie 9–11). · calitate maximă: ON · prima oră: Răspunde la fiecare comentariu în prima oră; adună manual keyword-urile până se activează ManyChat.

**NEVOIE_RESEARCH:** audience.voC_quotes — citatele de durere din caption sunt DEMO; înlocuiește-le cu citate reale (modula-research) înainte de filmare.

### R2 — 3 greșeli în ziua vizitei la dentist

- **Structură hook:** `number_led_proof` · **Pilon:** mituri și greșeli ale părinților · **Scop:** saves_authority · **Durată:** 45s

**Hook (primele 3 secunde, 4 straturi sincronizate):**

```text
[vizual]        0–1s: cadru din mașină, geanta de pe scaunul din față se răstoarnă și cade jucăria copilului
[verbal]        „Trei greșeli care fac prima vizită un coșmar.” (8 cuvinte)
[text-on-screen] 3 GREȘELI
[audio]         pop SFX + muzică discretă, tăiată la fiecare punct
Test mut: PASS
```

**Script (Attention Reset la fiecare ≤4s, marcat):**

```text
0:00–0:02  [vizual] geanta se răstoarnă, jucăria cade               [reset: pop SFX]
0:02–0:05  „Trei greșeli care fac prima vizită un coșmar.”         [reset: jump-zoom]
0:05–0:08  „1. Programezi la ora somnului, după grădiniță.”         [reset: text „1”]
0:08–0:11  „Copilul obosit nu are resurse pentru nou.”              [reset: b-roll mașină]
0:11–0:14  „2. Intri tu primul și vorbești cu medicul.”            [reset: schimbare cadru]
0:14–0:17  „Zece minute în care copilul așteaptă.”                  [reset: cadru apropiat]
0:17–0:20  „Și își imaginează ce se întâmplă acolo.”                [reset: pop SFX]
0:20–0:23  „3. Pleci imediat după.”                                [reset: text „3”]
0:23–0:26  „Prima vizită trebuie să fie scurtă.”                    [reset: schimbare unghi]
0:26–0:29  „Se termină înainte de oboseală.”                        [reset: cadru larg]
0:29–0:32  „Dimineața, împreună, scurt.”                            [reset: text pe ecran]
0:32–0:35  „Fără tratament în prima vizită.”                         [reset: b-roll cabinet]
0:35–0:38  „Doar familiarizare cu cabinetul.”                      [reset: pop SFX]
0:38–0:41  „Programează și respectă ora.”                          [reset: revenire pe față]
0:41–0:45  CTA „SALVEAZĂ pentru ziua programării”                   [reset: text mare „SALVEAZĂ”]
```

**Editare:**

- [x] Fiecare dintre cele 3 puncte începe cu text-on-screen numerotat (dwell time).
- [x] Subtitrări cuvânt-cuvânt; cifrele scrise cu cifre, nu cu litere.
- [x] B-roll din cabinet cu acord scris (fără pacienți identificabili).
- [x] Safe zone respectată: textul numerotat în centrul 3:4.
- [x] Export fără watermark, 1080×1920, 30fps.

**Caption:**

```text
Dentist pentru copii: 3 greșeli care transformă prima vizită în coșmar.
(71 caractere vizibile — buget ~125)

1. Ora: după grădiniță, la ora somnului. Copilul obosit nu are resurse pentru ceva nou.
2. Ordinea: părintele intră primul și vorbește zece minute. Copilul așteaptă și completează golul cu scenarii.
3. Finalul: pleci imediat, în grabă. Prima vizită trebuie să fie scurtă și să se termine înainte de oboseală.

Regula simplă: dimineața, împreună, scurt. Fără tratament în prima vizită — doar familiarizare.

Care e greșeala pe care o faci deja? (a doua e cea mai des întâlnită în cabinet)

Salvează postarea pentru ziua în care programezi și comentează LISTA pentru ghidul primelor 7 zile în DM.

#primavizitaladentist #dentistcopii #pedodontie #sfaturipentruparinti #sanatatedentara
```

**Publicare:** `normal` · Format de tip listă = format validat în nișă → publicare normală, marți 9:30. · calitate maximă: ON · prima oră: Răspunde cu un al patrulea pont la primele comentarii (dwell time pe postare).

**NEVOIE_RESEARCH:** content_pool.proven_formats — formatul „3 greșeli” e presupus dovedit; verifică în Content Pool (20+ Reels din nișă) înainte de scale.

### R3 — Sub 6 ani: ce se întâmplă (și ce nu) la prima vizită

- **Structură hook:** `audience_callout` · **Pilon:** prima vizită fără frică · **Scop:** leads_comment_to_dm · **Durată:** 38s

**Hook (primele 3 secunde, 4 straturi sincronizate):**

```text
[vizual]        0–1s: mâna unui copil mic pune o jucărie pe scaunul dentar, apoi se urcă singur
[verbal]        „Dacă copilul are sub 6 ani, citește asta.” (8 cuvinte)
[text-on-screen] SUB 6 ANI
[audio]         sunet ambiental de cabinet, fără muzică (autenticitate)
Test mut: PASS
```

**Script (Attention Reset la fiecare ≤4s, marcat):**

```text
0:00–0:02  [vizual] copilul urcă singur pe scaun                    [reset: sunet real, fără muzică]
0:02–0:05  „Dacă copilul are sub 6 ani, citește asta.”              [reset: jump-zoom]
0:05–0:08  „Sub 6 ani nu se tratează ca la adult.”                  [reset: b-roll instrumente]
0:08–0:11  „Se obișnuiește, în pași mici.”                         [reset: cadru apropiat]
0:11–0:14  „Vizita 1: copilul vede, atinge, întreabă.”              [reset: text „FĂRĂ TRATAMENT”]
0:14–0:17  „Fără tratament în prima vizită.”                        [reset: schimbare unghi]
0:17–0:20  „Vizita 2: curățare blândă.”                            [reset: text „2”]
0:20–0:23  „Doar dacă a stat liniștit.”                            [reset: cadru larg cabinet]
0:23–0:26  „I se anunță fiecare pas înainte.”                       [reset: pop SFX]
0:26–0:29  „Vizita 3+: tratament pe bucăți mici.”                   [reset: text „3+”]
0:29–0:32  „Cu pauze, la cerere.”                                  [reset: revenire pe față]
0:32–0:35  „Scopul nu e dintele de azi.”                           [reset: cadru cu copilul]
0:35–0:38  CTA verbal + text mare „GHIDUL”                          [reset: text mare „GHIDUL”]
```

**Editare:**

- [x] Fără muzică tensionată — sunetul cabinetului vinde autenticitatea.
- [x] Text-on-screen „FĂRĂ TRATAMENT” exact în momentul rostit (sincron).
- [x] Niciun cadru cu pacienți identificabili; acord scris pentru spațiu.
- [x] Cover 3:4: „SUB 6 ANI” + fața copilului, fără instrumente în prim-plan.
- [x] Export 1080×1920, MP4 H.264, 30fps, fără watermark.

**Caption:**

```text
Dentist pentru copii: prima vizită sub 6 ani, pas cu pas.
(57 caractere vizibile — buget ~125)

Sub 6 ani, obiectivul primei vizite nu e tratamentul — e obișnuința.

• Vizita 1: copilul vede cabinetul, atinge instrumentele, întreabă. Zero tratament.
• Vizita 2: curățare blândă, doar dacă a stat liniștit și i s-a explicat înainte fiecare pas.
• Vizita 3+: tratamentul propriu-zis, pe bucăți mici, cu pauze la cerere.

Scopul nu e dintele de azi, e ca la 10 ani copilul să intre singur în cabinet.

La ce vârstă ai dus copilul prima dată? Spune-mi în comentarii — și zi-mi ce te-a oprit.

Comentează GHID și primești în DM lista de 7 zile de pregătire (1 pagină, exact ce e în postare).

#dentistcopii #pedodontie #primavizita #parintiro #sănătateadintară
```

**Publicare:** `normal` · Postarea de conversație — joi seara 19:00, când părinții citesc în pat (verifică în Insights). · calitate maximă: ON · prima oră: Răspunde fiecărui părinte cu un răspuns personalizat (nu șablon); pregătește DM-ul cu ghidul înainte.

**NEVOIE_RESEARCH:** offer.lead_magnet — confirmă că lista de 7 zile există fizic înainte de a rula CTA-ul cu keyword.

## 3. Carusel

### P1 — Prima vizită la dentist: 7 zile de pregătire (carusel)

- **Format:** carousel · **Pilon:** prima vizită fără frică · **Slide-uri:** 10

| # | Text | Design | Referință |
|---|---|---|---|
| 1 | Prima vizită: 7 zile de pregătire | HOOK — titlu mare, fundal crem, începe cu cifra 7 |  |
| 2 | Ziua 1–2: joacă „dentistul” acasă cu o lanternă mică. | ilustrație simplă, o singură idee pe slide |  |
| 3 | Ziua 3: citește o carte despre dentist. Nu una despre durere. | copertă de carte reală, cadru apropiat |  |
| 4 | Ziua 4: scoate din vocabular „doare” și „nu-ți face nimic”. | text tăiat cu o linie vizuală |  |
| 5 | Ziua 5: programează dimineața, nu după grădiniță. | comparativ zi/noapte, fără dramatizare |  |
| 6 | Ziua 6: vizită scurtă — „doar salutăm”, fără tratament. | cadru cu copilul pe scaun, părintele aproape |  |
| 7 | Ziua 7: somn bun, mic dejun, fără discuții în mașină. | checklist cu bife |  |
| 8 | Ce NU faci: nu minți că nu se întâmplă nimic. | slide de tip „anti-sfat”, marcat vizual diferit |  |
| 9 | La cabinet: părintele stă jos, copilul vede tot, prima vizită nu are tratament. | 3 puncte scurte, nu text lung |  |
| 10 | Lista completă de 7 zile: salvează slide-ul și bifează. | REFERENCE — design de listă de salvat, numele contului jos, discret | ✅ |

**Open loop:** Partea 2: ce întrebi medicul în primele 3 minute (urmează miercurea viitoare).

**Caption:**

```text
Prima vizită la dentist pentru copii: planul de 7 zile, salvat de părinți.
(74 caractere vizibile)

Nu ai nevoie de curaj, ai nevoie de 7 zile de pregătire. Slide cu slide:

• Jocul „dentistul” acasă — copilul explorează înainte să fie explorat.
• Cărți despre dentist, nu despre durere.
• „Doare” și „nu-ți face nimic” ies din vocabular.
• Ora dimineții bate ora somnului.
• Prima vizită e de salut, nu de tratament.

Ce lipsește din planul tău: emoția ta. Copilul citește fața părintelui înainte să citească orice afiș.

La ce zi ai ajuns tu? Spune în comentarii și salvează pentru luna în care programezi.

Salvează postarea pentru ziua în care programezi și comentează LISTA pentru versiunea PDF de 1 pagină în DM.
SALVARE: Salvează pentru săptămâna în care ai programarea.

#primavizitaladentist #dentistpentrucopii #pedodontie #parinti #sănătateadintară
```

## 4. Plan de 30 zile

**Best of Nine — 30 zile (adaptat pedodonție)** · nișă: pedodonție — dentist pentru copii 0–12 ani · piloni: prima vizită fără frică, obiceiuri acasă, mituri și greșeli ale părinților

### Săptămâna 1 — Setare & Cercetare
- Repară cele 2 FAIL de setup (indexare Google, bio SEO) ÎNAINTE de orice postare.
- Construiește Content Pool: 20+ Reels virale din pedodonție, cu notițe (structură hook, durată, mecanism de retenție, CTA).
- Cere 5 citate reale de la părinți din cabinet (acord scris) → VoC înlocuiește frazele demo.
- Pregătește ghidul de 7 zile (PDF, 1 pagină) — CTA-ul cu keyword nu are voie să promită ceva inexistent.
- **Metrică de succes:** 7/7 puncte de setup PASS + 20 Reels în Content Pool + ghid PDF scris

### Săptămâna 2 — Testing: cele 9 formate
- Alege 3 formate dovedite din Content Pool (ex: „3 greșeli”, „povestea unei urgențe”, „ce face medicul pas cu pas”).
- Recreează-le în vocea cabinetului (fără copiere) și postează fiecare de 3 ori → 9 Reels.
- Rulează R1–R3 din acest pachet; primele două formate noi prin Trial Reels.
- Publică la orele din Insights; verifică rezultatul la 72h, nu la 30 de minute.
- **Metrică de succes:** 9 Reels publicate + raport la 72h pentru fiecare (hook rate, completion, sends)

### Săptămâna 3 — Scale pe formatul câștigător
- Identifică formatul cu cel mai bun watch time + sends și dublează producția pe el.
- Produce în lot (2–3 ore într-o sesiune → 4–5 Reels), variind hook-ul, nu formatul.
- Activează Comment-to-DM (ManyChat) pe Reels cu valoare de trimis; promisiunea din DM = exact cea din CTA.
- Publică caruselul P1 (motorul de saves) și Story-uri zilnice cu sondaje despre frica de dentist.
- **Metrică de succes:** 1 format validat (watch time > 8,5s) + 20 salvări la carusel + automatizarea activă

### Săptămâna 4 — Serii, comunitate, conversie
- Deschide seria „Prima vizită, pas cu pas” cu open loop la finalul fiecărui Reel.
- Postează a doua parte din open loop-ul caruselului (ce întrebi medicul în primele 3 minute).
- Verifică traseul comercial: Reel → profil → postări fixate (dovadă + ofertă) → CTA, și fixează 3 postări.
- Răspunde în primele 30–60 de minute la fiecare postare; pune întrebarea de opinie în caption.
- **Metrică de succes:** un Reel cu majoritate de views de la non-followeri; 10 cereri pe keyword; 3 postări fixate

**Metrica lunii:** un Reel în valul 2+ de distribuție (majoritate non-followeri) SAU un format validat cu watch time peste media 2026 (8,5s)

## 5. Audit de setup (7 puncte)

| Punct | Status | Reparație |
|---|---|---|
| professional_account | ✅ PASS | — |
| upload_highest_quality | ✅ PASS | — |
| search_engine_indexing | ❌ FAIL | Settings and activity → Media quality / indexare: bifează „Allow public photos and videos to appear in search engine results” (Google indexează conturile profesionale din 10.07.2025). |
| account_status | ✅ PASS | — |
| translations | ⚠️ UNKNOWN | Settings → Language and translations: verifică traducerile; dubbing Meta AI disponibil de la 1.000 de followeri. |
| bio_seo | ❌ FAIL | Rescrie bio-ul: „Zâmbetul Mic | Dentist pentru copii 0–12 ani” + ce primește părintele + CTA „Scrie GHID pentru lista de 7 zile”. |
| niche_clarity | ✅ PASS | — |

## 6. Warnings de livrare (goluri de research + proveniență)

- audience.voC_quotes este gol → frazele de durere din captions sunt DEMO, marcate NEVOIE_RESEARCH pe fiecare livrabil. Înlocuiește-le cu citate reale (skill modula-research) înainte de filmare.
- Cifrele de țintă din plan (sends 1/100–200 views, saves 1/50–100, comentarii 15–30/1k) sunt „heuristica kitului"; pragurile de skip rate (~40%), share rate (0,5–2%), save rate (1–3%) și completion (<15s: ≥70%) sunt T3 — practician 2026 (knowledge/corpus-2026.md). Livrează-le marcate, nu ca benchmark oficial.
- account_setup: 2 FAIL (search_engine_indexing, bio_seo) — se repară înainte de scalare; account_status e PASS, deci nu există blocant P0.
- ManyChat nu e activ: keyword-urile se adună manual până la activare; nimic din CTA nu are voie să promită altceva decât livrarea reală din DM.
- Compliance health respectat: zero promisiuni de rezultat medical, fără diagnostic la distanță, fără testimonial de pacient fără acord scris.
- Orele de publicare și durata sunt ținte de lucru — se recalibrează din Insights după primele 9 postări.

## 7. Ce a verificat mecanismul (nu ochiul)

- `tools/validate_output.py output.json` → **VALID** (schemă JSON completă + regulile dure: 5-8-5 pe hook, text-on-screen ≤3 cuvinte, caption ≤125 caractere vizibile, ≤5 hashtag-uri, test mut marcat, CTA cu schimb de valoare, audit prezent pe fiecare livrabil, verdict consistent cu scorul).
- `audita.py` → **0 probleme**: 4 straturi de hook pe fiecare Reel, 3 structuri de hook distincte, marker de Attention Reset pe fiecare linie de script cu interval maxim 3–4s, keyword în prima linie, CTA stratificat, carusel cu slide de referință, plan cu metrice măsurabile, zero promisiuni de rezultat (compliance health).

> **Limita de onestitate:** auditul de 0–100 a fost făcut de același model, aplicând
> criteriile scrise din `agents/viral-auditor.md` (nu de un auditor independent).
> Verificarea mecanică (`validate_output.py` + `audita.py`) e independentă de autor,
> dar acoperă doar regulile automatizabile — nu originalitatea, tonul sau VoC-ul real.

