# Solutions — 01-11-06 Dispersion Relations and Causality in Wave Physics

> **Read this after attempting the exercises, not before.**
>
> Every sign below belongs to the $e^{-i\omega t}$ convention, stated once here
> and assumed throughout. Where a residual is quoted, it is the value printed by
> the companion script in
> [`../code/`](../code/dispersion_causality_demo.py).

---

## ★1 — The relation and the convention

**(a)** Whole-line form:

$$\operatorname{Re}H(\omega) = -\frac{1}{\pi}\,\mathrm{P.V.}
\int_{-\infty}^{\infty}\frac{\operatorname{Im}H(\omega')}{\omega'-\omega}
\,\mathrm{d}\omega',$$

and folded onto positive frequencies (valid because $\operatorname{Im}H$ is odd):

$$\operatorname{Re}H(\omega) = -\frac{2}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\omega'\operatorname{Im}H(\omega')}
{\omega'^{2}-\omega^{2}}\,\mathrm{d}\omega' .$$

**(b)** $H$ is analytic in the **lower** half plane. Derivation in three lines:
write $H(\omega) = \int_{0}^{\infty}h(t)e^{-i\omega t}\mathrm{d}t$ with
$\omega = \omega_{r}+i\omega_{i}$; the integrand carries
$|e^{-i\omega t}| = e^{\omega_{i}t}$, which *decays* for $\omega_{i}<0$; so the
integral converges and is differentiable in $\omega$ throughout
$\operatorname{Im}\omega < 0$.

**(c)** The paper is using the opposite convention, $e^{+i\omega t}$, in which
$H$ is analytic in the **upper** half plane and the closure is taken there, which
flips the overall sign. The first thing to check is the paper's stated
time dependence — not the sign of the relation, which is a consequence, and not
the sign of an imaginary part, which is a convention.

---

## ★2 — Causality of four responses

**(a) $H = 1/(1+i\omega\tau)$, $\tau>0$.** This is the transform of
$(1/\tau)e^{-t/\tau}u(t)$ (computed in
[lesson 04](./04-laplace-transform-solutions.md) for the analogue pair). **Causal.**
Singularity: a simple pole at $\omega = i/\tau$, in the **upper** half plane, so
the lower half plane — the analyticity region — is free of singularities. ✓

**(b) $H = 1/(1-i\omega\tau)$.** The pole is at $\omega = -i/\tau$, in the
**lower** half plane, which is exactly the region where $H$ must be analytic. It
is therefore **not the transfer function of a causal system**; its time-domain
partner is $(1/\tau)e^{t/\tau}u(-t)$, which is non-zero only for $t<0$.

**(c) $H = e^{-a\omega^{2}}$, $a>0$.** There are no singularities at all: $H$ is
entire, so it is trivially analytic in the lower half plane. But analyticity is
only *necessary*. Two further checks are needed, and this response fails one of
them. Its inverse transform is

$$h(t) = \frac{1}{2\sqrt{\pi a}}e^{-t^{2}/(4a)},$$

a Gaussian in $t$ centred on $t=0$, which is **non-zero for every $t<0$**: the
system responds before it is driven, so it is **not causal**. Equivalently, check
the decay condition inside the half plane:
$|e^{-a\omega^{2}}| = e^{a\omega_{i}^{2}}e^{-a\omega_{r}^{2}}$ **grows** with
$|\operatorname{Im}\omega|$, so the arc in the lower half plane does not vanish and
the closure argument behind the Kramers–Kronig relation fails. The lesson is
general: analyticity of $H$ in the lower half plane must be accompanied by decay
there as $|\omega|\to\infty$, and by one-sidedness of the impulse response; the
three conditions together are causality.

**(d) $H = e^{i\omega t_{0}}$, $t_{0}>0$.** $|H| = 1$ everywhere: the decay
condition fails, and the inverse transform is $\delta(t+t_{0})$ — an **impulse at
$t = -t_{0}<0$**, i.e. a response that anticipates the input by $t_{0}$. **Not
causal.** (For $t_{0}<0$ it is a pure delay — the only causal possibility with
unit gain at all frequencies.)

---

## ★3 — Recovering the real part by Kramers–Kronig

**(a)** $\operatorname{Im}M(\omega) = -\Delta M\,\omega\tau/(1+\omega^{2}\tau^{2})$
behaves as $-\Delta M\omega\tau$ at low frequency (vanishing, as a passive
response must) and as $-\Delta M/(\omega\tau)$ at high frequency (decaying to
zero). Both are consistent with the statement that
$\Delta M'(\omega) \equiv M(\omega)-M_{U}$ is a response function that vanishes
at infinity on both counts, which is what the subtracted relation requires.

**(b)** Using the modulus form (Section 3.4 of the lesson), with
$\operatorname{Im}\Delta M = \operatorname{Im}M$,

$$\operatorname{Re}M(\omega)-M_{U} = \frac{2}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\omega'\operatorname{Im}M(\omega')}
{\omega'^{2}-\omega^{2}}\,\mathrm{d}\omega'
= -\frac{2\Delta M\tau}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\omega'^{2}}
{(1+\omega'^{2}\tau^{2})(\omega'^{2}-\omega^{2})}\,\mathrm{d}\omega' .$$

The partial fractions are exactly those of
[lesson 03](./03-contour-integration-solutions.md) ★★★9:
$A = 1/(1+\omega^{2}\tau^{2})$ multiplying $1/(1+\omega'^{2}\tau^{2})$ and
$B = \omega^{2}/(1+\omega^{2}\tau^{2})$ multiplying
$1/(\omega'^{2}-\omega^{2})$, whose principal value integrates to zero. So

$$\operatorname{Re}M(\omega) = M_{U} -
\frac{2\Delta M\tau}{\pi}\cdot\frac{1}{1+\omega^{2}\tau^{2}}
\cdot\frac{\pi}{2\tau}
= M_{U} - \frac{\Delta M}{1+\omega^{2}\tau^{2}} .$$

**(c)** At $\omega\tau = 1$: $M_{U} - \Delta M/2$, i.e. exactly the midpoint
between the unrelaxed and relaxed moduli. Direct evaluation of
$M = M_{R} + \Delta M\,i\omega\tau/(1+i\omega\tau)$ at $\omega\tau=1$ gives
$\operatorname{Re}M = M_{R}+\Delta M/2$, and since $M_{U} = M_{R}+\Delta M$ the
two agree ✓. The physically important reading:
$\operatorname{Re}M$ **decreases** from $M_{U}$ at high frequency to $M_{R}$ at
low frequency as $\omega$ increases — that is, the dispersion is *normal*
(stiffer at higher frequency), and it is forced by the attenuation through the
relation that was just integrated.

---

## ★4 — Energy from the hysteresis loop

**(a)** With $\sigma = \sigma_{0}\cos(\omega t-\phi)$ and
$\varepsilon = \varepsilon_{0}\cos\omega t$,
$M = \sigma_{0}e^{-i\phi}/\varepsilon_{0}$, so

$$M = \frac{\sigma_{0}}{\varepsilon_{0}}(\cos\phi - i\sin\phi)
= 40\ \mathrm{MPa}\times(0.866025 - 0.500000i)
= (3.464102 - 2.000000)\times10^{7}\ \mathrm{Pa}.$$

**(b)** The loop area is

$$W = \oint\sigma\,\mathrm{d}\varepsilon
= \pi\varepsilon_{0}^{2}|M|\sin\phi$$

(obtained by carrying $\sigma_{0}\cos(\omega t-\phi)$ and
$\varepsilon = \varepsilon_{0}\cos\omega t$ through
$\int_{0}^{T}\sigma\dot\varepsilon\,\mathrm{d}t$; equivalently
$W = -\pi\varepsilon_{0}^{2}\operatorname{Im}M$ with the sign of $\phi$
convention). Numerically,

$$W = \pi(5\times10^{-4})^{2}(2\times10^{7})\sin 30^{\circ}
= \pi\,(2.5\times10^{-7})(10^{7})
= \pi(2.5) = 7.853982\ \mathrm{J\,m^{-3}} .$$

**(c)** $\operatorname{Im}M<0$ (the value above is $-2.0\times10^{7}$ Pa), and
$W = -\pi\varepsilon_{0}^{2}\operatorname{Im}M =
\pi(2.5\times10^{-7})(2.0\times10^{7}) = 7.854$ ✓ positive. Both signs are
consistent, and that is the point: **the sign of $\operatorname{Im}M$ is not a
matter of taste, it is fixed by requiring the material to absorb energy.**

---

## ★★5 — A standard linear solid

**(a)** $M_{U}/M_{R} = \tau_{\varepsilon}/\tau_{\sigma} = 1.0/0.25 = 4$, so
$\rho = 4$ and $M_{U} = 40$ GPa. The relaxed modulus is $M_{R} = 10$ GPa and the
unrelaxed modulus is $M_{U} = 40$ GPa.

**(b)** The loss peaks at

$$\omega_{\max} = \frac{1}{\sqrt{\tau_{\varepsilon}\tau_{\sigma}}}
= \frac{1}{\sqrt{0.25}} = 2\ \mathrm{rad\,s^{-1}}
\qquad (f = 0.318\ \mathrm{Hz}),$$

with

$$\frac{1}{Q_{\max}} = \frac{M_{U}-M_{R}}{2\sqrt{M_{R}M_{U}}}
= \frac{\rho-1}{2\sqrt\rho} = \frac{3}{4} = 0.75 .$$

Both formulae were confirmed numerically for $\rho = 2$ in the lesson
($1/Q_{\max} = 0.353553391$ against a measured $0.353553387$). The dependence:
$\omega_{\max}$ is the geometric mean of the two relaxation rates, and
$1/Q_{\max}\to0$ both as $\rho\to1$ (no relaxation) and as
$\rho\to0$ (unphysical); it is largest for large contrast.

**(c)** With $\rho = M_{U}/M_{R} = 4$ and $\rho_{\text{mass}} = 2600$:

$$v_{\text{low}} = \sqrt{\frac{M_{R}}{\rho_{\text{mass}}}}
= \sqrt{\frac{10\times10^{9}}{2600}} = 1961.16\ \mathrm{m\,s^{-1}},$$

$$v_{\text{high}} = \sqrt{\frac{M_{U}}{\rho_{\text{mass}}}}
= \sqrt{\frac{40\times10^{9}}{2600}} = 3922.32\ \mathrm{m\,s^{-1}} .$$

The ratio is exactly $\sqrt{4} = 2$: **a factor of two in velocity over the
relaxation.** This is a large dispersion, and it is the price of a large $1/Q$;
the two are locked together by the Kramers–Kronig relation.

**(d)** The loss of a single relaxation is
$1/Q(\omega) = \omega(\tau_{\varepsilon}-\tau_{\sigma})/
(1+\omega^{2}\tau_{\varepsilon}\tau_{\sigma})$, which is $\propto\omega$ below the
peak and $\propto1/\omega$ above it. It has a *single* maximum and a
half-maximum width of about $1.1$ decades. A $Q$ constant to within, say, $\pm20\%$
over a decade is simply impossible with one relaxation — the loss falls off as
$1/(\omega\tau)$ in the tail. Constant $Q$ over a band requires a *distribution*
of relaxation times whose spread covers that band, which is what the
near-constant-$Q$ models construct.

---

## ★★6 — A laboratory measurement

**(a)** $|M| = \sigma_{0}/\varepsilon_{0} = 30\ \mathrm{MPa}/10^{-3}
= 3.0\times10^{10}$ Pa. Then

$$\operatorname{Re}M = |M|\cos\phi = 3.0\times10^{10}\times0.999800
= 2.999400\times10^{10}\ \mathrm{Pa},$$

$$\operatorname{Im}M = -|M|\sin\phi = -3.0\times10^{10}\times0.019999
= -5.99960\times10^{8}\ \mathrm{Pa},$$

with $\operatorname{Im}M<0$ because the material is dissipative in this
convention.

**(b)**

$$W = \pi\varepsilon_{0}^{2}\operatorname{Re}M\tan\phi
= \pi(10^{-6})(2.999400\times10^{10})(0.020003)
= 1.885\times10^{3}\ \mathrm{J\,m^{-3}},$$

and

$$\pi\varepsilon_{0}^{2}|M|\sin\phi = \pi(10^{-6})(3.0\times10^{10})(0.019999)
= 1.885\times10^{3}\ \mathrm{J\,m^{-3}} \ \checkmark$$

The two agree to five figures; the identity is exact because
$\operatorname{Re}M\tan\phi = \operatorname{Re}M\cdot
\operatorname{Im}M/\operatorname{Re}M = \operatorname{Im}M$ in magnitude.

**(c)** $1/Q = \tan\phi = 0.020003 \approx 0.02$, so $Q\approx50$. With
$\omega = 2\pi\times10 = 62.831853$ rad s⁻¹ and $v = 3500\ \mathrm{m\,s^{-1}}$:

$$\alpha = \frac{\omega}{2vQ} = \frac{62.831853}{2\times3500\times50}
= 1.795196\times10^{-4}\ \mathrm{m^{-1}} .$$

**(d)** The amplitude decays as $e^{-\alpha x}$, so the $1/e$ distance is
$1/\alpha = 5570.4$ m. Over a 557 m path (a tenth of that) the amplitude loses
$10\%$; the measurement of such a loss requires amplitude accuracy of better than
$1\%$ after correcting for geometric spreading — and this is precisely why
laboratory $Q$ measurements are hard, and why seismologists prefer to measure $Q$
from *ratios* of amplitudes within a single record.

---

## ★★7 — A real, frequency-dependent, non-causal model

**(a)** **Not causal.** Write $H = 0.7 + 0.3/(1+\omega^{2}\tau^{2})$: the constant
contributes nothing to the principal-value integral (as
$\mathrm{P.V.}\int_{0}^{\infty}\mathrm{d}\omega'/(\omega'^{2}-\omega^{2}) = 0$),
and the rest gives

$$\operatorname{Im}H(\omega) = \frac{2\omega}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{0.3}{(1+\omega'^{2}\tau^{2})(\omega'^{2}-\omega^{2})}
\,\mathrm{d}\omega' .$$

Partial fractions give $A = -\tau^{2}/(1+\omega^{2}\tau^{2})$ for the term
$1/(1+\omega'^{2}\tau^{2})$ (the other term again integrates to zero under the
principal value), and $\int_{0}^{\infty}\mathrm{d}\omega'/(1+\omega'^{2}\tau^{2})
= \pi/(2\tau)$, so

$$\operatorname{Im}H(\omega) = -0.3\,\frac{\omega\tau}{1+\omega^{2}\tau^{2}},
\qquad\text{and at }\omega\tau = 1: \quad \operatorname{Im}H = -0.15 .$$

The assumed value was zero, so the conflict is $0.15$ — half the size of the
largest value the model's own real part takes. The implied imaginary part is
exactly that of the causal response $H = 0.7 + 0.3/(1+i\omega\tau)$.

**(b)** The causal completion has an impulse response

$$h(t) = 0.7\,\delta(t) + \frac{0.3}{\tau}e^{-t/\tau}u(t),$$

which is zero for $t<0$. The proposed model, being real-only and even in
$\omega$, has the inverse

$$h_{\text{bad}}(t) = 0.7\,\delta(t) + \frac{0.15}{\tau}e^{-|t|/\tau},$$

**non-zero for every $t<0$**: the material would begin responding to a strain
applied in the future. Symmetric-in-frequency implies symmetric-in-time, and
symmetry in time is the definition of anticipatory.

**(c)** Measure the response to a step or an impulse and look at the amplitude
*before* the input arrives. Any repeatable signal above the noise floor at
$t<0$ falsifies causality directly, with no dispersion relation needed. In
practice the decisive version is a propagation experiment: send a pulse through a
long sample and check that no energy arrives earlier than the light-travel (or
wave-speed) time across the sample.

**(d)** A **static** modulus is a single number, i.e. the zero-frequency limit
$H(0) = 1$ here, and a constant real response $H\equiv$ const is causal (its
impulse response is $c\delta(t)$ — instantaneous, which is the idealisation that
"static modulus" makes). The model becomes non-causal only when it is used
*away* from $\omega = 0$, i.e. whenever its frequency dependence is used to
predict a response at finite frequency. So the model is acceptable as a label for
a measured zero-frequency stiffness and unacceptable as a dynamical model — which
is a statement about how the number is used, and it should be stated explicitly
in any paper that quotes a "modulus" with a frequency dependence.

---

## ★★8 — Convergence of the log-amplitude relation

**(a)** The residual falls from $7.9\times10^{-5}$ to $7.2\times10^{-6}$ when the
node count rises from $10^{5}$ to $10^{6}$ — a factor of about $11$ for a factor
of $10$ in nodes. That is **first-order** convergence in the node spacing,
$O(h)$, not the fourth-order behaviour of Simpson's rule on a smooth integrand.

**(b)** The mechanism is the behaviour of $\ln|H|$ at large argument. For the
Debye response $\ln|H| = -\tfrac12\ln(1+\omega^{2}\tau^{2})
\sim -\ln(\omega\tau)$. Under the substitution $\omega' = \tan u$ the transformed
integrand contains $-\ln(\cot u)$, which **diverges logarithmically** as
$u\to\pi/2$: a logarithmic endpoint singularity. Simpson's rule on a function with
a $\ln$-type endpoint singularity converges as $O(h|\ln h|)$, i.e. very close to
$O(h)$.

**(c)** To reach $10^{-8}$ from $7.2\times10^{-6}$ requires a further factor of
about $700$ in the residual, hence roughly $700\times10^{6} \approx 7\times10^{8}$
nodes. That is not a practical quadrature. The relation is nevertheless useful —
it is the basis of phase estimation from an amplitude spectrum — because in
practice one does not evaluate the divergent integral directly: one uses the
*Hilbert transform* of the log-spectrum on a **finite, tapered** support, whose
truncation error is the price paid instead. The lesson is that the singularity,
not the algorithm, sets the convergence, and the remedy is a change of formulation
(truncation, tapering, or a parametric model) rather than more nodes.

**(d)** The conjugate relation integrates $\operatorname{Im}H(\omega')/
(\omega'^{2}-\omega^{2})$, where $\operatorname{Im}H\sim-1/(\omega'\tau)$ gives a
$1/\omega'^{3}$ integrand: absolutely convergent, smooth after the subtraction,
and spectrally accurate with the $\tan$ substitution. That is why the same code
reaches $10^{-12}$ there. The contrast between $10^{-12}$ and $10^{-5}$ is
therefore a statement about the two integrands, and it is the reason the
log-amplitude relation must be handled differently from the conjugate one in any
numerical implementation.

---

## ★★★9 — Dispersion from a single relaxation at $1/Q_{\max} = 0.01$

**(a)** Solve $1/Q_{\max} = (\rho-1)/(2\sqrt\rho) = 0.01$ for $\rho$: with
$s = \sqrt\rho$, $s^{2}-0.02s-1 = 0$, so
$s = (0.02+\sqrt{4.0004})/2 = 1.010050$ and

$$\rho = \frac{M_{U}}{M_{R}} = 1.020201, \qquad
\frac{v(\infty)}{v(0)} = \sqrt{\rho} = 1.010050 .$$

The **total** dispersion across the whole relaxation is $1.005\%$ — for a
low-loss rock, about one per cent, which is small but not negligible: it is of the
same order as a typical velocity-model uncertainty, and it is systematic rather
than random.

**(b)** Normalise $\tau_{\sigma} = 1$, so $\tau_{\varepsilon} = \rho = 1.020201$
and the loss peaks at $\omega_{\max} = 1/\sqrt{\tau_{\varepsilon}\tau_{\sigma}}
= 0.990050$. Evaluating $v(\omega) = 1/\operatorname{Re}\sqrt{1/M(\omega)}$ with
$M = (1-i\omega\tau_{\varepsilon})/(1-i\omega\tau_{\sigma})$:

| $\omega\tau_{\sigma}$ | $v$ | $1/Q$ |
|---|---|---|
| 0.10 | 1.0001014996 | 0.002000 |
| 1.00 | 1.0050752453 | 0.010000 |
| 10.00 | 1.0099524402 | 0.001961 |
| 100.00 | 1.0100490137 | 0.000198 |
| 1000.00 | 1.0100499889 | 0.000020 |

So the change from $\omega\tau_{\sigma} = 1$ to $100$ is
$(1.0100490137-1.0050752453)/1.0050752453 = 0.495\%$ — **half the total** — and
the remainder lies mostly *below* $\omega\tau_{\sigma} = 1$. The tail beyond
$\omega\tau_{\sigma} = 100$ adds $0.0001\%$.

**The assumption** in this scaling is the shape of the loss curve: the dispersion
accumulates where $1/Q$ is largest, so a two-decade band placed "two decades away"
from a one-decade-wide peak sees only the tail, and its own dispersion follows the
tail's $1/\omega$ behaviour rather than a logarithm.

**(c)** The logarithmic law with $Q = 100$ over two decades gives

$$\frac{\Delta v}{v} = \frac{1}{\pi Q}\ln(100)
= \frac{4.605170}{314.159265} = 1.4659\% .$$

That is **larger than the single relaxation's total dispersion** ($1.005\%$) and
about **three times** the change across the band computed in (b) ($0.495\%$). The
discrepancy is not an error: the log law assumes $1/Q = 0.01$ *uniformly across
the band*, whereas the single relaxation's $1/Q$ has fallen to $1.98\times10^{-4}$
by the top of the band — a factor of about 50 below the law's assumption. Since
the dispersion is the integral of the loss weighted by $1/(\omega'^{2}-\omega^{2})$,
a model with much less loss over most of the band must have much less dispersion.

**(d)** Both numbers are properties of *models*, and neither is a property of the
Earth. The Kramers–Kronig relation is exact and tells us that dispersion follows
from attenuation, but it does not fix the *magnitude*: that depends on how
$1/Q$ is distributed in frequency, which is a physical question about relaxation
mechanisms. To settle it you need a measurement of $Q(\omega)$ **and** $v(\omega)$
over the same band on the same material — for instance laboratory forced-oscillation
measurements on a rock sample over several decades, or a field experiment with an
independent velocity estimate (a travel-time or a waveform-inversion estimate) at
more than one frequency band. Quoting a dispersion from a $Q$ value alone is
exactly the step that this exercise shows to be unsafe.

---

## ★★★10 — Testing measured data for causality

**(a) Procedure.** Fit a parametric causal model to $\ln|H|$ (for the
log-amplitude relation) or to $\operatorname{Re}H$ (for the conjugate relation) —
a sum of Debye terms, or a spline in $\ln\omega$ with a stated tail behaviour. Then

1. evaluate the principal value numerically by **subtracting the singularity**, so
   the integrand is finite at $\omega' = \omega$, and integrating with the
   substitution $\omega' = \tan u$ (or a logarithmic substitution if the data span
   only a band);
2. extend the fitted model *beyond* the measured band to both the low- and the
   high-frequency limits (this is unavoidable — the relation is an integral over
   all frequencies) and report the sensitivity of the answer to that extension;
3. compare the predicted $\operatorname{Im}H$ (or $\arg H$) with the measured one
   frequency by frequency, and form the residuals.

**(b) Diagnostic.** The residual at each frequency,
$\Delta_{k} = \operatorname{Im}H_{\text{measured}}(\omega_{k}) -
\operatorname{Im}H_{\text{predicted}}(\omega_{k})$, normalised by its propagated
uncertainty $\sigma_{k}$. Under the null hypothesis (the data are causal and the
noise Gaussian), each $\Delta_{k}/\sigma_{k}$ is standard normal and their sum of
squares $\chi^{2} = \sum_{k}(\Delta_{k}/\sigma_{k})^{2}$ has a $\chi^{2}$
distribution with degrees of freedom equal to the number of frequency points minus
the number of fitted model parameters. A value far in the upper tail is evidence
against the causal model; the *pattern* of the residuals (a systematic drift, a
ramp at the band edges) is often more informative than the $\chi^{2}$ itself.

**(c) False alarms.**

1. **Band truncation.** The relation integrates over all frequencies, but data
   exist only over two decades; whatever happens outside contributes to the
   predicted value and is unconstrained. Control: extend the model with explicit
   tails, and repeat the test with two or three different tail assumptions; report
   how much the conclusion moves. If it moves, the test has not decided anything.
2. **Noise correlated between amplitude and phase**, or non-Gaussian outliers.
   Amplitude and phase are often estimated from the same transform, so their
   errors are correlated; and heavy-tailed noise inflates $\chi^{2}$ without any
   failure of causality. Control: estimate the covariance from repeated or
   segment-averaged measurements and use the full covariance in the statistic, or
   use a bootstrap/permutation distribution of the residuals instead of a nominal
   $\chi^{2}$.

A third, commoner in practice: the log-amplitude relation requires *minimum
phase*, which is violated if the system has zeros in the lower half plane
(a non-minimum-phase sensor, a time-reversed or delayed record). Control: state
the minimum-phase assumption with the test, and use the conjugate (non-log)
relation if it is in doubt.

**(d) Three most likely explanations**, in order:

1. **The integral is band-limited and the band edges are not negligible.** The
   measured band ends where the integrand is still appreciable, so refining the
   quadrature reveals the missing-data contribution rather than convergence. The
   signature is a residual that *decreases* with refinement up to a floor set by
   the band, and then stops.
2. **A logarithmic endpoint singularity in the quadrature**, if the
   log-amplitude relation was used (Section ★★8). The signature is a residual
   falling only as the node spacing, which can look like non-convergence.
3. **The model or the data are genuinely non-causal / inconsistent** — a wrong
   sign convention, a timing error (a record shifted by a whole sample), a
   sensor-phase correction applied twice, or a real physical inconsistency
   (for example a noisy estimate of the imaginary part at low frequency, where
   the integrand is largest).

The diagnostic order matters: check the convention, then the timing, then the
band, and only then conclude that causality is violated. A non-causal *appearance*
is almost always one of the first three.

---

## Self-assessment: have you actually learned this?

You can, without notes:

- state the convention, derive the analyticity region, and write the
  Kramers–Kronig relations in both forms with the correct signs;
- say why analyticity alone is not sufficient for causality (a Gaussian
  counterexample) and what the missing condition is;
- evaluate a principal value by subtracting the singularity and say why that is
  legitimate;
- derive the sign of $\operatorname{Im}M$ for a dissipative medium from the
  hysteresis loop;
- explain why a frequency-dependent real response is non-causal, by two
  independent routes;
- give the log-amplitude/phase relation, its minimum-phase hypothesis, and its
  slow convergence mechanism;
- state the total dispersion of a single relaxation in terms of the moduli, and
  explain why the near-constant-$Q$ log law is a different (and stronger)
  assumption;
- describe how to test measured data for causality and how the test can fail.
