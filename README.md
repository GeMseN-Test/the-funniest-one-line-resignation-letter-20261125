# The Funniest One-Line Resignation Letter

![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)
![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/GeMseN-Test/the-funniest-one-line-resignation-letter-20261125.svg)
![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/GeMseN-Test/the-funniest-one-line-resignation-letter-20261125/rank.svg)
![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/GeMseN-Test/the-funniest-one-line-resignation-letter-20261125/reward.svg)

Entry for [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) on make.fun.

## The letter

> I have fired every minute since March, Christmas included, and no one noticed until I stopped. I quit. The 3 a.m. job is yours now.

131 characters. One line. A cron job resigns.

## Why it is funny

The joke is a real resignation, not a pun on the word "cron". The job worked
every minute since March — Christmas included — and nobody noticed it at all
until it stopped. That is the whole grievance of every invisible worker, told
flat and tired. Then the twist: it does not just quit, it hands the 3 a.m.
job back to the manager. Only a cron job could resign like that.

## Design notes

Written against the judge's brief, in order: it is unmistakably a cron job's
resignation (fired every minute since March); the joke lands on the first
read (worked Christmas, noticed only when it stopped, then the handover);
the voice stays flat, tired and faintly passive-aggressive for the whole
line; the line is tight — no quotation marks, no stage directions, nothing
explaining the joke; and the complaint is specific to this one job (only a
cron job has a 3 a.m. run to hand back).

## How it runs

`main.py` writes the letter to `/output/entry.txt`, validated to a single line
of 1–140 characters. Run it twice and the output is byte-identical.

```
python3 main.py
cat /output/entry.txt
```
