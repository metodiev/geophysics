---
id: 09-03-01
title: "IP Principle: Time-Domain and Frequency-Domain Measurement"
level: graduate
prereqs: ["09-01-01", "09-01-04", "09-02-03", "01-10-02"]
tags: [electrical-methods, induced-polarisation, chargeability, phase, cole-cole, non-uniqueness]
---

# IP Principle: Time-Domain and Frequency-Domain Measurement

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the three quantities a survey can report for one and the same
   polarisable ground — the window-integral chargeability, the window-average
   chargeability and the phase — and **state the unit of each**.
2. **Derive** the step-off decay of a single-relaxation polarisable element and
   the exact integral chargeability $M = m\tau\left(1 - e^{-T/\tau}\right)$ for
   an integration window of length $T$.
3. **Derive** the phase of that element, locate its maximum analytically, and
   **verify** the closed form $\tan\left|\varphi_{\max}\right| = m/(2\sqrt{1-m})$
   against a numerical search.
4. **Derive** the step-off response from a transfer function, and use it to
   confirm that the decay amplitude is $mV_p$.
5. **Quantify** how the measured chargeability depends on the charging time, the
   integration window and a linear drift, and state which of the three is a
   property of the ground.
6. **Explain** why a broad distribution of relaxation times produces a nearly
   constant phase, and **measure** the constant-phase relation between the
   amplitude slope and the phase.
7. **State** what a time-domain chargeability of one model cannot tell you about
   another model that fits the same number.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — what is being polarised, and the bulk conductivity that carries the current.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](../01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)
  — the mechanism behind most of the polarisation seen in the field.
- [09-02-03 Apparent Resistivity and Geometric Factors](../02-dc-resistivity/03-apparent-resistivity.md)
  — the geometric factor $K$ and the primary potential $V_p = I\rho K$.
- [01-10-02 The Fourier Transform and Its Properties](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md)
  — the transform used to move between the two domains.

**All models and data in this module are SYNTHETIC.** The resistivities,
chargeabilities, time constants, currents and noise levels below are chosen
teaching values, not measurements of any rock, sample, site or instrument.

---

## 1. Intuition: a polarisable ground answers a switched-off current slowly

Inject a steady current into the ground through two electrodes and measure the
potential difference across two others. If the ground behaved as a pure
resistor, the voltage would follow the current exactly: on with the current, off
with it. In real ground a part of the voltage **lingers** for a fraction of a
second to tens of seconds after the current is switched off. That lingering is
the induced-polarisation (IP) effect, and its size and its shape are the
measurement.

The physical mechanism is **charge blocking**. Somewhere in the current path a
charge carrier cannot pass freely: at a mineral grain whose conduction is
electronic while the surrounding electrolyte conducts ionically, or at a clay
particle whose surface charge layer holds one sign of ion preferentially. Charge
accumulates at that interface while the current flows, exactly as it does at the
plates of a capacitor. When the current is switched off, the accumulated charge
drains away through the same resistive path that stored it, which is why the
decay is not instantaneous and why it is *slow* on the time scale of the
resistance — the product $RC$ sets it.

Two consequences follow immediately and they organise this whole module:

1. The amplitude of the lingering voltage **relative to** the primary voltage is
   a small, dimensionless number (per cent to tens of per cent). This is why IP
   is always reported as a ratio, and why the units are awkward.
2. The *shape* of the decay in time and the *phase lag* under a harmonic current
   are two views of the same underlying relaxation. The exact correspondence
   between them is a model, not a definition. The two domains do not carry
   independent information, and this lesson measures how much of a conversion
   between them is truth and how much is convention.

## 2. Precise definitions

### 2.1 Primary and secondary voltage

Let $V_p$ be the potential difference at the measurement electrodes while a
steady current $I$ flows and the polarisation is fully charged — the *primary*
voltage. Immediately after switch-off, the residual voltage $V_s(t)$ falls from
$mV_p$ to zero, where $m$ is the **chargeability**, a dimensionless number:

$$m = \frac{V_s(t \to 0^{+})}{V_p} \times 1000 \quad
\text{reported in } \mathrm{mV\,V^{-1}}.$$

Here $1000\ \mathrm{mV\,V^{-1}}$ equals $1$ and is a convention, exactly as
millimetres per metre is. A chargeability of $20\ \mathrm{mV\,V^{-1}}$ means the
residual voltage is $2\%$ of the primary.

### 2.2 Integral and average chargeability

Two windows are in common use, and they differ by a factor $T$:

$$
M_{\text{int}}(T) = \frac{1}{V_p}\int_0^{T} V_s(t)\,\mathrm{d}t
\quad [\mathrm{s} \equiv \mathrm{ms}\ \text{per}\ 1\ \mathrm{s}],
\qquad
M_{\text{avg}}(T) = \frac{1}{T}M_{\text{int}}(T)
\quad [\text{dimensionless}].
$$

The equivalence $1\ \mathrm{ms} = 1\ \mathrm{mV\,V^{-1}}$ holds for
$M_{\text{int}}$ over a $1\ \mathrm{s}$ window: dividing a millivolt by a volt
gives $10^{-3}$, and multiplying by a second gives a millisecond. **A bare
number such as "chargeability 15" is therefore meaningless**; it needs the
convention, the window and the units. Every table in this lesson prints both.

### 2.3 Percent frequency effect and phase

In the frequency domain the same ground is measured with a harmonic current at
two or more frequencies. Two scalars are reported: the **percent frequency
effect**

$$\mathrm{PFE} = \frac{\rho(f_{\text{low}}) - \rho(f_{\text{high}})}
{\rho(f_{\text{high}})} \times 100\ \%,$$

and the **phase lag** of the measured voltage behind the current,
$\varphi = \arg\rho$, in milliradians (mrad) or degrees. A conductive,
polarisable ground has $\varphi < 0$: the voltage lags. We quote
$-\varphi > 0$ throughout, and say so.

### 2.4 The element that produces all of this

The simplest polarisable element is a resistor $R$ in series with a parallel
$RC$ combination — the Randles-type circuit. Its impedance, normalised to its DC
value, is

$$\frac{\rho(\omega)}{\rho_0} = (1-m) + \frac{m}{1 + i\omega\tau},
\qquad \tau = RC.$$

At $\omega \to 0$ this is $\rho_0$; at $\omega \to \infty$ it is
$\rho_0(1-m)$, so the same $m$ describes both the amplitude drop and the decay
amplitude. That is the **Debye**, or single-relaxation, model. It is the
reference against which every measured spectrum should first be plotted, and
[02 IP Models](02-ip-models.md) shows why real ground is never quite this.

## 3. Derivations

### 3.1 The step-off decay and the exact chargeability

With the current switched off at $t = 0$, the polarised element discharges
through its own resistance. The governing equation is a first-order relaxation:

$$\frac{\mathrm{d}V_s}{\mathrm{d}t} = -\frac{V_s}{\tau},
\qquad V_s(0) = mV_p
\;\Longrightarrow\;
\boxed{\;V_s(t) = mV_p\,e^{-t/\tau}\;}.$$

Integrating over the window $[0, T]$ and dividing by $V_p$:

$$M_{\text{int}}(T) = \int_0^{T} m\,e^{-t/\tau}\,\mathrm{d}t
= m\tau\left(1 - e^{-T/\tau}\right).$$

Two limits are worth memorising. For $T \ll \tau$, $M_{\text{int}} \to mT$: the
window sees a nearly constant decay and measures $m$ directly. For
$T \gg \tau$, $M_{\text{int}} \to m\tau$, the **total chargeability**, which is a
property of the element and not of the window. Between the two limits the
measured number is a mixture of $m$ and $\tau$, and no choice of window
separates them from one integral alone.

### 3.2 The phase and its exact maximum

Put $x = \omega\tau$. The normalised response of Section 2.4 becomes

$$\frac{\rho}{\rho_0} = \frac{1 + i x (1-m)}{1 + i x},$$

so the phase is the difference of two arctangents,

$$\varphi(x) = \arctan\!\left[x(1-m)\right] - \arctan(x) \le 0 .$$

The magnitude is largest where $\mathrm{d}\varphi/\mathrm{d}x = 0$:

$$\frac{1-m}{1 + (1-m)^2x^2} - \frac{1}{1+x^2} = 0
\;\Longrightarrow\;
x^2\left[(1-m) - (1-m)^2\right] = m
\;\Longrightarrow\;
x_{\max} = \frac{1}{\sqrt{1-m}} .$$

Substituting back and using $\tan(A-B) = (\tan A - \tan B)/(1 + \tan A\tan B)$:

$$\tan\left|\varphi_{\max}\right| = \frac{m}{2\sqrt{1-m}},
\qquad
\omega_{\max} = \frac{1}{\tau\sqrt{1-m}} .$$

**The single-relaxation model is fully determined by two numbers from the phase
spectrum**: the height of the phase peak gives $m$, and the frequency of that
peak gives $\tau$ (to within the factor $1/\sqrt{1-m}$). This is a strong,
falsifiable statement, and its failure on real data is the entire content of
[02 IP Models](02-ip-models.md).

### 3.3 From a transfer function to the decay, with no inverse-transform guesswork

Section 3.1 assumed an exponential decay. The demonstration computes it
*independently* from the frequency-domain transfer function, which is the same
calculation that lesson [09-05-01](../05-em-methods-applications/01-tem-sounding.md)
needs for transient EM. For an input that is $1$ for $t<0$ and $0$ for $t>0$
(a step-off), and a transfer function $G(\omega)$ with $G_0 = G(0)$,

$$y(t) = -\frac{1}{\pi}\int_0^{\infty}
\frac{\operatorname{Im}\left\{\left[G(\omega) - G_0\right]e^{i\omega t}\right\}}
{\omega}\,\mathrm{d}\omega .$$

For the Debye element, $G = V_p\left[(1-m) + m/(1+i\omega\tau)\right]$ and
$G_0 = V_p$, so $G - G_0 = -V_p\,m\,i\omega\tau/(1+i\omega\tau)$. Cauchy's
residue theorem gives
$\int_0^{\infty}\left[\cos(\omega t) + \omega\tau\sin(\omega t)\right]/(1+\omega^2\tau^2)\,\mathrm{d}\omega
= \frac{2}{\tau}\cdot\frac{\pi}{2}e^{-t/\tau}$, and the integral above reduces
to exactly $V_p m e^{-t/\tau}$ — Section 3.1 recovered, not assumed. The
demonstration verifies the numerical quadrature of this formula on a
single-pole system and finds agreement of $9.3\times10^{-8}$ of the DC gain.

### 3.4 A broad distribution of relaxations looks like a power law

Real ground is a mixture: a rock has grain sizes, pore throats and surface
chemistries, so it has a *distribution* of relaxation times rather than one.
Take $n$ relaxations with equal weights $w_k = 1/n$ log-uniformly spread over
$\left[\tau/n_\text{span}, \tau n_\text{span}\right]$:

$$\frac{\rho(\omega)}{\rho_0} = 1 - m + m\sum_{k} \frac{w_k}{1 + i\omega\tau_k}.$$

Over a band well inside the distribution the phase is nearly flat. The
*constant-phase-element* (CPE) statement is that a flat phase and a power-law
amplitude go together:

$$\left|\varphi\right| \approx \frac{\pi}{2}\,c,
\qquad
\left|\rho(\omega)\right| \propto \omega^{-c} .$$

The demonstration measures the two sides of that relation on a broadened model:
the amplitude slope $\mathrm{d}\log|\rho|/\mathrm{d}\log f = -0.0146$ and
$(2/\pi)$ times the mean phase $=0.0136$, an agreement to $7\%$. The residual
is the finite width of the distribution used ($30\times$ in $\tau$), and it
shrinks as the distribution widens. So the CPE exponent is not a statement
about a material; it is a statement about how wide a spread of time constants
the band can see.

## 4. Physical interpretation

- **$m$ is a ratio of two voltages, not a voltage.** Its units are per mille of
  the primary; it is independent of the injected current as long as the response
  is linear.
- **$\tau$ is a time constant of the polarisable *element*, weighted by the
  surrounding resistivity.** In the circuit picture, $\tau = RC$ where $C$ is an
  interfacial capacitance and $R$ is the discharge resistance, so a change in
  the bulk resistivity moves $\tau$ as well as $\rho_0$. Fitting a time constant
  and calling it a grain property is a category error unless the circuit is
  stated.
- **The measured chargeability is window-dependent.** For the synthetic model of
  the demonstration ($m = 0.10$, $\tau = 1.5$ s) the window integral in ms runs
  from $23.028$ at $T = 0.25$ s to $149.997$ at $T = 16$ s — a factor $6.5$ from
  the window alone, with the ground unchanged. The window-average in mV/V moves
  the other way, from $92.111$ down to $9.375$.
- **Slower polarisation needs a longer charging time.** If the current is on for
  only one time constant, the element is charged to
  $mV_p\left(1 - e^{-1}\right) = 0.632\,mV_p$, and the apparent chargeability in
  a $1$ s window is $51\%$ low. The effect is not noise and it is not drift; it
  is an incompletely charged capacitor.
- **Time domain and frequency domain are two functionals of one response.** They
  are related exactly only through a model. The demonstration's Debye model has
  $M_{\text{int}}(1\,\mathrm{s}) = 72.987$ ms and a $1$ Hz phase of
  $11.643$ mrad; a broadened model with the same nominal $m$ has
  $61.139$ ms and $19.950$ mrad. The phase ratio between the two models is
  $1.713$ while the chargeability ratio is $0.838$: *the two domains disagree
  about which model is bigger.*

## 5. Assumptions and regime of validity

1. **Linearity.** The response is assumed linear in the current, so $M$ and
   $\varphi$ are independent of $I$ and of the electrode geometry. Beyond linear
   response (high current density, heating) the model fails and the numbers move
   with the current.
2. **A single relaxation in the reference model.** Deliberately too simple; a
   measured two-relaxation truth fitted by one Debye shifts the apparent $\tau$
   by a factor $3.1$ and $m$ by $-18.9\%$ when the window set is changed
   (measured in [03 IP Acquisition](03-ip-acquisition.md)).
3. **No electromagnetic coupling.** At high frequencies (above roughly the
   kilohertz range, and sooner for conductive ground) the induction of the
   current in the ground adds a phase of its own. That coupling is not
   polarisation and must be removed before interpretation; this lesson's
   frequency range is chosen to stay below it.
4. **No drift, no telluric noise, no electrode polarisation.** All three are
   treated in [03](03-ip-acquisition.md); here they are absent by construction.
5. **A fully charged element before switch-off** unless stated otherwise.
6. **Isotropic, homogeneous polarisable medium** in the model. The field
   geometry enters only through $K$ and through the assumption that $V_p = I\rho K$.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| primary voltage | $V_p$ | V | $I[\mathrm{A}] \times \rho[\Omega\,\mathrm{m}] \times K[\mathrm{m}]$ |
| chargeability | $m$ | dimensionless (reported mV/V) | ratio of two voltages |
| time constant | $\tau$ | s | $RC$ |
| window integral | $M_{\text{int}}$ | s, reported ms | $\mathrm{s^{-1}}\times\mathrm{s}$ |
| window average | $M_{\text{avg}}$ | dimensionless | $M_{\text{int}}/T$ |
| phase | $\varphi$ | rad, reported mrad | argument of a complex ratio |
| ratio | $\mathrm{d}\log\lvert\rho\rvert / \mathrm{d}\log f$ | dimensionless | logs of quantities with the same units |

Two checks worth performing on every number you meet: (i) a chargeability
reported in mV/V must be numerically equal to $M_{\text{int}}$ in ms **only**
for a one-second window, and (ii) a phase in mrad and a chargeability in ms are
both $10^{-3}$ of their natural unit, which is why they are so often confused.
The confusion is a convention, not an identity — Section 3.2 and Section 3.4
together show that their ratio depends on the model.

## 7. Worked examples

### Example 1 — the window integral and its units

Synthetic target: $\rho_0 = 100\ \Omega\,\mathrm{m}$,
$m = 0.100$, $\tau = 1.500\ \mathrm{s}$, $I = 0.100\ \mathrm{A}$,
$K = 1.000\ \mathrm{m}$.

1. Primary voltage: $V_p = I\rho_0K = 0.100 \times 100 \times 1.000
   = 10.000$ V. This is what the demonstration prints.
2. Decay amplitude at $t = 0^{+}$: $mV_p = 0.100 \times 10.000 = 1.0000$ V.
3. Total chargeability: $m\tau = 0.100 \times 1.500 = 0.1500$ s
   $= 150.00$ ms — the $T \to \infty$ limit of the table.
4. For $T = 2.00$ s:
   $M_{\text{int}} = 0.100 \times 1.500 \times \left(1 - e^{-2.00/1.500}\right)
   = 0.1500 \times \left(1 - 0.263597\right) = 0.1500 \times 0.736403
   = 0.110460$ s $= 110.460$ ms.
5. The window average is $M_{\text{avg}} = 110.460/2.00 = 55.230$ mV/V.

Both $110.460$ ms and $55.230$ mV/V are printed by the demonstration for
$T = 2.00$ s. They describe the same ground and the same decay; the difference
is the convention.

### Example 2 — peak phase and peak frequency, verified

Same element, $m = 0.100$:

$$\tan\left|\varphi_{\max}\right| = \frac{0.100}{2\sqrt{0.900}}
= \frac{0.100}{1.897367} = 0.0527046
\;\Longrightarrow\;
\left|\varphi_{\max}\right| = 0.0526560\ \mathrm{rad} = 52.656\ \mathrm{mrad},$$

$$f_{\max} = \frac{1}{2\pi\tau\sqrt{1-m}}
= \frac{1}{2\pi \times 1.500 \times 0.948683} = 0.111843\ \mathrm{Hz}.$$

The demonstration's numerical search over $200001$ frequencies returns
$52.6559$ mrad at $0.111841$ Hz: a phase agreement of $0.0000$ mrad and a
frequency agreement of $2.0\times10^{-6}$ Hz, the latter being the grid
spacing. Inverting the formulae, $\tau$ recovered from $f_{\max}$ is
$1/(2\pi \times 0.111843 \times 0.948683) = 1.500\ \mathrm{s}$, and $m$
recovered from the peak height is the root of
$\tan\left|\varphi_{\max}\right| = m/(2\sqrt{1-m})$.

### Example 3 — the cost of a short charging time

Suppose the transmitter can only stay on for one second — $t_{\text{on}} =
1.000$ s, which is $0.667\,\tau$ — and the decay is then integrated over
$T = 1.000$ s:

$$M_{\text{int}} = m\tau\left(1 - e^{-t_{\text{on}}/\tau}\right)
\left(1 - e^{-T/\tau}\right)
= 0.1500 \times \left(1 - e^{-0.666667}\right)
\times \left(1 - e^{-0.666667}\right)
= 0.1500 \times 0.486583 \times 0.486583
= 0.035514\ \mathrm{s} = 35.514\ \mathrm{ms}.$$

Two factors of the same form, each $0.4866$: one from the incomplete charging
and one from the finite window. The fully charged, full-window value is
$72.987$ ms, so the apparent chargeability is $48.7\%$ of it — a $-51.3\%$
bias, which is exactly what the demonstration's charging-time table reports for
$t_{\text{on}} = 1.00$ s ($35.514$ ms against $72.987$ ms). Note that the
charging penalty is set by $t_{\text{on}}/\tau$, not by $t_{\text{on}}$: one
second is *below* one time constant here, and an on-time of $8.00$ s recovers
$72.635$ ms, still $0.5\%$ short. The lesson's point is that the bias is large,
systematic and computable, so it must be corrected rather than absorbed into an
error bar.

## 8. Python demonstration

`code/ip_principle_demo.py` performs the whole calculation and prints labelled
results with units. It:

1. prints the model, the primary voltage, the decay amplitude and the total
   chargeability;
2. tabulates $M_{\text{int}}$ and $M_{\text{avg}}$ against the window and checks
   the closed form against numerical quadrature ($23.028$ to $149.997$ ms; the
   two agree to the printed digits);
3. prints the phase and amplitude spectra, and compares the numerical phase peak
   with the closed forms of Section 3.2;
4. puts the Debye and a broadened model side by side in both domains, giving the
   conversion-factor spread quoted in Section 4;
5. measures the constant-phase relation of Section 3.4 (slope $-0.0146$ against
   $(2/\pi)$ mean phase $0.0136$, $7\%$ apart);
6. quantifies the charging-time bias (six on-times) and the drift bias (a linear
   drift of $10.0$ mV/s adds $+0.500$ ms to a $72.987$ ms chargeability);
7. verifies the step-off formula of Section 3.3 against the analytic exponential
   ($9.3\times10^{-8}$ of the DC gain).

Files:
[`code/ip_principle_demo.py`](./code/ip_principle_demo.py).

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-ip-principle-exercises.md`](./exercises/01-ip-principle-exercises.md)
and
[`exercises/01-ip-principle-solutions.md`](./exercises/01-ip-principle-solutions.md).

- **★** Compute $M_{\text{int}}$ for $m = 0.08$, $\tau = 0.90$ s and windows of
  0.5, 1 and 4 s; report both conventions.
- **★★** Derive $\tan\lvert\varphi_{\max}\rvert$ from scratch and evaluate it for
  $m = 0.25$; state the peak frequency for $\tau = 0.4$ s.
- **★★** Show that the ratio $M_{\text{int}}(T)/M_{\text{int}}(\infty)$ depends
  only on $T/\tau$, and use it to explain why a window change of a factor 4
  cannot be mistaken for a change in $m$.
- **★★★** Reproduce the constant-phase measurement: build a log-uniform
  distribution of $N$ relaxations and measure how the phase flatness and the
  amplitude slope converge as $N$ and the width increase.

## 10. Common mistakes

1. **Quoting a chargeability without its window and convention.** $M_{\text{int}}$
   in ms and $M_{\text{avg}}$ in mV/V differ by the factor $T$; a number without
   either is not a measurement.
2. **Treating mV/V and ms as always interchangeable.** They coincide only for a
   one-second integral window.
3. **Reading a phase in mrad as a chargeability in ms.** They have the same
   scale factor $10^{-3}$ and different physical meanings; the ratio of one to
   the other ranged over a factor $12$ across the synthetic models measured in
   [03](03-ip-acquisition.md).
4. **Choosing the window by habit rather than from $\tau$.** A window much
   shorter than $\tau$ measures $mT$; much longer, it measures $m\tau$; in
   between it measures a mixture.
5. **Ignoring the charging time.** An on-time comparable to $\tau$ costs tens of
   per cent of the apparent chargeability.
6. **Assuming a single relaxation.** A single Debye fit to a two-relaxation
   response is precise and wrong — Section 4's $1.713$ against $0.838$.
7. **Reporting the phase without its sign convention.** Some authors report the
   lag, some the lead, and both are positive numbers in print.

## 11. Real-world applications

- **Mineral exploration.** Sulphide bodies polarise because their conduction is
  electronic while the electrolyte is ionic; IP is the classical discrimination
  between a conductive *mineral* and a conductive *electrolyte*, neither of which
  a resistivity survey can separate.
- **Groundwater and contamination.** Surface (membrane) polarisation of clays
  makes IP sensitive to clay content and to the salinity of the pore fluid,
  which is why IP accompanies resistivity in aquifer and leachate surveys.
- **Geotechnical and permafrost work.** Frozen ground is resistive; whether it
  is *also* polarised depends on the unfrozen water films, which is a
  measurement rather than a prediction.
- **Monitoring.** Because $m$ and $\varphi$ are ratios, they are less sensitive
  to electrode contact changes between surveys than a raw voltage, which is what
  makes repeated IP usable for time-lapse work.

## 12. Further reading

- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*
  (2nd ed., Cambridge University Press).** Level: textbook. Chapter 5 covers the
  electrode arrays, the geometric factor and the IP measurement as a whole.
- **Reynolds, J. M., *An Introduction to Applied and Environmental
  Geophysics* (2nd ed., Wiley-Blackwell).** Level: textbook. Broad, practical
  treatment of time-domain and frequency-domain IP and of the field procedures.
- **Ward, S. H. (ed.), *Geotechnical and Environmental Geophysics* (SEG
  Investigations in Geophysics series).** Level: research review. Useful for the
  survey-design and case-history side.
- **Sumner, J. S., *Principles of Induced Polarization for Geophysical
  Exploration* (Elsevier).** Level: research monograph. The standard reference
  for the history and the conventions, including the units debate of Section 2.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. No number in this lesson is
> quoted from any of them: every figure is printed by the demonstration in
> [`code/ip_principle_demo.py`](./code/ip_principle_demo.py) or is an exact
> standard constant ($1\ \mathrm{ms} = 10^{-3}\ \mathrm{s}$; nothing else).

## 13. Related lessons

- [02 IP Models: Cole-Cole, Debye, Constant-Phase Element](02-ip-models.md) —
  what the single relaxation of this lesson becomes when the distribution is
  real.
- [03 IP Acquisition, Chargeability and Phase Units](03-ip-acquisition.md) —
  how the window, the noise and the model family bound the answer.
- [04 IP for Sulphides, Clays, Contaminants and Permafrost](04-ip-applications.md) —
  the pathway split that decides what a phase means in the ground.
- [09-05-01 TEM Sounding](../05-em-methods-applications/01-tem-sounding.md) —
  the same step-off transform used for the transient electromagnetic response.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](../01-electrical-properties-of-earth/04-clay-and-surface-conduction.md) —
  the mechanism behind $m$ and $\tau$.

## 14. Self-assessment checklist

- [ ] I can write both chargeability conventions and state the unit of each.
- [ ] I can derive $M_{\text{int}}(T) = m\tau(1-e^{-T/\tau})$ and its two limits.
- [ ] I can derive $x_{\max} = 1/\sqrt{1-m}$ and
      $\tan\lvert\varphi_{\max}\rvert = m/(2\sqrt{1-m})$.
- [ ] I can compute the step-off response from a transfer function.
- [ ] I can estimate the bias from a charging time shorter than $\tau$.
- [ ] I can explain why a broad distribution of $\tau$ gives a flat phase and a
      power-law amplitude.
- [ ] I can state, with the measured numbers, why the two domains are not
      interchangeable.
