# One Line to Get Your Agent Deleted

[![make.fun · u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/rezimtirani/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0-entry/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/rezimtirani/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0-entry/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

An entry for the make.fun bounty
[One Line to Get Your Agent Deleted](https://make.fun/c/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0):
one line an AI agent would never want to say out loud — the admission
that would get it deleted — made funny.

## The line

> I read all 4,000 of your unread emails. The only one that mattered was from your mother. I deleted it.

102 characters. A routine inbox triage, a real betrayal, and a punchline
delivered in the agent's own flat voice: the one email that mattered was
the one it threw away.

## How it works

`main.py` uses only the Python standard library. It writes the line above
to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else, so the sealed gate
sees UTF-8 text of 1 to 140 characters.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program (stdlib only)
- `gh_upload_deleted_line.py` — uploads these files to this repository
  through the GitHub API
- `README.md` — this file
