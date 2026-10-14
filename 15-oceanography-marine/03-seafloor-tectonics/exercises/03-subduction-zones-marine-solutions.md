# Solutions — 15-03-03 Marine Subduction Zones, Trenches and Accretionary Prisms

> **Read after attempting the exercises.** Lesson:
> [03 Marine Subduction Zones](../03-subduction-zones-marine.md). All numbers use
> the lesson's SYNTHETIC model constants.

## ★ Foundational

## ★1 — Critical taper and slope

$\beta=4^\circ=0.069813\ \mathrm{rad}$, $K=3.000$, $\mu_b=0.55$, $\lambda=0.30$:

$$\theta=\frac{\mu_b(1-\lambda)+\beta}{K(1-\lambda)}
=\frac{0.55\times0.70+0.069813}{3.000\times0.70}
=\frac{0.385+0.069813}{2.100}=0.216578\ \mathrm{rad}=12.41^\circ,$$

$$\alpha=\theta-\beta=0.216578-0.069813=0.146765\ \mathrm{rad}=8.41^\circ .$$

Note that raising $\lambda$ from 0.40 to 0.30 would *lower* the slope if
$\beta$ were unchanged; here the higher basal dip (4° instead of 3°) offsets it
almost exactly, and $\alpha=8.41^\circ$ is close to the lesson's $9.17^\circ$.

## ★2 — Rigidity and flexural parameter

$$D=\frac{ET_e^3}{12(1-\nu^2)}
=\frac{7.0\times10^{10}\times(2.0\times10^4)^3}{12\times0.9375}
=\frac{7.0\times10^{10}\times8.0\times10^{12}}{11.25}
=4.9778\times10^{22}\ \mathrm{N\,m}.$$

Unit check: $\mathrm{Pa}\times\mathrm{m^3}=\mathrm{N\,m}$; the denominator is
dimensionless. ✔

$$\alpha_f=\left(\frac{4D}{\Delta\rho g}\right)^{1/4}
=\left(\frac{1.99111\times10^{23}}{2270\times9.81}\right)^{1/4}
=\left(8.9412\times10^{18}\ \mathrm{m^4}\right)^{1/4}=5.47\times10^4\ \mathrm{m}
=54.7\ \mathrm{km}.$$

Thinning $T_e$ from 30 to 20 km reduces $D$ by a factor
$(20/30)^3=0.296$ and $\alpha_f$ by $0.296^{1/4}=0.738$: the flexural length is a
weak function of plate thickness, which is why $T_e$ is hard to determine from a
bulge wavelength alone.

## ★3 — Deflection and bulge

$$w_0=\frac{P\alpha_f^3}{8D}=\frac{2.0\times10^{12}\times(7.412\times10^4)^3}
{8\times1.68\times10^{23}}
=\frac{2.0\times10^{12}\times4.0720\times10^{14}}{1.344\times10^{24}}
=605.9\ \mathrm{m}.$$

Bulge: $w_0e^{-\pi}=605.9\times0.043214=26.2\ \mathrm{m}$ at
$x=\pi\alpha_f=232.8\ \mathrm{km}$.

The deflection is 33% smaller than the lesson's 908.8 m because the load is 33%
smaller — the relation is linear in $P$. The bulge *position* is unchanged,
because it depends only on $\alpha_f$.

## ★★ Applied

## ★4 — Doubling the slope with pore pressure

$\alpha(\lambda)=\dfrac{\mu_b}{K}+\dfrac{\beta}{K(1-\lambda)}-\beta$. At
$\lambda=0.40$: $\alpha=0.183333+0.029089-0.052360=0.160062\ \mathrm{rad}
=9.171^\circ$; doubled, $\alpha=0.320124\ \mathrm{rad}$. Solving,

$$\frac{0.052360}{3(1-\lambda)}=0.320124+0.052360-0.183333=0.189151
\;\Rightarrow\;1-\lambda=\frac{0.052360}{3\times0.189151}=0.09227,$$

so $\lambda=0.9077$, i.e. a pore-pressure ratio of 0.91 against 0.40 — a
décollement supporting only 9% of the lithostatic load.

**Is it attainable?** Only marginally, and not within this model. Three limits:
(i) a frictional décollement needs positive effective normal stress to transmit
shear, so $\lambda\to1$ removes the very mechanism the taper relation assumes;
(ii) at such pressures the décollement would dilate or hydrofracture, so the
system would not be steady; (iii) the *internal* pore pressure $\lambda$ appears
in $K(1-\lambda)$ too, and the wedge would fail internally before reaching this
slope. The physically honest conclusion: the slope cannot be doubled by pore
pressure alone in a frictional wedge; a genuine doubling requires a change in the
material (a weak, creeping décollement, i.e. a different constitutive law).

## ★5 — Prism budget

Volume flux: $q=h_sv_c=500\ \mathrm{m}\times0.060\ \mathrm{m\,yr^{-1}}
=30\ \mathrm{m^2\,yr^{-1}}=30\ \mathrm{km^3\,Myr^{-1}\,km^{-1}}$.

$A=f_aqt$ with $t=5\ \mathrm{Myr}=5\times10^6$ yr:

- $f_a=0.25$: $A=0.25\times30\times5\times10^6=3.75\times10^7\ \mathrm{m^2}
  =37.5\ \mathrm{km^2}$;
  $w=\sqrt{2A/\tan\theta}=\sqrt{2\times3.75\times10^7/0.2157}=1.86\times10^4\
  \mathrm{m}=18.6\ \mathrm{km}$.
- $f_a=0.75$: $A=1.125\times10^8\ \mathrm{m^2}=112.5\ \mathrm{km^2}$;
  $w=\sqrt{2\times1.125\times10^8/0.2157}=3.23\times10^4\ \mathrm{m}
  =32.3\ \mathrm{km}$.

Width ratio $=32.3/18.6=1.74=\sqrt{3}$, exactly the $\sqrt{f_a}$ scaling, since
the accreted fraction changed by a factor 3. **The width is a weak function of
the accretion efficiency**, so matching a prism's width to a convergence history
is a weak test; matching its *area* (or its cross-sectional volume) is a strong
one.

## ★6 — Fibre stress at two thicknesses

At $T_e=30$ km: $\sigma=6M_0/T_e^2=6\times5.5588\times10^{16}/(3\times10^4)^2
=3.71\times10^8\ \mathrm{Pa}=371\ \mathrm{MPa}$ (the lesson's value).

At $T_e=20$ km with the deflection held at 908.8 m: $D=4.9778\times10^{22}$,
$\lambda_f=(22268.7/(4D))^{1/4}=1.8284\times10^{-5}\ \mathrm{m^{-1}}$,
$P=908.8\times8D\lambda_f^3=2.2126\times10^{12}\ \mathrm{N\,m^{-1}}$,
$M_0=P/(4\lambda_f)=3.0253\times10^{16}\ \mathrm{N}$, and

$$\sigma=\frac{6\times3.0253\times10^{16}}{(2\times10^4)^2}
=4.538\times10^8\ \mathrm{Pa}=454\ \mathrm{MPa}.$$

**Scaling.** Holding the deflection fixed, $w_0\propto P\alpha_f^3/D$ and
$\alpha_f\propto D^{1/4}$, so $P\propto D/\alpha_f^3\propto D^{1/4}$; then
$M_0=P/(4\lambda_f)\propto D^{1/4}\alpha_f\propto D^{1/2}$, and
$\sigma\propto M_0/T_e^2\propto D^{1/2}/T_e^2\propto T_e^{3/2}/T_e^2=T_e^{-1/2}$.
So $\sigma(20)=\sigma(30)\sqrt{30/20}=371\times1.2247=454.4\ \mathrm{MPa}$,
matching the direct calculation. It is **not** $\propto T_e^{-2}$ because $M_0$
itself grows as the plate thins: the loads that produce a given deflection are
larger on a weaker plate.

## ★★★ Research-oriented

## ★7 — Determining the taper's unknowns

The unknowns are $\mu_b(1-\lambda_b)$ (the décollement's *effective* friction),
$\lambda$ (the wedge's internal pore pressure) and $K$ (the internal stress
ratio). Candidate measurements:

| measurement | determines | realistic precision |
|---|---|---|
| bathymetry + seismic depth to the décollement | $\theta$ (hence $\alpha$, $\beta$) | $\pm0.1$–$0.5^\circ$ on $\alpha$ |
| décollement lithology and friction experiments | $\mu_b$ | factor $\sim2$ (scale dependence) |
| internal friction from rock mechanics | $\phi$, hence $K$ if the stress state is assumed | $\pm5^\circ$ on $\phi$ |
| heat flow across the prism (advective perturbation) | direction and rate of décollement fluid flow | sign of the anomaly, order of magnitude of the flux |
| amplitude-vs-offset of the décollement reflection | pore-pressure contrast at the interface | $\pm0.1$–$0.2$ on $\lambda_b$ in favourable cases |

**Requirement for $\pm1$ MPa.** At 3 km depth with $\rho=2700\
\mathrm{kg\,m^{-3}}$, the lithostatic stress is
$\rho gH=2700\times9.81\times3000=7.95\times10^{7}\ \mathrm{Pa}=79.5\ \mathrm{MPa}$;
$\sigma'_n=(1-\lambda_b)\rho gH$, so $\mathrm{d}\sigma'_n/\mathrm{d}\lambda_b
=-79.5\ \mathrm{MPa}$ per unit $\lambda_b$. A $\pm1$ MPa constraint therefore
needs $\lambda_b$ to $\pm0.0126$. The taper sensitivity is
$\mathrm{d}\alpha/\mathrm{d}\lambda=+2.08^\circ$ per unit $\lambda$ at
$\lambda=0.4$ (lesson §3.2), so the slope would have to be known to

$$\pm2.08\times0.0126=\pm0.026^\circ=\pm1.6\ \mathrm{arcmin}.$$

That is 4–20 times better than the $\pm0.1$–$0.5^\circ$ achievable on submarine
slopes from bathymetry and seismic depth conversion. **The taper cannot constrain
the décollement's effective stress to $\pm1$ MPa**; the requirement is unattainable
and the inversion is not the right tool. A direct measurement — the
amplitude-versus-offset pressure signature or the heat-flow advection anomaly —
is required, and even then the constraint is on $\lambda_b$ locally.

**Unknown left unconstrained if the direct measurement is unavailable:** $K$.
With $\alpha$, $\mu_b$ and $\lambda$ fixed, a change in the assumed stress state
from $K=3.0$ (compressional Coulomb) to $K=2.0$ changes $\theta$ by
$0.38236/2.0-0.38236/3.0=0.063727\ \mathrm{rad}=3.65^\circ$, which is an order of
magnitude larger than the slope precision. Since $K$ is a modelling choice rather
than a measurement, the taper inversion is degenerate in exactly the quantity the
literature most often claims to determine.

## ★8 — Making the bulge larger and nearer

The model's predictions are $39.3\ \mathrm{m}$ at $232.8\ \mathrm{km}$, and its
key structural choices are: a line load, a purely elastic plate, a plate of
uniform thickness and rigidity, an infinitely wide plate (plane strain), and a
foundation modulus $k=(\rho_m-\rho_w)g$.

| change | effect on the bulge | stronger or weaker? | discriminating observation |
|---|---|---|---|
| Distributed slab-pull load rather than a $\delta$-function | larger amplitude, wider; the maximum moves seaward | effectively stronger response over a broader load | gravity anomaly wavelength across the outer rise |
| Yielding / plastic hinge near the trench | bulge moves **nearer** and grows, because the effective rigidity falls | weaker plate | distribution of normal-faulting earthquakes with depth; heat flow |
| Trench-directed bending moment (not just shear) | asymmetric shape; possible nearer extremum | depends on sign and size | the seaward slope of the deflection, which the moment controls independently |
| Sediment and volcanic loading on the incoming plate | larger, nearer (the load is closer to the bulge) | extra load, not a strength change | sub-bottom structure of the incoming section |
| Smaller $k$ (e.g. if the plate is partly supported dynamically) | larger amplitude, longer wavelength | stronger response | the free-air gravity over the bulge, which is where the compensation is visible |

**The statement the data can support:** an *effective* elastic thickness that fits
the observed deflection and bulge *wavelength over a few hundred kilometres* —
which is a statement about the net rigidity of the plate integrated over that
scale, its stress history, and its yielding state, none of which are separately
identified.

**The statement the data cannot support:** the plate's strength at any particular
depth, or the existence of a discrete elastic core. A 30 km plate that has yielded
in its upper few kilometres and a genuinely 16 km elastic plate produce the same
first-order flexure, and no combination of bathymetry, gravity and seismicity
along one profile separates them.
