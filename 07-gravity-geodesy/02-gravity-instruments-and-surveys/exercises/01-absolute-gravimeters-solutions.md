# Solutions — 07-02-01 Absolute Gravimeters: Free-Fall and Interferometry

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [01 Absolute Gravimeters: Free-Fall and Interferometry](../01-absolute-gravimeters.md).

---

## ★1 — The two-point estimate and its fragility

$$g = \frac{2h}{t^{2}} = \frac{2\times0.150}{\left(0.1748\right)^{2}}
= \frac{0.300}{0.0305550} = 9.818347\ \mathrm{m\,s^{-2}}.$$

With $t' = 0.1749\ \mathrm{s}$:

$$g' = \frac{0.300}{0.0305900} = 9.807123\ \mathrm{m\,s^{-2}},
\qquad
g' - g = -0.011224\ \mathrm{m\,s^{-2}} = -1.12\times10^{6}\ \mathrm{\mu Gal}.$$

**Implication.** A tenth of a millisecond — a timing error that any laboratory clock
would laugh at — moves the answer by more than a million microgal, because
$g \propto t^{-2}$ and $t$ is only $0.17\ \mathrm{s}$: the relative sensitivity is
$\left|\delta g/g\right| = 2\,\delta t/t = 2\times10^{-4}/0.1748 = 1.14\times10^{-3}$,
i.e. $0.114\%$. A single fall time cannot yield a microgal; the free-fall method
requires hundreds of sampled positions so that the *shape* of the trajectory, not a
single interval, determines $g$. This is the quantitative reason the least-squares
fit of Section 2 exists.

---

## ★2 — Fringes

$$\text{displacement per fringe} = \frac{\lambda}{2}
= \frac{633.0\times10^{-9}}{2} = 3.165\times10^{-7}\ \mathrm{m}
= 316.50\ \mathrm{nm}.$$

$$\text{fringes} = \frac{2h}{\lambda}
= \frac{0.300}{633.0\times10^{-9}} = 473\,933.$$

So a $15\ \mathrm{cm}$ drop is counted in hundreds of thousands of fringes, each
$316.5\ \mathrm{nm}$: the measurement is a *count*, which is why interferometric
fringe subdivision (interpolation within a fringe) is needed to reach nanometre
resolution, and why the laser wavelength must be known as an absolute scale rather
than merely be stable.

---

## ★3 — Three points, three unknowns

Model: $z = \tfrac12 gt^{2} + v_{0}t + z_{0}$, so

$$\underbrace{\begin{pmatrix} 0 & 0 & 1\\ 0.00125 & 0.05 & 1\\ 0.005 & 0.10 & 1
\end{pmatrix}}_{A}
\begin{pmatrix} g\\ v_{0}\\ z_{0}\end{pmatrix}
= \begin{pmatrix} 0\\ 0.01227531\\ 0.04910125\end{pmatrix}.$$

The solution is $g = 9.820250\ \mathrm{m\,s^{-2}}$, $v_{0} = 0$, $z_{0} = 0$
exactly (to round-off), because the three data values were generated from
$z = \tfrac12 gt^{2}$ with that $g$, and a three-parameter model reproduces three
exact data points uniquely.

**Why real data need more.** With exactly $N = 3$ there is no redundancy, so
(i) the residuals are identically zero and the fit gives no evidence about whether
the model is right, and (ii) $s^{2}$ has zero degrees of freedom, so no uncertainty
can be estimated. With many points, the residuals test the model (a drag term or a
timing non-linearity shows up as curvature in the residuals), and the covariance
$s^{2}\left(A^{T}A\right)^{-1}$ yields $\sigma_{g}$ — the two things the three-point
fit cannot provide. The lesson's one-drop result had 697 degrees of freedom and a
residual rms equal to the input noise, which is exactly the model check.

---

## ★★4 — One-drop uncertainty and the number of drops

**One drop.** The two random contributions are independent, so

$$\sigma_{g} = \sqrt{2.625^{2} + 3.066^{2}} = 4.036\ \mathrm{\mu Gal}.$$

**Drops needed for $0.5\ \mathrm{\mu Gal}$:**

$$n = \left(\frac{4.036}{0.5}\right)^{2} = 65.2 \;\longrightarrow\; 66\ \text{drops}
\quad\text{(using } \lceil\cdot\rceil\text{ to be safe, or } 65
\text{ if the target is inclusive).}$$

**Would that achieve $0.5\ \mathrm{\mu Gal}$ accuracy?** No — only its *precision*.
The random term falls as $1/\sqrt{n}$, but the lesson's systematics are untouched:

| systematic | size at these settings |
|---|---|
| laser wavelength error $10^{-8}$ | $9.820\ \mathrm{\mu Gal}$ |
| drag with $200\ \mathrm{\mu Gal}$ terminal | $100\ \mathrm{\mu Gal}$ |
| height definition ($1\ \mathrm{mm}$ error) | $0.308\ \mathrm{\mu Gal}$ |
| mean-minus-midpoint tide, 20 min set | $0.012\ \mathrm{\mu Gal}$ |

The smallest of the top two is twenty times the claimed $0.5\ \mathrm{\mu Gal}$, and
neither improves with more drops. Averaging to $0.5\ \mathrm{\mu Gal}$ while quoting
a $9.8\ \mathrm{\mu Gal}$ wavelength systematic is over-precision, not accuracy: the
honest statement is $0.5\ \mathrm{\mu Gal}$ *statistical*, $9.8\ \mathrm{\mu Gal}$
*systematic*.

---

## ★★5 — Drag bias and the drag coefficient

**Bias.**

$$\text{bias} = -\tfrac12\times a_{\text{term}} = -\tfrac12\times150
= -75.0\ \mathrm{\mu Gal}.$$

A terminal drag of $150\ \mathrm{\mu Gal}$ — half the size of the random noise of one
drop — therefore biases the answer by $75\ \mathrm{\mu Gal}$, fifteen times the
random term after 65 drops. This is the general lesson: **systematics scale
differently from statistics.**

**Drag coefficient for a $2\ \mathrm{\mu Gal}$ bias.** Since the bias is
$-\tfrac12 k v_{\text{end}} = -\tfrac12 k g T$ and $T = 0.2018\ \mathrm{s}$:

$$k = \frac{2\times2.0\times10^{-8}}{9.820250\times0.2018}
= 2.018\times10^{-8}\ \mathrm{s^{-1}}.$$

For comparison, the lesson's first test case used
$k = 10^{-5}\ \mathrm{s^{-1}}$, five hundred times larger, which produced a
$-991\ \mathrm{\mu Gal}$ bias. The requirement is therefore a residual gas pressure
low enough that the drag is negligible, or a measured correction of the size of the
drag itself — which is why real instruments operate in vacuum and calibrate the
residual-gas term rather than estimating it.

---

## ★★6 — Tidal bias over a 30-minute set

With $A = 1.2\times10^{-6}\ \mathrm{m\,s^{-2}}$,
$T_{\text{tide}} = 12.4\ \mathrm{h} = 44\,640\ \mathrm{s}$, a set of
$\tau = 1800\ \mathrm{s}$ starting at zero phase, and
$a(t) = A\sin\left(2\pi t/T_{\text{tide}}\right)$:

**Mean over the set.** Averaging the sine analytically,

$$\bar{a} = \frac{A}{\tau}\int_{0}^{\tau}\sin\left(\frac{2\pi t}{T}\right)
\mathrm{d}t
= \frac{A\,T}{2\pi\tau}
\left[1-\cos\left(\frac{2\pi\tau}{T}\right)\right],
\qquad T = T_{\text{tide}}.$$

Numerically: $2\pi\tau/T_{\text{tide}} = 2\pi\times1800/44640 = 0.25337$ rad,
$\cos = 0.96809$, so
$\bar{a} = 1.2\times10^{-6}\times44640/\left(2\pi\times1800\right)\times
\left(1-0.96809\right) = 4.7354\times10^{-6}\times0.03191
= 1.511\times10^{-7}\ \mathrm{m\,s^{-2}} = 15.11\ \mathrm{\mu Gal}$.

**Value at the midpoint** ($t = 900$ s):
$a_{m} = 1.2\times10^{-6}\sin\left(0.12669\right) = 1.516\times10^{-7}\
\mathrm{m\,s^{-2}} = 15.16\ \mathrm{\mu Gal}$.

**Difference:** $15.11 - 15.16 = -0.041\ \mathrm{\mu Gal}$.

**Peak-to-peak change across the set:**
$A\left[\sin\left(0.25337\right) - \sin(0)\right] = 1.2\times10^{-6}\times0.25066
= 3.008\times10^{-7}\ \mathrm{m\,s^{-2}} = 30.08\ \mathrm{\mu Gal}$.

**Is a midpoint correction adequate for $1\ \mathrm{\mu Gal}$?** Yes: the residual
after using the midpoint value is $0.041\ \mathrm{\mu Gal}$, twenty-four times smaller
than the target, while the *uncorrected* mean would be wrong by
$15.11\ \mathrm{\mu Gal}$ and the change across the set is
$30.08\ \mathrm{\mu Gal}$. Two distinct statements must be kept apart: the set's
sensitivity to the *phase* (tens of microgal, must be corrected) and the
inadequacy of a *midpoint* correction (hundredths of a microgal, negligible here).
The second grows as the cube of the set length relative to the tide period: the
linear part of the sine averages to exactly its midpoint value, so the residual is
the cubic term, $\propto\tau^{3}/T_{\text{tide}}^{3}$. The lesson's table confirms
the exponent (a factor $1.5$ in $\tau$ gives $0.0405/0.0120 = 3.38 \approx 1.5^{3}$,
and a factor $2$ gives $0.3209/0.0405 = 7.92 \approx 2^{3}$), which is why a set of
hours would not be safe with a midpoint correction.

---

## ★★★7 — A $1\ \mathrm{\mu Gal}$ absolute measurement (specification)

**Systematic budget target.** Each term must be below about
$0.5\ \mathrm{\mu Gal}$ so the quadrature sum stays near $1\ \mathrm{\mu Gal}$:

| term | requirement | size at that requirement |
|---|---|---|
| laser wavelength | relative error $< 5\times10^{-9}$ (traceable, stabilised) | $0.49\ \mathrm{\mu Gal}$ |
| residual drag | terminal drag $< 1\ \mathrm{\mu Gal}$ (bias is half of it) | $0.50\ \mathrm{\mu Gal}$ |
| vertical gradient / reference height | height known to $< 3\ \mathrm{mm}$ | $0.92\ \mathrm{\mu Gal}$ |
| tide model | residual after correction $< 0.5\ \mathrm{\mu Gal}$ | $0.50\ \mathrm{\mu Gal}$ |
| tilt / horizontal acceleration coupling | level to a few $\mathrm{\mu rad}$ so the coupling stays below target | $<0.5\ \mathrm{\mu Gal}$ |
| frequency standard during the set | stability $< 5\times10^{-9}$ over the set | $0.49\ \mathrm{\mu Gal}$ |
| atmospheric and polar-motion corrections | model uncertainty below target | $<0.5\ \mathrm{\mu Gal}$ |

**Quadrature sum:** seven terms near $0.5$–$0.9\ \mathrm{\mu Gal}$ give
$\sqrt{6\times0.5^{2} + 0.92^{2}} \approx 1.55\ \mathrm{\mu Gal}$, so the target
demands tightening each term to about $0.35\ \mathrm{\mu Gal}$ or eliminating one.
**Dominant term:** the reference-height and gradient term, because it is the only one
that scales with the station's height rather than with the instrument.

**Random budget and set structure.** One drop gives
$4.036\ \mathrm{\mu Gal}$ (from ★★4), so $1\ \mathrm{\mu Gal}$ statistically needs
17 drops; use 100–200 drops in sets of 20–60 minutes, i.e. 5–10 sets, so that each
set has its own midpoint tide correction and its own robust outlier test.
Re-occupying the station at different times of day gives independent tidal phases
and is the cheapest test of a tide-model error.

**Falsification.** (i) Demonstrate the instrument against a second absolute
instrument, or on a site whose gravity is known from an independent measurement; a
consistent offset falsifies the budget. (ii) Vary each systematic by a known amount
and show the value moves by the predicted size — for example refit with the drag
correction on and off; if the difference does not match half the drag, the drag
model is wrong. (iii) Repeat a set at a different tide phase; if the answer moves by
more than the tide-model uncertainty, the correction is incomplete. A claim of
$1\ \mathrm{\mu Gal}$ without tests (i)–(iii) is a claim about scatter.

---

## ★★★8 — Intercomparison of two absolute gravimeters (specification)

**Protocol.**

1. Both instruments occupy the same station, with the drop chambers' reference
   heights related by a surveyed height difference (levelling or GNSS, sub-millimetre
   at a co-located site). Without this, the comparison measures the gradient, not the
   instruments: $308.28\ \mathrm{\mu Gal\,m^{-1}}$.
2. Interleave the measurements in time (A, B, A, B, …) over several hours, so that
   tidal and environmental drifts are common to both and any real offset is
   distinguishable from a drift.
3. Record each instrument's full systematic budget (laser traceability, drag
   correction, tilt, frequency standard) alongside its values, because a difference
   smaller than the combined budget is not evidence of agreement.
4. Report per-set values with their statistical errors, the set-to-set scatter, and
   the mean difference with its uncertainty.

**Separating station from instrument.** The station gravity is a single number; the
instruments are two measurement processes. With interleaving, the model is

$$g_{i,k} = g_{\text{station}} + \delta_{k} + \epsilon_{i,k},$$

where $\delta_{k}$ is the offset of instrument $k$, $\epsilon$ the random error, and
$i$ indexes the sets. The station value and the offsets are only jointly
identifiable: a common offset in both instruments is absorbed into
$g_{\text{station}}$. The comparison therefore *constrains only the difference*
$\delta_{A} - \delta_{B}$. Reporting an absolute value requires at least one
instrument with an independently defended budget — which is why a third, better
characterised instrument or a reference site is the way to close the loop.

**Statistics.** Chi-square of the per-set differences against their combined
statistical uncertainty tests whether the two instruments agree within that
uncertainty; if $\chi^{2}$ is too large, either an instrument's scatter is
underestimated or one has an unrecognised systematic. Also report the autocorrelation
of the differences: interleaved series with correlated residuals indicate a shared
environmental effect (a pressure or tide model error) rather than instrument noise.

**Detecting a shared bias.** A shared bias — for example both instruments using the
same tide model or the same atmospheric correction — is invisible in the difference
and *cancels* in it, making the comparison look excellent. The only detection is
external: compare each instrument against an independent realisation (a different
tide model, an independent pressure record, a co-located superconducting or
absolute reference), or vary the shared input and check that the value moves by the
model's prediction. The demonstration that a comparison cannot see a shared bias is
itself the reason intercomparisons are reported as *relative* agreement.

---

## ★★★9 — Allocating a fixed time budget (specification with arithmetic)

**Setup.** Let the total available time at the station be $T_{\text{tot}}$ and a
single drop-set take $t_{\text{set}}$ minutes. Let the statistical term from one set
be $\sigma_{\text{stat}}/\sqrt{n_{\text{sets}}}$ and let each additional set reduce
the *systematic* uncertainty contributed by drift and tide by a factor related to
the number of independent phases sampled. Take, from the lesson:

- one set of 20 minutes gives a statistical uncertainty of
  $4.036/\sqrt{n_{\text{drops}}}$; with 700 drops per set and 20 sets that is
  $4.036/\sqrt{14\,000} = 0.034\ \mathrm{\mu Gal}$;
- the tide-model residual per set is $0.012\ \mathrm{\mu Gal}$ and drifts are
  partially common, so further sets buy very little systematics once several phases
  are sampled.

**Allocation.** With a total of, say, 4 hours at the station:

- 12 sets of 20 minutes gives a statistical term of
  $4.036/\sqrt{8400} = 0.044\ \mathrm{\mu Gal}$ and twelve tide phases;
- 4 sets of 60 minutes gives $4.036/\sqrt{8400}$ as well (the same number of drops)
  but only four tide phases, and a larger mean-minus-midpoint residual
  ($0.321\ \mathrm{\mu Gal}$ per set against $0.012\ \mathrm{\mu Gal}$ for a
  20-minute set, from Section 6).

So the *short set, many sets* allocation wins: the same statistics, more independent
sampling of the tide and environment, and a smaller per-set tide residual. The
answer is dominated by the systematic term, so the objective function is
"number of independent phases", not "total drops".

**The assumption that would make this wrong.** It assumes the per-set tide residual
is independent between sets and that there is no per-set overhead (setup, levelling,
thermal settling). If each set carries a fixed 10-minute settling time, a 20-minute
set is half overhead, and the optimum shifts towards longer sets; if the tide
residual is *correlated* between sets (because the same tide model is used), then
more sets do not reduce it at all, and the only fix is a better tide model — an
external improvement, not a time allocation. Stating which of these regimes applies
is part of the design, and it can be tested: plot the per-set residuals against time
of day and check whether they are independent.
