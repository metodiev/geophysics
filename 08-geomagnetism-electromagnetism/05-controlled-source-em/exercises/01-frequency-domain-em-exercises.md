# Exercises — 08-05-01 Frequency-Domain EM (FDEM) Systems and Responses

Attempt these before reading the
[solutions](./01-frequency-domain-em-solutions.md). The lesson is
[01 Frequency-Domain EM (FDEM) Systems and Responses](../01-frequency-domain-em.md).
All models are **SYNTHETIC** teaching values with
$\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ exact.

## ★ Foundational

**★1.** Compute the skin depth and the induction number for
$f=3\ \mathrm{kHz}$, $\sigma=0.1\ \mathrm{S\,m^{-1}}$ and a coil separation
$r=25\ \mathrm{m}$. Show every intermediate quantity with its unit. Using the
measured rule-of-thumb from the lesson, state whether the low-induction-number
(LIN) form is usable there.

**★2.** Show by dimensional analysis that $S=H_s/H_p$ is dimensionless, and that
the combination $\omega\mu_0\sigma r^2$ is dimensionless. What is the unit of
$\omega\mu_0\sigma$?

**★3.** A coplanar coil pair has loop radii $a=b=1\ \mathrm{m}$ and separation
$s=25\ \mathrm{m}$. Compute the free-space mutual inductance from
$M=-\mu_0\pi a^2b^2/(4s^3)$, and state how many orders of magnitude larger it is
than a typical ground response of $3\times10^{-3}$ times the primary.

## ★★ Applied

**★4.** Derive the LIN term $S_{\text{LIN}}=k^2r^2/4$ (for $h=0$) from the exact
response integral by taking $\sigma\to0$, using
$\int_0^\infty J_0(\lambda r)\,\mathrm{d}\lambda=1/r$ and
$R(\lambda)=-k^2/(\lambda+u)^2$. State at which step the approximation enters.

**★5.** A system has a bucking residual that leaves $20\ \mathrm{ppm}$ of
uncorrected in-phase primary in the measurement. For the lesson's reference model
($\sigma=0.02\ \mathrm{S\,m^{-1}}$, $r=15\ \mathrm{m}$, $f=1\ \mathrm{kHz}$),
compare that $20\ \mathrm{ppm}$ with (a) the true in-phase response and (b) the
quadrature response. Then compute the LIN bias in ppm at $\theta=0.1$ for the same
model and decide whether the bucking residual or the LIN bias dominates the
in-phase error budget.

**★6.** A coplanar pair with $r=20\ \mathrm{m}$ on a resistive ground
($\sigma=0.005\ \mathrm{S\,m^{-1}}$) records a quadrature of
$1.1229\times10^{-3}$ at $f=300\ \mathrm{Hz}$. Invert the LIN formula for
$\sigma_{\text{app}}$ and compare with the true value. Is the discrepancy
explained by noise or by bias? Justify with the lesson's measured rule.

## ★★★ Research-oriented

**★7.** Prove the scale invariance of the exact response — that $S$ depends on
$\sigma$, $\omega$ and $r$ only through the product $kr$ — by substituting
$\lambda=x/r$ in the integral. Then state precisely which additional observation
breaks the invariance for a two-layer ground, and what new quantity that
observation constrains.

**★8.** Design a multi-separation, multi-frequency FDEM experiment intended to
determine the conductivity of a homogeneous halfspace to $5\%$ and the coil
separation error to $1\%$ in the presence of $2\ \mathrm{ppm}$ (per component,
$1\sigma$) receiver noise. Specify the separations, the frequencies, the metric
you will use to separate $\sigma$ from $r$, and predict the outcome using the
$1.5\theta$ LIN bias rule. A specification that could not be executed is a failed
answer.
