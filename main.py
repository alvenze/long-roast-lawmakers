"""Entry program for make.fun: The Long Roast.

Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt, roasting lawmakers
who would regulate AI, crypto or the internet but cannot convert a file
to PDF. The gate accepts UTF-8 text of 1 to 320 characters.
"""

import os

LINE = (
    'They are writing the law that will govern the internet\'s future, '
    'and the draft lives in a Google Doc shared with "anyone with the '
    'link", comment-only, so not even its authors can turn it into a PDF.'
)
MAX_CHARS = 320


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("roast line outside the 1-320 character gate")
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("roast line must be a single line with no padding")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("roast line must be exactly one sentence")
    if "PDF" not in LINE:
        raise ValueError("roast line must name the file they cannot convert")
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())


if __name__ == "__main__":
    main()
