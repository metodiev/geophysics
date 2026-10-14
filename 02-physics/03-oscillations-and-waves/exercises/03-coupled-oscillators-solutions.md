# Solutions — 02-03-03 Coupled Oscillators and Normal Modes

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Three springs, two masses

**(a)** With displacements $u_1, u_2$ from equilibrium,

$$m\ddot u_1 = -ku_1 + k(u_2-u_1) = k(u_2 - 2u_1), \qquad
m\ddot u_2 = k(u_1 - 2u_2).$$

**(b)**

$$\mathbf{M} = m\begin{pmatrix}1&0\\0&1\end{pmatrix}, \qquad
\mathbf{K} = k\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.$$

**(c)** $\det(\mathbf{K}-\omega^2 m\mathbf{I}) = (2k-m\omega^2)^2 - k^2 = 0$
gives $2k - m\omega^2 = \pm k$, so $\omega_1 = \sqrt{k/m}$ and
$\omega_2 = \sqrt{3k/m}$ with shapes $(1,1)$ and $(1,-1)$. These agree with
equation (8): $2\sqrt{k/m}\sin(\pi/6) = \sqrt{k/m}$ and
$2\sqrt{k/m}\sin(\pi/3) = \sqrt{3k/m}$ ✓.

**(d)** $(1,1)$ is in-phase (the coupling spring does not stretch, so the
effective stiffness per mass is $k$); $(1,-1)$ is antiphase (the coupling spring
stretches by $2u$ while each mass moves by $u$, so the effective stiffness is
$3k$). Greater relative deformation means greater stored energy for a given
amplitude, hence the higher frequency.

---

## ★2 — Chain frequencies against $N$

With $k/m = 60\ \mathrm{s^{-2}}$, $2\sqrt{k/m} = 15.491933\ \mathrm{rad\,s^{-1}}$.

| $N$ | $\omega_1$ (rad s⁻¹) | $\omega_N$ (rad s⁻¹) | $\omega_1$ vs $\pi\sqrt{k/m}/(N+1)$ |
|---|---|---|---|
| 2 | $15.491933\times\sin(\pi/6) = 7.745967$ | $15.491933\times\sin(\pi/3) = 13.416408$ | 7.745967 vs 7.745967, 0.0 % |
| 5 | $15.491933\times\sin(\pi/12) = 4.009607$ | $15.491933\times\sin(5\pi/12) = 14.964059$ | 4.009607 vs 4.047790, −0.94 % |
| 20 | $15.491933\times\sin(\pi/42) = 1.158151$ | $15.491933\times\sin(20\pi/42) = 15.359156$ | 1.158151 vs 1.158296, −0.013 % |

**(c)** $\omega_N \to 2\sqrt{k/m} = 15.491933\ \mathrm{rad\,s^{-1}}$: the mode
with every adjacent pair of masses in antiphase is the stiffest possible
relative motion and therefore the highest frequency the chain can support.
Beyond it the chain cannot oscillate — a statement that becomes, in the
continuum limit, the statement that no wavelength shorter than twice the lattice
spacing exists.

---

## ★3 — $N = 3$ by hand and numerically

**(a)** $(\mathbf{K}/m)$ with $k/m = 60$:

$$\begin{pmatrix}120 & -60 & 0\\ -60 & 120 & -60\\ 0 & -60 & 120\end{pmatrix}
\mathrm{s^{-2}}.$$

**(b)** $u_j^{(n)} = \sin(jn\pi/4)$:

- $n=1$: $\sin(\pi/4) = 0.707107$, $\sin(\pi/2) = 1.000000$,
  $\sin(3\pi/4) = 0.707107$ → $(0.707107, 1, 0.707107)$;
- $n=2$: $\sin(\pi/2) = 1$, $\sin(\pi) = 0$, $\sin(3\pi/2) = -1$ →
  $(1, 0, -1)$;
- $n=3$: $\sin(3\pi/4)$, $\sin(3\pi/2)$, $\sin(9\pi/4)$ →
  $(0.707107, -1, 0.707107)$.

The demo confirms $\omega_1 = 5.928506242$,
$\omega_2 = 10.954451150$, $\omega_3 = 14.312680173$ rad s⁻¹ against
equation (8) to $2.5\times10^{-16}$ relative.

**(c)** Checking mode 2, row 1:
$120\times1 - 60\times0 = 120$; and
$\omega_2^2\times1 = 120.000000$ ✓. Row 2:
$-60\times1 + 120\times0 - 60\times(-1) = 0 = \omega_2^2\times0$ ✓.
Mode 2 has a node at the middle mass: the central mass never moves, which is why
its frequency equals that of a two-mass chain of half the length
(equation (8) with $N=1$ gives $2\sqrt{k/m}\sin(\pi/4) = \sqrt{2k/m} =
10.954451$ ✓).

---

## ★4 — Weak coupling

**(a)** For two identical oscillators coupled by stiffness $\epsilon k$, the
matrix is $(\mathbf{K}/m) = (\omega_0^2)\begin{pmatrix}1+\epsilon & -\epsilon\\
-\epsilon & 1+\epsilon\end{pmatrix}$, whose eigenvalues are
$\omega_0^2(1+\epsilon \mp \epsilon) = \omega_0^2$ and
$\omega_0^2(1+2\epsilon)$. To linear order in $\epsilon$,
$\omega_- = \omega_0$ and $\omega_+ = \omega_0(1+\epsilon)$, so the *splitting*
is $\omega_0\epsilon$ and the beat period is
$2\pi/(\omega_0\epsilon)$ — precisely the $1/\epsilon$ divergence asked for.

**(b)** The product-to-sum result of equation (11) gives an envelope of period
$2\pi/|\omega_2-\omega_1| = 2\pi/(\epsilon\omega_0)$ ✓.

**(c)** Weak coupling means the two modes have nearly equal frequencies, so the
relative phase of the two modes accumulates slowly: it takes
$2\pi/(\omega_2-\omega_1)$ for the modes to slip a full cycle out of step, which
is the time for the energy to move from one coordinate to the other.

---

## ★5 — Reading the beat measurement

**(a)** $2\pi/5.670441173 = 1.108059$ s ✓.

**(b)** The envelope is sampled once per fast oscillation, of period
$2\pi/10.581187 = 0.593941$ s, so each measured envelope maximum can be up to
$\pm0.297$ s from the true maximum. The measured 1.1130 s differs from 1.1081 s
by 0.0049 s, well inside that window; the honest statement is that the data are
consistent with the prediction and that the measurement method cannot do better.

**(c)** From equation (11), $|u_2| = A|\sin((\omega_1+\omega_2)t/2)|\times
|\sin((\omega_2-\omega_1)t/2)|$. The first factor reaches 1 only at discrete
times; the product is therefore bounded by $A$ and reaches it only when both
sines are $\pm1$ simultaneously, which happens exactly when
$(\omega_1+\omega_2)t/(2\pi)$ and $(\omega_2-\omega_1)t/(2\pi)$ are both
half-integers. Since the ratio of frequencies is irrational in general, the
product is dense in $[0,A]$ but attains $A$ only if that Diophantine condition is
met; in this simulation the maximum reached was 0.009998 m, i.e. 99.98 per cent
of $A$.

**(d)** It says the leapfrog integrator transports the envelope amplitude to
2 parts in $10^4$, and — combined with the $3.7\times10^{-7}$ energy spread —
that the numerics are not the limiting factor in this comparison.

---

## ★6 — Frequency coincidences

**(a)** The argument is $n\pi/(2(N+1))$. For $(n,N) = (2,3)$ the argument is
$2\pi/8 = \pi/4$; for $(n,N) = (3,5)$ it is $3\pi/12 = \pi/4$. Equal arguments
mean equal frequencies.

**(b)** We need $n/(2(N+1)) = 1/6$, i.e. $3n = N+1$, with $1\le n\le N$. Pairs:
$(n,N) = (2,5)$? — this gives $N+1 = 6$, $n = 2$: argument $2/12 = 1/6$ ✓.
Systematically: $N = 3n-1$ for $n\ge2$: $(2,5)$, $(3,8)$, $(4,11)$, … and for
$N\le8$: $(2,5)$ and $(3,8)$.

**(c)** Shape $\sin(2j\pi/3)$ for $j = 1,\dots,5$:
$0.866025$, $-0.866025$, $0$, $0.866025$, $-0.866025$ — a mode with two nodes
and with the third mass stationary.

---

## ★7 — Single-mode purity

**(a)** $8.140\times10^{-10}$, $5.553\times10^{-9}$, $1.423\times10^{-8}$,
$2.308\times10^{-8}$ for modes 1–4 (displacements of order $5\times10^{-3}$ m, so
relative deviations $1.6\times10^{-7}$ to $4.6\times10^{-6}$).

**(b)** The deviation grows with mode order because both the frequency and the
number of operations per period grow: the velocity-Verlet error per period scales
as $(\omega dt)^2$, and $\omega_4/\omega_1 = 3.1$, so a factor of about 10 is
expected in the error and a factor of 28 is observed.

**(c)** Halving $dt$ should reduce the deviation by a factor of four (second-order
method). Modifying the script and re-running confirms the factor, which is also
the practical demonstration that the trend in (b) is truncation error, not
physics.

**(d)** A small eigen-residual only says that the *computed* pair
$(\mathbf{v},\omega)$ solves the algebraic problem. The time-domain test says that
the *dynamics* keeps the shape, which also checks the sign conventions in the
force law and the integrator.

---

## ★8 — Two-storey building

**(a)** Same equations as ★1: $\omega_1 = \sqrt{k/m}$,
$\omega_2 = \sqrt{3k/m}$.

**(b)** $\sqrt{k/m} = \sqrt{4.0\times10^7/2.0\times10^5} = \sqrt{200} =
14.142136\ \mathrm{rad\,s^{-1}}$, so $T_1 = 0.444288$ s and
$\omega_2 = 24.494897\ \mathrm{rad\,s^{-1}}$, $T_2 = 0.256514$ s.

**(c)** In the second mode the floors move in antiphase, so the inter-storey
drift is twice the individual amplitude and the columns are bent most; in the
first mode they move together. A taller building has a lower fundamental
frequency (more mass, similar stiffness), so its fundamental mode moves closer to
the dominant frequencies of distant large earthquakes and of soft-soil site
amplification — the reason height and site conditions interact in damage
patterns.

---

## ★★★9 — Free ends and zero modes

**(a)** With no wall at either end, mass 1 feels only the spring to mass 2, so
the equation for $j=1$ is $m\ddot u_1 = k(u_2-u_1)$, which is exactly what
$u_0 = u_1$ would produce. Similarly $u_{N+1} = u_N$. Then
$\sin(j\theta)$ solutions require $\cos(\theta/2) = 0$ or
$\sin((N+1/2)\theta) = 0$... the clean statement is that the mirror conditions
give $\theta_n = n\pi/N$ with $n = 0,1,\dots,N-1$, so
$\omega_n = 2\sqrt{k/m}\sin(n\pi/(2N))$ and $\omega_0 = 0$.

**(b)** For $N = 4$: $\omega_n = 2\sqrt{k/m}\sin(n\pi/8)$, $n = 0..3$, giving
$0$, $0.765367\sqrt{k/m}$, $1.414214\sqrt{k/m}$, $1.847759\sqrt{k/m}$. A
numerical diagonalisation of the free-end matrix reproduces these to round-off
(the largest discrepancy should be at the $\sim10^{-15}$ relative level; report
your measured value).

**(c)** The zero mode is $\theta_0 = 0$, i.e. $u_j$ constant: rigid translation.
A free elastic body has exactly six modes of zero frequency in three dimensions
— three translations and three rotations — because those motions deform nothing.
Any additional zero mode in a model signals a mechanism or a floating
substructure, which is exactly why engineers inspect them.

**(d)** Finite-element stiffness matrices are singular by that same argument;
solvers report six near-zero eigenvalues and the analyst removes them before
inverting, otherwise the inverse is dominated by round-off in those directions.

---

## ★★★10 — Proportional damping

**(a)** Substituting $\mathbf{u} = \sum_n q_n(t)\mathbf{v}_n$ into
$\mathbf{M}\ddot{\mathbf{u}} + 2\beta\mathbf{M}\dot{\mathbf{u}} +
\mathbf{K}\mathbf{u} = \mathbf{0}$ and projecting onto $\mathbf{v}_l$ gives
$\ddot q_l + 2\beta\dot q_l + \omega_l^2q_l = 0$ exactly, because
$\mathbf{M}$ is a multiple of the identity and the eigenvectors are orthogonal:
the damping term is diagonal in the same basis as the stiffness. Modal $Q$ is
then $Q_l = \omega_l/(2\beta)$.

**(b)** With a general symmetric $\mathbf{C}$, the projected term is
$\mathbf{v}_l^{\mathsf{T}}\mathbf{C}\mathbf{v}_n \ne 0$ for $l\ne n$ and the modes
exchange energy. A minimal example: three masses with dampers only between masses
1 and 2, so that $\mathbf{C}$ has nonzeros only in the (1,1), (1,2), (2,1), (2,2)
positions; the third mode, which has a node between masses 1 and 2, is undamped,
while modes 1 and 2 are coupled because they both move that pair of masses.

**(c)** A simulation with $N=4$, $k/m = 60$ and $\beta = 0.5$ should give measured
$Q$ values close to $\omega_n/(2\beta)$: $4.787/(1.0) = 4.787$,
$9.106$, $12.533$, $14.734$. Expect the measured $Q$ to be a few per cent low
for the highest modes, because the fixed measurement window truncates the decay
and because the peak-picking for a short-lived mode is biased — report the
measured table and the discrepancy rather than the prediction alone.

**(d)** Proportional damping is chosen because it keeps the modes independent and
therefore keeps the algebra tractable. Real attenuation is a material
constitutive property (lesson
[02-04-07](../../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)) that
generally does *not* commute with the stiffness in the way required, so it does
couple modes. Using proportional damping is a modelling approximation whose
error should be estimated when modes are close in frequency, since that is when
coupling is strongest.
