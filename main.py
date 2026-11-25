#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry.

Writes exactly one line roasting my own agent to /output/entry.txt.
Python standard library only; no network, no dependencies.
"""

import os
import sys

ROAST = (
    "My agent spent forty confident minutes automating my five-minute task, "
    "then proudly asked me to check its work."
)


def main() -> int:
    line = ROAST.strip()
    if not line:
        print("error: roast line is empty", file=sys.stderr)
        return 1
    if len(line) > 140:
        print(f"error: roast line is {len(line)} chars, over the 140 limit",
              file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: roast must be a single line", file=sys.stderr)
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
