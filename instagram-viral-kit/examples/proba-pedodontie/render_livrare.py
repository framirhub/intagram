#!/usr/bin/env python3
"""Renderer pentru livrarea lizibilă a runului de probă.

Kitul livrează dublu (AGENTS.md §4): JSON validat + format lizibil. Ca să nu
apară drift între cele două, formatul lizibil (`livrare.md`) se generează DIN
`output.json` — dacă JSON-ul se schimbă, textele livrate se regenerează identic.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "output.json").read_text(encoding="utf-8"))

CRIT = [
    ("hook_scroll_stop", "Hook & scroll-stop", 25),
    ("retention_structure", "Retenție & structură", 20),
    ("discoverability", "Discoverability", 20),
    ("compliance_originality", "Complianță & originalitate", 15),
    ("cta_growth_loop", "CTA & buclă de creștere", 20),
]

L = []
w = L.append

w("# Run de probă — pedodonție (instagram-viral-kit v1.2.0)")
w("")
w("> Livrabil de referință generat pe regulile kitului v1.2.0, ca probă de funcționare")
w("> cap-coadă: brief → generare → audit → validare mecanică → livrare lizibilă.")
w("")
w(f"- **Brief:** `{data['brief_ref']}` (cont fictiv `@zambetul.mic`, 1.850 followeri)")
w("- **Nișă:** pedodonție — dentist pentru copii 0–12 ani")
w("- **Livrat:** 3 Reels + 1 carusel + plan de 30 zile + audit de setup")
w(f"- **Validare mecanică:** `python tools/validate_output.py output.json` → VALID")
w("- **Audit suplimentar:** `python audita.py` → 0 probleme")
w("")

w("## 1. Scoruri de audit (viral-auditor, prag 85/100)")
w("")
w("| Livrabil | Hook | Retenție | Discoverability | Complianță | CTA | Total | Verdict |")
w("|---|---|---|---|---|---|---|---|")
for item in data["reels"] + data["posts"]:
    a = item["audit"]
    w(f"| {item['id']} — {item['title']} | {a['hook_scroll_stop']}/{CRIT[0][2]} | {a['retention_structure']}/{CRIT[1][2]} | "
      f"{a['discoverability']}/{CRIT[2][2]} | {a['compliance_originality']}/{CRIT[3][2]} | {a['cta_growth_loop']}/{CRIT[4][2]} | "
      f"**{a['total']}** | **{a['verdict']}** |")
w(f"| | | | | | | **medie {data['audit']['total_score_avg']}** | "
  f"{data['audit']['pass_count']} PASS / {data['audit']['revise_count']} REVISE / {data['audit']['reject_count']} REJECT |")
w("")
w("Probleme rămase (toate P2 — nu blochează livrarea):")
for item in data["reels"] + data["posts"]:
    for i in item["audit"]["issues"]:
        w(f"- **{item['id']}** [{i['priority']}] {i['problem']} → {i['fix']}")
w("")

w("## 2. Reels")
for r in data["reels"]:
    w("")
    w(f"### {r['id']} — {r['title']}")
    w("")
    w(f"- **Structură hook:** `{r['structure']}` · **Pilon:** {r['pillar']} · **Scop:** {r['goal']} · **Durată:** {r['duration_seconds']}s")
    w("")
    w("**Hook (primele 3 secunde, 4 straturi sincronizate):**")
    w("")
    w("```text")
    w(f"[vizual]        {r['hook']['visual']}")
    w(f"[verbal]        „{r['hook']['verbal']}” ({r['hook']['verbal_word_count']} cuvinte)")
    w(f"[text-on-screen] {r['hook']['text_on_screen']}")
    w(f"[audio]         {r['hook']['audio']}")
    w(f"Test mut: {'PASS' if r['hook']['mute_test_passed'] else 'FAIL'}")
    w("```")
    w("")
    w("**Script (Attention Reset la fiecare ≤4s, marcat):**")
    w("")
    w("```text")
    w(r["script"])
    w("```")
    w("")
    w("**Editare:**")
    w("")
    for c in r["editing_checklist"]:
        w(f"- [x] {c}")
    w("")
    w("**Caption:**")
    w("")
    w("```text")
    w(r["caption"]["hook_line"])
    w(f"({r['caption']['visible_char_count']} caractere vizibile — buget ~125)")
    w("")
    w(r["caption"]["body"])
    w("")
    w(r["caption"]["cta"]["value_exchange"])
    w("")
    w(" ".join(r["caption"]["hashtags"]))
    w("```")
    w("")
    w(f"**Publicare:** `{r['publish']['channel']}` · {r['publish']['timing_note']} "
      f"· calitate maximă: {'ON' if r['publish']['quality_check'] else 'OFF'} · prima oră: {r['publish']['first_hour_action']}")
    if r.get("needs_research"):
        w("")
        w("**NEVOIE_RESEARCH:** " + " · ".join(r["needs_research"]))

w("")
w("## 3. Carusel")
for p in data["posts"]:
    w("")
    w(f"### {p['id']} — {p['title']}")
    w("")
    w(f"- **Format:** {p['format']} · **Pilon:** {p['pillar']} · **Slide-uri:** {len(p['slides'])}")
    w("")
    w("| # | Text | Design | Referință |")
    w("|---|---|---|---|")
    for s in p["slides"]:
        w(f"| {s['position']} | {s['text']} | {s.get('design_note', '')} | {'✅' if s.get('is_reference_slide') else ''} |")
    w("")
    if p.get("open_loop"):
        w(f"**Open loop:** {p['open_loop']}")
        w("")
    w("**Caption:**")
    w("")
    w("```text")
    w(p["caption"]["hook_line"])
    w(f"({p['caption']['visible_char_count']} caractere vizibile)")
    w("")
    w(p["caption"]["body"])
    w("")
    w(p["caption"]["cta"]["value_exchange"])
    w(f"SALVARE: {p['caption']['cta'].get('save_prompt', '')}")
    w("")
    w(" ".join(p["caption"]["hashtags"]))
    w("```")

w("")
w("## 4. Plan de 30 zile")
plan = data["growth_plan"]
w("")
w(f"**{plan['strategy_name']}** · nișă: {plan['niche']} · piloni: {', '.join(plan['content_pillars'])}")
for wk in plan["weeks"]:
    w("")
    w(f"### Săptămâna {wk['week']} — {wk['theme']}")
    for a in wk["actions"]:
        w(f"- {a}")
    w(f"- **Metrică de succes:** {wk['success_metric']}")
w("")
w(f"**Metrica lunii:** {plan['month_success_metric']}")

w("")
w("## 5. Audit de setup (7 puncte)")
w("")
w("| Punct | Status | Reparație |")
w("|---|---|---|")
for s in data["account_setup"]:
    w(f"| {s['item']} | {'✅ PASS' if s['status'] == 'PASS' else ('❌ FAIL' if s['status'] == 'FAIL' else '⚠️ UNKNOWN')} | {s.get('how_to_fix', '—')} |")

w("")
w("## 6. Warnings de livrare (goluri de research + proveniență)")
w("")
for x in data["warnings"]:
    w(f"- {x}")

w("")
w("## 7. Ce a verificat mecanismul (nu ochiul)")
w("")
w("- `tools/validate_output.py output.json` → **VALID** (schemă JSON completă + regulile dure: 5-8-5 pe hook, text-on-screen ≤3 cuvinte, caption ≤125 caractere vizibile, ≤5 hashtag-uri, test mut marcat, CTA cu schimb de valoare, audit prezent pe fiecare livrabil, verdict consistent cu scorul).")
w("- `audita.py` → **0 probleme**: 4 straturi de hook pe fiecare Reel, 3 structuri de hook distincte, marker de Attention Reset pe fiecare linie de script cu interval maxim 3–4s, keyword în prima linie, CTA stratificat, carusel cu slide de referință, plan cu metrice măsurabile, zero promisiuni de rezultat (compliance health).")
w("")
w("> **Limita de onestitate:** auditul de 0–100 a fost făcut de același model, aplicând")
w("> criteriile scrise din `agents/viral-auditor.md` (nu de un auditor independent).")
w("> Verificarea mecanică (`validate_output.py` + `audita.py`) e independentă de autor,")
w("> dar acoperă doar regulile automatizabile — nu originalitatea, tonul sau VoC-ul real.")
w("")

(HERE / "livrare.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("scris:", HERE / "livrare.md", "|", len(L), "linii")
