#!/usr/bin/env python3
"""Funniest Lost Sock Status Update - make.fun bounty entry.

Writes one status update (1-120 characters) in the voice of a lost sock
to $OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only. Deterministic: the same text is
written on every run.
"""

import os

MAX_CHARS = 120

ENTRY = "Update: I live in a magician's hat now. He pulled out a rabbit, a dove, a bouquet, and somehow still not me."


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
