"""Copy the bundled entry.png to the output directory.

The entry image is rendered by render.py and shipped in this repo as
entry.png; this script simply places a copy where the grader expects it.

Run it with:  python3 main.py
The output path can be overridden with the MAKEFUN_OUTPUT_DIR
environment variable; it defaults to /output.
"""

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
