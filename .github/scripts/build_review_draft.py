#!/usr/bin/env python3

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from urllib.parse import quote
from os.path import relpath as os_relpath
import re
import sys
from pathlib import Path


LINK_PATTERN = re.compile(r'(!?\[[^\]]*\])\(([^)]+)\)')
CHANGELOG_VERSION_PATTERN = re.compile(r"^## \[([^\]]+)\] - (\d{4}-\d{2}-\d{2})$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assemble the review draft Markdown source for PDF export."
    )
    parser.add_argument("--manifest", required=True, help="Path to the manifest file.")
    parser.add_argument("--output", required=True, help="Path to the combined Markdown output.")
    parser.add_argument(
        "--document-title",
        default="Dynamic Software Licensing Review Draft",
        help="Document title written into the generated front matter.",
    )
    parser.add_argument(
        "--document-subtitle",
        default="Best Practices",
        help="Document subtitle shown on the cover page.",
    )
    parser.add_argument(
        "--document-status",
        default="Reviewed Draft",
        help="Document status shown on the cover page.",
    )
    parser.add_argument(
        "--document-version",
        default=None,
        help="Document version shown on the version page. Defaults to the latest CHANGELOG entry.",
    )
    parser.add_argument(
        "--document-organization",
        default="International Association of MediaTech (IAMT)",
        help="Organization shown on the cover page.",
    )
    parser.add_argument(
        "--document-date",
        default=datetime.now(timezone.utc).strftime("%d %B %Y"),
        help="Date shown on the cover page.",
    )
    parser.add_argument(
        "--exclude-index-files",
        action="store_true",
        help="Exclude chapter 00-index.md files from the combined output.",
    )
    return parser.parse_args()


def load_manifest(manifest_path: Path, repo_root: Path) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()

    for raw_line in manifest_path.read_text(encoding="utf-8").splitlines():
        entry = raw_line.strip()
        if not entry or entry.startswith("#"):
            continue

        matches = sorted(repo_root.glob(entry))
        if not matches:
            raise ValueError(f"Manifest entry matched no files: {entry}")

        for match in matches:
            if not match.is_file() or match.suffix.lower() != ".md":
                continue
            resolved = match.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(resolved)

    if not files:
        raise ValueError("Manifest did not resolve to any Markdown files.")

    return files


def should_skip(path: Path, exclude_index_files: bool) -> bool:
    return exclude_index_files and path.name == "00-index.md"


def rewrite_local_links(text: str, source_path: Path, output_path: Path) -> str:
    source_dir = source_path.parent
    output_dir = output_path.parent.resolve()

    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        if target.startswith(("http://", "https://", "mailto:", "#", "/", "data:", "<")):
            return match.group(0)

        bare_target = target
        anchor = ""
        if "#" in target:
            bare_target, anchor_part = target.split("#", 1)
            anchor = f"#{anchor_part}"

        if not bare_target:
            return match.group(0)

        candidate = (source_dir / bare_target).resolve()
        if not candidate.exists():
            return match.group(0)

        rel_string = os_relpath(candidate, output_dir)
        rel_string = quote(rel_string, safe="/#-_.")
        return f"{label}(<{rel_string}{anchor}>)"

    return LINK_PATTERN.sub(replace, text)


def detect_latest_version(repo_root: Path) -> tuple[str | None, str | None]:
    changelog_path = repo_root / "CHANGELOG.md"
    if not changelog_path.exists():
        return None, None

    for line in changelog_path.read_text(encoding="utf-8").splitlines():
        match = CHANGELOG_VERSION_PATTERN.match(line.strip())
        if match:
            return match.group(1), match.group(2)

    return None, None


def build_cover_page(
    document_title: str,
    document_subtitle: str,
    document_status: str,
    document_organization: str,
    document_date: str,
) -> list[str]:
    return [
        r"\begin{titlepage}",
        r"\centering",
        r"\vspace*{0.18\textheight}",
        rf"{{\Huge\bfseries {document_title}\par}}",
        r"\vspace{0.8cm}",
        rf"{{\LARGE {document_subtitle}\par}}",
        r"\vspace{1.6cm}",
        rf"{{\Large {document_organization}\par}}",
        r"\vfill",
        rf"{{\large Status: {document_status}\par}}",
        r"\vspace{0.4cm}",
        rf"{{\large {document_date}\par}}",
        r"\end{titlepage}",
        "",
    ]


def build_version_page(
    document_version: str,
    document_status: str,
    document_date: str,
) -> list[str]:
    return [
        r"\section*{Version Information}",
        "",
        f"- Version: {document_version}",
        f"- Status: {document_status}",
        f"- Publication date: {document_date}",
        "- Review baseline: Complete chapter set available for group review",
        "",
        "This PDF is an assembled publication view generated from the Markdown sources in the repository.",
        "",
            r"\tableofcontents",
            r"\newpage",
        "",
    ]


def build_document(
    files: list[Path],
    output_path: Path,
    repo_root: Path,
    document_title: str,
    document_subtitle: str,
    document_status: str,
    document_version: str,
    document_organization: str,
    document_date: str,
    exclude_index_files: bool,
) -> int:
    sections = ["---", "lang: en", "---", ""]
    sections.extend(
        build_cover_page(
            document_title,
            document_subtitle,
            document_status,
            document_organization,
            document_date,
        )
    )
    sections.extend(
        build_version_page(
            document_version,
            document_status,
            document_date,
        )
    )
    included_count = 0

    for source_path in files:
        if should_skip(source_path, exclude_index_files):
            continue

        source_text = source_path.read_text(encoding="utf-8")
        source_text = rewrite_local_links(source_text, source_path, output_path)

        relative_source = source_path.relative_to(repo_root).as_posix()
        sections.append(f"<!-- Source: {relative_source} -->")
        sections.append(source_text.rstrip())
        sections.append("")
        included_count += 1

    if included_count == 0:
        raise ValueError("No Markdown files were included in the combined document.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    return included_count


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    manifest_path = (repo_root / args.manifest).resolve()
    output_path = (repo_root / args.output).resolve()
    detected_version, detected_date = detect_latest_version(repo_root)
    document_version = args.document_version or detected_version or "unversioned-draft"
    document_date = args.document_date

    if args.document_date == datetime.now(timezone.utc).strftime("%d %B %Y") and detected_date:
        document_date = datetime.strptime(detected_date, "%Y-%m-%d").strftime("%d %B %Y")

    try:
        files = load_manifest(manifest_path, repo_root)
        included_count = build_document(
            files,
            output_path,
            repo_root,
            args.document_title,
            args.document_subtitle,
            args.document_status,
            document_version,
            args.document_organization,
            document_date,
            args.exclude_index_files,
        )
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(
        f"Built {output_path.relative_to(repo_root)} from {included_count} Markdown files.",
        file=sys.stdout,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())