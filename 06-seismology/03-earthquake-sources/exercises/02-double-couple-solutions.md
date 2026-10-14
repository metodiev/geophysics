# Solutions — 06-03-02 The Double-Couple Source and Radiation Patterns

> **Read after attempting the exercises.** All numbers are SYNTHETIC. Angles are
> in degrees; dot products and amplitudes are dimensionless and quoted relative
> to the scalar moment $M_0$.

Lesson: [02 The Double-Couple Source and Radiation Patterns](../02-double-couple.md).

---

## ★1 — A vertical strike-slip

$\phi = 90^\circ$, $\delta = 90^\circ$, $\lambda = 0^\circ$:
$\sin\phi = 1$, $\cos\phi = 0$, $\sin\delta = 1$, $\cos\delta = 0$,
$\sin\lambda = 0$, $\cos\lambda = 1$.

$$\hat n = \left(-\sin\delta\sin\phi,\ \sin\delta\cos\phi,\ -\cos\delta\right)
= (-1,\ 0,\ 0),$$
$$\hat s = \left(\cos\lambda\cos\phi+\cos\delta\sin\lambda\sin\phi,\
\cos\lambda\sin\phi-\cos\delta\sin\lambda\cos\phi,\ -\sin\lambda\sin\delta\right)
= (0,\ 1,\ 0).$$

$$M = M_0\left(\hat n\hat s^{\mathsf T}+\hat s\hat n^{\mathsf T}\right)
= M_0\begin{pmatrix}
0 & -1 & 0\\
-1 & 0 & 0\\
0 & 0 & 0
\end{pmatrix}.$$

---

## ★2 — Trace and symmetry

$$\mathrm{tr}(M) = M_0\left(0+0+0\right) = 0.$$

Symmetry: $M_{xy} = M_{yx} = -M_0$; all other off-diagonal entries are zero, so
$M = M^{\mathsf T}$.

**Physical meaning.** A zero trace means the source **does not change volume**:
the tensor has no isotropic part. Symmetry means the source is a set of **force
couples with no net torque**, the condition $\hat n\perp\hat s$ guarantees. A
tensor with a non-zero trace would be an explosion or implosion; see
[03 Moment Tensors](../03-moment-tensors.md) and
[07 Explosion Sources](../07-nuclear-explosion-sources.md).

---

## ★3 — P amplitudes on three rays

With $\hat n = (-1,0,0)$ and $\hat s = (0,1,0)$,

$$A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s) = (-r_x)(r_y) = -r_x r_y.$$

| $\hat r$ | $A$ | Interpretation |
|---|---|---|
| $(1,0,0)$ | $-(1)(0) = 0$ | **nodal** (in the auxiliary plane, normal $\hat n$) |
| $(0,1,0)$ | $-(0)(1) = 0$ | **nodal** (in the fault plane, normal $\hat s$) |
| $(1,1,0)/\sqrt2$ | $-(1/\sqrt2)(1/\sqrt2) = -1/2$ | dilatational, inside a lobe |

**Nodal:** the first two. Both lie in one of the two planes through the origin
whose normals are $\hat n$ and $\hat s$, exactly as Section 3.3 predicts.

---

## ★4 — Deriving the quadrupole projection

With $\hat s\cdot\hat n = \hat n\cdot\hat s = 0$ and $\hat n\cdot\hat n
= \hat s\cdot\hat s = 1$,

$$\hat r^{\mathsf T}M\hat r
= M_0\,\hat r^{\mathsf T}\left(\hat n\hat s^{\mathsf T}
+ \hat s\hat n^{\mathsf T}\right)\hat r.$$

Now $\hat r^{\mathsf T}\hat n\hat s^{\mathsf T}\hat r
= (\hat r\cdot\hat n)(\hat s\cdot\hat r)$ and
$\hat r^{\mathsf T}\hat s\hat n^{\mathsf T}\hat r
= (\hat r\cdot\hat s)(\hat n\cdot\hat r)$; the two are equal because the dot
product commutes. Hence

$$\hat r^{\mathsf T}M\hat r = 2M_0(\hat r\cdot\hat n)(\hat r\cdot\hat s). ☑$$

**Property used:** $\hat n$ and $\hat s$ are orthonormal. In particular
$\hat n\cdot\hat s = 0$ was used implicitly to give $\hat n$ and $\hat s$ equal
standing (the cross terms are mirror images of one another). If $\hat n$ and
$\hat s$ were not orthogonal, the two terms would still add but the source would
no longer be a pure double couple.

---

## ★5 — Vertical-ray amplitude versus dip

For thrust ($\phi = 0^\circ$, $\lambda = +90^\circ$):
$\hat n = (0,\ \sin\delta,\ -\cos\delta)$ and
$\hat s = (0,\ -\cos\delta,\ -\sin\delta)$.

Check orthogonality: $\hat n\cdot\hat s = -\sin\delta\cos\delta
+ \sin\delta\cos\delta = 0$ ✔.

A ray going straight up is $\hat r = (0,0,-1)$:

$$A = (\hat r\cdot\hat n)(\hat r\cdot\hat s) = (+\cos\delta)(+\sin\delta)
= \sin\delta\cos\delta.$$

- Thrust, $\delta = 30^\circ$: $A = \sin30^\circ\cos30^\circ
  = 0.5000\times0.8660 = +0.4330$ → **compressional**.
- Normal, $\delta = 45^\circ$: for $\lambda = -90^\circ$ the sign of $\hat s$
  flips, so $A = -\sin45^\circ\cos45^\circ = -0.5000$ → **dilatational**.

This reproduces the demo's normal-at-$60^\circ$ entry $A = -0.4330
= -\sin60^\circ\cos60^\circ$ and its thrust-at-$20^\circ$ entry
$A = +0.3214 = \sin20^\circ\cos20^\circ$.

**Reading.** A thrust is compressional above the source (vertical $\hat P$); a
normal fault is dilatational above the source (vertical $\hat T$).

---

## ★6 — Plunge of the compressional axis

$\text{plunge} = 90^\circ - |\delta - 45^\circ|$:

| thrust dip $\delta$ | $|\delta-45^\circ|$ | plunge |
|---|---|---|
| $10^\circ$ | $35^\circ$ | $55^\circ$ |
| $35^\circ$ | $10^\circ$ | $80^\circ$ |
| $55^\circ$ | $10^\circ$ | $80^\circ$ |
| $80^\circ$ | $35^\circ$ | $55^\circ$ |

**Pattern.** The plunge is $90^\circ$ at $\delta = 45^\circ$ and falls
symmetrically as the dip departs from $45^\circ$ in either direction: a
$35^\circ$ thrust and a $55^\circ$ thrust have the same $80^\circ$ axis plunge.
This matches the demo table, where e.g. dips $20^\circ$ and $70^\circ$ both give
$65^\circ$. The relation follows from the geometry: with
$\hat n = (0,\sin\delta,-\cos\delta)$ and $\hat s = (0,-\cos\delta,-\sin\delta)$,
the bisector's vertical component is $-(\cos\delta+\sin\delta)/\sqrt2
= -\cos(\delta-45^\circ)$, so $\text{plunge} = 90^\circ-|\delta-45^\circ|$.
Hence "a vertical compressional axis means thrusting" is a statement about
dip-slip near $45^\circ$, not an identity.

---

## ★7 — Relative difference of the two tensor constructions

$$\frac{2.048\times10^{3}}{1.0\times10^{19}} = 2.048\times10^{-16}.$$

IEEE-754 double precision stores roughly $15.95$ decimal digits, i.e. a unit round
off of $\varepsilon \approx 1.1\times10^{-16}$. A relative difference of $2\times
10^{-16}$ is about $2\varepsilon$: the result of a handful of additions and
multiplications performed in a different order in the two routes. It is the
expected size of the **round-off floor**, and it says the two formulas compute
the same mathematical object. A difference of order $10^{-6}$ would instead
indicate a genuine inconsistency (a different convention, a missing factor or a
typo).

---

## ★8 — Invariance and sign

$$M(\hat n,\hat s) = M_0\left(\hat n\hat s^{\mathsf T}+\hat s\hat n^{\mathsf T}\right).$$

**Undo both:** $M(-\hat n,-\hat s)
= M_0\left((-\hat n)(-\hat s)^{\mathsf T}+(-\hat s)(-\hat n)^{\mathsf T}\right)
= M_0\left(\hat n\hat s^{\mathsf T}+\hat s\hat n^{\mathsf T}\right) = M$. Invariant.

**Undo one:** $M(\hat n,-\hat s)
= M_0\left(-\hat n\hat s^{\mathsf T}-\hat s\hat n^{\mathsf T}\right) = -M$.

**Physical operations.**

- $(\hat n,\hat s)\to(-\hat n,-\hat s)$: relabel the fault and the auxiliary
  planes *and* reverse the slip direction on the relabelled fault. This leaves
  the radiation pattern unchanged, which is the **fault-plane ambiguity**.
- $\hat s\to-\hat s$ alone: keep the same fault plane but take the slip as the
  **footwall** motion rather than the hanging-wall motion (equivalently, reverse
  the direction of slip). This flips the pattern, so it swaps the polarities and
  the $P$/$T$ labels. This is exactly the convention trap of Section 4.4: obspy
  and this module differ by this sign, so their eigen-labels are mirror images
  while their predicted polarities agree.

---

## ★9 — Which nodal plane is the fault? (specification)

**Hypocentre model.** Generate $N = 200$ aftershocks for a known event. Place
them on the fault plane by drawing positions uniformly in a rectangular patch
(along-strike length $L = 20\ \mathrm{km}$, down-dip width $W = 12\ \mathrm{km}$),
then add **independent Gaussian location errors** of $\sigma = 1.5\ \mathrm{km}$
in each coordinate. Use a SYNTHETIC mechanism with nodal-plane normals
$\hat n_1$ and $\hat n_2$ (the fault is the one with normal $\hat n_1$).

**Statistic.** Fit a plane to the hypocentres by total least squares (principal
component analysis: the best-fit plane is spanned by the two leading principal
axes). Report the **angle** between the fitted plane's normal and each candidate
normal $\hat n_1$, $\hat n_2$, and also fit two *constrained* planes with fixed
normals and compare the **residual scatter** $\chi^2$ about each.

**Decision rule.** Choose the candidate with the smaller residuals. Accept the
answer only if the ratio of the two $\chi^2$ values exceeds a threshold (say
$2$); otherwise declare the test inconclusive.

**Acceptable false-decision rate.** $5\%$ over 1000 synthetic repetitions, judged
by whether the test recovers the plane the hypocentres were generated on. With
$\sigma = 1.5\ \mathrm{km}$ on a patch of $20\times12\ \mathrm{km}$ and $N = 200$
events the two candidates are well separated, so the rate should be near zero;
re-running with $N = 10$ or $\sigma = 5\ \mathrm{km}$ should raise it, and the
*pair of curves* (rate versus $N$ and versus $\sigma$) is the real result.

---

## ★10 — How many stations to reach $p < 10^{-3}$?

Each station independently reads compression with probability $1/2$ under the
double-couple null hypothesis, so

$$p_{\text{all-compressional}} = \left(\tfrac12\right)^{N} = 2^{-N}.$$

Solve $2^{-N} < 10^{-3}$:

$$N > \frac{\log_{10}10^{3}}{\log_{10}2} = \frac{3}{0.30103} = 9.97 \Rightarrow N \ge 10.$$

The demo's table gives $9.766\times10^{-4}$ at $N = 10$ (just under $10^{-3}$) and
$3.906\times10^{-3}$ at $N = 8$; the crossing is between 9 and 10 stations.

**Why the real network is less decisive.**

1. **Dependence.** Stations are not independent draws. A poor velocity model, a
   systematic instrument-polarity error, or geometry that places all stations in
   one quadrant, makes a *block* of stations agree. The independence assumption
   is what makes $2^{-N}$ valid, and it fails precisely in the situations the
   discriminant is used in.
2. **Detection threshold.** A nodal-plane station has $A\approx0$ and its first
   motion is unreadable at the noise level; such stations are dropped, which both
   reduces the effective $N$ and biases the surviving sample away from the nodal
   planes.

A third practical point: a *single* dilatational first motion refutes the pure
explosion hypothesis, so the diagnostic value of $N$ compressional readings is
asymmetrically useful — $N = 10$ all-compressional is strong evidence, but the
absence of one such reading is not strong evidence the other way unless the
station is known to sit in a compressional lobe.
