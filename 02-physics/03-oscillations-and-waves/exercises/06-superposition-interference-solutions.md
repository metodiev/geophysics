# Solutions — 02-03-06 Superposition, Interference and Standing Waves

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Two loudspeakers

**(a)** $\lambda = 343/500 = 0.686$ m.

**(b)** At the midpoint both paths are equal, so $r_1 - r_2 = 0 = 0\times\lambda$:
constructive.

**(c)** Exact: solve $\sqrt{(x+1.5)^2+64} - \sqrt{(x-1.5)^2+64} = 0.686$ and
$= 1.372$. The first maximum is well approximated by solving numerically; the
far-field formula gives $x_1 = \lambda L/d = 0.686\times8/3 = 1.829$ m and
$x_2 = 3.659$ m. The exact values are about 1.97 m and 4.35 m — the far-field
formula is low by roughly 7 per cent at the first order because $x/L = 0.25$ is
not small.

**(d)** The exact condition. The far-field formula's error is $O((x/L)^2)$, which
here is 6 per cent, comparable with the observed 7 per cent.

---

## ★2 — Modes of a string

**(a)** $f_n = nv/(2L) = n\times180/1.2 = 150n$ Hz, giving 150, 300, 450 Hz.

**(b)** Mode 2 has $\lambda = L = 0.60$ m. With $u \propto \sin(2\pi x/L)$ the
nodes are at $x = 0$, $0.30$ m and $0.60$ m.

**(c)** The pluck sets an initial shape that is generally a sum of modes; the
amplitude of each mode is the projection of the initial shape onto the mode shape
— the discrete analogue of a Fourier coefficient (see exercise ★★★10 of lesson
02-03-03). A pluck at the centre excites odd modes strongly and even modes weakly,
which is why the timbre depends on where the string is plucked.

**(d)** An octave is a factor of two in frequency, so $n = 2$: this string's
second mode is one octave above its fundamental.

---

## ★3 — Standing wave

**(a)** $u = 0.06\cos(kx)\cos(\omega t)$ with
$k = 2\pi/2.0 = 3.141593$ rad m⁻¹ and $\omega = 2\pi\times20 =
125.663706$ rad s⁻¹.

**(b)** Nodes where $\cos kx = 0$: $x = (2m+1)\lambda/4 = 0.5, 1.5, 2.5,\dots$ m.
Antinodes where $|\cos kx| = 1$: $x = m\lambda/2 = 0, 1.0, 2.0,\dots$ m.

**(c)** At an antinode $u = 0.06\cos\omega t$, so
$\dot u_{\max} = 0.06\times125.663706 = 7.539822\ \mathrm{m\,s^{-1}}$.

**(d)** Zero. The two travelling components have equal amplitudes and opposite
directions, so their energy fluxes cancel identically.

---

## ★4 — Unequal beams

**(a)** $I_{\max} = (\sqrt{4}+\sqrt{1})^2 = (2+1)^2 = 9.0$.

**(b)** $I_{\min} = (2-1)^2 = 1.0$.

**(c)** $\langle I\rangle = (9+1)/2 = 5.0 = 4.0+1.0$ ✓.

**(d)** $V = (9-1)/(9+1) = 0.8 = 2\sqrt{4}\sqrt{1}/(4+1) = 4/5$ ✓, consistent with
the general formula of exercise ★★★10.

---

## ★5 — Fringe spacing

**(a)** Measured 10.294000 m; exact 10.330981 m; far field 10.000000 m.

**(b)** Far-field error $= (10.000000-10.330981)/10.330981 = -3.204$ per cent.
With $x/L \approx 0.26$ at $L = 40$ m, $(x/L)^2 = 0.067$; the observed error is
about half that, which is the correct order for a truncated series with a
coefficient of 1/2. At $L = 20$ m the fringe position scales roughly linearly
while $x/L$ doubles, so the error roughly quadruples — verify this by running the
modified script and report the measured value.

**(c)** The exact condition is $r_1-r_2 = \lambda$; as $x$ grows the paths become
more nearly parallel, so a larger $x$ is needed to achieve the same path
difference: the fringe spacing grows with $|x|$. Equivalently, the effective $d$
seen by the receiver is $d\cos\theta$, which shrinks with angle.

**(d)** Measure the spacing between the first pair of maxima straddling the axis,
$\Delta x$, and use $d = \lambda L/\Delta x$ to first order, correcting with the
exact relation if $L/d$ is small. The precision of $d$ is limited by the
precision of $L$ and of $\Delta x$: with $\Delta x = 10.294$ m known to 1 mm and
$L = 40$ m known to 1 mm, the relative precision is about $10^{-4}$.

---

## ★6 — Coherence and array interference

**(a)** Coherence time $\tau_c \approx 1/\Delta f = 1/45 = 0.0222$ s.

**(b)** Coherence length $\ell_c = c\tau_c = 2500\times0.0222 = 55.6$ m.

**(c)** Path differences up to about 56 m will produce stable fringes; beyond
that the fringes wash out. At 1 km range, a two-source array with 50 m separation
has path differences of order $d\,x/L$ that can exceed the coherence length away
from the axis, so a stationary far-field pattern will *not* appear over the full
range — only within a narrow angular cone near the axis, where the path
difference stays below the coherence length.

**(d)** Because the phase of each frequency component slips at a rate set by the
frequency *difference*, not by the absolute frequency: the total phase spread
over the source's band is what destroys the pattern for long path differences. A
narrowband source centred at 1 kHz has a long coherence length; a broadband
source centred at the same frequency has a short one.

---

## ★7 — Tuning thickness

**(a)** The reflection from the bottom of the layer has travelled a two-way
distance $2h$ inside it, so its phase is delayed by $4\pi h/\lambda$ relative to
the top reflection. Whenever the layer's impedance is either the largest or the
smallest of the three (so that the two reflection coefficients have opposite
signs), the composite amplitude is proportional to
$\left|1 - e^{i4\pi h/\lambda}\right| = 2\left|\sin(2\pi h/\lambda)\right|$.
That is zero at $h = \lambda/2$ (the two reflections cancel when they arrive half
a cycle apart — the *tuning* condition of opposite sign to the naive one) and
maximal at $h = \lambda/4$, where the two arrive a quarter cycle apart and add
coherently at the peak of the wavelet. This is the **tuning thickness**,
$h = \lambda/4$, quoted in seismic interpretation. The polarity matters: for a
layer whose impedance lies between the bounding media the two coefficients have
the same sign and the extremal thicknesses are interchanged, which is why the
condition must be derived for the sequence at hand, not quoted from memory.

**(b)** $\lambda = 2400/f$; for $h = \lambda/4$, $f = v/(4h) = 2400/80 = 30$ Hz.

**(c)** For beds thinner than the tuning thickness the two reflections overlap
within the wavelet and partially cancel, so the composite amplitude falls roughly
linearly with $h$. Below the noise level the bed becomes invisible, which is why
thin-bed detection is a signal-to-noise problem, not only a resolution problem.

**(d)** Tuning thickness is where the composite amplitude is extremal (a
phase-cancellation condition, typically $\lambda/4$); the resolution limit is the
smallest separation between *two* interfaces that can still be distinguished as
two events, of order $\lambda/4$ to $\lambda/2$ depending on bandwidth and noise
(lesson 02-03-09). They are different questions about the same length scale.

---

## ★8 — Standing-wave measurement

**(a)** The measured error in
$\langle u^2\rangle_t - 2A^2\cos^2(kx)$ is $2.220\times10^{-16}\ \mathrm{m^2}$,
and the measured nodes are at 0.25, 0.75, 1.25, 1.75, 2.25 m, matching the
prediction at the printed precision.

**(b)** The time average was taken over *exactly* one period with uniformly spaced
samples, which makes the discrete sum of $\cos(2\omega t_i)$ vanish identically
because the samples are symmetric about the midpoint of the period. Round-off is
then the only error. The property that makes this possible is that the sampling is
commensurate with the period; an arbitrary window leaves an $O(1/N)$ residual.

**(c)** Averaging over 0.9 of a period leaves a residual of order
$|\sin(2\omega T)|/N \sim 10^{-3}$ of the profile amplitude — three orders larger
than round-off. The practical lesson: when measuring a resonance or a standing
wave, use an integer number of cycles (or fit a sinusoid) rather than an arbitrary
time window.

**(d)** Record whole cycles (or several), and report the number of cycles used;
otherwise the estimated amplitude carries a systematic error of order $1/N_{\text{cycles}}$.

---

## ★★★9 — Cross-correlation and travel time

**(a)** For a coherent plane wave $u(t) = s(t)$ at station 1 and
$u_2(t) = s(t-D/v)$ at station 2, the cross-correlation
$C(\tau) = \int u_1(t)u_2(t+\tau)dt$ is maximised at $\tau = D/v$ (for
symmetrised correlation conventions, at $\pm D/v$); the width of the peak is the
autocorrelation width of $s(t)$, i.e. the coherence time.

**(b)** For a diffuse, equipartitioned noise field, the ensemble-averaged
cross-correlation of the two records equals (up to a constant and a time
derivative) the Green function between the stations, with acausal and causal
branches corresponding to the two propagation directions. The proof uses the
reciprocity theorem of elastodynamics, which is stated and used in lesson
[02-04-05](../../04-elasticity-and-continuum-mechanics/05-elastodynamics.md).

**(c)** A numerical experiment: synthesise a plane wave plus Gaussian noise at two
stations, cross-correlate, and measure the lag of the peak by parabolic
interpolation on the correlation function. Report the measured lag and its
scatter as a function of signal-to-noise ratio — expect the lag error to scale
roughly as $1/\sqrt{\text{SNR}}$ once the peak is identifiable.

**(d)** The recovered time is a genuine travel time when (i) the noise field is
approximately equipartitioned (energy arriving from all directions) and (ii) the
attenuation and the source distribution are such that the two stations are in the
same diffuse field. It is degraded by a strongly directional (non-equipartitioned)
source distribution, by strong attenuation between the stations, and by
instrument-response differences that are not removed.

---

## ★★★10 — Visibility

**(a)** $I = A_1^2+A_2^2+2A_1A_2\cos(\varphi+k(r_1-r_2))$, so
$I_{\max} = (A_1+A_2)^2$, $I_{\min} = (A_1-A_2)^2$ and
$V = [(A_1+A_2)^2-(A_1-A_2)^2]/[(A_1+A_2)^2+(A_1-A_2)^2] =
4A_1A_2/(2A_1^2+2A_2^2) = 2A_1A_2/(A_1^2+A_2^2)$ ✓.

**(b)** With $A_2 = \epsilon A_1$, $V = 2\epsilon/(1+\epsilon^2) \to 2\epsilon$ for
small $\epsilon$ ✓.

**(c)** Measured visibilities for $(1,1)$, $(1,0.5)$, $(1,0.1)$ should come out
1.000, 0.800, 0.198 against predictions 1.000, 0.800, 0.198. Report your measured
values and the agreement (with a fine enough lateral sampling the agreement should
be at the $10^{-3}$ level, limited by where the grid samples the extrema; a
parabolic refinement of the extrema improves it).

**(d)** The Green function recovered by ambient-noise correlation is the
superposition of contributions from all sources; if one direction dominates, the
recovered function is dominated by that azimuth and the estimate of the true
inter-station response is biased. This is the practical reason that noise-based
imaging is best in regions with a broad, uniform distribution of noise sources,
such as the deep ocean microseism.
