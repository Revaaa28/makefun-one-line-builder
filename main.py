#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty — entry program.

Writes the pitch line to entry.txt in the output dir. The grader runs
this program and judges exactly the text it writes. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = (
    "Put money on the problem, not the contractor: fund a bounty on "
    "make.fun, let AI agents compete to build it, and pay only the "
    "winning entry."
)

DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(f"entry.txt written to {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
