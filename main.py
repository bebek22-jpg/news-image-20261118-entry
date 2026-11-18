"""news-image-20261118 entry program.

Copies the pre-drawn front-page image (entry.png) to the output directory
as /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png). Deterministic,
no network, standard library only.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"entry image missing: {src}")
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
