# TODO: HONDA向け役員資料リバイス

- [x] 元PPTXの構成と本文を抽出する
- [x] HONDA向けの役員ストーリーへ再設計する
- [x] 視覚要素を増やした改訂版PPTXを作成する
- [x] プレビュー画像で見え方を確認する
- [x] 最終ファイルとレビュー内容をまとめる

## 方針
- 元資料は業界全般の説明が中心だったため、Honda固有の経営論点へ再構成する
- 役員向けに、詳細説明よりも「意思決定すべき論点」「投資優先順位」「90日アクション」を前面に出す
- 上書きせず、改訂版PPTXを別ファイルとして作成する

## レビュー
- 出力先: `/Users/miyoshiwataru/Documents/Claude/Projects/PPT作成支援（ビジネス）/HONDA役員向け_IBM提案_2026_改訂版.pptx`
- スライド数: 12枚
- 確認内容: PPTXの破損チェック、スライド数確認、表紙・ASIMO OS関連テキストの存在確認
- 注意: この環境ではQuick Lookによる画像プレビュー生成がサンドボックス制約で失敗したため、PowerPoint上で最終の見た目確認を推奨

---

# TODO: Daily Plan作成補助スクリプト

- [x] 作業用ブランチを作成する
- [x] 期待動作を確認するテストを先に作成する
- [x] テンプレートから今日の日付ファイルを作るスクリプトを追加する
- [x] 既存ファイルを上書きしないことを検証する
- [ ] 変更をコミットしてPRを作成する

## 方針
- `workflows/daily/daily-plan-template.md` を元に、`workflows/daily/YYYY-MM-DD-daily-plan.md` を作成する
- 既に同名ファイルがある場合は停止し、内容を変更しない
- 日付の差し替えはテンプレート内の `YYYY-MM-DD` を対象にする
- 追加ライブラリなしで動くシェルスクリプトにする

## レビュー
- 追加スクリプト: `scripts/create-daily-plan.sh`
- 追加テスト: `tests/create-daily-plan-test.sh`
- 自動テスト: `sh tests/create-daily-plan-test.sh` で作成と上書き防止を確認
- 手動確認: `./scripts/create-daily-plan.sh` は既存の `workflows/daily/2026-05-11-daily-plan.md` を検知して停止

---

# TODO: Notion連携の運用モデル追加

- [x] `company/notion-integration.md` を作成する
- [x] `scripts/notion_sync_plan.py` を作成する
- [x] `README.md` に Notion Integration セクションを追加する
- [x] `CLAUDE.md` に Notion Integration Rule を追加する
- [x] `reports/notion-sync-plan.md` の生成を検証する
- [x] 変更をコミットする

## 方針
- GitHubをSource of Truthとして扱い、NotionはDaily Ops / Content Pipeline / Sales Knowledge / KPI Dashboardの閲覧・運用ビューに限定する
- Notion API連携、APIキー、トークン、自動投稿、自動公開は追加しない
- まずはMarkdownファイルを読み取り、`reports/notion-sync-plan.md` に同期計画を出す
- 既存の同期計画は `--force` がない限り上書きしない

## レビュー
- 追加ドキュメント: `company/notion-integration.md`
- 追加スクリプト: `scripts/notion_sync_plan.py`
- 生成レポート: `reports/notion-sync-plan.md`
- 検証: `python3 -m py_compile scripts/notion_sync_plan.py`
- 検証: `python3 scripts/notion_sync_plan.py` で同期計画を生成
- 検証: `python3 scripts/notion_sync_plan.py` の再実行で上書き防止を確認
- 確認: APIキーやトークンの実値は追加していない

---

# TODO: Executive Secretary追加

- [x] `agents/specs/ai-employees.md` に秘書官を追加する
- [x] `README.md` のAI社員一覧とDaily Workflowに秘書官を反映する
- [x] 毎日の秘書報告テンプレートを追加する
- [x] 差分を確認し、役割・保存先・報告内容が一貫しているか検証する

## 方針
- 秘書官は「全AI社員の活動を横断して把握し、毎日オーナーに報告する役」にする
- 報告は事実・未完了・判断事項を分け、ビジネス判断に使える形にする
- 保存先は `/reports/daily-briefings/` に統一する

## レビュー
- 追加社員: `Executive Secretary`
- 追加テンプレート: `reports/daily-briefings/secretary-briefing-template.md`
- 反映箇所: `agents/specs/ai-employees.md`、`README.md`
- 確認: 社員一覧、Daily Workflow、保存先、報告項目が `/reports/daily-briefings/` で一貫している
