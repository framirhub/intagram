#!/usr/bin/env python3
"""Validator mecanic pentru outputurile instagram-viral-kit.

Verifică:
  1. Schema JSON (dacă pachetul `jsonschema` e instalat — validare completă;
     altfel cadere pe verificările structurale de mai jos, care acoperă regulile
     dure ale kitului).
  2. Regulile dure din knowledge/viral-guide.md:
     - hook verbal: 5–8 cuvinte (Regula 5-8-5; 3–12 tolerat de schemă, 5–8 e ținta)
     - text-on-screen: ≤ 3 cuvinte / 30 caractere
     - caption hook_line: ≤ 125 caractere vizibile recomandat (150 limita dură)
     - hashtag-uri: max 5 (limita oficială din dec. 2025)
     - durată Reel: 5–180s (sweet spot 30–60 recomandat, avertisment la abatere)
     - cross_channel (TikTok/Shorts): master curat fără watermark (P0), base_id
       prezent, adaptări native listate, titlu YouTube obligatoriu pe Shorts
     - diagnostics (ghid §11): câmpurile obligatorii + protocolul Hook Swap
       (minimum 3 hook-uri noi, fiecare cu 5–8 cuvinte)
     - CTA cu schimb de valoare (nu doar 'dă follow')
     - verdict de audit consistent cu scorul (≥85 PASS, 70–84 REVISE, <70 REJECT)
     - audit obligatoriu pe fiecare livrabil (reel, post, cross_channel) —
       poarta 85/100 nu e opțională (AGENTS.md §4)

Folosire:
  python tools/validate_output.py output.json
  python tools/validate_output.py output.json --schema templates/output-schema.json

Exit 0 = valid, 1 = probleme (se listează).
"""
import argparse
import json
import sys
from pathlib import Path

FOLLOW_ONLY_PHRASES = ("da follow", "dă follow", "give me a follow", "follow me")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_validate(data, schema_path, errors, notes):
    try:
        import jsonschema  # type: ignore
    except ImportError:
        notes.append("pachetul 'jsonschema' nu e instalat — rulez doar verificările dure ale kitului (pip install jsonschema pentru validare completă).")
        return
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    for err in jsonschema.Draft7Validator(schema).iter_errors(data):
        where = ".".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"SCHEMA {where}: {err.message}")


def check_verdict(audit, rid, errors):
    if not audit:
        return
    total = audit.get("total", 0)
    verdict = audit.get("verdict")
    has_p0 = any(i.get("priority") == "P0" for i in audit.get("issues", []))
    expected = "REJECT" if (total < 70 or has_p0) else ("PASS" if total >= 85 else "REVISE")
    if verdict != expected:
        errors.append(f"{rid} AUDIT: verdict {verdict} cu scor {total} (P0={has_p0}) — expected {expected}.")


def check_caption(caption, rid, errors, notes):
    if not caption:
        errors.append(f"{rid} CAPTION: lipsește complet.")
        return
    hook_line = caption.get("hook_line", "")
    visible = caption.get("visible_char_count")
    real = len(hook_line)
    if visible is not None and abs(visible - real) > 2:
        errors.append(f"{rid} CAPTION: visible_char_count declarat ({visible}) nu se potrivește cu cel real ({real}).")
    if real > 150:
        errors.append(f"{rid} CAPTION hook_line: {real} caractere > 150 (limita dură; bugetul vizibil e ~125).")
    elif real > 125:
        notes.append(f"{rid} CAPTION hook_line: {real} caractere > 125 — mesajul-cheie poate fi tăiat de „...more”.")

    cta = caption.get("cta") or {}
    exchange = (cta.get("value_exchange") or "").lower()
    if not exchange:
        errors.append(f"{rid} CTA: lipsește value_exchange (schimb de valoare obligatoriu).")
    else:
        if any(p in exchange for p in FOLLOW_ONLY_PHRASES) and "comenteaz" not in exchange and "salveaz" not in exchange and "dm" not in exchange:
            errors.append(f"{rid} CTA: doar „follow” fără schimb de valoare (keyword DM / saves).")

    tags = caption.get("hashtags") or []
    if len(tags) > 5:
        errors.append(f"{rid} HASHTAGS: {len(tags)} — max oficial ~5 (dec. 2025).")
    generic = {"viral", "fyp", "foryou", "explore", "love", "reels"}
    bad = [t for t in tags if t.lstrip("#").lower() in generic]
    if bad:
        notes.append(f"{rid} HASHTAGS generice: {', '.join(bad)} — atrag zero relevanță.")


def check_reel(r, errors, notes):
    rid = r.get("id", "?")
    hook = r.get("hook") or {}
    verbal = hook.get("verbal", "")
    words = len(verbal.split())
    if verbal and not (5 <= words <= 8):
        # 5–8 e legea kitului (Regula 5-8-5); sub 5 sau 9–12 = avertisment dur
        if 3 <= words <= 12:
            notes.append(f"{rid} HOOK verbal: {words} cuvinte — ținta Regulii 5-8-5 e 5–8.")
        else:
            errors.append(f"{rid} HOOK verbal: {words} cuvinte — în afara oricărui buget (țintă 5–8).")
    declared = hook.get("verbal_word_count")
    if declared is not None and declared != words:
        errors.append(f"{rid} HOOK verbal_word_count declarat ({declared}) != real ({words}).")
    if not hook.get("mute_test_passed", False):
        errors.append(f"{rid} TEST MUT: nu e marcat ca trecut (vizual + text-on-screen trebuie să funcționeze fără sunet).")

    tos = hook.get("text_on_screen", "")
    if tos:
        if len(tos) > 30:
            errors.append(f"{rid} TEXT-ON-SCREEN: {len(tos)} caractere > 30 (1–3 cuvinte de impact).")
        if len(tos.split()) > 3:
            errors.append(f"{rid} TEXT-ON-SCREEN: {len(tos.split())} cuvinte > 3.")

    dur = r.get("duration_seconds")
    if dur is not None:
        if dur > 180:
            errors.append(f"{rid} DURATĂ: {dur}s > 180s (max oficial 3 minute).")
        elif dur > 90:
            notes.append(f"{rid} DURATĂ: {dur}s peste 90s — boost-ul plătit nu funcționează, retenția la audiențe noi scade.")

    check_caption(r.get("caption"), rid, errors, notes)
    if not r.get("script"):
        errors.append(f"{rid} SCRIPT: lipsește (script cu timecodes obligatoriu).")
    pub = r.get("publish") or {}
    if pub and pub.get("channel") not in ("trial_reels", "normal"):
        errors.append(f"{rid} PUBLISH: channel invalid (trial_reels | normal).")
    if not r.get("audit"):
        errors.append(f"{rid} AUDIT: lipsește — poarta de livrare (≥85/100) nu e opțională; rulează viral-auditor înainte de livrare.")
    check_verdict(r.get("audit"), rid, errors)


def check_post(p, errors, notes):
    pid = p.get("id", "?")
    fmt = p.get("format")
    if fmt == "carousel":
        slides = p.get("slides") or []
        if len(slides) < 2:
            errors.append(f"{pid} CARUSEL: sub 2 slide-uri.")
        if len(slides) > 20:
            errors.append(f"{pid} CARUSEL: {len(slides)} slide-uri > 20 (max în app).")
        if slides and "hook" not in (slides[0].get("text", "").lower() + " " + (slides[0].get("design_note") or "").lower()):
            s1_words = len(slides[0].get("text", "").split())
            if s1_words > 15:
                notes.append(f"{pid} SLIDE 1: {s1_words} cuvinte — slide 1 = hook, țintă 5–8 cuvinte de impact.")
        has_ref = any(s.get("is_reference_slide") for s in slides)
        if not has_ref:
            notes.append(f"{pid} CARUSEL: niciun slide de referință marcat — motorul de saves lipsește.")
    elif fmt in ("text_post", "photo"):
        if not p.get("content"):
            errors.append(f"{pid} {fmt}: lipsește 'content' (textul complet).")
        if not p.get("hook_types"):
            errors.append(f"{pid} {fmt}: lipesc hook_types (cele 6 tipuri de hook text, ghid §8.4).")
    elif fmt is None:
        errors.append(f"{pid} POST: lipsește 'format'.")
    check_caption(p.get("caption"), pid, errors, notes)
    if not p.get("audit"):
        errors.append(f"{pid} AUDIT: lipsește — poarta de livrare (≥85/100) nu e opțională; rulează viral-auditor înainte de livrare.")
    check_verdict(p.get("audit"), pid, errors)


def check_diagnostic(d, errors, notes):
    """Diagnosticul post-publicare (ghid §11) trebuie să fie acționabil: metrică,
    valoare reală, țintă, diagnostic și o acțiune din lista tactică. Pentru
    `hook_swap`, protocolul din ghid §11 cere minimum 3 hook-uri noi, fiecare
    respectând Regula 5-8-5 — altfel „Hook Swap" e doar o promisiune."""
    did = d.get("id") or d.get("metric") or "?"
    for field in ("metric", "actual", "target", "diagnosis", "action"):
        if not d.get(field):
            errors.append(f"{did} DIAGNOSTIC: lipsește câmpul obligatoriu '{field}'.")

    action = d.get("action")
    if action == "hook_swap":
        hooks = d.get("new_hooks") or []
        if len(hooks) < 3:
            errors.append(
                f"{did} HOOK SWAP: {len(hooks)} hook-uri noi — protocolul cere 3 (ghid §11), "
                "câte unul pe structuri diferite."
            )
        for h in hooks:
            words = len(h.split())
            if not (5 <= words <= 8):
                if 3 <= words <= 12:
                    notes.append(f"{did} HOOK SWAP: hook de {words} cuvinte — ținta Regulii 5-8-5 e 5–8.")
                else:
                    errors.append(f"{did} HOOK SWAP: hook de {words} cuvinte — în afara oricărui buget (țintă 5–8).")
    elif action == "none_within_target" and (d.get("new_hooks") or []):
        notes.append(f"{did} DIAGNOSTIC: acțiune 'none_within_target' cu hook-uri noi listate — verifică dacă nu e nevoie de Hook Swap.")


def check_cross_channel(c, errors, notes):
    cid = c.get("id", "?")
    platform = c.get("platform")
    if platform not in ("tiktok", "youtube_shorts"):
        errors.append(f"{cid} CROSS-CHANNEL: platform invalid (tiktok | youtube_shorts).")
    if not c.get("base_id"):
        errors.append(f"{cid} CROSS-CHANNEL: lipsește base_id (ADN-ul trebuie să vină dintr-un Reel de bază).")
    if not c.get("master_clean", False):
        errors.append(f"{cid} MASTER: nu e marcat curat — export fără watermark obligatoriu (P0).")
    if not c.get("adaptations"):
        errors.append(f"{cid} CROSS-CHANNEL: lipsesc adaptările native (repost identic = anti-pattern).")

    verbal = c.get("hook_verbal", "")
    words = len(verbal.split())
    if verbal and not (5 <= words <= 8):
        if 3 <= words <= 12:
            notes.append(f"{cid} HOOK verbal: {words} cuvinte — ținta Regulii 5-8-5 e 5–8.")
        else:
            errors.append(f"{cid} HOOK verbal: {words} cuvinte — în afara oricărui buget (țintă 5–8).")
    declared = c.get("hook_verbal_word_count")
    if declared is not None and declared != words:
        errors.append(f"{cid} HOOK verbal_word_count declarat ({declared}) != real ({words}).")

    tos = c.get("text_on_screen", "")
    if tos:
        if len(tos) > 30:
            errors.append(f"{cid} TEXT-ON-SCREEN: {len(tos)} caractere > 30.")
        if len(tos.split()) > 3:
            errors.append(f"{cid} TEXT-ON-SCREEN: {len(tos.split())} cuvinte > 3.")

    dur = c.get("duration_seconds")
    if dur is not None:
        if dur > 180:
            errors.append(f"{cid} DURATĂ: {dur}s > 180s.")
        elif platform == "tiktok" and dur > 60:
            notes.append(f"{cid} DURATĂ TikTok: {dur}s — top conținut rămâne 21–34s (ghid §15.2).")
        elif platform == "youtube_shorts" and dur > 60:
            notes.append(f"{cid} DURATĂ Shorts: {dur}s — scurtul câștigă distribuția; 3 min e max, nu țintă.")

    cap = c.get("caption_or_title") or {}
    if platform == "youtube_shorts" and not cap.get("youtube_title"):
        errors.append(f"{cid} SHORTS: lipsește youtube_title (titlul = hook-ul scris pe Shorts).")
    yt_title = cap.get("youtube_title", "")
    if yt_title and len(yt_title) > 60:
        notes.append(f"{cid} YOUTUBE TITLE: {len(yt_title)} caractere > 60 — titlul se poate tăia.")
    tags = cap.get("hashtags") or []
    if len(tags) > 5:
        errors.append(f"{cid} HASHTAGS: {len(tags)} — max ~5.")
    if not c.get("audit"):
        errors.append(f"{cid} AUDIT: lipsește — poarta de livrare (≥85/100) nu e opțională; rulează viral-auditor înainte de livrare.")
    check_verdict(c.get("audit"), cid, errors)


def main():
    # Windows: stdout default (cp1252 etc.) nu conține diacriticele RO — orice
    # print cu ș/ț/ă crape cu UnicodeEncodeError. Forțăm UTF-8, cu înlocuire
    # în loc de crash, pe ambele streamuri.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Validator output instagram-viral-kit")
    ap.add_argument("output", help="fișierul JSON de validat")
    ap.add_argument("--schema", default=str(Path(__file__).resolve().parent.parent / "templates" / "output-schema.json"))
    args = ap.parse_args()

    errors = []
    notes = []
    data = load(args.output)
    schema_validate(data, args.schema, errors, notes)

    if data.get("kit") != "instagram-viral-kit":
        errors.append("ROOT: câmpul 'kit' trebuie să fie 'instagram-viral-kit'.")

    for r in data.get("reels", []):
        check_reel(r, errors, notes)
    for p in data.get("posts", []):
        check_post(p, errors, notes)
    for c in data.get("cross_channel", []):
        check_cross_channel(c, errors, notes)
    for d in data.get("diagnostics", []):
        check_diagnostic(d, errors, notes)
    for s in data.get("account_setup", []):
        if s.get("status") == "FAIL" and s.get("is_blocker"):
            errors.append(f"SETUP {s.get('item')}: FAIL blocant P0 (Account Status) — nu livra plan de conținut peste fundație blocată.")
    plan = data.get("growth_plan")
    if plan is not None and not plan.get("weeks"):
        errors.append("GROWTH PLAN: lipsește lista 'weeks'.")
    if not any(k in data for k in ("reels", "posts", "account_setup", "growth_plan", "diagnostics", "cross_channel")):
        errors.append("ROOT: outputul nu conține nici reels, nici posts, nici account_setup, nici growth_plan, nici diagnostics, nici cross_channel.")

    for n in notes:
        print(f"NOTĂ: {n}")
    if errors:
        print(f"INVALID — {len(errors)} problem(e):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("VALID — outputul trece schema și toate regulile dure ale kitului.")
    sys.exit(0)


if __name__ == "__main__":
    main()
