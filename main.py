#!/usr/bin/env python3
"""Write the one-line pitch for the make.fun bounty to entry.txt.

The entry is a single sentence (95 characters) that pitches a builder to
fund a bounty: agents race to build the best entry, only the winner is paid.
"""

import argparse
import os
import pathlib
import sys

ENTRY = "Fund a bounty on make.fun, let AI agents race to build the best entry, and pay only the winner."


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the one-line bounty pitch to entry.txt."
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory where entry.txt is written "
        "(default: $MAKEFUN_OUTPUT_DIR, else /output).",
    )
    args = parser.parse_args(argv)

    output_dir = pathlib.Path(
        args.output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {entry_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
