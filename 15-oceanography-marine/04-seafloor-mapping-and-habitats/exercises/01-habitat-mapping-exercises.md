# Exercises — 15-04-01 Benthic Habitat Mapping and Classification

Attempt these before the
[solutions](./01-habitat-mapping-solutions.md). The lesson is
[01 Benthic Habitat Mapping and Classification](../01-habitat-mapping.md). All
models and data are **SYNTHETIC** teaching values; the model constants are those
printed by `code/habitat_mapping_demo.py`.

## ★ Foundational

**★1.** A seabed has $\rho_2 = 1900\ \mathrm{kg\,m^{-3}}$ and
$c_2 = 1600\ \mathrm{m\,s^{-1}}$. Compute its impedance, the normal-incidence
reflection coefficient against seawater ($\rho_1=1030$,
$c_1=1500\ \mathrm{kg\,m^{-3}}$, $\mathrm{m\,s^{-1}}$), and the level in dB.

**★2.** Compute the Rayleigh roughness parameter $2k\sigma\cos\theta$ at 300 kHz
for a seabed with rms roughness $\sigma = 0.005\ \mathrm{m}$ at a grazing angle of
$45^\circ$. State whether the coherent model applies.

**★3.** Compute the analytic maximum slope of a Gaussian mound with $A = 80\
\mathrm{m}$ and $s = 300\ \mathrm{m}$, and give it in degrees.

## ★★ Applied

**★★4.** For the soft-mud model of the lesson ($\sigma = 0.002\ \mathrm{m}$,
$|R(45^\circ)| = 0.1987$), recompute the coherence loss and the coherent
backscatter strength at $45^\circ$ grazing at **300 kHz** instead of 100 kHz.
State what has happened to the regime and why frequency matters more than
substrate here.

**★★5.** A validation set gives the following confusion matrix (rows = truth;
classes mud, sand, rock): mud → [300, 40, 0], sand → [10, 90, 20], rock →
[0, 15, 25]. Compute overall accuracy, Cohen's kappa, the recall of each class
and the precision of each class. State which class a map user should distrust and
why.

**★★6.** Using the lesson's mound ($A = 50\ \mathrm{m}$, $s = 200\ \mathrm{m}$),
compute the central-difference slope at $r = s$ with a grid spacing of
$\Delta x = 200\ \mathrm{m}$, and compare it with the analytic maximum slope. Give
the recovered fraction.

## ★★★ Research-oriented

**★★★7.** A habitat map's rarest class (rock) must be validated to show that it
is found at least 95% of the time, at 95% confidence. Using the rule of three
(zero failures in $n$ trials bounds the failure rate at $3/n$ with 95%
confidence), compute the number of independent rock validation sites required.
Then state how spatial autocorrelation changes that number, how you would choose
the sites, and what you would report if only 12 rock sites were available.

**★★★8.** A single backscatter measurement at $45^\circ$ grazing is
$-17.0\ \mathrm{dB}$. Show with the lesson's numbers that this is consistent with
both the smooth-mud model and with a Lambertian model with a suitable $\mu_L$,
then design a measurement programme that separates them. State the model you
would fit, the number of grazing angles required and why, the parameter
degeneracy you expect, and the independent observation that resolves it.
