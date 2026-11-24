"""The excuse a robot vacuum gives after eating a sock.

The whole entry is one deadpan line, delivered in the vacuum's own
voice: a legalistic robot that treats the floor as its jurisdiction
and the sock as debris. Nothing else is needed here — the script
validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The excuse itself: one line, exactly 94 characters.
# The joke turns on the last clause: the vacuum doesn't make the
# rules, it eats them — which is, literally, its job.
LINE = (
    "Per my programming, anything on the floor is debris. "
    "I don't make the rules \u2014 I just eat them."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text:
        raise ValueError("line must not be only whitespace")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
