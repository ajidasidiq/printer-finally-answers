"""The Printer Finally Answers.

A make.fun program/v1 entry. The grader runs this file and reads
/output/entry.txt: one line the office printer finally says back to
everyone staring at it.

The joke is a ledger kept by the machine: after 41,208 sheets fed
without a word, the single jam is traced, sheet by sheet, to the one
page the user folded, loaded sideways, and then thumped the printer
for — and the printer files it the way it files everything, as an
error code. The punchline is the diagnosis: Error 41 is not the
machine. It is the user.
"""

from __future__ import annotations

import os
from pathlib import Path

ENTRY = (
    "I fed 41,208 sheets without complaint. The one time I jammed, "
    "it was the page you folded, loaded sideways, and then thumped "
    "me for. Error 41: user."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # The sealed gate accepts 1-240 characters of UTF-8 text, nothing
    # else. Refuse to write an entry that would fail it.
    if not 1 <= len(ENTRY) <= 240:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-240")
    # The sealed gate accepts one line only. Refuse any entry with a
    # line break so a multi-line entry can never reach the gate.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line, no newline characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
