# Exercises — 06-12-02 Pore-Pressure Diffusion and Triggering Mechanisms

Attempt these before reading the
[solutions](./02-pore-pressure-triggering-solutions.md). The lesson is
[02 Pore-Pressure Diffusion and Triggering](../02-pore-pressure-triggering.md);
all numbers are printed by
[`../code/diffusion_front_demo.py`](../code/diffusion_front_demo.py). All models
are **SYNTHETIC** teaching values; no real injection site, well or earthquake
catalogue is used.

## ★ Foundational

**★1.** For $D = 0.1\ \mathrm{m^2\,s^{-1}}$, $x_c = 1.1977$ and one year, compute
the triggering front $r_c = \sqrt{4Dx_ct}$ in metres and in kilometres. State the
unit of the product $4Dx_ct$.

**★2.** For a two-dimensional constant-rate source the pressure field is
$p(r,t) = \dfrac{Q}{4\pi D}E_1\!\left(\dfrac{r^2}{4Dt}\right)$. Given
$p = 5.0\times10^{6}\ \mathrm{Pa}$ at $r = 50\ \mathrm{m}$ after one year, and
$E_1(r^2/4Dt) = 7.9500$, compute the source strength $Q$ with units.

**★3.** Explain, using $D = r_c^2/(4x_ct)$, why a 10% error in a measured front
*radius* is already a 21% error in diffusivity.

## ★★ Applied

**★★4.** The demonstration reports $r_{\text{front}}/\sqrt{t} = 0.693$, $0.692$,
$0.692$, $0.692$, $0.692$ (m s$^{-0.5}$) at $t = 30, 60, 120, 240, 365$ days.
Verify that the fitted exponent $0.499902$ is consistent with those values, and
state how the measured spread ($0.0004\ \mathrm{m\,s^{-0.5}}$) compares with the
size of the numbers themselves.

**★★5.** The demonstration's $D$-inference table gives $x_c = 0.1298$ for an
assumed threshold ratio of $0.2$, and $x_c = 2.8454$ for a ratio of $0.002$. Using
the measured migration rate $a = 0.4792\ \mathrm{m^2\,s^{-1}}$ and
$D_{\text{inferred}} = a/(4x_c)$, compute both inferred diffusivities and compare
with the printed values $0.9226$ and $0.0421\ \mathrm{m^2\,s^{-1}}$.

**★★6.** The demonstration reports that a systematic hypocentral distance bias of
$b = 0.10$ moves the fitted $D$ by a factor $1.210$, while random location error of
$\sigma_{\text{loc}} = 1\ \mathrm{km}$ moves the median fitted $D$ by only a few
per cent with 150 events. Explain both results in terms of how the error enters
$r_c^2$, and state which one more events can reduce.

## ★★★ Research-oriented

**★★★7.** An analyst wants to separate $D$ from the threshold ratio
$p_c/\Delta p_{\text{ref}}$ using seismicity alone. Design the experiment that
would do it or, if it cannot be done, prove that it cannot: state what is measured,
what is inferred, and what additional independent observation would break the
degeneracy.

**★★★8.** Derive $p(r,t) = \dfrac{Q}{4\pi D}E_1\!\left(\dfrac{r^2}{4Dt}\right)$
from the diffusion equation with a line source switched on at $t = 0$, stating the
Green's function you start from and the assumption about the far-field pressure
boundary condition.

**★★★9.** Real reservoirs are anisotropic: horizontal permeability usually exceeds
vertical. Write the anisotropic diffusion equation, sketch the shape of the
$t^{1/2}$ front for $D_x = 4D_y$, and state what an analyst who fits an isotropic
$r_c = \sqrt{4Dx_ct}$ to this front would recover, in terms of $D_x$ and $D_y$.
