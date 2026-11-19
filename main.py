#!/usr/bin/env python3
"""Entry point for make.fun news-image-20261119.

Copies the pre-rendered entry.png (shipped in this repo) to the output
directory, then verifies the copy landed intact: the destination must
exist and its byte size must match the source exactly. Standard library
only: no network, no randomness, no clock, so repeated runs produce
byte-identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing from the repository: %s" % src)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    expected = os.path.getsize(src)
    if not os.path.isfile(dst):
        raise SystemExit("output entry.png was not created: %s" % dst)
    actual = os.path.getsize(dst)
    if actual != expected:
        raise SystemExit(
            "output entry.png size mismatch: expected %d bytes, got %d"
            % (expected, actual)
        )


if __name__ == "__main__":
    main()
