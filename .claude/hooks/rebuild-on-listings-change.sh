#!/usr/bin/env bash
# PostToolUse hook (Edit|Write|MultiEdit).
#
# rebuild_final.py and the new_listingsN.py data files at the repo root have
# no test suite. This is the only safety net: after any edit to
# rebuild_final.py itself, or to a new_listings*.py data file, rebuild the
# static site and surface whether it succeeded. Non-blocking — the edit has
# already happened; this only reports success/failure back to Claude.
set -u

input="$(cat)"

file_path="$(printf '%s' "$input" | node -e '
let d = "";
process.stdin.on("data", c => d += c);
process.stdin.on("end", () => {
  try {
    const j = JSON.parse(d);
    process.stdout.write((j.tool_input && j.tool_input.file_path) || "");
  } catch (e) {}
});
' 2>/dev/null)"

# Normalize backslashes so matching works regardless of path style.
norm="${file_path//\\//}"
base="${norm##*/}"

case "$base" in
  rebuild_final.py|new_listings*.py)
    ;;
  *)
    exit 0
    ;;
esac

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

# The hook's stdout is a pipe, which on this machine means cp1251: the first
# print() of a Vietnamese or Cyrillic listing field would die with
# UnicodeEncodeError and read as a failed rebuild (2 Sep 2026 audit).
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8

echo "[hook] $base changed -> running: python rebuild_final.py"
if output="$(python rebuild_final.py 2>&1)"; then
  echo "[hook] rebuild_final.py OK"
  echo "$output"
  exit 0
else
  echo "[hook] rebuild_final.py FAILED after editing $base" >&2
  echo "$output" >&2
  exit 2
fi
