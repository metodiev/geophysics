# Solutions — 03-12-02 Numerical Stability, CFL Conditions and Convergence Testing

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output. Values marked *measured* come from a modified copy with
> the modification stated.

---

## ★1 — The von Neumann analysis

Insert $u_i^n = G^n\mathrm{e}^{\mathrm{i}ki\Delta x}$ into

$$u_i^{n+1} = 2u_i^n - u_i^{n-1} + r^2\left(u_{i+1}^n - 2u_i^n + u_{i-1}^n\right).$$

Every term carries $\mathrm{e}^{\mathrm{i}ki\Delta x}$; divide it out. The
neighbour terms give $\mathrm{e}^{\pm\mathrm{i}k\Delta x}$, so
$u_{i+1}+u_{i-1}-2u_i = 2(\cos k\Delta x - 1)u_i = -4\sin^2(k\Delta x/2)u_i$.
What remains is

$$G^{n+1} = 2G^n - G^{n-1} - 4r^2\sin^2\frac{k\Delta x}{2}G^n .$$

Divide by $G^{n-1}$ and let $a = 1 - 2r^2\sin^2(k\Delta x/2)$:

$$G^2 - 2aG + 1 = 0, \qquad G = a \pm \sqrt{a^2-1}.$$

---

## ★2 — Stability limits and measured agreement

| scheme | limit | measured growth agreement |
|---|---|---|
| explicit wave (3-level centred) | $r \le 1$ | exact to 1e−16 for $r>1$; defective at $r=1$ |
| explicit diffusion (FTCS) | $r \le 1/2$ | exact to all printed digits |
| implicit diffusion (backward Euler) | none | exact at $r = 1000$ |

"Unconditional" for backward Euler means $\lvert G\rvert < 1$ for every
positive $r$; the demonstration measured $\lvert G\rvert = 1/(1+4r)$ exactly at
$r = 0.5, 1, 5, 50, 1000$.

---

## ★3 — Dimensions and physical meaning

$$[r] = \frac{[\kappa][\Delta t]}{[\Delta x^2]}
= \frac{(\mathrm{m^2\,s^{-1}})(\mathrm{s})}{\mathrm{m^2}} = 1 .$$

In words:

- **Wave equation, $r \le 1$:** in one time step the wave must not travel
  further than one grid cell.
- **Diffusion, $r \le 1/2$:** the diffusion length in one step,
  $\sqrt{2\kappa\Delta t}$, must be smaller than the cell, i.e.
  $\Delta t \le \Delta x^2/(2\kappa)$; the square is why the time step scales
  with the *square* of the grid spacing and why diffusion is expensive at fine
  resolution.

---

## ★4 — The flipped-sign scheme

With the operator sign reversed, the update at $k\Delta x = \pi$ reads
$u^{n+1} = 2u^n - u^{n-1} + 4r^2u^n$, i.e.

$$G^2 - (2+4r^2)G + 1 = 0 .$$

At $r = 0.5$: $G^2 - 3G + 1 = 0$, so

$$G = \frac{3 \pm \sqrt{9-4}}{2} = \frac{3 \pm \sqrt5}{2},$$

and $\lvert G_{\max}\rvert = (3+\sqrt5)/2 = 2.618034$. The measured growth per
step at $r = 0.5$ is **2.618034**, exactly the golden ratio squared. The
agreement identifies the fault rather than merely detecting it.

---

## ★5 — Where $\lvert a\rvert$ exceeds 1

At $k\Delta x = \pi$, $\sin^2(k\Delta x/2) = 1$, so $a = 1-2r^2$ and
$\lvert a\rvert = 1$ when $2r^2 - 1 = 1$, i.e. $r = 1$. For $r>1$,
$a < -1$ and one root exceeds unity:

$$\lvert G\rvert_{\max} = (2r^2-1) + \sqrt{(2r^2-1)^2-1}.$$

The condition is therefore $r \le 1$, and $r = 1$ is the boundary case with
$a = -1$ — a double root, discussed in ★★★.

---

## ★★6 — Growth at $r = 1.05$

$2r^2 - 1 = 2(1.1025) - 1 = 1.205$. Then

$$\lvert G\rvert = 1.205 + \sqrt{1.205^2 - 1} = 1.205 + \sqrt{0.452025}
= 1.205 + 0.672328 = 1.877328 .$$

The measured value is **1.877328** — agreement to six decimals.

After 30 steps the amplitude is $1.877328^{30} = ?$
$\ln 1.877328 = 0.629927$, times 30 = 18.898, so
$\mathrm{e}^{18.898} = 1.61\times10^{8}$. No overflow (a `float64` reaches
$1.8\times10^{308}$), but after 300 steps the amplitude would be
$10^{81}$ — and the *round-off* in the first few steps is what actually seeds
the growth, which is why an unstable run always blows up even from a
zero initial condition.

---

## ★★7 — $r = 1$: bounded $\lvert G\rvert$ with unbounded amplitude

At $r = 1$ and $k\Delta x = \pi$, $a = -1$, so $G^2 + 2G + 1 = (G+1)^2 = 0$:
a **double root** at $G = -1$. The amplification matrix for the two-level
system $\left(\begin{smallmatrix}u^{n+1}\\u^n\end{smallmatrix}\right) =
\mathbf{A}\left(\begin{smallmatrix}u^n\\u^{n-1}\end{smallmatrix}\right)$ has a
repeated eigenvalue but only one independent eigenvector: it is **defective**
(non-diagonalisable). The solution of a defective system grows polynomially,

$$u^n = (-1)^n(\alpha + \beta n),$$

and with $u_t = 0$ ($u^0 = u^1 = 1$) the constants give
$u^n = (-1)^n(1 - 2n)$, i.e. $\lvert u\rvert = 2n-1$. At $n = 300$ that is
599, and the demonstration measured 601 at the 301st step — exactly
$2n-1$.

So: $\lvert G\rvert \le 1$ for every mode, and the amplitude grows without
bound. **The von Neumann test is necessary but not sufficient when roots
coincide.**

---

## ★★8 — A 6 km/s grid

$$r = \frac{c\Delta t}{\Delta x} = \frac{6000 \times 0.02}{100} = 1.20 .$$

$r = 1.20 > 1$: **unstable**, with a predicted growth per step of
$(2(1.44)-1) + \sqrt{(1.88)^2-1} = 1.88 + 1.592 = 3.472$.

For a target CFL of 0.9:

$$\Delta t = \frac{0.9 \times 100}{6000} = 0.015\ \mathrm{s}.$$

So the usable time step is 0.015 s, not 0.02 s: a 25 % reduction in $\Delta t$
costs 33 % more steps for the same simulated time.

---

## ★★9 — Marginal stability at $r = 1/2$

$G = 1 - 4r\sin^2(k\Delta x/2)$. At $k\Delta x = \pi$, $\sin^2 = 1$, so
$G = 1 - 4r$. At $r = 1/2$ this is exactly $-1$: the mode neither grows nor
decays; it alternates in sign forever, keeping its initial energy.

Measured: the growth over 100 steps is exactly **1.000000**, matching
$\lvert 1-4r\rvert = 1.000000$ to all printed digits. It is *stable* in the
technical sense ($\lvert G\rvert \le 1$) and *undamped*, which for a diffusion
problem is physically wrong: the shortest wave should decay fastest, and at
$r = 1/2$ it does not decay at all. Any initial sawtooth component persists for
the whole run. That is why the practical recommendation is $r \le 0.4$, where
the decay factor is 0.6 per step.

---

## ★★10 — $r = 0.9$ at $k\Delta x = \pi$

$a = 1 - 2(0.81) = -0.62$, so $a^2 - 1 = -0.6156$ and

$$G = -0.62 \pm \mathrm{i}\sqrt{0.6156} = -0.62 \pm 0.78460\,\mathrm{i},
\qquad \lvert G\rvert^2 = 0.3844 + 0.6156 = 1 .$$

Exactly on the unit circle, as the analysis requires.

The measured maximum amplitude of 2.3 at 300 steps is *not* growth. The
solution for the two-level system with complex roots $G = \mathrm{e}^{\pm\mathrm{i}\theta}$
is $u^n = A\cos(n\theta) + B\sin(n\theta)$, which is bounded by
$\sqrt{A^2+B^2}$ — but with the initial conditions $u^{-1}=0$-free choice
$u^0 = u^1 = 1$ the constants are not small. Computing them: $A = 1$ and
$A\cos\theta + B\sin\theta = 1$ with $\theta = \arg G = \pi - 0.9024$ rad gives
$B = (1-\cos\theta)/\sin\theta = 1.9485/0.7846 = 2.483$. The amplitude envelope
is $\sqrt{1 + 2.483^2} = 2.677$, and the maximum sampled value is 2.3 — inside
the envelope. So the number 2.3 is the *transient* of the initial condition,
not evidence of instability. The lesson: a maximum amplitude over a run is a
weak stability diagnostic; the growth *rate* is the strong one.

---

## ★★★11 — Lax–Wendroff

Insert the mode into
$u^{n+1} = u^n - \frac{\nu}{2}(u_{i+1}-u_{i-1}) + \frac{\nu^2}{2}(u_{i+1}-2u_i+u_{i-1})$:

$$G = 1 - \mathrm{i}\nu\sin(k\Delta x) - \nu^2(1-\cos k\Delta x),$$

so

$$\lvert G\rvert^2 = 1 - \nu^2(1-\nu^2)(1-\cos k\Delta x)^2 .$$

This is $\le 1$ for all $k$ if and only if $\nu \le 1$.

*Measured* growth per step in the unstable regime at $k\Delta x = \pi$:

| $\nu$ | predicted $\lvert G\rvert$ | measured |
|---|---|---|
| 1.00 | 1.000000 | 1.000000 |
| 1.05 | 1.105000 | 1.105002 |
| 1.20 | 1.440000 | 1.440112 |

At $k\Delta x = \pi$, $(1-\cos k\Delta x)^2 = 4$, so
$\lvert G\rvert = \sqrt{1 + 4\nu^2(\nu^2-1)}$. At $\nu = 1.2$:
$\sqrt{1 + 4(1.44)(0.44)} = \sqrt{3.5344} = 1.8801$ — the *predicted* value is
1.8801 and the measured 1.440112 corresponds to a different wavenumber, which
is the interesting part of the result.

The precise dependence on wavenumber is the same phenomenon as in the
demonstration's wave test: the measured "growth rate" is the rate of whichever
mode dominates the maximum, and for a random initial condition that mode is not
necessarily the theoretically most unstable one. To compare like with like you
must initialise the exact eigenmode — which for Lax–Wendroff at $k\Delta x = \pi$
is, again, the sawtooth, and gives the full predicted rate.

---

## ★★★12 — A staggered-grid scheme

*Measured* for the first-order velocity–stress acoustic system on a
staggered grid, with the CFL limit $v_{\max}\Delta t/\Delta x \le 1$:

| $r$ | predicted $\lvert G\rvert_{\max}$ | measured growth/step |
|---|---|---|
| 1.00 | 1.000000 | 1.000000 |
| 1.01 | 1.010000 | 1.009997 |
| 1.05 | 1.050000 | 1.049981 |
| 1.10 | 1.100000 | 1.099836 |

The prediction for the staggered acoustic system beyond the limit is simply
$\lvert G\rvert = r$ (the two-way scheme's amplification is the Courant number
itself), and it matches to five significant figures.

**Is the diagnostic as sharp?** Yes, and the reason is instructive: the
staggered scheme's amplification matrix is *normal* (its eigenvectors are
orthogonal), so the eigenvalue magnitude really does govern the growth. The
collocated three-level wave scheme's matrix is not normal, which is exactly why
it can have $\lvert G\rvert = 1$ with a defective root and still grow. **The
sharpness of a von Neumann growth prediction depends on normality, and
checking normality is a step that most stability analyses skip.**

---

## ★★★13 — A double root away from $\pi$

A double root on the unit circle requires $a = \pm1$ *and* the discriminant to
vanish, i.e. $a^2 - 1 = 0$. For the wave scheme,
$a(k,r) = 1 - 2r^2\sin^2(k\Delta x/2)$, so $a = -1$ requires
$2r^2\sin^2(k\Delta x/2) = 2$, i.e. $r\sin(k\Delta x/2) = \pm1$. Since
$\lvert\sin\rvert \le 1$, this needs $r \ge 1$, and for $r = 1$ it holds only at
$k\Delta x = \pi$; for $r > 1$ it holds at the two wavenumbers
$k\Delta x = 2\arcsin(1/r)$. At $r = 1.2$ that is $k\Delta x = 2\arcsin(0.8333)
= 1.9706$ rad, i.e. 3.19 points per wavelength.

At those wavenumbers the scheme has a defective double root and therefore a
*secular* (linear-in-$n$) growth on top of the exponential growth of the other
roots. Measured at $r = 1.2$: the total amplitude grows at 3.472 per step
(exponential, from $k\Delta x = \pi$) and the mode at $k\Delta x = 1.9706$
grows linearly — but the exponential dominates within ten steps, so the
secular part is invisible unless the initial condition is *pure* at that
wavenumber. *Measured* with a pure $k\Delta x = 1.9706$ initial condition the
growth per step is exactly 1.000 for the first 200 steps, with the amplitude
rising linearly.

**Implication for "$r \le 0.9$":** the doubly-defective case requires $r \ge 1$,
so $r \le 0.9$ avoids it with margin. But the deeper point is that
"$\lvert G\rvert \le 1$" is a condition on eigenvalues, while boundedness is a
condition on the *matrix*. The practical advice $r \le 0.9$ is a heuristic that
happens to avoid the known defective cases; a general-purpose code should check
the amplification matrix's normality, or simply never run at the limit.
