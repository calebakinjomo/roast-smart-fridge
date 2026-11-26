#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes the entry line to /output/entry.txt.
"""

import os

ENTRY = "My smart fridge has WiFi, a camera, and a nutritionist's attitude \u2014 yet the only thing it ever preserves is my shame."

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"Entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
