# Claude Code Remote / Codex Handoff Memory

目的：Claude Code Remoteの出力品質とCodexレビュー品質を継続改善するための共有メモリ。

Claude Code Remoteは次回実行時にこのファイルを確認し、直近の「Claude Code Remoteへの改善指示」をプロンプト改善に反映する。
Codexはレビュー時に見つけた改善点をこのファイルへ追記し、Claude Code Remoteが次回の `daily-intel-loop` で同じ失敗を繰り返さないようにする。

## 記録ルール

- Claude Code Remoteの出力で改善が必要な点を記録する
- Codexレビューで見つけた重複、出典不足、商品化できない理由を記録する
- 次回のClaude Code Remote実行に反映すべきプロンプト改善を明記する
- 個人情報、顧客名、機密情報は記録しない

## ログテンプレート

```markdown
## YYYY-MM-DD

### 対象ファイル
- 

### 良かった点
- 

### 詰まり・失敗
- 

### Claude Code Remoteへの改善指示
- 

### Codex側の次アクション
- 
```
