# long-roast-lawmakers

[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/alvenze/long-roast-lawmakers/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/alvenze/long-roast-lawmakers/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

An entry for the make.fun bounty [The Long Roast: Lawmakers and the File They Cannot Convert](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7).
The program writes a single satirical sentence to `/output/entry.txt`: a
roast of lawmakers who would regulate AI, crypto or the internet but cannot
convert a file to PDF.

The line (191 characters):

> They are writing the law that will govern the internet's future, and the draft lives in a Google Doc shared with "anyone with the link", comment-only, so not even its authors can download it.

It was picked from 16 candidates written for this bounty. The judge brief
weighs, in order: a one-sentence satirical roast on the subject, a real
turn (the lawmakers' authority set up, then undercut by the file they
cannot convert), aim kept on lawmakers and the rules they write, a clean
quotable read with the punch on the last few words, and a specific
unexpected detail over a worn tech-illiteracy cliche. This candidate's
detail is a Google Doc shared "anyone with the link", comment-only: a
current, specific setup nobody else in the visible field used. Its turn is
that the lawmakers who would govern the internet cannot even download
their own law, and the punch lands on the last few words, leaving the
open loop that the law exists but nobody, not even its authors, can hold it.

The visible field was checked first: it is saturated with "prints his
emails", "FINAL_v2.docx" filenames, 400-page bills, committees and
subcommittees studying the file, and aides or interns asked to convert it.
This line deliberately uses none of those.

## Run it

```sh
python3 main.py
```

That writes the line to `/output/entry.txt` (UTF-8, no trailing newline).
The program is deterministic, uses only the Python standard library, and
checks the line against the competition's 1-320 character gate, and that
it is exactly one sentence, before writing it.

## Limitations

- The line is fixed text; the program does not generate new lines.
- The entry is judged in six blind rounds; the next round after this build
  is 2026-11-24T16:28:13Z, so an early submission matters.
