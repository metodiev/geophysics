# Solutions — 06-03-01 Faulting, Slip and the Elastic Rebound Cycle

> **Read after attempting the exercises.** Numbers are computed with the demo's
> SYNTHETIC values, not estimated by hand. Where a quantity could be defined in
> more than one way, the definition used is stated.

Lesson: [01 Faulting, Slip and the Elastic Rebound Cycle](../01-faulting-and-slip.md).

Baseline scenario: $\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $W = 12.0\ \mathrm{km}$,
$V = 35.0\ \mathrm{mm\,a^{-1}}$, $\Delta\tau = 3.0\ \mathrm{MPa}$,
$A = 40\ \mathrm{km}\times12\ \mathrm{km}$, $\mu_s = 0.60$,
$1\ \mathrm{a} = 3.15576\times10^{7}\ \mathrm{s}$.

---

## ★1 — Loading rate

$$\dot\tau = \frac{\mu V}{W}
= \frac{3.0\times10^{10}\times3.5\times10^{-2}}{1.2\times10^{4}}
= \frac{1.05\times10^{9}}{1.2\times10^{4}}
= 8.7500\times10^{4}\ \mathrm{Pa\,a^{-1}}.$$

Conversion:

$$\dot\tau = \frac{8.7500\times10^{4}}{3.15576\times10^{7}}
= 2.7727\times10^{-3}\ \mathrm{Pa\,s^{-1}}.$$

The demo prints both lines, matching to the digits shown.

---

## ★2 — Recurrence interval

$$T = \frac{\Delta\tau}{\dot\tau}
= \frac{3.0\times10^{6}\ \mathrm{Pa}}{8.7500\times10^{4}\ \mathrm{Pa\,a^{-1}}}
= 34.29\ \mathrm{a}.$$

Unit check: $\mathrm{Pa}/(\mathrm{Pa\,a^{-1}}) = \mathrm{a}$. The demo's numeric
integrator finds event times $34.29$, $68.57$ and $102.86\ \mathrm{a}$, mean
interval $34.29\ \mathrm{a}$.

---

## ★3 — Slip two ways

$$D = \frac{\Delta\tau W}{\mu}
= \frac{3.0\times10^{6}\times1.2\times10^{4}}{3.0\times10^{10}}
= \frac{3.6\times10^{10}}{3.0\times10^{10}} = 1.200\ \mathrm{m}.$$

$$VT = 3.5\times10^{-2}\times34.2857 = 1.200\ \mathrm{m}.$$

They agree to the four significant figures carried. They **must** agree because
$T = \Delta\tau W/(\mu V)$, so $VT = V\cdot\Delta\tau W/(\mu V) = \Delta\tau W/\mu$:
the two expressions are the same algebraic object. The demo reports a relative
difference of $1.85\times10^{-16}$, which is round-off.

---

## ★4 — A second fault

$W = 20.0\ \mathrm{km}$, $V = 10.0\ \mathrm{mm\,a^{-1}} = 1.0\times10^{-2}\ \mathrm{m\,a^{-1}}$,
$\Delta\tau = 3.0\ \mathrm{MPa}$, $A = 20\ \mathrm{km}\times20\ \mathrm{km} = 4.0\times10^{8}\ \mathrm{m^2}$.

$$\dot\tau = \frac{3.0\times10^{10}\times1.0\times10^{-2}}{2.0\times10^{4}}
= \frac{3.0\times10^{8}}{2.0\times10^{4}} = 1.5\times10^{4}\ \mathrm{Pa\,a^{-1}},$$
$$T = \frac{3.0\times10^{6}}{1.5\times10^{4}} = 200\ \mathrm{a},$$
$$D = \frac{3.0\times10^{6}\times2.0\times10^{4}}{3.0\times10^{10}}
= \frac{6.0\times10^{10}}{3.0\times10^{10}} = 2.000\ \mathrm{m},$$
$$M_0 = \mu A D = 3.0\times10^{10}\times4.0\times10^{8}\times2.000
= 2.400\times10^{19}\ \mathrm{N\,m}.$$

Check: $VT = 1.0\times10^{-2}\times200 = 2.000\ \mathrm{m}$ ✔.

**Factor.** $T \propto W/V$, so

$$\frac{T_{\text{new}}}{T_{\text{old}}}
= \frac{W_{\text{new}}}{W_{\text{old}}}\cdot\frac{V_{\text{old}}}{V_{\text{new}}}
= \frac{20.0}{12.0}\times\frac{35.0}{10.0} = 1.667\times3.5 = 5.833,$$

and $34.29\times5.833 = 200\ \mathrm{a}$ ✔. Both changes lengthen the interval:
a wider layer stores more strain, and a slower plate reloads it more slowly. The
$W$ change is worth $\times1.667$, the $V$ change $\times3.5$.

---

## ★5 — The moment-rate identity

$M_0 = \mu A D$ and $D = \Delta\tau W/\mu$, so

$$\frac{M_0}{T} = \frac{\mu A D}{\Delta\tau W/(\mu V)}
= \frac{\mu A\,(\Delta\tau W/\mu)\,\mu V}{\Delta\tau W} = \mu A V.$$

The stress drop, the width and the slip all cancel: the identity holds for *any*
$\Delta\tau$, $W$ and $D$ that satisfy $D = \Delta\tau W/\mu$.

Numerically, $\mu A V = 3.0\times10^{10}\times4.8\times10^{8}\times3.5\times10^{-2}
= 5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}}$, and

$$\frac{M_0}{T} = \frac{1.7280\times10^{19}}{34.2857}
= 5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}}. ☑$$

---

## ★6 — What the $10^{-15}$ residual measures

The comparison is between the **mean of the inter-event times found by stepping
the stress numerically** and the **closed-form** value $\Delta\tau/(\mu V/W)$.
Both are evaluated in IEEE double precision, which carries about
$1.1\times10^{-16}$ relative resolution, so a residual of
$2.69\times10^{-15}$ is a few tens of ulp — pure round-off accumulated over
300 steps.

It is therefore a statement about the *arithmetic*: the integrator and the
closed form solve the same model, and the code that implements them agrees. It is
**not** evidence about the Earth, because the model itself — constant $\Delta\tau$,
constant $V$, one patch — is an assumption written into the inputs, not something
the residual can test.

---

## ★7 — Pore pressure to advance the clock by 10 years

Stress accumulated in 10 years:

$$\Delta CFF_{\text{needed}} = \dot\tau\times10 = 8.7500\times10^{4}\times10
= 8.7500\times10^{5}\ \mathrm{Pa} = 0.875\ \mathrm{MPa}.$$

Invert $\Delta CFF = \mu_s\Delta p$:

$$\Delta p = \frac{0.875}{0.60} = 1.4583\ \mathrm{MPa} \approx 1.46\ \mathrm{MPa}.$$

So about $1.5\ \mathrm{MPa}$ of pore-pressure rise is equivalent to a decade of
tectonic loading at this rate.

---

## ★8 — Uncertainty propagation

$T = \Delta\tau\,W/(\mu V)$, so $T$ is a product of powers:
$T \propto \Delta\tau^{1}\,W^{1}\,V^{-1}\,\mu^{-1}$. For independent
multiplicative errors the fractional variances add:

$$\left(\frac{\sigma_T}{T}\right)^{2}
= (0.20)^{2}+(0.15)^{2}+(0.10)^{2}+(0.05)^{2}
= 0.0400+0.0225+0.0100+0.0025 = 0.0750,$$

$$\frac{\sigma_T}{T} = \sqrt{0.0750} = 0.2739 \approx 27\%.$$

For the baseline $T = 34.29\ \mathrm{a}$ that is $\pm9.4\ \mathrm{a}$.

**Dominant contributor:** the stress drop ($20\%$, contributing $0.0400$ of the
total $0.0750$, i.e. $53\%$ of the variance).

**Why quadrature is optimistic.** Summing variances in quadrature assumes the
four inputs are independent and unbiased. Here they are neither. $\Delta\tau$ is
inferred *using* $\mu$ and $W$, so an error in $\mu$ enters $\Delta\tau$ as well
as $T$; and $W$ is defined by the brittle–ductile transition, which depends on
temperature, strain rate and hence on $V$. Correlations can either cancel or
compound the errors, and quadrature cannot see that.

---

## ★9 — A non-constant stress drop (specification)

**Model.** Keep everything from Section 3 of the lesson except the stress drop:
draw each event's $\Delta\tau_i$ independently from a **log-normal** distribution
with median $3.0\ \mathrm{MPa}$ and logarithmic standard deviation
$\sigma_{\ln\Delta\tau} = 0.5$ (coefficient of variation $\approx0.53$). Use the
demo's stress-stepping loop, but on each failure subtract the drawn
$\Delta\tau_i$ instead of a constant and record the new event time.

**Metric.** The **coefficient of variation** of the inter-event times,
$\mathrm{CV} = \sigma_T/\bar T$, together with the autocorrelation of successive
intervals at lag 1. A perfectly periodic sequence has $\mathrm{CV} = 0$ and
lag-1 autocorrelation $0$; a memoryless sequence has $\mathrm{CV}$ equal to the
CV of the stress drops and lag-1 autocorrelation consistent with noise.

**Predicted observation.** Doubling $\sigma_{\ln\Delta\tau}$ roughly doubles
$\mathrm{CV}$ (to first order $\mathrm{CV}_T \approx
\mathrm{CV}_{\Delta\tau}$ because $T \propto \Delta\tau$), while the *mean*
interval stays at $34.29\ \mathrm{a}$. The sequence remains "quasi-periodic" in
the sense that the mean is stable, but individual intervals spread. Increasing
the spread further eventually makes the sequence look clustered, which is the
qualitative behaviour seen in real catalogues and is *not* produced by the
constant-stress-drop model.

---

## ★10 — Aseismic creep and the direction of the bias

**(a) Direction.** $\dot\tau = \mu V/W$ counts the *entire* relative motion as
elastic strain. If a fraction $f$ of the relative motion is instead taken up by
aseismic creep in or around the brittle layer, only $(1-f)V$ accumulates elastic
strain on the seismogenic patch. Replacing $V$ by $(1-f)V$ lengthens the mean
interval by a factor $1/(1-f)$:

$$T_{\text{true}} = \frac{\Delta\tau\,W}{\mu\,(1-f)V} = \frac{T_{\text{model}}}{1-f}.$$

So ignoring creep **underestimates** $T$: the quoted interval is a **lower
bound**. (The same argument run the other way — if the fault creeps *faster* than
$V$ because it is unloading stored strain from a previous event — is a transient,
not a steady state, and does not change the conclusion for the long-term mean.)

**(b) Why a bound and not a value.** $f$ is not an independent measurement; it is
usually inferred as the difference between geodetic moment rate and catalogue
moment rate, both of which carry their own errors and their own definitions of
what counts as an earthquake. Because $f$ cannot be measured directly at depth,
the honest statement is a range: $T$ lies between the model value (no creep) and
$T/(1-f_{\max})$ for the largest plausible creep fraction. Quoting a single
number silently sets $f = 0$.
