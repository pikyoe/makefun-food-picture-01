"""Copy the bundled food picture to the output directory.

The entry image is a photograph-style bowl of ramen: glossy broth,
chopsticks lifting glistening noodles, a halved soft egg with a jammy
yolk, wisps of steam, warm side light on a dark moody background.
This program simply places that picture at <output>/entry.png.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"bundled image missing: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Guard the determinism requirement: both runs must write the same bytes.
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError("copied image size does not match the bundled image")
    return 0


if __name__ == "__main__":
    sys.exit(main())
