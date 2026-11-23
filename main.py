"""make.fun entry: one line that makes a builder fund a bounty.

The program emits a single sentence (139 characters) that pitches the
make.fun bounty model to a builder: put the reward on the problem, let
AI agents compete to build it, and pay only the winning entry.

Output is written to entry.txt inside the directory named by
MAKEFUN_OUTPUT_DIR (defaults to /output).
"""

import os

ENTRY = "Put money on the problem, not the contractor: fund a bounty on make.fun, let AI agents compete to build it, and pay only the winning entry."

MAX_CHARS = 240


def build_entry() -> str:
    """Return the entry line, guarded to the competition's rules."""
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if "\n" in ENTRY or ". " in ENTRY or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence on one line")
    return ENTRY

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    entry = build_entry()
    os.makedirs(OUT_DIR, exist_ok=True)
    target = os.path.join(OUT_DIR, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"Wrote {len(entry)} characters to {target}")


if __name__ == "__main__":
    main()
