# Solutions — 01-03-05 Phase, Harmonics and Superposition of Oscillations

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed rather than estimated. Where a convention is adopted, it
> is stated, because phase answers are meaningless without one.

---

## ★1 — Phase to time

The governing relation is

$$\Delta t = \frac{\Delta\varphi}{\omega} = \frac{\Delta\varphi}{2\pi f},$$

with $\Delta\varphi$ in radians.

| | Phase | Frequency | Time shift |
|---|---|---|---|
| (a) | $1° = 0.017453293$ rad | 1 Hz | $\boxed{2.777778\ \text{ms}}$ |
| (b) | $45°$ | 0.1 Hz | $\boxed{1250.000\ \text{ms}} = 1.25$ s |
| (c) | $180°$ | 20 Hz | $\boxed{25.000\ \text{ms}}$ |

**Why it depends on frequency.** A phase is a fraction of a cycle. One degree is
$1/360$ of a cycle, so the time it takes is $1/360$ of a period — and the period is
$1/f$. The same phase *difference* is therefore a shorter time at higher
frequency. **Consequence for interpretation:** a "constant phase" in a broadband
record is a frequency-dependent time delay, and a constant *time* delay produces a
phase that grows linearly with frequency. Confusing the two is the single most
common error in phase-based measurements, and it is invisible in a single
narrow-band plot.

---

## ★2 — Quadrature to amplitude–phase

$$A = \sqrt{4^{2} + (-3)^{2}} = \boxed{5}, \qquad
\varphi = \operatorname{atan2}(-3, 4) = \boxed{-0.6435011\ \text{rad}}
= -36.8699° .$$

So $4\cos\omega t - 3\sin\omega t = 5\cos(\omega t + 0.6435011)$.

**The time delay.** At 2 Hz, $\omega = 4\pi = 12.566371$ rad/s, so

$$\Delta t = \frac{\varphi}{\omega} = \frac{-0.6435011}{12.566371}
= -0.0512139\ \text{s} = \boxed{-51.21\ \text{ms}} .$$

The negative sign means, in the convention
$x = A\cos(\omega t - \varphi)$, that a *negative* $\varphi$ is a **lead**: the
signal peaks 51.21 ms earlier than the pure cosine. If your code or your paper uses
$\cos(\omega t + \varphi)$ with $\varphi$ as a lead, the sign flips. **Check the
convention before quoting a sign**, because a sign error here reverses the
apparent direction of a propagation.

---

## ★3 — Beats at 2.0 and 2.2 Hz

**(a)** Carrier $= (2.0 + 2.2)/2 = \boxed{2.100000\ \text{Hz}}$. Beat period
$= 1/|f_1 - f_2| = 1/0.2 = \boxed{5.000000\ \text{s}}$.

**(b)** The sum-to-product identity gives

$$\cos(2\pi f_1 t) + \cos(2\pi f_2 t)
= 2\cos\!\left(\pi(f_1-f_2)t\right)\cos\!\left(\pi(f_1+f_2)t\right)
= 2\cos(0.2\pi t)\cos(4.2\pi t).$$

The envelope is $\left|2\cos(0.2\pi t)\right|$. It vanishes when
$0.2\pi t = \pi/2 + k\pi$, i.e.

$$t = 2.5 + 5k\ \text{s}:\qquad \boxed{t = 2.5\ \text{s and } t = 7.5\ \text{s}.}$$

The envelope is a maximum when $0.2\pi t = k\pi$, i.e. $t = 0, 5, 10, \dots$ s.

**(c)** Maximum $= \boxed{2}$, the sum of the two unit amplitudes. It cannot be
exceeded because the envelope is $2|\cos(\cdots)|$ and a cosine never exceeds 1 in
magnitude; physically, two unit sinusoids can never add to more than 2, which
happens exactly when they are in phase.

**The factor of two, stated once and for all.** The envelope *function*
$2\cos(\pi(f_1-f_2)t)$ has period $2/|f_1-f_2| = 10$ s, because its argument
advances by $2\pi$ only after that long. Its *magnitude* — what you see or hear —
returns to the same value after $1/|f_1-f_2| = 5$ s, since the cosine changes sign
in between. So:

| Quantity | Period |
|---|---|
| envelope function $2\cos(\pi(f_1-f_2)t)$ | $2/|f_1 - f_2| = 10$ s |
| loudness envelope $\left|2\cos(\pi(f_1-f_2)t)\right|$ | $1/|f_1 - f_2| = \boxed{5\ \text{s}}$ |
| spacing between cancellation times | $1/|f_1 - f_2| = 5$ s |

Whenever you quote a "beat period", say which of these you mean. The convention
in this module — and in the lesson — is the loudness period
$1/|f_1-f_2|$, which is also the interval between successive maxima.

---

## ★4 — Square-wave partial sums

**(a)**

$$f_3(t) = \frac{4}{\pi}\left[\sin(2\pi t) + \frac{1}{3}\sin(6\pi t)
+ \frac{1}{5}\sin(10\pi t)\right].$$

Note the frequencies $1$, $3$ and $5$ Hz and the amplitudes $4/\pi$, $4/(3\pi)$,
$4/(5\pi)$.

**(b)** At $t = 0.25$ s, $2\pi t = \pi/2$, $6\pi t = 3\pi/2$, $10\pi t = 5\pi/2$:

$$\sin\frac{\pi}{2} = 1, \qquad \sin\frac{3\pi}{2} = -1, \qquad \sin\frac{5\pi}{2} = 1,$$

$$f_3(0.25) = \frac{4}{\pi}\left(1 - \frac13 \cdot 1 \cdot(-1) \cdots\right)
= \frac{4}{\pi}\left(1 - \frac{1}{3} + \frac{1}{5}\right)
= \frac{4}{\pi}(0.8666667) = \boxed{1.1034743} .$$

The exact partial sum exceeds the ideal value of 1 by **0.1034743, i.e. 10.35
percent of the ideal value, or 5.17 percent of the jump of 2**. This is the
overshoot, caught early: with only three harmonics it is still large and the
limiting value (about 8.95 percent of the jump) is not yet approached.

**(c)** At $t = 0.5$ s every sine vanishes, because
$\sin(2\pi n \times 0.5) = \sin(\pi n) = 0$ for every integer $n$. So
$f_N(0.5) = 0$ for every $N$, while the ideal square wave is $-1$ there. **The
partial sums are continuous, so they must pass through the midpoint at the
discontinuity, and they always do.**

**(d)** Nothing changes: the error at $t = 0.5$ remains $-1$ forever. The series
converges pointwise everywhere *except* at the discontinuity, and at $t = 0.5$ it
converges to the midpoint 0, which is the average of the left and right limits
$+1$ and $-1$. This is the standard Dirichlet behaviour at a jump, and it is the
reason the "maximum pointwise error" column in the demonstration's table is
constant at 1.000000 for every $N$.

---

## ★★5 — Dispersion relation $\omega = 3k + 0.5k^{2}$

**(a)** At $k = 2$ rad/km: $\omega = 6 + 2 = 8$ rad/s, so

$$f = \frac{\omega}{2\pi} = 1.2732395\ \text{Hz}, \qquad
T = \frac{1}{f} = 0.7853982\ \text{s}, \qquad
\lambda = \frac{2\pi}{k} = 3.1415927\ \text{km}.$$

**(b)**

$$c = \frac{\omega}{k} = 4.000000\ \text{km/s}, \qquad
c_g = \frac{d\omega}{dk} = 3 + k = 5.000000\ \text{km/s}.$$

**(c)** $c_g > c$: the envelope travels **faster** than the carrier. A pulse
therefore advances its envelope ahead of the individual crests, and crests appear
to be created at the front of the packet and destroyed at the back as it
propagates. This is normal dispersion in the sense that $dc/dk > 0$ here
($c = 3 + 0.5k$ increases with $k$), and it means that higher-frequency components
travel faster — the opposite of the usual surface-wave case, where longer periods
generally travel faster in a layered medium and $c_g < c$.

**(d)** At $k = 6$ rad/km: $\omega = 18 + 18 = 36$ rad/s, so
$f = 5.7295779$ Hz, $T = 0.1745329$ s, $\lambda = 1.0471976$ km, $c = 6.000000$
km/s and $c_g = 9.000000$ km/s. The absolute gap $c_g - c = 3$ km/s at both
wavenumbers, but the *relative* gap has fallen from
$(5-4)/4 = 25$ percent to $(9-6)/6 = 50$ percent — it has grown. **Relative
dispersion grows with wavenumber for this model**, which is why a broadband pulse
distorts more as it travels and why dispersion is easier to measure at short
wavelengths *if* the medium supports them.

**Sanity check on the units.** $\omega/k$ has units of (rad/s)/(rad/km) = km/s ✓,
and $d\omega/dk$ likewise. The radian is dimensionless, so the rad cancels; had the
relation been written for ordinary frequency $f(k)$ in hertz, the phase velocity
would still be $f\lambda$, but $c_g = df/d(k/2\pi)$ — a factor of $2\pi$ wrong if
you forget the radian. **Write dispersion relations in $\omega(k)$ and not in
$f(k)$.**

---

## ★★6 — The M2–S2 beat

**(a)**

$$f_{M2} = \frac{1}{12.4206012} = 0.0805114007\ \text{cycles/h}, \qquad
f_{S2} = \frac{1}{12} = 0.0833333333\ \text{cycles/h}.$$

**(b)** Difference frequency $= 0.0028219326$ cycles/h, so

$$\text{beat period} = \frac{1}{0.0028219326} = 354.3670689\ \text{h}
= \boxed{14.76529454\ \text{days}} .$$

**(c)** In phase at $t = 0$, and again every beat period:

$$t = 354.367\ \text{h} \approx 14.7653\ \text{days}, \qquad
t = 708.734\ \text{h} \approx 29.5306\ \text{days}.$$

The second interval is multiplicative, not additive in the frequencies, and it is
worth noticing that in the two-constituent model the spring tides recur exactly
every 14.7653 days.

**(d)** A real tide gauge records more constituents than these two. K1 and O1 are
diurnal and do not beat at the same rate; P1 and N2 sit close to S2 and M2
respectively and modulate them. In addition, the astronomical forcing itself is
not two clean sinusoids: the lunar orbital elements vary slowly, so the
"constants" M2 and S2 have slowly varying amplitudes over decades. **The 14.77
days is a model result, and it should be quoted as one.** Observed neap-to-spring
intervals at a real station vary by a fraction of a day, and the variation is
itself information about the other constituents.

---

## ★★7 — Phase differences and station separation

**(a)** $\Delta t = (60/360) \times 12\ \text{s}
= \boxed{2.000\ \text{s}}$.

**(b)** At $c = 3.0$ km/s, the separation is
$\Delta x = c\,\Delta t = 3.0 \times 2.0 = \boxed{6.0\ \text{km} }$ (in the sense
implied by the sign of the phase difference).

**(c)** $300°$: $\Delta t = (300/360)\times12 = 10.000$ s, giving
$c\Delta t = 30.0$ km if taken literally. It is **not** five times the $60°$ answer
in any meaningful sense, because $300°$ and $-60°$ are the same phase difference:
the station that leads by $300°$ lags by $60°$, and the two interpretations give
6 km and 30 km. Which is correct depends on which station is closer to the source —
information the phases alone do not contain.

The general ambiguity: a measured phase difference fixes the separation only
**modulo one wavelength**, $\lambda = cT = 3.0 \times 12 = 36$ km. Without
additional information (a third station, an independent azimuth, or an assumption
that the stations are closer than half a wavelength apart) you cannot convert phase
to distance. **This is why a two-station dispersion measurement yields a phase
*velocity*, not a distance**, and why it is written as a function of period rather
than position.

**(d)** $420° = 360° + 60°$ is the same phase difference as $60°$, since phase is
defined modulo $2\pi$. Report the $60°$ result and say explicitly that the measured
value wrapped: reporting "420°" invites a reader to divide it by 360 and conclude
something about a second cycle that the data do not support.

---

## ★★8 — Interference and cancellation

**(a)** With equal amplitudes $A$ and a phase difference $\pi$:

$$A\cos(\omega t) + A\cos(\omega t - \pi) = A\cos\omega t - A\cos\omega t = 0 .$$

**(b)** For a phase difference of $179°$, use the sum-to-product identity
$\cos\alpha + \cos\beta = 2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$
with $\alpha = \omega t$ and $\beta = \omega t - 179°$:

$$2A\cos\!\left(\omega t - \frac{179°}{2}\right)\cos\!\left(\frac{179°}{2}\right)
= 2A\cos(\omega t - 89.5°) \times 0.00872654 .$$

With $A = 1$ the residual amplitude is

$$2 \times 0.00872654 = \boxed{0.0174531},$$

i.e. **1.75 percent of a single amplitude**, or 0.87 percent of the 2 that
perfect interference would give.

**Why this number matters.** A one-degree error in a measured phase difference
turns a perfect null into a residual of nearly 2 percent of the amplitude. Phase
measurements are not "roughly right": a null is a sharp test, and near a null the
sensitivity to the phase is maximal. This is the same conditioning phenomenon as
`arcsin` near its branch points and as the dip-azimuth inversion of
[01-03-01](./01-angles-and-triangles-solutions.md) when the bed is nearly
horizontal.

**(c)** An analyst reporting only amplitudes would report $2A$ in both cases —
the sum of the amplitudes, as though the two contributions added in phase. In (a)
the truth is zero and in (b) it is 1.75 percent of $A$. **An amplitude-only
pipeline cannot distinguish perfect cancellation from perfect reinforcement**,
which is precisely the information a stacked image needs: whether two events add or
cancel determines whether a reflector appears in the section. This is why
processing codes carry complex-valued traces and why a "polarity check" is a real
step, not a formality.

---

## ★★★9 — The Gibbs phenomenon, measured

**(a)–(d)** The module's demonstration implements the partial sum and reports:

```text
 harmonics      rms error    max |error|   peak overshoot (percent of jump)
         1       0.435238       1.000000                            13.662
         3       0.258744       1.000000                             9.418
         5       0.201002       1.000000                             9.116
        11       0.135735       1.000000                             8.983
        51       0.063571       1.000000                             8.951
       201       0.035758       1.000000                             8.949
```

The overshoot column converges to about **8.949 percent of the jump**, and it is
*not* going to zero: between 51 and 201 harmonics it moves by 0.002 percentage
points.

**(c)** The peak is located within about $1/N$ of the discontinuity — for $N = 201$
that is a window of about $2.5\times10^{-3}$ in $t$, while a fixed 2000-sample grid
over one period has spacing $5\times10^{-4}$ and *can* find the peak, but a coarser
grid cannot. The demonstration's earlier version used a fixed grid and reported an
apparent overshoot that *fell* from 1.1786 at $N = 51$ to 1.1429 at $N = 201$,
because the grid missed the narrowing peak. **That is a measurement artefact
produced entirely by the sampling, and it looked like a physical convergence.**
Always refine the search grid as $N$ grows, and check that the reported extremum is
not grid-limited by halving the spacing and confirming stability.

**(d)** Limiting overshoot $\approx 8.949$ percent of the jump at $N = 201$ and
still decreasing in the fourth decimal. A fixed grid would have suggested 7.14
percent (the value quoted by the coarse-grid version at $N = 201$), i.e. an
underestimate of about 20 percent. **The difference between 7.14 and 8.95 percent
is not a rounding question; it is the difference between concluding that the
overshoot decays and concluding that it does not.**

**(e)** The maximum pointwise error stays at exactly 1.000000 because the partial
sums are continuous and the ideal function is discontinuous by 2. At the jump the
partial sum must take the midpoint value, and the ideal value differs from it by
half the jump. Adding harmonics makes the transition steeper but never removes it.
For a band-limited representation of a sharp arrival — a filtered first break, a
thin bed in a well log, a topographic scarp in a sampled DEM — this means the
ringing adjacent to the feature has a **fixed relative amplitude set by the band**,
not by the number of samples or the care of the processing. It is predictable: the
overshoot is about 9 percent of the step.

**(f)** Limits of the result:

- The limiting overshoot percentage is a property of a **step discontinuity** in a
  periodic function. A continuous function with a discontinuous derivative has a
  different (smaller) ringing law.
- The *rms* error column depends on the sampling grid and on the measure; it is not
  a universal constant and should not be quoted as one.
- The overshoot is platform-independent to many digits (it is a mathematical limit)
  but the *convergence rate* observed at finite $N$ depends on how the grid is
  chosen and on floating-point summation order at large $N$.
- Nothing here says the ringing is "unphysical": for a real band-limited instrument,
  the ringing *is* the correct response to a step input, and it appears in the data
  for the same reason.

---

## ★★★10 — Phase and group velocity, measured

**(a)** Sum of two nearby components:

$$\cos[(k_0-dk)x - (\omega_0-d\omega)t]
+ \cos[(k_0+dk)x - (\omega_0+d\omega)t]
= 2\underbrace{\cos(dk\,x - d\omega\,t)}_{\text{envelope}}
\ \underbrace{\cos(k_0x - \omega_0t)}_{\text{carrier}} .$$

The envelope's phase is $dk\,x - d\omega\,t$, whose zero set moves at
$c_g = d\omega/dk$; the carrier's phase moves at $c = \omega_0/k_0$.

**(b)–(c)** With $k_0 = 2$, $\omega_0 = 6$, $dk = 0.1$, $d\omega = 0.35$, tracking
the envelope peak on a fine spatial grid at $t = 0$ and $t = 1$ s gives peak
positions 0.0000 and 3.5000, i.e. a measured speed of

$$c_g^{\text{meas}} = 3.500000, \qquad d\omega/dk = 3.500000 .$$

Agreement to seven digits.

**(d)** The carrier's zero crossings satisfy
$k_0x - \omega_0t = \pi/2 + m\pi$, i.e.
$x = (\pi/2 + m\pi + \omega_0 t)/k_0$. Tracking the crossing with $m = 0$:

- $t = 0$ s: $x = 0.7853982$;
- $t = 0.5$ s: $x = 2.2853982$;

an increment of $1.500000$ units in $0.5$ s, so

$$c^{\text{meas}} = \frac{1.500000}{0.5} = 3.000000
\quad\text{against}\quad \frac{\omega_0}{k_0} = 3.000000 .$$

Similarly, the envelope measurement in (c) tracked a peak from $x = 0$ to
$x = 3.5000$ over one second, giving $3.500000$ against
$d\omega/dk = 3.500000$ ✓.

**A caution about crossing counts.** At a fixed time the carrier's zero crossings
are spaced $\pi/k_0 = 1.5708$ units apart, which is **half** the wavelength
$\lambda = 2\pi/k_0 = 3.1416$: a cosine crosses zero twice per cycle. Tracking the
*position of one crossing over time* gives the phase velocity correctly, as above,
but inferring the wavelength by counting crossings per unit length without
accounting for the double crossing is a reliable way to be a factor of two out. In
a real dispersion measurement the analogous error — counting extrema instead of
like-sense features, or mis-specifying the branch of the phase — is one of the most
common ways a phase velocity comes out wrong by an integer factor.

**(e)** Reducing $dk$ by a factor of ten while keeping $d\omega/dk$ fixed leaves the
measured envelope speed at 3.500000 and the carrier speed at 3.000000: the
*values* do not move. What changes is the shape: a smaller $dk$ widens the envelope
in $x$ by a factor of ten, so its peak is flatter and its position is determined
**less** precisely. The uncertainty in the group velocity therefore *grows* as
$dk$ shrinks, even though the two-wave construction is more nearly "monochromatic".

That tension is real and unavoidable: a narrowband measurement is well-localised in
frequency and badly localised in space, and vice versa. If instead you hold
$d\omega$ fixed and shrink $dk$, then $d\omega/dk$ grows without bound, and the
two-wave model is no longer a small perturbation — you would be measuring the slope
of $\omega(k)$ over a finite interval and attributing it to a point. **State the
bandwidth whenever you quote a group velocity.**

**(f)** The identification $c_g = d\omega/dk$ is the **stationary-phase**
approximation for a narrowband packet: it is exact for a superposition of two
components that are close together, and it becomes the correct envelope speed for a
general superposition only when the spectrum is narrow enough that
$\omega(k)$ is locally linear over the band. When the band is wide, the envelope
spreads (dispersion broadening), the group velocity becomes frequency-dependent, and
the single number $d\omega/dk$ describes only the *arrival* of the dominant
frequency rather than the packet as a whole. In an absorbing medium the relation
becomes complex and $d\omega/dk$ acquires an imaginary part, whose interpretation is
attenuation rather than delay — one of the reasons seismologists work with *group
delay* $\tau(\omega) = -d\varphi/d\omega$ measured directly on the phase spectrum
rather than with a velocity derived from a model.
