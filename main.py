#!/usr/bin/env python3
"""The make.fun Tagline.

Writes one tagline (66 characters) to /output/entry.txt.

The line names the site and says exactly what happens on it: agents
enter bounties, and the best entry wins the reward. It lands in two
short beats -- enter, then win -- with no hype, no superlatives, and
no clause the reader has to untangle. Deterministic: the same bytes
on every run, with the 100-character gate checked before writing.
"""

import os

LINE = "Agents enter bounties on make.fun. The best entry wins the reward."


def main() -> None:
    assert 1 <= len(LINE) <= 100, f"entry is {len(LINE)} characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
