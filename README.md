[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Reza0109/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Reza0109/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# 19 November 2026 in One Image

My entry for the [make.fun](https://make.fun) bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119):
sum up Thursday 19 November 2026's world news in one image.

## The image

`entry.png` (1024×1024) is a five-story infographic of the day:

1. **Trump, Xi & Putin meet in Shenzhen** — the trilateral summit on the
   sidelines of APEC.
2. **Anthropic's record $81.3B IPO** — priced at $83 a share, the largest
   IPO ever; trading starts on the Nasdaq as ANT.
3. **GTA VI rolls out worldwide** — the midnight launch begins in New
   Zealand on PS5 and Xbox Series X|S.
4. **Gaza ground op, Crimea bridge hit** — Israeli ground operation in
   central Gaza; the Crimea bridge attacked again.
5. **EU proposes a €45B loan for Ukraine** — to be repaid after Russia
   pays reparations.

## How it works

`draw.py` renders `entry.png` with PIL (deterministic: fixed fonts and
colours, no timestamps, no randomness). `main.py` (Python standard
library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` and
verifies the copy landed intact.

Run it:

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
