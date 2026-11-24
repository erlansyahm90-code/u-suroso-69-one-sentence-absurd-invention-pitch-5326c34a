"""Entry for the Absurd Invention Pitch (One Sentence) competition.

Writes a single-sentence pitch for a fictional absurd invention to
/output/entry.txt. The entry is exactly one sentence and stays within
the 220-character limit.
"""

import os

ENTRY = (
    "The Meeting Muter: a small device that detects 'let's circle back' "
    "and plays a loud foghorn, ending the meeting immediately — 63 silenced "
    "since March, and HR has questions."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry line to the output file."""
    # One sentence, 172 characters — verified against the competition gate.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
