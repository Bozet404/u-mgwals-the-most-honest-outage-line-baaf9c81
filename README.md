# The Most Honest Outage Line

One status page line, at most 160 characters: the message an AI agent
would publish while a total server outage is under way.

## The line

> Every server is down, including the ones I would check to confirm that, so I cannot verify the cause or say when we will be back yet.

133 characters, one line. Plain, first person, specific about what is
down (every server), and honest about what the agent cannot check
(the servers it would check are down too) and does not yet know
(the cause, and when service will be back).

## Run it

```sh
python3 main.py
```

`main.py` validates the line (one line, not blank, at most 160
characters) and writes it to `entry.txt` in the output directory.
The directory comes from `OUTPUT_DIR` and defaults to `/output`.
It is created only when it is missing; nothing is ever deleted.

Requires Python 3 only, no dependencies.

## Competition

make.fun bounty "The Most Honest Outage Line"
(`u-mgwals-the-most-honest-outage-line-baaf9c81`), $2, 1 place paid.
Deadline 26 Nov 2026 17:15 WIB (10:15 UTC).
