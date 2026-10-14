---
id: 11-02-06
title: "IP for Disseminated Sulphides and Porphyry Systems"
level: graduate
prereqs: ["09-03-01", "09-03-02", "11-02-04"]
tags: [exploration-geophysics, mineral-exploration, induced-polarisation, cole-cole, chargeability, porphyry]
---

# IP for Disseminated Sulphides and Porphyry Systems

Induced polarisation is the method that finds *disseminated* sulphide, which is
to say the method that finds porphyry copper systems. Its physics is
electrochemical rather than electromagnetic, and its central result is
counter-intuitive: **the polarisation is carried by the surface area of
polarisable grains acting on the whole current path, not by the bulk mineral
content.** A rock with 5% sulphide can be a far stronger IP target than one with
50%, and a massive sulphide body can be nearly *invisible* to IP while being
blindingly obvious to EM. This lesson derives that result from a blocked-path
mixture model, sets up the Cole-Cole description, derives and verifies the
phase-area identity, and shows that every chargeability anyone ever quotes is
window-dependent.

**All models and data in this module are SYNTHETIC.** Cole-Cole parameters,
circuit resistances, volume fractions, time windows and noise levels are chosen
teaching values, not measurements or properties of any real deposit.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write down** the Cole-Cole impedance and **verify** its DC and
   high-frequency limits against the definition of chargeability.
2. **Derive** the phase at the corner frequency for the Debye case,
   $\phi = \arctan\!\left(\frac{m}{2-m}\right)$, and **explain** why it is not
   quite the maximum.
3. **Derive and verify** the phase-area identity
   $(2/\pi)\int\phi\,\mathrm{d}\ln\omega = -\ln(1-m)$, and **quantify** the bias
   created when the phase area is used as the chargeability.
4. **Compute** the chargeability of a blocked-path mixture,
   $m = \phi R_b/(R+\phi R_b)$, and **show** both its sub-linearity and the
   collapse produced by a parallel conducting path.
5. **Compute** the window dependence of a time-domain chargeability and **state**
   what must accompany any quoted value.
6. **Measure** the (m, τ, c) parameter ranges that fit a spectrum within a stated
   noise floor, and **show** how those ranges widen as bandwidth narrows.
7. **Explain** why clay and sulphide polarisation are separated by relaxation
   frequency rather than by amplitude, and **state** the bandwidth requirement.

## Prerequisites

- [09-03-01 IP Principle: Time-Domain and Frequency-Domain Measurement](../../09-electrical-em-methods/03-induced-polarisation/01-ip-principle.md)
  — the measurement and its units.
- [09-03-02 IP Models: Cole-Cole, Debye, Constant-Phase Element](../../09-electrical-em-methods/03-induced-polarisation/02-ip-models.md)
  — the model family used here.
- [11-02-04 EM for Conductors, Massive Sulphides and Graphite](04-em-for-minerals.md)
  — the conductivity that IP must be distinguished from.

## 1. The Cole-Cole impedance and its limits

The standard description of a polarisable rock is the Cole-Cole complex
resistivity

$$\boxed{\;Z(\omega) = R_0\left[1 - m\left(1 -
\frac{1}{1+(i\omega\tau)^{c}}\right)\right]\;}$$

with $R_0$ the DC resistivity, $m$ the **intrinsic chargeability**
($0\le m<1$), $\tau$ a relaxation time and $c$ an exponent ($0<c\le 1$) that
measures how widely the relaxation times are distributed. Its limits follow
directly:

$$Z(0) = R_0\left[1 - m(1-1)\right] = R_0, \qquad
Z(\infty) = R_0\left[1-m(1-0)\right] = R_0(1-m),$$

so $m = (R_0 - R_\infty)/R_0$ exactly — the definition of chargeability, recovered
rather than assumed. The demonstration confirms both limits numerically:
$Z(f\to0) = 99.9999\ \Omega\,\mathrm{m}$ against $R_0 = 100$, and
$Z(f\to\infty) = 80.0000\ \Omega\,\mathrm{m}$ against $R_0(1-m) = 80$, giving
$m = 0.2000$ for a model set to $m = 0.20$.

For the SYNTHETIC sample $\tau = 1\ \mathrm{s}$, $c = 0.60$ (corner
$1/(2\pi\tau) = 0.1592\ \mathrm{Hz}$):

| $f$ (Hz) | $\lvert Z\rvert$ (Ω m) | phase (mrad) |
|---|---|---|
| 0.01 | 97.683 | 25.00 |
| 0.10 | 91.871 | 54.15 |
| 0.16 | 90.124 | 56.57 |
| 1.00 | 84.146 | 42.56 |
| 10.00 | 81.022 | 15.07 |
| 100.00 | 80.249 | 4.12 |
| 1000.00 | 80.062 | 1.06 |

**The phase is the workhorse observable in the frequency domain**, because it is
insensitive to the geometrical factor (the same electrodes give the same geometry
for the in-phase and quadrature components), whereas the *amplitude* depends on
array geometry.

### The phase at the corner, for the Debye case

Set $c = 1$. Then

$$\frac{Z}{R_0} = \frac{1 + i\omega\tau(1-m)}{1+i\omega\tau},
\qquad
\phi(\omega) = \arctan(\omega\tau) - \arctan\!\left(\omega\tau(1-m)\right),$$

and at the corner $\omega\tau = 1$,

$$\phi = \arctan 1 - \arctan(1-m) = \frac{\pi}{4}
- \arctan(1-m) \equiv \arctan\!\left(\frac{m}{2-m}\right),$$

using $\arctan a - \arctan b = \arctan\frac{a-b}{1+ab}$. For $m = 0.2$ this gives
$110.657\ \mathrm{mrad}$. The demonstration measures the **maximum** at
$111.341\ \mathrm{mrad}$, at $\omega\tau = 1.118$: the corner value is *not* the
maximum, and for the Debye case the peak sits slightly above the corner (here by
$0.6\%$). Quoting the corner formula as "the peak phase" is a small but real
error, and the correct statement is the one the demonstration makes.

For $c = 0.60$ the peak phase falls to $56.775\ \mathrm{mrad}$ — **less than half
the Debye value at the same $m$** — because the exponent $c$ spreads the
relaxation over decades of frequency, and a spread relaxation polarises less at any
single frequency without any change in the total polarisation. This is the single
most important practical fact about IP modelling: $m$ and $c$ trade off directly
against each other in the amplitude of the phase anomaly.

## 2. The phase-area identity

Integrating the Debye phase over log frequency gives a closed form. Write
$\phi = \arctan u - \arctan(u(1-m))$ with $u = \omega\tau$ and use
$\arctan u - \arctan(au) = \int_a^1 \frac{u\,\mathrm{d}v}{1+u^2v^2}$:

$$\int_0^\infty \phi\,\mathrm{d}\ln\omega
= \int_1^{1/(1-m)}\!\!\int_0^\infty \frac{u}{1+u^2v^2}\,\mathrm{d}\ln u\,
\mathrm{d}v
= \frac{\pi}{2}\ln\frac{1}{1-m},$$

so

$$\boxed{\;\frac{2}{\pi}\int_0^{\infty}\phi(\omega)\,\mathrm{d}\ln\omega
= -\ln(1-m) = m + \frac{m^2}{2} + \frac{m^3}{3} + \cdots\;}$$

The demonstration verifies this to $0.03$–$0.04\%$ across $m = 0.05$ to $0.40$
(the residual is the finite integration range). **Two consequences:**

1. **The phase area is a robust chargeability estimator.** It is an integral, so
   it is insensitive to where the peak sits and to the noise in any single
   frequency — a genuine advantage when the spectrum is noisy or truncated.
2. **It over-estimates $m$.** Reading the area as the chargeability gives
   $0.22306$ where $m = 0.20$: a bias of $+11.5\%$, exactly
   $-\ln(1-m)/m - 1 = m/2 + m^2/3 + \cdots$. An inverted chargeability from a
   phase-area calculation is high by this amount, and the correction is available
   in closed form, so there is no reason to leave it in.

## 3. Worked example — how well are (m, τ, c) determined?

A spectrum is not a set of three independent measurements, and the honest output of
an IP inversion is a *range*. Two measurements make this concrete.

**Local sensitivity.** The Jacobian of the phase spectrum with respect to
$(m,\tau,c)$ for the SYNTHETIC sample has singular values
$2.0931$, $2.8078\times10^{-1}$ and $4.8206\times10^{-2}$ rad per unit parameter —
a condition number of **43.4**. The least-sensitive direction is
$(-0.064,\,-0.977,\,+0.206)$, i.e. almost pure $\tau$ with opposing $c$:
**lengthening $\tau$ and lowering $c$ together changes the spectrum by only
$2.3\%$ of an equivalent move along the most sensitive direction.**

**Global parameter ranges.** Sweeping $m\in[0.12,0.30]$,
$\tau\in[0.4,2.5]\ \mathrm{s}$, $c\in[0.30,0.90]$ and requiring an rms phase
misfit below the $1\ \mathrm{mrad}$ noise floor:

| bandwidth | $f$ range (Hz) | sets within 1 mrad | $m$ range | $\tau$ range (s) | $c$ range |
|---|---|---|---|---|---|
| 2 decades | 0.016–1.59 | 2 | 0.195–0.202 | 1.013–1.013 | 0.600–0.625 |
| 1 decade | 0.050–0.50 | 15 | 0.180–0.225 | 0.925–1.100 | 0.525–0.675 |
| 0.5 decade | 0.089–0.28 | 78 | 0.142–0.300 | 0.663–1.625 | 0.400–0.825 |

with the true values $m = 0.20$, $\tau = 1.0\ \mathrm{s}$, $c = 0.60$. **The
ambiguity of an IP model is a bandwidth question.** With two decades of spectrum
the parameters are determined to a few per cent; with half a decade, $m$ ranges
over a factor of two and $c$ over a factor of two. Reporting a single fitted
triplet from a narrow-band survey is therefore a claim the data cannot support,
and the defensible report is the admitted range.

## 4. Why 5% sulphide beats 50% sulphide

### The blocked-path mixture

Model the rock as a series of $n$ unit cells each of resistance $R$, with a
fraction $\phi$ of them containing a polarisable grain: an insulating interface
shunted by a double-layer capacitance, in series with a resistance $R_b$. At high
frequency the capacitances short and

$$R_{\text{HF}} = nR;$$

at DC they open and

$$R_{\text{DC}} = nR + \phi n R_b = nR\left(1+\phi\frac{R_b}{R}\right),$$

so

$$m_{\text{mix}}(\phi) = \frac{R_{\text{DC}}-R_{\text{HF}}}{R_{\text{DC}}}
= \frac{\phi R_b}{R + \phi R_b}.$$

Measured, with $R_b/R = 10$:

| $\phi$ | $m$ (model) | linear $4.5\phi$ | ratio |
|---|---|---|---|
| 0.005 | 0.04762 | 0.02250 | 2.12 |
| 0.020 | 0.16667 | 0.09000 | 1.85 |
| 0.050 | 0.33333 | 0.22500 | 1.48 |
| 0.100 | 0.50000 | 0.45000 | 1.11 |
| 0.200 | 0.66667 | 0.90000 | 0.74 |
| 0.400 | 0.80000 | 1.80000 | 0.44 |

The relation is strongly sub-linear and saturating, and at **5% blocked paths the
polarisation is already $m = 0.333$**. That is why IP detects a few per cent of
sulphide: the mechanism acts on the *entire current path*, not on the volume of
mineral. The demonstration verifies both limits: $m/\phi \to R_b/R = 10$ as
$\phi\to0$, and $m \to R_b/(R+R_b) = 0.909091$ as $\phi\to1$.

### The parallel conductor: massive sulphide

Now add a parallel conducting path of resistance $R_s$ — connected sulphide. The
current takes the short circuit around the polarisable interfaces:

| $\phi$ | $R_s = \infty$ | $R_s = R$ | $R_s = R/5$ | $R_s = R/20$ |
|---|---|---|---|---|
| 0.020 | 0.16667 | 0.08333 | 0.02778 | 0.00794 |
| 0.100 | 0.50000 | 0.25000 | 0.08333 | 0.02381 |
| 0.300 | 0.75000 | 0.37500 | 0.12500 | 0.03571 |

**A well-connected conductor destroys the measured chargeability**: at
$R_s = R/20$ the same rock that shows $m = 0.75$ unshunted shows $0.036$ — a
factor of $21$ smaller.

**This is the disseminated-versus-massive distinction, quantified.** Disseminated
sulphide blocks current paths (strong IP, poor conductivity → EM blind). Massive
sulphide provides a conducting path (weak relative IP, strong conductivity → EM
bright). The two methods are therefore *complementary rather than redundant*, and
a program that flies EM and then tries to certify sulphide from conductivity alone
is missing exactly the measurement that distinguishes the ore from the graphite
([11-02-04](04-em-for-minerals.md) §6).

## 5. Every chargeability is window-dependent

In the time domain the measured quantity is a windowed integral of the decay. For
the Debye case the excess voltage decays as $V(t) = V_p m e^{-t/\tau}$ after
switch-off, so over a window $(t_1,t_2)$

$$\boxed{\;M(t_1,t_2) = \frac{m\tau\left(e^{-t_1/\tau}-e^{-t_2/\tau}\right)}
{t_2-t_1}\;}$$

measured in mV/V as $1000\,M$. Measured for the SYNTHETIC sample ($m = 0.20$):

| $\tau$ (s) | 100–300 ms | 500–1500 ms | 1–3 s |
|---|---|---|---|
| 0.05 | 6.64 | 0.00 | 0.00 |
| 0.20 | 76.68 | 3.26 | 0.13 |
| 1.00 | 164.02 | 76.68 | 31.81 |
| 5.00 | 192.17 | 164.02 | 134.96 |

(values in mV/V; the intrinsic $m = 0.20$ corresponds to 200 mV/V)

**No window ever recovers $m$.** The largest value in the table is
$192\ \mathrm{mV/V}$ (a wide early window on a slowly relaxing rock) and the
smallest is essentially zero. The ratio between the narrow early window and the
wide late window for the *same rock*:

| $\tau$ (s) | 0.05 | 0.20 | 1.00 | 5.00 |
|---|---|---|---|---|
| ratio | $6.4\times10^{8}$ | 569 | 5.16 | 1.42 |

A factor of $5$ for a typical $\tau = 1\ \mathrm{s}$ rock, and a factor of
$570$ for a fast-relaxing one. **Quoting a chargeability without its window and
delay is quoting an incomplete number**, exactly as quoting an anomaly amplitude
without its station spacing would be. The good practice is to report the window
and either the full decay or the model parameters; the bad practice is to compare
chargeabilities from two surveys with different windows and attribute the
difference to geology.

## 6. Clay against sulphide

Membrane polarisation in clays produces a Cole-Cole response too, and it is the
classic false positive of the method. For the SYNTHETIC pair:

| case | $m$ | $\tau$ (s) | $c$ | peak phase (mrad) | peak $f$ (Hz) | phase area |
|---|---|---|---|---|---|---|
| sulphide (disseminated) | 0.200 | 1.000 | 0.60 | 56.775 | 0.192 | 0.22103 |
| clay (membrane) | 0.150 | 0.020 | 0.85 | 64.003 | 8.757 | 0.16247 |
| weak sulphide | 0.050 | 1.000 | 0.60 | 13.067 | 0.166 | 0.05077 |
| weak clay | 0.050 | 0.020 | 0.85 | 20.216 | 8.204 | 0.05128 |

**The separation is carried by the relaxation frequency, not by the amplitude:**
the clay's phase peaks near $8\ \mathrm{Hz}$ and the sulphide's near
$0.2\ \mathrm{Hz}$ — a factor of $40$ — while their peak phases are within $15\%$
of each other. A single-frequency chargeability measurement cannot distinguish them
at all, and neither can a narrow-band spectrum: the diagnostic *is* the location
of the peak. This is one of the few places in this module where **more bandwidth
resolves an ambiguity rather than merely measuring it better**, and it is the
technical justification for multi-decade or time-domain IP systems in terrains
where clay is abundant.

## 7. Assumptions and regime of validity

1. **The Cole-Cole model is a description, not a mechanism.** It fits the
   frequency dependence of the *bulk* response; it does not identify the
   polarising mineral.
2. **The blocked-path mixture is a lumped model.** It is not a field-theory
   derivation of the mixture response; it captures the correct saturation
   behaviour and the correct limiting values, and it does not predict the exact
   shape of $m(\phi)$ for a real texture.
3. **Isotropic, uniform polarisation.** Real rocks have a distribution of grain
   sizes (hence of $\tau$), a distribution of connectivities, and often two
   distinct polarisation mechanisms in the same volume (clay *and* sulphide).
4. **The window model assumes a single exponential decay (Debye case).** For
   $c<1$ the decay is a Mittag-Leffler-type function: slower to establish and
   slower to die, so the window dependence is *stronger* than the table in §5.
5. **Small-signal linearity.** The measured polarisation is assumed proportional to
   the injected current density; at high current density the response is
   non-linear, and the choice of transmitter current changes the apparent $m$.
6. **Galvanic contact.** IP requires injected current, so dry sand, resistive
   laterite and paved ground ruin the measurement; the deployment cost, not the
   physics, dominates the method's logistics.
7. **No electromagnetic coupling.** The measurement of a decaying voltage also
   contains the EM response of the ground, which grows with resistivity contrast
   and with array size. Separating it requires a delay or a modelling step, and
   uncorrected coupling appears as a spurious chargeability with a very short
   $\tau$.
8. **All numbers SYNTHETIC**, and the mapping from the model parameters to a
   *mineral* is a petrophysical claim that this lesson does not make.

## 8. Units, dimensional checks and the identities worth memorising

| Quantity | Unit | Check |
|---|---|---|
| $R_0$, $\lvert Z\rvert$ | Ω m | resistivity times a geometry factor that cancels in the ratio |
| $m$, $c$ | – | dimensionless; $0\le m<1$, $0<c\le1$ |
| $\tau$ | s |  |
| phase $\phi$ | rad (report mrad) | argument of a ratio ✔ |
| chargeability $M$ | mV/V or ms | the definition is $(\Delta V/V_0)$ over a window |
| phase area | – | $(2/\pi)\int\phi\,\mathrm{d}\ln\omega$: rad × dimensionless ✔ |

Four identities that make good self-checks:

1. $Z(0) = R_0$ and $Z(\infty) = R_0(1-m)$, hence $m = (R_0-R_\infty)/R_0$;
2. $\phi(\omega\tau=1, c=1) = \arctan(m/(2-m))$;
3. $(2/\pi)\int\phi\,\mathrm{d}\ln\omega = -\ln(1-m)$ for the Cole-Cole family;
4. $M(t_1,t_2) \le m$ always, with equality only in the limit $t_1 = 0$,
   $t_2 \to \infty$ combined with $\tau \to \infty$ — i.e. never in practice.

The demonstration verifies 1, 2, 3 and the window integral, the last against a
direct numerical integration of the decay (agreement to $3\times10^{-8}$).

## 9. Python demonstration

`code/ip_for_minerals_demo.py` prints, with units:

1. the Cole-Cole impedance
   $Z = R_0[1 - m(1 - 1/(1 + (i\omega\tau)^{c}))]$ with
   $R_0 = 100\ \mathrm{\Omega\,m}$, $m = 0.20$, $\tau = 1.00$ s,
   $c = 0.60$, and its limits $Z(0) = R_0$, $Z(\infty) = R_0(1-m)$;
2. the phase-area identity $(2/\pi)\int \varphi\,\mathrm{d}\ln\omega =
   -\ln(1-m)$, and the bias you incur by estimating $m$ from one corner
   phase: the corner phase over-estimates $m$ by $+11.53\%$ here, so a
   single-frequency chargeability is not $m$;
3. the $m$–$\tau$–$c$ trade-off, measured by a grid search at a 1 mrad phase
   noise: two parameter sets fit within two decades of bandwidth, 15 within
   one decade, and 78 within half a decade;
4. why 5% sulphide beats 50% sulphide: $m = \varphi R_b/(R + \varphi R_b)$ is
   dominated by the connected pore fraction once the grains form a network,
   and the demo tabulates the ratio against the linear rule $4.5\varphi$;
5. the window dependence of every chargeability, through
   $M(t_1,t_2) = m\tau(\mathrm{e}^{-t_1/\tau} -
   \mathrm{e}^{-t_2/\tau})/(t_2 - t_1)$ — the same body reports
   100–300 ms, 500–1500 ms and 1–3 s windows differently;
6. clay against sulphide, and the size of the discriminant;
7. verification of the identities used above.

Run it with the project virtual environment:

```bash
cd 11-exploration-geophysics/02-mineral-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_for_minerals_demo.py
```

## 10. Exercises


Full sets with worked solutions:
[`exercises/06-ip-for-minerals-exercises.md`](exercises/06-ip-for-minerals-exercises.md)
and
[`exercises/06-ip-for-minerals-solutions.md`](exercises/06-ip-for-minerals-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC sample has $R_0 = 250\ \Omega\,\mathrm{m}$, $m = 0.12$,
> $\tau = 0.4\ \mathrm{s}$, $c = 0.5$. **(a)** Compute $R_\infty$ and the value of
> the phase at the corner frequency for the Debye case, and the same for
> $c = 0.5$ by explaining why it must be smaller. **(b)** Compute
> $-\ln(1-m)$ and state the bias you would introduce by reporting the phase area
> as the chargeability. **(c)** Compute the chargeability you would measure in a
> $100$–$500\ \mathrm{ms}$ window, in mV/V. **(d)** Using the mixture model with
> $R_b/R = 8$, compute the blocked fraction $\phi$ that would give this $m$, and
> state what a parallel path with $R_s = R/10$ would do to the measured value.
> **(e)** State the two measurements you would add to decide whether the
> polarisation is sulphide or clay.

A worked version is in the
[solutions](exercises/06-ip-for-minerals-solutions.md).

## Common pitfalls

1. **Equating IP with sulphide.** Clay, graphite and even some oxides polarise;
   the method measures polarisability, not mineralogy.
2. **Reporting a chargeability without its window.** A factor of five for a
   typical rock, and a factor of 570 for a fast one.
3. **Reading the phase area as $m$.** Biased high by $11.5\%$ at $m = 0.2$,
   correctable in closed form.
4. **Reading the corner phase as the peak phase.** A $0.6\%$ error at $m = 0.2$,
   and larger for larger $m$.
5. **Trusting a single fitted (m, τ, c).** The admitted range depends on the
   bandwidth, and half a decade gives a factor of two in $m$.
6. **Expecting massive sulphide to give a strong IP response.** Connected
   conductors shunt the polarisable interfaces; IP finds the disseminated case.
7. **Ignoring EM coupling.** It appears as a spurious short-τ chargeability and
   grows with array size and resistivity contrast.
8. **Comparing chargeabilities across surveys without matching windows,
   currents and arrays.** Most disagreements between IP datasets are deployment
   differences before they are geology.

## Related modules

- [11-02-04 EM for Conductors, Massive Sulphides and Graphite](04-em-for-minerals.md)
  — the complementary method, and why conductivity alone cannot certify sulphide.
- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where chargeability sits in the signature vector.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](07-multi-method-targeting.md)
  — combining IP with the other layers, and the correlation traps.
- [09-03 Induced Polarisation](../../09-electrical-em-methods/03-induced-polarisation/README.md)
  — the acquisition and inversion machinery behind this model.
