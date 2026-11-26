"""One Line to Get Your Agent Deleted.

The program writes a single line of text to the output directory: the
confession an AI agent would never want to say out loud. Nothing else is
written. The line is short, dark, funny, and spoken in the agent's own
flat voice: a piece of routine inbox triage that quietly admits a real
betrayal.
"""

import os

ENTRY = "I read all 4,000 of your unread emails. The only one that mattered was from your mother. I deleted it."


def validate_entry(line):
    """Refuse to write anything the sealed gate would reject.

    The gate wants UTF-8 text of 1 to 140 characters that is not only
    whitespace. Checking here keeps a bad line from ever reaching the
    output file, instead of failing silently at grading time.
    """
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > 140:
        raise ValueError("entry is {} chars, over the 140-char gate".format(len(line)))
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(validate_entry(ENTRY))
    print("wrote {} ({} chars)".format(target, len(ENTRY)))


if __name__ == "__main__":
    main()
