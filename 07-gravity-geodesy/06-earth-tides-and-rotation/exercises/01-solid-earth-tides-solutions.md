# Solutions — 07-06-01 Solid Earth Tides and Their Gravity Signature

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values or stated standard constants.

Lesson: [01 Solid Earth Tides](../01-solid-earth-tides.md).

---

## ★1 — The solar/lunar tidal ratio

$$\frac{(\mathrm{GM}/d^{3})_{\odot}}{(\mathrm{GM}/d^{3})_{\text{Moon}}}
= \frac{1.32712440018\times10^{20}}{(1.495978707\times10^{11})^{3}}
\times\frac{(3.844\times10^{8})^{3}}{4.902800118\times10^{12}} .$$

Compute each factor:

$$d_{\odot}^{3} = 3.3480\times10^{33}\ \mathrm{m^{3}}
\;\Rightarrow\; (\mathrm{GM}/d^{3})_{\odot} = 3.9643\times10^{-14},$$
$$d_{\text{Moon}}^{3} = 5.6801\times10^{25}\ \mathrm{m^{3}}
\;\Rightarrow\; (\mathrm{GM}/d^{3})_{\text{Moon}} = 8.6323\times10^{-14},$$
$$\text{ratio} = \frac{3.9643\times10^{-14}}{8.6323\times10^{-14}} = 0.4592 .$$

**A body of the Moon's mass at twice the distance:** the forcing scales as
$d^{-3}$, so the ratio to the Moon is $2^{-3} = 0.1250$, i.e. one eighth. The
strong distance dependence is why the solar tide is only $46\%$ of the lunar tide
despite the Sun being $2.7\times10^{7}$ times more massive.

---

## ★2 — The O1 period

$$n_m = \frac{2\pi}{27.321661 \times 86400} = 2.661700\times10^{-6}\
\mathrm{rad\,s^{-1}},$$
$$\omega_{O1} = \omega - 2n_m = 7.2921150\times10^{-5} - 5.323400\times10^{-6}
= 6.759775\times10^{-5}\ \mathrm{rad\,s^{-1}},$$
$$T_{O1} = \frac{2\pi}{6.759775\times10^{-5}} = 92949\ \mathrm{s}
= 25.8193\ \mathrm{h}.$$

Compare with the sidereal day $2\pi/\omega = 86164\ \mathrm{s} = 23.9345\
\mathrm{h}$: O1 is **longer** than the sidereal day by $1.88\ \mathrm{h}$,
because it is the *lunar* diurnal constituent and the Moon's motion retards the
apparent rotation of the tide-raising body. K1, whose combination is $\omega$
alone, sits exactly on the sidereal day.

---

## ★3 — An alternative $\delta$

$$\delta' = 1 + 0.6078 - 1.5(0.2990) = 1 + 0.6078 - 0.4485 = 1.1593 .$$

Relative to the lesson's $\delta = 1.1530$:

$$\frac{\delta' - \delta}{\delta} = \frac{0.0063}{1.1530} = +0.55\% .$$

So a change of $\Delta h_2 = -0.0012$ and $\Delta k_2 = -0.0050$ moves the
predicted tide by $0.55\%$ — about $0.5\ \mathrm{\mu Gal}$ on a $95\
\mathrm{\mu Gal}$ M2 signal. **The cancellation matters:** $h_2$ and $k_2$ enter
with opposite signs, so an error in one can be partly hidden by an error in the
other; only the combination $1 + h_2 - \tfrac32k_2$ is constrained by a gravity
tide measurement, which is why the pair is usually taken from independent
observations (VLBI/GNSS for $h_2$, gravity and tilt for $k_2$).

---

## ★4 — The S2 identity

In cycles per mean solar day, the Earth's rotation rate is
$1.0027379\ \mathrm{c\,d^{-1}}$ (one extra sidereal rotation per year, because
the Earth must turn once more to face the Sun) and the Sun's mean motion is
$n_s = 1/365.2422 = 0.0027379\ \mathrm{c\,d^{-1}}$. Then

$$2(\omega - n_s) = 2(1.0027379 - 0.0027379) = 2.0000000\ \mathrm{c\,d^{-1}}
\;\Longrightarrow\; T_{S2} = \frac{24}{2.0000} = 12.0000\ \mathrm{h}.$$

The identity holds *because* the difference between the sidereal and solar
rotation rates is by definition the Sun's apparent mean motion. Computing S2 from
the two rates reproduces the definition; it does not test any physics. That is
exactly why it is a useful **arithmetic** check: if the two rates are quoted in
inconsistent conventions (e.g. one from a sidereal day in seconds and one from a
tropical year in days), the identity fails and the error is caught.

---

## ★5 — Rayleigh separation in a 10-day record

The Rayleigh criterion: two frequencies separated by $\Delta f$ need a record of
about $1/\Delta f$.

| pair | $\Delta f$ ($\mathrm{c\,d^{-1}}$) | required length | separable in 10 d? |
|---|---|---|---|
| M2, S2 | $0.0677$ | $14.8\ \mathrm{d}$ | no |
| K1, O1 | $0.0732$ | $13.7\ \mathrm{d}$ | no |
| M2, K2 | $0.00548$ | $182.6\ \mathrm{d}$ | no |

So in 10 days **none** of the three pairs is separable under the strict
criterion. (M2/S2 and K1/O1 are both marginal at 10 days in the loose
convention, which is why 15-day and 30-day analyses are common.)

**What a least-squares fit does anyway:** it returns two amplitudes and two
phases, with small formal standard errors, because the normal-equation matrix is
merely ill-conditioned rather than singular. The two estimated constituents are
then *not* the two true constituents but linear combinations of them, and the
formal error understates the true uncertainty, because it assumes the other
constituent's amplitude is zero. This is why a tidal analysis must state its
record length relative to the pair separations it claims to resolve.

---

## ★6 — The equatorial M2 amplitude

The analytic value assumes the body in the **equatorial plane**, so that
$\cos^{2}\delta = 1$:

$$|\delta g|_{M2}^{\text{analytic}} = \tfrac34\,\frac{2\mathrm{GM}_mR}{d^{3}}\,\delta
= 0.75 \times 1.099845\times10^{-6} \times 1.1530
= 9.5109\times10^{-7}\ \mathrm{m\,s^{-2}} = 95.11\ \mathrm{\mu Gal}.$$

The synthetic Moon's orbit is inclined $5.15^\circ$ to an ecliptic tilted
$23.44^\circ$, so its declination reaches $28.58^\circ$. The semidiurnal
amplitude carries a factor $\cos^{2}\delta$ that varies through the orbit, and the
fitted M2 constituent is the appropriate average:

$$\frac{83.8668}{95.11} = 0.8818
\quad\Longrightarrow\quad
\cos^{2}\bar\delta = 0.8818,\quad \bar\delta = 20.1^\circ .$$

So the difference is exactly a declination factor, not an error: the fitted
amplitude is $88.18\%$ of the equatorial-plane ideal.

**What else you would need for an exact prediction:** the body's ephemeris
(declination and distance as functions of time), the station's latitude and
longitude, the exact frequency of the constituent being predicted, and the
gravity-tide factor. The declination factor is then computed rather than
averaged — which is precisely what a full tidal prediction algorithm does.

---

## ★7 — Ocean-load contamination (specification)

1. **Synthetic body tide.** Generate the body tide from a simplified ephemeris as
   in the demonstration (degree 2, circular orbits), at a coastal station.
2. **Synthetic load tide.** Add a load tide generated by convolving a synthetic
   ocean-tide potential with a synthetic elastic load Green's function, or more
   simply by adding a second harmonic series at the same constituents with
   *spatially* varying amplitude and a phase lag of a stated amount (e.g.
   $30^\circ$ at M2). The *true* load is a stated perturbation: choose
   amplitude $=0.15\times$ the body tide at M2, phase $+30^\circ$.
3. **Perturbed model.** Build a *second* load model with a $10\%$ amplitude error
   and a $5^\circ$ phase error — the error the analysis is asked to detect.
4. **Noise.** Add white noise at a stated level (say $0.5\ \mathrm{\mu Gal}$ per
   sample, i.e. the level at which the load error is comparable to the noise).
5. **Analysis.** Fit M2, S2, K1, O1 with 60 days of 5-minute samples, both with
   and without correcting for the (perturbed) load model.
6. **Diagnostic.** The fitted M2 amplitude error and its formal standard error,
   and — crucially — the *phase* error, which is often more sensitive to a load
   model than the amplitude.
7. **Prediction.** A $10\%$ amplitude error in a load that is $15\%$ of the body
   tide produces an M2 amplitude bias of order $1.5\%$, i.e. about
   $0.6\ \mathrm{\mu Gal}$ at a $40\ \mathrm{\mu Gal}$ M2 amplitude, and a phase
   bias of a few tenths of a degree. Whether that is detectable depends on step
   4: the experiment's real content is the *ratio* of the load error to the noise.
8. **What it cannot establish.** With one station and one load model, the load
   error is degenerate with (i) an error in the neighbouring ocean tide model,
   (ii) an error in the elastic parameters of the load response, and (iii) a
   lateral structure anomaly beneath the station. Separating them requires a
   *network* of stations with different coastal geometry, or an independent ocean
   tide model comparison — which is the experiment's natural extension.

---

## ★8 — Omitted modulation

**(i) Orbital eccentricity.** The Moon's distance and longitude vary with the
anomalistic period; the tidal force, which scales as $d^{-3}$, is modulated with
the anomaly. This introduces the elliptic constituents, principally:
N2 ($2\omega - 3n_m + p$, where $p$ is the perigee rate), L2, and the elliptic
diurnal terms, all within about $0.1\ \mathrm{c\,d^{-1}}$ of M2. Because they lie
so close to M2, they are *not* separable in a 60-day record (Rayleigh: $1/0.1 =
10$ days to separate — actually separable, but marginal with further nearby
terms), and the standard practice is to either fit them explicitly with known
relative amplitudes (the "satellite constituent" or admittance approach) or to
accept their aliasing.

**(ii) Nodal regression.** The lunar node regresses with an 18.6-year period,
which modulates the amplitude of every lunar constituent slowly. In a 60-day
record this appears as a *scale factor* on M2 and O1, conventionally
$1 - 0.037\cos N$ for M2, i.e. a variation of $\pm3.7\%$ in amplitude.

**Rough amplitude-error estimate.** Take the omitted effect to be $5\%$ of the
lunar tide. If the omitted energy sits at frequencies that are *near* the fitted
constituent but not included in the basis, the fit attributes the coherent part
to the nearest constituent, so the M2 amplitude error is of order the omitted
amplitude — about $5\%$, i.e. $2\ \mathrm{\mu Gal}$ on an M2 amplitude of
$41.9\ \mathrm{\mu Gal}$— rather than a random small number. If the omitted
frequencies are far from M2, the error is instead spread across all constituents
and is smaller per constituent. **The lesson is that "how big is the omitted
term" and "where is it in frequency" both matter, and only the pair determines
the error in a fitted amplitude.**
