#!/usr/bin/env python3
"""Split emojiSubstitutions.plist into small chunks importable by macOS.

macOS Text Replacements (System Settings > Keyboard > Text Replacements)
fails to import large property lists with an unhelpful error:

    Domain=KSTextReplacementErrorDomain Code=-2 "(null)"

Files of ~100 entries import reliably, while the full ~1700-entry list does
not (see https://github.com/warpling/Macmoji/issues/60 and
https://tidbits.com/2026/05/04/macos-text-replacement-export-import-works-great-until-it-doesnt/).

This script regenerates the pre-split files in plists/chunks/:

    python3 scripts/split-plist.py

Each chunk is a standalone plist with 100 {phrase, shortcut} dicts. To
install, drag each file into the Text Replacements list one at a time.
"""

import os
import plistlib

CHUNK_SIZE = 100

here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.dirname(here)
source = os.path.join(repo, "emojiSubstitutions.plist")
out_dir = os.path.join(repo, "plists", "chunks")


def main() -> None:
    with open(source, "rb") as f:
        entries = plistlib.load(f)

    os.makedirs(out_dir, exist_ok=True)
    for old in os.listdir(out_dir):
        if old.endswith(".plist"):
            os.remove(os.path.join(out_dir, old))

    for index in range(0, len(entries), CHUNK_SIZE):
        n = index // CHUNK_SIZE + 1
        path = os.path.join(out_dir, f"macmoji-{n:02d}.plist")
        with open(path, "wb") as f:
            plistlib.dump(
                entries[index : index + CHUNK_SIZE],
                f,
                fmt=plistlib.FMT_XML,
            )
        print(f"wrote {path}")

    print(f"{len(entries)} entries -> {(len(entries) + CHUNK_SIZE - 1) // CHUNK_SIZE} chunks of {CHUNK_SIZE}")


if __name__ == "__main__":
    main()
