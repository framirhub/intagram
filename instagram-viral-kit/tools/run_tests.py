#!/usr/bin/env python3
"""Runner de teste pentru instagram-viral-kit.

De ce există: `tools/validate_output.py` era testat doar „pe pozitiv" — nimeni nu
dovedea că respinge ceva. Aici se verifică AMBELE direcții:

  - fixturi POZITIVE  — `examples/**/output.json`            → validator exit 0
  - fixturi NEGATIVE  — `examples/**/negative-*.json`        → validator exit 1
    (fixturile negative sunt intenționat invalide: NU se repară)

Plus un gard împotriva testelor care trec „pe gol": dacă nu există cel puțin o
fixtură pozitivă și una negativă, runnerul eșuează.

Folosire:
  python tools/run_tests.py           # rulare normală
  python tools/run_tests.py -v        # afișează și outputul validatorului

Exit 0 = toate așteptările s-au respectat, 1 = cel puțin un test a picat.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "tools" / "validate_output.py"
EXAMPLES = ROOT / "examples"

# Pentru fixturile negative: ce text trebuie să apară în raport (gard de regresie).
# Dacă cineva slăbește verificarea, testul cade chiar dacă exit code-ul rămâne 1.
EXPECTED_MARKER = {
    "negative-hook-swap.json": "HOOK SWAP",
}


def run_validator(path):
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def main():
    ap = argparse.ArgumentParser(description="Runner de teste instagram-viral-kit")
    ap.add_argument("-v", "--verbose", action="store_true", help="afișează outputul validatorului")
    args = ap.parse_args()

    positives = sorted(EXAMPLES.glob("**/output.json"))
    negatives = sorted(p for p in EXAMPLES.glob("**/*.json") if p.name.startswith("negative-"))

    failures = []
    if not positives:
        failures.append("nu există nicio fixtură pozitivă (examples/**/output.json)")
    if not negatives:
        failures.append("nu există nicio fixtură negativă (examples/**/negative-*.json)")

    print(f"Fixturi pozitive: {len(positives)} · negative: {len(negatives)}")
    print("-" * 72)

    for path in positives:
        code, out = run_validator(path)
        rel = path.relative_to(ROOT)
        if code == 0:
            print(f"  PASS  {rel}  (exit 0)")
        else:
            print(f"  FAIL  {rel}  (așteptat exit 0, primit {code})")
            failures.append(f"{rel}: fixtura pozitivă a picat validarea")
        if args.verbose:
            print("        " + out.strip().replace("\n", "\n        "))

    for path in negatives:
        code, out = run_validator(path)
        rel = path.relative_to(ROOT)
        marker = EXPECTED_MARKER.get(path.name)
        ok = code == 1 and "INVALID" in out and (marker is None or marker in out)
        if ok:
            detail = f", marker „{marker}” prezent" if marker else ""
            print(f"  PASS  {rel}  (exit 1{detail})")
        else:
            print(f"  FAIL  {rel}  (așteptat exit 1 + INVALID, primit {code})")
            failures.append(f"{rel}: fixtura negativă a trecut sau a picat cu alt motiv")
        if args.verbose:
            print("        " + out.strip().replace("\n", "\n        "))

    print("-" * 72)
    if failures:
        print(f"EȘUAT — {len(failures)} problem(e):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"OK — {len(positives) + len(negatives)} fixturi verificate (pozitive trec, negative sunt respinse).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
