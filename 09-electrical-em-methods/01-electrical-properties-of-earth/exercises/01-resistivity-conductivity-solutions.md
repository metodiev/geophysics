# Solutions — 09-01-01 Resistivity and Conductivity: Definitions and Ranges

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. Lesson: [01 Resistivity and Conductivity](../01-resistivity-conductivity.md).

---

## ★1 — Resistivity from conductivity

$$\rho = \frac{1}{\sigma} = \frac{1}{2.5\times10^{-3}} = 400\ \Omega\,\mathrm{m}.$$

In the teaching catalogue that sits between "sandstone, fresh water"
(200 $\Omega\,\mathrm{m}$) and "dry limestone" (5000 $\Omega\,\mathrm{m}$):
consistent with a saturated, moderately clean sedimentary rock.

---

## ★2 — Core plug

$$A = \pi r^{2} = \pi(0.010)^{2} = 3.1416\times10^{-4}\ \mathrm{m^{2}},$$

$$\rho = \frac{RA}{L} = \frac{2400\times3.1416\times10^{-4}}{0.050}
= 15.08\ \Omega\,\mathrm{m}, \qquad
\sigma = \frac{1}{15.08} = 0.0663\ \mathrm{S\,m^{-1}}.$$

Units: $\Omega\times\mathrm{m^{2}}/\mathrm{m} = \Omega\,\mathrm{m}$. ✔

---

## ★3 — Point source

$$V = \frac{\rho I}{2\pi r} = \frac{250\times0.25}{2\pi\times2.5}
= \frac{62.5}{15.708} = 3.979\ \mathrm{V}.$$

---

## ★4 — A caliper error, doubled

Correct radius $r = 0.015$ m:

$$A = 7.0686\times10^{-4}\ \mathrm{m^{2}}, \qquad
\rho = \frac{1000\times7.0686\times10^{-4}}{0.080}
= 8.836\ \Omega\,\mathrm{m}.$$

Wrong radius $r = 0.0151$ m gives
$A = 7.1631\times10^{-4}\ \mathrm{m^{2}}$ and
$\rho = 8.954\ \Omega\,\mathrm{m}$: an error of $+1.33\%$ for a $0.67\%$ radius
error. The factor is exactly 2, as
$\delta\rho/\rho = -2\,\delta r/r$.

---

## ★5 — Contact resistance, and the wrong trend

Geometric term for two hemispheres separated widely:

$$R_\text{geo} = \frac{\rho}{2\pi}\left(\frac{1}{a}+\frac{1}{a}\right)
= \frac{50}{2\pi}\times\frac{2}{0.03} = 530.52\ \Omega.$$

With $2\times250\ \Omega$ of contact: $R = 1030.52\ \Omega$. Since
$R_\text{measured}/R_\text{geo} = 1.9425$, the inferred resistivity is
$97.1\ \Omega\,\mathrm{m}$ instead of $50$: a factor **1.94**.

For $a = 0.15$ m: $R_\text{geo} = 106.10\ \Omega$, so
$R = 606.10\ \Omega$ and the factor is **5.71**. The relative error *grows* with
electrode size because the geometric term falls while the contact term does not.
Larger electrodes reduce the absolute resistance and are easier to drive, but
they make a two-electrode resistivity measurement *worse*.

---

## ★6 — Voltmeter loading

$$i_\text{pot} = \frac{0.5}{10^{7}} = 5.0\times10^{-8}\ \mathrm{A}, \qquad
\Delta V_\text{error} = i_\text{pot}R_c = 5.0\times10^{-8}\times600
= 3.0\times10^{-5}\ \mathrm{V},$$

$$\frac{\Delta V_\text{error}}{\Delta V} = \frac{3.0\times10^{-5}}{0.5}
= 6.0\times10^{-5} = 0.006\%.$$

That is 40 times smaller than the $0.25\%$ cost of a 1 cm mislocation: on this
survey the geometry is the limiting error, not the voltmeter.

---

## ★7 — Two hemispheres

Each electrode has resistance $\rho/(2\pi a_i)$ to infinity, and in the
superposition (large-$d$) approximation the mutual term is negligible:

$$R \approx \frac{\rho}{2\pi}\left(\frac{1}{a_1}+\frac{1}{a_2}\right).$$

The approximation fails because the current from one electrode also passes
through a finite potential at the other, adding a term
$\approx \rho/(2\pi d)$ per direction: with two such terms the mutual correction
is about $2/d$ relative to $(1/a_1 + 1/a_2)$. For $d = 10a$ and $a_1 = a_2 = a$
the correction is $(2/10a)/(2/a) = 10\%$ — not negligible.

---

## ★8 — An error budget

$$\left(\frac{\delta\rho}{\rho}\right)^{2} =
\left(\frac{\delta R}{R}\right)^{2} +
\left(\frac{\delta L}{L}\right)^{2} +
\left(2\frac{\delta r}{r}\right)^{2}
= 0.5^{2} + 0.2^{2} + (2\times0.1)^{2} = 0.25+0.04+0.04 = 0.33,$$

so $\delta\rho/\rho = 0.575\%$: the 1% target **is** achievable with margin.

The quadrature sum is justified only if the errors are independent and roughly
Gaussian. A *systematic* caliper offset is not: it biases the answer in a fixed
direction, and adding it in quadrature understates the risk. The single most
valuable improvement is not the caliper but a second, independent measurement of
the resistance (or of the sample dimensions), which converts a systematic into a
checked value.
