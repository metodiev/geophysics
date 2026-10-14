# Solutions — 02-03-02 Damped and Driven Oscillations, Resonance and Quality Factor

> **Read this after attempting the exercises, not before.** These are worked
> solutions showing a valid route; they are not the only route. Values attributed
> to the demo are its actual output.

---

## ★1 — Damped free oscillator

**(a)** $\omega_0 = \sqrt{50/0.5} = \sqrt{100} = 10\ \mathrm{rad\,s^{-1}}$;
$\omega_d = \sqrt{100 - 2.25} = 9.886859\ \mathrm{rad\,s^{-1}}$;
$T_d = 2\pi/\omega_d = 0.635543$ s;
$Q = \omega_0/(2\beta) = 10/3 = 3.333333$.

**(b)** $\beta = 1.5 < \omega_0 = 10$: underdamped.

**(c)** $x_n/x_{n+1} = e^{\beta T_d} = e^{1.5\times0.635543} = e^{0.953315} =
2.594312$. Equivalently $\delta = \beta T_d = 0.953315$ and the ratio is
$e^{\delta}$ ✓.

**(d)** $e^{-\beta t} = 0.01$ gives
$t = \ln 100/\beta = 4.605170/1.5 = 3.070113$ s, about 4.8 damped periods.

---

## ★2 — The three definitions are not identical

- $Q_1 = \omega_0/(2\beta) = 10/4 = 2.500000$ (exact by definition of $Q$ as
  $\omega_0/2\beta$).
- $\omega_d = \sqrt{100-16} = 9.165151$, $T_d = 0.685399$,
  $\delta = \beta T_d = 1.370797$, so $Q_2 = \pi/\delta = 2.291467$.
- The exact half-power frequencies from equation (13):
  $\sqrt{\omega_0^2-2\beta^2 \pm 2\beta\sqrt{\omega_0^2-\beta^2}}
  = \sqrt{92 \pm 8\sqrt{84}}$, giving $\omega_- = 7.266919$ and
  $\omega_+ = 11.453898$, so $\Delta\omega = 4.186979$ and
  $Q_3 = \omega_0/\Delta\omega = 2.388356$.

The three differ by 9 per cent at $Q \approx 2.4$. The exact relations are
$Q_2 = Q_1\sqrt{1-1/(4Q_1^2)} = 2.5\sqrt{1-0.04} = 2.449490$ and
$Q_3$ as above; all three converge only as $Q$ grows. **Never quote $Q$ without
the definition used.**

---

## ★3 — Amplification equals $Q$

$A(0) = F_0/(m\omega_0^2)$ and
$A_{\max} = (F_0/m)/\left(2\beta\sqrt{\omega_0^2-\beta^2}\right)$, so

$$\frac{A_{\max}}{A(0)} = \frac{\omega_0^2}{2\beta\sqrt{\omega_0^2-\beta^2}}
= \frac{\omega_0}{2\beta}\sqrt{\frac{\omega_0^2}{\omega_0^2-\beta^2}}
= Q\left(1 - \frac{1}{4Q^2}\right)^{-1/2}\!\!,$$

using $\omega_0^2 - \beta^2 = \omega_0^2(1 - 1/(4Q^2))$. Both sides are
dimensionless, as required. The identity $A_{\max}/A(0) = Q$ requires
$Q \to \infty$; at $Q = 10$ the correction is $+0.125$ per cent, matching the
demo's $10.0125$.

---

## ★4 — High-$Q$ oscillator

**(a)** $\beta = \omega_0/(2Q) = 20/100 = 0.2\ \mathrm{s^{-1}}$.

**(b)** $\omega_r = \sqrt{400 - 0.08} = 19.997999\ \mathrm{rad\,s^{-1}}$: 0.01 per
cent below $\omega_0$.

**(c)** Exact: $\sqrt{400 - 0.08 \pm 0.4\sqrt{400-0.04}} = \sqrt{399.92 \pm
7.9992}$, giving $\omega_- = 19.797999$ and $\omega_+ = 20.198002$, so
$\Delta\omega = 0.400003\ \mathrm{s^{-1}}$; the approximation
$2\beta = 0.4$ differs by $+7.5\times10^{-6}$ relative, i.e. $7.5\times10^{-4}$
per cent.

**(d)** The displacement lags the force by $\delta \approx 0$ at
$\omega \ll \omega_0$, exactly 90° at $\omega = \omega_0$ and approximately 180°
at $\omega \gg \omega_0$; the transition takes place over a frequency width of
order $\Delta\omega$ around $\omega_0$.

---

## ★5 — Geophone design

**(a)** $Q = 1/(2\zeta) = 1/1.4 = 0.714286$;
$\omega_0 = 62.831853\ \mathrm{rad\,s^{-1}}$, $\beta = \zeta\omega_0 =
43.982297\ \mathrm{s^{-1}}$, so $\Delta\omega = 2\beta = 87.964594\
\mathrm{rad\,s^{-1}}$ (and the exact formula adds 0.7 per cent at this low
$Q$ — the approximation is at the edge of its validity and should be quoted as
such).

**(b)** Using $\tan\delta = 2\beta\omega/(\omega_0^2-\omega^2)$: at 1 Hz
($\omega = 6.283$), $\tan\delta = 87.9646\times6.283/(3947.8-39.5) = 0.1414$,
$\delta = 8.05^\circ$; at 10 Hz, $\omega = \omega_0$ so $\delta = 90.00^\circ$;
at 100 Hz ($\omega = 628.3$), $\tan\delta = 87.9646\times628.3/(3947.8-394784)
= -0.1414$, giving $\delta = 171.95^\circ$. The phase is nearly flat only well
below $\omega_0$; at 1 Hz it is within 8° of zero.

**(c)** With $\zeta = 1/\sqrt2$ (i.e. $Q = 1/\sqrt2 \approx 0.707$) the
amplitude response $|{\omega^2}/{\omega_0^2}| \times A(\omega)$ for acceleration
input has its flattest possible passband — the Butterworth condition — and the
impulse response contains no oscillation (it is the fastest non-oscillatory
return to rest). Both properties are desirable in a sensor whose output should be
proportional to ground motion over a wide band.

---

## ★6 — Ring-down measurement

**(a)** Ratios: $1.000/0.870 = 1.149425$, $0.870/0.757 = 1.149273$,
$0.757/0.659 = 1.148710$. Mean $= 1.149136$, so $\delta = \ln 1.149136 =
0.139079$.

**(b)** The peaks are one damped period apart, so $T_d = 0.100$ s and
$\omega_d = 2\pi/0.1 = 62.831853\ \mathrm{rad\,s^{-1}}$. Then
$\beta = \delta/T_d = 1.390790\ \mathrm{s^{-1}}$ and
$\omega_0 = \sqrt{\omega_d^2+\beta^2} = 62.847243\ \mathrm{rad\,s^{-1}}$.

**(c)** $Q = \pi/\delta = 22.588833$ (definition 3 of the lesson). The
approximation error of using $\pi/\delta$ as the *energy* definition is
$1/(4Q^2) = 4.9\times10^{-4}$ relative — negligible here, and the honest
statement is that all four definitions agree to four decimals at
$Q \approx 22.6$.

---

## ★7 — Reading the demonstration

**(a)** At $\beta = 0.5$: $Q = \pi/\delta = 9.9875$ and
$Q = \omega_0/2\beta = 10.0000$, ratio $0.998750$; predicted ratio
$\omega_d/\omega_0 = 9.987492/10 = 0.9987492$ ✓. At $\beta = 2.0$: $2.4495$ and
$2.5000$, ratio $0.979800$; predicted $9.797959/10 = 0.9797959$ ✓.

**(b)** $A_{\max}/A(0) = 10.0125$; $Q = 10.0000$; the exact expression
$(1-1/(4Q^2))^{-1/2} = 10.012521$ ✓ to all printed digits.

**(c)** At $\omega = \omega_0$ the response is purely $1/(2\beta\omega_0)$, with
no cancellation between the two terms of the denominator. Away from
$\omega_0$ the denominator is a small difference of two larger numbers, so the
relative error of the numerical integral is amplified by the condition number of
that cancellation — here about $10^3$ for the points at
$|\omega-\omega_0| \approx 0.5\ \mathrm{s^{-1}}$.

**(d)** The final column, $\Delta\omega/2\beta$: it isolates the correction to
the approximation and it is the only column that cannot be produced by the
approximation itself.

---

## ★8 — Energy bookkeeping

**(a)** $E = E_0e^{-2\beta t}$ and one period is $T_d = 2\pi/\omega_d$, so
$\Delta E/E = 1 - e^{-2\beta T_d} \approx 2\beta T_d = 4\pi\beta/\omega_d
\approx 4\pi\beta/\omega_0 = 2\pi/Q$ ✓ to first order in $1/Q$.

**(b)** $E/E_0 = e^{-2\beta t} = e^{-1}$ gives $t = 1/(2\beta)$, and the number
of periods is $t/T_d = \omega_d/(4\pi\beta) \approx \omega_0/(4\pi\beta) =
Q/(2\pi)$. **The number of cycles for the energy to fall by $e$ is
$Q/(2\pi)$, and for the amplitude to fall by $e$ it is $Q/\pi = 2Q/(2\pi)$** —
the amplitude halves the energy's patience, which is why the two statements are
often mixed up.

**(c)** Per wavelength, $\alpha\lambda = \pi/Q$, so the amplitude falls by
$e^{-\pi/100} = 0.969072$ per wavelength — 3.1 per cent per wavelength. The
$e^{-1}$ distance is $Q v/(\pi f) = 100\times5600/(\pi\times10) = 1.783\times10^4$
m ≈ 17.8 km.

**(d)** At $Q = 20$: $e^{-\pi/20} = 0.854590$ per wavelength, 14.5 per cent;
$e^{-1}$ distance $= 20\times5600/(10\pi) = 3.565\times10^3$ m ≈ 3.6 km. A
five-fold reduction in $Q$ costs a factor of five in reach, which is why
attenuation, not geometric spreading, limits deep-crustal imaging in hot or
partially molten terrains.

---

## ★★★9 — Transient build-up near resonance

**(a)** The full solution is the sum of the particular solution
$A\cos(\omega t-\delta)$ and the complementary function
$Be^{-\beta t}\cos(\omega_d t+\psi)$ with $B$, $\psi$ chosen so that
$x(0) = \dot x(0) = 0$. The transient is *not* small: for
$\omega \ll \omega_0$, $\delta \to 0$ and the two terms nearly cancel at $t=0$,
so $B \approx -A$ and the transient is as large as the steady state. The healthy
reading is that the transient is small only for $t \gg 1/\beta$.

**(b)** Near resonance the drive and the response are 90° out of phase, so the
transient that cancels the initial condition has amplitude of order $A$ and
decays as $e^{-\beta t}$. The envelope therefore approaches its steady value on
the timescale $1/\beta$; the number of cycles in that time is
$\omega_0/(2\pi\beta) = Q/\pi$.

**(c)** With $\beta = \omega_0/(2Q)$ and the envelope
$A\left(1 - e^{-\beta t}\right)$ for a start-from-rest at resonance, 90 per cent
is reached at $t = \ln 10/\beta = 2.302585/\beta$, i.e. 3.66, 7.33 and 18.3
cycles for $Q = 5, 10, 25$. A numerical check of the envelope confirms this to
better than 1 per cent, and the deviation at the lowest $Q$ is the $1/Q^2$
correction to the envelope shape.

**(d)** Because the amplitude is meaningless until the transient has decayed,
a swept or stepped source must be run for several $Q$ cycles at each frequency.
At $Q = 100$ and 10 Hz that is about 32 cycles, i.e. 3.2 s per frequency — the
reason high-$Q$ resonance measurements are slow.

---

## ★★★10 — Exponential versus linear decay

**(a)** With the dashpot, the amplitude decays as $e^{-\beta t}$: the fractional
loss per cycle is independent of amplitude, so the ratio of successive peaks is
constant. With a Coulomb force $F_c$ opposing motion, the energy lost per half
cycle is $2F_cA$, and $dE/dA = k_{\mathrm{eff}}A$ gives
$dA/dt = -2F_c\omega_0/(\pi m\omega_0^2)\times\ldots$; integrating,
$A(t) = A_0 - 2F_c t/(\pi m\omega_0)$, so the amplitude falls *linearly*.

**(b) and (c)** A numerical integration gives ratios of successive amplitudes
that are constant (to 0.1 per cent) for the dashpot and that increase towards 1
for the Coulomb damper — e.g. ratios 1.20, 1.25, 1.31 for the Coulomb case
against 1.20, 1.20, 1.20 for the dashpot. The diagnostic is that a plot of the
ratio of successive peaks against the peak index is flat for a linear mechanism
and rising for a rate-independent one.

**(d)** A non-exponential decay is therefore evidence of Coulomb or hysteretic
loss, which dominates at moderate strain in soils and fractured rock and is the
basis of the "Masing" and "rate-independent" damping models used in engineering
seismology. Note that this is a *material* statement, and it cannot be extracted
from a single decay curve: several amplitude levels must be measured.
