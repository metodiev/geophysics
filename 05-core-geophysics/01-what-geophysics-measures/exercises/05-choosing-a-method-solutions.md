# Solutions — 05-01-05 Choosing a Method: A Decision Framework

> Numbers marked *verified* were computed.

---

## ★1

Contrast (cheapest test: compute the predicted anomaly from a stated contrast
and compare with the noise); resolution (compute the required band and aperture);
access (walk the ground or check imagery); cost and logistics (compare against
the value of the information). Contrast is tested first because if it fails,
nothing else matters.

---

## ★2

$\mathrm{CNR} = A/\sqrt{\sigma_\text{instr}^2+\sigma_\text{model}^2+
\sigma_\text{geol}^2}$. Geological noise dominates because the subsurface varies
with everything except the target, and no processing can remove variation that
is real.

---

## ★3

For example: "locate the buried channel to within $\pm10$ m horizontally and
$\pm3$ m in depth, where the channel is at least 4 m thick and at least 15 m
wide at 25–40 m depth, with a resistivity contrast of at least 3:1."

---

## ★★4 *(verified)*

2-D line mass: $\lambda = \Delta\rho\cdot(\text{width}\times1\ \mathrm{m}) =
250\cdot15 = 3750$ kg/m. Then

$$A = \frac{2G\lambda}{d} = \frac{2(6.6743\times10^{-11})(3750)}{35}
= 1.43\times10^{-8}\ \mathrm{m\,s^{-2}} = 0.00143\ \mathrm{mGal}.$$

That is about **seven times below** 0.01 mGal repeatability, and the combined
uncertainty is larger still. Conclusion: gravity is not viable for this target
at this depth, despite the contrast being real.

---

## ★★5

Electrode spacing $\le 7.5$ m; for a 200 m line, at least
$200/7.5 \approx 27$ electrode positions (a standard 32- or 48-electrode
multi-electrode system covers it with margin). The resistivity contrast governs
the choice: the density contrast fails on CNR while the resistivity contrast
does not.

---

## ★★6 *(verified)*

$\Delta T \propto \sin(\text{inclination})$ for a vertical magnetisation
directly above the body: 0.00, 0.50, 0.87 and 1.00 of the maximum. At the
magnetic equator (inclination 0°) the anomaly directly over the body is
**exactly zero**. A magnetic survey there is not pointless in absolute
terms — the anomaly is non-zero off-axis and the field is still measurable —
but a naive single-station check over the target would show nothing.

---

## ★★7 *(verified)*

$\delta = \sqrt{2/(\mu\sigma\omega)}$ with $\sigma = 0.02$ S/m,
$\mu_0 = 1.2566\times10^{-6}$ H/m: $\mu\sigma = 2.513\times10^{-8}$.
Setting $\delta = 500$ m means $\delta^2 = 2/(\mu\sigma\omega) = 2.5\times10^{5}$
m², so

$$\omega = \frac{2}{\mu\sigma\,\delta^2}
= \frac{2}{2.513\times10^{-8}\cdot 2.5\times10^{5}} = 318.3\ \mathrm{rad\,s^{-1}},
\qquad T = \frac{2\pi}{\omega} = 0.0197\ \mathrm{s}.$$

(Equivalently $T = \pi\mu\sigma\delta^2$.) So the penetration requirement is met
by any period **longer than about 0.02 s**, i.e. by frequencies below 50 Hz. A
1 Hz transmitter is comfortably adequate on penetration grounds: at 1 Hz,
$\delta = \sqrt{2/(2.513\times10^{-8}\cdot6.283)} = 3559$ m, far deeper than the
500 m target. At 0.1 Hz, $\delta = 1.13\times10^{4}$ m.

The honest answer therefore distinguishes the *penetration* requirement
($T \gtrsim 0.02$ s, easily satisfied) from the *resolution and signal*
requirements, which must be modelled: a very long period buys penetration but
averages over a thick interval, so the achievable resolution falls.

**Correction of an earlier draft.** A previous version of this solution gave
$T = 19.7$ s, a factor of $10^{3}$ too long, by writing $2/(\mu\sigma\delta^2)$
as $2.5\times10^{-3}$ where the correct value is $2.5\times10^{5}$ m². The
conclusion inverted: the draft claimed 1 Hz was inadequate when in fact 1 Hz is
2500 times deeper-reaching than needed. The error was caught by the dimensional
sanction $T = \pi\mu\sigma\delta^2$ — check that
$[\mathrm{H\,m^{-1}\cdot S\,m^{-1}\cdot m^2}] = \mathrm{s}$ before trusting any
intermediate number.

---

## ★★★8

A complete dossier contains the seven items listed in Exercise ★★8 of the
lesson's framework: objective; contrast candidates; amplitude predictions;
noise budget; geometry and resolution; feasibility test; decision. Marks are
lost for unsourced property values, for omitting the geological noise term, and
for failing to state which assumption is pivotal.

---

## ★★★9

Missing: the target's depth measured numerically; its size and shape (which
decide 2-D versus 3-D kernels); the combined noise including geological;
whether the instrument can reach the terrain. The two calculations that must
precede commitment are the CNR and the required resolution. "Large contrast"
implies only that the *amplitude per unit volume* will be adequate near the
body; it says nothing about depth decay, which for a compact body goes as
$d^{-2}$, or about whether the survey geometry can resolve the target's shape.
Owning the instrument is a cost argument, and cost arguments cannot rescue a
contrast that fails at depth.
