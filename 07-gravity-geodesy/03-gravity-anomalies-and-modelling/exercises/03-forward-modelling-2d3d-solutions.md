# Solutions — 07-03-03 Forward Modelling in 2-D and 3-D

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [03 Forward Modelling](../03-forward-modelling-2d3d.md).

---

## ★1 — Prism terms

Eight terms per station: two $x$ faces $\times$ two $y$ faces $\times$ two $z$
faces. The sign $(-1)^{i+j+k}$ alternates because the prism is the difference of
two half-spaces in each direction: the field of the body is obtained by inclusion
and exclusion, exactly as a definite integral over $[a,b]$ is
$F(b)-F(a)$. Each term is the antiderivative evaluated at a face, so the eight
terms are the $2^{3}$ corner evaluations.

---

## ★2 — Dimensions in the prism formula

Each bracket is
$x_i\ln(y_j+r)+y_j\ln(x_i+r)-z_k\arctan(x_iy_j/z_kr)$. The first two terms are a
length times a logarithm of a dimensionless ratio of lengths; the third is a
length times an angle. A logarithm of a dimensional quantity is itself only
meaningful as a difference, and here the differences are dimensionless because
each logarithm multiplies a length and appears with face-to-face sign changes.
Hence the bracket is a length, and

$$[G\Delta\rho\times\text{length}]
= \left[\mathrm{m^{3}kg^{-1}s^{-2}}\right]\left[\mathrm{kg\,m^{-3}}\right]
\left[\mathrm{m}\right] = \mathrm{m\,s^{-2}} ✔$$

---

## ★3 — Linearity and negative contrasts

$g_z$ is linear in $\Delta\rho$ (the kernel contains no $\rho$-dependent term), so
the anomaly of a sum of bodies is the sum of their anomalies — exactly, not
approximately. A **negative contrast** models a low-density body: a salt dome in
sediment, a cavity or mine working, an air-filled void, a magma chamber lighter
than its host. The demonstration's two-prism example sums
$0.92806\ \mathrm{mGal}$ and $-0.71450\ \mathrm{mGal}$ to $0.21355\ \mathrm{mGal}$.

---

## ★4 — Conditioning and the slab comparison

At the origin the observation point is directly above the centre of every face, so
each of the eight terms is evaluated at comparable distances
($r$ ranges from $\sqrt{500^{2}+1000^{2}+200^{2}} = 1136\ \mathrm{m}$ for the
nearest corner to $\sqrt{500^{2}+1000^{2}+1500^{2}} = 1871\ \mathrm{m}$ for the
farthest). No term dominates, no logarithm has a near-zero argument, and the sum
is well conditioned.

Infinite slab for the thickness $t = 1300\ \mathrm{m}$:

$$2\pi G\Delta\rho t = 2\pi(6.67430\times10^{-11})(300)(1300)
= 1.6355\times10^{-4}\ \mathrm{m\,s^{-2}} = 16.3550\ \mathrm{mGal}.$$

The finite prism gives $5.0047\ \mathrm{mGal}$, i.e. $30.6\%$ of the slab — the
same conclusion as the lesson's worked example: at this depth-to-width ratio the
slab is a poor shorthand.

---

## ★5 — 2-D error from the strike table

The demonstration's strike table gives, at $x = 0$ (broadside), ratios
$0.8517$ ($2\ \mathrm{km}$ strike), $0.9980$ ($20\ \mathrm{km}$),
$0.99998$ ($200\ \mathrm{km}$). The body here has a $2\ \mathrm{km}$ strike over a
depth range $200$–$1500\ \mathrm{m}$:

- at a $2\ \mathrm{km}$ strike: $14.8\%$ error;
- at a $20\ \mathrm{km}$ strike: $0.20\%$ error;
- at a $200\ \mathrm{km}$ strike: $0.002\%$ error.

The error falls roughly as (depth/strike)$^{2}$, so $0.1\%$ requires
$(\text{depth}/\text{strike})^{2} \lesssim 10^{-3}$, i.e.

$$\text{strike} \gtrsim \frac{\text{depth}}{\sqrt{10^{-3}}}
= 31.6\times\text{depth} \approx \mathbf{47\ km}$$

for the $1500\ \mathrm{m}$ maximum depth. The practical rule of thumb
($\gtrsim 10\times$ depth for $0.2\%$) follows the same scaling.

---

## ★6 — Volume error becomes anomaly error

For a body small compared with its depth, the anomaly is approximately
proportional to its total excess mass, so a fractional volume error
$\epsilon$ with the density unchanged produces approximately the same fractional
anomaly error:

$$\frac{\delta g}{g} \approx \frac{\delta M}{M} = \epsilon = 10.22\%.$$

With a peak of $0.9705\ \mathrm{mGal}$, that is
$0.099\ \mathrm{mGal}$ — the demonstration's measured rms error at
$150\ \mathrm{m}$ voxels is $0.04815\ \mathrm{mGal}$ *without* mass matching,
i.e. about half, because the voxel model also distorts the *shape*, partially
cancelling the volume excess.

**Correction:** scale every voxel's density by the inverse volume ratio,

$$\Delta\rho_{\text{corr}} = \Delta\rho\times\frac{V_{\text{true}}}{V_{\text{voxels}}}
= 400\times\frac{1}{1.1022} = 362.9\ \mathrm{kg\,m^{-3}},$$

which is the mass-matching step applied in the demonstration; the rms error then
falls to $0.00135\ \mathrm{mGal}$ ($0.14\%$ of the peak).

---

## ★7 — Exact volume conservation at $150\ \mathrm{m}$

Two routes, both exact:

1. **Density rescaling (mass matching).** Keep the cube grid, set each cube's
   density to $\Delta\rho\times V_{\text{sphere}}/V_{\text{cubes}}$ as in ★6. The
   total mass is then exact by construction; only the shape is approximate. The
   demonstration measures an rms error of $0.00135\ \mathrm{mGal}$ at
   $150\ \mathrm{m}$ voxels, i.e. $0.139\%$ of the $0.97049\ \mathrm{mGal}$ peak,
   and it is *not* monotone in voxel size because the cube grid shifts relative to
   the sphere.
2. **Partial boundary cells.** Summation over only the cells whose centres are
   inside the sphere leaves the volume $10.22\%$ high; rescaling the *boundary*
   cells' densities (or their volumes) so the total matches is equivalent to (1)
   but keeps interior cells physical.

**Verification:** (i) compute $\sum V_i$ and compare with
$\tfrac{4}{3}\pi R^{3}$; (ii) compute the forward model of the voxelised body and
compare with the analytic sphere on a profile; (iii) refine the voxel size and
check that the error falls, at least in the mean. Only after (i) passes is (ii)
meaningful.

---

## ★8 — A dipping slab with prisms

Discretise the slab into vertical columns of constant horizontal cross-section (a
regular $x$–$y$ grid, cell size $h$), and inside each column place a prism whose
top follows the dipping plane and whose base is the flat bottom. The top of the
plane varies within a cell by $h\tan20^{\circ}$; assigning each prism the mean top
depth over its cell therefore mis-locates the top by at most

$$\frac{h\tan20^{\circ}}{2} = 0.182\,h .$$

**Mass conservation** is exact if each prism's top is chosen so the prism volume
equals the true volume of the slab inside that column (equivalently, use the mean
top depth and account for the extra triangle at one side and the missing one at
the other). Constructing the mesh by *column and mean depth* conserves volume
exactly and leaves only a shape error of order $(h\tan20^{\circ})/z$ relative to
the depth.

**Controlling parameter:** the ratio $h\tan\theta/z$ — cell size times dip tangent
over depth. For a $20^{\circ}$ dip, $z = 1\ \mathrm{km}$ and a target shape error
of $1\%$, $h \lesssim 0.01\times1000/0.364 = 27\ \mathrm{m}$. Doubling the dip
angle halves the permissible cell size, which is the practical reason dipping-body
forward models are expensive.
