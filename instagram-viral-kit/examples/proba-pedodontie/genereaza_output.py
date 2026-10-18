#!/usr/bin/env python3
"""Generator pentru runul de probă (v1.2.0) — nișa pedodonție.

De ce un generator și nu JSON scris de mână: `visible_char_count`,
`verbal_word_count` și `hook_verbal_word_count` trebuie să fie IDENTICE cu
valorile reale din text (validatorul mecanic le compară, iar kitul cere ca
raportul să fie adevărat, nu declarat). Aici numărătoarea se calculează, deci
runul e reproductibil: rulează `python genereaza_output.py` și apoi
`python ../../tools/validate_output.py output.json`.

Conținutul (hook-uri, scripturi, caption-uri, planul) e scris de autor în
structurile de mai jos; scriptul doar completează câmpurile derivate și scrie
`output.json`.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def finalize_reel(r):
    r["hook"]["verbal_word_count"] = len(r["hook"]["verbal"].split())
    r["caption"]["visible_char_count"] = len(r["caption"]["hook_line"])
    return r


def finalize_post(p):
    p["caption"]["visible_char_count"] = len(p["caption"]["hook_line"])
    return p


reels = [
    {
        "id": "R1",
        "title": "Frica de dentist se învață acasă, nu la cabinet",
        "structure": "negative_warning",
        "pillar": "prima vizită fără frică",
        "goal": "reach",
        "duration_seconds": 32,
        "hook": {
            "visual": "0–1s mid-motion: mâna părintelui închide brusc ușa cabinetului, în fundal scaunul dentar gol",
            "verbal": "Frica de dentist se învață acasă, nu aici.",
            "text_on_screen": "GREȘEALA PĂRINȚILOR",
            "audio": "whoosh + tăcere totală 1 secundă, apoi voce fără muzică",
            "mute_test_passed": True,
        },
        "script": "\n".join([
            "0:00–0:01  [vizual] mid-motion — mâna închide ușa cabinetului      [reset: whoosh]",
            "0:01–0:03  „Frica de dentist se învață acasă, nu aici.”            [reset: jump-zoom pe față]",
            "0:03–0:06  „Trei lucruri care o construiesc în casa voastră.”      [reset: b-roll scaun gol]",
            "0:06–0:09  „1. Nu-i spune «nu doare».”                              [reset: text pe ecran „1”]",
            "0:09–0:12  „Când doare, nu te mai crede.”                           [reset: cadru apropiat]",
            "0:12–0:15  „2. Nu promite cadouri.”                                [reset: schimbare unghi]",
            "0:15–0:18  „Vizita devine negociere, nu rutină.”                    [reset: pop SFX]",
            "0:18–0:21  „3. Nu-l duce când are deja durere.”                     [reset: text pe ecran „3”]",
            "0:21–0:24  „Prima amintire rămâne cea rea.”                         [reset: zoom out]",
            "0:24–0:27  „Du-l o dată doar să salutăm.”                           [reset: cadru larg cabinet]",
            "0:27–0:30  „Fără tratament, fără surprize.”                         [reset: revenire pe față]",
            "0:30–0:32  CTA verbal + text mare „GHIDUL”                          [reset: text mare „GHIDUL”]",
        ]),
        "editing_checklist": [
            "Dead air tăiat; nicio pauză mai lungă de 0,4s între propoziții.",
            "Subtitrări cuvânt-cuvânt, centrate, galben pe negru (testul mut).",
            "Mixaj: voce 0 dB, muzică −20 dB, whoosh doar la reset-uri.",
            "Text cheie în centrul 3:4 (1080×1440) — nimic sub 350px jos sau 250px dreapta.",
            "Cover: „FRICA SE ÎNVAȚĂ ACASĂ” lizibil în grila 3:4.",
            "Export 1080×1920, MP4 H.264, 30fps, fără watermark.",
        ],
        "caption": {
            "hook_line": "Prima vizită la dentist pentru copii: frica se construiește acasă, în 3 propoziții.",
            "body": "\n".join([
                "Cele trei propoziții care fac prima vizită un coșmar:",
                "1. „Nu doare, promit.” → când doare, copilul nu mai crede nimic.",
                "2. „Dacă ești cuminte, îți iau ceva.” → vizita devine negociere.",
                "3. Prima vizită se face când apare durerea. → prima amintire rămâne cea rea.",
                "",
                "Ce funcționează în schimb: o vizită scurtă, „doar salutăm”, fără tratament,",
                "cu părintele lângă scaun. Copilul memorabil nu ce i-ai spus, ci cum te-a văzut pe tine.",
                "",
                "Care dintre cele trei propoziții ți-a scăpat și ție? Scrie în comentarii. 👇",
            ]),
            "cta": {
                "value_exchange": "Comentează GHID și îți trimit lista de 7 zile de pregătire (1 pagină) în DM.",
                "keyword": "GHID",
                "layers": ["text_on_screen", "verbal_end", "caption"],
            },
            "hashtags": ["#pedodontie", "#dentistpentrucopii", "#primavizita", "#parinti", "#sănătateadintară"],
        },
        "publish": {
            "channel": "trial_reels",
            "timing_note": "Format nou pentru cont → Trial Reels; ora din Insights (baseline mar–mie 9–11).",
            "quality_check": True,
            "first_hour_action": "Răspunde la fiecare comentariu în prima oră; adună manual keyword-urile până se activează ManyChat.",
        },
        "audit": {
            "hook_scroll_stop": 23,
            "retention_structure": 19,
            "discoverability": 18,
            "compliance_originality": 15,
            "cta_growth_loop": 19,
            "total": 94,
            "verdict": "PASS",
            "issues": [
                {"priority": "P2", "criterion": "hook_scroll_stop", "problem": "Text-on-screen „GREȘEALA PĂRINȚILOR” are 20 caractere — la 3:4 rămâne lizibil, dar mai slab contrastant pe fundal deschis.", "fix": "Adaugă o bandă semi-transparentă în spatele textului."},
            ],
        },
        "needs_research": ["audience.voC_quotes — citatele de durere din caption sunt DEMO; înlocuiește-le cu citate reale (modula-research) înainte de filmare."],
    },
    {
        "id": "R2",
        "title": "3 greșeli în ziua vizitei la dentist",
        "structure": "number_led_proof",
        "pillar": "mituri și greșeli ale părinților",
        "goal": "saves_authority",
        "duration_seconds": 45,
        "hook": {
            "visual": "0–1s: cadru din mașină, geanta de pe scaunul din față se răstoarnă și cade jucăria copilului",
            "verbal": "Trei greșeli care fac prima vizită un coșmar.",
            "text_on_screen": "3 GREȘELI",
            "audio": "pop SFX + muzică discretă, tăiată la fiecare punct",
            "mute_test_passed": True,
        },
        "script": "\n".join([
            "0:00–0:02  [vizual] geanta se răstoarnă, jucăria cade               [reset: pop SFX]",
            "0:02–0:05  „Trei greșeli care fac prima vizită un coșmar.”         [reset: jump-zoom]",
            "0:05–0:08  „1. Programezi la ora somnului, după grădiniță.”         [reset: text „1”]",
            "0:08–0:11  „Copilul obosit nu are resurse pentru nou.”              [reset: b-roll mașină]",
            "0:11–0:14  „2. Intri tu primul și vorbești cu medicul.”            [reset: schimbare cadru]",
            "0:14–0:17  „Zece minute în care copilul așteaptă.”                  [reset: cadru apropiat]",
            "0:17–0:20  „Și își imaginează ce se întâmplă acolo.”                [reset: pop SFX]",
            "0:20–0:23  „3. Pleci imediat după.”                                [reset: text „3”]",
            "0:23–0:26  „Prima vizită trebuie să fie scurtă.”                    [reset: schimbare unghi]",
            "0:26–0:29  „Se termină înainte de oboseală.”                        [reset: cadru larg]",
            "0:29–0:32  „Dimineața, împreună, scurt.”                            [reset: text pe ecran]",
            "0:32–0:35  „Fără tratament în prima vizită.”                         [reset: b-roll cabinet]",
            "0:35–0:38  „Doar familiarizare cu cabinetul.”                      [reset: pop SFX]",
            "0:38–0:41  „Programează și respectă ora.”                          [reset: revenire pe față]",
            "0:41–0:45  CTA „SALVEAZĂ pentru ziua programării”                   [reset: text mare „SALVEAZĂ”]",
        ]),
        "editing_checklist": [
            "Fiecare dintre cele 3 puncte începe cu text-on-screen numerotat (dwell time).",
            "Subtitrări cuvânt-cuvânt; cifrele scrise cu cifre, nu cu litere.",
            "B-roll din cabinet cu acord scris (fără pacienți identificabili).",
            "Safe zone respectată: textul numerotat în centrul 3:4.",
            "Export fără watermark, 1080×1920, 30fps.",
        ],
        "caption": {
            "hook_line": "Dentist pentru copii: 3 greșeli care transformă prima vizită în coșmar.",
            "body": "\n".join([
                "1. Ora: după grădiniță, la ora somnului. Copilul obosit nu are resurse pentru ceva nou.",
                "2. Ordinea: părintele intră primul și vorbește zece minute. Copilul așteaptă și completează golul cu scenarii.",
                "3. Finalul: pleci imediat, în grabă. Prima vizită trebuie să fie scurtă și să se termine înainte de oboseală.",
                "",
                "Regula simplă: dimineața, împreună, scurt. Fără tratament în prima vizită — doar familiarizare.",
                "",
                "Care e greșeala pe care o faci deja? (a doua e cea mai des întâlnită în cabinet)",
            ]),
            "cta": {
                "value_exchange": "Salvează postarea pentru ziua în care programezi și comentează LISTA pentru ghidul primelor 7 zile în DM.",
                "keyword": "LISTA",
                "layers": ["text_on_screen", "caption"],
            },
            "hashtags": ["#primavizitaladentist", "#dentistcopii", "#pedodontie", "#sfaturipentruparinti", "#sanatatedentara"],
        },
        "publish": {
            "channel": "normal",
            "timing_note": "Format de tip listă = format validat în nișă → publicare normală, marți 9:30.",
            "quality_check": True,
            "first_hour_action": "Răspunde cu un al patrulea pont la primele comentarii (dwell time pe postare).",
        },
        "audit": {
            "hook_scroll_stop": 22,
            "retention_structure": 18,
            "discoverability": 18,
            "compliance_originality": 15,
            "cta_growth_loop": 17,
            "total": 90,
            "verdict": "PASS",
            "issues": [
                {"priority": "P2", "criterion": "cta_growth_loop", "problem": "Textul de ecran „SALVEAZĂ” apare abia în ultimele 4 secunde (0:41–0:45) — CTA-ul nu e vizibil pentru cine abandonează la 0:35.", "fix": "Avansează textul „SALVEAZĂ” la 0:35, suprapus peste ultimul punct, sau ridică salvarea în textul de la 0:32."},
            ],
        },
        "needs_research": ["content_pool.proven_formats — formatul „3 greșeli” e presupus dovedit; verifică în Content Pool (20+ Reels din nișă) înainte de scale."],
    },
    {
        "id": "R3",
        "title": "Sub 6 ani: ce se întâmplă (și ce nu) la prima vizită",
        "structure": "audience_callout",
        "pillar": "prima vizită fără frică",
        "goal": "leads_comment_to_dm",
        "duration_seconds": 38,
        "hook": {
            "visual": "0–1s: mâna unui copil mic pune o jucărie pe scaunul dentar, apoi se urcă singur",
            "verbal": "Dacă copilul are sub 6 ani, citește asta.",
            "text_on_screen": "SUB 6 ANI",
            "audio": "sunet ambiental de cabinet, fără muzică (autenticitate)",
            "mute_test_passed": True,
        },
        "script": "\n".join([
            "0:00–0:02  [vizual] copilul urcă singur pe scaun                    [reset: sunet real, fără muzică]",
            "0:02–0:05  „Dacă copilul are sub 6 ani, citește asta.”              [reset: jump-zoom]",
            "0:05–0:08  „Sub 6 ani nu se tratează ca la adult.”                  [reset: b-roll instrumente]",
            "0:08–0:11  „Se obișnuiește, în pași mici.”                         [reset: cadru apropiat]",
            "0:11–0:14  „Vizita 1: copilul vede, atinge, întreabă.”              [reset: text „FĂRĂ TRATAMENT”]",
            "0:14–0:17  „Fără tratament în prima vizită.”                        [reset: schimbare unghi]",
            "0:17–0:20  „Vizita 2: curățare blândă.”                            [reset: text „2”]",
            "0:20–0:23  „Doar dacă a stat liniștit.”                            [reset: cadru larg cabinet]",
            "0:23–0:26  „I se anunță fiecare pas înainte.”                       [reset: pop SFX]",
            "0:26–0:29  „Vizita 3+: tratament pe bucăți mici.”                   [reset: text „3+”]",
            "0:29–0:32  „Cu pauze, la cerere.”                                  [reset: revenire pe față]",
            "0:32–0:35  „Scopul nu e dintele de azi.”                           [reset: cadru cu copilul]",
            "0:35–0:38  CTA verbal + text mare „GHIDUL”                          [reset: text mare „GHIDUL”]",
        ]),
        "editing_checklist": [
            "Fără muzică tensionată — sunetul cabinetului vinde autenticitatea.",
            "Text-on-screen „FĂRĂ TRATAMENT” exact în momentul rostit (sincron).",
            "Niciun cadru cu pacienți identificabili; acord scris pentru spațiu.",
            "Cover 3:4: „SUB 6 ANI” + fața copilului, fără instrumente în prim-plan.",
            "Export 1080×1920, MP4 H.264, 30fps, fără watermark.",
        ],
        "caption": {
            "hook_line": "Dentist pentru copii: prima vizită sub 6 ani, pas cu pas.",
            "body": "\n".join([
                "Sub 6 ani, obiectivul primei vizite nu e tratamentul — e obișnuința.",
                "",
                "• Vizita 1: copilul vede cabinetul, atinge instrumentele, întreabă. Zero tratament.",
                "• Vizita 2: curățare blândă, doar dacă a stat liniștit și i s-a explicat înainte fiecare pas.",
                "• Vizita 3+: tratamentul propriu-zis, pe bucăți mici, cu pauze la cerere.",
                "",
                "Scopul nu e dintele de azi, e ca la 10 ani copilul să intre singur în cabinet.",
                "",
                "La ce vârstă ai dus copilul prima dată? Spune-mi în comentarii — și zi-mi ce te-a oprit.",
            ]),
            "cta": {
                "value_exchange": "Comentează GHID și primești în DM lista de 7 zile de pregătire (1 pagină, exact ce e în postare).",
                "keyword": "GHID",
                "layers": ["text_on_screen", "verbal_end", "caption"],
            },
            "hashtags": ["#dentistcopii", "#pedodontie", "#primavizita", "#parintiro", "#sănătateadintară"],
        },
        "publish": {
            "channel": "normal",
            "timing_note": "Postarea de conversație — joi seara 19:00, când părinții citesc în pat (verifică în Insights).",
            "quality_check": True,
            "first_hour_action": "Răspunde fiecărui părinte cu un răspuns personalizat (nu șablon); pregătește DM-ul cu ghidul înainte.",
        },
        "audit": {
            "hook_scroll_stop": 21,
            "retention_structure": 18,
            "discoverability": 18,
            "compliance_originality": 15,
            "cta_growth_loop": 17,
            "total": 89,
            "verdict": "PASS",
            "issues": [
                {"priority": "P2", "criterion": "compliance_originality", "problem": "Sunetul ambiental de cabinet poate conține voci de copii identificabile.", "fix": "Folosește doar înregistrări cu acord scris sau înlocuiește cu ambianță neutră."},
            ],
        },
        "needs_research": ["offer.lead_magnet — confirmă că lista de 7 zile există fizic înainte de a rula CTA-ul cu keyword."],
    },
]

posts = [
    {
        "id": "P1",
        "title": "Prima vizită la dentist: 7 zile de pregătire (carusel)",
        "format": "carousel",
        "pillar": "prima vizită fără frică",
        "slides": [
            {"position": 1, "text": "Prima vizită: 7 zile de pregătire", "design_note": "HOOK — titlu mare, fundal crem, începe cu cifra 7", "is_reference_slide": False},
            {"position": 2, "text": "Ziua 1–2: joacă „dentistul” acasă cu o lanternă mică.", "design_note": "ilustrație simplă, o singură idee pe slide", "is_reference_slide": False},
            {"position": 3, "text": "Ziua 3: citește o carte despre dentist. Nu una despre durere.", "design_note": "copertă de carte reală, cadru apropiat", "is_reference_slide": False},
            {"position": 4, "text": "Ziua 4: scoate din vocabular „doare” și „nu-ți face nimic”.", "design_note": "text tăiat cu o linie vizuală", "is_reference_slide": False},
            {"position": 5, "text": "Ziua 5: programează dimineața, nu după grădiniță.", "design_note": "comparativ zi/noapte, fără dramatizare", "is_reference_slide": False},
            {"position": 6, "text": "Ziua 6: vizită scurtă — „doar salutăm”, fără tratament.", "design_note": "cadru cu copilul pe scaun, părintele aproape", "is_reference_slide": False},
            {"position": 7, "text": "Ziua 7: somn bun, mic dejun, fără discuții în mașină.", "design_note": "checklist cu bife", "is_reference_slide": False},
            {"position": 8, "text": "Ce NU faci: nu minți că nu se întâmplă nimic.", "design_note": "slide de tip „anti-sfat”, marcat vizual diferit", "is_reference_slide": False},
            {"position": 9, "text": "La cabinet: părintele stă jos, copilul vede tot, prima vizită nu are tratament.", "design_note": "3 puncte scurte, nu text lung", "is_reference_slide": False},
            {"position": 10, "text": "Lista completă de 7 zile: salvează slide-ul și bifează.", "design_note": "REFERENCE — design de listă de salvat, numele contului jos, discret", "is_reference_slide": True},
        ],
        "open_loop": "Partea 2: ce întrebi medicul în primele 3 minute (urmează miercurea viitoare).",
        "caption": {
            "hook_line": "Prima vizită la dentist pentru copii: planul de 7 zile, salvat de părinți.",
            "body": "\n".join([
                "Nu ai nevoie de curaj, ai nevoie de 7 zile de pregătire. Slide cu slide:",
                "",
                "• Jocul „dentistul” acasă — copilul explorează înainte să fie explorat.",
                "• Cărți despre dentist, nu despre durere.",
                "• „Doare” și „nu-ți face nimic” ies din vocabular.",
                "• Ora dimineții bate ora somnului.",
                "• Prima vizită e de salut, nu de tratament.",
                "",
                "Ce lipsește din planul tău: emoția ta. Copilul citește fața părintelui înainte să citească orice afiș.",
                "",
                "La ce zi ai ajuns tu? Spune în comentarii și salvează pentru luna în care programezi.",
            ]),
            "cta": {
                "value_exchange": "Salvează postarea pentru ziua în care programezi și comentează LISTA pentru versiunea PDF de 1 pagină în DM.",
                "keyword": "LISTA",
                "save_prompt": "Salvează pentru săptămâna în care ai programarea.",
            },
            "hashtags": ["#primavizitaladentist", "#dentistpentrucopii", "#pedodontie", "#parinti", "#sănătateadintară"],
        },
        "audit": {
            "hook_scroll_stop": 22,
            "retention_structure": 19,
            "discoverability": 18,
            "compliance_originality": 15,
            "cta_growth_loop": 16,
            "total": 90,
            "verdict": "PASS",
            "issues": [
                {"priority": "P2", "criterion": "cta_growth_loop", "problem": "Caruselul cere două acțiuni (salvează + comentează) — risc de diluare a CTA-ului.", "fix": "Ține salvarea pe slide 10 și keyword-ul în ultima linie din caption, ca acum; nu adăuga al treilea CTA."},
            ],
        },
        "needs_research": ["audience.voC_quotes — formularea „nu-ți face nimic” e presupusă din cabinet; confirmă cu citate reale de părinți."],
    },
]

setup = [
    {"item": "professional_account", "status": "PASS", "is_blocker": False},
    {"item": "upload_highest_quality", "status": "PASS", "is_blocker": False},
    {"item": "search_engine_indexing", "status": "FAIL", "how_to_fix": "Settings and activity → Media quality / indexare: bifează „Allow public photos and videos to appear in search engine results” (Google indexează conturile profesionale din 10.07.2025).", "is_blocker": False},
    {"item": "account_status", "status": "PASS", "is_blocker": False},
    {"item": "translations", "status": "UNKNOWN", "how_to_fix": "Settings → Language and translations: verifică traducerile; dubbing Meta AI disponibil de la 1.000 de followeri.", "is_blocker": False},
    {"item": "bio_seo", "status": "FAIL", "how_to_fix": "Rescrie bio-ul: „Zâmbetul Mic | Dentist pentru copii 0–12 ani” + ce primește părintele + CTA „Scrie GHID pentru lista de 7 zile”.", "is_blocker": False},
    {"item": "niche_clarity", "status": "PASS", "is_blocker": False},
]

growth_plan = {
    "strategy_name": "Best of Nine — 30 zile (adaptat pedodonție)",
    "niche": "pedodonție — dentist pentru copii 0–12 ani",
    "content_pillars": ["prima vizită fără frică", "obiceiuri acasă", "mituri și greșeli ale părinților"],
    "weeks": [
        {
            "week": 1,
            "theme": "Setare & Cercetare",
            "actions": [
                "Repară cele 2 FAIL de setup (indexare Google, bio SEO) ÎNAINTE de orice postare.",
                "Construiește Content Pool: 20+ Reels virale din pedodonție, cu notițe (structură hook, durată, mecanism de retenție, CTA).",
                "Cere 5 citate reale de la părinți din cabinet (acord scris) → VoC înlocuiește frazele demo.",
                "Pregătește ghidul de 7 zile (PDF, 1 pagină) — CTA-ul cu keyword nu are voie să promită ceva inexistent.",
            ],
            "success_metric": "7/7 puncte de setup PASS + 20 Reels în Content Pool + ghid PDF scris",
        },
        {
            "week": 2,
            "theme": "Testing: cele 9 formate",
            "actions": [
                "Alege 3 formate dovedite din Content Pool (ex: „3 greșeli”, „povestea unei urgențe”, „ce face medicul pas cu pas”).",
                "Recreează-le în vocea cabinetului (fără copiere) și postează fiecare de 3 ori → 9 Reels.",
                "Rulează R1–R3 din acest pachet; primele două formate noi prin Trial Reels.",
                "Publică la orele din Insights; verifică rezultatul la 72h, nu la 30 de minute.",
            ],
            "success_metric": "9 Reels publicate + raport la 72h pentru fiecare (hook rate, completion, sends)",
        },
        {
            "week": 3,
            "theme": "Scale pe formatul câștigător",
            "actions": [
                "Identifică formatul cu cel mai bun watch time + sends și dublează producția pe el.",
                "Produce în lot (2–3 ore într-o sesiune → 4–5 Reels), variind hook-ul, nu formatul.",
                "Activează Comment-to-DM (ManyChat) pe Reels cu valoare de trimis; promisiunea din DM = exact cea din CTA.",
                "Publică caruselul P1 (motorul de saves) și Story-uri zilnice cu sondaje despre frica de dentist.",
            ],
            "success_metric": "1 format validat (watch time > 8,5s) + 20 salvări la carusel + automatizarea activă",
        },
        {
            "week": 4,
            "theme": "Serii, comunitate, conversie",
            "actions": [
                "Deschide seria „Prima vizită, pas cu pas” cu open loop la finalul fiecărui Reel.",
                "Postează a doua parte din open loop-ul caruselului (ce întrebi medicul în primele 3 minute).",
                "Verifică traseul comercial: Reel → profil → postări fixate (dovadă + ofertă) → CTA, și fixează 3 postări.",
                "Răspunde în primele 30–60 de minute la fiecare postare; pune întrebarea de opinie în caption.",
            ],
            "success_metric": "un Reel cu majoritate de views de la non-followeri; 10 cereri pe keyword; 3 postări fixate",
        },
    ],
    "month_success_metric": "un Reel în valul 2+ de distribuție (majoritate non-followeri) SAU un format validat cu watch time peste media 2026 (8,5s)",
}

output = {
    "kit": "instagram-viral-kit",
    "kit_version": "1.2.0",
    "brief_ref": "examples/proba-pedodontie/brief.json",
    "language": "ro",
    "generated_at": "2026-10-15T12:00:00+03:00",
    "warnings": [
        "audience.voC_quotes este gol → frazele de durere din captions sunt DEMO, marcate NEVOIE_RESEARCH pe fiecare livrabil. Înlocuiește-le cu citate reale (skill modula-research) înainte de filmare.",
        "Cifrele de țintă din plan (sends 1/100–200 views, saves 1/50–100, comentarii 15–30/1k) sunt „heuristica kitului\"; pragurile de skip rate (~40%), share rate (0,5–2%), save rate (1–3%) și completion (<15s: ≥70%) sunt T3 — practician 2026 (knowledge/corpus-2026.md). Livrează-le marcate, nu ca benchmark oficial.",
        "account_setup: 2 FAIL (search_engine_indexing, bio_seo) — se repară înainte de scalare; account_status e PASS, deci nu există blocant P0.",
        "ManyChat nu e activ: keyword-urile se adună manual până la activare; nimic din CTA nu are voie să promită altceva decât livrarea reală din DM.",
        "Compliance health respectat: zero promisiuni de rezultat medical, fără diagnostic la distanță, fără testimonial de pacient fără acord scris.",
        "Orele de publicare și durata sunt ținte de lucru — se recalibrează din Insights după primele 9 postări.",
    ],
    "reels": [finalize_reel(r) for r in reels],
    "posts": [finalize_post(p) for p in posts],
    "account_setup": setup,
    "growth_plan": growth_plan,
    "audit": {
        "auditor": "viral-auditor",
        "total_score_avg": round(sum(r["audit"]["total"] for r in reels + posts) / (len(reels) + len(posts)), 1),
        "pass_count": 4,
        "revise_count": 0,
        "reject_count": 0,
        "common_issues": [
            "Toate cele 4 livrabile stau pe P2 (contrast, ritm, ambianță) — zero P0/P1 după reparații; livrarea e curată mecanic.",
            "Keyword-ul „dentist pentru copii” a fost mutat identic în prima linie din caption la R2, R3 și P1 (înainte apărea parafrazat).",
            "Promisiunea din CTA-ul cu keyword = exact livrarea din DM (lista de 7 zile) — de confirmat că PDF-ul există fizic înainte de publicare.",
        ],
    },
}

out = HERE / "output.json"
out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("scris:", out)
print("hook-uri verbale (cuvinte):", [r["hook"]["verbal_word_count"] for r in output["reels"]])
print("caption hook_line (caractere):", [r["caption"]["visible_char_count"] for r in output["reels"]] + [p["caption"]["visible_char_count"] for p in output["posts"]])
