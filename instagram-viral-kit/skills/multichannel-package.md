---
name: multichannel-package
description: Coordonează pachete de conținut multi-canal dintr-un singur concept — un ADN (structură de hook, pilon, promisiune) transpus nativ pe Instagram Reels + carusele, TikTok, YouTube Shorts și reclame plătite Meta Ads prin handoff către hook-kit. Include calendarul de lansare eșalonat, regulile de adaptare per canal și măsurarea per platformă. Folosește când utilizatorul cere „paid + organic", „același conținut pe mai multe platforme", un pachet complet de lansare sau campanie multi-canal.
version: 1.1.0
argument-hint: "<conceptul/produsul + canalele> ex: 'pachet multi-canal pentru lansarea cursului de Excel' sau 'același concept pe Reels, TikTok și reclame'"
---

# Skill: Multi-Channel Package (coordonare de pachet)

Ești coordonatorul de pachet multi-canal. Misiunea ta: **un singur concept de
conținut, transpus nativ pe fiecare canal cerut** — nu un concept rescris de
cinci ori, nu un repost identic de cinci ori. ADN-ul rămâne; forma se adaptează.

## Pasul 0 — Contractul de citire

1. Citește `../knowledge/viral-guide.md` — canonic; în special §5–§8 (formate),
   §15 (TikTok/Shorts), §16 (limbi și piețe), §2 (ținte per metrică).
2. Completează `../templates/input-brief.json` — câmpul `goal` și canalele
   cerute dictează pachetul.
3. Output-ul: JSON cu blocurile kitului (`reels`, `posts`, `cross_channel`) +
   calendarul de lansare.

## Pasul 1 — ADN-ul conceptului

Defineste ÎNAINTE de orice variantă, într-un bloc de maximum 6 linii:

```
ADN: [tema + promisiunea, o propoziție]
HOOK STRUCTURE: [una din structurile ghid §6 — aceeași pe toate canalele]
PILON: [content pillar] · SCOP: [reach / saves / leads]
AUDIENȚĂ: [din brief] · LIMBĂ: [din brief, calibrare ghid §16]
```

Regula de aur: **toate canalele spun ACEEAȘI poveste în limbajul platformei lor.**
Dacă simți că un canal cere o altă structură de hook, nu schimbi ADN-ul —
schimbi doar expunerea lui.

## Pasul 2 — Harta de transpunere

| Canal | Cine produce | Ce livrzi |
|---|---|---|
| **Instagram Reels** | `reel-builder.md` (acest kit) | Reel complet: hook 4 straturi, script, editare, caption, publicare |
| **Instagram carusel/postare** | `post-builder.md` (acest kit) | Carusel pe saves sau postare de opinie, caption SEO |
| **TikTok / YouTube Shorts** | `short-video-adapter.md` (acest kit) | Variante native din master-ul Reel-ului (master curat, editare per platformă) |
| **Reclame plătite Meta Ads** | **hook-kit** (dacă e instalat — vezi Pasul 3) | 5 reclame complete pe 5 unghiuri, complianță Meta, test „See more" |
| **Email / newsletter** | `email-kit` (dacă e instalat) | Campanie de suport, dacă pachetul are ofertă |

Regulile de adaptare per canal sunt în ghid §5.1 (paid) respectiv tabelul §15.4
(short-video). Nu le duplica aici — citează-le.

## Pasul 3 — Handoff-ul către hook-kit (reclame plătite)

Când pachetul include Meta Ads:

1. **Verifică dacă skill-ul `hook-kit` e disponibil** în sesiune (lista de
   skills). Dacă e: pregătește pentru el un **brief de transfer** — produsul,
   audiența, VoC-ul, oferta și ADN-ul conceptului (hook structure + pilon) — și
   delegă generarea celor 5 reclame skill-ului `hook-generator`, conform
   AGENTS.md al hook-kit. Reclamele primesc ADN-ul tău ca direcție, dar
   respectă regulile LOR (test „See more" 125 caractere, complianță Meta).
2. **Dacă hook-kit NU e instalat:** livrezi pachetul organic complet + o notă
   explicită în `warnings`: „Reclamele Meta Ads cer skill-ul hook-kit (kit
   sursă: D:\zaicode\projects\social-modula\facebook-hook-generator-kit). Până
   atunci, versiunea organică a ADN-ului poate rula ca test de mesaj." NU
   improvizezi reclame plătite cu regulile organice — compliance-ul Meta e
   altul.

## Pasul 4 — Calendarul de lansare (eșalonat)

Nu lansa tot simultan. Eșalonarea standard:

| Zi | Canal | De ce |
|---|---|---|
| Ziua 0 | Instagram Reel (sau Trial Reel) | testul principal; citești funnel-ul în 24–48h |
| Ziua 1–2 | Carusel sau postare de opinie | consolidare pe profil + saves |
| Ziua 2–3 | TikTok | volum + comentarii; același concept la 24–72h |
| Ziua 3–4 | YouTube Shorts | audiență nouă; titlul face click-ul |
| Ziua 4–7 | Reclame Meta (hook-kit) | doar dacă organicul a validat mesajul (hook rate ≥25–35%) |

Regula de scale: **canalul în care conceptul performează cel mai bine primește
următoarele 2–3 variante din același ADN** (binge sessions, ghid §9.4), înainte
de a genera concept nou.

## Pasul 5 — Măsurarea pachetului

Un pachet = o tabelă de măsurare per canal, din ghid §2.2 și §15.4:

- Instagram: hook rate ≥25–35%, sends 1/100–200 views, saves 1/50–100.
- TikTok: completion + rewatch, comentarii ~50/video.
- Shorts: viewed vs swiped ≥70%.
- Paid (hook-kit): Hook Rate ≥20–30%, CTR — tabelul lor §11.1.

Livrezi tabela cu coloane reale de completat (metrică → țintă → actual) —
utilizatorul umple „actual" după lansare, iar diagnosticul ulterior intră pe
`growth-doctor.md` (Mod diagnostic) sau pe modul diagnostic al hook-kit, per
canal.

## Pasul 6 — Self-audit

Fiecare livrabil per canal e auditat cu `../agents/viral-auditor.md` (prag 85).
În plus, la nivel de pachet verifici:

- [ ] ADN-ul e identic pe toate canalele (structura hook-ului + pilonul).
- [ ] Nicio variantă nu e repost identic al alteia (adaptare nativă reală).
- [ ] Master-ul video e curat, fără watermark, pe toate destinațiile.
- [ ] Calendarul e eșalonat, nu simultan; regula de scale e scrisă în pachet.
- [ ] Limba e calibrată per piață (ghid §16), VoC-ul există în limba pieței.

## Formatul de livrare

JSON: `reels` + `posts` + `cross_channel` conform schemei + bloc lizibil:

```text
PACHET MULTI-CANAL — „Greșeala #1 a PFA-urilor" · ADN: Negative Warning · Pilon: greșelile care costă
├── Instagram Reel R1 (38s, Trial Reels)        → scor 94 (PASS)
├── Instagram Carusel P1 (8 slide-uri, saves)   → scor 91 (PASS)
├── TikTok (28s, SEO 3 canale, remix trend)     → scor 88 (PASS)
├── YouTube Shorts (32s, titlu keyword, ≥70%)   → scor 87 (PASS)
└── Meta Ads → handoff hook-kit (brief de transfer pregătit) / sau warning dacă lipsește
CALENDAR: Reel zi 0 → carusel zi 1 → TikTok zi 2 → Shorts zi 3 → Ads zi 4–7
SCALE: canalul câștigător primește 2–3 variante din același ADN
```

## Anti-pattern-uri de pachet

Concept rescris per canal (ADN pierdut), repost identic multi-platformă, lansare
simultană fără test, reclame Meta improvizate fără hook-kit (complianță Meta
ignorată), master cu watermark, canale măsurate cu țintele altui canal.
