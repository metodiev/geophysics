# Solutions — 04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — A moderate magnitude

**(a)** $N(\ge 6) = 20\times10^{-1\times(6-4)} = 20\times10^{-2} = 0.2$ per year.

**(b)** $1/0.2 = 5$ years.

**(c)** $P = 1 - e^{-0.2\times50} = 1 - e^{-10} = 0.99995$, which the demo prints
as `1.000`.

**(d)** Because the Poisson process is memoryless: each year independently offers
a 20 per cent chance, and "not in 50 years" has probability $e^{-10} = 4.5\times
10^{-5}$, not zero. The interval is an average, not a guarantee.

---

## ★2 — A larger magnitude

**(a)** $N(\ge 7) = 20\times10^{-3} = 0.02$ per year.

**(b)** Interval 50 years; $P = 1 - e^{-0.02\times50} = 1 - e^{-1} = 0.632$.

**(c)** The interval divided by the window is $50/50 = 1$, but the probability is
0.632. The linear approximation holds only when the rate is small compared with
the window, and here the expected number of events in the window is exactly 1, so
the exponential is far from linear.

**(d)** The probability — or, more precisely, the ground-motion level associated
with a stated probability of exceedance. An interval says nothing about the
exposure time of the structure being designed.

---

## ★3 — Tsunami speed

**(a)** $c = \sqrt{9.81\times3000} = 171.6$ m/s $= 171.6\times3.6 = 618$ km/h.

**(b)** $6000\times10^3/171.6 = 3.497\times10^4$ s $= 9.72$ hours.

**(c)** $c = \sqrt{9.81\times200} = 44.3$ m/s $= 160$ km/h.

**(d)** Because the shallow-water speed follows from the depth and gravity only —
it is the speed of a long wave in a layer of fluid, like the speed of sound in a
gas, and it is independent of how large the wave is or how it was made.

---

## ★★4 — A $b$-value

**(a)** $b = \log_{10}e/(3.43-3.00) = 0.4343/0.43 = 1.010$.

**(b)** $0.4343/0.60 = 0.724$.

**(c)** $0.4343/0.30 = 1.448$.

**(d)** The 3.30 case, because an artificially low mean magnitude for the same
$M_c$ is what a catalogue with missing large events would look like — or, more
commonly, the 3.60 case with a mean pulled *up* by missing small events. Which of
the three is biased cannot be decided from the $b$-value alone: it needs a
completeness analysis on the catalogue, which is exactly the point.

---

## ★★5 — Completeness bias

**(a)** $b = 0.4343/(3.43-3.20) = 0.4343/0.23 = 1.888$.

**(b)** The value is much *higher* (steeper) than the 1.010 of ★★4(a), because
raising $M_c$ without changing the magnitudes shrinks the denominator.

**(c)** A steeper $b$ means the rate falls faster with magnitude, so the implied
rate of $M\ge6$ is much *lower* — by a factor of order $10^{(1.888-1.010)\times3}
= 10^{2.6}$, i.e. more than two orders of magnitude, once both analyses are
anchored to the same rate at their own completeness magnitude. That is the size
of the error a completeness mistake can introduce.

**(d)** A completeness analysis determines, as a function of time and magnitude,
the level above which the catalogue is complete — usually from the departure of
the observed magnitude–frequency curve from a straight line. The demo shows the
consequence of skipping it: a $b$-value of 0.696 against a true 1.0, and a
large-event rate that is wrong by orders of magnitude.

---

## ★★6 — Shoaling

**(a)** $(5000/25)^{1/4} = 200^{0.25} = 3.76$.

**(b)** $9.0/3.76 = 2.39$ m offshore.

**(c)** $(4000/25)^{1/4} = 160^{0.25} = 3.56$.

**(d)** Two of the effects Green's law ignores:

- **Harbour and shelf resonance**, which can amplify the height by a further
  factor of several at a particular period — and can also *reduce* it, if the
  period is not near a resonance.
- **Run-up on a beach and overland flow**, which usually *raises* the maximum
  inundation height above the value at the beach line, and is the quantity that
  matters for evacuation.

---

## ★★★7 — A moment-balanced recurrence

**(a)** $A = 6.0\times10^5\times1.2\times10^5 = 7.2\times10^{10}$ m²;
$v = 70\times10^{-3}/3.15576\times10^7 = 2.218\times10^{-9}$ m/s;
$\dot M_0 = 3\times10^{10}\times7.2\times10^{10}\times2.218\times10^{-9}
= 4.791\times10^{12}$ N·m/s $= 1.512\times10^{20}$ N·m/a.

**(b)** The bracket is
$10^{4.75} - 10^{3.0} = 5.6234\times10^4 - 1.000\times10^3
= 5.5234\times10^4$, so the denominator is
$2\times1.2589\times10^9\times5.5234\times10^4 = 1.3906\times10^{14}$ and
$10^a = 1.512\times10^{20}/1.3906\times10^{14} = 1.087\times10^6$, giving
$a = 6.036$.

**(c)** The rate of $M_w\ge8$ is $10^{6.036-8} = 1.087\times10^{-2}$ per year, so
the mean interval is **92 years**.

**(d)** With 60 per cent coupling, $a$ falls by $\log_{10}(1/0.6) = 0.2218$ to
5.814 and the interval rises to **153 years**.

**(e)** The naive calculation would attribute the whole $1.512\times10^{20}$ N·m/a
to $M_w$ 8 events, each of $1.259\times10^{21}$ N·m, giving an interval of
$1.259\times10^{21}/1.512\times10^{20} = 8.3$ years. That is a **lower bound** on
the true interval for $M_w\ge8$, because it assumes every event is at least
$M_w$ 8 and that nothing else ever occurs; any real magnitude distribution spends
part of the budget on smaller events, leaving less for the largest ones and
lengthening the interval. The balanced value of 92 years is 11 times longer,
which is the quantitative statement of how wrong the naive calculation is.

---

## ★★★8 — The demo's output

**(a)** Complete catalogue at $M_c = 2.0$: `b = 0.999` against an input of 1.000
(−0.1 per cent). Incomplete catalogue: `b = 0.696` at $M_c = 2.0$ (wrong) and
`b = 0.996` at $M_c = 3.0$ (right).

**(b)**

| $M$ | rate (per a) | mean interval (a) | $P(\ge1$ in 50 a$)$ |
|---|---|---|---|
| 5.0 | 1 | 1 | 1.000 |
| 7.0 | 0.01 | 100 | 0.393 |
| 9.0 | 0.0001 | 10 000 | 0.005 |

**(c)** Area `1.500e+11 m^2`; moment rate `8.556e+12 N m/s` and
`2.700e+20 N m/a`; intercept `a = 6.288`.

**(d)** $M\ge6$: `1.941` per a, interval 1 a; $M\ge7$: `0.1941`, 5 a;
$M\ge8$: `0.01941`, 52 a; $M\ge9$: `0.001941`, 515 a.

**(e)** Naive intervals: $M_w$ 7.5 `0.8 a`, 8.0 `4.7 a`, 8.5 `26.2 a`,
9.0 `147.4 a`.

**(f)** At 4000 m: `198.1 m/s = 713.1 km/h`, `11.22 h` over 8000 km. At 5000 m
(interpolating the table between 6000 and 4000 m): about 221 m/s, about 10.1 h.
Shoaling from 4000 m to 20 m: `3.76`.

**(g)** The catalogue is generated, the $b$-values are estimated, the moment rates
and the balanced intercept are computed, and the tsunami speeds and shoaling
factors follow from $g$ and the depths — all computed. The Gutenberg–Richter
parameters used to generate the catalogue, the elastic modulus and the depth
table are tabulated inputs. The megathrust length, width and convergence rate are
labelled `ILLUSTRATIVE`, because they are order-of-magnitude values rather than
measurements of a named margin, and stating that is what allows the reader to
check the robustness of the conclusion instead of trusting it.

---

## ★★★9 — The coupling coefficient

**(a)** Three mechanisms:

1. **Steady creep**, in which the fault slides continuously and aseismically.
2. **Slow slip events**, in which the fault slips over days to years without
   generating high-frequency shaking.
3. **Post-seismic afterslip**, in which the fault continues to slip after a large
   earthquake, releasing moment that would otherwise accumulate.

**(b)** All three remove moment from the budget available for large earthquakes,
so they *lengthen* the recurrence interval of large events in proportion to the
aseismic fraction. A coupling coefficient of 0.6 lengthens the interval by
$1/0.6 = 1.67$.

**(c)** They do not necessarily reduce the maximum magnitude. If the aseismic
slip is distributed smoothly, the locked zone still accumulates strain over a
longer period and can still fail in a large event — the event is just rarer. If
the aseismic slip occurs on the same patches that would otherwise rupture, it can
also reduce the rupture area available and therefore the maximum magnitude. Which
applies is a property of the specific margin, and it is the reason a single
coupling number is not enough for a hazard model.

**(d)** A hazard assessment must therefore *measure* the coupling rather than
assume it. The observations that constrain it are the geodetic velocity field of
the overriding plate — in particular, offshore GNSS and seafloor pressure
observations that record how much of the convergence the locked zone actually
holds — and the moment released by the recorded earthquakes, compared with the
moment accumulated. The two together give the seismic fraction, and the
comparison is the standard way a coupling coefficient is estimated.
