# Notion Integration Operating Model

## Purpose

Notionは、AI Company OSの日々の運用を見やすくするためのワークスペースとして使う。
GitHubに保存されたMarkdownを正本とし、NotionはDaily Ops、Content Pipeline、Sales Knowledge、KPI Dashboardのビューとして扱う。

## Source of Truth

このRepositoryのGitHub管理ファイルを唯一のSource of Truthとする。

- 戦略、ワークフロー、コンテンツ、営業ナレッジ、レポートはGitHubに保存する
- Notion上で編集した内容は、そのまま正本にしない
- Notionで得た気づきや修正は、Markdownに戻してから反映する
- Notion API連携は現時点では実装しない

## Notionの役割

| Notion Area | 目的 | GitHub上の対象 |
|---|---|---|
| Daily Ops | 今日の計画、レビュー、実行状況を見る | `workflows/daily/`, `reports/` |
| Content Pipeline | X投稿とNote記事の下書き状況を見る | `content/x/drafts/`, `content/note/drafts/` |
| Sales Knowledge | 営業ナレッジを検索・参照しやすくする | `memory/sales-knowledge/` |
| KPI Dashboard | 週次・月次の成果や改善点を見る | `reports/` |

## Operating Rules

1. GitHubのMarkdownを先に更新する
2. Notionへは公開・投稿ではなく、運用確認用に反映する
3. 自動投稿・自動公開は行わない
4. APIキー、トークン、顧客情報、社内機密は保存しない
5. Notion連携の初期段階では、同期計画Markdownのみを生成する

## Sync Planning

同期計画は `scripts/notion_sync_plan.py` で作成する。
出力先は `reports/notion-sync-plan.md` とする。

この計画には、Notionに反映したいMarkdownファイル、想定するNotion Area、運用上の用途をまとめる。
既存の `reports/notion-sync-plan.md` は、`--force` を付けた場合のみ上書きできる。

## Current Scope

現時点で行うこと：

- 対象フォルダのMarkdownを読み取る
- Notion Areaごとに同期候補を整理する
- `reports/notion-sync-plan.md` に計画を書き出す

現時点で行わないこと：

- Notion APIへの接続
- APIキーやトークンの追加
- Notionへの自動作成・自動更新
- X、Note、その他外部サービスへの自動投稿・自動公開
