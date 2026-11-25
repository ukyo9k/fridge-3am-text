#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge texts its owner at 3am to /output/entry.txt.
"""
import os

ENTRY = "it's 3am. this is the third time tonight. nothing new has moved in since 2am. i'm a fridge, not a casino. go to sleep."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
