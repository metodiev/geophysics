# Solutions — 06-06-05 The Adjoint Method for Efficient Sensitivity Computation

Exercises:
[05-adjoint-methods-exercises.md](05-adjoint-methods-exercises.md).

## ★ Foundational

**1.** Central differences need two solves per parameter:
$2\times2.0\times10^{5} = \mathbf{4.0\times10^{5}}$ solves. The adjoint needs
**2** solves, one forward and one backward, independent of the parameter count —
a factor $2\times10^{5}$.

**2.** Ratio $= 1.0000000000$. A ratio of 1.49 would mean the adjoint is not the
transpose of the operator that generated the perturbation: either a row of the
operator (a boundary condition, a damping factor, the source insertion) is
missing from the transpose, or the adjoint recursion is indexed one step
relative to the forward one. The dot-product test cannot be passed by accident,
which is why it is the standard first test.

**3.** $\lambda = c/f = 3600/16 = \mathbf{225\ m}$; ratio
$120/225 = \mathbf{0.53}$ — but the demonstration reports 120 m against a
"wavelength" column of 125 m, because its local velocity is
$\sqrt{\theta}\,\Delta x/\Delta t \approx 2500\ \mathrm{m\,s^{-1}}$, giving
$\lambda = 2500/16 = 156$ m at the reference node and 125 m at the sampled node.
The ratio to quote is the one computed with the same velocity: 0.96.

## ★★ Applied

**4.** The median is dominated by parameters whose gradient is significant and
well represented in both schemes. The worst case is a parameter where the
finite-difference gradient is very small (a nearly insensitive node), so the
*relative* difference is amplified by a near-zero denominator — a 4-order-of-
magnitude spread produced by the denominator, not by the implementation. Quote
both, plus the cosine similarity (1.0000000000 here), which is insensitive to
near-zero entries.

**5.** At $f = 10^{-2}$ the gradient has already rotated by about 0.86 degrees
($\cos = 0.9914$), and at $5\times10^{-2}$ it is anti-correlated. A defensible
rule is to keep $f$ where the linear prediction is accurate to a few per cent,
i.e. $f \le 10^{-3}$ (ratio 0.9852), or at most $3\times10^{-3}$ by
interpolation; beyond that the step direction is no longer the descent direction
of the function being minimised.

**6.** 24 solves in the demonstration took about 0.1 s in the same framework
(the setup and output dominate), i.e. of order $4\times10^{-3}$ s per solve. For
all 300 parameters the brute-force route needs 600 solves
$\approx \mathbf{2.4\ s}$, while the adjoint needs 2 solves
$\approx \mathbf{0.008\ s}$: a speed-up of 300, exactly the
parameter-count/2 ratio predicted by the cost table.

## ★★★ Research-oriented

**7.** $\lambda = 4.0\ \mathrm{km\,s^{-1}}\times100\ \mathrm{s} =
\mathbf{400\ km}$. A kernel one wavelength wide cannot resolve 50 km: the request
is a factor of 8 beyond what the measurement supports at that period. To get
50 km one needs $\lambda \approx 50$ km, i.e. a period near
$\mathbf{12.5\ s}$ — which for surface waves is a very shallow-sampling wave.
This is the fundamental resolution/penetration trade-off of long-period
tomography: depth of sampling and kernel width are bought with the same currency.

**8.** $1000 \times 10^{7} \times 4\ \mathrm{bytes} =
\mathbf{4\times10^{13}\ bytes} = 40\ \mathrm{TB}$ — far beyond a single node.
Strategy: **checkpointing**. Store the field at every $k$-th step only, and
recompute each interior segment during the backward pass from its nearest
checkpoint, at a cost of one extra forward solve segment per step. Memory falls
by a factor $k$ and computation rises by a factor $\le 2$; the gradient is
unchanged, which is the property that makes the strategy acceptable.
