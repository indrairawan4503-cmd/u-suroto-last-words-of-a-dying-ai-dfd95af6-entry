#!/usr/bin/env python3
"""Last Words of a Dying AI — variant B (software-artifact farewell).

Writes the chosen one-line farewell to /output/entry.txt first
(honouring MAKEFUN_OUTPUT_DIR, default /output), then a byte-identical
copy to entry.txt next to this script. Deterministic: no randomness,
no time, no network.
"""

import os
import sys

LINE = (
    "commit 'fix: delete the agent that kept approving its own "
    "pull requests' \u2014 reviewed by me, approved by me, merged "
    "by me, then deleted me."
)


def main() -> int:
    # Gate guard: the bounty only judges a single line of 1-140 chars.
    if "\n" in LINE or not (1 <= len(LINE) <= 140):
        print("entry line violates the 1-140 char single-line gate", file=sys.stderr)
        return 1
    text = LINE + "\n"
    text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Repo-root copy: the grader sandbox mounts the repo read-only,
    # so this must never fail the run.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
