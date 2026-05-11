# Notion Sync Plan

Generated: 2026-05-11

## Operating Policy

- GitHub is the Source of Truth.
- Notion is used only as an operating view for Daily Ops, Content Pipeline, Sales Knowledge, and KPI Dashboard.
- This plan does not connect to the Notion API.
- Do not add API keys, tokens, customer secrets, or confidential internal information.
- Do not auto-post or auto-publish content from this plan.

## Sync Targets

| Notion Area | Purpose | GitHub Directory | Files |
|---|---|---|---:|
| Daily Ops | Daily Plan、Daily Review、日次実行状況の確認 | `workflows/daily/` | 2 |
| Daily Ops / KPI Dashboard | 週次・月次レビュー、KPI、改善メモの確認 | `reports/` | 0 |
| Content Pipeline | X投稿下書きの進行状況確認 | `content/x/drafts/` | 1 |
| Content Pipeline | Note記事下書きの進行状況確認 | `content/note/drafts/` | 0 |
| Sales Knowledge | 営業ナレッジの検索・再利用 | `memory/sales-knowledge/` | 1 |

## File Mapping

### Daily Ops: `workflows/daily/`

Purpose: Daily Plan、Daily Review、日次実行状況の確認

| File | Suggested Notion Use |
|---|---|
| `workflows/daily/2026-05-11-daily-plan.md` | Daily Plan、Daily Review、日次実行状況の確認 |
| `workflows/daily/daily-plan-template.md` | Daily Plan、Daily Review、日次実行状況の確認 |

### Daily Ops / KPI Dashboard: `reports/`

Purpose: 週次・月次レビュー、KPI、改善メモの確認

No Markdown files found yet.

### Content Pipeline: `content/x/drafts/`

Purpose: X投稿下書きの進行状況確認

| File | Suggested Notion Use |
|---|---|
| `content/x/drafts/2026-05-11-ai-agent.md` | X投稿下書きの進行状況確認 |

### Content Pipeline: `content/note/drafts/`

Purpose: Note記事下書きの進行状況確認

No Markdown files found yet.

### Sales Knowledge: `memory/sales-knowledge/`

Purpose: 営業ナレッジの検索・再利用

| File | Suggested Notion Use |
|---|---|
| `memory/sales-knowledge/saas-competitive-differentiation.md` | 営業ナレッジの検索・再利用 |

## Next Manual Steps

1. Review this plan before creating any Notion database or page.
2. Create Notion views manually only for the areas that are useful now.
3. Keep edits in GitHub Markdown first, then mirror the useful view into Notion.
4. Re-run this script when new Markdown files are added.

## Out of Scope

- Notion API integration
- API keys or tokens
- Automatic Notion page creation
- Automatic posting or publishing
