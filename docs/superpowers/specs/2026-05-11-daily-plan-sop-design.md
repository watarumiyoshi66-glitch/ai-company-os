# Design Spec: Daily Plan自動生成ワークフロー SOP

- 作成日: 2026-05-11
- ステータス: 承認済み
- 実装先: `workflows/daily/daily-plan-sop.md`

---

## 目的

Daily Plan自動生成ワークフローの運用手順を文書化する。
人間（オーナー）の日次操作ガイドと、AIエージェントが設定変更・障害対応時に参照できる技術仕様を1ファイルに統合する。

---

## 対象読者

- **人間（オーナー）**: 毎朝・毎晩の運用手順として参照
- **AIエージェント（Codex/Claude）**: テンプレート更新・障害対応時のみ参照

---

## 構成（5セクション）

### Section 1: 全体フロー

5フェーズのワークフロー概要。

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
  → memory/daily-insights/ に保存

[Phase 5] 障害・例外処理
  スクリプト失敗時・ファイル重複時の手動対応
```

**分岐判断基準:**
- ファイル重複 → スクリプト停止、既存ファイルをそのまま使用
- テンプレート未発見 → スクリプトエラー終了、Section 4-A参照

---

### Section 2: 人間向け日次運用手順

**朝のルーティン（07:00〜08:00）**

```
07:00  生成確認
       └─ workflows/daily/YYYY-MM-DD-daily-plan.md の存在を確認
       └─ なければ手動: sh scripts/create-daily-plan.sh

07:05  必須記入項目
       └─ 今日のフォーカス（1つだけ）
       └─ 今日の目標（最大3つ）
       └─ X投稿テーマと形式（インサイト型/問い型/体験型）

07:15  該当日のみ記入
       └─ Note記事ステータス更新
       └─ 営業ナレッジのトピック
```

**夜のルーティン（21:00〜）**

```
21:00  Daily Review記入（同ファイルの下半分）
       └─ 今日の成果・学び・うまくいったこと・改善点
       └─ 明日に持ち越すタスク・明日のフォーカス

21:15  インサイト保存
       └─ 重要な気づきを memory/daily-insights/YYYY-MM-DD.md に転記
```

**判断ルール:**
- 目標は最大3つ。それ以上は「その他タスク」へ
- X投稿は必ず下書き確認後に投稿
- Daily Reviewは翌朝に書かない（その日のうちに完結）

---

### Section 3: AI技術仕様

**スクリプト仕様**

```
ファイル:     scripts/create-daily-plan.sh
テンプレート: workflows/daily/daily-plan-template.md
出力先:       workflows/daily/YYYY-MM-DD-daily-plan.md
実行方法:     sh scripts/create-daily-plan.sh
日付指定:     DAILY_PLAN_DATE=2026-05-12 sh scripts/create-daily-plan.sh
```

**環境変数**

| 変数名 | デフォルト | 説明 |
|---|---|---|
| `DAILY_PLAN_DATE` | `date +%F`（当日） | 生成対象日（YYYY-MM-DD形式） |

**終了コードと意味**

| コード | 意味 | 対処 |
|---|---|---|
| 0 | 正常生成 | 不要 |
| 1（テンプレート未発見） | テンプレートファイルが存在しない | Section 4-A参照 |
| 1（ファイル重複） | 当日分が既に存在する | Section 4-B参照 |

**CCRルーティン設定（参照用）**

```
ルーティンID: trig_01SBKJ4ke5HJVyfeCivrRjJe
Cron:         0 22 * * 0  （日曜22:00 UTC = 月曜07:00 JST）
リポジトリ:   watarumiyoshi66-glitch/ai-company-os
```

**テンプレート更新手順（AIが参照するのはこのケース）**

```
1. workflows/daily/daily-plan-template.md を編集
2. sh tests/create-daily-plan-test.sh でテスト実行
3. 問題なければコミット → CCRが次回から新テンプレートを使用
```

---

### Section 4: トラブルシューティング

```
[4-A] テンプレートが見つからない
  症状: "Template not found: workflows/daily/daily-plan-template.md"
  原因: ファイル削除・リネーム・リポジトリが壊れている
  対処: git status で確認 → git checkout でテンプレートを復元

[4-B] ファイルが既に存在する（重複）
  症状: "Daily Plan already exists: workflows/daily/YYYY-MM-DD-daily-plan.md"
  原因: 当日分が手動または前回のCCRで生成済み
  対処: 既存ファイルを開いてそのまま使う（上書き不要）

[4-C] CCRルーティンが動かなかった
  症状: 07:15時点でファイルが存在しない（かつエラーもない）
  確認: https://claude.ai/code/routines でステータス確認
  対処: sh scripts/create-daily-plan.sh を手動実行
```

---

### Section 5: 改善サイクル

**テンプレート更新のトリガー**

- 同じ記入漏れが3日以上続く
- 新しいAI社員の追加でセクションが不足する
- Daily Reviewの振り返りで「必要なかった」セクションが判明

**更新手順**

```
1. 変更内容をオーナーが決定（Claude相談可）
2. workflows/daily/daily-plan-template.md を編集
3. sh tests/create-daily-plan-test.sh でテスト
4. コミット → 翌日から新テンプレートが適用される
```

**週次レビュー（毎週日曜）**

- その週のDaily Planを見返して記入率を確認
- 空欄が多いセクションはテンプレートから削除候補

---

## 実装対象ファイル

| ファイル | 用途 |
|---|---|
| `workflows/daily/daily-plan-sop.md` | 本SOP文書（実装先） |
| `scripts/create-daily-plan.sh` | 変更なし（参照のみ） |
| `workflows/daily/daily-plan-template.md` | 変更なし（参照のみ） |
| `tests/create-daily-plan-test.sh` | 変更なし（参照のみ） |
