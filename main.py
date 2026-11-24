"""Emit a single-sentence pitch for a daft invention.

This script produces the competition entry: one sentence, saved to
/output/entry.txt, describing a gadget that cures a small daily
irritation in a delightfully over-the-top way.
"""

import os

# The pitch itself. One sentence, no more, no less. The humour lives
# in the gadget, not in a punchline tacked on afterwards.
ENTRY = "The Meeting Muter: a small device that detects the phrase 'let's circle back' and plays a loud foghorn, ending the meeting immediately."

# Where the judge looks for the finished text.
OUTPUT_PATH = "/output/entry.txt"

# The competition's own gate: a non-empty sentence of at most 220 chars.
MAX_CHARS = 220


def main():
    # Keep the entry inside the allowed window before writing anything.
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}"
    )

    # Make sure the output folder exists, then write the bare sentence.
    # No trailing newline: the file is the sentence, nothing extra.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
