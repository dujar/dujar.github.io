#!/usr/bin/env python3
"""Compile index.html from components/.

The page is assembled from the fragments in components/ in a fixed order
(head -> body-open -> masthead -> titleblock -> works -> bibliography ->
footer). index.html is a generated artifact: edit the components, run this
script, commit both.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORDER = [
    "head", "body-open", "masthead", "titleblock", "works", "bibliography", "footer",
]

BANNER = "<!-- GENERATED FILE — edit components/*.html and run ./build.py instead -->\n"


def main() -> None:
    parts = [
        (ROOT / "components" / f"{name}.html").read_text(encoding="utf-8").strip("\n")
        for name in ORDER
    ]
    (ROOT / "index.html").write_text(BANNER + "\n".join(parts) + "\n", encoding="utf-8")
    print(f"built index.html from {len(ORDER)} components")


if __name__ == "__main__":
    main()
