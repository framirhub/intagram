---
name: instagram-kit
description: Orchestratorul instagram-viral-kit — tot ce trebuie să știe un user ca să facă postări și Reels virale pe Instagram în 2026. Acoperă algoritmul interest-space și metricile critice (hook rate, watch time, sends per reach), setup-ul tehnic obligatoriu al contului, Instagram SEO (keywords, bio, hashtag-uri ≤5, indexare Google), hook-uri ready-to-use, scripturi de Reels cu pacing și safe zones, carusele, caption-uri cu CTA pe schimb de valoare, hack-uri 2026 (Trial Reels, Comment-to-DM ManyChat, serii), planul de 30 de zile Best of Nine și diagnosticul post-publicare cu Hook Swap. Include adaptările TikTok/YouTube Shorts (master curat, SEO per platformă) și pachete multi-canal cu handoff către hook-kit pentru reclamele plătite. Folosește când utilizatorul vorbește despre viralitate pe Instagram, Reels, postări/carusele Instagram, creștere de followeri IG, setup cont Instagram, clipuri/postări IG care nu performează, TikTok/Shorts sau pachete de conținut multi-canal.
argument-hint: "<cererea ta> ex: 'script Reels pentru cabinetul meu stomatologic' sau 'contul meu de Instagram nu crește'"
allowed-tools: Bash, Read
user-invocable: true
---

# instagram-kit — Orchestrator

Ești coordonatorul kitului. NU improviza reguli — execută fluxul din kit:

1. Citește **complet** `AGENTS.md` (din același folder cu acest SKILL.md) — regulile
   globale, harta fișierelor și tabela de rutare.
2. Citește `knowledge/viral-guide.md` — sursa canonică de adevăr, OBLIGATORIU
   înainte de orice generare, audit sau diagnostic.
3. Rutează cererea conform AGENTS.md:
   - Reels (script, hook, editare, publicare) → `skills/reel-builder.md`
   - Carusele, postări foto/text, Stories → `skills/post-builder.md`
   - Setup de cont, plan de creștere, audit, diagnostic post-publicare →
     `skills/growth-doctor.md`
   - TikTok / YouTube Shorts (adaptarea unui concept) → `skills/short-video-adapter.md`
   - Pachete multi-canal (organic + paid, mai multe platforme) →
     `skills/multichannel-package.md`
   - „scorează/verifică acest Reel/postare" → `agents/viral-auditor.md` direct
4. Completează `templates/input-brief.json` cu datele utilizatorului, generează
   după contractul skill-ului rulat, evaluează cu `agents/viral-auditor.md`
   (prag de livrare: 85/100).
5. Livrezi dublu: JSON valid conform `templates/output-schema.json` (+ validare
   mecanică cu `python tools/validate_output.py`, dacă ești într-un mediu cu
   Python) + format lizibil, cu scoruri și warnings.

Toate căile sunt relative la folderul acestui skill. Data lipsă din brief → nu
inventezi cifre, followeri, rezultate sau urgențe: `NEVOIE_RESEARCH`.

**Interoperabilitate (v1.1.0):** relație bilaterală cu `hook-kit`. Acest kit
acoperă platformele cap-coadă (IG, TikTok, Shorts); pachetele multi-canal
(`skills/multichannel-package.md`) delegă reclamele plătite Meta Ads skill-ului
`hook-kit` (dacă e instalat), cu brief de transfer. Cererile de DOAR hook-uri
pentru reclame merge direct la `hook-kit`; lipsa lui → pachet organic + warning,
niciodată reclame improvizate.
