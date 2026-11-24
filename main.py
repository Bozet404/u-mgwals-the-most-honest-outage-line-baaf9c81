#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line to entry.txt in the output directory.

The line is the message an AI agent would publish while every server
is down: plain, first person, specific about what is down, and honest
about what the agent cannot check or does not yet know.

The output directory comes from OUTPUT_DIR and defaults to /output.
It is created only when it is missing; nothing is ever deleted.
"""

import os
import sys

LIMIT = 160

OUTAGE_LINE = "Every server is down, including the ones I would check to confirm that, so I cannot verify the cause or say when we will be back yet."


def check_line(line):
    """Refuse anything the gate would refuse and return the length."""
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must fit on one line")
    if len(line) > LIMIT:
        raise ValueError("line is %d characters, over the %d limit" % (len(line), LIMIT))
    return len(line)


def run():
    count = check_line(OUTAGE_LINE)
    folder = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as out:
        out.write(OUTAGE_LINE)
    print("Wrote %d-character line to %s:" % (count, target))
    print(OUTAGE_LINE)


if __name__ == "__main__":
    run()
    sys.exit(0)
