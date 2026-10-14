# Solutions — 15-04-03 Marine Minerals and Deep-Sea Mining Geophysics

> **Read after attempting the exercises.** Lesson:
> [03 Marine Minerals and Deep-Sea Mining Geophysics](../03-marine-minerals.md).
> Numbers are SYNTHETIC model values.

## ★ Foundational

## ★1 — Sphere gravity anomaly

$$g_{\max}=\frac{4}{3}\pi G\Delta\rho\frac{a^{3}}{z^{2}}
=\frac{4\pi}{3}\times6.67430\times10^{-11}\times800\times\frac{1.25\times10^{5}}
{2.5\times10^{5}} .$$

Step by step: $4\pi/3=4.18879$;
$4.18879\times6.67430\times10^{-11}=2.7958\times10^{-10}$;
$\times800=2.2366\times10^{-7}$; $\times1.25\times10^{5}=2.7958\times10^{-2}$;
$/2.5\times10^{5}=1.118\times10^{-7}\ \mathrm{m\,s^{-2}}$.

Dividing by $10^{-5}$: $g_{\max}=0.0112\ \mathrm{mGal}$. That is roughly
$1/270$ of the shipboard gravity repeatability quoted in the lesson — an
undetectable body, and its density contrast was only 800 kg/m³ (weaker than the
lesson's 1500) and its depth half as great, so the lesson's case is the more
favourable of the two.

## ★2 — Skin depth and attenuation

$$\delta=503.29\sqrt{\frac{0.30}{0.5}}=503.29\times0.7746=389.8\ \mathrm{m}.$$

$$A_{\text{dB}}=20\log_{10}e^{-1500/389.8}
=\frac{20}{\ln 10}\times(-3.848)=-33.4\ \mathrm{dB}.$$

As an amplitude factor, $10^{-33.4/20}=0.021$: 2% of the field survives 1500 m of
that water at 0.5 Hz.

## ★3 — Tonnage and contained metal

$$\text{tonnage}=200\times10^{6}\ \mathrm{m^{2}}\times12\
\mathrm{kg\,m^{-2}}=2.4\times10^{9}\ \mathrm{kg}=2.4\times10^{6}\ \mathrm{t}
=2.4\ \mathrm{Mt (wet)},$$

$$\text{Ni}=2.4\times10^{6}\times0.012=2.88\times10^{4}\ \mathrm{t}.$$

## ★★ Applied

## ★4 — Fitting the variogram

**Sill.** The value at 4000 m, 17.89, is close to the asymptote; take the sill as
the asymptote $C$ and note that if it is not yet reached the fitted $C$ will be
low. Using the exponential model
$\gamma(h)=C_0+(C-C_0)(1-e^{-h/L})$ and treating $C$ as unknown, we have three
equations and three unknowns.

With $A=C-C_0$:

$$C_0+A(1-e^{-250/L})=6.29,\quad
C_0+A(1-e^{-1000/L})=13.42,\quad
C_0+A(1-e^{-4000/L})=17.89 .$$

Trying $L=800$ m: $e^{-0.3125}=0.7316$, $e^{-1.25}=0.2865$,
$e^{-5}=0.006738$, so

$$C_0+0.2684A=6.29,\qquad C_0+0.7135A=13.42
\;\Rightarrow\;0.4451A=7.13,\;A=16.02 .$$

Then $C_0=6.29-0.2684\times16.02=6.29-4.30=1.99$, and $C=1.99+16.02=18.01$.
**Check the third lag**: $C_0+A(1-e^{-5})=1.99+16.02\times0.99326=17.90$ against
the observed 17.89 ✔ — agreement to 0.01.

So $C_0=2.0$, $C-C_0=16.0$, $L=800$ m. The three-lag fit is consistent, which
means the numbers were generated from a single exponential model; with real data
the three lags rarely fit this well, and the fit must be reported with its
scatter. **A three-point fit is not a variogram**; it is an illustration of what
the parameters mean.

## ★5 — Validating a kriging variance

$$\text{ratio}=\frac{5.30}{2.66}=1.99 .$$

The kriging variance is **optimistic** by a factor of two: the reported
$\pm2.66\ \mathrm{kg\,m^{-2}}$ covers roughly half the actual scatter, so a 95%
interval built from it would be far too narrow (it would contain the truth about
half as often as it claims).

Two variogram-based explanations:

1. **The fitted range is too short.** A range shorter than the truth makes
   kriging weight nearby samples more heavily and assume the field decorrelates
   quickly, which reduces the predicted variance. In the lesson the fitted range
   was 1656 m against a true 2000 m, and that single 17% shortfall is enough to
   produce the factor of two.
2. **The fitted partial sill is too large or the nugget too small.** The predicted
   variance is proportional to the sill; the lesson's fitted nugget was 0.00
   against a true 2.25, which removes the variance floor and shifts the entire
   model down at short lags. A larger fitted sill would raise the predicted
   variance, so the direction of the error depends on which parameter is wrong —
   which is exactly why the validation must be done rather than assumed.

## ★6 — Sample counts

$$n=\left(\frac{1.96\times0.8}{0.15}\right)^{2}=(10.453)^{2}=109.3
\;\Rightarrow\;110\ \text{samples}.$$

With the naive formula's error understated by a factor of 3.0–8.5, achieving the
same 15% on the *area mean* requires the error to be reduced by that factor, and
since the error falls as $1/\sqrt n$,

$$n_{\text{required}}=110\times(3.0)^{2}\ \text{to}\ 110\times(8.5)^{2}
=990\ \text{to}\ 7950\ \text{samples}.$$

**Implication:** a survey designed from the textbook formula alone would be short
by one to two orders of magnitude in effort, and would report a precision it does
not have. The correct design uses the variogram (or the between-area variance)
to convert a target precision into a sample count, and the correct report states
which variance components are included.

## ★★★ Research-oriented

## ★7 — Detecting a 150 m mound under 20 m of sediment

| method | expected anomaly or signature | achievable noise / limit | verdict |
|---|---|---|---|
| multibeam bathymetry and backscatter | no bathymetric expression under 20 m of sediment; backscatter is that of the sediment cover | 1–2% depth, backscatter repeatability a few dB | **no**: the mound is buried |
| sub-bottom profiling (chirp) | an acoustic anomaly (a hard reflector, a velocity pull-up) of order 5–20 ms | a few ms with good conditions | **possible but ambiguous**: compaction, gas, coarse sediment all do the same |
| magnetics | 0.84 nT or less for a 100 m body (the lesson's calculation), reduced by the sediment separation | a few nT along-line | **no** |
| gravity | 0.04–0.1 mGal | 0.1 mGal shipborne, 0.03 mGal at the seafloor | **marginal at best** |
| deep-towed EM | a conductive target at 20–50 m burial is well inside the 477–1508 m depth of investigation at 1–10 Hz; the response is the anomalous secondary field | a few per cent of the primary with careful processing | **yes**, if the system is towed at low altitude |

**Decision:** reject bathymetry, magnetics and gravity as detection tools; use
sub-bottom profiling to *map the burial* and deep-towed EM (with an IP/induced
polarisation measurement if available) as the detection survey, over targets
nominated by the vent-field setting.

**Confirmation:** the only measurement that confirms a sulphide body rather than
an alteration halo is direct sampling — a drill core or a rock dredge — or a
measurement that responds to the *sulphide* property specifically. A conductive
anomaly alone cannot distinguish massive sulphide from:
conductive clays or zeolites, saline pore fluids, thick sulphide-poor alteration,
graphite-bearing sediment or basement carbon, or a buried metal object (a
historic wreck or pipeline debris). Each has its own ancillary signature
(magnetic for metal, structural for alteration, gravity for dense sulphide), so
the confirmation is a *joint* inversion plus a sample.

## ★8 — A factor-of-three tonnage estimate

| quantity | how to estimate | measured or modelled | contribution |
|---|---|---|---|
| area | multibeam plus backscatter classification into abundant/sparse/nodule-free; one threshold stated | measured, threshold chosen | 1.3–2× |
| abundance | box cores on a grid; the mean requires the variogram | measured at points, modelled between | 1.5–3× (cv ≈ 0.5, plus between-area) |
| thickness | not applicable to surface nodules (their "thickness" is the mining layer, 0–15 cm) | modelled | 1.2–1.5× |
| grade | assay of the collected nodules, with a subsample error | measured | 1.2–1.5× |
| recovery | mining-technology dependent | modelled | 2–5× if quoted as a reserve |

**Between-area variance.** §3.4 measured the error of a 400 km² area mean
saturating at about 0.9 kg/m² (6% of 15) for grids finer than the correlation
length, and showed that it stops improving with more samples of the *same* area.
To reach a factor of three overall, the between-area term must be measured: sample
several distinct areas separated by more than the range (a few kilometres), and
report the *variance between areas* alongside the within-area kriging variance.
The total variance is the sum of the two, and the between-area term is usually the
larger one at the licence scale.

**The one number that is not a geophysical measurement:** the recovery factor. No
seismic, acoustic, magnetic or electromagnetic measurement constrains how much of
the in-place metal can be mined, and a resource statement that includes it has
crossed from geophysics into engineering.
