# Daily CEO Digest SOP

## 目的

平日にオーナーが細かい成果物を追わなくても、今日見るべき判断事項だけを5分で確認できる状態にする。

## 実行タイミング

- 推奨：毎日 21:20 JST
- 実行主体：Claude Code Remote
- Codex確認：必要に応じて翌朝または週次監査で確認
- 保存先：`/reports/ceo-office/YYYY-MM-DD-ceo-digest.md`

## 入力

- `/research/market/YYYY-MM-DD-market-intel.md`
- `/research/competitors/`
- `/content/x/drafts/`
- `/content/note/research/`
- `/intel/services-genai/`
- `/tasks/owner-decisions.md`
- `/reports/automation-memory/claude-codex-handoff-memory.md`

## 出力に必ず含めるもの

1. 今日の重要サマリー3行
2. オーナー判断事項 最大3件
3. 承認待ちX投稿
4. Note化候補
5. 商品化候補
6. リスク・未確認事項
7. Codexに引き継ぐ確認事項

## 判断ルール

- オーナーに見せる項目は最大3件に絞る
- 公開・投稿・送信は行わない
- 判断が必要なものは `tasks/owner-decisions.md` にも追記する
- 細かい作業ログはDigestに入れず、関連ファイルへのリンクにする

## 完了条件

- `/reports/ceo-office/YYYY-MM-DD-ceo-digest.md` を保存済み
- 判断事項がある場合は `tasks/owner-decisions.md` に追記済み
- Codex確認事項がある場合はDigest末尾に明記済み
