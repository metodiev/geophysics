# Solutions — 10-02-01 Survey Design

> Read after attempting. Lesson: [01 Survey Design](../01-gpr-survey-design.md).

---

## ★1 — Wavelength and spacing

$v = c/\sqrt{\varepsilon_r} = 0.299792458/4 = 0.074948\ \mathrm{m\,ns^{-1}}$;
$\lambda = v/f = 0.074948/0.1\ \mathrm{GHz} = 0.7495\ \mathrm{m}$.

$\Delta x = \lambda/(4\sin\theta_{\max})$: for $90^\circ$,
$\Delta x = 0.7495/4 = 0.1874\ \mathrm{m}$; for $30^\circ$,
$\Delta x = 0.7495/(4\times0.5) = 0.3748\ \mathrm{m}$.

---

## ★2 — Time window

Two-way time to $4.50\ \mathrm{m}$: $2\times4.50/0.07495 = 120.1\ \mathrm{ns}$;
plus a $15\ \mathrm{ns}$ guard: $135.1\ \mathrm{ns}$.

Samples at $0.05\ \mathrm{ns}$: $\lceil 135.1/0.05 \rceil = 2702$ samples.

---

## ★3 — Fresnel diameter and line spacing

$$D = 2\sqrt{\frac{\lambda d}{2} + \frac{\lambda^{2}}{16}}
= 2\sqrt{\frac{0.4996\times2.0}{2} + 0.01560}
= 2\sqrt{0.4996+0.0156} = 2\times0.7178 = 1.4356\ \mathrm{m}.$$

Detection probability is $\min(1, D/\Delta y)$, so it stays at one for
$\Delta y \le 1.4356\ \mathrm{m}$ and falls as $1.4356/\Delta y$ beyond that. At
$\Delta y = 2.0\ \mathrm{m}$ it would be $0.72$.

---

## ★4 — Grid size

Lines: $\lceil 15/0.30 \rceil + 1 = 51$. Traces per line:
$\lceil 25/0.05 \rceil + 1 = 501$. Total traces: $51\times501 = 25\,551$.

Profiled distance: $25\,551 \times 0.05 = 1278\ \mathrm{m}$ of line, i.e. $51$
passes of $25\ \mathrm{m}$.

---

## ★5 — Offset for an 8 ns moveout

$t_0 = 2\times2.0/0.075 = 53.333\ \mathrm{ns}$;
$t = 61.333\ \mathrm{ns}$.

$$x = v\sqrt{t^{2}-t_0^{2}} = 0.075\sqrt{61.333^{2}-53.333^{2}}
= 0.075\sqrt{3761.7-2844.4} = 0.075\times30.29 = 2.27\ \mathrm{m},$$

i.e. $1.14$ target depths.

Velocity error from a $0.25\ \mathrm{ns}$ pick error at that offset:

$$\delta v = \frac{v^{3}t\,\delta t}{x^{2}}
= \frac{4.219\times10^{-4}\times61.333\times0.25}{5.16} = 1.25\times10^{-3}\
\mathrm{m\,ns^{-1}}\ (1.67\%).$$

---

## ★6 — Cross-hole coverage estimate

Ray count: $15\times25 = 375$ rays from source to receiver positions, so the
panel receives $375$ straight paths.

Poorly covered regions: (i) the two top-corner triangles, since a ray from a deep
source to a shallow receiver (or vice versa) cannot reach them within the
aperture; (ii) the bottom-centre wedge, since rays connecting the deepest source
to the deepest receiver pass on either side; (iii) any pixel reached only by
near-vertical rays, which carry no lateral resolution because their crossing
angles are small. The demonstration's larger panel ($21\times21$, boreholes
$5\ \mathrm{m}$ apart over $10\ \mathrm{m}$) leaves $15\%$ of pixels with no ray
at all and only $25.1\%$ with five or more.

---

## ★★★7 — A complete design

Assumptions stated first: $\varepsilon_r = 12$ so
$v = 0.299792458/\sqrt{12} = 0.08655\ \mathrm{m\,ns^{-1}}$; a $200\ \mathrm{MHz}$
band with useful energy to about $500\ \mathrm{MHz}$; the deepest target of
interest is $3\ \mathrm{m}$; a $15\ \mathrm{ns}$ guard; a $0.05\ \mathrm{m}$
along-line step; and CMP offsets to $1.5\times$ the target depth.

- $\lambda = 0.08655/0.2 = 0.4328\ \mathrm{m}$.
- Trace spacing for $40^\circ$ dips:
  $\Delta x = 0.4328/(4\times0.643) = 0.168\ \mathrm{m}$; use
  $0.10\ \mathrm{m}$ for margin.
- Line spacing: from the detection rule at $d = 3\ \mathrm{m}$,
  $D = 2\sqrt{0.4328\times3/2 + 0.01171} = 2\sqrt{0.6609} = 1.626\ \mathrm{m}$;
  use $0.25\ \mathrm{m}$ so that both detection and lateral resolution are
  satisfied ($0.25 \le 0.4328/4\times$? — $\lambda/4 = 0.108\ \mathrm{m}$ is the
  resolution-grade spacing; $0.25\ \mathrm{m}$ is a compromise that must be
  declared).
- Offsets for $3\%$ velocity with $\delta t = 0.25\ \mathrm{ns}$:
  $x^2 \ge v^{2}t\,\delta t/0.03$ with $t \approx 2\times3.4/0.08655 = 78.6\
  \mathrm{ns}$ at the far offset: $x \ge \sqrt{(0.08655^{2}\times78.6\times
  0.25)/0.03} = \sqrt{4.90} = 2.2\ \mathrm{m}$.
- Time window: $2\times3/0.08655 + 15 = 84.3\ \mathrm{ns}$; at $0.05\ \mathrm{ns}$
  sampling, $1686$ samples.
- Volume: lines $= \lceil12/0.25\rceil+1 = 49$; traces per line
  $= \lceil50/0.10\rceil+1 = 501$; total $24\,549$ traces;
  $24\,549\times1686\times2\ \mathrm{bytes} = 82.8\ \mathrm{MB}$ (plus the CMP
  soundings).

---

## ★★★8 — Detection spacing versus resolution spacing

Detection: $\Delta y = D = 1.4356\ \mathrm{m}$ at $1.5\ \mathrm{m}$ — the
probability of *seeing* each target is one.

Resolution: two targets $0.4\ \mathrm{m}$ apart need a between-line sampling
finer than the migrated point-spread width. From the measurement in
[10-01-05 §4](../../01-gpr-principles/05-gpr-resolution.md), a $\pm2\ \mathrm{m}$
aperture at $1\ \mathrm{m}$ depth gives $0.225\ \mathrm{m} = 0.45\lambda$; at
$1.5\ \mathrm{m}$ with $\lambda = 0.4996\ \mathrm{m}$ the Fresnel diameter is
$1.250\ \mathrm{m}$, and the migrated width is of order $0.5\lambda = 0.25\
\mathrm{m}$. Separating $0.4\ \mathrm{m}$ therefore requires a line spacing of a
few tenths of a metre at most — **not** the $1.4\ \mathrm{m}$ detection spacing.
Recommended: $\Delta y \le 0.25\ \mathrm{m}$, and declared as a resolution
requirement rather than a detection one.
