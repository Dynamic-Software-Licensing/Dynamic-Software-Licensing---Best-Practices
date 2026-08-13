#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import re
from os.path import relpath as os_relpath
from pathlib import Path


SOURCE_PATTERN = re.compile(r"^<!-- Source: (.+) -->$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract Mermaid code blocks from Markdown and replace them with image references."
    )
    parser.add_argument("--input", required=True, help="Path to the input Markdown file.")
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the rewritten Markdown file.",
    )
    parser.add_argument(
        "--assets-dir",
        required=True,
        help="Directory where Mermaid source files should be written.",
    )
    return parser.parse_args()


def build_base_name(source_path: str | None, mermaid_code: str, diagram_count: int) -> str:
    digest = hashlib.sha256(mermaid_code.encode("utf-8")).hexdigest()[:12]
    if not source_path:
        return f"diagram-{diagram_count:02d}-{digest}"

    stem = Path(source_path).stem
    stem = re.sub(r"^\d{2}-", "", stem)
    stem = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    if not stem:
        return f"diagram-{diagram_count:02d}-{digest}"

    return f"{stem}-{digest}"


def replace_mermaid_blocks(text: str, output_path: Path, assets_dir: Path) -> tuple[str, int]:
    output_dir = output_path.parent.resolve()
    assets_dir = assets_dir.resolve()
    assets_dir.mkdir(parents=True, exist_ok=True)
    diagram_count = 0
    rewritten_lines: list[str] = []
    lines = text.splitlines()
    current_source: str | None = None
    in_mermaid = False
    mermaid_lines: list[str] = []

    for line in lines:
        source_match = SOURCE_PATTERN.match(line)
        if source_match and not in_mermaid:
            current_source = source_match.group(1)
            rewritten_lines.append(line)
            continue

        if line.strip() == "```mermaid" and not in_mermaid:
            in_mermaid = True
            mermaid_lines = []
            continue

        if line.strip() == "```" and in_mermaid:
            in_mermaid = False
            diagram_count += 1
            mermaid_code = "\n".join(mermaid_lines).strip()
            base_name = build_base_name(current_source, mermaid_code, diagram_count)

            mermaid_source_path = assets_dir / f"{base_name}.mmd"
            mermaid_source_path.write_text(mermaid_code + "\n", encoding="utf-8")

            image_path = assets_dir / f"{base_name}.png"
            rel_image_path = os_relpath(image_path, output_dir).replace("\\", "/")
            rewritten_lines.append(f"![]({rel_image_path})")
            continue

        if in_mermaid:
            mermaid_lines.append(line)
            continue

        rewritten_lines.append(line)

    return "\n".join(rewritten_lines) + "\n", diagram_count


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    assets_dir = Path(args.assets_dir).resolve()

    source_text = input_path.read_text(encoding="utf-8")
    rewritten_text, diagram_count = replace_mermaid_blocks(source_text, output_path, assets_dir)
    output_path.write_text(rewritten_text, encoding="utf-8")

    print(f"Prepared {diagram_count} Mermaid diagrams in {assets_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())