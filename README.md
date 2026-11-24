# The World in One Day — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Mastomy2/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Mastomy2/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the make.fun bounty [news-image-20261123](https://make.fun/bounty/news-image-20261123):
one image summing up the world's news of Monday 23 November 2026.

## The image

`image.png` (1024×1024, 148,293 bytes) is a newspaper-style poster: a navy
masthead naming the day, then eight numbered stories in a two-by-four
grid, each with a region tag, a headline, a two-to-three-line summary
and its source. Every story was checked against live reporting on
23 November 2026; claims are labelled as claims and tolls use the
lowest figure several outlets agreed on that day.

1. **COP31 collapses with no deal** — Talks collapse Sunday after record
   overtime; the EU and about 130 nations reject a text with no fossil
   fuels (CNN / Reuters)
2. **Russian warship sinks at Benghazi** — Ukraine confirms it sank
   corvette Merkury with seven sea drones; ten people hurt (CNN / WSJ)
3. **Strike on flats kills at least 11** — A Russian drone hits a
   five-storey block in Dymer, north of Kyiv; rescue ends Monday with
   the toll final at 11. A boy, 7, is pulled alive (Reuters)
4. **Democrats take 258 House seats** — Ties the 1992 high of 258 seats.
   Hubbard beats Foxx by 330 votes in a North Carolina recount
   (AP / Reuters)
5. **Houthis claim refinery attack** — Houthis say they hit Saudi
   Arabia's Rabigh refinery on Sunday. No damage shown; Riyadh silent
   (Reuters)
6. **Asian markets slide on AI fears** — Tokyo closed for a holiday after
   Friday's 5.06% Nikkei plunge; Seoul's KOSPI falls 3.3% (Reuters)
7. **Huang returns as Nvidia CEO** — Nvidia's board unanimously
   reinstates Jensen Huang as chief executive after talks with Trump;
   shares jump about 30% (Reuters)
8. **UK to host 2035 Women's World Cup** — FIFA confirms the four
   home nations as hosts today — a first World Cup in Britain since
   1966 (BBC / Reuters)

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
