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
grep -q "保存先: 2026-05-12" "$TARGET"

printf 'keep me\n' > "$TARGET"
if (
  cd "$TMP_DIR"
  DAILY_PLAN_DATE=2026-05-12 "$SCRIPT"
); then
  echo "expected overwrite protection to fail" >&2
  exit 1
fi

test "$(cat "$TARGET")" = "keep me"
