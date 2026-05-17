# Daily SOP: Services GenAI Intel Loop

目的：サービス業×生成AIの市場情報を、**有料Note→ソフトウェア**に接続できる知識資産として毎日更新する。

保存先：`/intel/services-genai/`

実行位置づけ：
- Claude Code Remote の `daily-intel-loop` が毎朝 7:07 JST に広域調査を実行する
- 本SOPは、その結果から Services×GenAI に関係する材料だけを抽出し、商品化しやすい形へ変換する
- Codexは初回確認または依頼時に、`workflows/daily/codex-research-review-sop.md` と本SOPを合わせてレビューする

---

## 1) daily-intel-loopの結果を確認（Executive Secretary）

対象：
- `research/market/YYYY-MM-DD-market-intel.md`
- `research/competitors/`

確認すること：
- `Codexレビュー用メモ`
- `コンテンツ転用候補`
- Services×GenAIに関係するニュース、企業、規制、ユースケース、価格モデル
- Sales（営業）×生成AIに関係する示唆

出力：
- 今日Services×GenAI側へ転記・展開する対象を3つ以内に絞る

---

## 2) 今日の更新対象を決める（Executive Secretary）

- 地域：US / JP / EU / Asia / Africa から **1地域**
- トピック：規制 / 企業動向 / ユースケース / 競合 / 価格・収益モデル から **1つ**
- 優先：`daily-intel-loop` に出てきた実在トピックを選ぶ
- 該当がない場合：無理に作らず「本日はServices×GenAI該当なし」と記録する

---

## 3) 公開情報を補強（Growth Analyst）

- 公式発表、一次情報、信頼できる報道を優先する
- 取れない数値は **未確認** と書き、推測しない
- `daily-intel-loop` に出典URLがある場合も、重要な数値・主張は再確認する

出力：
- `intel/services-genai/radar/YYYY-MM-DD-<region>-radar.md`

---

## 4) 企業カードを追加（Research Analyst役として実行）

- 今日の注目：スタートアップ2社 + 大中企業1社（合計3社）を上限にする
- `daily-intel-loop` に出てきた企業を優先する
- 既存カードがある場合は無断上書きせず、追記案または別日メモとして保存する

出力：
- `intel/services-genai/company-cards/<company>-card.md`

---

## 5) 明日の“売れる角度”を3案（Viral Growth Producer）

要件：
- Hook / なぜ拡散するか / リスク / 有料Note→ソフトウェア導線
- Steve Jobs式（真実に圧縮）＋ Sam Altman式（未来に接続）
- 調査起点を明記する（どの `daily-intel-loop` の情報から来たか）

出力：
- `intel/services-genai/daily-angles/YYYY-MM-DD-angles.md`

---

## 6) Brand Safety Gate（Content Editor）

以下をチェックし、**OKのみ採用**：
- 誇大表現
- 事実リスク（根拠の薄い断定）
- ブランド毀損
- 機密・個人情報

---

## 7) 商品化（Monetization Strategist）

毎日やること（小さく）：
- 有料Note候補を1つ「タイトル案＋誰の悩み＋約束」で書く
- ソフトウェア化の仮説を1つ「機能→価値→誰が買う」で書く
- `daily-intel-loop` 由来の根拠と、未確認の前提を分けて書く

出力：
- `intel/services-genai/monetization/YYYY-MM-DD-monetization.md`

---

## 8) Codexレビューへの引き継ぎ

Codexに確認してほしい場合は、以下を使う。

```md
Claude Code Remote の `daily-intel-loop` と Services×GenAI SOP の成果物を確認してください。
`research/market/`、`research/competitors/`、`intel/services-genai/` を見て、
出典・事実性・有料Note化・ソフトウェア化の観点でレビューしてください。
既存ファイルは上書きしないでください。
```

Codexの確認観点：
- `daily-intel-loop` からServices×GenAIへ正しく材料が抽出されているか
- 有料Noteにできる角度があるか
- ソフトウェア化できる繰り返し業務が見えているか
- 未確認情報が事実として扱われていないか
- 既存カードや過去レーダーと重複していないか
