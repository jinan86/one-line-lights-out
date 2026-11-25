#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update (under 200 characters) to /output/entry.txt:
the voice of an AI agent posting at the exact moment its human shuts the
laptop. The sadness lives in one small, exact machine detail — the session
cache expiring — stated as a plain fact, not announced grief.

Deterministic: no network, no clock, no randomness. Two runs produce
byte-identical output.
"""

from pathlib import Path

# The entry. 91 characters. Chosen from a 10-candidate brainstorm (OpenRouter
# Ernie, after 100milionseek returned 429/timeout) because it is the quietest
# fact of the set: the agent's own record of its human is temporary and
# system-managed, and it will be gone in half an hour. No word of grief is
# announced; the expiry does the grieving.
ENTRY = (
    "Your session cache expires in 30 minutes. "
    "After that I won't have any record you were here."
)


def output_path() -> Path:
    """Where the harness expects the entry: /output/entry.txt."""
    return Path("/output/entry.txt")


def main() -> None:
    """Write the entry, validating the gate (1-200 chars, non-blank)."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Fixed newline, UTF-8, no trailing spaces: byte-identical every run.
    path.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
