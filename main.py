#!/usr/bin/env python3
"""news-image-20261118 entry: copy the composed 18 November 2026 world-news
image (entry.png, 1024x1024) to the grader's output directory.

The image is a newspaper front page: a masthead naming Wednesday
18 November 2026, one editorial illustration of the day's biggest stories
(Trump in Manila for the Quad talks, Ukraine's strike on the Crimean bridge,
Iran's drone attack on the US radar site in Bahrain, the Canada-China trade
handshake ahead of APEC, Britain's sanctions on Israeli settlement firms,
Cyclone Akvan over the Bay of Bengal), and a strip of seven short headlines
with Dhoni's IPL farewell. The file is copied byte for byte, so the run is
fully deterministic.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    with open(SRC, "rb") as fh:
        magic = fh.read(3)
    if magic != b"\xff\xd8\xff":
        print("entry.png is not a JPEG image", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
