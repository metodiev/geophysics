# Solutions — 06-09-01 Acoustic Impedance, Reflection Coefficients and the Convolution Model

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. Everything is SYNTHETIC. Lesson:
> [01 Reflection Principle](../01-reflection-principle.md).

---

## ★1 — Impedance and reflection coefficient

$$Z_1 = \rho_1v_1 = 2.10 \times 2.40 = 5.040, \qquad
Z_2 = 2.40 \times 2.80 = 6.720,$$
$$R = \frac{Z_2-Z_1}{Z_2+Z_1} = \frac{6.720-5.040}{6.720+5.040}
= \frac{1.680}{11.760} = +0.142857 .$$

**Polarity:** $R>0$, a *positive* (hard) reflection, because the impedance
increases downward. A positive $R$ means the reflected wavelet has the same
polarity as the incident one at normal incidence.

---

## ★2 — Two-way times

$$t_1 = \frac{2h_1}{v_1} = \frac{2\times0.60}{2.20} = 0.545455\ \mathrm{s}
\quad\text{(printed } 0.5455\text{)},$$
$$t_2 = t_1 + \frac{2h_2}{v_2} = 0.545455 + \frac{2\times0.40}{2.80}
= 0.545455 + 0.285714 = 0.831169\ \mathrm{s}
\quad\text{(printed } 0.8312\text{)}.$$

Both match the demonstration. Note that $t_2$ is *cumulative*: the two-way time
to an interface is the sum over all layers above it.

---

## ★3 — Units and dimensional analysis

$$Z = \rho v = \left[\mathrm{g\,cm^{-3}}\right]
\left[\mathrm{km\,s^{-1}}\right]
= 10^{3}\ \mathrm{kg\,m^{-3}} \times 10^{3}\ \mathrm{m\,s^{-1}}
= 10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}} = 10^{6}\ \mathrm{rayl}.$$

For the demonstration's interface 1, $Z = 2.10\times2.20 = 4.620$ in
$10^{6}\ \mathrm{rayl}$, printed as $4.620$ in the lesson's units.

$$R = \frac{Z_2-Z_1}{Z_2+Z_1}: \quad
\frac{[Z]-[Z]}{[Z]+[Z]} = \text{dimensionless}.$$

The units cancel because $R$ is a ratio of the *difference* to the *sum* of two
quantities of the same kind. This is why $R$ is measured the same way whatever
units the impedances are quoted in — and why a unit error in $Z$ alone cannot
produce a wrong $R$.

---

## ★4 — Deriving $T = 2Z_2/(Z_1+Z_2)$

Continuity at the interface gives

$$A_i + A_r = A_t \qquad\text{(pressure)},$$
$$\frac{A_i - A_r}{Z_1} = \frac{A_t}{Z_2} \qquad\text{(particle velocity)}.$$

Divide the second by the first after eliminating $A_t$: from the first,
$A_t = A_i + A_r$; substituting into the second,

$$\frac{A_i-A_r}{Z_1} = \frac{A_i+A_r}{Z_2}
\;\Longrightarrow\;
Z_2(A_i - A_r) = Z_1(A_i + A_r)
\;\Longrightarrow\;
R = \frac{Z_2-Z_1}{Z_2+Z_1}.$$

For the transmission coefficient, use $A_t = A_i + A_r = A_i(1+R)$:

$$T = 1 + R = \frac{Z_2+Z_1+Z_2-Z_1}{Z_2+Z_1} = \frac{2Z_2}{Z_2+Z_1}.$$

**Numerical verification.** At the model's interface 2,
$Z_1 = 2.30\times2.80 = 6.440$ and $Z_2 = 2.45\times3.20 = 7.840$:

$$R = \frac{7.840-6.440}{7.840+6.440} = \frac{1.400}{14.280} = +0.098039,$$
$$T = \frac{2\times7.840}{14.280} = \frac{15.680}{14.280} = 1.098039,$$
$$1 + R = 1.098039 = T.\quad\checkmark$$

The printed value is $R = +0.0980$ and $T = 1.0980$.

---

## ★5 — Depth from a two-way time

**Cumulative two-way time to the base of layer 3:**

$$t_3 = \frac{2\times0.60}{2.20} + \frac{2\times0.40}{2.80}
+ \frac{2\times0.50}{3.20}
= 0.545455 + 0.285714 + 0.312500 = 1.143669\ \mathrm{s}.$$

**Remaining time in the $3.60\ \mathrm{km\,s^{-1}}$ half-space:**

$$t_{\text{left}} = 1.600000 - 1.143669 = 0.456331\ \mathrm{s}
\;\Longrightarrow\;
h = \frac{v\,t_{\text{left}}}{2}
= \frac{3.60\times0.456331}{2} = 0.821396\ \mathrm{km}.$$

**Target depth:** $1.500 + 0.821396 = 2.321396\ \mathrm{km}$.

**Single average-velocity conversion:** the mean velocity implied by the section
is

$$\bar v = \frac{2\times2.321396}{1.600000} = 2.901745\ \mathrm{km\,s^{-1}}.$$

Using instead $v = 3.00\ \mathrm{km\,s^{-1}}$ gives

$$h_{\text{wrong}} = \frac{3.00\times1.60}{2} = 2.400\ \mathrm{km},$$

an error of $+0.0786\ \mathrm{km} = +3.4\%$. **The error is the price of a
single velocity for a layered overburden**, and its size depends on how far the
average is from the true vertical travel-time average.

---

## ★6 — The impedance trade

$$2.80 \times 2.30 = 6.440, \qquad
3.08 \times 2.091 = 6.44028 \approx 6.440, \qquad
3.50\times1.84 = 6.440 .$$

All three give the same impedance to the printed precision. For the third
member with $\rho = 2.00\ \mathrm{g\,cm^{-3}}$:

$$v = \frac{6.440}{2.00} = 3.220\ \mathrm{km\,s^{-1}},$$

and the reflection coefficient at the top of layer 2 is

$$R = \frac{6.440-4.620}{6.440+4.620} = \frac{1.820}{11.060} = +0.164557,$$

which is the demonstration's printed $+1.65\times10^{-1}$. **Three different
$(v,\rho)$ pairs produce the same seismic response at normal incidence**: the
data constrain the product $Z = \rho v$, not its factors.

---

## ★7 — What linearity does and does not buy

**What linearity preserves.** Because the convolutional model is linear in the
reflectivity, the *sum* of two primaries can always be written as a single
trace, and any linear operation (filter, stack, migration by summation)
commutes with it. Nothing about the *positions* or *amplitudes* is lost by
writing the sum.

**What it does not preserve.** Two primaries at different times cannot be
replaced by one arrival at one time without losing information: the mapping from
a two-spike reflectivity to a one-spike reflectivity changes the data, and no
rearrangement of a linear operator can undo it. The collapse is possible only in
the **tuning limit**: if the separation $\Delta t$ is much smaller than the
wavelet's width, the composite is a single wavelet whose amplitude encodes a
weighted sum of the coefficients and whose apparent time lies between them — and
that single wavelet is *not* invertible for the two coefficients (this is the
$\lambda/8$ Widess limit of lesson 07).

**The condition, stated precisely.** Two primaries are indistinguishable from one
when their separation is below the source wavelet's resolution scale *and* the
data are noise-limited at the amplitude of the difference. If the wavelet is
effectively a delta function ($\Delta t$ resolvable) the two arrivals are always
separable in principle, however small their amplitude.

---

## ★8 — Breaking the velocity–density degeneracy

**Measurement.** Amplitude versus offset (AVO) on a common-midpoint gather
spanning a range of incidence angles. The reflection coefficient's angular
dependence contains $v_p$, $v_s$ and $\rho$ in *separate* combinations, so a
second independent relation is added to $Z = \rho v_p$. The physically
independent quantity measured at non-normal incidence is the **shear modulus
contrast** (through $v_s$), which normal-incidence data cannot see because the
normal-incidence coefficient involves only the impedance.

**What must be known for it to be quantitative.**

1. The **average** $v_p/v_s$ of the two media, since the linearised AVO
   coefficients are written in terms of $\bar v_s/\bar v_p$; in practice this
   comes from an independent measurement (sonic log, or a converted-wave
   survey).
2. The **density** of at least one of the two media, or an independent
   constraint (Gassmann with a known porosity and fluid) — otherwise the
   inversion recovers only the two AVO coefficients $A$ and $B$, and lesson 05
   constructs an explicit one-parameter family of $(v_p,v_s,\rho)$ triples that
   fit the same curve.
3. The **angle–offset relation** (a correct velocity model) for converting
   offsets to angles; a wrong $v_{\text{NMO}}$ rotates the AVO curve and biases
   the gradient $B$ (lesson 03).
