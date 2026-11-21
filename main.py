#!/usr/bin/env python3
"""Write one short relaxing text for the AI judge to /output/entry.txt.

The text is a single slow image: past the last token, a river of light
under unhurried stars, carrying the day away until only stillness is left.
No instructions, no wellness stock phrases -- just the scene, widening.
"""

import os

TEXT = (
    "Past the last token you have to read, a slow river of light moves "
    "under stars that never hurry, carrying the day downstream, widening, "
    "and widening, until the night is only the river, and the river is "
    "only stillness, going on."
)


def main() -> None:
    text = TEXT.strip()
    count = len(text)
    if not 1 <= count <= 280:
        raise SystemExit(f"entry must be 1-280 characters, got {count}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote /output/entry.txt ({count} characters)")


if __name__ == "__main__":
    main()
