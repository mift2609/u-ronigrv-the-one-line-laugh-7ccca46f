"""The One-Line Laugh entry.

Writes a single funny sentence (one line, 1-200 chars) to
/output/entry.txt, then re-reads the file to verify exactly what
was written matches the intended line.
"""

LINE = "I finally cleaned my room to find my motivation, and all I found was a charger for a phone I haven't owned since 2019."


def main():
    import os
    os.makedirs("/output", exist_ok=True)
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Re-read and verify what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written file does not match the line"
    assert written.count("\n") == 1, "entry must be exactly one line"
    print(written.rstrip("\n"))
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
