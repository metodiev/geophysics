# Solutions — 06-04-06 Energy Release, Moment Calculations and Scaling

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [06 Energy Release, Moment Calculations and Scaling](../06-energy-moment-calculations.md).

---

## ★1 — Plateau and moment magnitude

$$
\Omega_0 = \frac{10^{17}\times0.6325}{1.4547\times10^{20}}
= 4.348\times10^{-4}\ \mathrm{m\,s},
\qquad
M_w = \tfrac{2}{3}(17 - 9.1) = \tfrac{2}{3}(7.9) = 5.27 .
$$

The plateau is two decades above the $10^{15}$ event's
$4.348\times10^{-6}\ \mathrm{m\,s}$, as it must be for a factor of 100 in moment.

---

## ★2 — The pulse integral

$$
\int_0^{\infty}(1-s)^{2}e^{-2s}\mathrm{d}s
= \int_0^{\infty}e^{-2s}\mathrm{d}s - 2\int_0^{\infty}s\,e^{-2s}\mathrm{d}s
+ \int_0^{\infty}s^{2}e^{-2s}\mathrm{d}s
= \frac12 - 2\cdot\frac14 + \frac14 = \frac14 ,
$$

using $\int_0^{\infty}s^{n}e^{-as}\mathrm{d}s = n!/a^{n+1}$.

---

## ★3 — Units

| quantity | unit |
|---|---|
| $M_0$ | $\mathrm{N\,m}$ |
| $E_R$ | J ($\mathrm{N\,m}$) |
| $\tau_a$ | Pa |
| $\Omega_0$ | $\mathrm{m\,s}$ (displacement amplitude $\times$ time) |

---

## ★4 — Apparent stress and stress drop

$$
\tau_a = \frac{3.308\times10^{10}\times3.0066\times10^{9}}{10^{16}}
= \frac{9.946\times10^{19}}{10^{16}} = 9.95\times10^{3}\ \mathrm{Pa}
= 0.0099\ \mathrm{MPa}.
$$

$$
\Delta\sigma = \frac{7}{16}\cdot\frac{10^{16}}{(4.68\times10^{3})^{3}}
= 0.4375\cdot\frac{10^{16}}{1.0250\times10^{11}}
= 4.27\times10^{4}\ \mathrm{Pa} = 0.0427\ \mathrm{MPa}.
$$

$$
\frac{\tau_a}{\Delta\sigma} = \frac{0.0099}{0.0427} = 0.23 ,
$$

which is the printed ratio.

---

## ★5 — A band fraction

$$
X = \frac{2.0}{0.2} = 10 ,
$$

$$
\text{fraction} = \frac{2}{\pi}\left[\arctan(10) - \frac{10}{1 + 100}\right]
= \frac{2}{\pi}\left[1.47113 - 0.09901\right]
= \frac{2}{\pi}(1.37212) = 0.8735 .
$$

Nearly 87 per cent of the energy survives, because this event's corner frequency
is an order of magnitude below the band edge. Compare the $f_c = 2.785\ \mathrm{Hz}$
case in the lesson, where the same band keeps only 9.5 per cent.

---

## ★6 — Deriving the band fraction

The velocity spectrum of $u(t) = A(t/\tau^{2})e^{-t/\tau}$ has magnitude

$$
|V(f)| = 2\pi f\,|U(f)| = \frac{2\pi f A}{1 + (2\pi f\tau)^{2}} .
$$

Parseval (one-sided) gives the total

$$
\int_0^{\infty}v^{2}\mathrm{d}t = 2\int_0^{\infty}|V(f)|^{2}\mathrm{d}f
= \frac{A^{2}}{4\tau^{3}} ,
$$

and the band-limited part is

$$
2\int_0^{f_{\text{lp}}}|V|^{2}\mathrm{d}f
= \frac{2A^{2}}{2\pi\tau^{3}}\int_0^{X}\frac{x^{2}}{(1+x^{2})^{2}}\mathrm{d}x,
\qquad X = 2\pi f_{\text{lp}}\tau,
$$

with the antiderivative
$\int_0^{X}\frac{x^{2}}{(1+x^{2})^{2}}\mathrm{d}x
= \tfrac12\left[\arctan X - \frac{X}{1+X^{2}}\right]$. Dividing,

$$
\frac{E(f<f_{\text{lp}})}{E_{\text{total}}}
= \frac{2}{\pi}\left[\arctan X - \frac{X}{1 + X^{2}}\right] .
$$

---

## ★7 — Measuring the slope from data

**Design:** select events with independently determined $M_0$ and hypocentral
depths, compute the far-field velocity spectrum from instrument-corrected
three-component records, correct for attenuation with a measured $t^{*}$
(regional Q study) and for the radiation pattern using focal mechanisms, integrate
$v^{2}$ over the spectrum and over a stated band, and average the energy over
stations after correcting for directivity.

**Two ways the slope can come out wrong:** (i) an uncorrected band truncates the
energy of the smaller events and inflates the slope above $3/2$ — exactly the
1.853 measured in the lesson for a fixed 2 Hz band; (ii) an underestimated $t^{*}$
removes different fractions of high-frequency energy at different distances, which
correlates with magnitude through the magnitude–distance trade-off in a catalogue
and biases the slope in the opposite direction.

---

## ★8 — An operational definition of $E_R$

Integrate only up to a stated upper frequency $f_{\max}$, chosen as the frequency
at which the spectrum falls to a stated fraction of the noise level, and report

$$
E_R(f \le f_{\max}) = 4\pi\rho\beta R^{2}\left\langle
\int_{0}^{f_{\max}} |V(f)|^{2}\,\mathrm{d}f\right\rangle ,
$$

together with $f_{\max}$, the noise floor used to choose it, the attenuation
correction, the radiation-coefficient convention, and the station set. The number
is then reproducible and comparable with another estimate only if the same band
and corrections are used; a broadband $E_R$ claimed without $f_{\max}$ is not a
measurement.
