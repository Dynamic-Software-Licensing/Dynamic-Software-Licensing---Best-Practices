#!/usr/bin/env python3
"""
Reads all recommendation/**/00-index.md files, extracts the Chapter Status
block, and regenerates the status table in recommendation/index.md.

Safe to run locally and in CI. Only writes if content actually changed.
"""

import re
import sys
from pathlib import Path


STATUS_FIELDS = ["Status", "Editorial maturity", "Normative readiness"]

TABLE_HEADER = (
    "| Chapter | Status | Editorial maturity | Normative readiness |\n"
    "|---|---|---|---|"
)


def extract_chapter_title(content: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def extract_status_fields(content: str) -> dict[str, str] | None:
    match = re.search(
        r"## Chapter Status\n(.*?)(?=\n## |\Z)",
        content,
        re.DOTALL,
    )
    if not match:
        return None

    section = match.group(1)
    result: dict[str, str] = {}
    for field in STATUS_FIELDS:
        m = re.search(rf"[-*]\s+{re.escape(field)}:\s*(.+)", section)
        result[field] = m.group(1).strip() if m else "—"
    return result


def build_new_table() -> str:
    root = Path("recommendation")
    rows: list[str] = []

    for chapter_dir in sorted(root.iterdir()):
        if not chapter_dir.is_dir():
            continue
        index_file = chapter_dir / "00-index.md"
        if not index_file.exists():
            continue

        content = index_file.read_text(encoding="utf-8")
        title = extract_chapter_title(content, chapter_dir.name)
        status = extract_status_fields(content)

        if status:
            rows.append(
                f"| {title} "
                f"| {status['Status']} "
                f"| {status['Editorial maturity']} "
                f"| {status['Normative readiness']} |"
            )

    return TABLE_HEADER + "\n" + "\n".join(rows)


def update_index() -> None:
    index_path = Path("recommendation/index.md")
    if not index_path.exists():
        print(f"❌ {index_path} not found.", file=sys.stderr)
        sys.exit(1)

    content = index_path.read_text(encoding="utf-8")
    new_table = build_new_table()

    updated = re.sub(
        r"(\| Chapter \| Status \|.*?\n(?:\|[^\n]*\n)+)",
        new_table + "\n",
        content,
        flags=re.DOTALL,
    )

    if updated == content:
        print("ℹ️  Status table is already up to date.")
    else:
        index_path.write_text(updated, encoding="utf-8")
        print("✅ Status table updated in recommendation/index.md")


if __name__ == "__main__":
    update_index()
