# Exemplu diagnostic — bucla post-publicare și Protocolul Hook Swap

> Run complet pe traseul cel mai folosit din kit: **ce faci când un Reel nu
> performează**. Caz real de lucru (cont fictiv `@zambetul.mic`, pedodonție —
> același cont ca în [`proba-pedodontie`](proba-pedodontie/livrare.md)), cu
> metricile la 48 de ore, diagnostic pe funnel, **o singură acțiune tactică** și
> pachetul de Hook Swap gata de filmat.
>
> Versiunea mecanică a acestui run (pentru validare automată) e fixtura
> [`proba-diagnostic/output.json`](proba-diagnostic/output.json); fixtura
> negativă care dovedește că regula chiar e verificată e
> [`negative-hook-swap.json`](proba-diagnostic/negative-hook-swap.json).
> Regulile citate: `knowledge/viral-guide.md` §2.1, §2.2, §11, §18.
>
> **Calibrare, nu copiere:** copiază ORDINEA de citire și structura hook-urilor,
> nu conținutul — cifrele de aici sunt de test.

## 1. Datele de intrare (Insights la 48h)

Reel-ul: „Frica de dentist se învață acasă, nu aici" (32s, hook
`negative_warning`), publicat **normal** (format considerat validat), marți 9:30.

| Metrică | Actual | Țintă (ghid §2.2) | Sursă țintă |
|---|---|---|---|
| Views | 4.180 | — | — |
| Hook rate (>3s) | **18%** | ≥25–35% | benchmark Meta Ads (proxy) |
| Skip rate | **52%** | peste ~40% = intro de reparat | T3 (corpus 2026) |
| Watch time mediu | 7,2s | >8,5s | Metricool 2026 (T2) |
| Completion (clip 32s) | 41% | ≥50% pentru 30–60s | heuristica kitului |
| Sends | 1 la 620 views | 1 la 100–200 | heuristica kitului |
| Saves | 1 la 430 views | 1 la 50–100 | heuristica kitului |
| Comentarii | 9 la 1k views | 15–30+ | heuristica kitului |
| Followeri / non-followeri | 71% / 29% | majoritate non-followeri | distribuție activă (§2.3) |

## 2. Ordinea de diagnostic (regula care contează)

Funnel-ul (§2.1) se citește **de la prima etapă spre ultima** — reparați prima
etapă stricată, nu ultima:

```
Impresii → 3s (hook rate / skip rate) → retenție → completare
        → sends · saves · comentarii → follows → views noi
```

Aici prima etapă e ruptă: **52% abandonează înainte de secunda 3**. Consecințe:

- Sends 1/620 și saves 1/430 **nu sunt diagnostice** — sunt simptome în aval. Dacă
  reparăm CTA-ul de sends și lăsăm hook-ul rupt, nu se schimbă nimic.
- 71% views de la followeri arată că valul nu s-a extins dincolo de baza
  existentă: distribuția a murit în etapa de test, exact din cauza skip rate-ului.
- Vestea bună, citită tot din funnel: watch time 7,2s și completion 41% pe un clip
  de 32s spun că **corpul Reel-ului ține** pentru cei care rămân. Corpul nu se
  atinge.

## 3. Tabelul de diagnostic livrat

| Metrică sub țintă | Diagnostic | Acțiune tactică |
|---|---|---|
| **Hook rate 18% / skip rate 52%** | hook-ul nu oprește scroll-ul; prima etapă e stricată | **Hook Swap** — vezi §4 |
| Sends 1/620 | lipsă de valoare de trimis — urmare a reach-ului mic | **nu se repară acum** (se reevaluează la 72h după Hook Swap) |
| Saves 1/430 | conținut consumabil, nu de referință | reprogramat: `reference_slide` pe următoarea postare de tip listă |
| Comentarii 9/1k | fapt rece în loc de opinie | reprogramat: întrebare de opinie în caption (nu în acest Reel) |
| 71% views de la followeri | distribuția nu s-a extins | consecință a hook rate-ului, nu cauză separată |

**Regula de disciplină:** un singur diagnostic, o singură acțiune. Trei reparații
simultane = nu mai știi ce a produs diferența.

## 4. Pachetul de Hook Swap (3 hook-uri, structuri diferite)

Se schimbă **doar primele 3 secunde**. Corpul, caption-ul, hashtag-urile, CTA-ul
și audio-ul rămân identice — altfel nu compari hook-uri, compari două Reel-uri.
Fiecare hook: cele 4 straturi sincronizate + test mut + Regula 5-8-5.

### H1 — Contrarian

```text
[structură]      Contrarian (opinie împotriva consensului)
[vizual]         0–1s mid-motion: mâna toarnă apă peste un pahar cu suc
[verbal]         „Cariile la copii nu apar de la dulciuri.”            (8 cuvinte)
[text-on-screen] „NU DULCIURILE"                                       (2 cuvinte)
[audio]          tăcere 0,5s, apoi pop SFX pe ultimul cuvânt
[test mut]       PASS — paharul + textul transmit contrariul fără sunet
[plasare text]   centrul 3:4, text mare galben/negru
```

### H2 — Industry Shock

```text
[structură]      Industry Shock (cifră care contrazice nișa)
[vizual]         0–1s: periuța pusă greșit pe masă, mâna o întoarce
[verbal]         „Nouă din zece părinți greșesc periajul copilului.”    (7 cuvinte)
[text-on-screen] „9 DIN 10"                                             (3 cuvinte)
[audio]          sunet real de periuță pe masă (fără muzică)
[test mut]       PASS — cifra pe ecran e hook-ul; gestul o întărește
```

### H3 — Audience Callout

```text
[structură]      Audience Callout (calificare directă a avatarului)
[vizual]         0–1s: cadru apropiat pe o periuță mușcată de copil
[verbal]         „Dacă copilul tău mușcă periuța, ascultă asta.”       (7 cuvinte)
[text-on-screen] „MUȘCĂ PERIUȚA?"                                      (2 cuvinte)
[audio]          ambianță de baie, fără muzică
[test mut]       PASS — obiectul (periuța mușcată) e hook-ul vizual
```

Cele trei acoperă structuri diferite (nu trei variante de formulare a aceleiași
idei) — cerința din ghid §6 și verificarea mecanică din `tools/validate_output.py`.

### Checklist de re-filmare (≈15 minute)

- [ ] Se filmează doar secunda 0–3 pentru fiecare variantă (restul clipului e deja filmat).
- [ ] Subtitlele primelor 3 secunde se rescriu cu textul nou (sincron cu verbalul).
- [ ] Textul nou rămâne în centrul 3:4 (nimic sub 350px jos / 250px dreapta).
- [ ] Export fără watermark, 1080×1920, 30fps.
- [ ] Caption, hashtag-uri și CTA-ul rămân EXACT cele vechi.

## 5. Protocolul de republicare (ghid §11)

1. **NU șterge clipul original.** Corpul e bun, doar ușa e greșită — iar ștergerea
   îți ia și datele de comparație.
2. Publici varianta cu hook nou **după 3 zile** (nu mai devreme: altfel
   cannibalizezi testul variantei originale).
3. Fiecare variantă de hook nou = un Reel separat (nu trei hook-uri în același
   clip), ca Insights-ul să le citească individual.
4. Prima oră: răspuns la fiecare comentariu; fără modificări de caption în primele
   24h (dwell time-ul și semnalele conținutului rămân curate).
5. **Citești rezultatul la 72h, nu la 30 de minute** (ghid §1.2: ~65% din views-urile
   unui Reel se adună în primele 72h).

## 6. Ramura alternativă (dacă skip rate era ok)

Diagnosticul depinde de ce etapă e ruptă — aceeași postare, alt set de date:

| Dacă metrica asta era cea slabă | Nu hook-ul e problema | Acțiunea corectă |
|---|---|---|
| Sends sub țintă, hook rate ok | conținut fără valoare de identitate | `cta_identity`: „trimite-i-l părintelui care amână programarea” |
| Saves sub țintă, retenție ok | material consumabil | `reference_slide`: checklist / listă de salvat |
| Comentarii sub țintă | fapt, nu opinie | tehnica găurii / întrebare polarizantă moderată |
| Views 90%+ de la followeri, restul ok | nisa neclară sau conținut generic | `fix_niche` + verificarea originalității |
| Totul sub țintă, inclusiv reach | nu e conținutul, e contul | `run_setup_audit` (Account Status = P0) |

## 7. Ce urmărești după Hook Swap (criteriul de succes)

| Rezultat la 72h | Interpretare | Următorul pas |
|---|---|---|
| Hook rate ≥25%, restul similar | ușa era greșită; corpul funcționează | scalezi formatul + hook-ul câștigător în serii |
| Hook rate tot <25%, dar retenție bună | problema nu e hook-ul, e promisiunea | rescrii deschiderea corpului (`rewrite_opening`) |
| Hook rate ok, sends încă 0 | conținut educativ fără valoare de identitate | `cta_identity` pe următoarea postare |
| Nicio schimbare, toate metricile moarte | problemă de cont, nu de conținut | `run_setup_audit` (ghid §3) |

**Verdictul se dă pe funnel, nu pe views.** 4.200 de views cu hook rate 18% e un
Reel eșuat pe care nimeni nu-l vede; 900 de views cu hook rate 32% și sends 1/180
e un format care merită repetat.

## 8. Fixtura mecanică (cum se testează acest traseu)

```bash
python tools/validate_output.py examples/proba-diagnostic/output.json        # exit 0 (VALID)
python tools/validate_output.py examples/proba-diagnostic/negative-hook-swap.json  # exit 1 (INVALID)
python tools/run_tests.py                                                   # toate fixturile
```

Ce verifică validatorul, dincolo de schemă (ghid §11): câmpurile obligatorii ale
unui diagnostic (`metric`, `actual`, `target`, `diagnosis`, `action`) și
**protocolul Hook Swap** — minimum 3 hook-uri noi, fiecare în bugetul 5-8-5.
Fixtura negativă (2 hook-uri, unul de 16 cuvinte, unul de 2) este respinsă cu
exact aceste motive, iar `tools/run_tests.py` cade dacă o fixtură negativă ajunge
să treacă — adică garda de regresie e testată în ambele direcții.
