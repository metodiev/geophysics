# Solutions — 19-08-01 Simulating a 2-D/3-D Seismic Wavefield

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [01 Simulating a 2-D/3-D Seismic Wavefield](../01-simulate-seismic-wavefield.md).

---

## ★1 — Group velocity at 6 points per wavelength

$\theta = 2\pi/6 = 1.04720$ rad, so $\theta/2 = 0.52360$ and

$$c_g/c = \frac{\cos(0.52360)}{\sqrt{1 - 0.25\sin^{2}(0.52360)}}
= \frac{0.86603}{\sqrt{1 - 0.25(0.25)}} = \frac{0.86603}{\sqrt{0.93750}}
= \frac{0.86603}{0.96825} = 0.89443 .$$

The numerical wave travels at $89.4$ per cent of the medium velocity: **slower**,
and $10.6$ per cent too slow at this coarse resolution. This is the value the
demonstration's "analytic" column prints.

---

## ★2 — Grid design and stability

$$\Delta x = \frac{c}{f\,\mathrm{ppw}} = \frac{4000}{25\times10} = 16\ \mathrm{m},
\qquad
\Delta t = \frac{C\Delta x}{c} = \frac{0.6\times16}{4000} = 2.4\ \mathrm{ms}.$$

The exact 2-D limit for the five-point Laplacian is $C \le 1/\sqrt{2} = 0.70711$,
and $0.6 < 0.70711$: stable, with $15$ per cent margin in the Courant number. Note
that the margin in *time step* is the same $15$ per cent, because $C$ is linear in
$\Delta t$; and note that $\Delta t$ must also be checked against the source
wavelet and the receiver sampling, which are separate requirements.

---

## ★3 — Group versus phase

A travel-time pick locates the *envelope* of a wave packet, and the envelope
travels at the group velocity $\mathrm{d}\omega/\mathrm{d}k$, not at the phase
velocity $\omega/k$. In a dispersive scheme the two differ: at 8 points per
wavelength the demonstration's phase speed is about $1$ per cent below $c$ while the
group speed is about $6$ per cent below (from the table, $c_g/c = 0.94127$ at
$\theta = \pi/4$); the difference is itself a measurable property of the scheme and
grows with $\theta$.

---

## ★4 — Depth error at 8 points per wavelength

The measured velocity is $0.95808c$, so the medium velocity overestimates the
propagation speed; converting a measured two-way time to depth with $c$ places the
reflector too deep:

$$z_{\text{apparent}} = \frac{3.000}{0.95808} = 3.131\ \mathrm{km},$$

i.e. an error of $+131$ m, about $4.4$ per cent. The sign is positive: a scheme
that propagates waves too slowly makes reflectors appear too deep when depth is
computed with the true velocity. The correction is to use an effective velocity
equal to the numerical group velocity, or to refine the grid until the error is
below the stated depth tolerance.

---

## ★5 — 3-D cost

$$\Delta x = \frac{3500}{20\times10} = 17.5\ \mathrm{m},
\qquad \Delta t = \frac{0.5\times17.5}{3500} = 2.5\ \mathrm{ms}.$$

Node counts: $15000/17.5 = 857$, $15000/17.5 = 857$, $8000/17.5 = 457$ →
$857\times857\times457 = 3.36\times10^{8}$ nodes. Working set:
$3.36\times10^{8}\times7\times8 = 1.88\times10^{10}$ bytes $\approx 18.8$ GB, which
fits a large node but not a desktop. A $2.5$ s record needs $1000$ time steps, each
moving about $19$ GB of data, i.e. $1.9\times10^{13}$ bytes of traffic — the
memory-bandwidth argument of the lesson in numbers.

---

## ★6 — Anisotropy as a travel-time error

A wave crossing $5$ km along the fast direction arrives
$5000\times0.01312 = 65.6$ m "early" relative to the slow direction, i.e.
$65.6/3500\ \mathrm{m\,s^{-1}}$ scaled by the medium velocity gives a time
difference of about $18.7$ ms if the medium velocity is $3500$ m/s. A
shear-wave-splitting measurement resolves delays of order $0.1$ s
($100$ ms), so an $18.7$ ms numerical contribution is around $19$ per cent of the
signal: **not negligible, and it must be shown to be subtracted or resolved to
below that level before real anisotropy is claimed.** Refining from $8$ to $32$
points per wavelength reduces it by a factor of $16$ to $1.2$ ms.

---

## ★7 — Benchmark for an absorbing boundary

**Geometry.** Homogeneous medium, a point source near the centre, receivers on a
line between the source and the boundary, a run long enough that the direct arrival
has passed the receivers and the boundary reflection would have returned.

**Observable.** The peak amplitude of the boundary reflection divided by the peak
amplitude of the direct arrival at the furthest receiver, measured in a time window
after the direct arrival.

**The target signal level and threshold.** If the interior scheme is verified, the
only energy in that window is the reflection plus dispersion tails; the dispersion
tails are already quantified by the group-velocity measurement, so the test is:
reflection amplitude $\le \tau$ with $\tau = 0.01$ (i.e. $1$ per cent), well below
the $5$ per cent defect to be detected. Include a second run with a larger domain,
so that the reflection arrives later: if the window amplitude does not fall
accordingly, the defect is in the boundary, not in the interior.

**The test fails** if the window amplitude exceeds $\tau$, or if the amplitude does
not scale with domain size as a boundary reflection must.

---

## ★8 — The two-dimensional Courant limit

The five-point Laplacian has the symbol
$-4\left[\sin^{2}(k_xh/2) + \sin^{2}(k_yh/2)\right]/h^{2}$, whose magnitude is
maximal when both sines equal $1$, i.e. at $k_x = k_y = \pi/h$. The leapfrog update
is stable only while $C^{2}$ times that magnitude, converted to the same units, does
not exceed the time-difference operator's maximum of $4/\Delta t^{2}$:

$$C^{2}\frac{4}{h^{2}}\times2 \le \frac{4}{\Delta t^{2}}c^{2}
\quad\Longrightarrow\quad 2C^{2} \le 1
\quad\Longrightarrow\quad C \le \frac{1}{\sqrt{2}} .$$

The limit is set by the **corner wavenumbers**, which are grid-scale modes with
$k_x$ and $k_y$ both at Nyquist: they are the modes with the most negative discrete
Laplacian eigenvalue, so they are the most violently amplified. Nothing about the
medium enters except through $c$; the factor $1/\sqrt{2}$ is a property of the
stencil's geometry and disappears if the stencil is changed (a nine-point Laplacian
has a less restrictive limit).
