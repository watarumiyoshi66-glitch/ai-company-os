#!/usr/bin/env python3
"""Generate a Markdown-only Notion sync plan.

This script does not call the Notion API. It only reads local Markdown files
and writes reports/notion-sync-plan.md as an operating plan.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


OUTPUT_PATH = Path("reports/notion-sync-plan.md")


@dataclass(frozen=True)
class SyncTarget:
    area: str
    purpose: str
    directory: Path


SYNC_TARGETS = (
    SyncTarget(
        area="Daily Ops",
        purpose="Daily Plan、Daily Review、日次実行状況の確認",
        directory=Path("workflows/daily"),
    ),
    SyncTarget(
        area="Daily Ops / KPI Dashboard",
        purpose="週次・月次レビュー、KPI、改善メモの確認",
        directory=Path("reports"),
    ),
    SyncTarget(
        area="Content Pipeline",
        purpose="X投稿下書きの進行状況確認",
        directory=Path("content/x/drafts"),
    ),
    SyncTarget(
        area="Content Pipeline",
        purpose="Note記事下書きの進行状況確認",
        directory=Path("content/note/drafts"),
    ),
    SyncTarget(
        area="Sales Knowledge",
        purpose="営業ナレッジの検索・再利用",
        directory=Path("memory/sales-knowledge"),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate reports/notion-sync-plan.md from local Markdown files."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite reports/notion-sync-plan.md if it already exists.",
    )
    return parser.parse_args()


def find_markdown_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []

    files = [
        path
        for path in directory.rglob("*.md")
        if path.is_file() and path.name != OUTPUT_PATH.name
    ]
    return sorted(files, key=lambda path: path.as_posix())


def build_report() -> str:
    lines = [
        "# Notion Sync Plan",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Operating Policy",
        "",
        "- GitHub is the Source of Truth.",
        "- Notion is used only as an operating view for Daily Ops, Content Pipeline, Sales Knowledge, and KPI Dashboard.",
        "- This plan does not connect to the Notion API.",
        "- Do not add API keys, tokens, customer secrets, or confidential internal information.",
        "- Do not auto-post or auto-publish content from this plan.",
        "",
        "## Sync Targets",
        "",
        "| Notion Area | Purpose | GitHub Directory | Files |",
        "|---|---|---|---:|",
    ]

    target_files: list[tuple[SyncTarget, list[Path]]] = []
    for target in SYNC_TARGETS:
        files = find_markdown_files(target.directory)
        target_files.append((target, files))
        lines.append(
            f"| {target.area} | {target.purpose} | `{target.directory.as_posix()}/` | {len(files)} |"
        )

    lines.extend(["", "## File Mapping", ""])

    for target, files in target_files:
        lines.extend(
            [
                f"### {target.area}: `{target.directory.as_posix()}/`",
                "",
                f"Purpose: {target.purpose}",
                "",
            ]
        )
        if files:
            lines.append("| File | Suggested Notion Use |")
            lines.append("|---|---|")
            for path in files:
                lines.append(f"| `{path.as_posix()}` | {target.purpose} |")
            lines.append("")
        else:
            lines.extend(["No Markdown files found yet.", ""])

    lines.extend(
        [
            "## Next Manual Steps",
            "",
            "1. Review this plan before creating any Notion database or page.",
            "2. Create Notion views manually only for the areas that are useful now.",
            "3. Keep edits in GitHub Markdown first, then mirror the useful view into Notion.",
            "4. Re-run this script when new Markdown files are added.",
            "",
            "## Out of Scope",
            "",
            "- Notion API integration",
            "- API keys or tokens",
            "- Automatic Notion page creation",
            "- Automatic posting or publishing",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> int:
    args = parse_args()

    if OUTPUT_PATH.exists() and not args.force:
        print(
            f"{OUTPUT_PATH} already exists. Re-run with --force to overwrite.",
            file=sys.stderr,
        )
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_report(), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
