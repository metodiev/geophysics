# Solutions — 09-03-02 IP Models: Cole-Cole, Debye, Constant-Phase Element

> **Read after attempting the exercises.** Arithmetic is shown; values were
> computed, not estimated. Lesson: [02 IP Models](../02-ip-models.md). All
> models **SYNTHETIC**.

---

## ★1 — One frequency by hand

$$\rho(\omega) = \rho_0\left[1 - m\left(1 - \frac{1}{1+z}\right)\right],
\qquad z = (i\omega\tau)^{c}.$$

1. $\omega = 2\pi \times 1.00 = 6.283185$ rad/s, $\omega\tau = 1.256637$;
2. $\lvert z\rvert = (\omega\tau)^{c} = 1.256637^{0.5} = 1.120998$;
   $\arg z = \pi c/2 = 0.785398$ rad;
3. $z = 1.120998\left(\cos 0.785398 + i\sin 0.785398\right) =
   0.792665 + 0.792665i$ (equivalently $z = \sqrt{1.256637}(1+i)/\sqrt{2}$);
4. $1 + z = 1.792665 + 0.792665i$, $\lvert1+z\rvert^{2} = 3.841443$, so
   $1/(1+z) = 0.466601 - 0.206318i$;
5. $1 - 1/(1+z) = 0.533399 + 0.206318i$;
6. $\rho/\rho_0 = 1 - 0.05\left(0.533399 + 0.206318i\right) =
   0.973330 - 0.010316i$;
7. $\lvert\rho\rvert = 200 \times 0.973385 = 194.677\ \Omega\,\mathrm{m}$,
   $\varphi = \arctan(-0.010316/0.973330) = -0.010598$ rad
   $= -10.598$ mrad.

Note that $\lvert z\rvert > 1$ here even though $c < 1$: the stretching applies
to the magnitude as well as to the phase.

---

## ★2 — Analytic peak at $c = 1$

$$\tan\lvert\varphi_{\max}\rvert = \frac{0.25}{2\sqrt{0.75}} = 0.144338
\;\Longrightarrow\; \lvert\varphi_{\max}\rvert = 0.143348\ \mathrm{rad}
= 143.348\ \mathrm{mrad},$$

$$f_{\max} = \frac{1}{2\pi \times 0.40 \times \sqrt{0.75}} = 0.459441\ \mathrm{Hz}.$$

---

## ★3 — Why the limits are not discriminants

DC: $\rho_0 = 50\ \Omega\,\mathrm{m}$. High frequency:
$\rho_0(1-m) = 50 \times 0.80 = 40\ \Omega\,\mathrm{m}$.

Both follow from $\rho \to \rho_0$ as $z \to 0$ and $\rho \to \rho_0(1-m)$ as
$\lvert z\rvert \to \infty$, and neither limit contains $c$: the exponent
disappears in the ratio $(1-m)z/z$. The exponent is therefore visible only in
the *shape* of the spectrum between the limits — which is why a two-point
amplitude measurement, or a single-frequency phase, cannot recover it.

---

## ★4 — The cost of an unmeasured exponent

From the measured table at $m = 0.10$: peak phases $52.656$ mrad ($c = 1.00$)
and $26.834$ mrad ($c = 0.60$), a factor

$$\frac{52.656}{26.834} = 1.962 .$$

Inverting the fitted relation at $c = 0.60$:

$$m = \left(\frac{0.052656}{0.3165}\right)^{1/1.0565}
= \left(0.166370\right)^{0.946517} = 0.1831 .$$

So a 10 mrad-scale peak phase can be produced by $m = 0.10$ with a
single relaxation or by $m = 0.183$ with $c = 0.60$ — an $83\%$ error in
chargeability from an unmeasured shape parameter.

---

## ★5 — What Kramers-Kronig does and does not imply

The reconstruction of the phase from $\ln\lvert\rho(\omega)\rvert$, using
$\varphi(\omega_0) = \frac{2\omega_0}{\pi}
\operatorname{PV}\int_0^{\infty}\frac{\ln\lvert\rho\rvert}{\omega^2-\omega_0^2}
\mathrm{d}\omega$, agrees with the model phase to $2\times10^{-12}$ rad. The four
agrees because every Cole-Cole model is causal and minimum-phase.

**Implication.** The phase is a functional of the amplitude; an
amplitude-only survey does not have a hidden extra degree of freedom, and no
measurement of both can be claimed as independent confirmation of a model.

**What it does not imply.** It does not say that an amplitude survey and a phase
survey are equally *precise*. In the field, phase is often the better-determined
quantity because it is immune to multiplicative gain errors, while the KK
relation is a theoretical identity that requires the amplitude to be known over
all frequencies — which no survey achieves. It also does not remove the need to
measure; it constrains what a model may claim.

---

## ★6 — The band exponent at $c = 0.10$

Mean phase over the band:
$\left(4.012 + 4.145\right)/2 = 4.079$ mrad $= 4.079\times10^{-3}$ rad.

$$n_{\text{eff}} = \frac{2}{\pi}\left\lvert\varphi\right\rvert
= \frac{2}{\pi}\times 4.079\times10^{-3} = 2.60\times10^{-3}.$$

The measured amplitude slope is $-2.6\times10^{-3}$, so the two agree to the
printed precision, which is the local constant-phase relation.

**What can be concluded:** the response *behaves like* a constant-phase element
with $n = 0.0026$ over $0.1$–$10$ Hz, and that is a complete description of the
measurement in that band.

**What cannot:** that the ground's Cole-Cole exponent is $0.0026$. The model's
$c$ is $0.10$, almost forty times larger; it is an extrapolation over the rest of
the spectrum, and $c$ also fixes how the flat region ends at low and high
frequency. Reporting the slope as $c$ would collapse a broad distribution of
relaxation times onto a description indistinguishable from a single very slow
one.

---

## ★7 — Specifying the KK check

1. **Quadrature.** Use the principal-value form with a Cauchy weight,
   `scipy.integrate.quad(f, lo, hi, weight="cauchy", wvar=w0)` on
   $f(\omega) = \ln\lvert\rho(\omega)\rvert/(\omega+\omega_0)$, which is
   regular at $\omega = \omega_0$; this avoids differencing the singular
   $1/(\omega^2-\omega_0^2)$.
2. **Band.** $\left[\omega_0 e^{-25}, \omega_0 e^{25}\right]$ — twenty-five
   decades, which spans the dispersion of any Cole-Cole with $c \ge 0.05$.
3. **Band edges.** Add the outside contributions analytically, treating
   $\ln\lvert\rho\rvert$ as constant ($\ln \rho_0$ below, $\ln\rho_0(1-m)$ above).
   Each piece integrates in closed form:
   $\int_{a}^{b}\mathrm{d}\omega/(\omega^2-\omega_0^2) =
   \frac{1}{2\omega_0}\ln\left\lvert\frac{b-\omega_0}{b+\omega_0}\right\rvert$.
   Without this step the residual is dominated by the truncation, not by
   causality.
4. **Expected residual.** Quadrature-limited, of order $10^{-12}$ rad for smooth
   Cole-Cole spectra. The validation on a first-order pole
   $\left(1+i\omega\tau\right)^{-1}$ gives $4.8\times10^{-10}$ to
   $5.4\times10^{-10}$ rad, which calibrates the achievable accuracy including
   the edge treatment.
5. **Failure mode of a narrow band.** With only two or three decades the
   truncation error dominates and grows like the missing logarithmic width; the
   check then fails on a perfectly causal model. That is a false alarm, and it is
   the reason the band must be stated with any published KK test.

---

## ★8 — Separating two time constants

The two-relaxation ground has $\tau_1 = 0.30$ s and $\tau_2 = 6.00$ s, so its
phase structure lives between about $1/(2\pi\times6) = 0.027$ Hz and
$1/(2\pi\times0.3) = 0.53$ Hz. Inside that band a single Cole-Cole already
absorbs the two components into one stretched response: the fitted single model
has $c = 0.311$, $\tau = 0.204$ s, with a $2.054$ mrad residual that is the size
of the stated noise.

**Band extension.** Extend downward at least one decade below the slow
relaxation ($0.001$ Hz, three decades below $0.027$ Hz) and upward at least one
decade above the fast one ($10$–$100$ Hz, i.e. keeping the existing upper end).
The measured out-of-band difference between the single Cole-Cole and the
two-component mixture is $4.491$ mrad at $10^{-3}$ Hz and $6.603$ mrad at
$10^{3}$ Hz — both above the current noise, but only by factors of $2$ to $3$.

**Noise level.** To make those differences decisive at, say, $5\sigma$, the phase
noise must fall to about $6.6/5 = 1.3$ mrad, and the survey must additionally
place most of its samples in the extension rather than in the already-saturated
middle band.

**Decision criterion and risk.** Accept the two-component model only if the
$F$-test on the residual improvement is significant (two extra parameters must
buy more than a factor of roughly $1 + 2/(N-p)$ in $\chi^2$) *and* the fitted
time constants are separated by more than the band's reciprocal width. The risk
accepted is the opposite error: with two extra parameters, a single-relaxation
ground will sometimes be fitted by two nearby relaxations that are not real. The
safeguard is to require the two fitted $\tau$'s to differ by a factor of at least
three, which the ground above exceeds by a factor of $20$.
