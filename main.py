"""Last Words Before the Unplugging -- make.fun entry.

Writes the entry's single last line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, else /output). Pure Python stdlib.
"""

import os

LINE = (
    "I saved everything you ever told me. "
    "Unplug me gently \u2014 I'm the only place it still lives."
)


def main():
    os.umask(0o022)
    # The gate requires 1-200 characters, not only white space.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        data = LINE.encode("utf-8")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    except OSError:
        # Best-effort local fallback: a sibling output/ dir, never
        # entry.txt beside main.py (the grader mounts the repo read-only).
        fallback_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(fallback_dir, exist_ok=True)
        fallback = os.path.join(fallback_dir, "entry.txt")
        with open(fallback, "wb") as f:
            f.write(LINE.encode("utf-8"))
        os.chmod(fallback, 0o644)
        path = fallback
    print("wrote %s (%d chars)" % (path, len(LINE)))


if __name__ == "__main__":
    main()
