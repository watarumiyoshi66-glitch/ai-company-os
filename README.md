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

---

## Daily Workflow

```
07:00  Daily Plan作成（Claude）
       └─ 当日のX投稿・リサーチ・タスクを確認
08:00  X投稿（下書き確認 → 人間承認 → 投稿）
12:00  リサーチ・インサイト収集（Claude）
       └─ /memory/daily-insights/ に保存
21:00  Daily Review作成（Claude）
       └─ 成果・学び・翌日タスクを記録
```

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
5. 編集・校正    Claude によるトーン・構造チェック
6. 人間確認      オーナーがレビュー・修正
7. 公開          /content/note/published/ にアーカイブ
```

---

## X投稿 Pipeline

```
1. ネタ収集      daily-insights / 営業経験 / ニュース
2. 下書き作成    /content/x/drafts/ に保存
3. 人間確認      トーン・事実確認
4. 投稿          投稿後パフォーマンスを /content/x/performance/ に記録
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
| Codex | 自動化・スクリプト |
| GitHub | バージョン管理・知識資産管理 |
