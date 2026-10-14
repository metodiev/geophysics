# Solutions — 06-03-07 Discriminating Explosions from Earthquakes

> **Read after attempting the exercises.** All sources are SYNTHETIC. No yield,
> catalogue magnitude or calibration constant appears anywhere; the magnitude
> scales in the demo are labelled stand-ins and only differences are interpreted.

Lesson: [07 Discriminating Explosions from Earthquakes](../07-nuclear-explosion-sources.md).

Constants: $\beta = 3500\ \mathrm{m\,s^{-1}}$, $k = 0.37$,
$k\beta = 1295\ \mathrm{m\,s^{-1}}$.

---

## ★1 — The isotropic pattern

For $M = M_{\text{iso}}I$ and any unit vector,
$\hat r^{\mathsf T}M\hat r = M_{\text{iso}}\,\lVert\hat r\rVert^{2}
= M_{\text{iso}}$. Taking $\hat r = (1,0,0)$, $(0,1,0)$ and
$(1,1,1)/\sqrt3$, the value is $M_{\text{iso}}$ in every case: the amplitude is
**constant in direction and positive**.

**Measured compression fraction:** $1.0000$ over $5000$ random directions.

**Why no nodal planes:** a nodal surface is the locus of directions where $A = 0$.
$A = M_{\text{iso}}$ never vanishes for $M_{\text{iso}}\neq0$, so there is no
such locus. Geometrically, a sphere of radius $|A|$ is painted a single colour,
which is why an isotropic source has no focal mechanism.

---

## ★2 — The $2^{-N}$ table

| $N$ | $2^{-N}$ | $-\log_{10}p$ |
|---|---|---|
| 6 | $1.5625\times10^{-2}$ | 1.81 |
| 12 | $2.4414\times10^{-4}$ | 3.61 |
| 20 | $9.5367\times10^{-7}$ | 6.02 |

Computations: $2^{-6} = 1/64 = 0.015625$; $2^{-12} = 1/4096 = 2.4414\times10^{-4}$;
$2^{-20} = 1/1\,048\,576 = 9.5367\times10^{-7}$.

The $N = 6$ and $N = 20$ rows match the demo's table ($1.562\times10^{-2}$ and
$9.537\times10^{-7}$). The probability is a statement about the **source**: it is
the chance that a double couple would produce an all-compressional pattern at $N$
independent stations, and it is the same number for any network, because it
depends only on the radiation pattern.

---

## ★3 — Radius and corner frequency

**(a)** $\Delta\sigma = 3.0\times10^{6}\ \mathrm{Pa}$:

$$a^{3} = \frac{7}{16}\frac{M_0}{\Delta\sigma}
= 0.4375\times\frac{1.0\times10^{15}}{3.0\times10^{6}}
= 0.4375\times3.3333\times10^{8} = 1.45833\times10^{8},$$
$$a = 526.4\ \mathrm{m},\qquad f_c = \frac{1295}{526.4} = 2.4601\ \mathrm{Hz}.$$

**(b)** $\Delta\sigma_{\text{eff}} = 3.0\times10^{8}\ \mathrm{Pa}$:

$$a^{3} = 0.4375\times\frac{1.0\times10^{15}}{3.0\times10^{8}}
= 1.45833\times10^{6},\qquad a = 113.4\ \mathrm{m},$$
$$f_c = \frac{1295}{113.4} = 11.417\ \mathrm{Hz}.$$

**Ratio:**

$$\frac{f_c^{(b)}}{f_c^{(a)}} = \frac{11.417}{2.4601} = 4.641,$$

against $100^{1/3} = 4.6416$. They agree because
$a\propto\Delta\sigma^{-1/3}$ and $f_c\propto a^{-1}$, so
$f_c\propto\Delta\sigma^{1/3}$ exactly. The demo's $M_0 = 10^{15}$ rows give
$a = 526.4$, $f_c = 2.4603$ and $a = 113.4$, $f_c = 11.4196$.

---

## ★4 — Why one band is blind and the other is not

The model spectrum is $\Omega(f) = \Omega_0/(1+(f/f_c)^{2})$, i.e. the plateau
$\Omega_0$ for $f\ll f_c$ and the tail $\Omega_0(f_c/f)^{2}$ for $f\gg f_c$.

**Long band, 0.02–0.1 Hz.** Both corner frequencies from ★3 — $2.46\ \mathrm{Hz}$
and $11.42\ \mathrm{Hz}$ — are far above the top of the long band. So at every
frequency in the band the ratio $(f/f_c)^{2}$ is at most
$(0.1/2.4601)^{2} = 1.65\times10^{-3}$, and $\Omega(f)\approx\Omega_0$ to better
than $0.2\%$ **regardless of which of the two sources is measured**. The band sees
the plateau, and the plateau is proportional to $M_0$ only.

**Short band, 0.5–2.0 Hz.** Now the band straddles the corners:
$(0.5/2.4601)^{2} = 0.041$ and $(2/2.4601)^{2} = 0.661$ for the earthquake, so
the band-average amplitude is already appreciably below the plateau;
for the explosion $(0.5/11.417)^{2} = 0.0019$ and $(2/11.417)^{2} = 0.031$, so the
band is still essentially on the plateau. The two sources therefore differ in the
short band while agreeing in the long band.

**Summary.** The long band measures $\Omega_0\propto M_0$; the short band measures
where the corner sits relative to fixed band edges — i.e. the ratio
$M_0/a^{3}$, the stress drop. That is exactly the division of labour the
discriminant uses.

---

## ★5 — Converting the offset to an amplitude ratio

The synthetic magnitude is
$m = \log_{10}(\text{amplitude}/\text{period}) + \log_{10}(d/100\,\mathrm{km})$.
At matched distance and period, an offset $\Delta m$ in the magnitude is a factor

$$10^{\Delta m} = 10^{0.605} = 4.03$$

in amplitude. Physically: for two sources of the **same long-period size**, the
isotropic one radiates about **four times** more amplitude in the $0.5$–$2\
\mathrm{Hz}$ band. Because its source is smaller at the same moment
($a = 526.4\ \mathrm{m}$ against $2443.2\ \mathrm{m}$ — a factor $4.64$), its
corner frequency is $4.64$ times higher, so much more of its spectrum lies inside
the short-period band.

**Caveat.** The factor $4.03$ is a property of the assumed stress-drop ratio of
$100$, not a universal number, and the demo says so explicitly.

---

## ★6 — Interpreting "the source-level probability is $9.8\times10^{-4}$"

**Station count:** $N = 10$, since $2^{-10} = 9.766\times10^{-4}$.

**Assumption:** the $N$ station readings are **independent**, each compressional
with probability exactly $1/2$ under the double-couple hypothesis — i.e. the
stations sample the focal sphere independently and every first motion is read
correctly.

**A mechanism that destroys it:** a systematic error common to many stations.
A single wrong velocity model, or one mis-set instrument polarity affecting a
group of stations, or a geometry that places many stations inside the same
compressional lobe, makes them agree for reasons unrelated to the source. The
$N$ readings then carry far less than $N$ independent bits, and the true
false-positive rate is the binomial value for an **effective** $N$ much smaller —
which can easily be an order of magnitude larger in probability.

---

## ★7 — The implosive third class

With $M = -M_{\text{iso}}I$ and $M_{\text{iso}}>0$:

$$\mathrm{tr}(M) = -3M_{\text{iso}} < 0,$$

and for every unit ray direction $\hat r^{\mathsf T}M\hat r = -M_{\text{iso}} < 0$:
**every direction is dilatational**, with no nodal planes (again a single-coloured
focal sphere, but of the opposite colour to an explosion).

**Separation from the other two classes.** First motions alone separate an
implosion from an explosion *completely* (all directions dilatational vs all
compressional) and from an earthquake with the same one-sided logic as Section 4.1
of the lesson — one compressional reading refutes a pure implosion. In the
moment-tensor language the three classes differ in
$\mathrm{sgn}\,\mathrm{tr}(M)$: negative for implosion, zero for a double couple,
positive for an explosion. The magnitude of $\mathrm{tr}(M)$ (equivalently
$M_{\text{iso}}$) then measures *how much* volume change, which is the
quantitative version of the same statement.

---

## ★8 — A combined discriminant and its calibration (specification)

**Observables** (chosen to rest on different physics):

1. **First-motion polarity pattern** — source radiation geometry. Statistic: the
   number of dilatational readings (and the fraction, since an explosion has
   none).
2. **Short-period/long-period band-amplitude ratio** — source spectral shape, from
   ★4.
3. **Depth and depth-consistency** — hypocentral depth relative to a tectonic
   depth distribution, plus whether the depth is stable under relocation with
   different velocity models.

**Decision rule.** Combine them into a single score, e.g. a likelihood ratio
$L = p(\text{data}\mid\text{explosion})/p(\text{data}\mid\text{earthquake})$ under
each source model, and declare "explosion-like" when $L$ exceeds a threshold
chosen to fix the false-positive rate at a stated value. The threshold is what
carries the calibrated meaning; the individual observables only enter through
their likelihoods.

**Calibration.** The false-positive rate **cannot** be computed from the source
models, because it is dominated by path, site, instrument and network effects that
are not in the source model. It must be estimated empirically from a reference
population of *known* earthquakes (and, separately, from well-recorded reference
explosions), using the same processing pipeline. This is why the demo's $2^{-N}$ is
labelled an upper bound: it is a source-level quantity, and the network-level rate
requires data.

**Assumptions.** (1) The polarity observable needs correct instrument polarity and
reliable picks; (2) the spectral observable needs path and site equalisation
between the two populations, and a common $k$; (3) the depth observable needs a
velocity model good enough that relocation uncertainty is smaller than the depth
difference being tested. Each can fail independently, which is the argument for
combining them: a discriminant that requires three independent conditions to be
fooled is harder to defeat than any single one.

---

## ★9 — Correlated stations and the effective $N$ (specification)

**Correlation model.** Draw station positions from a *clustered* process rather
than a uniform distribution: pick $K$ cluster centres with a correlation length
$r_c$ and place stations within $r_c$ of a centre. Because a double couple's
polarity pattern varies on the scale of the nodal-plane separation, stations
closer together than the lobe structure sample nearly the same value of
$A(\hat r)$ — their readings are correlated.

**Statistic.** Estimate the **effective number of independent stations**
$N_{\text{eff}}$ as follows: (i) generate $N$ stations from the clustered process;
(ii) compute the polarity indicator $s_i = \mathrm{sign}\,A(\hat r_i)$ for a fixed
double couple; (iii) form the "variance inflation" from the empirical variance of
$\sum_i s_i$ over many random mechanism orientations, and compare it with the
independent-station value $N$:

$$N_{\text{eff}} = \frac{\mathrm{Var}\left(\sum_i s_i\right)\big|_{\text{independent}}}
{\mathrm{Var}\left(\sum_i s_i\right)\big|_{\text{clustered}}}
= \frac{N}{\mathrm{Var}\left(\sum_i s_i\right)\big|_{\text{clustered}}}.$$

(iv) Report $N_{\text{eff}}/N$ as a function of $r_c$.

**Prediction.** For $r_c$ large compared with the source-station distance, all $N$
stations sit inside one lobe and $N_{\text{eff}}\to1$; for $r_c\to0$ the stations
are effectively independent and $N_{\text{eff}}\to N$. The interesting prediction
to test is the shape of the transition $N_{\text{eff}}(r_c)$, which is set by the
angular size of the lobes as seen from the cluster. The measured curve is the
correction factor one would apply to the $2^{-N}$ table.

---

## ★10 — The two-band degeneracy

**To first order.** Let the band amplitudes be
$B_s = \overline{\Omega}_{\text{short}}(M_0,a)$ and
$B_l = \overline{\Omega}_{\text{long}}(M_0,a)$, where $a$ enters only through
$f_c = k\beta/a$. Holding $M_0$ fixed changes both bands through $f_c$; holding
$a$ fixed scales both bands linearly with $M_0$. Invariance of the *pair* requires
the two effects to cancel in both bands simultaneously:

$$\frac{\partial\ln B_s}{\partial\ln M_0}\,\mathrm{d}\ln M_0
+ \frac{\partial\ln B_s}{\partial\ln a}\,\mathrm{d}\ln a = 0,$$
$$\frac{\partial\ln B_l}{\partial\ln M_0}\,\mathrm{d}\ln M_0
+ \frac{\partial\ln B_l}{\partial\ln a}\,\mathrm{d}\ln a = 0.$$

The long band is on the plateau, so
$\partial\ln B_l/\partial\ln a\approx0$ and
$\partial\ln B_l/\partial\ln M_0 = 1$. Then the second equation forces
$\mathrm{d}\ln M_0 = 0$: the long band **pins the moment**. Substituting into the
first gives
$\mathrm{d}\ln a = 0$ only if
$\partial\ln B_s/\partial\ln a \neq 0$; but that derivative is small when
$f_c\gg$ the short band (both sources on the plateau there), and the set of
$(M_0,a)$ pairs for which the short-band change is smaller than the $\pm10\%$
tolerance is exactly the $1.25$-decade ridge the demo measures.

**Why it is unavoidable.** Two numbers cannot determine more than two parameters
independently; the relation between them is one equation, so the solutions lie on
a one-dimensional set (a curve) in the plane, and its *length* is set by how
weakly the second band responds to the second parameter. Enlarging the tolerance
lengthens the curve; it does not thicken it into a region.

**What breaks it.** A third observation that responds to source dimension
*independently of the two band amplitudes* — for example an independently
determined source duration from the moment-rate function
[04 Source Time Functions](../04-source-time-function.md), or directivity from an azimuthal set of
durations, or a finite-fault dimension from waveform modelling. Such an
observation constrains $a$ (or, equivalently, $k\beta/a$) without going through
the band amplitudes, and the intersection of the ridge with that constraint
picks out a point. Note what does **not** break it: adding more stations in the
same two bands, because that reduces the *noise* on the same two numbers rather
than adding an independent equation.
