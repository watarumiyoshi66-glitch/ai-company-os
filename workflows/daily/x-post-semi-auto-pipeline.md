# X Post Semi-Auto Pipeline

## 目的

Claude Code RemoteがX投稿案を毎日3本作り、Codexが品質採点して1本に絞る。
オーナーは投稿可否だけ判断する。

## 実行タイミング

- Claude Code Remote：毎朝 `daily-intel-loop` 後
- Codex：初回レビュー時、またはDaily CEO Digest作成前
- 保存先：`/content/x/drafts/YYYY-MM-DD-topic.md`

## 流れ

1. Claude Code Remoteが `/research/` と `/intel/services-genai/` からX投稿案を3本作る
2. 各案に出典、狙い、リスク、想定読者を付ける
3. Codexが `agents/specs/quality-scorecards.md` で採点する
4. Codexが最もよい1本を推奨案として選ぶ
5. 投稿可否を `tasks/owner-decisions.md` に記録する
6. オーナー承認後のみ投稿する

## X投稿案テンプレート

```markdown
# X投稿案 — YYYY-MM-DD

## 推奨案

本文：

## 候補3本

| 案 | 本文 | 狙い | リスク | 点数 |
|---|---|---|---|---:|
| A |  |  |  |  |
| B |  |  |  |  |
| C |  |  |  |  |

## 出典

- 

## オーナー判断事項

- 投稿してよいか：
```

## 禁止事項

- 自動投稿しない
- 出典不明の断定をしない
- 炎上狙いの煽りにしない
