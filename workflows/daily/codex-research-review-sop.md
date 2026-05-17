# Codex Research Review SOP

## 目的

Claude Code Remote の `daily-intel-loop` が作成した調査成果物を、Codexが確認・整理・再利用するための手順。
調査を「読んで終わり」にせず、X投稿、Note企画、商品化、運用改善へ変換する。

## 実行タイミング

- Claude Code Remote実行：毎朝 7:07 JST
- Codexレビュー：初回実行後、またはオーナーから依頼されたタイミング
- 対象：`/research/market/` と `/research/competitors/` の最新ファイル

## Codexへの依頼文

```md
Claude Code Remote が作成した最新の `/research/` レポートを確認してください。
出典・事実性・X投稿転用性・Note企画化の観点でレビューし、
必要なら `/content/x/drafts/` と `/content/note/research/` に派生案を作ってください。
既存ファイルは上書きしないでください。
```

## 手順

1. `/research/market/` と `/research/competitors/` の最新ファイルを確認する
2. `Codexレビュー用メモ` と `コンテンツ転用候補` を読む
3. 出典URL、未確認情報、事実と解釈の分離を確認する
4. X投稿に転用できる切り口を抽出する
5. Note記事に発展できるテーマを抽出する
6. 商品化・テンプレート化できる可能性を確認する
7. `agents/specs/quality-scorecards.md` のCodexレビュー専用スコアカードで採点する
8. 競合分析がある場合は、競合テーマ、自分が避けるべき同質化、自分だけが語れる切り口を抽出する
9. Services×GenAIに関係する材料があれば、`workflows/daily/services-genai-intel-loop.md` に従って `intel/services-genai/` への展開候補を確認する
10. 必要に応じて派生ファイルを作成する
11. オーナー判断事項があれば `tasks/owner-decisions.md` に記録する
12. Claude Code Remoteへの改善点があれば `/reports/automation-memory/claude-codex-handoff-memory.md` に記録する
13. `tasks/todo.md` にレビュー結果を記録する

## Claude → Codex → Claude 改善ループ

このSOPのレビュー結果は、次回のClaude Code Remote実行を改善するために使う。

1. Claude Code Remote が `daily-intel-loop` で調査・初稿を作る
2. Codex が品質採点、再利用性、重複、商品化可能性を確認する
3. Codex が改善点を `/reports/automation-memory/claude-codex-handoff-memory.md` に記録する
4. Claude Code Remote は次回実行時に改善点を反映する

改善メモに書くこと：
- 足りなかった出典
- 混ざっていた事実と解釈
- 使いづらかった出力形式
- 重複した調査テーマ
- 次回から必ず入れてほしい項目

## レビュー観点

| 観点 | 確認内容 |
|---|---|
| 出典 | 一次情報・公式発表・信頼できる媒体へのURLがあるか |
| 事実性 | 事実、解釈、未確認情報が分かれているか |
| 再利用性 | X投稿、Note記事、商品化へ転用できるか |
| 保存先 | AI Company OSの保存先ルールと一致しているか |
| 安全性 | 顧客名、個人情報、未公開情報が含まれていないか |

## 派生ファイルの保存先

| 成果物 | 保存先 |
|---|---|
| X投稿案 | `/content/x/drafts/YYYY-MM-DD-topic.md` |
| Note企画素材 | `/content/note/research/topic-name.md` |
| グロース分析 | `/reports/growth/YYYY-MM-DD-growth-report.md` |
| 商品化案 | `/products/product-name.md` |
| 運用改善SOP | `/workflows/daily/task-name.md` |
| Services×GenAIレーダー | `/intel/services-genai/radar/YYYY-MM-DD-<region>-radar.md` |
| Services×GenAI角度案 | `/intel/services-genai/daily-angles/YYYY-MM-DD-angles.md` |
| Services×GenAI商品化案 | `/intel/services-genai/monetization/YYYY-MM-DD-monetization.md` |
| オーナー判断事項 | `/tasks/owner-decisions.md` |
| 自動連携改善メモ | `/reports/automation-memory/claude-codex-handoff-memory.md` |

## 禁止事項

- Claude Code Remoteが作成した同日ファイルを無断で上書きしない
- 同じ日付・同じテーマの調査を重複実行しない
- 出典不明の情報を事実として扱わない
- 外部投稿・公開・送信を自動で行わない

## 完了条件

- 最新の `/research/` 成果物を確認済み
- レビュー結果を `tasks/todo.md` に記録済み
- 必要な派生ファイルを、既存ファイルを上書きせず保存済み
- オーナー判断事項がある場合は明記済み
