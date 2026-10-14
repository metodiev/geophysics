# Solutions — 05-03-04 Numerical Forward Modelling and Discretisation

> Numbers marked *verified* were computed.

---

## ★1

Modelling error: unchanged by refinement (it is a property of the equations, not
the grid). Discretisation error: decreases with refinement at the scheme's order.
Round-off: increases slowly with refinement (more operations) and eventually
dominates.

---

## ★2

$\nabla^2u = [\text{5-point stencil}]/h^2 - \frac{h^2}{12}(u_{xxxx}+u_{yyyy}) +
O(h^4)$, so the local truncation error is $O(h^2)$ — second order.

---

## ★3 *(verified)*

$p = \log(5.142\times10^{-4}/1.2852\times10^{-4})/\log(2)
= \log(4.0004)/\log 2 = 2.0001$.

---

## ★★4

$\nabla^2u = -2\pi^2\sin\pi x\sin\pi y$, so $b = -\nabla^2u =
+2\pi^2\sin\pi x\sin\pi y$. (Sign convention: the solver is written for
$-\nabla^2u = b$, matching the demonstration.)

---

## ★★5

$dt \le dz^2/(2D)$ gives the maximum stable step; the demonstration uses the
more conservative $0.4\,dz^2/D$. With $dz = 251.6$ m,
$dz^2 = 6.330\times10^{4}$ m², so $0.4\,dz^2/D = 0.4(6.330\times10^{4})/
7.9577\times10^{5} = 3.183\times10^{-2}$ s.

---

## ★★6

Ratios: $1.2\times10^{-2}\to1.5\times10^{-4}$ is a factor 80 for a doubling of
$n$; $1.5\times10^{-4}\to3.6\times10^{-8}$ is a factor $4.2\times10^{3}$;
$3.6\times10^{-8}\to8.5\times10^{-15}$ is a factor $4.2\times10^{6}$. The
convergence is faster than any fixed power (super-algebraic), as expected for
Gauss–Legendre on a smooth integrand. The round-off floor is
$\approx10^{-15}$ relative, reached at $n = 32$; beyond that, refinement does
nothing ($4.0\times10^{-15}$ at $n = 64$). Largest useful $n$: about 32.

---

## ★★★7

Expected: fitted slope $2.0006$ (measured over four grids) with a stated
tolerance $|p-2|<0.01$. With a 1% error in the coefficient of $u$ (changing 4
to 4.04), the scheme becomes inconsistent or lower-order; the measured order
drops sharply (often to 1 or below, or the error stops converging).

Why the collapse is diagnostic: a *consistently* wrong coefficient introduces a
lower-order error term that dominates as $h\to0$, so the measured slope changes.
A scaling error alone would leave the order intact while offsetting the answer —
which is why both an order test *and* a closed-form comparison are needed.

---

## ★★★8

Expected structure:

| depth | modelling error (point mass vs prism) | discretisation (quadrature) | round-off |
|---|---|---|---|
| shallow ($d \sim$ body size) | tens of percent | $\sim10^{-15}$ at $n\ge32$ | $\sim10^{-15}$ |
| intermediate ($d \sim 3\times$ body) | $\sim1$–10% | $\sim10^{-14}$ | $\sim10^{-15}$ |
| deep ($d \gg$ body) | $<1\%$ | $\sim10^{-15}$ | $\sim10^{-15}$ |

At shallow depths the modelling error dominates by many orders of magnitude; the
practical tolerance is set by the *modelling*, i.e. a few percent, and there is
no point refining the quadrature beyond $n = 32$. At depth the point-mass
approximation becomes excellent and the tolerance can be pushed toward
$10^{-12}$ if the input parameters justify it — but only the *modelling*
tolerance matters if the density is known to 10%.
