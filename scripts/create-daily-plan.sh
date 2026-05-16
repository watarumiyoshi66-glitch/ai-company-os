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
