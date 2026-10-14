# Solutions — 14-01-05 Groundwater Chemistry and Salinity

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All analyses are **SYNTHETIC**.

Lesson: [05 Groundwater Chemistry and Salinity](../05-groundwater-chemistry.md).

---

## ★1 — Milliequivalents

$$c_{\text{meq}} = \frac{c_{\text{mg/L}}}{E},\qquad E = \frac{M}{\lvert z\rvert}.$$

$$\text{Ca: } \frac{80}{20.04} = 3.9920\ \mathrm{meq\,L^{-1}},$$
$$\text{SO}_4\text{: } \frac{150}{96.06/2} = \frac{150}{48.03}
= 3.1230\ \mathrm{meq\,L^{-1}},$$
$$\text{Na: } \frac{200}{22.99} = 8.6994\ \mathrm{meq\,L^{-1}}.$$

**The sulfate factor.** The lab reports sulfate as the ion, $M = 96.06\
\mathrm{g\,mol^{-1}}$, with $z = 2$, so $E = 48.03\ \mathrm{mg\,meq^{-1}}$. Using
96.06 would give $1.5615\ \mathrm{meq\,L^{-1}}$ — half the correct value, which
would put a 1.56 meq L$^{-1}$ hole in a charge balance and look like a missing
anion. (Watch for the alternative reporting convention "sulfur as S", where
$M = 32.06$ and $E = 16.03$.)

---

## ★2 — Hardness two ways

**(a) Empirical factors.**
$$\text{hardness} = 2.497(55) + 4.118(18) = 137.34 + 74.12
= 211.5\ \mathrm{mg\,L^{-1}\ as\ CaCO_3}.$$

**(b) Equivalents.**
$$\frac{55}{20.04} + \frac{18}{12.15} = 2.7445 + 1.4815
= 4.2260\ \mathrm{meq\,L^{-1}},$$
$$4.2260 \times 50.04 = 211.5\ \mathrm{mg\,L^{-1}\ as\ CaCO_3}.$$

**Why they agree.** The factors 2.497 and 4.118 *are* the equivalent-weight ratios
$M_{\mathrm{CaCO_3}}/M_{\mathrm{Ca}}/2 \times \ldots$ — explicitly,
$100.09/40.08 = 2.497$ and $100.09/24.31 = 4.118$ — and 50.04 is
$M_{\mathrm{CaCO_3}}/2$. Both routes multiply each cation by its equivalent weight
ratio to CaCO$_3$; they are the same calculation with the algebra pre-multiplied.
The only difference is that route (b) exposes the charge arithmetic, which is why
it is the safer check.

---

## ★3 — Seawater fraction and mixing

$$f_{\text{sw}} = \frac{1500 - 30}{19350 - 30} = \frac{1470}{19320}
= 0.07609 \ (7.61\%).$$

$$ \mathrm{TDS} = (1 - 0.07609)(400) + 0.07609(35{,}000)
= 369.6 + 2663.2 = 3032.6\ \mathrm{mg\,L^{-1}}.$$

Note the leverage: a 7.6% seawater fraction raises TDS by a factor of 7.6. A
chloride of $1500\ \mathrm{mg\,L^{-1}}$ is already far beyond any drinking-water
limit for chloride, and the water is unusable for most irrigation. If the
measurement uncertainty on Cl is $30\ \mathrm{mg\,L^{-1}}$, the uncertainty on
$f_{\text{sw}}$ is $30/19320 = 0.16\%$ — the fresh end member's chloride matters,
the seawater end member's does not.

---

## ★★4 — Charge balance, and a decimal error

| Ion | mg L$^{-1}$ | $E$ | meq L$^{-1}$ |
|---|---|---|---|
| Ca | 88 | 20.04 | 4.3912 |
| Mg | 24 | 12.15 | 1.9753 |
| Na | 120 | 22.99 | 5.2197 |
| K | 6 | 39.10 | 0.1535 |
| HCO$_3$ | 260 | 61.02 | 4.2609 |
| SO$_4$ | 70 | 48.03 | 1.4574 |
| Cl | 200 | 35.45 | 5.6418 |

$$\sum c_{\text{cat}} = 11.7397, \quad \sum c_{\text{an}} = 11.3601, \quad
\mathrm{CBE} = \frac{0.3796}{23.0998} \times 100\% = +1.64\%.$$

Acceptable ($\lvert \mathrm{CBE}\rvert < 5\%$).

**With SO$_4$ misreported as 700 mg L$^{-1}$:**
$\mathrm{SO_4} = 700/48.03 = 14.5740\ \mathrm{meq\,L^{-1}}$, so
$\sum c_{\text{an}} = 24.4769$ and

$$\mathrm{CBE} = \frac{11.7397 - 24.4769}{36.2166} \times 100\% = -35.2\%.$$

**Which to accept:** the first. A −35% CBE is far outside any analytical
tolerance and is a red flag, not a result. This is exactly what the charge balance
is for — it is a *consistency* check that catches transcription errors, and it
costs one line of arithmetic. Note that the check cannot tell you *which* of the
seven numbers is wrong; it only tells you that at least one is.

---

## ★★5 — Calcite saturation index

$[\mathrm{H^+}] = 10^{-7.5} = 3.162 \times 10^{-8}$;
$K_{a2}/[\mathrm{H^+}] = 4.677 \times 10^{-11}/3.162 \times 10^{-8}
= 1.479 \times 10^{-3}$.

$$[\mathrm{HCO_3^-}] = \frac{3.0 \times 10^{-3}}{1 + 2(1.479 \times 10^{-3})}
= \frac{3.0 \times 10^{-3}}{1.002958} = 2.9912 \times 10^{-3}\
\mathrm{mol\,L^{-1}},$$
$$[\mathrm{CO_3^{2-}}] = 2.9912 \times 10^{-3} \times 1.479 \times 10^{-3}
= 4.424 \times 10^{-6}\ \mathrm{mol\,L^{-1}}.$$

**Activities**, with $\sqrt{I} = \sqrt{0.010} = 0.1000$:
$$\log_{10}\gamma_{\mathrm{Ca}} = \frac{-0.509(4)(0.1000)}{1 + 0.328(5)(0.1000)}
= \frac{-0.20360}{1.1640} = -0.17492 \Rightarrow \gamma_{\mathrm{Ca}} = 0.66848,$$
$$\log_{10}\gamma_{\mathrm{CO_3}} = \frac{-0.20360}{1 + 0.328(3.5)(0.1000)}
= \frac{-0.20360}{1.1148} = -0.18263 \Rightarrow
\gamma_{\mathrm{CO_3}} = 0.65670.$$

$$m_{\mathrm{Ca}} = 80 \times 10^{-3}/40.08 = 1.9960 \times 10^{-3}\
\mathrm{mol\,L^{-1}},$$
$$\mathrm{IAP} = (0.66848 \times 1.9960 \times 10^{-3})(0.65670 \times 4.424
\times 10^{-6}) = 3.877 \times 10^{-9},$$
$$\mathrm{SI} = \log_{10}\frac{3.877 \times 10^{-9}}{3.311 \times 10^{-9}}
= \log_{10}(1.171) = +0.068.$$

**Interpretation.** $\mathrm{SI} = +0.07 > 0$: the water is marginally
supersaturated with respect to calcite and calcite **cannot** dissolve in it — it
would tend to precipitate, though a small positive SI is within the uncertainty of
the constants and the pH measurement. An error of 0.07 in SI corresponds to a pH
error of only 0.07 units, which is at the edge of routine field measurement. **The
honest conclusion is "at saturation, within uncertainty"**, not "supersaturated".
Ignoring the activity coefficients would have given
$\mathrm{SI} = +0.068 - 0.307 = -0.24$, i.e. a confident but wrong statement that
the water is undersaturated.

---

## ★★6 — Cation exchange

Mixing line at $f_{\text{sw}} = 0.02$:
$$\mathrm{Ca}_{\text{mix}} = 0.98(42) + 0.02(400) = 41.16 + 8.00
= 49.16\ \mathrm{mg\,L^{-1}},$$
$$\mathrm{Na}_{\text{mix}} = 0.98(45) + 0.02(10{,}800) = 44.10 + 216.0
= 260.1\ \mathrm{mg\,L^{-1}}.$$

Exchange of $1.5\ \mathrm{meq\,L^{-1}}$: Ca decreases by
$1.5\ \mathrm{meq\,L^{-1}}$ and Na increases by $1.5\ \mathrm{meq\,L^{-1}}$
(charge-equivalent, not mass-equivalent):

$$\mathrm{Ca}_{\text{after}} = \left(\frac{49.16}{20.04} - 1.5\right)20.04
= (2.4531 - 1.5)(20.04) = 0.9531 \times 20.04 = 19.10\ \mathrm{mg\,L^{-1}},$$
$$\mathrm{Na}_{\text{after}} = \left(\frac{260.1}{22.99} + 1.5\right)22.99
= (11.3136 + 1.5)(22.99) = 12.8136 \times 22.99 = 294.6\ \mathrm{mg\,L^{-1}}.$$

| Ion | mixing line | after exchange | change |
|---|---|---|---|
| Ca (mg L$^{-1}$) | 49.16 | 19.10 | $-61.1\%$ |
| Na (mg L$^{-1}$) | 260.1 | 294.6 | $+13.3\%$ |

**Comment.** The calcium has fallen by 61% — a sample with 19 mg L$^{-1}$ Ca and
Cl = 511 mg L$^{-1}$ (the mixture's chloride) would be badly misinterpreted by
anyone reading a mixing fraction from calcium. Sodium moves far less in percentage
terms for the same reason as in the lesson: 1.5 meq L$^{-1}$ is 34.5 mg L$^{-1}$ of
Na on a pool of 260 mg L$^{-1}$. **The lesson is that charge-based exchange
produces mass-based asymmetries, and the largest *relative* change always appears
in the ion with the smallest pool.**

---

## ★★★7 — Detecting the onset of intrusion

**The arithmetic.** Starting from the synthetic fresh water
(TDS $= 394\ \mathrm{mg\,L^{-1}}$, $\sigma_w = 0.0591\ \mathrm{S\,m^{-1}}$,
$\rho_{\text{bulk}} = 16.92/0.09 = 188.0\ \Omega$ m), a seawater fraction $f$ gives
(from the lesson's table, linear mixing):
$$\mathrm{TDS}(f) = (1-f)(394) + f(35{,}000), \qquad
\sigma_w = 0.15\,\mathrm{TDS}\,[\mathrm{g\,L^{-1}}], \qquad
\rho_{\text{bulk}} = \frac{1}{0.09\,\sigma_w}.$$

| $f_{\text{sw}}$ | Cl (mg L$^{-1}$) | TDS (mg L$^{-1}$) | $\rho_{\text{bulk}}$ ($\Omega$ m) | change in $\rho$ |
|---|---|---|---|---|
| 0 | 25 | 394 | 188.0 | – |
| 0.001 | 44 | 428.6 | 172.8 | $-8.1\%$ |
| 0.010 | 218 | 740.1 | 100.1 | $-46.8\%$ |
| 0.050 | 991 | 2124 | 34.9 | $-81.4\%$ |

(The change is exactly $\Delta\rho/\rho = -\dfrac{87.83\,f}{1 + 87.83\,f}$
because the seawater TDS exceeds the fresh TDS by a factor of
$35000/394 = 88.83$, so the TDS ratio is $1 + 87.83f$; for small $f$ the
fractional change is $-87.8f$ — a 0.1% seawater fraction is already an 8%
resistivity change.)

**Comparison with a 3% ERT repeatability.** $f = 0.001$ gives 8.1%, a factor of
2.7 above the noise — detectable, but only just, and only if the *same* static
heterogeneity is subtracted (which is why time-lapse, not single-survey, is the
right design). $f = 0.01$ gives 47%: unmissable.

**Detection limit in chloride.** For a 3% change,
$f = 3\%/88 = 3.4 \times 10^{-4}$, so
$\mathrm{Cl} = 25 + 3.4 \times 10^{-4}(19325) = 25 + 6.6 = 31.6\
\mathrm{mg\,L^{-1}}$. **A ERT repeatability of 3% corresponds to detecting about
$32\ \mathrm{mg\,L^{-1}}$ of chloride**, i.e. a change of $6.6\
\mathrm{mg\,L^{-1}}$ above the fresh background. That is an optimistic figure
because it assumes porosity, clay content and saturation are unchanged between
surveys — which is exactly the assumption intrusion itself can violate (density
changes, pumping changes saturation).

**Programme design.**

  - **Piezometers:** 6–10 nests screened at the base, middle and top of the
    aquifer, sampled quarterly for Cl (and annually for the full suite with a
    charge balance). This is the ground truth and it is cheap.
  - **Time-lapse ERT:** the same 48-electrode line, the same electrode positions
    (permanently installed, with a surveyed reference), the same acquisition
    schedule (seasonally, at the same tidal state and after the same pumping
    pattern), difference imaging with a stated error model. Static heterogeneity
    cancels in the difference; *repeatability* then controls detection.
  - **Cross-checks:** water levels (to separate a salinity change from a head
    change) and a temperature log (a second, independent tracer of a seawater
    front, since seawater is colder).
  - **What can be mistaken for intrusion:** a falling water table (which changes
    saturation and hence resistivity), clay-rich channel fill (static, cancels in
    the difference but not in a single survey), and electrode contact-resistance
    drift (which the reciprocal-error check detects).

---

## ★★★8 — How many salinities fit one resistivity?

With $\rho_{\text{bulk}} = \rho_w/\phi^{2}$ (i.e. $a = 1$, $m = 2$, $S_w = 1$) and
$\sigma_w = 0.15\,\mathrm{TDS}$ [g L$^{-1}$]:
$$\rho_w = 60\,\phi^{2}, \qquad \sigma_w = \frac{1}{60\phi^{2}}, \qquad
\mathrm{TDS}\,[\mathrm{mg\,L^{-1}}] = \frac{1000}{0.15 \times 60\phi^{2}}
= \frac{111.1}{\phi^{2}}.$$

| $\phi$ | $\rho_w$ ($\Omega$ m) | $\sigma_w$ (S m$^{-1}$) | TDS (mg L$^{-1}$) |
|---|---|---|---|
| 0.20 | 2.40 | 0.4167 | 2778 |
| 0.25 | 3.75 | 0.2667 | 1778 |
| 0.30 | 5.40 | 0.1852 | 1235 |
| 0.35 | 7.35 | 0.1361 | 907 |
| 0.40 | 9.60 | 0.1042 | 694 |

**Range from porosity alone: 694 to 2778 mg L$^{-1}$ — a factor of 4.** Note that
the fresh water of this lesson (394 mg L$^{-1}$) is *not* in the range for
$\phi \le 0.40$: to explain $\rho = 60\ \Omega$ m with fresh water you would need
$\phi$ beyond 0.53, which is not a sand.

**Cementation exponent uncertainty** at $\phi = 0.30$:
$$\rho_w = 60(0.30)^{m}, \qquad
m = 1.8 \Rightarrow \rho_w = 6.87\ \Omega\,\mathrm{m} \Rightarrow
\mathrm{TDS} = 970\ \mathrm{mg\,L^{-1}},$$
$$m = 2.0 \Rightarrow 1235\ \mathrm{mg\,L^{-1}}, \qquad
m = 2.2 \Rightarrow 1571\ \mathrm{mg\,L^{-1}}.$$

**The single measurement that reduces the range most** is an independent porosity
(or, equivalently, a measurement that fixes the formation factor): a density or
neutron log, or a nuclear-magnetic-resonance log, at the same location and in the
same unit. That converts a 4-fold ambiguity into the 1.6-fold ambiguity left by
$m$; then a single water sample fixes the TDS calibration and the ambiguity
collapses. Note the ordering: **porosity first, salinity second**, because the
resistivity is far more sensitive to porosity (a factor of 4 over a plausible
porosity range) than the salinity interpretation is to the cementation exponent (a
factor of 1.6). This is the same lesson as
[Archie's law](../../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md),
applied to a real decision.

---

## Mastery checkpoint — worked

Synthetic sample (mg L$^{-1}$): Ca 120, Mg 30, Na 254, K 8, HCO$_3$ 180, SO$_4$ 90,
Cl 500, SiO$_2$ 12.

**(a) Charge balance.**

| Ion | mg L$^{-1}$ | $E$ | meq L$^{-1}$ |
|---|---|---|---|
| Ca | 120 | 20.04 | 5.9880 |
| Mg | 30 | 12.15 | 2.4691 |
| Na | 254 | 22.99 | 11.0483 |
| K | 8 | 39.10 | 0.2046 |
| HCO$_3$ | 180 | 61.02 | 2.9499 |
| SO$_4$ | 90 | 48.03 | 1.8738 |
| Cl | 500 | 35.45 | 14.1044 |

$$\sum c_{\text{cat}} = 19.7100, \quad \sum c_{\text{an}} = 18.9281, \quad
\mathrm{CBE} = \frac{0.7819}{38.6381} \times 100\% = +2.02\%.$$
Acceptable under the 5% convention, though tighter than ideal for a water of this
ionic strength.

**(b) TDS by the ion sum.**
$$120 + 30 + 254 + 8 + 180 + 90 + 500 + 12 = 1194\ \mathrm{mg\,L^{-1}}.$$

**(c) Seawater fraction and the mixing-line TDS.**
$$f_{\text{sw}} = \frac{500 - 25}{19350 - 25} = \frac{475}{19325} = 0.02458
\ (2.46\%),$$
$$\mathrm{TDS}_{\text{mix}} = 0.97542(394) + 0.02458(35{,}000)
= 384.3 + 860.3 = 1244.6\ \mathrm{mg\,L^{-1}}.$$
The measured 1194 mg L$^{-1}$ is **50.6 mg L$^{-1}$ (4.1%) below** the conservative
mixing line. That is a small but real discrepancy: either the fresh end member used
here is not the right one for this site, or a reaction removed dissolved solids
(most likely calcite precipitation, which would also lower Ca and HCO$_3$).

**(d) Hardness.**
$$2.497(120) + 4.118(30) = 299.6 + 123.5 = 423.2\ \mathrm{mg\,L^{-1}\ as\ CaCO_3}.$$
Check by equivalents: $5.9880 + 2.4691 = 8.4571\ \mathrm{meq\,L^{-1}}$, and
$8.4571 \times 50.04 = 423.2$ ✔. This is a hard water by any convention.

**(e) Facies and the sodium test.** Cation percentages: Na 56.1%, Ca 30.4%,
Mg 12.5%, K 1.0%. Anion percentages: Cl 74.5%, HCO$_3$ 15.6%, SO$_4$ 9.9%. The
water is a **Na-Cl type**, i.e. chloride-dominated — consistent with a seawater
influence.

The sodium test: in seawater the charge ratio $\mathrm{Cl/Na} = 545.8/469.8 =
1.162$ (meq basis, from 19,350/35.45 and 10,800/22.99). In this sample
$14.1044/11.0483 = 1.277$, i.e. **10% more chloride per unit sodium than
seawater**. A pure seawater mixture cannot produce that: mixing a fresh Ca-HCO$_3$
water with seawater moves the ratio *towards* 1.162 from whatever the fresh water
had ($25/35.45$ vs $45/22.99$ gives Cl/Na $= 0.36$ in the fresh water, so mixing
must give a ratio *below* 1.162, not above it). The 10% excess chloride requires an
additional source of chloride **or** a loss of sodium — and cation exchange on clay
is exactly a sodium-loss mechanism (Section 6 of the lesson), as is an evaporite or
a pollution source. **So a simple seawater-mixing explanation fails, and the
diagnosis is either exchange or a non-marine chloride source.** Deciding between
them needs a second conservative tracer (bromide, or the Cl/Br ratio, which is
distinctive for seawater) and a look at the aquifer mineralogy.

**(f) Bulk resistivity at $\phi = 0.30$.** With $\sigma_w = 0.15 \times 1.194
= 0.1791\ \mathrm{S\,m^{-1}}$, $\rho_w = 5.583\ \Omega$ m, and
$\rho_{\text{bulk}} = \rho_w/\phi^{2} = 5.583/0.09 = 62.0\ \Omega$ m.

**What you would need before calling a low resistivity here an intrusion:**
(i) an independent porosity or formation factor at the same location (a log, or a
core) — from ★★★8, a plausible porosity range moves the inferred TDS by a factor
of four; (ii) a water sample at that depth, to fix the TDS–conductivity
calibration and to run the chloride test of part (e); (iii) a check on clay
content, since surface conduction lowers resistivity without any salinity change.
Only then is the resistivity interpretable as salinity.
