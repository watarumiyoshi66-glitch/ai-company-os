# Daily Plan Script Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Daily Planテンプレートから今日の日付ファイルを安全に作成するスクリプトを追加する。

**Architecture:** ルート直下から実行できるシェルスクリプトを `scripts/` に置く。テンプレートと出力先は既存の `workflows/daily/` に固定し、同名ファイルがあれば終了して上書きを防ぐ。

**Tech Stack:** POSIX shell、標準Unixコマンド、シェルベースのテスト。

---

### Task 1: Test-first setup

**Files:**
- Create: `tests/create-daily-plan-test.sh`
- Create: `scripts/create-daily-plan.sh`

- [ ] **Step 1: Write the failing test**

```sh
#!/bin/sh
set -eu

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT="$REPO_ROOT/scripts/create-daily-plan.sh"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$TMP_DIR/workflows/daily"
cat > "$TMP_DIR/workflows/daily/daily-plan-template.md" <<'TEMPLATE'
# Daily Plan — YYYY-MM-DD

保存先: YYYY-MM-DD
TEMPLATE

(
  cd "$TMP_DIR"
  DAILY_PLAN_DATE=2026-05-12 "$SCRIPT"
)

TARGET="$TMP_DIR/workflows/daily/2026-05-12-daily-plan.md"
test -f "$TARGET"
grep -q "Daily Plan — 2026-05-12" "$TARGET"

printf 'keep me\n' > "$TARGET"
if (
  cd "$TMP_DIR"
  DAILY_PLAN_DATE=2026-05-12 "$SCRIPT"
); then
  echo "expected overwrite protection to fail" >&2
  exit 1
fi

test "$(cat "$TARGET")" = "keep me"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `sh tests/create-daily-plan-test.sh`

Expected: FAIL because `scripts/create-daily-plan.sh` does not exist yet.

- [ ] **Step 3: Write minimal implementation**

```sh
#!/bin/sh
set -eu

DATE_VALUE="${DAILY_PLAN_DATE:-$(date +%F)}"
TEMPLATE="workflows/daily/daily-plan-template.md"
TARGET="workflows/daily/${DATE_VALUE}-daily-plan.md"

if [ ! -f "$TEMPLATE" ]; then
  echo "Template not found: $TEMPLATE" >&2
  exit 1
fi

if [ -e "$TARGET" ]; then
  echo "Daily Plan already exists: $TARGET" >&2
  exit 1
fi

sed "s/YYYY-MM-DD/$DATE_VALUE/g" "$TEMPLATE" > "$TARGET"
echo "Created: $TARGET"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `sh tests/create-daily-plan-test.sh`

Expected: PASS with exit code 0.

- [ ] **Step 5: Manual safety check**

Run: `./scripts/create-daily-plan.sh`

Expected on 2026-05-11: FAIL because `workflows/daily/2026-05-11-daily-plan.md` already exists, and the existing file remains unchanged.

- [ ] **Step 6: Commit and PR**

```bash
git add scripts/create-daily-plan.sh tests/create-daily-plan-test.sh tasks/todo.md docs/superpowers/plans/2026-05-11-daily-plan-script.md
git commit -m "feat: add daily plan creation script"
git push -u origin codex-daily-plan-script
gh pr create --title "Add Daily Plan creation script" --body "Adds a small script to create today's Daily Plan from the template without overwriting existing files."
```
