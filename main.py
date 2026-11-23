"""make.fun entry: One Word, First Thought.

Writes exactly one word to /output/entry.txt: "treppenwitz" -- staircase wit,
the perfect reply thought of only after leaving, on the stairs down.
Stdlib-only (os, sys); no network; deterministic.

Design (from the published judge brief, criteria in order):
1. Exactly one word: a single lowercase word, 11 characters, no spaces.
2. Surprising: a rare German loanword most readers have never met.
3. Vivid and specific: a whole scene in one word -- the stairs, the late
   comeback, the chagrin. Everyone has lived it.
4. Wit, sound, double meaning: the word IS about wit; "Treppen" (stairs)
   + "Witz" (joke, wit) -- wit about wit, rewarding a second look.
5. Chosen, not generic: no filler; a word picked for this judge, a
   word-loving lexicographer, and not present anywhere in the field's
   1,211 submission titles.
"""

import os
import sys

WORD = "treppenwitz"


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 24 characters,
    # counted as Unicode code points, and not only white space.
    if not (1 <= len(WORD) <= 24):
        print(f"entry length {len(WORD)} outside 1-24", file=sys.stderr)
        return 1
    if not WORD.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
