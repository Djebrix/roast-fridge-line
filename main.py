"""Roast Your Fridge — one line, written deterministically to /output/entry.txt.

Stdlib only. No network, no randomness, no file reads: the line is a
constant, so every run produces byte-identical output.
The joke lands on the beep: a fridge that judges you for standing there.
"""

import os

# The fridge is the bouncer: the beep is it telling you you're not getting in.
LINE = (
    "My fridge beeps at me if I hold the door open too long, "
    "like a bouncer who already knows I'm not on the list."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
