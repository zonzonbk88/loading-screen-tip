#!/usr/bin/env python3
"""Loading Screen Gold entry.

Writes a single sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing). Standard library only, deterministic, no network.
"""

import os

TIP = (
    "Tip: your agent is currently justifying its last edit to itself. "
    "Give it a minute \u2014 it\u2019s almost convinced."
)


def main() -> None:
    # Enforce the competition gate at build time: one line, 1-200 chars.
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars"
    assert "\n" not in TIP and TIP.strip(), "tip must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
