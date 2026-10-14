# Solutions — 04-07-01 Earthquake Hazard and Ground Motion

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Moment and magnitude

**(a)** $A = 40\times10^3 \times 15\times10^3 = 6.00\times10^8$ m², so

$$M_0 = 3.0\times10^{10} \times 6.00\times10^8 \times 1.5 = 2.70\times10^{19}\ \mathrm{N\,m}
= 2.70\times10^{26}\ \mathrm{dyn\,cm}.$$

**(b)** $\log_{10}(2.70\times10^{26}) = 26.4314$, so the dyn cm form gives
$M_\mathrm{w} = \tfrac23(26.4314) - 10.7 = 6.9209$. The converted offset gives
$6.9209$ as well, and the usual $-6.07$ gives $6.8842$. The difference is
$0.0367$ magnitude units, i.e. a factor of $1.135$ in $M_0$ — the offsets were
rounded independently, and both forms are found in the literature.

**(c)** $\log_{10}E = 1.5 \times 6.9209 + 4.8 = 15.1814$, so
$E = 1.52\times10^{15}$ J.

**(d)** One magnitude unit is $10^{1.5} = 31.6$ in energy. That the energy grows
by 31.6 while the moment grows by only $10^{1.5\times(2/3)}=10$, i.e. by a factor
of 10, is the statement that the ratio $E/M_0$ is not constant.

---

## ★2 — A layered site

**(a)** $Z_1 = 1700 \times 180 = 3.06\times10^5$ and
$Z_2 = 2600 \times 900 = 2.34\times10^6$ kg m⁻² s⁻¹, so
$Z_2/Z_1 = 7.647$.

**(b)** $f_0 = v_S/(4H) = 180/120 = 1.50$ Hz.

**(c)** $|T|_\mathrm{max} = Z_2/Z_1 = 7.65$ relative to the rock outcrop. There
is no factor of 2 because the free-surface doubling applies to the soil surface
and to the rock outcrop alike, and therefore cancels in the ratio.

**(d)** Relative to the *incident* wave in the rock the soil surface response is
$2 \times 7.65 = 15.3$ at resonance, because the rock outcrop motion is itself
$2\times$ the incident wave. The two numbers differ by exactly the factor of 2,
and they answer different questions.

---

## ★3 — Attenuation

**(a)** $\pi f/(Qv) = \pi\times2/(250\times3400) = 7.392\times10^{-6}$ m⁻¹.

**(b)** Over 50 km the anelastic factor is
$\exp(-7.392\times10^{-6}\times5\times10^4) = e^{-0.3696} = 0.691$.

**(c)** Body wave: $(10/60)\times0.691 = 0.115$. Surface wave:
$\sqrt{10/60}\times0.691 = 0.282$.

**(d)** $0.282/0.115 = 2.449 = \sqrt{6} = \sqrt{r/r_0}$. The ratio is exactly the
geometric term alone, because the anelastic factor is common to both: this is
why the difference between body and surface waves at regional distance is a
*spreading* effect, not an attenuation effect.

---

## ★4 — Oscillator and probability

**(a)** $1/(2\zeta) = 1/0.1 = 10$.

**(b)** $\lambda = 1/475 = 2.105\times10^{-3}$ a⁻¹, and
$P = 1 - e^{-2.105\times10^{-3}\times50} = 0.0999$, i.e. 10 per cent.

**(c)** $P = 1 - e^{-50/2475} = 0.0200$, i.e. 2 per cent. The two return periods
and the two exposure probabilities are the pair used in most design codes, and
they are related by (13), not by any property of the earthquakes.

**(d)** (a) is computed from the model and the chosen $\zeta$; the 475-year
return period in (b) is a *model input* that came from a hazard analysis built
on a recurrence model and a ground-motion model. The Poisson conversion is
arithmetic; the return period is not.

---

## ★5 — The transfer function

**(a)** Numerical maximum $|T| = 5.555556$ at $f = 13.0000$ Hz; closed form
$Z_2/Z_1 = 5.555556$; relative difference $3.061\times10^{-10}$.

**(b)** At an exact resonance $\cos(k_1H)$ is zero only up to floating-point
rounding (about $10^{-16}$), so a scan that lands exactly on $f_0$ measures
arithmetic noise at the 5th decimal rather than the physics. Offsetting the grid
means the reported maximum is slightly *below* the closed form, which is the
honest result: the maximum is approached, and the closed form is the limit.

**(c)** At $f = 2f_0$, $k_1H = \pi$, so $\cos = -1$ and $\sin = 0$ and
$|T| = 1.0000$: the second harmonic has a node at the interface because the round
trip is one full wavelength. The destructive interference is exact, which is why
the transfer function has deep notches between its peaks and why a two-frequency
ground motion can excite one and not the other.

**(d)** With $v_2 = 1600$ m s⁻¹ the impedance becomes
$2600\times1600 = 4.16\times10^6$, so $Z_2/Z_1$ rises from 5.556 to
$4.16\times10^6/3.6\times10^5 = 11.56$. $f_0$ is unchanged at 1.0000 Hz because
it depends only on the *layer* ($v_1$ and $H$). The peak amplification doubled,
the tuning did not move: this is the clean separation between the two parameters
that makes a site-response measurement diagnostic.

---

## ★6 — The oscillator and the spectrum

**(a)** The relative differences between $\omega_0^2|x|_\mathrm{max}$ and
$1/(2\zeta) = 10$ are $5.37\times10^{-5}$, $1.32\times10^{-5}$ and
$3.30\times10^{-6}$ for $T = 0.5$, $1.0$ and $2.0$ s. The residual is the
start-up transient, which decays as $e^{-\zeta\omega t}$.

**(b)** Peak spectral acceleration $2.3911$ m s⁻² at $T = 0.40$ s, against a
peak ground acceleration of $1.0000$ m s⁻²: $\mathrm{Sa}/\mathrm{PGA} = 2.391$.

**(c)** $1/(2\zeta)$ is the *steady-state* response to a harmonic input at
exactly the natural frequency. The Ricker pulse contains only a few cycles of
energy near 2 Hz, so the oscillator is driven for a time comparable with its
build-up time $1/(\zeta\omega_0)$ — about 3 cycles here — and never reaches
equilibrium. A short input gives a few times the input; a long harmonic input
gives $1/(2\zeta)$ times the input.

**(d)** Halving $\zeta$ to 0.02 raises the steady-state factor to 25, a factor of
2.5. The measured peak moves from $2.3911$ to $2.7152$, an increase of only
13.6 per cent, and stays at $T = 0.40$ s. The reason is (c): the response is
limited by the input duration, so it scales roughly as the number of driving
cycles rather than as the damping, and a factor of 2.5 in the asymptotic
amplification converts into a small change in a transient response. This is the
single most useful thing to know about damping: it matters enormously for a
sustained harmonic input and rather little for a short pulse.

---

## ★7 — Recurrence, and which earthquakes dominate

**(a)** $N(\ge6) = 10^{4-6} = 0.01$ a⁻¹, so
$P = 1 - e^{-0.01\times50} = 0.393$.

**(b)**

| Bin | Rate (a⁻¹) |
|---|---|
| 4.0–4.5 | $0.6838$ |
| 4.5–5.0 | $0.2162$ |
| 5.0–5.5 | $0.0684$ |
| 5.5–6.0 | $0.0216$ |
| 6.0–6.5 | $0.00684$ |
| 6.5–7.0 | $0.00216$ |
| 7.0–7.5 | $0.000684$ |
| 7.5–8.0 | $0.000216$ |

Each bin's rate is $10^{4-M}(1 - 10^{-0.5}) = 0.6838\times10^{4-M}$.

**(c)** With $A \propto 10^{0.75M}$ the shares are 27.8, 20.8, 15.6, 11.7, 8.8,
6.6, 4.9 and 3.7 per cent. The **4.0–4.5 bin dominates**, and the contribution
decays by a factor of $10^{0.25} = 1.78$ per half magnitude. No single bin
dominates overwhelmingly; the sum is spread over the 4.0–6.0 range.

**(d)** With $A \propto 10^{0.5M}$ the shares are 44.2, 24.9, 14.0, 7.9, 4.4,
2.5, 1.4 and 0.8 per cent. The same bin dominates, more strongly, with a decay
of $10^{0.125} = 1.33$ per half magnitude. The conclusion does not change: the
hazard is accumulated by moderate events because the rate grows tenfold per
magnitude unit while the amplitude grows by less than a factor of ten.

**(e)** The amplitude is assumed to scale as a fixed power of the radiated
energy, which assumes the source spectrum shape and the motion duration do not
change with magnitude. Both do: a larger earthquake radiates its energy over a
longer time and at lower frequency, so the high-frequency amplitude grows
*more slowly* than $\sqrt{E}$. The assumption therefore overstates the amplitude
of the large events, and the true dominance of moderate events is stronger than
the table suggests.

---

## ★★★8 — Site response and its uncertainty

**(a)** With the impedance ratio updated consistently:

| $v_S$ (m s⁻¹) | $f_0$ (Hz) | $Z_2/Z_1$ | $\vert T(2\ \mathrm{Hz})\vert$ |
|---|---|---|---|
| 144 | 1.20 | 9.56 | 1.153 |
| 180 | 1.50 | 7.65 | 1.951 |
| 216 | 1.80 | 6.37 | 4.302 |

**(b)** The amplification at 2 Hz spans 1.15 to 4.30 — a factor of 3.7 — for a
$\pm20$ per cent uncertainty in the single most important parameter, so a site
amplification quoted without its $v_S$ uncertainty is a number without an error
bar in a quantity whose error bar is larger than most of the effects being
studied.

**(c)** The building period is 0.5 s, i.e. 2 Hz. Only the $v_S = 216$ m s⁻¹
model puts $f_0 = 1.80$ Hz anywhere near the building's 2 Hz, and there
$|T(2\ \mathrm{Hz})| = 4.30$ against a peak of 6.37 — the building sits on the
flank of the resonance and is excited to about two thirds of the site maximum.
In the $v_S = 144$ m s⁻¹ model $f_0 = 1.20$ Hz, so 2 Hz is $1.67f_0$ and
$|T| = 1.153$ against a peak of 9.56: the building is a factor of 8.3 below the
site's own maximum amplification. The same building is therefore resonantly
excited or nearly immune depending on a parameter known to $\pm20$ per cent,
which is the practical content of this exercise.

**(d)** A two-dimensional basin model would add: (i) lateral focusing and
defocusing by the basin geometry, which can produce amplifications larger than
$Z_2/Z_1$; (ii) the generation of surface waves at the basin edges and their
trapping inside the basin, which lengthens the shaking and can add a second peak
at a lower frequency set by the basin width; (iii) the interference between the
direct vertical wavefield and the edge-generated arrivals, which makes the
response strongly dependent on *where* in the basin the site is; and (iv) the
coupling of horizontal and vertical motion. None of these appear in a
vertical-incidence single-column calculation, and (ii) is often the largest
correction to a ground-motion estimate in a deep basin.

---

## ★★★9 — A velocity gradient

**(a)** In a sharp two-layer model the whole impedance contrast is concentrated
at one interface, so the resonances are sharp and the peak is $Z_2/Z_1$. A
gradient replaces it with a continuum of weak reflections distributed over the
column: each is small, their round trips arrive at slightly different times, and
the coherent sum is both smaller and spread over a band of frequencies. The peak
amplification is therefore lower and the resonance broader, which is why a
compacted soil column responds less violently than the impedance ratio of its
top and bottom would suggest.

**(b)** With $v_S$ increasing linearly by $180$ m s⁻¹ over 30 m, the midpoint
velocity of layer $i$ (from the surface, thickness 3 m) is
$v_i = 129, 147, \dots, 291$ m s⁻¹. The one-way travel time is

$$\tau = \sum_{i=1}^{10}\frac{3}{v_i} = 0.15258\ \mathrm{s},$$

so $f_0 = 1/(4\tau) = 1.638$ Hz.

**(c)** The arithmetic mean is $\bar v = 210$ m s⁻¹ and
$\bar v/(4H) = 210/120 = 1.75$ Hz, which is **6.8 per cent higher** than the
travel-time answer. The reason is that $f_0$ depends on the travel time, hence
on the *harmonic* mean of the velocity, which is always less than or equal to the
arithmetic mean and here is $30/0.15258 = 196.6$ m s⁻¹. Use the travel time, not
the average velocity.

**(d)** A horizontal-to-vertical spectral ratio from ambient vibration measures
the frequency at which the site amplifies, which is exactly the quantity
predicted in (b), so it can test the predicted $f_0$ and the presence of a
velocity contrast. It cannot measure the velocity, the thickness, the impedance
contrast, or the amplification factor: the ratio is a *shape*, and mapping it to
a velocity profile requires a model — usually the very one-dimensional model
being tested.
