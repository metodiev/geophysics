# Solutions — 24-01-05 Keeping Up

> Read after attempting. Numbers computed. Lesson:
> [05 Keeping Up](../05-keeping-up-with-literature.md).

---

## ★1 — Volume arithmetic

Daily rate $= 2.0 + 6.0 + 15.0 + 0.5 = 23.5$ items/day.

$$V_{\text{week}} = 7 \times 23.5 = 164.5\ \text{items/week},$$
$$V_{46} = 164.5 \times 46 = 7567\ \text{items per 46-week year}.$$

At $6\ \mathrm{min}$ per item:

$$7567 \times 6\ \mathrm{min} = 45\,402\ \mathrm{min}
= 756.7\ \text{h per year},$$

i.e. $16.4\ \mathrm{h}$ per week — about two full working days a week, from four
sources and no journal reading of your own.

---

## ★2 — Relevant items

$$164.5 \times 0.04 = 6.58\ \text{relevant items/week},$$
$$6.58 \times 46 = 302.7\ \text{relevant items/year}.$$

Of the $756.7\ \mathrm{h}$ budget in ★1, the $302.7$ relevant items are what you
are actually there for: roughly $2.5\ \mathrm{h}$ of reading per relevant item, if
the entire budget were spent on triage.

---

## ★3 — A filter with precision $0.40$, recall $0.70$

$$\text{relevant kept} = 0.70 \times 987 = 690.9 \approx 691\ \text{items},$$
$$\text{items kept} = \frac{690.9}{0.40} = 1727\ \text{items},$$
$$\text{reading hours} = \frac{1727 \times 6}{60} = 172.7\ \mathrm{h},$$
$$\text{missed} = 987 - 690.9 = 296.1\ \text{items}
= \frac{296.1}{987} = 30.0\%\ \text{of the relevant set}.$$

A $9.3\times$ time saving for a $30\%$ miss rate. The filter is only as good as the
recall you are willing to accept, and that number belongs in the policy sentence.

---

## ★4 — Cap with and without filtering

Unfiltered: $V = 500$ items/week, $25$ relevant items/week. With cap $C = 50 < V$,
the opened fraction is $50/500 = 10\%$, so

$$R_{\text{unfiltered}} = 0.10 \times 500 \times 0.05 = 2.5\ \text{relevant items/week}.$$

Filtered: $60$ items/week kept, $24$ relevant. With the same cap $C = 50 < 60$,
the opened fraction is $50/60 = 83.3\%$, so

$$R_{\text{filtered}} = 0.833 \times 60 \times 0.40 = 20.0\ \text{relevant items/week}.$$

$$\text{ratio} = \frac{20.0}{2.5} = 8.0 .$$

The cap is identical in both cases; the filter changed what the cap saw. Note also
the internal consistency: $24$ relevant kept out of the stream's $25$ relevant
items is a recall of $96\%$, so the stated precision and recall are compatible.

---

## ★5 — The cap needed to match a filter

Filtered stream at full coverage: $21.0$ relevant items/week un-filtered, at
precision $0.534$, gives

$$R_{\text{filtered}} = 21.0 \times 0.534 = 11.21\ \text{relevant items/week}.$$

Unfiltered, with a cap $C < V = 349$ items/week, the reached count is

$$R_{\text{unfiltered}} = \frac{C}{V}\times V \times 0.06 = 0.06\,C .$$

Setting $0.06\,C = 11.21$ gives

$$C = \frac{11.21}{0.06} = 186.8 \approx 187\ \text{items/week}.$$

So matching the filtered stream's reach without a filter requires opening $187$
titles and abstracts a week — about $18.7\ \mathrm{h}$ of triage, or half of a
working week, every week. This is the quantitative case for filtering: it buys back
the equivalent of a large cap.

---

## ★6 — Two filters compared

| | Kept items/year | Relevant/year | Hours/year | Minutes per relevant |
|---|---|---|---|---|
| (a) | $1456$ | $777$ | $145.6$ | $11.24$ |
| (b) | $700$ | $620$ | $70.0$ | $6.77$ |

$$(a):\ 1456 \times 6 / 60 = 145.6\ \mathrm{h},\quad
\frac{1456\times 6}{777} = 11.24\ \mathrm{min};$$
$$(b):\ 700 \times 6 / 60 = 70.0\ \mathrm{h},\quad
\frac{700\times 6}{620} = 6.77\ \mathrm{min}.$$

Filter (b) forgoes $777 - 620 = 157$ relevant items a year and saves
$145.6 - 70.0 = 75.6\ \mathrm{h}$, at a lower cost per relevant item found. Whether
that is a good trade depends on the value of the marginal relevant item, which is
exactly the judgement the arithmetic exposes.

---

## ★7 — Measuring your own filter's precision

**Stream and cap.** Fix the sources, the filter and the cap ($25$ items/week) for
eight weeks, and log every kept item with its date.

**Outcome.** An opened item counts as *useful* if, within the eight weeks, it is
(a) added to the project's bibliography and cited in a draft, (b) used to change a
method, or (c) forwarded as directly relevant to a collaborator. Fix the list in
advance and record the reason for each judgement.

**Avoiding circularity.** The filter must be frozen before the experiment starts;
if you tune keywords during the eight weeks, the measured precision is a
post-hoc property of the final filter, not a prospective one. Log every tuning
event and report the experiment as split at that point.

**Confound.** The project's own progress changes what counts as useful: early in a
project almost anything on the method is new, and late in a project almost nothing
is. Report the recall/precision against the project's phase, or run the experiment
twice, at two phases, and report both.

---

## ★8 — Separating volume from fatigue

**Treatment.** Two arms over eight weeks: a capped daily digest (up to $5$
items/day) versus a continuous stream with the same weekly total, identical items
and identical filter. What differs is the *arrival pattern*, not the volume.

**Unit of randomisation.** The participant-week, with each participant
experiencing each arm in a crossover (four weeks per arm, order randomised), because
fatigue is a within-person phenomenon and between-person comparisons confound it
with disposition.

**Sample size.** The outcome is the opened fraction per participant-week, with a
within-person standard deviation typically larger than the between-arm difference.
For a difference of $0.10$ in opened fraction with a within-person SD of $0.15$,
the paired sample size at $80\%$ power is

$$n = \frac{(1.96+0.842)^{2}\times 0.15^{2}}{0.10^{2}}
= \frac{7.851 \times 0.0225}{0.01} = 17.7 \approx 18\ \text{participant-pairs},$$

i.e. $18$ participants over $8$ weeks — a real study, not an anecdote.

**Outcome.** Opened fraction per week, and the number of items opened *and* logged
as useful. Report both, because a digest can raise opened fraction while lowering
throughput if it changes the mode of reading from scanning to reading.

**Why within-person.** Between-person designs cannot separate fatigue from the
stable differences between readers (disposition, workload, field breadth), which
are much larger than the treatment effect. Crossover also makes the volume
identical across arms, so any difference must come from arrival pattern.
