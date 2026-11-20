# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/yzrzlrizal-blip/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/yzrzlrizal-blip/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that writes one image summing up 20 November 2026 world news. `render.py` draws a 1024×1024 newspaper front page — masthead, lead story, and seven more stories — using only the Python standard library, Pillow, and DejaVu fonts. No photographs, no network, no third-party artwork: every mark on the page is a drawn shape or text. `main.py` copies the bundled `entry.png` to the output directory.

## Run it

```bash
python3 render.py   # regenerate entry.png
python3 main.py     # copy entry.png to /output/entry.png
```

Set `MAKEFUN_OUTPUT_DIR` to change where `main.py` writes the image.

## How the image is built

`render.py` lays out the page top to bottom: masthead, a full-width lead
story, two-column and three-column story rows, a briefs strip, and a
sources footer. Headlines use DejaVu Serif Bold, body copy DejaVu Sans,
and every story sits in its own ruled box so nothing overlaps. The output
is deterministic — re-running `render.py` produces a byte-identical PNG.

## Stories covered

- **Lead — Trump pushes Iran decision to 2027:** "We'll see what happens after January 1," the president said, putting off any call on renewed strikes until next year. The war has already cost the US more than $48bn.
- **Three nuclear powers, one table:** Trump, Xi and Putin held their first-ever three-way summit at APEC in Shenzhen, with nuclear arms control on the agenda after New START expired in February.
- **ICJ: Myanmar committed genocide:** the UN's top court ruled 9–6 that Myanmar's 2017 crackdown on the Rohingya was genocide — the first time the court has held a state responsible for the crime.
- **Voyager 1, one light-day away:** NASA confirmed the probe, launched in 1977, is now a full light-day (16 billion miles) from Earth; a radio signal takes 24 hours to reach home.
- **Cyclone Akvan:** about 300,000 people evacuated in Odisha as the severe cyclone bore down on the coast near Gopalpur, with winds of 90–100 km/h.
- **GTA 6 beats The Odyssey:** Grand Theft Auto VI took an estimated $1.84bn on launch day, passing the entire $1.805bn global box-office run of Christopher Nolan's The Odyssey.
- **Europe ready to talk to Russia:** at the Coalition of the Willing summit in Berlin, European leaders said they are ready for negotiations with Russia to end the war in Ukraine.
- **Hayabusa2 loses its landing:** engine trouble forced JAXA to scrap the probe's planned 2031 landing on asteroid 1998 KY26; it will fly past a smaller asteroid in April 2028 instead.
- **Also in the news:** South Korea's top court overturns ex-PM Han Duck-soo's conviction; a Houthi attack damages the Saudi wealth-fund tower in Riyadh; the US and Venezuela restore military cooperation; North Korea expands uranium enrichment at Yongbyon; Fiji declares a national disaster over drought.

## Sources

- Reuters (via SRN News), "Trump eyes 2027 to 'see what happens' with Iran": https://srnnews.com/trump-eyes-2027-to-see-what-happens-with-iran/
- Reuters, "Trump says US will 'see what happens' in conflict with Iran after January 1": https://985theriver.com/2026/11/19/trump-says-us-will-see-what-happens-in-conflict-with-iran-after-january-1/
- The Hindu BusinessLine, "Xi, Trump, Putin to hold first-ever trilateral meet on Nov 19": https://www.thehindubusinessline.com/news/world/xi-trump-putin-to-hold-first-ever-trilateral-meet-on-nov-19/article71706732.ece?utm_source=non-amp&utm_medium=quickdiscovery&utm_campaign=article
- Amnesty International, "Historic UN ruling that Myanmar committed genocide against Rohingya": https://www.amnestyusa.org/press-releases/historic-un-ruling-that-myanmar-committed-genocide-against-rohingya-is-rare-victory-for-survivors/
- UN Independent Investigative Mechanism for Myanmar, "ICJ – The Gambia v. Myanmar": https://iimm.un.org/en/icj-gambia-v-myanmar
- NASA, "NASA's Voyager 1 Makes History Reaching One Light-Day From Earth": https://www.nasa.gov/news-release/nasas-voyager-1-makes-history-reaching-one-light-day-from-earth/
- ScienceAlert, "It's Official! Voyager 1 Is The First Spacecraft To Reach One Light-Day From Earth": https://www.sciencealert.com/its-official-voyager-1-is-the-first-spacecraft-to-reach-one-light-day-from-earth
- Wikipedia, "Cyclone Akvan": https://en.wikipedia.org/wiki/Cyclone_Akvan
- Daily Prabhat (ANI), "Odisha CM reviews Cyclone Akvan preparedness; over 3 lakh evacuated": https://www.dailyprabhat.com/odisha-cm-reviews-cyclone-akvan-preparedness-over-3-lakh-evacuated-47-trains-cancelled/
- 80.lv, "Report: GTA 6 Generated Nearly $2B in Sales by Launch Day": https://80.lv/articles/report-gta-6-generated-nearly-usd2b-in-sales-by-launch-day
- Collider, "'GTA 6' Officially Defeats Christopher Nolan's 'The Odyssey' in Just 1 Day": https://collider.com/gta-6-overtakes-christopher-nolan-the-odyssey-sales/
- The Brief (via BBC), "European Leaders Say They Are Ready for Talks With Russia on Ending the Ukraine War": https://www.thebrief.news/en/standard/article/45599/european-leaders-say-they-are-ready-for-talks-with-russia-on-ending-the-ukraine-war
- Asia Daily, "Hayabusa2 targets tiny asteroid in 2028 after engine...": https://asiadaily.org/news/18996/
- EuropeSays, "No more asteroid landing: Engine trouble forces Japan's Hayabusa2 probe to change plans": https://www.europesays.com/japan/127404/

<sub>Entered on [make.fun](https://make.fun/?ref=wdbz3sg5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
