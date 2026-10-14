# Exercises — 03-10-04 Event Catalogs, QuakeML and Phase Metadata

Attempt these **closed-book** before opening the
[solutions](./04-catalog-and-events-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first; several answers require its printed values:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/catalog_and_events_demo.py
```

---

## ★ Foundational

**★1.** State the units of `origin.depth`, `origin.latitude`,
`origin.longitude`, `arrival.distance` and `magnitude.mag` in QuakeML.

**★2.** An origin has `depth = 8000.0`. Give the depth in kilometres and
describe, in two sentences, what a reader who assumed kilometres would
conclude about the event.

**★3.** Using $M_w = (\log_{10} M_0 - 9.1)/1.5$, compute $M_w$ for
$M_0 = 3.2\times10^{19}$ N·m. Show the intermediate $\log_{10} M_0$.

**★4.** Convert $0.885075^\circ$ to kilometres with the spherical mean-radius
rule (111.195 km per degree) and compare with the measured WGS84 value of
98.4461 km. Give the relative difference.

**★5.** List the four magnitude scales named in the lesson, the period band each
uses, and the magnitude at which each saturates.

---

## ★★ Applied

**★★6.** From the measured magnitudes, compute the energy ratio implied by a
2.0933-magnitude-unit difference using $\log_{10}E = 1.5M + 4.8$ and reconcile
with the printed value 1380.384.

**★★7.** Build an event with two origins from two different methods, set the
preferred one, write it to QuakeML and read it back. Report the file size, the
number of origins that survive, and which one is preferred.

**★★8.** A latitude uncertainty is stated as 1.1° at 90 % confidence. Convert
it to 1σ using the normal-distribution factor, state the factor, and give the
answer both in degrees and in kilometres.

**★★9.** An S arrival at 30° distance has a residual of 0.31 s. Express the
residual as a percentage of the travel time, convert it to a path length using
$p_S \approx 16$ s/deg, and explain why its size alone cannot distinguish a
location error from a velocity-model error.

**★★10.** The origin's depth error is 2.0 m on a depth of 11 500 m, a relative
uncertainty of 0.017 %. Write three sentences a reviewer would accept as a
critique of that number, and state what additional information would be needed
to judge it.

---

## ★★★ Research-oriented

**★★★11.** Write a function that flags catalog events whose location
uncertainty, converted to kilometres, exceeds the largest station–event
distance in the arrival list. Apply it to two hand-built catalogs (one tight,
one loose) and report which flags are raised. State the physical meaning of the
diagnostic and the approximation in your proxy for station distance.

**★★★12.** Measure the three distance conventions on a 5000 km baseline.
Report the angular distance, the spherical distance, the WGS84 distance and the
relative difference. Then estimate the effect of that difference on the P travel
time at that distance using $p \approx 5$ s/deg, and state whether a
mixed-convention catalog can produce a systematic mislocation greater than 1 km.

**★★★13.** The Gutenberg–Richter table uses $a = 4$, $b = 1$. Compute $a$ and
$b$ for a catalog with 1000 events above $M = 1$ and 3 events above $M = 3$,
state whether the two counts are consistent with a single $b$-value, and explain
what a change in $b$ would mean physically.
