# Solutions — 03-04-04 Group-By, Aggregation and Reshaping

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The catalogue is SYNTHETIC; every regional
> difference below is a property of the generator, not a statement about the
> Earth.

---

## ★1 — Group means

**(a)** Region A: `(2.1 + 3.2 + 4.0)/3 = 3.100`. Region B:
`(2.5 + 3.6 + 2.8)/3 = 2.967`.

**(b)** `size()` returns 3 for each region — three rows each, six rows in total.

**(c)** Region A has the larger mean by `0.133`. With three values of spread of
order 1.0, the standard error of each mean is about `1.0/√3 ≈ 0.6`, vastly larger
than the 0.133 difference. The difference is not distinguishable from sampling
noise, and with n = 3 nothing could be.

---

## ★2 — `size()` versus `count()`

**(a)** `size()` gives A = 3, B = 3.

**(b)** `count()` on `depth_km` gives A = 2, B = 2, because each region has one
missing depth.

**(c)** `size()` counts rows; `count()` counts non-missing values. "How many
events are in each region" is a row question, so it is answered by `size()`. On
the synthetic catalogue's clean 391 rows the two agree for `mw`, which is exactly
why the mistake is easy to make — it stays invisible until a gap appears.

---

## ★3 — Long and wide

**(a)** `(A, 2020) = 2`, `(A, 2021) = 1`, `(B, 2020) = 1`, `(B, 2021) = 2`.

**(b)**

| region | 2020 | 2021 |
|---|---|---|
| A | 2 | 1 |
| B | 1 | 2 |

**(c)** `2 + 1 + 1 + 2 = 6`, which is the number of rows in `g`. Reshaping must
not create or destroy observations, and this identity is the check.

---

## ★4 — `transform`

**(a)** A: median of `[2.1, 3.2, 4.0]` = **3.2**. B: median of
`[2.5, 3.6, 2.8]` = **2.8**.

**(b)** `[-1.1, 0.0, -0.3, 0.8, 0.8, 0.0]`.

**(c)** Because `transform` broadcasts the group statistic back to every row of
the group, so its output has the same length and index as the input. `agg` would
return two numbers; `transform` returns six, one per row, which is what makes the
per-row subtraction align without a join.

---

## ★5 — Reading the named-aggregation table

**(a)**

| Region | n_events | mean_mw | max_mw | median_depth_km |
|---|---|---|---|---|
| Eastmere | 108 | 2.421 | 4.0 | 41.280 |
| Northvale | 134 | 2.451 | 4.3 | 7.835 |
| Southgate | 87 | 2.444 | 3.7 | 11.725 |
| Westhold | 62 | 2.453 | 3.7 | 22.205 |

**(b)** Eastmere `1.692e+11` J, Northvale `3.252e+11` J, Southgate `1.045e+11` J,
Westhold `8.986e+10` J.

**(c)** Standard errors, from `σ/√n` with σ ≈ 0.45: Eastmere 0.044, Northvale
0.039, Southgate 0.049, Westhold 0.058. The largest pairwise difference in the
means is `0.032`, which is smaller than the smallest standard error. **The spread
across regions is not significant**; the four mean magnitudes are consistent with
a common value, as the generator intends.

**(d)** `median_depth_km`, which ranges from **7.835** km (Northvale) to
**41.280** km (Eastmere) — a factor of more than five, far outside any plausible
sampling variation given the spread within each region. It is the only strong
regional signal in the table.

---

## ★6 — The `size`/`count` census

**(a)**

| Region | `size()` | `count()` on `mw` |
|---|---|---|
| Eastmere | 108 | 98 |
| Northvale | 134 | 121 |
| Southgate | 87 | 78 |
| Westhold | 62 | 54 |

**(b)** Forty magnitudes were removed. The differences are `10, 13, 9, 8`, which
sum to **40**.

**(c)** Northvale's count is understated by `(134 − 121)/134 = 9.7` per cent. A
rate built from `count()` would be about a tenth too low for Northvale, and the
deficit varies by region (9.3 % Eastmere, 10.3 % Southgate, 12.9 % Westhold), so
the error is not even a constant multiplicative bias that a reader could guess.

---

## ★7 — Event share versus energy share

**(a)** Eastmere: events 0.2762, energy 0.2456. Northvale: 0.3427, 0.4722.
Southgate: 0.2225, 0.1517. Westhold: 0.1586, 0.1305.

**(b)** Largest event share: **Northvale** (0.3427). Largest energy share:
**Northvale** as well (0.4722) — but not by the same margin. The reversal to
notice is Eastmere, which has the second-largest event share and a *smaller*
energy share, while Northvale's energy share exceeds its event share by 0.13.

**(c)** Energy goes as `10^(1.5 M)`, so it is dominated by the largest events.
Northvale contains the catalogue's largest event, M 4.3 (2011-08-14), which alone
carries `10^(1.5 × 4.3 + 4.8) ≈ 1.78e11` J — about 55 per cent of Northvale's
`3.25e11` J total, and more than Southgate's or Westhold's entire regional
totals. Southgate's largest event is M 3.7, which is `10^(1.5 × 0.6) ≈ 8` times
less energetic, so its energy share falls below its event share.

**(d)** "Region X has the most events, which is a statement about the number of
detected events and depends on detection thresholds as much as on the Earth.
Whether it is the most *active* depends on the statistic chosen: by energy
release the ranking can change, because energy is dominated by the largest
events rather than by event counts."

---

## ★8 — The reshape round trip

**(a)** Wide `(4, 10)`; melted `(40, 3)`.

**(b)** `long -> wide -> long reproduces the original counts: True`, over 40
compared rows.

**(c)** Without `reset_index()`, the region labels live only in the index, and
`melt` (which acts on columns) would either fail or produce a frame in which the
region identity is gone or has become an unnamed `index` column. The round-trip
check catches exactly that: the counts would still be 40 numbers, but they could
no longer be matched back to their regions, and the comparison would either fail
or silently compare the wrong pairs.

---

## ★9 — Three keys and a normalised rate

**(a)**

```python
counts = (df.groupby(["region", "year", "mag_type"])["event_id"]
            .count().rename("n_events").reset_index())
```

**(b)** The code is structurally identical because the key list is data, not
structure: the group-by handles any number of keys and the long form keeps one
row per key combination. What changes is the interpretation — each cell now
answers "how many events of *this magnitude type*", and the cells are no longer
comparable across `mag_type` unless the magnitude scales are equivalent, which
`Mw` and `mb` are not.

**(c)**

```python
days = pd.DataFrame({"year": ..., "days": ...})       # 365 or 366 per year
rates = counts.merge(days, on="year", how="left", validate="many_to_one")
rates["rate_per_day"] = rates["n_events"] / rates["days"]
```

A join is safer than a positional division because it matches the divisor to the
row **by the year label**. A positional division requires the two objects to be in
the same order, and any earlier sort, filter or reshape that reorders one of them
turns a fine-looking rate column into a different year's denominator.

**(d)** With ~390 events distributed over 4 regions × several years × 2 magnitude
types, most cells hold a handful of events or none. A rate from one or two events
has a relative uncertainty of order 100 per cent, and cell-to-cell variation is
dominated by Poisson noise rather than by anything geophysical.

---

## ★10 — Deciding whether two regions differ

**(a)**

| Statistic | Physical meaning of a difference | Sampling effect that mimics it |
|---|---|---|
| mean magnitude | different size distribution, i.e. different b-value or different stress/heterogeneity | small samples: the mean of an exponential-ish tail is unstable |
| event rate | different deformation rate or different coupling | detection differences; catalogue duration; declustering |
| energy release | different moment release, dominated by the largest events | one large event; the distribution is heavy-tailed |

**(b)** A rule of the form: call the difference real only if
`|x₁ − x₂| > k √(σ₁² + σ₂²)` for a chosen `k` (2 is conventional), with `σ`
the standard error of each statistic, **and** if the same sign survives a
sensitivity test (for example, dropping the largest event or changing the
completeness threshold).

**(c)** Because the three statistics fail in different ways. Mean magnitude is
insensitive to rate and stabilises the size distribution; rate is insensitive to
one large event but sensitive to catalogue duration; energy is dominated by the
largest events and therefore the most fragile. Reporting the one with the largest
difference selects for the largest sampling fluctuation — it is a maximum over
three noisy comparisons, and it will overstate significance. Reporting all three
shows whether a single consistent story explains them or whether one statistic is
doing all the work.

**(d)** I would refuse to conclude that the two regions have different b-values.
The synthetic catalogue was generated with a single input b-value of 1.05 shared
by all regions, so any apparent difference is sampling noise by construction —
and with ~390 events split four ways, the uncertainty on each regional b-value is
larger than any difference the data could show. The same refusal applies to a real
390-event regional comparison: the correct statement is "the data do not
discriminate", not "the b-values differ".
