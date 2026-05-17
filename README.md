# AI Company OS

> 外資IT営業職が運営する、AI-Nativeな一人会社の事業運営システム。

---

## Mission

AIを社員として活用し、コンテンツ・知識・収益を複利で積み上げる。
人間はビジネス判断に集中し、実行はAIが担う。

---

## 事業の柱

### 1. X運用
企業AI・SaaS・GTM領域の専門知見を日本語で発信。
フォロワーを資産として積み上げ、Note・セミナー・顧問契約へ転換する。

### 2. Note収益化
X投稿から派生した深掘り記事を有料・無料で展開。
外資IT営業のリアル、AI活用術、戦略フレームワークを製品化する。

### 3. AI Agent Business構築
Claude・ChatGPT・Codexを社員として定義し、繰り返し業務を自動化。
ワークフローを資産として蓄積し、外部販売・受注の土台にする。

### 4. 外資IT営業知見の資産化
SAP・Salesforce・ServiceNow等の商談・提案・交渉ノウハウを体系化。
`/memory/sales-knowledge/` に蓄積し、コンテンツ・コンサルの源泉とする。

---

## AI社員一覧

| 名前 | 役割 | 主な担当 |
|---|---|---|
| Content Writer | X投稿・Note記事の起草 | `/content/` |
| Research Analyst | 競合・市場・AI動向の調査 | `/research/` |
| Sales Strategist | 営業ナレッジの整理・体系化 | `/memory/sales-knowledge/` |
| Workflow Builder | SOP・自動化フローの設計 | `/workflows/` |
| Weekly Reporter | 週次レビューの作成 | `/reports/` |
| Executive Secretary | 全AI社員の活動把握・日次報告 | `/reports/daily-briefings/` |
| Visual Designer | 投稿用画像のデザイン仕様・生成プロンプト作成 | `/content/design/` |
| Growth Analyst | X・Noteのパフォーマンス分析・改善提案 | `/reports/growth/` |
| Monetization Strategist | 有料コンテンツ・ワークフロー販売の設計 | `/products/` |
| Content Editor | X投稿・Note記事の品質チェック・改善 | `/content/` |
| Market Researcher | グローバルAI活用・産業動向の収集・要約 | `/research/market/` |
| Viral Growth Producer | X・Noteを拡散されやすい切り口へ変換 | `/content/growth/` |

---

## Daily Workflow

```
07:00  Daily Plan作成（Claude）
       └─ 当日のX投稿・リサーチ・タスクを確認
07:07  daily-intel-loop（Claude Code Remote）
       └─ 市場調査・競合チェックを /research/market/ と /research/competitors/ に保存
07:15  秘書官による朝のブリーフィング
       └─ 今日の優先事項・判断事項・未完了タスクを整理
08:00  X投稿（下書き確認 → 人間承認 → 投稿）
12:00  リサーチ・インサイト収集（Claude）
       └─ /memory/daily-insights/ に保存
21:00  Daily Review作成（Claude）
       └─ 成果・学び・翌日タスクを記録
21:15  秘書官による日次報告
       └─ 全AI社員の活動・成果物・未完了タスクを /reports/daily-briefings/ に記録
21:30  AI経営会議
       └─ 収益改善・チーム改善・社長判断事項を /reports/boardroom/ と /reports/ceo-office/ に記録
```

---

## Claude Code Remote / Codex Operations

Claude Code Remoteは毎朝7:07 JSTに `daily-intel-loop` を実行し、市場調査と競合チェックの初稿を作る。
Codexはその成果物をレビューし、X投稿案・Note企画・商品化アイデア・自動化改善へ展開する。

| 担当 | 主な役割 | 保存先 |
|---|---|---|
| Claude Code Remote | 市場調査・競合チェックの収集と初稿作成 | `/research/market/`, `/research/competitors/` |
| Codex | 出典・事実性・再利用性のレビュー | `/reports/growth/`, `/tasks/todo.md` |
| Codex | X投稿案・Note企画への変換 | `/content/x/drafts/`, `/content/note/research/` |
| Codex | 繰り返し作業のSOP化・自動化改善 | `/workflows/`, `/scripts/` |
| Codex | 週次監査・オーナー判断事項の整理 | `/reports/YYYY-MM-DD-weekly-codex-audit.md`, `/tasks/owner-decisions.md` |

運用ルール：
- Claude Code Remoteは、出典URL、未確認情報、事実と解釈の分離、`Codexレビュー用メモ`、`コンテンツ転用候補`、オーナー判断事項を必ず残す
- Codexは、同じ日付・同じテーマの調査を重複実行しない
- Codexは、Claude Code Remoteが作成した同日ファイルを無断で上書きしない
- 公開・投稿・送信は、どちらのAIでもオーナー承認後のみ行う
- Codexレビュー手順は `/workflows/daily/codex-research-review-sop.md` を参照する
- 週次監査は `/workflows/weekly/codex-weekly-audit-sop.md` を参照する
- 判断事項は `/tasks/owner-decisions.md` に集約する

---

## AI Executive Board Room / CEO Office

AI社員は毎日、`AI Executive Board Room` で収益改善とチーム改善を議論する。
会議内容はExecutive Secretaryが整理し、社長室である `CEO Office` にオーナー向けの要約として報告する。

| 場所 | 用途 | 保存先 |
|---|---|---|
| AI Executive Board Room | AI社員同士の経営会議 | `/company/ai-boardroom.md` |
| CEO Office | 秘書官による社長向け報告 | `/company/ceo-office.md` |
| 会議ログ | 毎日の議論・決定事項 | `/reports/boardroom/` |
| 社長室報告 | オーナー判断用の要約 | `/reports/ceo-office/` |
| 改善バックログ | 毎日の改善案と実行状況 | `/tasks/ai-improvement-backlog.md` |

---

## Social Accounts

| 媒体 | URL | 用途 |
|---|---|---|
| X | https://x.com/Yosshi159971 | 認知拡大・Note送客 |
| Note | https://note.com/genial_phlox6211 | 信頼形成・収益化 |

毎日のAI経営会議で、Growth AnalystとViral Growth Producerが投稿・記事の反応と翌日の伸ばす切り口を確認する。
詳細は `/company/social-accounts.md` を参照。

---

## Weekly Workflow

```
月曜  週次目標設定・コンテンツカレンダー確認
水曜  Note記事の企画・リサーチ完了
金曜  Note記事の執筆・下書き完了
日曜  Weekly Review作成 → /reports/ に保存
      次週のX投稿スケジュール確定
```

---

## Note記事制作 Pipeline

```
1. テーマ選定    X反響 / リサーチ / 営業経験から抽出
2. リサーチ      /content/note/research/ に素材収集
3. 構成設計      見出し・章立て・CTA設計
4. 執筆          /content/note/drafts/ に下書き保存
5. バズ化設計    タイトル・導入・SNS告知の切り口を強化
6. 編集・校正    Claude によるトーン・構造・安全性チェック
7. 人間確認      オーナーがレビュー・修正
8. 公開          /content/note/published/ にアーカイブ
```

---

## X投稿 Pipeline

```
1. ネタ収集      daily-insights / 営業経験 / ニュース
2. 下書き作成    /content/x/drafts/ に保存
3. バズ化設計    Viral Growth Producerがフック・切り口を強化
4. 人間確認      トーン・事実確認
5. 投稿          投稿後パフォーマンスを /content/x/performance/ に記録
```

---

## 競合分析 Workflow

```
1. 対象選定      X・Note上の競合アカウントを特定
2. データ収集    /research/competitors/ にプロフィール・投稿傾向を記録
3. 分析          差別化ポイント・参考要素を抽出
4. 戦略反映      /company/ の戦略ドキュメントに反映
```

---

## Notion Integration

GitHubをSource of Truthとし、Notionは日々の運用を見やすくするためのビューとして使う。
Notion API連携はまだ実装せず、まずはMarkdownの同期計画を `reports/notion-sync-plan.md` に出力する。

| Notion Area | 用途 | GitHub上の対象 |
|---|---|---|
| Daily Ops | Daily Plan、Daily Review、秘書官の日次報告、日次実行状況の確認 | `/workflows/daily/`, `/reports/`, `/reports/daily-briefings/` |
| Content Pipeline | X投稿・Note記事の下書き管理 | `/content/x/drafts/`, `/content/note/drafts/` |
| Sales Knowledge | 営業ナレッジの検索・再利用 | `/memory/sales-knowledge/` |
| KPI Dashboard | 週次・月次の成果確認 | `/reports/` |

運用ルール：
- APIキーやトークンはRepositoryに追加しない
- Notionへの自動投稿・自動公開は行わない
- Notion上の編集は正本にせず、必要な変更はMarkdownへ戻す
- 同期計画は `python3 scripts/notion_sync_plan.py` で生成する
- 秘書官はDaily Ops上で、朝に「今日やること」、夜に「今日やったこと・翌日の準備」を報告する

詳細は `/company/notion-integration.md` を参照。

---

## Repository構成

```
ai-company-os/
├── README.md              # この説明書
├── CLAUDE.md              # Claude Code実行指示書
│
├── company/               # 事業戦略・ポジショニング・OKR
│
├── agents/
│   ├── prompts/           # AI社員のシステムプロンプト
│   ├── specs/             # AI社員の定義・役割仕様
│   └── workflows/         # エージェント別ワークフロー
│
├── content/
│   ├── x/
│   │   ├── drafts/        # X投稿下書き
│   │   └── performance/   # 投稿パフォーマンス記録
│   └── note/
│       ├── research/      # 記事リサーチ素材
│       ├── drafts/        # 記事下書き
│       └── published/     # 公開済み記事アーカイブ
│
├── memory/
│   ├── sales-knowledge/   # 外資IT営業ナレッジ
│   └── daily-insights/    # 日次インサイト蓄積
│
├── workflows/
│   ├── daily/             # デイリータスクSOP
│   └── weekly/            # ウィークリータスクSOP
│
├── reports/               # 週次・月次レビュー
│
├── research/
│   └── competitors/       # 競合分析データ
│
├── products/              # 販売・配布コンテンツ製品
│
└── archive/               # 旧バージョン・参考資料
```

---

## KPI

| 指標 | 現在 | 目標（90日） |
|---|---|---|
| Xフォロワー数 | - | +500 |
| Note記事本数 | 0 | 12本 |
| Note収益 | ¥0 | ¥30,000/月 |
| AIワークフロー数 | 0 | 10本 |
| 営業ナレッジ記事 | 0 | 20本 |

---

## 30日計画

| 週 | 目標 | 成果物 |
|---|---|---|
| Week 1 | 基盤構築 | ワークフロー設計・AI社員定義・Daily習慣確立 |
| Week 2 | コンテンツ開始 | X毎日投稿・Note第1本目公開 |
| Week 3 | 知識資産化 | 営業ナレッジ10本・競合分析完了 |
| Week 4 | 収益化設計 | 有料Note設計・ワークフロー外部向け整理 |

---

## Stack

| Tool | Role |
|---|---|
| Claude Code | 主力AIアシスタント・実行エンジン |
| ChatGPT | アイデア発散・下書き補助 |
| Codex | 市場調査レビュー・資産化・改善ループ |
| GitHub | バージョン管理・知識資産管理 |
| Notion | Daily Ops・Content Pipeline・Sales Knowledge・KPI Dashboardの運用ビュー |
