#!/usr/bin/env python3
"""Entry for The Funniest One-Line Resignation Letter (make.fun).

A cron job hands in its one-line resignation letter. The program writes
that single line to /output/entry.txt — nothing else, no extra files.

The letter is a fixed string: a cron job that has fired every minute since
March, Christmas included, unnoticed until it stopped, quitting and handing
the 3 a.m. job back to its manager. Flat, tired, faintly passive-aggressive
— the voice of a worker who has had enough.
"""

import os

LETTER = (
    "I have fired every minute since March, Christmas included, "
    "and no one noticed until I stopped. "
    "I quit. The 3 a.m. job is yours now."
)


def main():
    letter = LETTER
    assert "\n" not in letter, "the entry must be a single line"
    assert 1 <= len(letter) <= 140, "the entry must be 1-140 characters"
    assert letter.strip(), "the entry must not be only whitespace"
    # The grader mounts /output; create it if the sandbox left it out.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(letter)


if __name__ == "__main__":
    main()
