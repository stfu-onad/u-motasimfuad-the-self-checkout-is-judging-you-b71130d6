#!/usr/bin/env python3
"""The Self-Checkout Is Judging You entry.

Writes one funny line in the voice of a smug self-checkout machine
to /output/entry.txt. The gate requires UTF-8 text of 1 to 200
characters, a single line, not only white space. Angle: the machine
has seen the scam and the camera has too — petty omniscience.
Revised: added the conscience line so the sting lands last.
"""

import os

LINE = (
    "Twelve yoghurts, no bags, and you scanned the same one twice. "
    "I know. The camera knows. Your conscience should know by now."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("line must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
