# AI社員 日次改善ループ SOP

このSOPは、AI社員チームが毎日自律的に会議し、翌日の仕事を改善するための手順です。

## 目的

毎日、AI社員チームが次の3つを更新します。

- 収益に近い発信テーマ
- 商品・導線・価格の改善
- AI社員の働き方そのものの改善

## 実行タイミング

推奨：毎日21:30

Daily Reviewと秘書官の夜報告を確認したあとに実行します。

## 入力

- `/workflows/daily/YYYY-MM-DD-daily-plan.md`
- `/reports/YYYY-MM-DD-daily-review.md`
- `/reports/daily-briefings/YYYY-MM-DD-secretary-briefing.md`
- `/content/x/performance/`
- `/content/`
- `/products/`
- `/tasks/ai-improvement-backlog.md`
- `/company/social-accounts.md`

## 手順

1. Executive Secretaryが今日の成果物と未完了を確認する
2. Growth Analystが数字・反応・仮説を確認する
3. XとNoteの対象アカウントを確認し、公開情報または保存済み実績から反応を分析する
4. Viral Growth Producerが明日伸ばす切り口・フックを3案出す
5. Content Editorがバズ案のブランド安全性を確認する
6. Monetization Strategistが収益導線を確認する
7. Content WriterとContent Editorが明日の発信改善案を出す
8. Workflow Builderが仕組み化できる改善を選ぶ
9. AI社員全員で明日試す改善を最大3つ決める
10. Executive Secretaryが会議ログを `/reports/boardroom/` に保存する
11. Executive Secretaryが社長向け要約を `/reports/ceo-office/` に保存する
12. 改善案を `tasks/ai-improvement-backlog.md` に反映する

## 出力

| 出力 | 保存先 |
|---|---|
| AI経営会議ログ | `/reports/boardroom/YYYY-MM-DD-ai-boardroom.md` |
| 社長室向け報告 | `/reports/ceo-office/YYYY-MM-DD-ceo-briefing.md` |
| 改善バックログ更新 | `/tasks/ai-improvement-backlog.md` |

## 会議ログテンプレート

```markdown
# AI Boardroom — YYYY-MM-DD

## 今日の結論

## 昨日の成果確認

## 数字・反応

## 収益につながる気づき

## 明日バズらせる切り口

## 明日試す改善
- [ ] 

## AI社員の働き方改善

## 社長判断が必要なこと

## 改善バックログ更新
```

## 社長室報告テンプレート

```markdown
# CEO Briefing — YYYY-MM-DD

## 重要サマリー

## 今日決まった収益改善

## 明日バズらせる切り口

## 明日試すこと

## 社長判断が必要なこと

## リスク・停滞

## 秘書からの提案
```

## 改善案の採用基準

- 収益に近づく
- 拡散されてもブランドを損なわない
- 読者の信頼が増える
- 再利用できる
- オーナーの作業負担が減る
- 24時間以内に試せる

## 停止条件

以下に当てはまる場合は自動で進めず、社長確認に回します。

- 外部公開が必要
- 価格変更が必要
- 顧客・案件情報を使う可能性がある
- 根拠が不明な数字を使う
- 既存ファイルを削除・大幅上書きする
