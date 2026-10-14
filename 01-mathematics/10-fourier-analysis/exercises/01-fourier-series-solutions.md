# Solutions — 01-10-01 Fourier Series and Periodic Decomposition

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Every numeric answer below was computed, and the
> numbers quoted from the supplied script are the values it actually printed.

---

## ★1 — Coefficients of the square wave

**(a)** $f(t) = \mathrm{sign}(\sin t)$ is odd: $f(-t) = -f(t)$. The integrands of

$$a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos(nt)\,dt$$

are odd (odd times even), so every $a_n = 0$, including $a_0$ — which also
follows directly from the signal having zero mean over a period.

**(b)** With $f$ odd, $f(t)\sin(nt)$ is even, so

$$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\sin(nt)\,dt
= \frac{2}{\pi}\int_0^{\pi}\sin(nt)\,dt
= \frac{2}{\pi}\cdot\frac{1 - \cos(n\pi)}{n}.$$

$1-\cos(n\pi)$ is $2$ for odd $n$ and $0$ for even $n$. Therefore

$$\boxed{b_n = \frac{4}{n\pi}\ \text{ for odd } n, \qquad b_n = 0\ \text{ for even } n,}$$

so only the odd harmonics appear:
$f(t) = \frac{4}{\pi}\left(\sin t + \frac{\sin 3t}{3} + \frac{\sin 5t}{5} + \cdots\right)$.

**(c)** $|b_n| \sim 4/(\pi n)$: the coefficients decay like $1/n$, i.e.
algebraically and slowly. This is the signature of a function with a jump
discontinuity. A function that is continuous but has a corner (the triangular
wave) has $|b_n| \sim 1/n^2$, and a smooth periodic function decays faster than
any power of $n$. The decay rate of the coefficients *is* the smoothness of the
function.

**The trap.** It is tempting to say "the coefficients decay like $1/n$, so the
series converges slowly but it converges". True, but the more important
consequence is that the *truncated* series is a poor pointwise approximation
near the jumps — see ★★★10.

---

## ★2 — Coefficient pairs to amplitude and phase

The conversion is $A_n = \sqrt{a_n^2+b_n^2}$ and $\phi_n = \arctan_2(b_n,a_n)$,
reported on $[0^\circ, 360^\circ)$.

| | $a_n$ | $b_n$ | $A_n$ | $\phi_n$ |
|---|---|---|---|---|
| (a) | 3 | 4 | $\sqrt{9+16} = 5$ | $\arctan_2(4,3) = 53.13^\circ$ |
| (b) | 0 | −2 | 2 | $\arctan_2(-2,0) = -90^\circ \equiv 270^\circ$ |
| (c) | −1 | −1 | $\sqrt{2} = 1.414214$ | $\arctan_2(-1,-1) = -135^\circ \equiv 225^\circ$ |
| (d) | 0.5 | 0 | 0.5 | $\arctan_2(0,0.5) = 0^\circ$ |

**Check each one** by expanding $A\cos(\omega t - \phi)$:

(a) $5\cos(\omega t - 53.13^\circ) = 5(0.6\cos\omega t + 0.8 \sin\omega t)
= 3\cos\omega t + 4\sin\omega t$ ✓ where $\cos 53.13^\circ = 0.6$ and
$\sin 53.13^\circ = 0.8$.

(b) $2\cos(\omega t - 270^\circ) = 2\cos\omega t\cos270^\circ + 2\sin\omega t\sin270^\circ
= -2\sin\omega t$ ✓, matching $a=0$, $b=-2$.

**On the phase range.** (b) gives the same angle whether written $-90^\circ$ or
$270^\circ$, and (c) whether $-135^\circ$ or $225^\circ$. The *only* thing that
distinguishes them is the convention, which must be stated. Tidal practice
quotes $g$ on $[0^\circ, 360^\circ)$; a table mixing the two conventions is
unreadable.

---

## ★3 — Orthogonality integrals

**(a)** Different harmonics: $\int_0^{2\pi}\cos(2x)\cos(3x)dx = \boxed{0}$. Rule:
$\langle\cos m,\cos n\rangle = 0$ for $m \ne n$ on a full period.

**(b)** Equal harmonics: $\int_0^{2\pi}\sin^2(4x)dx = \boxed{\pi}$. Rule:
$\langle\sin n,\sin n\rangle = \pi$ for $n \ge 1$ on a period of $2\pi$ (the
general formula is $T/2 = \pi$).

**(c)** Mixed functions, same harmonic: $\int_0^{2\pi}\cos(2x)\sin(2x)dx
= \frac{1}{2}\int_0^{2\pi}\sin(4x)dx = \boxed{0}$. Rule: cosine and sine are
orthogonal even at the same harmonic, because the integrand is odd about
$x = \pi/2$ within the period.

**(d)** $\int_0^{2\pi}\cos(0x)\cos(2x)dx = \int_0^{2\pi}\cos(2x)dx = \boxed{0}$.
The constant is orthogonal to every non-zero harmonic.

**Why this matters.** These four cases are exactly the four outcomes needed to
derive the coefficient formulas: only the matching term survives, and it survives
with the value $T/2$ (or $T$ for the constant). If any of these integrals were
non-zero, the coefficients would not be independent of one another and the whole
method would collapse.

---

## ★4 — Beat periods

**(a)** To convert degrees per hour to cycles per hour, divide by 360:

$$f_{M2} = \frac{28.9841042}{360} = 0.08051140\ \mathrm{cyc/h}, \qquad
f_{S2} = \frac{30.0000000}{360} = 0.08333333\ \mathrm{cyc/h}.$$

**(b)** The beat period is $1/|\Delta f|$:

$$T_{\text{beat}} = \frac{1}{0.08333333 - 0.08051140}
= \frac{1}{0.00282193} = 354.37\ \mathrm{h} = 14.765\ \mathrm{d}.$$

This is the spring–neap period: the familiar fortnightly modulation of tidal
range is this one number.

**(c)** $f_{K1} = 15.0410686/360 = 0.04178075$ and
$f_{P1} = 14.9589314/360 = 0.04155259$ cyc/h, so

$$T_{\text{beat}} = \frac{1}{0.00022816} = 4382.89\ \mathrm{h} = 182.62\ \mathrm{d}.$$

**Compare.** 14.765 days versus 182.6 days — a factor of 12.4 — from a difference
in speeds of only $30.0000000-28.9841042 = 1.016$ deg/h versus
$0.0821372$ deg/h. The diurnal pair K1/P1 beat so slowly that a six-month record
is needed to see one cycle of their interference; this is why K1 and P1 are
routinely analysed as a joint pair with the ratio P1/K1 fixed from theory.

---

## ★★5 — A three-term sawtooth partial sum

**(a)** With $b_n = 2(-1)^{n+1}/n$:

$$S_3(t) = 2\left(\sin t - \frac{\sin 2t}{2} + \frac{\sin 3t}{3}\right).$$

**(b)** At $t = \pi/2$: $\sin(\pi/2) = 1$, $\sin(\pi) = 0$, $\sin(3\pi/2) = -1$, so

$$S_3(\pi/2) = 2\left(1 - 0 - \frac{1}{3}\right) = 2\cdot\frac{2}{3} = 1.333333.$$

The true value is $f(\pi/2) = (\pi/2)/\pi = 0.5$. The error is $0.833333$ — the
partial sum is 167% too large, and it is large for a reason: $t = \pi/2$ sits
between two features (the jump at $t = \pi$ is nearby), and the higher harmonics
that would cancel the overshoot have been truncated.

**(c)** At $t = 0.1\pi$: $\sin(0.1\pi) = 0.309017$,
$\sin(0.2\pi) = 0.587785$, $\sin(0.3\pi) = 0.809017$, so

$$S_3(0.1\pi) = 2\left(0.309017 - \frac{0.587785}{2} + \frac{0.809017}{3}\right)
= 0.569593,$$

against the true value $f(0.1\pi) = 0.1$. The error is $0.469593$ — smaller than
in (b) but still enormous.

**(d)** Both errors are large; the one at $\pi/2$ is larger. The partial sum
oscillates about the function with an amplitude that does not vanish with more
terms (the Gibbs phenomenon), and the *envelope* of that oscillation is largest
adjacent to the discontinuity at $t = \pi$ and decays away from it. At
$t = 0.1\pi$ the point is far from the jump and the truncation error is
correspondingly smaller. The useful habit: never quote a Fourier partial sum at
a point close to a jump without saying so.

---

## ★★6 — Rayleigh criterion for a 20-day record

The record length is $T = 20\ \mathrm{d} = 480$ h. The criterion is
$T > 1/|\Delta f|$.

**(a)**

| pair | $\Delta f$ (cyc/h) | $1/\lvert\Delta f\rvert$ | satisfied at 20 d (480 h)? |
|---|---|---|---|
| M2–S2 | 0.00282193 | 354.37 h | **yes** |
| M2–N2 | 0.00151215 | 661.31 h | no |
| K1–P1 | 0.00022816 | 4382.89 h | no |
| S2–K2 | 0.00022816 | 4382.89 h | no |

**(b)** M2/N2 needs at least 661.31 h = 27.6 d, i.e. about 1.4 times the record
available. K1/P1 and S2/K2 need 4382.89 h = 182.6 d, i.e. about 9.1 times the
record available. (The values differ from the "closest-neighbour" table in the
lesson only because here each pair is considered on its own.)

**(c)** A defensible review comment:

> The M2 and S2 amplitudes are reported as if separately determined, but with a
> 20-day record S2 lies within the Rayleigh limit of K2 (182.6 days required) and
> the fit cannot separate them. Please quote the formal standard errors from the
> normal matrix; on this record the S2 and K2 coefficients are strongly
> correlated, and an S2 estimate alone is not interpretable without S2 and K2
> being reported jointly.

The second sentence is the operational point: it is not that the numbers are
undefined, it is that they cannot be read one at a time.

---

## ★★7 — Parseval and the sum of odd inverse squares

**(a)** On a period, $f(t)^2 = \mathrm{sign}(\sin t)^2 = 1$, so

$$\frac{1}{2\pi}\int_0^{2\pi}f(t)^2\,dt = \frac{1}{2\pi}\cdot 2\pi = \boxed{1}.$$

**(b)** With $a_n = 0$ and $b_n = 4/(n\pi)$ for odd $n$,

$$\frac{1}{2}\sum_{n\ \mathrm{odd}} b_n^2
= \frac{1}{2}\sum_{n\ \mathrm{odd}}\frac{16}{n^2\pi^2}
= \frac{8}{\pi^2}\sum_{n\ \mathrm{odd}}\frac{1}{n^2}.$$

**(c)** Equating (a) and (b): $\frac{8}{\pi^2}\sum_{n\ \mathrm{odd}} n^{-2} = 1$,
so

$$\sum_{n\ \mathrm{odd}}\frac{1}{n^2} = \frac{\pi^2}{8} = \boxed{1.233701}.$$

**(d)** The partial sum over odd $n \le 9$ is
$1 + \frac{1}{9} + \frac{1}{25} + \frac{1}{49} + \frac{1}{81} = 1.183865$,
which is $1.183865/1.233701 = \boxed{0.959605}$, i.e. 95.96% of the limit.

**Comment.** The terms decay as $1/n^2$, so the missing tail beyond $n = 9$ is
about $4\%$ of the total — small, because Parseval integrates a *squared*
quantity. Yet the *function* represented by those nine terms still overshoots by
9.1% of the jump (★★★10). Energy convergence and pointwise convergence are
different things, and this pair of results is the cleanest demonstration of it.

---

## ★★8 — Phase, coefficients and a time shift

**(a)** $A\cos(\omega t - \phi) = A\cos\phi\cos\omega t + A\sin\phi\sin\omega t$, so

$$a = 1.5\cos 40^\circ = 1.149067, \qquad b = 1.5\sin 40^\circ = 0.964181.$$

**(b)** A quarter period for this constituent means
$t_0 = T/4 = 1/(4f)$, i.e. $\omega t_0 = \pi/2$. Shifting the record so the
constituent is $t_0$ later multiplies its complex coefficient by
$e^{-i\omega t_0} = e^{-i\pi/2} = -i$, which subtracts $\pi/2$ from the phase:

$$\phi' = 40^\circ - 90^\circ = -50^\circ \equiv 310^\circ,$$

$$a' = 1.5\cos 310^\circ = 0.964181, \qquad b' = 1.5\sin 310^\circ = -1.149067.$$

**(c)** Every harmonic of a shifted signal has the same modulus
$\lvert c_n e^{-in\omega_0 t_0}\rvert = \lvert c_n\rvert$, because a multiplication
by a unit-modulus complex number is a rotation in the complex plane; amplitudes
are invariant under time shifts, phases are not.

**(d)** No conflict: $310^\circ$ in (b) is exactly the value reached by shifting
the epoch by a quarter period. The two numbers are the same analysis referred to
different time origins. This is why every published tidal phase must come with
the epoch it refers to, and why two tables of $g$ values can differ wildly while
describing identical data.

---

## ★★★9 — How long a record does a constituent need?

**(a)** Using
[`code/fourier_series_demo.py`](../code/fourier_series_demo.py) with
$\sigma = 0.0200$ m and hourly sampling, the formal standard error of the K2
amplitude is

| record | $\sigma_A(\mathrm{K2})$ (script prints two decimals) |
|---|---|
| 14 d | 18.66 mm (18.665) |
| 20 d | 6.80 mm (6.799) |
| 30 d | 3.74 mm (3.740) |

(The parenthetical values have one more decimal than the script prints; they come
from calling the same fitting function with the amended record length rather than
from reading the printed table.)

**(b)** Between 20 d (6.799 mm) and 30 d (3.740 mm) the error crosses 5 mm, so the
answer is between 20 and 30 days. Interpolating in $\log T$ against
$\log \sigma_A$ — the local slope is about $-1.5$ — gives roughly 24 days:

| record | $\sigma_A(\mathrm{K2})$ |
|---|---|
| 21 d | 6.186 mm |
| 24 d | 5.151 mm |
| 25 d | 4.927 mm |
| 26 d | 4.707 mm |

(obtained by calling the script's `harmonic_fit`/`amp_sigma` pair with each of
these record lengths — the script itself scans 14, 30, 60 and 365 days).

so **25 days** is the smallest whole day count in this scan that satisfies
$5$ mm (24 days gives 5.151 mm, just above). Always state the criterion used:
"25 days at the 5 mm level".

**(c)** Two different regimes.

- **14 d to 30 d (factor 5):** K2's closest neighbour S2 is 0.00022816 cyc/h
  away, needing 4382.89 h = 182.6 d. On a 14-day record the fit has to
  distinguish two nearly parallel basis functions, and the normal matrix is
  ill-conditioned: the error is dominated by that near-degeneracy, not by the
  record length per se. Each increment of record length attacks the degeneracy
  directly, so the error falls faster than $1/\sqrt{T}$ — the local slope here is
  roughly $T^{-1.5}$.
- **182 d to 365 d (factor 1.4):** once the record exceeds the Rayleigh limit the
  basis functions are genuinely distinct and the estimator becomes efficient. The
  error then falls as $\sigma\sqrt{2/N}$, i.e. as $1/\sqrt{T}$: doubling the
  record improves the estimate by $\sqrt{2} = 1.414$, which is the observed 1.42.

**(d)** A 5 mm uncertainty on an amplitude of 0.110 m is 4.5%. That is useful:
K2 is a small constituent used mainly to constrain the S2/K2 pair and the
lunisolar ratio, and a 4.5% amplitude error is well within the systematic
uncertainty from the assumed S2/K2 ratio in most practical work.

**The general lesson.** The record length needed is set by the *closest pair*,
not by the constituent of interest, and the payoff for a longer record is
nonlinear while you are below the Rayleigh limit and $\sqrt{T}$ once you are
above it.

---

## ★★★10 — The Gibbs overshoot

**(a)** The overshoots fall 9.116% → 8.974% → 8.951% → 8.949%. The last two
differ by 0.002 percentage points and the sequence is visibly flattening, so the
limit is $\boxed{8.949\%}$ of the jump — to the precision of the table, and
certainly not below 8.948%.

**(b)** 99 terms give 8.951%, which is 0.002 percentage points above 8.949%, and
199 terms give 8.949%. So the smallest tabulated count meeting the
$\pm 0.002$ percentage-point tolerance is **99 odd harmonics**; a smaller count
does not meet it (25 terms give 8.974%, which is 0.025 points out).

**(c)** The classical result gives

$$\text{maximum} \to \frac{2}{\pi}\int_0^\pi\frac{\sin u}{u}\,du
= \frac{2}{\pi}\times 1.85193705 = 1.1789797 .$$

For a jump of 2, the overshoot is $1.1789797 - 1 = 0.1789797$, which as a
fraction of the jump is

$$\frac{0.1789797}{2} = 0.0894899 \approx \boxed{8.949\%}.$$

This agrees with (a) to the four figures the table carries. The agreement is a
genuine check: the script measured partial sums numerically while the classical
formula comes from the sine-integral; they are the same quantity.

**(d)** As $N$ grows, the extra terms contribute
$\sin(nt)/n$ with ever smaller amplitude, and their sum at the point of maximum
converges to a fixed number — the integral above — because the series of
contributions at the overshoot peak is a convergent alternating series with a
non-zero limit. The *region* over which the oscillation is significant, however,
is set by the highest retained harmonic: the first zero of
$\sin(Nt)/(N\sin t)$ sits at $t \approx \pi/N$, so the overshoot is squeezed
into a width of order $1/N$ while its height stays fixed. That is why the
phenomenon is invisible in a plot of many terms but fatal to a band-limited
interpretation of a sharp interface.
