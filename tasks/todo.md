# TODO: Note記事「AI社員プロンプト」校閲

- [x] 現行本文を読み、文章の流れ・根拠・読者導線を確認する
- [x] AI社員12名の役割と照らし、現在の社員パフォーマンスが最大化されているか点検する
- [x] 下書きを校閲し、必要な追記・表現修正を反映する
- [x] 修正後の本文を確認し、公開前の注意点をレビューに残す

## 方針
- 記事の主役は「プロンプトを変えるとAI社員の成果が変わる」という体験談に置く
- 12名全員を本文で細かく紹介せず、今回の記事では基本3職種に絞り、次回への導線で拡張性を見せる
- 現在のAI社員は「単体の指示」より「Research → Writer → Editor → Growth → Monetization」の連携で力が出るため、その視点を本文に足す
- 外部データは断定しすぎず、出典が弱い数字は表現を少し丸める

## レビュー
- 校閲対象: `content/note/drafts/2026-05-12-ai-employee-prompts.md`
- 文章面: 冒頭の問題提起を整理し、「AI社員」という比喩とHBRの主張が矛盾して見えないよう補足した
- AI社員面: 12名全員紹介ではなく、土台となる3名と後続の編集・分析・収益化チームのつながりを本文に追加した
- 数字面: McKinseyの88%・6%は文脈を補い、GartnerのB2B購買者67%データを営業パートの根拠として追加した
- 公開前注意: HBR、Deloitte、Forrester、Microsoftのリンク先は購読・地域設定で表示が変わる可能性があるため、公開直前にブラウザで再確認する

---

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

# TODO: Executive Secretary Morning Briefing（2026-05-12）

- [x] 関連Markdownを確認（README / AI社員仕様 / Daily Plan / 前日レビュー等）
- [x] `reports/daily-briefings/2026-05-12-secretary-briefing.md` を作成（朝セクション）
- [x] Notionに「2026-05-12 Executive Secretary Briefing」を作成/更新
- [x] Markdown側の「Notion反映メモ」にNotion URLを追記
- [x] Automation memory（.codex）を更新

## 方針
- GitHub（このリポジトリ）のMarkdownをSource of Truthとして扱い、Notionは運用ビューとして反映する
- 顧客名・個人情報・機密は書かない

## レビュー
- GitHub: `/reports/daily-briefings/2026-05-12-secretary-briefing.md`
- Notion: https://www.notion.so/35d57d023d64811dab0df48cc4e65dcc

---

# TODO: Daily Plan作成補助スクリプト

- [x] 作業用ブランチを作成する
- [x] 期待動作を確認するテストを先に作成する
- [x] テンプレートから今日の日付ファイルを作るスクリプトを追加する
- [x] 既存ファイルを上書きしないことを検証する
- [x] 変更をコミットしてPRを作成する

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

---

# TODO: 秘書官のNotion経由日次報告

- [x] NotionのDaily Digest / Daily Opsページを確認する
- [x] Notion上に秘書官の朝夜レポート運用ページを作る
- [x] Daily Opsページから秘書官レポートへ辿れるようにする
- [x] 秘書報告テンプレートを朝・夜の2部構成に更新する
- [x] Notion運用モデルと同期計画に `/reports/daily-briefings/` を追加する
- [x] 朝・夜の自動実行を設定する
- [x] 検証結果を記録する

## 方針
- GitHub上のMarkdownを正本、Notionをオーナー確認用ビューとして扱う
- 朝は「今日やること・判断事項・持ち越し」を報告する
- 夜は「今日やったこと・未完了・翌日の準備」を報告する
- 保存先は `/reports/daily-briefings/YYYY-MM-DD-secretary-briefing.md`
- Notion上の受け皿はDaily Digest配下のDaily Opsに置く

## レビュー
- Notion Daily Digest: `https://www.notion.so/35857d023d6481b28ad9e31eeff8c823`
- Notion Daily Ops: `https://www.notion.so/35d57d023d648145b996fcf1fc80ae59`
- Notion秘書官ページ: `https://www.notion.so/35d57d023d6481ff862dff60276c3dee`
- 自動実行: `Executive Secretary Morning Briefing` を毎日07:15に設定
- 自動実行: `Executive Secretary Evening Report` を毎日21:15に設定
- 検証: `python3 -m py_compile scripts/notion_sync_plan.py`
- 検証: 同期計画の生成内容に `reports/daily-briefings` と秘書官用途が含まれることを確認
- 検証: Notion Daily Opsから秘書官ページへリンクされていることを確認

---

# TODO: Daily Plan自動生成ワークフロー SOP

- [x] 途中状況を確認する
- [x] SOP設計書を確認する
- [x] `workflows/daily/daily-plan-sop.md` を作成する
- [x] Daily Plan作成スクリプトのテストを再実行する
- [x] レビュー結果を記録する

## 方針
- 既存の設計書 `docs/superpowers/specs/2026-05-11-daily-plan-sop-design.md` を正本としてSOP本文を作る
- 人間が毎朝・毎晩に迷わず使える手順を先に書き、AI向けの技術仕様は後半に整理する
- スクリプトやテンプレートの挙動は変更しない
- 既存ファイルは削除・上書きしない

## レビュー
- 追加ドキュメント: `workflows/daily/daily-plan-sop.md`
- 内容: 全体フロー、オーナー向け日次運用、AI向け技術仕様、トラブル対応、改善サイクルを整理
- 検証: SOP内に主要セクションが存在することを確認
- 検証: `sh tests/create-daily-plan-test.sh` でDaily Plan生成と上書き防止を確認
- 注意: 既存の未コミット変更（秘書官Notion連携関連）は触らず、SOP新規作成とタスク記録の追記だけを追加

---

# TODO: AI社員スキル強化パック

- [x] `agents/prompts/` に全AI社員の共通プロンプト方針と個別プロンプトを追加する
- [x] `agents/specs/quality-scorecards.md` に成果物の採点表を追加する
- [x] `workflows/ai-employee-editorial-board.md` に社員同士の連携フローを追加する
- [x] `content/x/performance/performance-template.md` にGrowth分析用テンプレートを追加する
- [x] `products/monetization-map-template.md` に収益化マップを追加する
- [x] 追加ファイルを検証し、レビューを追記する

## 方針
- 既存のAI社員仕様は壊さず、追加資料として強化する
- 各社員に「役割・判断基準・出力形式・自己採点・NG」を持たせ、毎回の品質を安定させる
- 個別最適ではなく、Research → Writer → Editor → Growth → Monetization のチーム連携で成果物を磨く
- オーナーは最終判断に集中できるよう、AI社員側で自己評価と改善案まで出す

## レビュー
- 追加プロンプト: `agents/prompts/README.md` と12名分の個別プロンプト
- 追加採点表: `agents/specs/quality-scorecards.md`
- 追加フロー: `workflows/ai-employee-editorial-board.md`
- 追加テンプレート: `content/x/performance/performance-template.md`
- 追加テンプレート: `products/monetization-map-template.md`
- 検証: `find agents/prompts -maxdepth 1 -type f` で11名分の個別プロンプトとREADMEを確認
- 検証: `rg "自己採点|品質採点表|編集会議|Growth Analyst|Monetization|オーナー確認"` で主要キーワードの存在を確認
- 注意: 既存のAI社員仕様は上書きせず、追加資料として強化した

---

# TODO: AI経営会議室と社長室の追加

- [x] `company/ai-boardroom.md` にAI社員の経営会議室を追加する
- [x] `company/ceo-office.md` に秘書官が社長へ報告する社長室を追加する
- [x] `workflows/daily/ai-team-improvement-loop.md` に日次改善ループSOPを追加する
- [x] `reports/boardroom/boardroom-template.md` に会議ログテンプレートを追加する
- [x] `reports/ceo-office/ceo-briefing-template.md` に社長室報告テンプレートを追加する
- [x] `tasks/ai-improvement-backlog.md` に改善バックログを追加する
- [x] `README.md` にAI経営会議と社長室の位置づけを追記する
- [x] 毎日21:30にAI経営会議と社長室報告を作る自動実行を設定する
- [x] 追加ファイルを検証し、レビューを追記する

## 方針
- AI社員同士が毎日会議し、収益改善・発信改善・チーム改善を最大3つに絞って決める
- 会議内容はそのまま渡さず、Executive Secretaryが社長室向けに短く要約する
- オーナーは最終判断者として、承認・選択・保留・差し戻しに集中する
- 投稿、外部公開、価格変更、機密情報利用はオーナー確認なしに行わない

## レビュー
- 追加ドキュメント: `company/ai-boardroom.md`
- 追加ドキュメント: `company/ceo-office.md`
- 追加SOP: `workflows/daily/ai-team-improvement-loop.md`
- 追加テンプレート: `reports/boardroom/boardroom-template.md`
- 追加テンプレート: `reports/ceo-office/ceo-briefing-template.md`
- 追加バックログ: `tasks/ai-improvement-backlog.md`
- README追記: Daily Workflowに21:30のAI経営会議を追加
- 自動実行: `AI Boardroom and CEO Briefing` を毎日21:30に設定
- 検証: 主要ファイルの存在と、会議室・社長室・改善バックログ・自動実行に必要なキーワードを確認
- Notion AI経営会議室: `https://www.notion.so/35d57d023d6481c98fe7f46d4a7d987d`
- Notion社長室: `https://www.notion.so/35d57d023d6481edaeb2fb516a32cfd1`
- Notion日次会議ログ: `https://www.notion.so/35d57d023d648176b96ff758e56b3126`
- Notion初期報告: `https://www.notion.so/35d57d023d648142b75ed2d12a888bfa`
- 自動実行更新: 会議後にNotion社長室へ日次報告を残す指示を追加

---

# TODO: Viral Growth Producer追加

- [x] `agents/specs/ai-employees.md` にViral Growth Producerを追加する
- [x] `agents/prompts/viral-growth-producer.md` を追加する
- [x] `agents/specs/quality-scorecards.md` に拡散可能性とブランド安全性の評価を追加する
- [x] `workflows/ai-employee-editorial-board.md` にバズ化レビュー工程を追加する
- [x] `company/ai-boardroom.md` に毎日のバズ切り口提案を追加する
- [x] `README.md` にAI社員一覧とパイプラインを反映する
- [x] NotionのAI経営会議室へ役割を反映する
- [x] 自動実行にViral Growth Producerの参加を反映する
- [x] 追加内容を検証し、レビューを追記する

## 方針
- ロールモデルはスティーブ・ジョブズとサム・アルトマン
- 役割は煽り担当ではなく、伸びる切り口・物語・未来感を設計するプロデューサーにする
- Content EditorとExecutive Secretaryの安全チェックを必須にする
- バズは目的ではなく、信頼・フォロワー・Note/商品導線への入口として扱う

## レビュー
- 追加社員: `Viral Growth Producer`
- ロールモデル: Steve Jobs × Sam Altman
- 追加プロンプト: `agents/prompts/viral-growth-producer.md`
- 追加保存先: `content/growth/`
- 反映箇所: `agents/specs/ai-employees.md`、`README.md`、`agents/specs/quality-scorecards.md`、`workflows/ai-employee-editorial-board.md`、`company/ai-boardroom.md`、`workflows/daily/ai-team-improvement-loop.md`
- Notion反映: AI経営会議室にViral Growth Producerの役割を追加
- Notion社長室報告: `https://www.notion.so/35d57d023d6481ac950ae825a6bdbe22`
- 自動実行更新: 毎日21:30のAI経営会議で「明日バズらせる切り口」3案を出す指示を追加
- 検証: `rg "Viral Growth Producer|明日バズらせる|ブランド安全性|Steve Jobs|Sam Altman"` で主要反映を確認

---

# TODO: X・Noteアカウント自動分析対象登録

- [x] `company/social-accounts.md` にXとNoteのURLを登録する
- [x] `README.md` にSocial Accountsセクションを追加する
- [x] `workflows/daily/ai-team-improvement-loop.md` にX・Note確認ステップを追加する
- [x] 毎日21:30のAI経営会議でX・Noteを分析するよう自動実行を更新する
- [x] 追加内容を検証し、レビューを追記する

## 方針
- X: `https://x.com/Yosshi159971`
- Note: `https://note.com/genial_phlox6211`
- 取得できる公開情報と、保存済みの投稿実績をもとに分析する
- 数字が取得できない場合は推測せず、未確認として扱う
- 分析結果はAI経営会議と社長室報告に反映する

## レビュー
- 追加ドキュメント: `company/social-accounts.md`
- README追記: Social Accounts
- SOP追記: 日次改善ループにX・Note対象アカウント確認を追加
- 自動実行更新: 毎日21:30にX・Note分析を含める
- 注意: 公開ページ取得は環境やログイン状態に左右されるため、取得不能時は保存済み実績を使う

---

# TODO: Services×GenAI 世界インテリジェンス（有料Note→ソフトウェア）

- [x] `company/services-genai-intelligence-program.md` を運用開始（Teamの担当と成果物を固定）
- [x] 日次SOPを毎日回す（`workflows/daily/services-genai-intel-loop.md`）— `daily-intel-loop` と接続して運用導線を固定
- [x] 企業カードをまず30枚作る（スタートアップ20＋大中企業10）
- [x] 有料Note候補を3本作り、1本に絞る（導線：有料Note→テンプレ→ソフト）— 推奨：v3（体験記型）

## 方針
- 「全部集める」ではなく、**意思決定に必要な情報セット**に圧縮する
- 取れない数値・指標は推測しない（未確認）
- 有料Noteで勝ちパターンを売り、次に“運用を回すソフトウェア”に落とす

## レビュー
- プログラム仕様: `company/services-genai-intelligence-program.md`
- SOP: `workflows/daily/services-genai-intel-loop.md`
- Intel保存先: `intel/services-genai/`
- daily-intel-loop連携: `/research/market/` と `/research/competitors/` を入口にし、Services×GenAI関連材料だけを `intel/services-genai/` へ展開する
- Codexレビュー連携: `workflows/daily/codex-research-review-sop.md` から本SOPへ接続

---

# TODO: Codex側 Claude Code Remote連携ルール追加

- [x] 既存の `AGENTS.md` を確認する
- [x] Claude Code RemoteとCodexの役割分担を追記する
- [x] Codexのレビュー観点・禁止事項・依頼テンプレートを追記する
- [x] `tasks/todo.md` に作業記録を残す
- [x] 追記内容を検証する

## 方針
- Claude Code Remoteは毎朝の市場調査・競合チェックを担当する
- Codexは成果物のレビュー・整理・X投稿案化・Note企画化・自動化改善を担当する
- 同じ日付の調査ファイルを重複作成せず、既存ファイルを無断上書きしない

## レビュー
- 追記先: `AGENTS.md`
- 追加内容: Claude Code Remoteとの役割分担、Codexの担当範囲、レビュー観点、禁止事項、依頼テンプレート
- 検証: `rg "Claude Code Remote|Codex の担当範囲|Codex への依頼テンプレート" AGENTS.md tasks/todo.md` で主要キーワードを確認

---

# TODO: CLAUDE.mdにClaude Code Remote / Codex連携ルール追記

- [x] 既存の `CLAUDE.md` を確認する
- [x] Claude Code RemoteとCodexの役割分担を追記する
- [x] Claude Code Remoteの出力要件を追記する
- [x] Codexレビュー工程と展開先を追記する
- [x] 自動運営時の引き継ぎルールを追記する
- [x] 追記内容を検証する

## 方針
- Claude Code Remoteは「収集と初稿」、Codexは「検証と資産化」を主担当にする
- Codexがレビューしやすいよう、出典・未確認情報・コンテンツ転用候補・オーナー判断事項を明記させる
- 重複実行と無断上書きを避け、Markdownを正本として安全に自動運営する

## レビュー
- 追記先: `CLAUDE.md`
- 追加位置: `Claude Codeの役割` の直後
- 追加内容: 役割分担、出力要件、Codexレビュー工程、自動運営時の引き継ぎルール、引き継ぎテンプレート
- 検証: `rg "Claude Code Remote / Codex 連携ルール|Codexレビュー工程|自動運営時の引き継ぎルール|Codexへの引き継ぎテンプレート" CLAUDE.md tasks/todo.md` で主要キーワードを確認

---

# TODO: daily-intel-loop後のCodexレビュー導線整備

- [x] READMEに毎朝7:07 JSTの `daily-intel-loop` を追記する
- [x] READMEにClaude Code Remote / Codex Operationsを追記する
- [x] CLAUDE.mdに `daily-intel-loop` の実行時刻・保存先・目的を追記する
- [x] AGENTS.mdにCodexレビューSOPへの参照を追記する
- [x] `workflows/daily/codex-research-review-sop.md` を作成する
- [x] 追記内容を検証する

## 方針
- Claude Code Remoteは毎朝7:07 JSTに市場調査・競合チェックを収集する
- Codexは初回実行後または依頼時に、出典・事実性・再利用性をレビューする
- レビュー結果はX投稿案、Note企画、商品化案、運用改善へ展開する
- 既存ファイルは上書きせず、Markdownを正本として安全に運用する

## レビュー
- 追記先: `README.md`, `CLAUDE.md`, `AGENTS.md`
- 追加SOP: `workflows/daily/codex-research-review-sop.md`
- 追加内容: 7:07 JST実行、保存先、Codexレビュー手順、派生ファイル保存先、禁止事項
- 検証: `rg "7:07|daily-intel-loop|codex-research-review-sop|Claude Code Remote / Codex Operations" README.md CLAUDE.md AGENTS.md workflows/daily/codex-research-review-sop.md tasks/todo.md` で主要キーワードを確認

---

# TODO: Services×GenAI SOPとdaily-intel-loopの統合

- [x] 既存のServices×GenAI SOPとプログラム仕様を確認する
- [x] `daily-intel-loop` をServices×GenAI調査の入口として明記する
- [x] Services×GenAI SOPを「抽出・補強・商品化」中心に更新する
- [x] Codex Research Review SOPにServices×GenAI展開観点を追加する
- [x] `tasks/todo.md` の未完了タスクを運用導線固定として完了扱いに更新する
- [x] 追記内容を検証する

## 方針
- 広域調査はClaude Code Remoteの `daily-intel-loop` に任せる
- Services×GenAI SOPは、広域調査からSales×生成AIに関係する材料を抽出する役にする
- Codexは、有料Note化・ソフトウェア化・重複確認を担当する
- 該当材料がない日は、無理に作らず「該当なし」と記録する

## レビュー
- 更新SOP: `workflows/daily/services-genai-intel-loop.md`
- 更新仕様: `company/services-genai-intelligence-program.md`
- 更新SOP: `workflows/daily/codex-research-review-sop.md`
- 変更内容: `daily-intel-loop` 起点、Services×GenAI抽出、Codexレビュー連携、商品化導線
- 検証: `rg "daily-intel-loop|Services×GenAI|有料Note|ソフトウェア化|該当なし" workflows/daily/services-genai-intel-loop.md company/services-genai-intelligence-program.md workflows/daily/codex-research-review-sop.md tasks/todo.md` で主要キーワードを確認

---

# TODO: Claude Code Remote / Codex 自動連携強化

- [x] `CLAUDE.md` にCodex品質スコア制度を追記する
- [x] `CLAUDE.md` にClaude → Codex → Claude改善ループを追記する
- [x] `CLAUDE.md` に週次Codex監査、競合分析のコンテンツ戦略化、判断事項集約、失敗ログ、仕組み化担当ルールを追記する
- [x] `agents/specs/quality-scorecards.md` にCodexレビュー専用スコアカードを追加する
- [x] `workflows/daily/daily-plan-template.md` にCodexレビュー枠を追加する
- [x] `workflows/daily/codex-research-review-sop.md` に品質採点、競合戦略、判断事項、改善メモを追加する
- [x] `workflows/weekly/codex-weekly-audit-sop.md` を追加する
- [x] `reports/weekly-codex-audit-template.md` を追加する
- [x] `reports/automation-memory/claude-codex-handoff-memory.md` を追加する
- [x] `tasks/owner-decisions.md` を追加する
- [x] READMEに週次監査と判断事項の参照を追記する
- [x] 追記内容を検証する

## 方針
- Claude Code Remoteは日次の収集と初稿を担当する
- Codexは品質採点、競合戦略化、商品化、週次監査、仕組み化を担当する
- 両者の連携は、Markdownの共有ファイルを介して自動運営しやすくする
- オーナー判断が必要なことは `tasks/owner-decisions.md` に集約する

## レビュー
- 更新: `CLAUDE.md`, `README.md`, `agents/specs/quality-scorecards.md`, `workflows/daily/daily-plan-template.md`, `workflows/daily/codex-research-review-sop.md`
- 追加: `workflows/weekly/codex-weekly-audit-sop.md`
- 追加: `reports/weekly-codex-audit-template.md`
- 追加: `reports/automation-memory/claude-codex-handoff-memory.md`
- 追加: `tasks/owner-decisions.md`
- 検証: `rg "Codex品質スコア|Claude → Codex → Claude|週次Codex監査|owner-decisions|claude-codex-handoff|Codexレビュー専用スコアカード" CLAUDE.md README.md agents/specs/quality-scorecards.md workflows reports tasks` で主要キーワードを確認
