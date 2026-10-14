# Solutions — 12-07-02 Icy Moons, Subsurface Oceans and Induction Studies

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [02 Icy Moons, Subsurface Oceans and Induction Studies](../02-icy-moons.md).

---

## ★1 — Skin depth

$$
\delta = \sqrt{\frac{2}{\omega\mu_{0}\sigma}},
\qquad
\omega = \frac{2\pi}{5\times10^{4}} = 1.2566\times10^{-4}\ \mathrm{s^{-1}},
$$

$$
\delta = \sqrt{\frac{2}{(1.2566\times10^{-4})(4\pi\times10^{-7})(0.05)}}
= \sqrt{\frac{2}{7.8957\times10^{-12}}}
= \sqrt{2.5330\times10^{11}} = 5.033\times10^{5}\ \mathrm{m} = 503.3\ \mathrm{km}.
$$

The ratio to a 20 km layer is $503.3/20 = 25.2$: the skin depth is 25 times the
layer thickness, so the field changes by only a few percent across the layer. The
layer is **electromagnetically thin**, and the response depends on
$\sigma d = 0.05\times20\times10^{3} = 1000$ S. It is a marginal conductance: the
lesson's scan puts $C = 10^{3}$ S at $|Q| = 0.0129$, on the edge of
measurability.

---

## ★2 — The induction equation and its boundary conditions

For a poloidal field written through the radial function $h$ as

$$
B_{r} = \frac{n(n+1)}{r^{2}}h\,P_{n}(\cos\theta),
\qquad
B_{\theta} = \frac{h'}{r}\frac{\partial P_{n}}{\partial\theta},
$$

the quasi-static diffusion equation in a spherically symmetric conductor is

$$
h'' - \frac{n(n+1)}{r^{2}}h = i\omega\mu_{0}\sigma\,h .
$$

**Boundary conditions at each interface:** $h$ continuous and $h'$ continuous.
The first follows from continuity of $B_{r}$ (no magnetic monopoles), the second
from continuity of $B_{\theta}$ (no surface current in the absence of a
perfectly conducting sheet).

**Why no first-derivative term?** Because the representation already contains the
radial divergence: $B_{r}\propto h/r^{2}$ and $B_{\theta}\propto h'/r$ are
constructed so that $\nabla\cdot\mathbf{B} = 0$ identically. The resulting
operator $h''-n(n+1)h/r^{2}$ has the exact potential solutions $h\propto r^{n+1}$
(regular interior) and $h\propto r^{-n}$ (exterior), which is what makes the
insulating-region matching algebra work. Adding a $2h'/r$ term — the form that
belongs to the *potential* rather than to $h$ — gives a different operator whose
solutions are not those two powers, and the boundary-value problem then fails its
insulating limit. That is the single most common implementation error in this
problem, and the demonstration's $\sigma = 0$ check is designed to catch it.

---

## ★3 — Conductance and response

$$
C = \sigma d = 1\ \mathrm{S\,m^{-1}}\times5\times10^{3}\ \mathrm{m}
= 5\times10^{3}\ \mathrm{S}.
$$

From the lesson's table (period $10^{5}$ s):

$$
|Q| = 0.0646,
\qquad
\arg Q = 82.54^{\circ} .
$$

Two features are worth naming. The amplitude is small — the induced field is 6.5%
of the driving field — because the layer is thin and only moderately conducting.
The phase is close to $90^{\circ}$, the signature of a response proportional to
$\mathrm{d}B/\mathrm{d}t$: at low conductance the induced current follows the rate
of change of the field, exactly as in an inductor. A measurement in this regime
must therefore have a well-understood amplitude normalisation, because the signal
is small and the information is carried by the phase.

---

## ★4 — Conductance collapse

| $\sigma$ (S/m) | $d$ (km) | $C = \sigma d$ (S) | $|Q|$ | $\arg Q$ |
|---|---|---|---|---|
| 1.0 | 5 | $1.0\times5\times10^{3} = 5.0\times10^{3}$ | 0.0646 | $82.54^{\circ}$ |
| 0.5 | 10 | $0.5\times10\times10^{3} = 5.0\times10^{3}$ | 0.0640 | $82.58^{\circ}$ |
| 0.2 | 25 | $0.2\times25\times10^{3} = 5.0\times10^{3}$ | 0.0621 | $82.69^{\circ}$ |
| 0.1 | 50 | $0.1\times50\times10^{3} = 5.0\times10^{3}$ | 0.0591 | $82.87^{\circ}$ |

All four conductances are equal, and the amplitudes agree to about ten percent.

**Why they differ at all.** The collapse is exact only in the limit
$d\ll\delta$, i.e. an infinitesimally thin shell. At finite $d/\delta$ the field
decays *inside* the layer, so the current distribution has a radial profile and
the geometric factor that turns $|Q|$ into a conductance depends weakly on $d$:
thicker layers screen slightly less per unit conductance because their inner parts
carry less current. The measured trend — larger $d$ giving slightly smaller
$|Q|$ at fixed $C$ — is that effect, and it is the only handle (a weak one) that
a single frequency gives on the thickness.

---

## ★5 — Inverting an amplitude with an error bar

The response scales as a power law near this operating point:
$|Q|\propto C^{0.700}$. To go from $|Q| = 0.2724$ at $C = 2500$ S to
$|Q| = 0.30$:

$$
C = 2500\left(\frac{0.30}{0.2724}\right)^{1/0.700}
= 2500\,(1.1013)^{1.4286}
= 2500\times1.1479 = 2.87\times10^{3}\ \mathrm{S}.
$$

A 3% error in $|Q|$ propagates to

$$
\frac{\delta C}{C} = \frac{1}{0.700}\frac{\delta |Q|}{|Q|}
= \frac{0.03}{0.700} = 0.0429 = 4.3\%,
$$

so $C$ is admitted between $2.87\times10^{3}\times(1\mp0.043)$, i.e.
$2.75\times10^{3}$ S to $3.00\times10^{3}$ S.

**Would the phase help?** No, not by itself: the phase and the amplitude are both
functions of the same single number $C$ (and weakly of $d$), so they carry the
same information and combining them does not break the degeneracy. It does
improve the precision — an independent phase measurement with a comparable
relative error halves the variance in $C$ — but it does not separate $\sigma$
from $d$.

---

## ★6 — The perfect-conductor limit

Let the shell become a perfect conductor, so the interior field must vanish:

$$
\mathbf{B}_{\text{in}} = 0
\qquad\Longrightarrow\qquad
I = 0 .
$$

Continuity of $B_{r}$ at $r = a$ (using the potential expansions
$V_{\text{ext}} = Er^{n} + Qa^{2n+1}r^{-(n+1)}$ and $V_{\text{in}} = Ir^{n}$ with
$B_{r} = -\partial V/\partial r$):

$$
-\left[nE\,a^{n-1} - (n+1)Q\,a^{n-1}\right]_{\text{out}}
= -\left[nI\,a^{n-1}\right]_{\text{in}} = 0 ,
$$

so

$$
nE - (n+1)Q = 0
\qquad\Longrightarrow\qquad
\frac{Q}{E} = \frac{n}{n+1},
\qquad
\left|\frac{Q}{E}\right|_{n=1} = \frac{1}{2} = 0.5000 .
$$

The demonstration reaches $|Q| = 0.499881$ at $\sigma = 10^{6}$ S/m with
$|I| = 1.55\times10^{-17}$, i.e. the interior field is numerically zero and the
response sits at the geometric ceiling. Two consequences: the ceiling is
geometric (it depends only on the harmonic degree), and a measurement near it
carries almost no information about the conductance.

---

## ★7 — A two-frequency specification

**The idea.** The collapse of §4 happens because the layer is thin compared with
the skin depth. Two frequencies with very different skin depths can put the layer
in two different regimes: at the higher frequency $\delta$ may become comparable
to or smaller than $d$, so the response starts to depend on $d$ separately.

**The frequencies.** Take $f_{1}$ such that $\delta(f_{1})\sim 10d$ (the linear,
conductance-dominated regime, which fixes $C$ precisely) and $f_{2}$ such that
$\delta(f_{2})\sim d$ (the saturated regime, where the response depends on $d$
through the internal field profile). Concretely, $\delta\propto\omega^{-1/2}$, so
a factor 100 in frequency changes $\delta$ by 10.

**The precision needed.** In the saturated regime the sensitivity
$\mathrm{d}\ln|Q|/\mathrm{d}\ln C$ falls to a few percent (the demonstration
measures $0.0228$ at the saturated end), so the second frequency must be measured
to well under 1% to say anything about $d$: a 1% amplitude error in a regime with
sensitivity $0.02$ admits a 50% range in $C$. This is the quantitative reason
that separating $\sigma$ from $d$ is hard, and why most induction studies report a
conductance with an assumed layer thickness.

**The assumption that remains.** A single uniform layer. A depth-dependent
conductivity (which is physically expected — conductivity rises with pressure and
temperature) makes the response a superposition over depth, and two frequencies
cannot determine a function. The recovery of a profile requires a multi-frequency
inversion with its own null space: the honest deliverable is a *conductance
profile* with stated resolution.

---

## ★8 — Partial shells and what they do

**Scaling argument.** The response of a conducting region is proportional to the
total induced current, and the induced current is the integral of $\sigma$ times
the tangential electric field over the conducting volume. For a full thin shell
the current flows in closed latitude circles around the body, encircling the
polar axis, and its magnetic effect adds coherently. For a partial cap of angular
extent, (i) the total path length available is shorter, and (ii) the return
currents must close through the non-conducting region, which forces the current
system into a smaller effective loop. Both effects reduce the induced field
approximately in proportion to the conducting area fraction, so to first order

$$
|Q|_{\text{partial}} \sim f\,|Q|_{\text{full}},
\qquad f\sim\frac{\text{conducting area fraction}}{1},
$$

with an additional dependence on where the cap is relative to the driving field's
symmetry axis. Physically: the induced field of a small cap is closer to that of a
small current loop than to that of a global shell.

**Consequence for the inversion.** Using a full-shell model on a partial-shell
body *underestimates* the conductance — the model must work harder to produce the
same field. The bias is of order $1/f$ and can be a factor of several for a small
cap, which is far larger than the few-percent statistical error of a good
measurement. Reporting a conductance without the assumed geometry therefore
overstates the result.

**What breaks the ambiguity.** A second harmonic degree. The responses for $n=1$
and $n=2$ weight the conducting region differently (different Legendre weights of
the induced current), so the *ratio* of the two responses is sensitive to the
geometry in a way that a single degree is not. A mission that measures the
induced field at two harmonics therefore constrains both the conductance and the
geometry — this is the standard argument for measuring the field at more than one
spatial scale, and it is a statement about *where* the conductor is rather than
*how* conductive it is.
