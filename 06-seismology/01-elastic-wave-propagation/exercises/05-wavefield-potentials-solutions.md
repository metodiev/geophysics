# Solutions — 06-01-05 Helmholtz Decomposition and Wavefield Potentials

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [05 Wavefield Potentials](../05-wavefield-potentials.md).

---

## ★1 — The decomposition and its gauge

Two dimensions (the case used in the lesson):

$$\mathbf u = \nabla\phi + \nabla\times(\psi\hat{\mathbf z}),
\qquad \nabla\times\nabla\phi = 0,\quad \nabla\cdot\nabla\times(\psi\hat{\mathbf z}) = 0 .$$

Three dimensions:

$$\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi,
\qquad \nabla\cdot\boldsymbol\psi = 0 .$$

**Gauge freedom.** Adding a constant to $\phi$ changes nothing, because only
$\nabla\phi$ enters $\mathbf u$. In three dimensions one may additionally add
$\nabla\chi$ to $\boldsymbol\psi$ for any scalar $\chi$: this changes
$\boldsymbol\psi$ but $\nabla\times(\boldsymbol\psi + \nabla\chi) =
\nabla\times\boldsymbol\psi$ when $\nabla^2\chi = 0$. Physically the gauge freedom
is the statement that the *decomposition* — not the potentials — is the observable
quantity: the dilatation $\nabla\cdot\mathbf u = \nabla^2\phi$ and the rotation
$\nabla\times\mathbf u = -\nabla^2\boldsymbol\psi$ are gauge-invariant.

---

## ★2 — Grid, Nyquist and resolvability

$$\Delta x = \frac{L}{n} = \frac{1.0}{256} = 3.90625\times10^{-3}\ \mathrm{m}.$$

Nyquist wavenumber $k_{\max} = \pi/\Delta x = 804.2\ \mathrm{rad\,m^{-1}}$.

The injected P wavenumber is

$$\lvert\mathbf k_P\rvert = \sqrt{18.8496^{2} + 6.2832^{2}}
= \sqrt{355.31 + 39.478} = \sqrt{394.79} = 19.869\ \mathrm{rad\,m^{-1}},$$

with wavelength $\lambda = 2\pi/19.869 = 0.3162\ \mathrm{m}$, i.e. 81 grid points
per wavelength. It is comfortably resolvable ($k \ll k_{\max}$). The S
wavenumber $\sqrt{6.2832^{2} + 25.1327^{2}} = \sqrt{39.478 + 631.65} =
25.906\ \mathrm{rad\,m^{-1}}$, wavelength $0.2425\ \mathrm{m}$, 62 points per
wavelength — also well resolved.

---

## ★3 — The undetermined zero mode

On a periodic domain, taking the Fourier transform of $\nabla^2\phi =
\nabla\cdot\mathbf u$ gives $-k^2\hat\phi = \mathrm{i}\mathbf k\cdot\hat{\mathbf u}$.
At $\mathbf k = 0$ both sides vanish identically, so $\hat\phi(0)$ is not
determined by the equation: changing $\phi$ by a constant changes nothing in
$\mathbf u$. The demonstration sets that mode aside (its code assigns a harmless
value to $k^2 = 0$ to avoid dividing by zero) and **removes the mean from both
sides** before comparing. The reported error therefore measures the non-constant
part only, which is the part that is physically defined — a detail that would be
easy to hide, and which the demonstration prints explicitly.

---

## ★4 — Why the errors are at round-off

On a periodic grid the Fourier spectral derivative is **exact** for band-limited
data: multiplying by $\mathrm{i}k$ is the derivative operator, not a
discretisation of it. There is no truncation error to make; the only error
available is floating-point rounding in the FFT, the multiplication and the
inverse FFT.

The contrast with a finite difference is worth quantifying. The second-order
central difference has relative error of order $(k\Delta x)^2/6$; for the P mode
with $k\Delta x = 19.869 \times 3.906\times10^{-3} = 7.76\times10^{-2}$,

$$\frac{(k\Delta x)^2}{6} = \frac{6.02\times10^{-3}}{6} = 1.0\times10^{-3},$$

i.e. about $10^{-3}$ — thirteen orders of magnitude larger than the reported
$3\times10^{-16}$. Because the demonstration uses the spectral operator, the
truncation term is absent by construction, and the measured error is exactly the
machine precision of a double-precision FFT chain. A measured error of $10^{-3}$
here would have meant the derivative was computed by finite differences, not
spectrally.

---

## ★5 — The P share of the energy

$$\frac{\sum\lvert\nabla\phi\rvert^{2}}
{\sum\lvert\nabla\phi\rvert^{2} + \sum\lvert\nabla\times(\psi\hat{\mathbf z})\rvert^{2}}
= \frac{1.293629\times10^{7}}{1.293629\times10^{7} + 5.497922\times10^{6}}
= \frac{1.293629\times10^{7}}{1.8434212\times10^{7}} = 0.701754 .$$

This matches the printed value exactly. Note what the number is *not*: it is the
energy share of the potentials that the demonstration chose to inject, not a
property of the decomposition. A different pair of injected potentials would give
a different share with the same machinery.

---

## ★6 — Why the cross term is exactly zero

The cross term is $\int 2\nabla\phi\cdot\nabla\times(\psi\hat{\mathbf z})\,
\mathrm{d}A$. Integrating by parts,

$$\int \nabla\phi\cdot\nabla\times(\psi\hat{\mathbf z})\,\mathrm{d}A
= -\int\phi\,\nabla\cdot\nabla\times(\psi\hat{\mathbf z})\,\mathrm{d}A
+ \oint\phi\,\nabla\times(\psi\hat{\mathbf z})\cdot\hat n\,\mathrm{d}s .$$

The divergence of a curl is **identically** zero, and on a periodic domain the
boundary integral vanishes because contributions from opposite edges cancel. The
two remaining contributions are therefore exactly zero as a matter of vector
calculus, and the residual $1.605827\times10^{-11}$ is the round-off of the two
large integrals ($\sim10^{7}$) cancelling: $1.6\times10^{-11}/10^{7} =
1.6\times10^{-18}$, i.e. a few units in the last place of a double.

This is the check that matters most in the lesson: it verifies that the
decomposition is an **orthogonal** decomposition, which is the reason the P and S
energies may simply be added. If the decomposition were not orthogonal, the
statement "70% of the energy is in P" would have no meaning.

---

## ★★★7 — The three-dimensional case (worked derivation)

In three dimensions write

$$\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi,
\qquad\nabla\cdot\boldsymbol\psi = 0,$$

which expands into **four** scalar fields ($\phi$ plus the three components of
$\boldsymbol\psi$) subject to **one** constraint ($\nabla\cdot\boldsymbol\psi =
0$), i.e. three independent scalars — as it must be, since $\mathbf u$ has three
components.

The two-dimensional shortcut replaces the vector $\boldsymbol\psi$ by
$\hat{\mathbf z}\psi$ with $\psi$ a scalar. That field automatically satisfies
$\nabla\cdot(\psi\hat{\mathbf z}) = \partial_z\psi$, which is zero only if $\psi$
does not depend on $z$. Two-dimensional problems are defined by
$\partial/\partial z = 0$ (plane strain), and it is *that* assumption, not the
decomposition, that makes the scalar shortcut work. In three dimensions one needs
the full vector potential, two more scalar fields, and a solution for the
constraint; the SH part of the field in a laterally varying 3-D medium cannot be
described by a single scalar.

---

## ★★★8 — Surface-array design (specification)

**Geometry.** A 2-D surface array with station spacing $\Delta x$ on a grid of
$2^{m}$ points in each horizontal direction, giving $k_{\max} = \pi/\Delta x$ and
$k_{\min} = 2\pi/L$. For a target band up to $k_t$, choose $\Delta x \le \pi/k_t$
and $L \ge 2\pi/k_{\min}$ for the smallest wavenumber of interest. Record three
components, so the vector field is sampled rather than a single projection.

**Band.** State the band explicitly, e.g. $0.05 \le k \le 1.0\
\mathrm{rad\,m^{-1}}$, and taper the data to control wraparound.

**Test.** Compute $\phi$ and $\boldsymbol\psi$ in the wavenumber domain and then
apply two independent checks: (i) the residual
$\lVert\mathbf u - \nabla\phi - \nabla\times\boldsymbol\psi\rVert /
\lVert\mathbf u\rVert$ must be at round-off; (ii) the cross term
$\int\nabla\phi\cdot\nabla\times\boldsymbol\psi$ must vanish relative to the
energies. Both are the same checks the demonstration performs, now on measured
data.

**What the array cannot determine.** A surface array samples a *boundary*, not a
volume. The decomposition of a boundary field is not unique: the field on the
surface can be produced by many volume fields, and in particular the upward
continuing (evanescent) part is not determined by the surface values in the
absence of an assumption about what lies below. Any statement about $\phi$ and
$\boldsymbol\psi$ separated in depth from a surface array alone is therefore
conditional — the classic ambiguity that separates "decomposition of the recorded
vector field" from "decomposition of the wavefield in the Earth".

---

## ★★★9 — Why a non-periodic field fails (three explanations)

1. **Spectral leakage from the implicit periodisation (largest effect).** The
   FFT treats the field as periodic; a non-periodic edge creates a jump that
   spreads energy into every wavenumber. For a field with a comparable power
   spectrum this can dominate, and it is the standard explanation for errors of
   order $10^{-1}$. *Cheapest fix:* multiply by a smooth (e.g. cosine) taper
   before transforming, and state the taper width.
2. **Aliasing of the derivative at high wavenumber (medium).** The spectral
   derivative is exact only for band-limited data; a jump contains energy above
   $k_{\max}$ that folds back and contaminates the recovered potentials. This
   typically contributes a few per cent. *Cheapest fix:* low-pass filter the field
   to a stated fraction of $k_{\max}$ before differentiating.
3. **The zero mode and the mean (smallest).** The undetermined $\hat\phi(0)$
   contaminates only the constant part of the solution; removing means removes it.
   *Cheapest fix:* subtract the mean from $\phi$ and $\psi$ before comparing, as
   the demonstration does.

Ranked as above, the repair order is: taper, filter, then subtract means. A
report that does none of the three and attributes the error to "the Fourier method
being approximate" has misdiagnosed all three.
