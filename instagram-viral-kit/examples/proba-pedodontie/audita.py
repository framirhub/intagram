#!/usr/bin/env python3
"""Audit suplimentar pentru runul de probă — verifică reguli din ghid pe care
`tools/validate_output.py` NU le acoperă mecanic:

  - cele 4 straturi de hook prezente și ne-goale (ghid §5.1)
  - structuri de hook DISTINCTE într-un pachet de 3 (ghid §6: „minimum 3
    structuri diferite”)
  - marker de Attention Reset pe fiecare linie de script (convenția din
    examples/exemplu-reel.md) + cel mai mare interval dintre reset-uri
  - keyword-ul exact în prima linie a caption-ului (discoverability, ghid §4)
  - CTA stratificat (≥2 straturi) și hashtag-uri 3–5, fără generice (ghid §4.3)
  - carusel: slide 1 = hook (≤15 cuvinte), slide de referință marcat, ≤25
    cuvinte/slide (ghid §8.2)
  - plan: 4 săptămâni, fiecare cu metrică măsurabilă (ghid §12)
  - compliance health: zero promisiuni de rezultat (ghid §10.4)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "output.json").read_text(encoding="utf-8"))

ok, problems = [], []
GENERIC = {"viral", "fyp", "foryou", "explore", "love", "reels"}
CLAIM_PATTERNS = [r"garantat", r"garanteaz", r"vindec", r"fără\s+durere", r"nu\s+mai\s+ai\s+nevoie"]

KEYWORD = "dentist pentru copii"

# --- 1. Reels: straturi, structuri, script, caption ---
structures, hook_layers_ok = [], True
for r in data["reels"]:
    rid = r["id"]
    structures.append(r["structure"])
    for layer in ("visual", "verbal", "text_on_screen", "audio"):
        if not r["hook"].get(layer):
            hook_layers_ok = False
            problems.append(f"{rid}: stratul de hook „{layer}” lipsește sau e gol")
    lines = [l for l in r["script"].splitlines() if l.strip()]
    without_reset = [l for l in lines if "[reset:" not in l]
    if without_reset:
        problems.append(f"{rid}: {len(without_reset)} linie/linii de script fără marker [reset:]")
    stamps = re.findall(r"(\d+):(\d{2})–(\d+):(\d{2})", r["script"])
    gaps = [int(a1) * 60 + int(a2) - (int(b1) * 60 + int(b2)) for b1, b2, a1, a2 in
            [(m[0], m[1], m[2], m[3]) for m in stamps]]
    max_gap = max(gaps) if gaps else 0
    if max_gap > 4:
        problems.append(f"{rid}: interval de {max_gap}s fără Attention Reset (limita din ghid §5.1 e 4s)")
    ok.append(f"{rid}: {r['hook']['verbal_word_count']} cuvinte verbale, {r['hook']['text_on_screen']!r} pe ecran, "
              f"{len(lines)} linii de script, toate cu [reset:], interval max {max_gap}s, "
              f"hook_line {r['caption']['visible_char_count']} caractere")
    cap = r["caption"]
    if KEYWORD not in cap["hook_line"].lower():
        problems.append(f"{rid}: keyword-ul „{KEYWORD}” nu apare în prima linie a caption-ului")
    layers = (cap.get("cta") or {}).get("layers") or []
    if len(layers) < 2:
        problems.append(f"{rid}: CTA are {len(layers)} straturi (minim 2)")
    tags = cap.get("hashtags") or []
    if not (3 <= len(tags) <= 5):
        problems.append(f"{rid}: {len(tags)} hashtag-uri (țintă 3–5)")
    bad = [t for t in tags if t.lstrip("#").lower() in GENERIC]
    if bad:
        problems.append(f"{rid}: hashtag-uri generice {bad}")

if len(set(structures)) < 3:
    problems.append(f"Structuri de hook insuficiente: {structures} (minim 3 diferite)")
ok.append(f"Structuri de hook distincte: {structures} ({len(set(structures))} diferite)")
ok.append(f"Straturi de hook complete pe toate Reels: {hook_layers_ok}")

# --- 2. Carusel ---
for p in data["posts"]:
    if p["format"] != "carousel":
        continue
    slides = p["slides"]
    ok.append(f"{p['id']}: {len(slides)} slide-uri, slide de referință: "
              f"{[s['position'] for s in slides if s.get('is_reference_slide')]}")
    if len(slides) > 20:
        problems.append(f"{p['id']}: {len(slides)} slide-uri > 20")
    if len(slides[0]["text"].split()) > 15:
        problems.append(f"{p['id']}: slide 1 are {len(slides[0]['text'].split())} cuvinte (>15)")
    heavy = [s["position"] for s in slides if len(s["text"].split()) > 25]
    if heavy:
        problems.append(f"{p['id']}: slide-uri peste 25 de cuvinte: {heavy}")
    if not any(s.get("is_reference_slide") for s in slides):
        problems.append(f"{p['id']}: lipsește slide-ul de referință (motorul de saves)")
    if KEYWORD not in p["caption"]["hook_line"].lower():
        problems.append(f"{p['id']}: keyword-ul nu apare în prima linie a caption-ului")
    ok.append(f"{p['id']}: hook_line {p['caption']['visible_char_count']} caractere, "
              f"{len(p['caption']['hashtags'])} hashtag-uri, open loop: "
              f"{'da' if p.get('open_loop') else 'nu'}")

# --- 3. Plan ---
weeks = data["growth_plan"]["weeks"]
ok.append(f"Plan: {len(weeks)} săptămâni, teme: {[w['theme'] for w in weeks]}")
if len(weeks) != 4:
    problems.append(f"Plan: {len(weeks)} săptămâni (kitul cere 4)")
for w in weeks:
    if not re.search(r"\d", w["success_metric"]):
        problems.append(f"Săptămâna {w['week']}: metrica de succes nu conține nicio cifră măsurabilă")
ok.append(f"Metrice măsurabile cu cifre: {sum(1 for w in weeks if re.search(r'[0-9]', w['success_metric']))}/4")

# --- 4. Compliance health ---
blob = json.dumps(data, ensure_ascii=False).lower()
hits = [pat for pat in CLAIM_PATTERNS if re.search(pat, blob)]
if hits:
    problems.append(f"Compliance: tipare de promisiune de rezultat găsite — {hits}")
else:
    ok.append("Compliance health: zero promisiuni de rezultat / vindecare / „fără durere”")

# --- 5. Setup ---
fails = [s["item"] for s in data["account_setup"] if s["status"] == "FAIL"]
blockers = [s["item"] for s in data["account_setup"] if s.get("is_blocker")]
ok.append(f"Setup: FAIL = {fails}; blocanți P0 = {blockers or 'niciunul'}")
if blockers:
    problems.append(f"Setup: blocant P0 prezent ({blockers})")

print("=== VERIFICĂRI TRECUTE ===")
for line in ok:
    print("  ✓", line)
print("\n=== PROBLEME ===")
print("  niciuna" if not problems else "\n".join(f"  ✗ {p}" for p in problems))
print(f"\nREZULTAT: {'CURAT (0 probleme)' if not problems else str(len(problems)) + ' probleme'}")
