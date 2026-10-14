# Solutions — 11-02-06 IP for Disseminated Sulphides and Porphyry Systems

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All model parameters are **SYNTHETIC**.

Lesson: [06 IP for Minerals](../06-ip-for-minerals.md).

---

## ★1 — Intrinsic chargeability

$$m = \frac{R_0 - R_\infty}{R_0} = \frac{180-162}{180} = 0.1000 .$$

Phase at the corner, Debye case:

$$\phi = \arctan\!\left(\frac{m}{2-m}\right) = \arctan\!\left(\frac{0.1}{1.9}\right)
= \arctan(0.052632) = 0.052584\ \mathrm{rad} = 52.58\ \mathrm{mrad}.$$

Below 100 mrad the phase is small enough that the small-angle approximation
$\phi \approx m/2$ is within a few per cent: $0.1/2 = 50$ mrad against
$52.58\ \mathrm{mrad}$ — a $5\%$ error, which is exactly the size of the
correction that $\arctan$ supplies. **A frequent mistake is to report the
chargeability as twice the peak phase; it is close but not correct, and the
exact relation is the $\arctan$ above.**

---

## ★2 — Amplitude and phase versus frequency

With $R_0 = 180$, $m = 0.1$, $\tau = 0.25\ \mathrm{s}$ ($f_{\text{corner}} =
0.6366\ \mathrm{Hz}$), $c = 1$:

$$Z = R_0\frac{1+i\omega\tau(1-m)}{1+i\omega\tau}.$$

| $f$ (Hz) | $\omega\tau$ | $\lvert Z\rvert$ (Ω m) | phase (mrad) |
|---|---|---|---|
| 0.1 | 0.1571 | 179.588 | 0.88 |
| 0.6366 | 1.0000 | 171.237 | 3.01 |
| 4.0 | 6.2832 | 162.469 | 0.99 |

Check: $R_0(1-m) = 162\ \Omega\,\mathrm{m}$ and the amplitude at $4\ \mathrm{Hz}$
is $162.469$, close to the high-frequency limit but not yet at it ($\omega\tau = 6.3$
is only a factor of $6.3$ above the corner).

**Note where the phase peaks**: between $0.1$ and $4\ \mathrm{Hz}$ the maximum in
this coarse sampling is at the corner, with only $3.01\ \mathrm{mrad}$ — a
reminder that a *single* frequency sampled away from the corner underestimates the
polarisation badly, and that the phase is a peaked function whose location carries
the $\tau$ information.

---

## ★3 — The phase-area bias

$$-\ln(1-m) = -\ln(0.75) = 0.287682 .$$

Reporting the phase area as the chargeability gives $0.28768$ against the true
$m = 0.25$:

$$\text{bias} = \frac{0.287682}{0.25} - 1 = +15.07\% .$$

The bias grows with $m$ (it is $m/2 + m^2/3 + \cdots$); at $m = 0.5$ it reaches
$+38.6\%$. Since the correction is a closed form and the area is trivially
computed, an uncorrected phase-area chargeability is always an avoidable
overestimate — and it is the *reason* that published chargeabilities sometimes
exceed the physical range implied by a sample's resistivity ratio.

---

## ★4 — Mixture chargeability, $R_b/R = 6$

$$m = \frac{\phi R_b}{R+\phi R_b} = \frac{6\phi}{1+6\phi}.$$

| $\phi$ | $m$ |
|---|---|
| 0.01 | 0.05660 |
| 0.05 | 0.23077 |
| 0.20 | 0.54545 |

**Not linear**: from $\phi = 0.01$ to $0.05$ (a factor of five) $m$ rises by a
factor of $4.08$; from $0.05$ to $0.20$ (a factor of four) $m$ rises by only a
factor of $2.36$. The relation approaches saturation as $\phi\to1$, where
$m\to R_b/(R+R_b) = 6/7 = 0.857$. **The marginal efficiency of added sulphide
falls**, which is why a rock with 1% sulphide can already be an IP anomaly and a
rock with 10% is not ten times stronger.

---

## ★5 — Blocked fraction from $m$, and the parallel path

With $R_b/R = 12$ and $m = 0.30$:

$$0.30 = \frac{12\phi}{1+12\phi} \Longrightarrow 0.30 + 3.6\phi = 12\phi
\Longrightarrow \phi = \frac{0.30}{8.4} = 0.035714 .$$

**About 3.6% of the current paths are blocked** — the quantitative statement of
why IP finds a few per cent of sulphide.

Now add a connected path with $R_s = R/15$. With $A = R_{\text{HF}}/R = 1$,
$B = R_{\text{DC}}/R = 1.428571$, and the parallel combination
$X\parallel R_s = XR_s/(X+R_s)$:

$$A\parallel R_s = \frac{1 \times (1/15)}{1 + 1/15} = 0.062500,$$

$$B\parallel R_s = \frac{1.428571 \times (1/15)}{1.428571 + 1/15}
= \frac{0.095238}{1.495238} = 0.063694,$$

$$m_{\text{meas}} = \frac{0.063694-0.062500}{0.063694} = 0.01875 .$$

**The measured chargeability collapses from $0.300$ to $0.0188$ — a factor of 16.**
The parallel conductor carries most of the current, so most of the current never
crosses a polarisable interface.

**Physical interpretation:** the same total sulphide content produces a strong IP
response when it is disseminated (all paths blocked, current forced across
interfaces) and a weak one when it is connected (current short-circuited). This is
the disseminated-versus-massive distinction, and it means that IP and EM answer
*different questions* about the same body rather than confirming each other.

---

## ★6 — What a chargeability reading actually pins down

For $m = 0.30$ with $\tau = 0.5\ \mathrm{s}$:

$$M(0.2,0.8) = 0.3\frac{0.5(e^{-0.4}-e^{-1.6})}{0.6} = 0.3(0.39035)
= 0.11711 \rightarrow 117.1\ \mathrm{mV/V}.$$

A survey reading $45\ \mathrm{mV/V}$ in that window therefore implies
$m = 0.30 \times 45/117.1 = 0.1153$ **if the relaxation time is $0.5\ \mathrm{s}$**.

| window | $\tau = 0.5$ s | $\tau = 2.0$ s |
|---|---|---|
| 100–300 ms | 77.8 mV/V | 52.1 mV/V |
| 200–800 ms (the reading) | 45.0 | 45.0 |
| 800–2400 ms | 6.98 mV/V | 26.6 mV/V |
| ratio late/early | **0.0897** | **0.510** |

For $\tau = 2.0\ \mathrm{s}$ the same $45\ \mathrm{mV/V}$ reading implies
$m = 0.0576$ — **half** the value implied for $\tau = 0.5\ \mathrm{s}$.

**The widest spread found:** for $\tau = 0.5\ \mathrm{s}$ the ratio between the late
and early windows is $0.0897$, i.e. an **11-fold** difference in the reported
chargeability for the same rock. For $\tau = 2\ \mathrm{s}$ the spread is a factor
of $2$. The conclusion is that a time-domain chargeability is a
window-and-$\tau$-weighted integral: it is a legitimate *survey-specific*
measurement, but it is not a rock property, and comparing it across surveys with
different windows (or comparing it to a laboratory Cole-Cole $m$) requires the
window and the decay to be stated.

---

## ★7 — The exponent $c$ and the phase at a single frequency

At the corner frequency $0.16\ \mathrm{Hz}$, $m = 0.2$, $\tau = 1\ \mathrm{s}$:

| $c$ | phase at 0.16 Hz (mrad) | peak phase (mrad) | peak $f$ (Hz) |
|---|---|---|---|
| 0.4 | 36.09 | 36.21 | ~0.26 |
| 0.6 | 56.57 | 56.77 | ~0.19 |
| 1.0 | 110.72 | 111.34 | ~0.18 |

**A factor of three in the measured phase from $c$ alone, at fixed $m$.** The
implication for a narrow-band survey is severe: a survey that measures phase only
near one frequency cannot separate a rock with $(m = 0.2, c = 0.4)$ from one with
$(m = 0.1, c = 1.0)$, because both give about $55\ \mathrm{mrad}$. Any $m$
inverted from a single frequency is therefore conditional on an assumed $c$, and
$c$ is the parameter a narrow band constrains worst (the lesson's grid search:
$c$ spans $0.400$–$0.825$ within the noise floor at half a decade of bandwidth,
against $0.600$–$0.625$ at two decades).

---

## ★8 — Clay against sulphide at equal $m$

Both models have $m = 0.18$. Clay: $\tau = 0.01\ \mathrm{s}$, $c = 0.9$.
Sulphide: $\tau = 1.5\ \mathrm{s}$, $c = 0.6$.

| observable | clay | sulphide | ratio |
|---|---|---|---|
| peak phase (mrad) | 84.63 | 50.51 | 0.60 |
| peak frequency (Hz) | 17.77 | 0.125 | 142 |
| $M$(100–500 ms) (mV/V) | $2.0\times10^{-4}$ | 147.8 | $7.2\times10^{5}$ |

**Which observable separates them, and by how much?**

1. **Peak frequency: a factor of 142.** This is the *window-independent*
   observable, and it is the one to use: it requires only that the spectrum span
   both frequencies, i.e. roughly three decades.
2. **Windowed chargeability: a factor of $7\times10^{5}$ in this window** — but
   *only because the window was chosen long*. In a $5$–$20\ \mathrm{ms}$ window
   the clay gives $56.5\ \mathrm{mV/V}$ and the sulphide $178.5\ \mathrm{mV/V}$: a
   factor of only $3.2$, and with the clay now *under*-represented rather than
   over-represented. The time-domain separation therefore depends entirely on
   whether the window matches the relaxation, and a survey designed for a slow
   sulphide will systematically miss a fast clay — which is a success by accident,
   not by design.

**Conclusion:** use the peak frequency (or a full multi-decade fit) to identify
the polarisation mechanism, and use the windowed chargeability to *quantify* it
once the mechanism is known. Reversing that order produces a number with no
interpretation.

---

## ★9 — Design to separate disseminated sulphide from clay

**Frequency band.** The two mechanisms are separated by the peak frequency, so the
band must span at least three decades containing both peaks: from about
$2\times10^{-2}\ \mathrm{Hz}$ (below a slow sulphide's corner) to about
$5\times10^{2}\ \mathrm{Hz}$ (above a clay's). In practice: $0.0156$, $0.0625$,
$0.25$, $1$, $4$, $16$, $64$, $256\ \mathrm{Hz}$ — **eight frequencies in a
geometric series**, which is the standard decade-and-a-half coverage.

**Observable to fit.** The phase spectrum (not the amplitude, which carries the
geometry), fitted with a **two-term Cole-Cole model**: one term per polarisation
mechanism. Report both $(m_1,\tau_1,c_1)$ and $(m_2,\tau_2,c_2)$, plus the
covariance between them.

**Decision rule.** A target is sulphide-dominated if the term with
$\tau \gtrsim 0.1\ \mathrm{s}$ carries more than half of the total
$-\ln(1-m_1) - \ln(1-m_2)$ phase area; clay-dominated if the short-$\tau$ term
dominates. Report the fitted *areas* rather than the $m$'s, because the area is the
well-determined combination (lesson §2 and §3).

**Computed separability.** Fitting the *clay* model to a *sulphide* spectrum over
$0.015$–$256\ \mathrm{Hz}$ with a $1\ \mathrm{mrad}$ noise floor gives a mismatch
dominated by the location of the peak: the sulphide's phase peaks near
$0.13\ \mathrm{Hz}$ and falls to a few mrad by $20\ \mathrm{Hz}$, whereas the clay
form has its maximum near $18\ \mathrm{Hz}$. The two are separated at the peak
positions, so the **discriminating power comes from frequency coverage, not from
amplitude precision**: halving the number of frequencies but keeping three decades
loses almost nothing, whereas halving the bandwidth destroys the test. (This is the
quantitative form of lesson §3's bandwidth table.)

**One more design element.** Include a *repeat* measurement with the array
rotated, to check for anisotropy and for EM coupling, which corrupts the
high-frequency end precisely where the clay signature lives.

---

## ★10 — EM coupling as a spurious response

Model the coupling contribution to the phase as

$$\phi_{\text{coup}}(f) = a\sqrt{\omega}, \qquad
a = 2\times10^{-3}\ \mathrm{rad\,s^{1/2}} \ (\text{SYNTHETIC}),$$

so at $f = 100\ \mathrm{Hz}$ it contributes
$2\times10^{-3}\sqrt{628} = 0.0501\ \mathrm{rad} = 50.1\ \mathrm{mrad}$ — comparable
to the polarisation signal at that frequency, and growing with frequency.

Same quantities, before and after contamination:

| band | contaminated quantity | bias |
|---|---|---|
| 2 decades (0.016–1.59 Hz) | $m$ inverted from the phase area | high by the coupling's contribution at the top of the band, $\approx +8\%$ |
| 2 decades | $\tau$ | shortened (the coupling mimics a fast relaxation) |
| 0.5 decade near 10 Hz | $m$ | high by a factor $\approx 2$, because the coupling dwarfs the signal |
| 0.5 decade near 0.1 Hz | $m$ | almost unbiased (coupling is $\approx 5$ mrad there) |

**Why resistive ground is worse.** Coupling scales with the *inductive* response of
the ground, i.e. with the product of the array's mutual inductance and the ground
conductivity's ability to support a current loop. In a resistive ground the
polarisation signal itself is weak (little surface conduction), so a coupling
contribution of the same absolute size becomes a much larger fraction of the
measurement. Dipping the array into a conductive overburden can therefore *reduce*
the apparent coupling bias while reducing the target response.

**Geometry change that reduces the bias.** Reduce the transmitter–receiver
separation and/or the wire loop area: coupling grows roughly as the square of the
dipole length. Practical rules are a single short dipole with the receiver inside
the transmitter loop, and a *delay* in the time domain (the coupling decays much
faster than a slow polarisation, so windowing at late times separates them — the
same separation-by-shape argument as in
[11-02-04](../04-em-for-minerals.md) §4).

**Diagnostic.** A *negative* negative-phase behaviour at high frequency, or an
apparent $c > 1$, is the signature of uncorrected coupling: the coupling term
$\propto\sqrt{\omega}$ has no natural peak and therefore cannot be fitted by any
Cole-Cole term with $c\le1$.

---

## ★11 — The blocked-path model as a network (specification and expected result)

**Construction.** Build a $40\times40$ square lattice of nodes; each nearest-neighbour
bond is a resistor $R$; replace a randomly chosen fraction $\phi$ of the bonds with
a series combination $R_1 + (R_b \parallel C)$ where $R_1 + R_b = R$ so that the
DC resistance of a replaced bond exceeds the plain bond. Inject current across one
pair of opposite edges and measure the voltage across the opposite pair; compute
$R_{\text{HF}}$ (capacitors shorted) and $R_{\text{DC}}$ (capacitors open) and form
$m = (R_{\text{DC}}-R_{\text{HF}})/R_{\text{DC}}$. Average over $\ge20$
realisations per $\phi$.

**Expected result and where it diverges from the closed form.**

1. **At small $\phi$** the network reproduces the closed form
   $\phi R_b/(R+\phi R_b)$ closely, because the current paths are essentially
   independent and each blocked bond contributes independently. The measured slope
   $m/\phi \to R_b/R$ as $\phi\to0$, as in the lesson's limit check.
2. **At intermediate $\phi$** the two curves separate, and the network gives a
   *lower* $m$ than the closed form: in a network the current can route *around* a
   blocked bond through neighbouring paths, whereas the series model forces the
   current through every blocked element. This is a genuine percolation effect.
3. **Above the percolation threshold for the high-resistance bonds** the network
   develops a connected path of unblocked bonds, the current largely bypasses the
   polarisable elements, and $m$ *falls* with increasing $\phi$ — the
   same mechanism as the parallel-conductor collapse in ★5, appearing here
   spontaneously rather than by construction.

**Why this matters.** The closed form is a *series* model: it cannot represent
current routing. Real rocks route current, which is why the measured $m$ saturates
and then declines as sulphide content rises, and why a widely used empirical rule
"chargeability increases with sulphide content" fails at high content. The network
experiment is the cheapest way to see the mechanism without pretending to model a
specific rock texture.
