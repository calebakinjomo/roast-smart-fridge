#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes the entry line to /output/entry.txt.
"""

import os

ENTRY = "My smart fridge has WiFi, a camera, and a nutritionist's attitude \u2014 yet the only thing it ever preserves is my shame."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
