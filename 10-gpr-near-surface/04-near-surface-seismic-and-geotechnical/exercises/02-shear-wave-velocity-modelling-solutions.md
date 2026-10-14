# Solutions — 10-04-02 Shear-Wave Velocity Modelling and Site Classification

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment. Where a problem has more than one defensible answer, that
> is said. All models are **SYNTHETIC**; the empirical relations are labelled.

Lesson: [02 Shear-Wave Velocity Modelling and Site Classification](../02-shear-wave-velocity-modelling.md).

---

## ★1 — $V_{S30}$ and its weights

$$T = \frac{4}{160} + \frac{10}{240} + \frac{16}{420}
= 0.02500 + 0.041667 + 0.038095 = 0.104762\ \mathrm{s} = 104.76\ \mathrm{ms},$$

$$V_{S30} = \frac{30}{0.104762} = 286.4\ \mathrm{m\,s^{-1}}.$$

| layer | $h$ (m) | $V_s$ (m/s) | $h/V_s$ (ms) | $w_i$ |
|---|---|---|---|---|
| 1 | $4$ | $160$ | $25.00$ | $0.2386$ |
| 2 | $10$ | $240$ | $41.67$ | $0.3977$ |
| 3 | $16$ | $420$ | $38.10$ | $0.3636$ |

The weights sum to $1.0000$, as the derivation requires. **Layer 2 dominates**
(39.8% of the weight) because it is thick *and* slow; the ratio of the largest
weight to the smallest is $1.67$, so no single layer decides the answer — which is
the benign case. (In the lesson's borehole profile the top $2\ \mathrm{m}$ carried
$15.6\%$ of the weight, and there the profile can be wrecked by one omission.)

The class is D ($180$–$360\ \mathrm{m\,s^{-1}}$).

---

## ★2 — Stiffness from a velocity

$$G_{\max} = \rho V_s^{2} = 1900(300)^{2} = 1.710\times10^{8}\ \mathrm{Pa}
= 171.0\ \mathrm{MPa},$$

$$E = 2G(1+\nu) = 2(171.0)(1.35) = 461.7\ \mathrm{MPa}.$$

**Exact:** the relation $G = \rho V_s^2$ for a linear elastic isotropic medium, and
$E = 2G(1+\nu)$ given $\nu$. No fitted constants appear.

**Assumption:** $\nu = 0.35$, and $\rho = 1900\ \mathrm{kg\,m^{-3}}$, are known
values. Since $G \propto V_s^2$, a $5\%$ velocity error is a $10\%$ modulus error,
and the same factor propagates into $E$ — this is the one place in the lesson where
a measurement error is *amplified* rather than merely inherited.

---

## ★3 — Class near a boundary

Boundaries: A $>1500$, B $760$–$1500$, C $360$–$760$, D $180$–$360$,
E $<180\ \mathrm{m\,s^{-1}}$. $V_{S30} = 352\ \mathrm{m\,s^{-1}}$ → **class D**.

Distance to the nearest boundary ($360$): $8.0\ \mathrm{m\,s^{-1}}$, i.e.
$2.27\%$ of $352$.

With a $6\%$ velocity uncertainty, $\sigma = 0.06(352) = 21.1\ \mathrm{m\,s^{-1}}$
and the boundary sits at $-0.38\sigma$, so

$$P(\text{class C}) = \Phi(0.38) \approx 0.65.$$

**The class is more likely C than D, on the basis of a measurement reported as D.**
An engineer must be told both: the class the number falls in, and the probability
of the neighbouring class. Two design details follow from the difference — the
governing code spectrum and the required site-specific analysis — so a class
decision at $0.38\sigma$ from a boundary is not a decision the data can carry
alone.

---

## ★4 — Operative modulus and settlement

$$G_{\max} = 1900(300)^2 = 171.0\ \mathrm{MPa}, \qquad
\gamma_r = \frac{\tau_{\max}}{G_{\max}} = \frac{50\times10^{3}}{171.0\times10^{6}}
= 2.924\times10^{-4},$$

$$\frac{G}{G_{\max}}\bigg|_{\gamma = 5\times10^{-4}}
= \frac{1}{1+5\times10^{-4}/2.924\times10^{-4}} = \frac{1}{2.710} = 0.3690,$$

$$G_{\mathrm{op}} = 0.3690(171.0) = 63.1\ \mathrm{MPa}, \qquad
E_{\mathrm{op}} = 2(63.1)(1.35) = 170.4\ \mathrm{MPa}.$$

Footing: $q = 120\ \mathrm{kPa}$, $B = 2.0\ \mathrm{m}$, so
$a = B/\sqrt{\pi} = 1.1284\ \mathrm{m}$, and with $E_{\max} = 461.7\ \mathrm{MPa}$,

$$\delta_{\max} = \frac{\pi}{2}\frac{(120)(1.1284)(1-0.35^{2})}{461.7\times10^{3}}
= \frac{186.6}{461.7\times10^{3}}\ \mathrm{m} = 0.40\ \mathrm{mm},$$

$$\delta_{\mathrm{op}} = \frac{186.6}{170.4\times10^{3}} = 1.09\ \mathrm{mm}.$$

**Ratio: $2.71$.** The small-strain calculation hides almost two thirds of the
settlement; and note the direction of the error — using $G_{\max}$ is
*unconservative* for a settlement check.

---

## ★5 — $CSR$ and why it grows with depth

Water table at $3.0\ \mathrm{m}$; $\gamma = 18\ \mathrm{kN\,m^{-3}}$ above and
$20\ \mathrm{kN\,m^{-3}}$ below (SYNTHETIC). At $z = 3.0\ \mathrm{m}$:
$\sigma_v = 54.0$ kPa, $u = 0$, $\sigma'_v = 54.0$ kPa,
$r_d = 1-0.00765(3.0) = 0.9770$.

$$CSR = 0.65\left(\frac{54.0}{54.0}\right)(0.25)(0.9770) = 0.1588.$$

At $z = 6.0\ \mathrm{m}$: $\sigma_v = 54.0+20(3) = 114.0$ kPa,
$u = 9.81(3) = 29.43$ kPa, $\sigma'_v = 84.57$ kPa,
$r_d = 1-0.00765(6.0) = 0.9541$.

$$CSR = 0.65\left(\frac{114.0}{84.57}\right)(0.25)(0.9541) = 0.2090.$$

**Why it grows.** Three factors: $\sigma_v/\sigma'_v$ rises from $1.000$ to
$1.348$ (the pore pressure grows faster than the total stress below the water
table), which is a $35\%$ increase; $r_d$ falls from $0.9770$ to $0.9541$, a
$2.4\%$ decrease. The stress ratio wins by a factor of fifteen. This is why the
critical depth in a sand profile is usually just below the water table and
increases with the depth of the water table — an engineering fact that follows from
one ratio, not from a curve.

---

## ★6 — A class boundary $0.71\sigma$ away

A central value $20\ \mathrm{m\,s^{-1}}$ above the boundary, with an $8\%$
uncertainty on $V_{S30} = 352$: $\sigma = 28.2\ \mathrm{m\,s^{-1}}$. The boundary is
at $-20/28.2 = -0.71\sigma$, so

$$P(\text{lower class}) = \Phi(-0.71) = 0.239 \approx 24\%.$$

**What the engineer should be told.** "Class X by the measured value; the
probability of class Y, which would require a site-specific analysis (or would
change the design spectrum), is about one in four." Two cautions to add, because
they make $24\%$ an optimistic figure rather than a conservative one: the Gaussian
assumption ignores the systematic part of the velocity error (a wrong $V_{S30}$
profile below the deepest measurement is not a random error at all), and the
boundary itself is a code convention, not a physical threshold — the site response
varies continuously across it.

---

## ★7 — The $18$–$24\ \mathrm{m}$ soft layer

**Construction.** Take a profile that is $4\ \mathrm{m}$ at $200$,
$10\ \mathrm{m}$ at $330$, and then either (i) $6\ \mathrm{m}$ at $260$ followed by
$10\ \mathrm{m}$ at $500\ \mathrm{m\,s^{-1}}$ (the $30\ \mathrm{m}$ profile), or
(ii) $16\ \mathrm{m}$ at $420\ \mathrm{m\,s^{-1}}$ (the $20\ \mathrm{m}$ profile,
which cannot see the soft layer).

*Profile (i):*
$T = 4/200 + 10/330 + 6/260 + 10/500 = 20.0 + 30.3 + 23.1 + 20.0 =
93.4\ \mathrm{ms}$,
$V_{S30} = 30/0.0934 = 321.2\ \mathrm{m\,s^{-1}}$ → class D.

*Profile (ii):* $T = 20.0+30.3+16/420 = 20.0+30.3+38.1 = 88.4\ \mathrm{ms}$,
$V_{S30} = 30/0.0884 = 339.4\ \mathrm{m\,s^{-1}}$ → class D.

**Difference:** $18.2\ \mathrm{m\,s^{-1}}$, $5.7\%$, and no class change here — but
the *soft layer* is the one that would control the seismic response at its own
depth, and its absence from the shallower profile is a $23\ \mathrm{ms}$
travel-time error in the column, i.e. a systematic $5.7\%$ velocity error. Whether
that matters depends on the decision: a $5.7\%$ velocity error is a $11.7\%$
stiffness error, and the site period scales as $4H/V_s$, so the period of a
$30\ \mathrm{m}$ column changes by the same $5.7\%$.

**The measurement that settles it.** A surface-wave array whose longest usable
wavelength samples beyond $24\ \mathrm{m}$ — practically, an array length of
$40$–$60\ \mathrm{m}$ with the receiver spread laid out to maximise the longest
offset, plus a borehole (cross-hole or down-hole) interval measurement across
$18$–$24\ \mathrm{m}$. **The specification must state a target depth** ("$V_s$ to
$30\ \mathrm{m}$ with a resolution of $2\ \mathrm{m}$"), because "a $V_s$ profile"
without a depth is exactly the ambiguity this exercise is about. A passive
(microtremor) array can extend the depth range beyond the active source's reach and
is the standard remedy.

---

## ★8 — Two profiles, one $V_{S30}$, different settlements

Construct profile A with $V_{S30} = 300\ \mathrm{m\,s^{-1}}$ exactly:
$10\ \mathrm{m}$ at $150$ and $20\ \mathrm{m}$ at $600\ \mathrm{m\,s^{-1}}$ gives
$T = 10/150+20/600 = 0.066667+0.033333 = 0.100000\ \mathrm{s}$, so
$V_{S30} = 300.0\ \mathrm{m\,s^{-1}}$. Profile B is uniform at
$300\ \mathrm{m\,s^{-1}}$.

For an equivalent uniform half-space, use the **travel-time-weighted operative
modulus**: weight each layer's $G$ at the design strain by its fraction of the
column's travel time. With $\rho = 1900\ \mathrm{kg\,m^{-3}}$,
$\tau_{\max} = 50\ \mathrm{kPa}$, $\gamma = 10^{-3}$, $\nu = 0.30$:

| profile | $V_s$ (m/s) | weight | $G_{\max}$ (MPa) | $\gamma_r$ | $G/G_{\max}$ at $10^{-3}$ | $G$ (MPa) |
|---|---|---|---|---|---|---|
| A | $150$ | $0.6667$ | $42.75$ | $1.170\times10^{-3}$ | $0.5391$ | $23.05$ |
| A | $600$ | $0.3333$ | $684.0$ | $7.31\times10^{-5}$ | $0.0681$ | $46.58$ |
| B | $300$ | $1.0000$ | $171.0$ | $2.924\times10^{-4}$ | $0.2263$ | $38.70$ |

Weighted operative modulus:

$$G_A = 0.6667(23.05) + 0.3333(46.58) = 30.90\ \mathrm{MPa}
\;\Rightarrow\; E_A = 80.3\ \mathrm{MPa},$$

$$G_B = 38.70\ \mathrm{MPa} \;\Rightarrow\; E_B = 100.6\ \mathrm{MPa}.$$

Settlement of a $2\ \mathrm{m}$ square footing at $150\ \mathrm{kPa}$
($a = 1.1284\ \mathrm{m}$, $1-\nu^2 = 0.91$):

$$\delta_A = \frac{\pi}{2}\frac{(150)(1.1284)(0.91)}{80.3\times10^{3}}
= 3.01\ \mathrm{mm}, \qquad
\delta_B = \frac{2.405\times10^{2}}{100.6\times10^{3}} = 2.40\ \mathrm{mm}.$$

**Result: equal $V_{S30}$, settlements differing by $26\%$.** The reason is visible
in the table: at design strain the soft layer's $G$ ($23.1\ \mathrm{MPa}$) is not
much below the stiff layer's ($46.6\ \mathrm{MPa}$), because the soft soil starts
closer to its reference strain. $V_{S30}$ is a small-strain travel-time average and
carries no information about the strain dependence of the layers it averages;
using it as the sole description of a site is a statement that the strain
dependence does not matter, which is false whenever the profile is strongly
contrasted.

**What the single number is and is not.** $V_{S30}$ is a well-defined, comparable
site parameter for *classification* — a code band, a first-order indicator of
amplification. It is not a stiffness for settlement, and two sites with equal
$V_{S30}$ can behave differently by tens of per cent under the same load. The
second number to report is the profile's contrast (or the weighted operative
modulus), not a second $V_{S30}$.

---

## ★9 — Arguing that neither factor of safety is "the" one

**The argument.** Both numbers are outputs of *empirical* resistance curves, each
fitted to its own database: the NCEER $CRR$–$(N_1)_{60cs}$ relation to case
histories classified by penetration testing, the Andrus–Stokoe $CRR$–$V_{s1}$
relation to a different (and smaller) set of case histories. Neither is a physical
law, and the two are not calibrated against each other by construction. A factor of
two between them at one depth is therefore *expected* — it is the model
uncertainty — and it is larger than either measurement's stated uncertainty
($3\%$). Reporting one of them to two decimal places would represent a model choice
as a measurement.

**Why the disagreement cannot be closed by better measurement of the same kind.**
To raise $FS_N$ from $0.42$ to $0.78$ requires $CRR_N$ to rise by $86\%$, from
$0.096$ to $0.179$. Solving the NCEER form,

$$\frac{1}{34-N} + \frac{N}{135} + \frac{50}{(10N+45)^{2}} - \frac{1}{200} = 0.179
\;\Rightarrow\; (N_1)_{60cs} \approx 16.9,$$

against the assumed $8.0$: more than a doubling of the normalised, clean-sand
equivalent penetration resistance in the same ground. A better SPT cannot produce
that; only a different ground, or a different relation, can.

**Measurements that would reduce the gap to less than a factor of $1.3$, and their
contributions.**

1. **Fines content and plasticity from samples at the critical depth.** The
   $(N_1)_{60cs}$ correction is the single largest lever in the penetration route:
   a fines-content correction that moves the equivalent clean-sand count from $8$ to
   $14$ alone takes $CRR_N$ from $0.096$ to $0.150$ ($+56\%$). This is a
   *measurement*, not a new model, and it is cheap (a borehole sample and a sieve
   analysis).
2. **A site-specific cyclic test** (cyclic triaxial or simple shear on a recovered
   sample) gives a direct $CRR$ at the in-situ density and stress state, replacing
   the empirical curve in the critical layer. This is the only measurement that can
   *arbitrate* between the two routes rather than refine one of them. Cost: one
   sample, one apparatus, days.
3. **A cross-hole $V_s$ across the critical layer**, to replace the surface-wave
   value: this removes the method-difference term in $V_{s1}$ (of the order of
   $10\%$ in the lesson's three-profile comparison, i.e. about $20\%$ in $CRR$),
   which is much smaller than the fines-content term.
4. **Measured unit weights and a measured water table, at the time of year that
   matters.** Every stress in the calculation is an input, and the water table
   alone can move $CSR$ by tens of per cent between seasons.

**What to report meanwhile.** Both factors of safety with their procedures named,
the statement that the spread is model uncertainty rather than measurement error,
and — for a decision — the *lowest* of the routes as the screening value, plus a
sensitivity to the water table. That is defensible; averaging the two would be
choosing a number that no procedure produced.
