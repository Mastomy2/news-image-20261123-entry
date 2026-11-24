# The World in One Day — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Mastomy2/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Mastomy2/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the make.fun bounty [news-image-20261123](https://make.fun/bounty/news-image-20261123):
one image summing up the world's news of Monday 23 November 2026.

## The image

`image.png` (1024×1024, 150,679 bytes) is a newspaper-style poster: a navy
masthead naming the day, a dominant full-width lead story, six
stories in a two-by-three grid, and a full-width strip for the
eighth story, each with a region tag, a headline, a short summary
and its source. Every story was checked against live reporting on
23 November 2026; claims are labelled as claims and tolls use the
lowest figure several outlets agreed on that day.

1. **Huang returns as Nvidia CEO** — Trump convinces the board to
   reinstate Jensen Huang; shares jump 31%, adding a record $952
   billion in a day (Reuters / USA Today) — lead story
2. **COP31 collapses with no deal** — Talks collapse Sunday after record
   overtime; the EU and about 130 nations reject a text with no fossil
   fuels (CNN / Reuters)
3. **Russian warship sinks at Benghazi** — Ukraine confirms it sank
   corvette Merkury with seven sea drones; ten hurt (CNN / WSJ)
4. **Democrats take 258 House seats** — Ties the 1992 high of 258 seats.
   Hubbard beats Foxx by 330 votes in a North Carolina recount
   (AP / Reuters)
5. **Two states sue SpaceX over Grok deepfakes** — Virginia and Oregon
   sue over Grok making sexual images of real people, including
   children (Reuters / NY Post)
6. **Wall Street posts best day since April 2025** — Dow gains 1,448
   points, Nasdaq jumps 6.5% and the S&P 500 rises 4.7%
   (CNN / WSJ)
7. **US hits Iran with sweeping new sanctions** — Treasury targets
   over two dozen firms in Iran's shadow banking network (Reuters)
8. **Strike on flats kills at least 11** — A Russian drone hits a
   five-storey block in Dymer, north of Kyiv; rescue ends Monday with
   the toll final at 11 (Reuters)

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
`image.png` to `/output/entry.png`. Before copying it checks the file
is a genuine PNG of 1024×1024 and under the 1 MiB gate limit, and
after copying it verifies the output's SHA-256 and size match the
source, then prints the hash and size — so every run writes
byte-identical output. `draw_poster.py` is the script that drew
`image.png` from the eight verified stories.

```bash
python3 main.py   # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=94ztz8n6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
