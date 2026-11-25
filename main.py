#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert entry.

One sentence, one roast. The lawmakers who would govern AI, crypto
and the whole internet cannot convert a file to PDF — the grand
regulators of tomorrow's technology, defeated by today's most
ordinary button. The sentence keeps the contrast tight: a 400-page
bill before lunch, then a staffer, a printer and a prayer.
"""
import os

LINE = (
    "They can draft a 400-page bill regulating artificial intelligence "
    "before lunch, but ask them to turn that bill into a PDF and suddenly "
    "the future of technology needs a staffer, a printer, and a prayer."
)


def main():
    assert 1 <= len(LINE) <= 320, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
