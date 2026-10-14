# Solutions — 02-09-04 Gamma-Ray Spectrometry and Natural Radioelements

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

No answer below mixes the three categories. **Computed** results follow from the
equations of the lesson; **tabulated** inputs are the nuclear data and the
heat-generation coefficients, each of which needs a cited compilation; **model**
inputs are the detector parameters, the stripping coefficients, the soil density
and the window definitions. All conversion factors were recomputed from the
stated constants, not copied.

---

## ★1 — Specific activities

**(a)** $N$ per kg of rock for 1 ppm: mass fraction $10^{-6}$, so
$N = 10^{-6} \times 6.022\,140\,76 \times 10^{23} \times 10^3/232.038 =
2.5953 \times 10^{18}$ atoms. With
$\lambda = \ln 2/(1.405 \times 10^{10} \times 3.155\,76 \times 10^7) =
1.5633 \times 10^{-18}$ s⁻¹, $A = \lambda N = \mathbf{4.0573}$ Bq per kg.

**(b)** The quoted factor is 4.1, so the difference is 1.0 per cent. It is
entirely in the tabulated half-life and the molar mass: a half-life of
$1.39 \times 10^{10}$ a would give 4.1. **This is the reason a conversion factor
must be recomputed from the compilation you cite**, and the reason the difference
is not a mistake.

**(c)** 1 % K is a mass fraction $10^{-2}$, of which $1.17 \times 10^{-4}$ is
$^{40}$K: $N = 1.17 \times 10^{-6} \times 6.022\,140\,76 \times 10^{23} \times
10^3/39.0983 = 1.8021 \times 10^{19}$ atoms per kg. With
$\lambda = \ln 2/(1.248 \times 10^9 \times 3.155\,76 \times 10^7) =
1.759\,98 \times 10^{-17}$ s⁻¹, $A = \mathbf{317.17}$ Bq per kg. The commonly
quoted factor is 313, i.e. 1.3 per cent lower.

**(d)** "Equivalent thorium" assumes that the $^{232}$Th series is in **secular
equilibrium**, so that the activity of the measured gamma line equals the
activity of the parent and one conversion factor connects them.

---

## ★2 — Resolution

**(a)** $\mathrm{FWHM}/E = 7.00$ % at 662 keV, so FWHM $= 46.34$ keV
$= k\sqrt{E}$; with $E$ in keV, $k = 46.34/\sqrt{662} = \mathbf{1.801}$
keV^½.

**(b)** At 1460.8 keV: FWHM $= 1.801 \times \sqrt{1460.8} = 68.84$ keV, i.e.
**4.71 per cent**. The demo prints 68.8 keV and 4.71 per cent.

**(c)** At 2614.5 keV: FWHM $= 1.801 \times \sqrt{2614.5} = 92.09$ keV, i.e.
**3.52 per cent**. The demo prints 92.1 keV and 3.52 per cent.

**(d)** The absolute width grows because the number of carriers is proportional
to the deposited energy, so the absolute standard deviation grows as $\sqrt{E}$.
The *relative* width is that standard deviation divided by $E$, which therefore
falls as $1/\sqrt E$. The 1460.8 keV potassium line is resolved better than the
662 keV caesium line even though its peak is physically wider on the chart.

---

## ★3 — Compton edges and window contamination

$E_\mathrm{edge} = E\alpha/(1 + \alpha)$ with $\alpha = E/m_ec^2$ — equivalently
$E_\mathrm{edge} = 2\alpha E/(1 + 2\alpha)$ — giving:

**(a)** $\alpha = 2.6145/0.510\,998\,95 = 5.1166$;
$E_\mathrm{edge} = 2.6145 \times 5.1166/(1 + 2 \times 5.1166) = \mathbf{2.3817}$
MeV.

**(b)** $\alpha = 1.7645/0.510\,998\,95 = 3.4530$;
$E_\mathrm{edge} = \mathbf{1.5413}$ MeV.

**(c)** $\alpha = 1.4608/0.510\,998\,95 = 2.8587$;
$E_\mathrm{edge} = \mathbf{1.2433}$ MeV.

**(d)** The potassium window is 1.37–1.57 MeV and the potassium line's own
Compton edge is at 1.2433 MeV, i.e. **below** the window, so the window contains
almost none of its own continuum — which is why the potassium window is the
cleanest of the three and why it can be used as a gain reference. But the
thorium line at 2.6145 MeV has its edge at 2.3817 MeV, which is above the entire
uranium window, and its continuum therefore *extends across* both the uranium
and the potassium windows. That is the physical origin of the stripping
coefficients $\alpha$ and $\beta$: they are not calibration fictions but the
Compton continuum of a real line falling in the wrong window.

---

## ★★4 — Stripping

**(a)** $c_\mathrm{Th} = 260.0$;
$c_\mathrm{U} = 420.0 + 0.36 \times 260.0 = 513.6$;
$c_\mathrm{K} = 850.0 + 0.52 \times 260.0 + 0.74 \times 420.0 = 850.0 + 135.2 +
310.8 = \mathbf{1296.0}$. The demo prints 1296.0, 513.6, 260.0.

**(b)** Invert from the top: $t_\mathrm{Th} = 260.0$;
$t_\mathrm{U} = 513.6 - 0.36 \times 260.0 = 420.0$;
$t_\mathrm{K} = 1296.0 - 0.52 \times 260.0 - 0.74 \times 420.0 = 1296.0 -
135.2 - 310.8 = \mathbf{850.0}$. Recovery is exact to round-off, which verifies
the inverse.

**(c)** With $\gamma = 0.74 \times 1.01 = 0.7474$: $t_\mathrm{U}$ is unchanged
at 420.0 (it does not involve $\gamma$), and
$t_\mathrm{K} = 1296.0 - 135.2 - 0.7474 \times 420.0 = 1296.0 - 135.2 - 313.91 =
\mathbf{846.89}$. The error is $-3.11$ counts, i.e. $-0.37$ per cent of 850. The
demo prints 846.89 and $-3.11$.

**(d)** With $\beta = 0.52 \times 1.01 = 0.5252$:
$t_\mathrm{K} = 1296.0 - 0.5252 \times 260.0 - 310.8 = 1296.0 - 136.55 - 310.8 =
\mathbf{848.65}$, an error of $-1.35$ counts or $-0.16$ per cent. The potassium
result is therefore about twice as sensitive to $\gamma$ (the uranium
contribution) as to $\beta$ (the thorium contribution) in this dataset, for a
simple reason: the uranium contribution subtracted from the potassium window is
$0.74 \times 420 = 310.8$ counts against the thorium's $0.52 \times 260 = 135.2$,
so a proportional error in the larger subtrahend does more damage. The general
rule is that a window's error is governed by the size of what is subtracted from
it.

---

## ★★5 — Depth of investigation

**(a)** With $\mu = 0.08369$ cm⁻¹:
$z(0.5) = 0.693\,147/0.08369 = \mathbf{8.28}$ cm;
$z(0.9) = 2.302\,585/0.08369 = \mathbf{27.51}$ cm;
$z(0.99) = 4.605\,170/0.08369 = \mathbf{55.03}$ cm. The demo prints 8.28 and
27.51.

**(b)** 27.5 cm against the commonly quoted 30 cm: the quoted figure is the same
quantity rounded, computed with an illustrative attenuation coefficient. State
which $\mu$, which density and which fraction you used, because the quoted figure
is nowhere near a universal constant.

**(c)** $z(0.9) = 2.302\,585/0.06018 = \mathbf{38.26}$ cm. The ratio is
$38.26/27.51 = \mathbf{1.39}$, so the thorium window samples about 40 per cent
deeper.

**(d)** Water has a higher mass attenuation coefficient than dry soil at these
energies and, more importantly, replaces air in the pore space, so it increases
the *mass per unit area* above a given depth. The low-energy (potassium) window
is attenuated more than the high-energy (thorium) one, because attenuation falls
with energy. The ratio therefore changes while the concentrations do not — which
is why a survey needs a moisture correction and why surveys flown in different
weather are not directly comparable.

---

## ★★6 — Heat production

**(a)** $A = 2700 \times 10^{-5} \times (9.52 \times 2.5 + 2.56 \times 11.0 +
3.48 \times 2.5) = 0.027 \times (23.80 + 28.16 + 8.70) = 0.027 \times 60.66 =
\mathbf{1.638}$ µW m⁻³.

**(b)** U: $23.80/60.66 = \mathbf{39.2}$ %; Th: $28.16/60.66 = \mathbf{46.4}$ %;
K: $8.70/60.66 = \mathbf{14.3}$ %.

**(c)** The uranium coefficient 9.52, in the unit system of equation (4), means
$9.52 \times 10^{-11}$ W per kg of rock per ppm. Dividing by the specific
activity of 12.3472 Bq kg⁻¹ per ppm gives $7.71 \times 10^{-12}$ J per decay, or
**48.1 MeV** per decay. That is physically sensible for a $^{238}$U decay: the
series emits eight alpha particles of a few MeV each plus betas and gammas, and
after removing the neutrino energy the total is of this order. A coefficient
wrong by a factor of ten would show up immediately.

**(d)** The potassium coefficient is small because each $^{40}$K decay deposits
only about 0.68 MeV, against about 48 MeV for $^{238}$U — a factor of 70 per
decay. But potassium is present at per cent levels while uranium is present at
ppm levels, a factor of $10^4$, and the two factors partly cancel: the potassium
term in (a) is 8.70 out of 60.66, i.e. 14 per cent. In a potassium-rich rock the
fraction rises further. Reporting all three elements is therefore necessary, and
reporting a single "heat production" number hides the fact that they are measured
separately and can be in or out of equilibrium independently.

---

## ★★★7 — Running the demo

**(a)** 1 ppm U: 12.3472 Bq kg⁻¹ against a quoted 12.4 (−0.4 per cent); 1 ppm Th:
4.0573 against 4.1 (−1.0 per cent); 1 % K: 317.1654 against 313 (+1.3 per cent).

**(b)** Measured: K = 1296.0, U = 513.6, Th = 260.0 counts. Stripped:
K = 850.000000, U = 420.000000, Th = 260.000000, with recovery error
0.00e+00 on all three.

**(c)** $\alpha + 1$ %: K = 850.69 (+0.69), U = 419.06; $\beta + 1$ %:
K = 848.65 (−1.35); $\gamma + 1$ %: K = 846.89 (−3.11); all three:
K = 846.24 (−3.76).

**(d)** $\|M\|_\infty = 2.2600$, $\|M^{-1}\|_\infty = 1.9936$, product (the
condition number) 4.5055. A condition number of 4.5 means the sequential
inversion can amplify an input error by up to a factor of 4.5 — which is why a
1 per cent coefficient error produced a 0.4 per cent concentration error and not
a 5 per cent one.

**(e)** Granite ($\rho = 2650$, K = 3.50 %, U = 4.00 ppm, Th = 15.00 ppm):
$A = 2.3495$ µW m⁻³, with contributions U 43.0 per cent, Th 43.3 per cent,
K 13.7 per cent.

**(f)** $z(0.9)$: K 27.51 cm, U 30.49 cm, Th 38.26 cm.

**(g)** Computed: the specific activities, the stripping inverse and its
condition number, the heat production once the coefficients are supplied, and the
depths once $\mu$ is supplied. Tabulated: every half-life, abundance and molar
mass, the heat-generation coefficients, the window definitions and the line
energies. Model: the NaI resolution, the peak-to-total ratio, the stripping
coefficients and the soil density of 1.60 g cm⁻³. One further input is a
*physical* assumption disguised as an instrument parameter — the secular
equilibrium of the uranium and thorium series — and it is the one most likely to
fail.

---

## ★★★8 — Interpretation limits

**(a)** Two mechanisms, both requiring no change in uranium concentration.
First, **disequilibrium**: if radon has escaped from the soil-covered area, the
$^{226}$Ra–$^{222}$Rn pair is out of equilibrium and the $^{214}$Bi line that the
U window measures reports less activity than the parent uranium — so the soil
area reads lower eU. Second, **attenuation**: the soil cover itself, especially
if wet, attenuates the low-energy windows selectively and changes the
count-rate-to-concentration conversion. A third mechanism worth naming is
**dilution by a low-uranium cover**, which is a real concentration difference but
in the *soil* and not in the granite.

**(b)** The thorium window sits at the highest energy, where the flux from the
ground is lowest and the count rate in any fixed counting time is smallest. The
relative uncertainty of a Poisson count is $1/\sqrt N$, so the smallest count
rate gives the largest relative uncertainty — and after stripping, the thorium
result is not diluted but the *uranium and potassium* results inherit the
thorium window's uncertainty through the subtraction. This is why a survey
reported with three channels has three quite different detection limits.

**(c)** "The map shows the gamma-ray activity of the top few tens of centimetres
of soil and weathered rock, from which potassium concentrations have been derived
through an instrument calibration and an assumed secular equilibrium." The
corrections are the substance of the sentence, not a hedge.

**(d)** Both windows are attenuated by the same overburden, and the ratio of two
count rates therefore cancels the common part of the attenuation — the
first-order effect of moisture, of a uniform snow layer and of a slight change in
source–detector distance. What does *not* cancel is any mechanism that is
energy-dependent in a way not shared by the two windows, such as an edge in the
overburden or radon loss affecting only the uranium chain. A ratio is robust to
a common-mode error and blind to a differential one, and both statements must
appear when a ratio map is interpreted.
