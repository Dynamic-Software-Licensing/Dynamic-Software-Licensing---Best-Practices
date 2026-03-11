#!/usr/bin/env python3
"""
Validates chapter status fields in best-practices/**/00-index.md files.

Usage:
  python3 validate_status.py                   # validates all 00-index.md files
  python3 validate_status.py path/to/00-index.md ...  # validates specific files

Exit code 0 = all valid.
Exit code 1 = one or more validation errors found.
"""

import re
import sys
from pathlib import Path


ALLOWED_VALUES: dict[str, set[str]] = {
    "Status": {
        "Working Draft",
        "Reviewed Draft",
        "Candidate Best Practices Text",
        "Stable for Cross-Reference",
    },
    "Editorial maturity": {
        "outline",
        "partial draft",
        "developed draft",
        "review-ready",
    },
    "Normative readiness": {
        "not started",
        "informative only",
        "partially normative",
        "ready for normative review",
    },
    "Open drafting points": {
        "yes",
        "no",
    },
}

REQUIRED_FIELDS = list(ALLOWED_VALUES.keys())


def validate_file(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    errors: list[str] = []

    match = re.search(
        r"## Chapter Status\n(.*?)(?=\n## |\Z)",
        content,
        re.DOTALL,
    )
    if not match:
        return ["Missing '## Chapter Status' section"]

    section = match.group(1)

    for field in REQUIRED_FIELDS:
        pattern = rf"[-*]\s+{re.escape(field)}:\s*(.+)"
        m = re.search(pattern, section)
        if not m:
            errors.append(f"Missing field: '{field}'")
        else:
            value = m.group(1).strip()
            if value not in ALLOWED_VALUES[field]:
                allowed = sorted(ALLOWED_VALUES[field])
                errors.append(
                    f"Invalid value for '{field}': '{value}'"
                    f"\n       Allowed: {allowed}"
                )

    return errors


def main() -> None:
    if len(sys.argv) > 1:
        files = [Path(arg) for arg in sys.argv[1:]]
    else:
        root = Path("best-practices")
        files = sorted(root.glob("**/00-index.md"))

    if not files:
        print("⚠️  No 00-index.md files found to validate.")
        sys.exit(0)

    all_ok = True
    for f in files:
        if not f.exists():
            all_ok = False
            print(f"\n❌ {f}:")
            print("   - File does not exist")
            continue

        errors = validate_file(f)
        if errors:
            all_ok = False
            print(f"\n❌ {f}:")
            for e in errors:
                print(f"   - {e}")
        else:
            print(f"✅ {f}")

    if all_ok:
        print("\nAll chapter status fields are valid.")
        sys.exit(0)
    else:
        print("\nValidation failed. See GOVERNANCE.md for allowed status values.")
        sys.exit(1)


if __name__ == "__main__":
    main()
