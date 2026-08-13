#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import re
from os.path import relpath as os_relpath
from pathlib import Path


MERMAID_BLOCK_PATTERN = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)


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


def replace_mermaid_blocks(text: str, output_path: Path, assets_dir: Path) -> tuple[str, int]:
    output_dir = output_path.parent.resolve()
    assets_dir = assets_dir.resolve()
    assets_dir.mkdir(parents=True, exist_ok=True)
    diagram_count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal diagram_count

        diagram_count += 1
        mermaid_code = match.group(1).strip()
        digest = hashlib.sha256(mermaid_code.encode("utf-8")).hexdigest()[:12]
        base_name = f"diagram-{diagram_count:02d}-{digest}"

        mermaid_source_path = assets_dir / f"{base_name}.mmd"
        mermaid_source_path.write_text(mermaid_code + "\n", encoding="utf-8")

        image_path = assets_dir / f"{base_name}.png"
        rel_image_path = os_relpath(image_path, output_dir).replace("\\", "/")

        return f"![Mermaid diagram]({rel_image_path})"

    return MERMAID_BLOCK_PATTERN.sub(replace, text), diagram_count


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