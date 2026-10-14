# Exercises — 17-03-02 InSAR: Interferometric Phase and Deformation Measurement

Attempt these before reading the
[solutions](./02-insar-solutions.md). The lesson is
[02 InSAR](../02-insar.md). All models are **SYNTHETIC** teaching values.

Useful values from the lesson's demonstration: $\lambda = 5.6565\ \mathrm{cm}$,
$4\pi/\lambda = 222.16\ \mathrm{rad\,m^{-1}}$, $R = 800\ \mathrm{km}$,
$\theta = 35^\circ$ (so $\sin\theta = 0.5736$, $\cos\theta = 0.8192$),
$\Delta g = 8.71\ \mathrm{m}$, $B_c = 3171.2\ \mathrm{m}$.

## ★ Foundational

**★1.** A pixel's range changes by $1.70\ \mathrm{cm}$ along the line of sight
between two acquisitions. Compute the interferometric phase in radians, the
equivalent number of fringes, and the wrapped phase.

**★2.** A wrapped phase of $-1.40\ \mathrm{rad}$ is measured. List four
line-of-sight displacements, spanning positive and negative values, that produce
exactly this wrapped phase, and give the displacement that separates them.

**★3.** Compute the ambiguity height for $\theta = 35^\circ$,
$B_{\perp} = 50\ \mathrm{m}$ and for $B_{\perp} = 150\ \mathrm{m}$, using the
vertical-displacement sensitivity of the lesson. State what happens to the
fringe density over a fixed relief when the baseline grows.

## ★★ Applied

**★★4.** Show that a displacement along the direction perpendicular to the line
of sight produces a height sensitivity larger by $1/\sin^{2}\theta$ than the
vertical displacement, and evaluate the ratio at $\theta = 35^\circ$. Explain,
using a trigonometric argument about the direction vector, why the
"perpendicular" motion is mostly horizontal at shallow incidence.

**★★5.** Using the lesson's coherence-bias table, decide whether a coherence
threshold of 0.30 can be applied identically to regions processed with $L = 4$
and with $L = 64$ looks. For a true coherence of 0.20, give the expected
estimated coherence in each case and state the practical consequence for a mask
built from the threshold.

**★★6.** A pixel spacing of $20\ \mathrm{m}$ and $\lambda = 5.6565\ \mathrm{cm}$:
compute the largest line-of-sight phase gradient per pixel that can be unwrapped
unambiguously, express it as a displacement gradient in millimetres per metre of
ground, and compare it with a subsidence bowl of amplitude $6\ \mathrm{cm}$
spread over $400\ \mathrm{m}$.

## ★★★ Research-oriented

**★★★7.** Design the observations that would determine whether a $1\ \mathrm{cm}$
LOS signal in a single interferogram is deformation, atmosphere, or orbital
error. State which additional data you would acquire, what diagnostic you would
compute on each, and the signature that distinguishes the three. Specify how you
would report the residual uncertainty in each case. A specification that could
not be executed is a failed answer.

**★★★8.** The demonstration's asymptotic phase-precision formula,
$\sigma_\phi^{2} \approx (1-\gamma^{2})/(2L\gamma^{2})$, is stated for large $L$
and moderate-to-high $\gamma$. Derive the direction in which it errs at
$\gamma = 0.3$, $L = 1$ (the measured spread is smaller, not larger), explain the
mechanism, and propose the criterion you would use to decide when the formula is
usable for an error budget.
