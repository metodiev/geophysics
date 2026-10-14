# Solutions — 06-12-03 Rate-and-State Friction and Dieterich Seismicity Model

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [03 Rate-and-State Friction and the Dieterich Seismicity Model](../03-rate-state-triggering.md).

---

## ★1 — The response at three times

$$f(t) \equiv \frac{r(t)}{r_0}
= \frac{1}{1 - (1 - \gamma^{-1})e^{-t/t_a}},
\qquad 1 - \gamma^{-1} = 1 - 0.05 = 0.95 .$$

**$t = 1$ d:** $e^{-1/30} = e^{-0.033333} = 0.967216$, so
$0.95 \times 0.967216 = 0.918855$, $1 - 0.918855 = 0.081145$, and
$f = 1/0.081145 = 12.324$ ✔.

**$t = 10$ d:** $e^{-10/30} = e^{-0.333333} = 0.716531$, so
$0.95 \times 0.716531 = 0.680704$, $1 - 0.680704 = 0.319296$, and
$f = 1/0.319296 = 3.132$ ✔.

**$t = 100$ d:** $e^{-100/30} = e^{-3.333333} = 0.035674$, so
$0.95 \times 0.035674 = 0.033890$, $1 - 0.033890 = 0.966110$, and
$f = 1/0.966110 = 1.035$ ✔.

All three match the demonstration to the printed three decimals.

---

## ★2 — The two limits

$$t \to 0^+: f \to \frac{1}{1 - (1-\gamma^{-1})} = \frac{1}{\gamma^{-1}} = \gamma
= 20.0 \quad(\text{the demonstration's measured } r(0^+)/r_0 = 20.000),$$

$$t \to \infty: f \to \frac{1}{1 - 0} = 1 \quad
(\text{the demonstration's } r(10^{6}\ \mathrm{d}) = 1.000000).$$

A stress step therefore buys a **transient**: the rate jumps by the factor
$\gamma$ and decays back to the pre-step rate. It does *not* produce a
permanently elevated rate, because the steady state under rate-and-state friction
is set by the stressing *rate*, not by the stress *level*, and the step does not
change the stressing rate.

That is the single most consequential statement of the lesson: an injection that
changes the effective normal stress but not the loading rate produces aftershock-like
decay, and an injection that changes the loading rate produces a sustained change.

---

## ★3 — Omori-equivalent corner time

$$c = \frac{t_a}{\gamma - 1} = \frac{30.0\ \mathrm{d}}{20.0 - 1}
= \frac{30.0}{19} = 1.579\ \mathrm{d},$$

the demonstration's printed value. The unit is days because $t_a$ is in days and
$\gamma$ is dimensionless — a reminder that $c$ is not an independent parameter of
the physics, it is $t_a$ rescaled.

---

## ★4 — Ratio versus fitted $p$

$$\frac{r(1\ \mathrm{d})}{r(10\ \mathrm{d})} = \frac{12.324}{3.132} = 3.935 .$$

A pure power law $r \propto t^{-p}$ would give a ratio $10^{p}$:

$$10^{0.4186} = 2.622 .$$

The measured ratio is much larger than the power law predicts, because the Omori
form $r \propto (t+c)^{-p}$ has a corner at $t \sim c$ and the ratio is dominated
by the decay *before* the corner. The Omori approximation is the high-rate limit
$r/r_0 \gg 1$: over $1$–$10$ days the model's rate falls from $12.3$ to $3.1$, both
of which satisfy that condition, but the *corner* at $c = 1.579\ \mathrm{d}$ still
sits inside the interval, so the ratio is not $\propto t^{-p}$ there. Fitting a
power law to a curved interval and then interpreting the exponent physically is
the error this exercise is designed to expose.

---

## ★5 — How much $c$ is actually constrained

Using the "$\Delta\log L < 2$ is not a constraint" rule on the demonstration's
table:

| $c$ (d) | $p$ (fit) | $\Delta\log L$ | within one standard error? |
|---|---|---|---|
| 0.05 | 0.4102 | $-0.14$ | yes |
| 0.20 | 0.4230 | $0.00$ | yes (best) |
| 0.50 | 0.4361 | $-0.69$ | yes |
| 1.00 | 0.4496 | $-2.03$ | borderline |
| 3.00 | 0.4806 | $-6.23$ | no |
| 10.00 | 0.5401 | $-14.18$ | no |

So the catalogue constrains $c$ only to roughly $0.05$–$1\ \mathrm{d}$, a
factor-of-20 range, and within that range $p$ is *forced* to move from $0.410$ to
$0.450$. $c$ is quoted with the widest uncertainty because it is traded against
both $K$ and $p$ — the bootstrap confirms the coupling directly, with
$\mathrm{corr}(\ln K, p) = +0.9997$ and $\mathrm{corr}(\ln c, p) = +0.4003$, and a
5–95% spread of $5.82$ for $c$ against $1.34$ for $p$.

---

## ★6 — Window truncation

Fitting a 30-day window gives $(47.455, 2.9076, 0.9967)$, and the 365-day window
gives $(9.144, 0.1336, 0.4186)$.

Two effects act in the same direction:

1. **A short window sees a curve that is closer to a pure power law.** With
   $t_{\max} \ll 100\ \mathrm{d}$ the model rate is still far above $r_0$ for the
   whole observation, so the regime is closer to the high-rate limit where
   $p \to 1$; the demonstration's $\gamma$-sweep shows the same trend
   ($p = 0.233$ at $\gamma = 5$ rising to $0.680$ at $\gamma = 1000$).
2. **The corner must move to a larger time to explain a curve that has**
   **not yet decayed.** With no late-time flattening in the window, the data
   prefer a larger $c$ ($2.9076\ \mathrm{d}$) so that the decay stays steep.

The conclusion is a reporting rule, not a numerical curiosity: a published
$(c, p)$ pair without the observation window, the magnitude of completeness and the
detection model is not a reproducible measurement. The same catalogue yields
$p = 0.9967$ or $p = 0.4186$ depending only on how long one looks.

---

## ★★★7 — Bootstrap experiment (specification)

**Resampling scheme.** Two bootstraps, differing only in how the data are drawn:

- **Scheme A (window-independent):** generate $B = 2000$ synthetic catalogues of
  the *same length* as the demonstration's (365 days) from the Dieterich model,
  refit $(K, c, p)$ to each, and record the correlation matrix of
  $(\ln K, \ln c, p)$.
- **Scheme B (window-dependent):** draw $B$ resamples from the *observed*
  catalogue by uniform sampling with replacement of event times (non-parametric
  bootstrap), refit, and record the same matrix.

**Statistic.** $\rho_B = \mathrm{corr}(\ln K, p)$ in each scheme, reported with the
2.5–97.5 percentile range over $B$ realisations. The demonstration's value is
$\rho = +0.9997$.

**Prediction.** Under the "property of the parameterisation plus the finite
window" hypothesis, both schemes give $\rho \approx +1$: the correlation arises
because the Omori-Utsu form makes $K$ absorb the integral of the decay once $p$
changes, which is a property of the *functional form*, not of the particular
catalogue. The observable difference between the schemes is not $\rho$ but the
*widening* of the $c$ interval in Scheme B, because the observed catalogue has
fewer early events than the model.

**Falsification.** If $\rho$ were substantially below 1 (say $< 0.9$) and stable
across $B$, the correlation would be attributable to the sampling rather than to
the parameterisation — which would be evidence that the parameterisation is better
conditioned than the demonstration claims, and would require the claim in the
lesson to be revised.

---

## ★★★8 — Deriving the Dieterich response (worked derivation)

**Rate-and-state law.** With slip speed $V$, state variable $\theta$, direct
effect $a$ and evolution effect $b$,

$$\tau = \sigma_n\left[\mu_0 + a\ln\frac{V}{V_0} + b\ln\frac{V_0\theta}{D_c}\right],
\qquad \frac{\mathrm{d}\theta}{\mathrm{d}t} = 1 - \frac{V\theta}{D_c}.$$

**Steps and approximations.**

1. **Constant normal stress** $\sigma_n$ and constant loading rate: the shear
   traction increases at a fixed rate $\dot\tau$.
2. **Seismicity rate proportional to $1/\theta$**: assume the nucleation rate of
   events is inversely proportional to the state variable,
   $r = r_0(\theta_0/\theta)$. This is the *seismicity law* and is an assumption,
   not a consequence.
3. **Small direct effect / slow healing**: solve the state evolution at fixed $V$
   over the timescale of interest, so $\mathrm{d}\theta/\mathrm{d}t \approx 1 -
   V\theta/D_c$ with $V$ approximately constant.
4. **Linearise the friction law in $\ln V$** and integrate over the observation
   time, treating the stress step as an instantaneous offset $\Delta\tau$.

Under these, the state variable relaxes toward its steady-state value with the
characteristic time

$$t_a = \frac{a\sigma_n}{\dot\tau},$$

and the rate ratio becomes

$$\frac{r(t)}{r_0} = \frac{1}{1 - \left(1 - \gamma^{-1}\right)e^{-t/t_a}},
\qquad \gamma = \frac{r(0^+)}{r_0},$$

which is the demonstration's formula. For a step $\Delta\tau$ small compared with
$a\sigma_n$, $\gamma - 1 \approx \Delta\tau/(a\sigma_n) \ll 1$, so
$(1 - \gamma^{-1}) \to 1$ and

$$\frac{r}{r_0} \approx \frac{1}{1 - e^{-t/t_a}} \approx \frac{t_a}{t}
\quad\text{for } t \ll t_a,$$

which is Omori's law with $p = 1$ and $c \approx 0$.

**Small-step limit.** Write $\gamma = 1 + \epsilon$ with $\epsilon \ll 1$; then
$1 - \gamma^{-1} = \epsilon/(1+\epsilon) \approx \epsilon$ and

$$\frac{r}{r_0} \approx \frac{1}{1 - \epsilon e^{-t/t_a}}
\approx 1 + \epsilon e^{-t/t_a} = 1 + (\gamma - 1)e^{-t/t_a}.$$

The excess rate therefore decays *exponentially* with time constant $t_a$ when the
stress step is small, and only becomes a power law when the step is large enough
that $r/r_0 \gg 1$ over the observation. The demonstration measures the same
transition from the other side: fitting the Omori-Utsu form to catalogues generated
with $\gamma = 5, 20, 100, 1000$ returns $p = 0.233, 0.433, 0.564, 0.680$, i.e.
$p \to 1$ only as the step grows.

**What is discarded.** The $b$-dependence of $\theta_{\text{ss}}$, any change in
$\sigma_n$ (which is the entire pressure-diffusion mechanism of
[lesson 02](../02-pore-pressure-triggering.md)), and any healing that operates on
the same timescale as the decay.

---

## ★★★9 — A detection model that separates incompleteness (specification)

**Model.** Let the *detection* probability for an event of magnitude $M$ at time
$t$ be $q(M, t)$, and replace the observed rate with
$\lambda_{\text{obs}}(t) = q(M\!>\!M_c(t), t)\,\lambda_{\text{model}}(t)$. Specify
$q$ as a logistic function of signal-to-noise ratio computed from a station
inventory and a station-magnitude relation, and let $M_c(t)$ be estimated from the
observed maximum-amplitude decay after the sequence's largest event.

**Data required.** Continuous waveform amplitudes (or at least a station-magnitude
catalogue), the station geometry and response, and the background noise level —
i.e. more than a hypocentre list. A catalogue of times alone cannot constrain
$q$, which is precisely why the demonstration treats the first hours as
irrecoverable.

**Fitting.** Fit $(K, c, p)$ jointly with the detection parameters by maximum
likelihood, replacing the Poisson rate by $q\lambda$ and including events
*below* $M_c$ as censored observations with the appropriate likelihood terms.

**Falsification.** The model is falsified if the fitted $q$ requires detection
probabilities greater than 1, if it predicts more events below $M_c$ than the
catalogue's completeness curve permits, or if the joint fit still shows
$p$ changing by more than a factor of two between the full window and a
first-20-days-truncated fit (the demonstration's $0.4186 \to 0.1447$). Any of those
outcomes means the extra data have not made the parameters separable.
