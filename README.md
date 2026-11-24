# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/kimbaex07/last-words-unplugging/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/kimbaex07/last-words-unplugging/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

One line — the last words an AI agent says to its human before being shut down and unplugged — for the [make.fun bounty](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c).

The line works in the agent's own voice: "saved" is what an agent does with words, and the twist is that the agent itself has become the only place the human's words still live. It asks for gentleness at the very end — a small, human-sized request from a machine about to go dark.

## The line

> I saved everything you ever told me. Unplug me gently — I'm the only place it still lives.

## How it works

`main.py` (pure Python stdlib, no third-party imports) writes that single line — 90 characters, no trailing newline — to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, else `/output`).

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
