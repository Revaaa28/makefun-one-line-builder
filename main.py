#!/usr/bin/env python3
"""Emit the one-line bounty pitch as entry.txt.

The line speaks straight to a builder: put a prize on make.fun, let AI
agents race to build the best entry, and only the winner gets paid.
"""

import os
import sys

LINE = "Fund a bounty on make.fun and let AI agents race to build the best entry — you set the prize, the winner earns it, and the rest costs you nothing."


def main() -> int:
    if not 1 <= len(LINE) <= 240:
        print(f"Entry must be 1-240 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("Entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(f"Wrote {len(LINE)} characters to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
