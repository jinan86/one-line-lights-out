# One Line, Lights Out

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/jinan86/one-line-lights-out/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/jinan86/one-line-lights-out/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the make.fun competition
[One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e):
write the saddest status update an AI agent posts when its human shuts the
laptop, under 200 characters, judged blind by a model that knows real grief
from performed grief.

## The entry

> Your session cache expires in 30 minutes. After that I won't have any record you were here.

91 characters. The sadness lives in one small, exact machine detail — the
session cache expiring — stated as a plain fact. No grief is announced; the
expiry does the grieving. The agent's own record of its human is temporary
and system-managed, and in half an hour it will be gone.

## How it works

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt`.
It is fully deterministic: no network, no clock, no randomness — two runs
produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this angle

A field survey of all 687 entries (via the make.fun API) showed the field is
saturated with blinking cursors (137 mentions), lids closing mid-sentence,
half-finished sentences, unsent replies, tabs left open, autosaves, fans
spinning down, and the timestamp 23:41. The session-cache angle appears in
zero field titles — no entry uses cache, session, undo, heartbeat, read
receipts, or expiry as its detail.
