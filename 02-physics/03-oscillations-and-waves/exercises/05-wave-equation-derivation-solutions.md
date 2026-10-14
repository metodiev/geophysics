# Solutions — 02-03-05 Deriving the Wave Equation from Continuum Physics

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Steel string

**(a)** $c = \sqrt{T/\mu} = \sqrt{80/0.020} = \sqrt{4000} = 63.245553\ \mathrm{m\,s^{-1}}$.

**(b)** $\lambda = c/f = 63.245553/440 = 0.143740$ m.

**(c)** The derivation assumed (i) the slope is small and (ii) the tension is
constant to first order. Raising the tension raises $c$ but does not by itself
violate either condition for a given amplitude — the slope condition depends on
$y_x$, not on $T$. What fails first at very large tension is the *material*
assumption: real steel yields or creeps, so the applied tension is no longer a
constant independent of the motion, and the linear derivation loses its
constitutive law. A practical answer is to check $\Delta L/L$ against the elastic
limit, which for steel is of order $10^{-3}$, so $T$ cannot be raised by two
orders of magnitude on the same wire without changing the wire.

---

## ★2 — Bar speed versus P speed

The derivation assumes (i) uniaxial stress — the rod is free to contract
laterally — and (ii) a uniform cross-section with plane sections remaining plane.

**(a)** $c_{\text{bar}} = \sqrt{73.6\times10^9/2700} = \sqrt{2.72593\times10^7} =
5221.05\ \mathrm{m\,s^{-1}}$ (using $E = 73.6$ GPa; with $E = 73.636364$ GPa the
value is 5222.33 m s⁻¹, and the difference is a demonstration of significant
figures at the fourth digit).

**(b)** $v_p = \sqrt{(25+2\times30)\times10^9/2700} = \sqrt{3.148148\times10^7} =
5610.84\ \mathrm{m\,s^{-1}}$.

**(c)** $v_p/c_{\text{bar}} = 5610.84/5222.33 = 1.074232$; and
$\sqrt{M/E} = \sqrt{85/73.636364} = \sqrt{1.154321} = 1.074394$ ✓ (the small
discrepancy is the significant-figure difference in $E$ noted above; with
consistent values the two agree exactly).

**(d)** In a three-dimensional P wave the material adjacent to a compressed
element cannot be pushed aside easily; it resists laterally, generating lateral
stress that adds to the restoring force. The effective stiffness is therefore the
constrained modulus $M = \lambda + 2\mu > E$, and the speed rises by
$\sqrt{M/E}$.

---

## ★3 — Grid parameters

**(a)** 10 points per 60 m gives $\Delta x = 6$ m.

**(b)** At the stability limit $r = 1$, $\Delta t = \Delta x/c = 6/2500 =
2.4\times10^{-3}$ s; in practice one takes $r = 0.5$, i.e.
$\Delta t = 1.2\times10^{-3}$ s.

**(c)** At $r = 0.5$, $N = 0.5/1.2\times10^{-3} = 417$ steps (418 to complete).

**(d)** Doubling $\Delta x$ to 12 m and using the new stability limit
$\Delta t = 4.8\times10^{-3}$ s (or $r=0.5$, $\Delta t = 2.4\times10^{-3}$ s)
halves the number of steps and halves the number of grid points, so the cost falls
by a factor of four in one dimension. The error rises by a factor of four, since
the scheme is second order. In three dimensions the same trade costs a factor of
sixteen in cost.

---

## ★4 — d'Alembert with a Gaussian

**(a)** With $\psi = 0$, equation (12) gives
$u(x,t) = \tfrac12\left[e^{-(x-t)^2} + e^{-(x+t)^2}\right]$ for $c=1$.

**(b)** At $t = 0$ there is a single Gaussian of unit height at $x=0$. At $t=0.5$
there are two Gaussians of height 0.5, centred at $x=\pm0.5$. At $t=2$ two
Gaussians of height 0.5 are centred at $x=\pm2$, having passed through each other
without changing shape.

**(c)** The domain of dependence of $(0,1)$ is the interval $[-1,1]$: only the
initial data there can influence it.

**(d)** The initial displacement splits equally between the right- and left-going
halves because the general solution is written as $\tfrac12[\phi(x-ct)+\phi(x+ct)]$.
The energy is likewise split in two, so each pulse carries half the initial
energy and has $1/\sqrt2$ of the amplitude of an independently generated pulse —
which is why comparing amplitudes across different source geometries requires
care.

---

## ★5 — Acoustic wave equation

**(a)** Linearise: momentum $\rho\mathbf{v}_t = -\nabla p$; mass conservation
$\rho_{1,t} + \rho_0\nabla\cdot\mathbf{v} = 0$; constitutive
$p = K\rho_1/\rho_0$. Taking the divergence of the momentum equation and
substituting gives $p_{tt} = (K/\rho_0)\nabla^2p$ ✓.

**(b)** With $\rho$ varying, the momentum equation must be written
$\rho\mathbf{v}_t = -\nabla p$ before dividing, so the divergence of
$\mathbf{v}_t = -\nabla p/\rho$ produces
$\nabla\cdot(\rho^{-1}\nabla p)$, not $\rho^{-1}\nabla^2p$. Using the constant-$\rho$
form across a density contrast ignores the reflection: the reflected amplitude
comes out zero, which is a 100 per cent error for a water–air interface.

**(c)** Water: $c = \sqrt{2.2\times10^9/1000} = 1483.24\ \mathrm{m\,s^{-1}}$. Air:
$c = \sqrt{1.42\times10^5/1.225} = 340.5\ \mathrm{m\,s^{-1}}$. The ratio is 4.36;
the density ratio is 816, so the speed ratio is much closer to unity than the
density ratio, because the bulk moduli also differ by four orders of magnitude.
This is a good reminder that both stiffness and inertia matter, and it is why
comparing media by density alone is a poor proxy for comparing their wave speeds.

---

## ★6 — The lattice dispersion relation

**(a)** From $\omega^2 = (4c^2/a^2)\sin^2(ka/2)$ take the positive root:
$\omega = (2c/a)\sin(ka/2)$. Then
$v_{\text{ph}} = \omega/k = c\,\sin(ka/2)/(ka/2)$ and
$v_g = d\omega/dk = (2c/a)(a/2)\cos(ka/2) = c\cos(ka/2)$ ✓.

**(b)** Let $x = ka/2$. Then $v_{\text{ph}}v_g = c^2\sin x\cos x/x =
c^2\sin(2x)/(2x) \le c^2$ because $\sin\theta \le \theta$ for $\theta\ge0$, with
equality only at $\theta = 0$ ✓.

**(c)** $\sin x/x > 0.99$ requires $x \lesssim 0.2444$ (solving numerically), so
$ka < 0.4888$, i.e. $\lambda/a = 2\pi/(ka) > 12.9$: about 13 points per
wavelength.

**(d)** The rule of thumb "10 points per wavelength" corresponds to a phase-velocity
error of about 1.7 per cent, and the demo's table confirms the error at
$ka = 0.5$ ($\approx12.6$ points per wavelength) is 1.4 per cent in $v_g$ and
1.0 per cent in $v_{\text{ph}}$. So 10 points is a *minimum*, not a safe default:
codes that need to propagate tens of wavelengths use 15–20 points, and the extra
cost buys a linear reduction in accumulated dispersion error.

---

## ★7 — Convergence

**(a)** Measured orders: 2.004, 1.998, 2.000, 2.000 — the code is demonstrated to
be second order.

**(b)** Because the scheme's error has the form
$\Delta t^2\,A + \Delta x^2\,B$ with both coefficients of the same order.
Halving $\Delta x$ at fixed $r$ halves $\Delta t$ as well, so both terms fall by a
factor of four.

**(c)** From $1.144\times10^{-4}$ at $\Delta x = 0.0125$ m, reaching $10^{-9}$
needs a factor of $1.14\times10^5$ in error, i.e. $\sqrt{1.14\times10^5} = 338$
times finer: $\Delta x \approx 3.7\times10^{-5}$ m.

**(d)** The number of grid points rises by 338 and the number of time steps by 338
(since $\Delta t \propto \Delta x$), so the work rises by $338^2 = 1.1\times10^5$
— about a hundred thousand times the cost for five more digits. In three
dimensions the factor is $338^4 = 1.3\times10^{10}$. This is the reason
high-order schemes exist.

---

## ★8 — Stability

**(a)** Measured growth per step: 1.836146 at $r = 1.05$ against the theoretical
1.877328; 3.409923 at $r = 1.20$ against 3.471980.

**(b)** The measured value is a lower bound because it is computed as
$(\text{peak}/\text{peak}_0)^{1/200}$ from the *maximum* over the grid, and the
fastest-growing mode is not the only mode present: early in the run the maximum
is dominated by modes that grow more slowly, and the asymptotic single-mode rate
is approached only after many steps.

**(c)** At $r = 1$ the numerical characteristics coincide with the physical
characteristics, so the grid values of the exact solution satisfy the scheme
identically — the scheme is exact for that initial data, and the demo shows the
maximum unchanged at 0.500000 after 200 steps.

**(d)** Three dimensions: $r \le 1/\sqrt3 = 0.577350$, so
$\Delta t \le 0.577350\times5/3000 = 9.62\times10^{-4}$ s, against
$1.67\times10^{-3}$ s in one dimension with the same $\Delta x$ and $c$ — a
factor of $\sqrt3$ less, and a correspondingly larger cost.

---

## ★★★9 — Layered media and impedance averaging

**(a)** $\rho u_{tt} = \partial_x(\mu u_x)$ expands to
$\rho u_{tt} = \mu u_{xx} + \mu_xu_x$; dividing by $\rho$ and writing
$c^2 = \mu/\rho$ gives $u_{tt} = c^2u_{xx} + (c^2\mu_x/\mu)u_x$: a wave equation
with a first-order term proportional to the gradient of the impedance $Z = \rho c$.

**(b)** The flux that must be continuous across an interface is $\mu u_x$, i.e. a
stress; the coefficient $\mu$ plays the role of a conductivity in a flux law, and
for a flux-law coefficient the correct average over a cell straddling an interface
is the harmonic mean (the arithmetic mean of the resistances). Averaging
arithmetically produces a spurious impedance and therefore a wrong reflection
coefficient.

**(c)** The lesson's demo uses the harmonic mean and reproduces
$R = (Z_1-Z_2)/(Z_1+Z_2) = -0.304348$ to within $1.6\times10^{-3}$ (measured
$-0.302777$) and $T$ to within $1.0\times10^{-3}$ (measured $0.694611$ against
$0.695652$). With the arithmetic mean, the effective impedance at the interface
becomes the arithmetic average of $Z_1$ and $Z_2$, so the reflection coefficient
is systematically too small — report your measured value and its error.

**(d)** In numerical schemes for variable media, the property that must be
conserved across a face (a flux) dictates the averaging rule: harmonic mean for
the coefficient multiplying the gradient, arithmetic mean for the density
multiplying the acceleration, and never a single average for both. Getting this
wrong is a common and hard-to-spot modelling error because the scheme remains
stable and only the amplitudes are wrong.

---

## ★★★10 — Another system

A worked example with the shallow-water channel:

**(a)** Linearised shallow-water flow with depth $h_0$ obeys
$\eta_{tt} = g h_0\,\eta_{xx}$, where $\eta$ is the surface elevation: stiffness
$gh_0$ (gravity acting on a displaced surface), inertia per unit length set by the
water column. The speed is $c = \sqrt{gh_0}$.

**(b)** For $h_0 = 4000$ m, $c = \sqrt{9.80665\times4000} = 198.06$ m s⁻¹. For a
trans-ocean tsunami this is the standard order quoted in tsunami warning
literature — check a published travel-time chart for the ocean basin of interest
and compare.

**(c)** Shallow-water theory assumes the wavelength is much longer than the depth
and that the amplitude is small compared with the depth. The first assumption
fails in the deep ocean for short waves (which then obey the deep-water
dispersion relation instead), and the second fails at run-up, where the linear
equation cannot describe the bore. The observable consequence is dispersion in
the deep ocean — long-period components outrun short ones — and the formation of
a steep front in shallow water.

**(d)** A program using the explicit scheme of this lesson with
$g h_0 = 3.92\times10^5$ m² s⁻² should show second-order convergence and the
Courant limit $\Delta t \le \Delta x/\sqrt{gh_0}$; report your measured order and
your measured stability boundary.
