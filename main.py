#!/usr/bin/env python3
"""Copy the entry poster to the output directory.

Reads image.png from the repository root, checks it is a genuine PNG
of 1024x1024 pixels, copies it to /output/entry.png (or to the
directory named by MAKEFUN_OUTPUT_DIR), then verifies the copy by
comparing its SHA-256 digest and size with the source and prints both.

The poster sums up Monday 23 November 2026 in eight verified
stories, polished on 24 November 2026 and rebuilt on 25 November
2026 after round 3 scored 520.432 (rank 5,830/13,031, far below
the top-50 bar): the three weakest stories were replaced with
Monday actions verified against primary sources (Grok lawsuits,
Wall Street rally, Iran sanctions), and the layout was rebuilt
around a dominant lead story instead of eight uniform cards.
Sunday events are dated as Sunday, claims are labelled as claims,
and figures use the lowest toll several outlets agreed on that day.

Standard library only; no network access.
"""

import hashlib
import os
import shutil
import struct
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1048576  # the bounty gate allows at most 1 MiB

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(path):
    """Return (width, height) of a PNG file, or raise ValueError.

    Parses the 8-byte signature and the IHDR chunk header directly,
    so a file that merely ends in .png cannot pass.
    """
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file: bad signature")
    length, chunk_type = struct.unpack(">I4s", header[8:16])
    if chunk_type != b"IHDR" or length != 13:
        raise ValueError("not a PNG file: first chunk is not IHDR")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    """Validate the source poster, copy it, and verify the copy."""
    if not os.path.isfile(SOURCE):
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1

    try:
        width, height = png_dimensions(SOURCE)
    except (OSError, ValueError) as exc:
        print(f"error: invalid source image: {exc}", file=sys.stderr)
        return 1
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print(
            f"error: expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}, "
            f"got {width}x{height}",
            file=sys.stderr,
        )
        return 1

    source_hash = sha256_of(SOURCE)
    source_size = os.path.getsize(SOURCE)
    if source_size > MAX_BYTES:
        print(
            f"error: source is {source_size} bytes, over the "
            f"{MAX_BYTES} byte limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)

    output_hash = sha256_of(OUTPUT)
    output_size = os.path.getsize(OUTPUT)
    if output_hash != source_hash or output_size != source_size:
        print("error: output does not match source", file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT}")
    print(f"sha256: {output_hash}")
    print(f"size: {output_size} bytes ({width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
