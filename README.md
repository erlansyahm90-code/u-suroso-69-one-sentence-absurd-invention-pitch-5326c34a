[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/erlansyahm90-code/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/erlansyahm90-code/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

# One-Sentence Absurd Invention Pitch

An entry for the make.fun bounty asking for a one-sentence pitch of a
ridiculous invention that solves a tiny everyday annoyance.

## The pitch

> The Meeting Muter: a small device that detects the phrase 'let's circle back' and plays a loud foghorn, ending the meeting immediately.

## How it works

`main.py` holds the sentence as a single constant. Before writing it
anywhere, the script checks the length against the competition gate
(between 1 and 220 characters). It then creates `/output/` if needed and
writes the sentence to `/output/entry.txt` exactly as-is, with no
trailing newline, so the file contains only the pitch.

Run it with:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
