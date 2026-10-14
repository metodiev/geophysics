# Solutions — 06-06-06 Global Mantle Tomography and Its Geodynamic Interpretation

Exercises:
[06-global-mantle-tomography-exercises.md](06-global-mantle-tomography-exercises.md).

## ★ Foundational

**1.** $v(R) = 8.0\times(6371/6371) = \mathbf{8.00\ km\,s^{-1}}$;
$v(3480) = 8.0\times(6371/3480) = \mathbf{14.65\ km\,s^{-1}}$.

**2.** $r^2 = p\,V_{\text{surf}}R = 423.3\times8000\times6.371\times10^{6}
= 2.157\times10^{13}\ \mathrm{m^2}$, so $r = 4.644\times10^{6}$ m and the depth
is $6371 - 4644 = \mathbf{1727\ km}$ — matching the table's 1726 km to rounding.

**3.** $\mathrm{d}\Delta = \mathrm{d}T/p = 0.8/500 = 1.6\times10^{-3}$ rad
$= \mathbf{0.0917^\circ}$. So a sub-second travel-time residual corresponds to a
distance error of a tenth of a degree: residual maps and travel-time maps are not
the same picture and cannot be compared cell by cell.

## ★★ Applied

**4.** $p = 700$ s/rad lies between the rows $p = 606.7$ (depth 810 km) and
$p = 790.0$ (depth 26 km). Linear interpolation in $p$:
$810 + (700-606.7)/(790.0-606.7)\times(26-810) =
810 - 0.509\times784 = \mathbf{411\ km}$. This is why the deep-mantle sampling
is coarse: the whole range from 26 to 810 km is covered by 183 s/rad of ray
parameter.

**5.** $6.07$ per cent of $0.5$ per cent $= \mathbf{0.030}$ per cent, i.e. a
degree-2 anomaly of 0.03 per cent appears in the map. A reader who saw only the
degree-2 map would attribute that 0.03 per cent to degree-2 structure in the
mantle, when in fact it is an alias of degree-12 structure eight times larger.
This is why maximum degree and the amplitude of the unmodelled band must be
reported together.

**6.** Doubling the noise level to 2.0 s admits every row whose residual is below
2.0 s: the 800 km row (1.149 s) and the 2200 km row (1.194 s) are now also
admitted, so the depth range *widens* to roughly 700-2300 km. The amplitudes do
not change with the noise level — the amplitude is fixed by the required
travel-time delay — so 800 km and 2200 km are admitted at 0.577 and 1.079 per
cent respectively. The important consequence: **the quoted uncertainty of the
depth is only as good as the stated noise level**, and doubling the assumed
noise doubles the admitted depth range here.

## ★★★ Research-oriented

**7.** Add **surface-wave dispersion** (or normal-mode splitting) measured over
the same region. Its kernel is depth- and period-dependent, with sensitivity that
peaks at different depths for different periods, so it is not proportional to the
body-wave kernel. The criterion for claiming that the depth is determined is
quantitative: on a trade-off curve of misfit against depth (with amplitude
fitted at each depth), the set of depths whose *combined* misfit is below the
stated noise level must be narrower than the discrepancy being claimed — for
example 1200-1800 km collapsing to 1450-1600 km — and the same test must be shown
for the amplitude. Without that curve, the claim of a resolved depth is not
checkable.

**8.** The real conversion depends on: (i) temperature itself, through the
temperature dependence of elastic moduli and of thermal expansion; (ii) pressure;
(iii) composition (iron, water, melt); (iv) the presence of partial melt, for
which the velocity drop per degree is very different; (v) phase changes
(olivine-wadsleyite-ringwoodite) that make velocity a step function of depth;
(vi) anelasticity, which makes $v$ frequency dependent. Effects that tend to make
a published temperature anomaly **too large** are those where a given anomaly is
partly compositional or melt-related but is attributed entirely to temperature —
notably a constant conversion applied near a phase boundary or in a region where
melt is likely — and any conversion that ignores anelasticity, which weakens the
velocity change per degree.
