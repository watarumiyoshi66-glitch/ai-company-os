# Daily Plan SOP文書 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `workflows/daily/daily-plan-sop.md` に Daily Plan自動生成ワークフローのSOP文書を作成する。

**Architecture:** 設計仕様 `docs/superpowers/specs/2026-05-11-daily-plan-sop-design.md` に基づき、5セクション構成（全体フロー・人間向け手順・AI技術仕様・トラブルシューティング・改善サイクル）の1ファイルを新規作成する。既存ファイルへの変更はない。

**Tech Stack:** Markdown、シェルスクリプト（参照のみ）

---

### Task 1: SOP文書を作成する

**Files:**
- Create: `workflows/daily/daily-plan-sop.md`

- [ ] **Step 1: 既存ファイルがないことを確認する**

```bash
ls workflows/daily/
```

Expected: `daily-plan-template.md` と `2026-05-11-daily-plan.md` のみ存在。`daily-plan-sop.md` は存在しない。

- [ ] **Step 2: SOP文書を作成する**

`workflows/daily/daily-plan-sop.md` を以下の内容で新規作成する：

```markdown
# Daily Plan 自動生成ワークフロー SOP

> 対象読者：オーナー（日次運用）、AIエージェント（設定変更・障害対応時のみ参照）
> 最終更新：2026-05-11

---

## Section 1: 全体フロー

### ワークフロー概要

```
[Phase 1] 自動生成     07:00 JST
  Codex CCR が create-daily-plan.sh を実行
  → workflows/daily/YYYY-MM-DD-daily-plan.md を生成

[Phase 2] 朝の記入     07:00〜08:00
  オーナーがファイルを開き、今日の目標・X投稿テーマ・フォーカスを記入

[Phase 3] コンテンツ実行 08:00〜12:00
  X投稿（下書き確認→承認→投稿）
  リサーチ・インサイト収集

[Phase 4] 夜のレビュー  21:00〜
  同ファイルの Daily Review セクションを記入
  → memory/daily-insights/YYYY-MM-DD.md に保存

[Phase 5] 障害・例外処理
  スクリプト失敗時・ファイル重複時の手動対応
```

### 分岐判断基準

| 状況 | 動作 | 対処 |
|---|---|---|
| ファイルが既に存在する | スクリプト停止（上書きしない） | 既存ファイルをそのまま使う |
| テンプレートが見つからない | スクリプトエラー終了 | Section 4-A参照 |
| CCRが動かなかった | ファイル未生成 | Section 4-C参照 |

---

## Section 2: 人間向け日次運用手順

### 朝のルーティン（07:00〜08:00）

**07:00 — 生成確認**

`workflows/daily/YYYY-MM-DD-daily-plan.md` が存在するか確認する。
存在しない場合は手動で実行する：

```bash
sh scripts/create-daily-plan.sh
```

**07:05 — 必須記入項目**

| 項目 | 記入内容 |
|---|---|
| 今日のフォーカス | 1つだけ選ぶ。複数書かない |
| 今日の目標 | 最大3つ。それ以上は「その他タスク」へ |
| X投稿テーマ | テーマ＋形式（インサイト型/問い型/体験型）を決める |

**07:15 — 該当日のみ記入**

| 項目 | 条件 |
|---|---|
| Note記事ステータス | 執筆・編集・確認待ち等を更新する |
| 営業ナレッジのトピック | その日に記録したい商談・経験がある場合のみ |

### 夜のルーティン（21:00〜）

**21:00 — Daily Review記入（同ファイルの下半分）**

| 項目 | 記入内容 |
|---|---|
| 今日の成果 | 完了したタスク・公開したコンテンツ |
| 学んだこと・インサイト | 気づき・発見 |
| うまくいったこと | 再現したいアクション |
| 改善したいこと | 次回変えること |
| 明日に持ち越すタスク | チェックボックス形式で記入 |
| 明日のフォーカス | 1つだけ |

**21:15 — インサイト保存**

重要な気づきを `memory/daily-insights/YYYY-MM-DD.md` に転記する。

### 判断ルール

- 目標は最大3つ。超える場合は「その他タスク」に移す
- X投稿は必ず下書き確認後に投稿する（自動投稿禁止）
- Daily Reviewは翌朝に書かない。その日のうちに完結させる

---

## Section 3: AI技術仕様

> このセクションはAIエージェントがテンプレート更新・障害対応時に参照する。通常運用では不要。

### スクリプト仕様

| 項目 | 値 |
|---|---|
| ファイル | `scripts/create-daily-plan.sh` |
| テンプレート | `workflows/daily/daily-plan-template.md` |
| 出力先 | `workflows/daily/YYYY-MM-DD-daily-plan.md` |
| 実行コマンド | `sh scripts/create-daily-plan.sh` |
| 日付指定実行 | `DAILY_PLAN_DATE=2026-05-12 sh scripts/create-daily-plan.sh` |

### 環境変数

| 変数名 | デフォルト | 説明 |
|---|---|---|
| `DAILY_PLAN_DATE` | `date +%F`（当日） | 生成対象日（YYYY-MM-DD形式） |

### 終了コード

| コード | 意味 | 対処先 |
|---|---|---|
| 0 | 正常生成 | 不要 |
| 1（テンプレート未発見） | テンプレートファイルが存在しない | Section 4-A |
| 1（ファイル重複） | 当日分が既に存在する | Section 4-B |

### CCRルーティン設定（参照用）

| 項目 | 値 |
|---|---|
| ルーティンID | `trig_01SBKJ4ke5HJVyfeCivrRjJe` |
| Cron | `0 22 * * 0`（日曜22:00 UTC = 月曜07:00 JST） |
| リポジトリ | `watarumiyoshi66-glitch/ai-company-os` |
| 管理URL | https://claude.ai/code/routines |

### テンプレート更新手順

AIエージェントがテンプレートを更新する場合の手順：

```bash
# 1. テンプレートを編集
# workflows/daily/daily-plan-template.md を変更する

# 2. テストを実行
sh tests/create-daily-plan-test.sh

# 3. テスト通過を確認してからコミット
git add workflows/daily/daily-plan-template.md
git commit -m "docs: update daily plan template"
```

Expected output of test: 終了コード 0（エラーなし）

---

## Section 4: トラブルシューティング

### 4-A: テンプレートが見つからない

**症状:** `Template not found: workflows/daily/daily-plan-template.md`

**原因:** テンプレートファイルが削除・リネームされている、またはリポジトリが壊れている

**対処:**

```bash
# 状態確認
git status

# テンプレートを復元
git checkout workflows/daily/daily-plan-template.md

# 再実行
sh scripts/create-daily-plan.sh
```

---

### 4-B: ファイルが既に存在する（重複）

**症状:** `Daily Plan already exists: workflows/daily/YYYY-MM-DD-daily-plan.md`

**原因:** 当日分が手動または前回のCCRで既に生成されている

**対処:** エラーではない。既存ファイルをそのまま開いて使う。上書きは不要。

---

### 4-C: CCRルーティンが動かなかった

**症状:** 07:15時点でファイルが存在しない（かつエラーメッセージもない）

**確認:**

1. https://claude.ai/code/routines でルーティンのステータスを確認する
2. `trig_01SBKJ4ke5HJVyfeCivrRjJe` が `enabled: true` であることを確認する

**対処:**

```bash
# 手動でスクリプトを実行
sh scripts/create-daily-plan.sh
```

---

## Section 5: 改善サイクル

### テンプレート更新のトリガー

以下のいずれかに該当したら更新を検討する：

- 同じ記入漏れが3日以上続く
- 新しいAI社員の追加でセクションが不足する
- Daily Reviewの振り返りで「必要なかった」セクションが判明

### 更新手順

```
1. 変更内容をオーナーが決定（Claude相談可）
2. workflows/daily/daily-plan-template.md を編集
3. sh tests/create-daily-plan-test.sh でテスト
4. テスト通過を確認してコミット
   → 翌日から新テンプレートが適用される
```

### 週次レビュー（毎週日曜）

- その週のDaily Planを見返して記入率を確認する
- 空欄が多いセクション：テンプレートから削除を検討
- 毎回追記しているセクション：テンプレートに追加を検討
- このSOP自体の更新が必要な変更があれば `workflows/daily/daily-plan-sop.md` も更新する
```

- [ ] **Step 3: ファイルが正しく作成されたか確認する**

```bash
ls workflows/daily/
```

Expected: `daily-plan-sop.md` が存在する

```bash
wc -l workflows/daily/daily-plan-sop.md
```

Expected: 160行以上

---

### Task 2: コミットする

**Files:**
- Modify: `workflows/daily/daily-plan-sop.md`（新規追加のコミット）

- [ ] **Step 1: 差分を確認する**

```bash
git diff --stat
git status
```

Expected: `workflows/daily/daily-plan-sop.md` が新規ファイルとして表示される

- [ ] **Step 2: コミットする**

```bash
git add workflows/daily/daily-plan-sop.md
git commit -m "docs: add daily plan workflow SOP"
```

Expected: `1 file changed, N insertions(+)`
