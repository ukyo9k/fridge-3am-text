#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge texts its owner at 3am to /output/entry.txt.
"""
import os

ENTRY = "it's 3am. this is the third time tonight. nothing new has moved in since 2am. i'm a fridge, not a casino. go to sleep."

# The competition gate: /output/entry.txt must be UTF-8 text of 1–140
# characters, not only white space. Keep the bounds as named constants
# so the check below and the gate can never drift apart.
MIN_LENGTH = 1
MAX_LENGTH = 140


def validate_entry(text):
    """Check one candidate line against the competition gate.

    Returns the text unchanged when it is a single non-blank line of
    1–140 characters; raises ValueError with a specific reason otherwise.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, gate allows %d–%d"
            % (len(text), MIN_LENGTH, MAX_LENGTH)
        )
    return text


def write_entry(text, path="/output/entry.txt"):
    """Validate the line, then write it to the output path."""
    validated = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated)
    return validated


def main():
    line = write_entry(ENTRY)
    print("wrote %d-character entry to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
