# Solutions — 15-04-01 Benthic Habitat Mapping and Classification

> **Read after attempting the exercises.** Lesson:
> [01 Benthic Habitat Mapping and Classification](../01-habitat-mapping.md).
> Numbers are computed from the SYNTHETIC model constants of the lesson.

## ★ Foundational

## ★1 — Impedance and reflection

$$Z_2=\rho_2c_2=1900\times1600=3.040\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}},

Z_1=1030\times1500=1.545\times10^{6}.$$

$$R=\frac{3.040-1.545}{3.040+1.545}=\frac{1.495}{4.585}=0.3261
\;\Rightarrow\;20\log_{10}0.3261=-9.73\ \mathrm{dB}.$$

Compare the lesson's mud ($-14.33$ dB) and rock ($-3.26$ dB): this seabed sits
between them, which is why a single backscatter value maps onto a range of
sediments.

## ★2 — Roughness parameter at 300 kHz

$$k=\frac{2\pi f}{c}=\frac{2\pi\times3\times10^{5}}{1500}
=1256.6\ \mathrm{m^{-1}}\quad(\text{wavelength }5.0\ \mathrm{mm}),$$

$$2k\sigma\cos\theta=2\times1256.6\times0.005\times0.7071=8.885 .$$

$8.9\gg1$: the coherent model does **not** apply; the surface is in the diffuse
(scattering) regime and a Lambertian or Kirchhoff model is required.

## ★3 — Analytic maximum slope

$$\left|\frac{\mathrm{d}h}{\mathrm{d}r}\right|_{\max}
=\frac{A}{s}e^{-1/2}=\frac{80}{300}\times0.6065=0.1617
\;\Rightarrow\;\arctan(0.1617)=9.19^\circ .$$

## ★★ Applied

## ★4 — The same mud at 300 kHz

$k=1256.6\ \mathrm{m^{-1}}$, so
$2k\sigma\cos45^\circ=2\times1256.6\times0.002\times0.7071=3.554$ (against
$1.18$ at 100 kHz). The coherence loss is

$$10\log_{10}\exp(-3.554^{2})=\frac{-12.63}{\ln 10}=-54.9\ \mathrm{dB},$$

so $\mathrm{BS}=20\log_{10}0.1987-54.9=-14.04-54.9=-68.9$ dB — far outside the
coherent regime, and in reality replaced by diffuse scattering that the model does
not describe.

**Why frequency dominates:** $2k\sigma\cos\theta$ is linear in $f$ and only
linear in $\sigma$. Tripling the frequency is equivalent to tripling the
roughness, so a seabed that is "smooth" for a 12 kHz system is rough for a
300 kHz system. **Every statement about seabed roughness must state the
frequency**, and two surveys of the same ground at different frequencies will
classify it differently unless the roughness parameter is what is compared.

## ★5 — Accuracy, kappa and per-class statistics

Total $n = 300+40+10+90+20+15+25 = 500$. Correct
$= 300+90+25 = 415$.

- Overall accuracy $=415/500=0.830$.
- Row sums: 340, 120, 40. Column sums: 310, 145, 45.
  $p_e=(340\times310+120\times145+40\times45)/500^2
  =(105400+17400+1800)/250000=124600/250000=0.4984$.
  $\kappa=(0.830-0.4984)/(1-0.4984)=0.3316/0.5016=0.661$.
- Recall: mud $300/340=0.882$; sand $90/120=0.750$;
  rock $25/40=0.625$.
- Precision: mud $300/310=0.968$; sand $90/145=0.621$;
  rock $25/45=0.556$.

**A map user should distrust the rock class**, on both counts: it is found only
62.5% of the time (recall) and only 55.6% of the cells labelled rock are actually
rock (precision). Any area-based statistic computed from "rock" polygons — a
protected-area estimate, a tonnage, a sample allocation — inherits a factor of
$0.556$ of false positives and misses 37.5% of the real rock. An accuracy of 0.83
and a kappa of 0.66 do not tell you that; the per-class table does.

## ★6 — Central-difference slope at $r=s$, $\Delta x=200$ m

The analytic slope at $r=s$ is $A/s\,e^{-1/2}=0.1516$. The central difference
across $\pm\Delta x/2$ at $r=s=200\ \mathrm{m}$:

$$\frac{h(100)-h(300)}{200}
=\frac{50\left[\exp(-100^{2}/80000)-\exp(-300^{2}/80000)\right]}{200}
=\frac{50(0.88250-0.32465)}{200}=0.13946,$$

$$\arctan(0.13946)=7.94^\circ,\qquad
\frac{7.94}{8.62}=0.921\ (\text{92.1\%}).$$

This reproduces the demonstration's 200 m entry exactly, and it shows the
mechanism: the central difference averages the slope over a 200 m window, and
across a mound whose length scale is also 200 m that averaging removes 8% of the
peak slope.

## ★★★ Research-oriented

## ★7 — Validating the rare class

**Sample size.** With zero failures in $n$ independent trials, the 95% upper
bound on the failure rate is $3/n$. Requiring $3/n\le0.05$ gives
$n=60$ independent rock validation sites.

**Spatial autocorrelation.** Rock habitat occurs in patches, and two sites 100 m
apart are not independent observations of "does the classifier find rock". The
*effective* number of independent samples is closer to the number of distinct
patches (or the number of blocks larger than the patch scale) than to 60. If the
effective sample size is 5 patches, the bound is $3/5=0.60$ — useless. The
practical statement is: **report the patch count, not the site count**, and treat
the 60-site requirement as a lower bound on the survey effort.

**Site selection.** Draw one site per mapped rock patch where possible, spread
across the full range of depths, slope classes and acoustic facies in which rock
is predicted, and include deliberately ambiguous cells (near class boundaries) as
a separate, reported stratum. A validation set made only of "obvious" rock will
pass and teach nothing.

**With only 12 rock sites.** Report: "12 independent rock sites; the classifier
found rock at 12 of 12, which bounds the failure rate at 25% (95% confidence);
the bound is set by the sample size, not by the classifier." Do not report "100%
recall".

## ★8 — One number, two worlds

At $45^\circ$ grazing the lesson gives mud at $-20.1$ dB (coherent) and the
Lambertian end-member with $\mu_L=0.02$ at $-20.0$ dB. The observation of
$-17.0$ dB is therefore reproduced by **either**:

- a coherent seabed with a weaker coherence loss than the mud model, i.e. a
  smoother or lower-contrast interface whose impedance level is
  $-17.0+6.1=-10.9$ dB ($|R|=0.285$); or
- a Lambertian seabed with
  $\mu_L=10^{-1.70}/\sin^{2}45^\circ=0.0200/0.5000=0.0399$, i.e. a rougher seabed
  with a larger backscattering constant.

Both are one-parameter fits to one datum. The first is even under-determined,
since $|R|$ and $\sigma$ trade off inside the coherence loss.

**Measurement programme.** Fit the three-parameter model
$\mathrm{BS}(\theta)=10\log_{10}[|R(\theta)|^{2}e^{-(2k\sigma\cos\theta)^{2}}+\mu_L\sin^{2}\theta]$
to backscatter at **at least four grazing angles** spanning $20^\circ$–$80^\circ$
(three parameters need three constraints, and four angles give a residual to test
the model). The reason four and not two is the degeneracy: at a single angle,
$|R|$ and $\sigma$ trade exactly; at two angles they trade along a curve; only
across a range do the different angle dependencies — the coherence loss falling
as $\cos^{2}\theta$ and the Lambert term rising as $\sin^{2}\theta$ — separate
them. The identifiable pair is roughly (level near normal incidence, curvature in
the mid-angles).

**Expected degeneracy.** $|R|$ and $\sigma$ remain correlated at moderate
roughness (both raise BS at oblique angles), so the fitted pair should be reported
as a confidence ellipse, not two numbers.

**Independent observation that resolves it.** A physical sample: a grab, core or
photograph gives the substrate (hence $\rho$ and $c$, hence $|R|$) or the
roughness directly. Alternatively, a second survey at a different frequency
breaks the degeneracy because $2k\sigma\cos\theta\propto f$ while $|R|$ is
frequency-independent to first order — the classic multi-frequency
roughness-versus-impedance separation.
