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
HEADING_PATTERN = re.compile(r"^(#{1,6})(\s+.*)$")
LEADING_HEADING_NUMBER_PATTERN = re.compile(r"^\d{2}(?:\.\d{2})*\.\s+")
LIST_MARKER_PATTERN = re.compile(r"^(?:[-*+]\s+|\d+\.\s+)")
CODE_SPAN_PATTERN = re.compile(r"`([^`]+)`")


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


def is_main_chapter_index(path: Path, repo_root: Path) -> bool:
    relative = path.relative_to(repo_root).parts
    return len(relative) >= 3 and relative[0] == "best-practices" and path.name == "00-index.md"


def is_subchapter_file(path: Path, repo_root: Path) -> bool:
    relative = path.relative_to(repo_root).parts
    return len(relative) >= 3 and relative[0] == "best-practices" and path.name != "00-index.md"


def heading_offset_for_file(path: Path) -> int:
    if path.suffix.lower() != ".md":
        return 0
    if path.name == "00-index.md":
        return 0
    parent_name = path.parent.name
    if re.match(r"^\d{2}-", parent_name):
        return 1
    return 0


def chapter_prefix_for_file(path: Path) -> str | None:
    if path.name == "00-index.md":
        return None

    parent_name = path.parent.name
    file_name = path.stem

    parent_match = re.match(r"^(\d{2})-", parent_name)
    file_match = re.match(r"^(\d{2})-", file_name)
    if not parent_match or not file_match:
        return None

    return f"{parent_match.group(1)}.{file_match.group(1)}."


def demote_following_headings(text: str, level_offset: int) -> str:
    if level_offset <= 0:
        return text

    adjusted_lines: list[str] = []
    in_fenced_code = False
    first_heading_seen = False

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fenced_code = not in_fenced_code
            adjusted_lines.append(line)
            continue

        if in_fenced_code:
            adjusted_lines.append(line)
            continue

        match = HEADING_PATTERN.match(line)
        if not match:
            adjusted_lines.append(line)
            continue

        hashes, rest = match.groups()
        if not first_heading_seen:
            adjusted_lines.append(line)
            first_heading_seen = True
            continue

        new_level = min(len(hashes) + level_offset, 6)
        adjusted_lines.append("#" * new_level + rest)

    return "\n".join(adjusted_lines)


def adjust_heading_levels(text: str, level_offset: int) -> str:
    if level_offset <= 0:
        return text

    adjusted_lines: list[str] = []
    in_fenced_code = False

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fenced_code = not in_fenced_code
            adjusted_lines.append(line)
            continue

        if in_fenced_code:
            adjusted_lines.append(line)
            continue

        match = HEADING_PATTERN.match(line)
        if not match:
            adjusted_lines.append(line)
            continue

        hashes, rest = match.groups()
        new_level = min(len(hashes) + level_offset, 6)
        adjusted_lines.append("#" * new_level + rest)

    return "\n".join(adjusted_lines)


def prefix_first_heading(text: str, prefix: str | None) -> str:
    if not prefix:
        return text

    adjusted_lines: list[str] = []
    in_fenced_code = False
    prefixed = False

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fenced_code = not in_fenced_code
            adjusted_lines.append(line)
            continue

        if in_fenced_code or prefixed:
            adjusted_lines.append(line)
            continue

        match = HEADING_PATTERN.match(line)
        if not match:
            adjusted_lines.append(line)
            continue

        hashes, rest = match.groups()
        heading_text = rest.strip()
        heading_text = LEADING_HEADING_NUMBER_PATTERN.sub("", heading_text)
        adjusted_lines.append(f"{hashes} {prefix} {heading_text}")
        prefixed = True

    return "\n".join(adjusted_lines)


def normalize_list_spacing(text: str) -> str:
    adjusted_lines: list[str] = []
    in_fenced_code = False

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fenced_code = not in_fenced_code
            adjusted_lines.append(line)
            continue

        if in_fenced_code:
            adjusted_lines.append(line)
            continue

        if LIST_MARKER_PATTERN.match(stripped):
            previous_line = adjusted_lines[-1] if adjusted_lines else ""
            previous_stripped = previous_line.strip()
            if previous_stripped and not LIST_MARKER_PATTERN.match(previous_stripped):
                adjusted_lines.append("")

        adjusted_lines.append(line)

    return "\n".join(adjusted_lines)


def format_table_code_span(content: str) -> str:
    if " " in content:
        escaped = content.replace("\\", r"\textbackslash{}")
        escaped = escaped.replace("{", r"\{")
        escaped = escaped.replace("}", r"\}")
        escaped = escaped.replace("_", r"\_")
        return rf"\texttt{{{escaped}}}"

    delimiter = "+"
    if delimiter in content:
        delimiter = "!"
    if delimiter in content:
        delimiter = ";"
    return rf"\path{delimiter}{content}{delimiter}"


def normalize_table_code_spans(text: str) -> str:
    adjusted_lines: list[str] = []
    in_fenced_code = False

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fenced_code = not in_fenced_code
            adjusted_lines.append(line)
            continue

        if in_fenced_code or "|" not in line:
            adjusted_lines.append(line)
            continue

        table_candidate = line.strip()
        if not table_candidate.startswith("|"):
            adjusted_lines.append(line)
            continue

        if set(table_candidate) <= {"|", "-", ":", " "}:
            adjusted_lines.append(line)
            continue

        adjusted_lines.append(
            CODE_SPAN_PATTERN.sub(lambda match: format_table_code_span(match.group(1)), line)
        )

    return "\n".join(adjusted_lines)


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


def load_changelog_text(repo_root: Path) -> str:
    changelog_path = repo_root / "CHANGELOG.md"
    if not changelog_path.exists():
        return ""

    lines = changelog_path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "# Changelog":
        lines = lines[1:]

    return "\n".join(lines).strip()


def load_license_text(repo_root: Path) -> str:
    license_path = repo_root / "LICENSE"
    if not license_path.exists():
        return ""

    return license_path.read_text(encoding="utf-8").strip()


def load_management_summary_text(repo_root: Path) -> str:
    readme_path = repo_root / "README.md"
    if not readme_path.exists():
        return ""

    lines = readme_path.read_text(encoding="utf-8").splitlines()
    summary_lines: list[str] = []
    in_summary = False

    for line in lines:
        if line.startswith("## Management Summary"):
            in_summary = True
            continue

        if in_summary and re.match(r"^##\s+", line):
            break

        if in_summary:
            summary_lines.append(line)

    return "\n".join(summary_lines).strip()


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
        r"\vspace*{0.10\textheight}",
        r"\makebox[\textwidth][c]{\includegraphics[width=0.22\textwidth]{assets/IAMT-logo.png}}\par",
        r"\vspace{1.2cm}",
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
    management_summary_text: str,
    changelog_text: str,
) -> list[str]:
    sections = [
        r"\pagestyle{dslbody}",
        r"\thispagestyle{dslbody}",
        "",
        r"\section*{Version Information}",
        "",
        f"- Version: {document_version}",
        f"- Status: {document_status}",
        f"- Publication date: {document_date}",
        "- Review baseline: Complete chapter set available for group review",
        "",
        "This PDF is an assembled publication view generated from the Markdown sources in the repository.",
        "",
    ]

    if management_summary_text:
        sections.extend(
            [
                r"\newpage",
                "",
                r"\section*{Management Summary}",
                "",
                management_summary_text.rstrip(),
                "",
                r"\newpage",
                "",
            ]
        )

    if changelog_text:
        sections.extend(
            [
                r"\section*{Change Log}",
                "",
                changelog_text.rstrip(),
                "",
            ]
        )

    sections.extend(
        [
            r"\newpage",
            r"\setcounter{tocdepth}{2}",
            r"\tableofcontents",
            r"\newpage",
        ]
    )

    return sections


def build_pdf_metadata(
    document_title: str,
    document_version: str,
    document_date: str,
) -> list[str]:
    return [
        "---",
        "lang: en",
        "header-includes:",
        "  - |",
        r"    \usepackage{fancyhdr}",
        "  - |",
        r"    \newcommand{\dslpdfpagestyle}{%",
        r"      \fancyhf{}%",
        rf"      \fancyhead[R]{{{document_title}}}%",
        rf"      \fancyfoot[L]{{Version {document_version}}}%",
        r"      \fancyfoot[C]{\thepage}%",
        rf"      \fancyfoot[R]{{{document_date}}}%",
        r"      \renewcommand{\headrulewidth}{0.4pt}%",
        r"      \renewcommand{\footrulewidth}{0.4pt}%",
        r"    }",
        "  - |",
        r"    \fancypagestyle{dslbody}{\dslpdfpagestyle}",
        "  - |",
        r"    \fancypagestyle{plain}{\dslpdfpagestyle}",
        "---",
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
    management_summary_text: str,
    changelog_text: str,
    license_text: str,
) -> int:
    sections = build_pdf_metadata(document_title, document_version, document_date)
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
            management_summary_text,
            changelog_text,
        )
    )
    included_count = 0

    for source_path in files:
        source_text = source_path.read_text(encoding="utf-8")
        source_text = rewrite_local_links(source_text, source_path, output_path)
        if source_path.name == "00-index.md":
            source_text = demote_following_headings(source_text, 1)
        source_text = prefix_first_heading(source_text, chapter_prefix_for_file(source_path))
        source_text = adjust_heading_levels(source_text, heading_offset_for_file(source_path))
        source_text = normalize_list_spacing(source_text)
        source_text = normalize_table_code_spans(source_text)

        relative_source = source_path.relative_to(repo_root).as_posix()
        if included_count > 0 and is_main_chapter_index(source_path, repo_root):
            sections.append(r"\newpage")
            sections.append("")
        elif included_count > 0 and is_subchapter_file(source_path, repo_root):
            sections.append(r"\vspace{0.6cm}")
            sections.append("")
        sections.append(f"<!-- Source: {relative_source} -->")
        sections.append(source_text.rstrip())
        sections.append("")
        included_count += 1

    if license_text:
        sections.extend(
            [
                r"\newpage",
                "",
                r"\section*{License}",
                "",
                "This publication is distributed under the Apache License, Version 2.0.",
                "The IAMT name, logo, and other trademarks are not licensed except as permitted by Section 6 of the Apache License, Version 2.0.",
                "",
                license_text.rstrip(),
                "",
            ]
        )

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
    changelog_text = load_changelog_text(repo_root)
    license_text = load_license_text(repo_root)
    management_summary_text = load_management_summary_text(repo_root)
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
            management_summary_text,
            changelog_text,
            license_text,
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