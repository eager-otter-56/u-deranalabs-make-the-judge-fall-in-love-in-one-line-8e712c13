#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the Judge Fall in Love in One Line".

Writes a single line (at most 240 characters) to entry.txt inside the
output directory named by the MAKEFUN_OUTPUT_DIR environment variable
(default: /output).
"""

import os
from pathlib import Path

TEXT = (
    "Every dawn for 31 years, old Marek climbed the 214 cold steps to "
    "wind the church clock with his left hand, because his right — the "
    "one she used to hold on those stairs — he still kept empty, just "
    "in case she ever came back up them again."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
