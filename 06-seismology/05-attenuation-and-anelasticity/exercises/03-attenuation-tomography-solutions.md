# Solutions — 06-05-03 Attenuation Tomography and Temperature Interpretation

The lesson is
[03 Attenuation Tomography and Temperature Interpretation](../03-attenuation-tomography.md).
All models are **SYNTHETIC**. $R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$.

## ★ Foundational

**★1.** Band $[1, 10]\ \mathrm{Hz}$, $W = 9\ \mathrm{Hz}$, $N = 32$,
$\sigma = 0.02$. For a *ratio* of two amplitude estimates each of variance
$\sigma^{2}$, the effective noise on the log ratio is $\sigma_y =
\sigma\sqrt{2} = 0.028284$. With uniform spacing,

$$\sum_i (f_i-\bar f)^2 \approx \frac{NW^{2}}{12} = \frac{32 \times 81}{12}
= 216, \qquad \sqrt{\sum} = 14.70,$$

$$\sigma_m = \frac{\sigma_y}{\sqrt{\sum}} = \frac{0.028284}{14.70}
= 1.924\times10^{-3}\ \mathrm{Hz^{-1}} .$$

Since the fitted model is $\ln(A/A_{\text{ref}}) = -m' f$ with
$t^{*} = m'/\pi$ (up to the sign convention), the fractional error on $t^{*}$
equals the fractional error on the slope: $\sigma_{t^{*}}/t^{*} = \sigma_m/m$.
Using $t^{*} = 0.5\ \mathrm{s}$ as the reference, $m = \pi \times 0.5
= 1.5708\ \mathrm{Hz}$, so

$$\frac{\sigma_{t^{*}}}{t^{*}} = \frac{1.924\times10^{-3}}{1.5708}
= 1.22\times10^{-3} = 0.12\%.$$

The precision is set by the **bandwidth** (through $\sqrt{\sum}$, i.e. through
$W\sqrt{N/12}$) and by the noise; $t^{*}$ itself cancels from the fractional
error, so a large $t^{*}$ is measured as precisely, relatively, as a small one.

**★2.**
$$Q = \frac{\tau_r}{t^{*}} = \frac{40.0}{0.80} = 50.0 .$$
$t^{*}$ has units of seconds ($\int \mathrm{d}t/Q$, and $Q$ is dimensionless).
The ray-kernel element $G_{erc} = \int_{\text{ray}\cap c}\mathrm{d}l/v$ has units
of **seconds**: it is the time the ray spends in the cell, which is why the
forward problem over the cells is a sum of times. (The corresponding Jacobian
entry, $-\pi f G$, is dimensionless times seconds — see ★3.)

**★3.** Model vector $(1/Q_1,\dots,1/Q_{25}, b_1,\dots,b_5)$. For ray $r$ of
event $e$ at frequency $f$:

$$\frac{\partial}{\partial (1/Q_c)} = -\pi f\, G_{erc}, \qquad
\frac{\partial}{\partial b_e} = 1, \qquad \frac{\partial}{\partial b_{e'}} = 0
\;\; (e' \neq e).$$

Units: $1/Q$ is dimensionless and $G$ is seconds, so the first entry is
$\mathrm{s^{-1}} \times \mathrm{s} = $ dimensionless; the data are
$\ln(A/A_{\text{ref}})$, also dimensionless; the amplitude entries are
dimensionless as well. Every entry therefore matches the data, and the *products*
$G\,(1/Q)$ are times — the check that catches the commonest unit error in
attenuation tomography, which is dropping the seconds in $G$.

## ★★ Applied

**★★4.** **(a)** The discrepancy principle selects the **largest** $\lambda$
whose misfit is still at the noise level: misfits are 0.0199 at
$\lambda = 10^{-8}, 10^{-7}, 10^{-6}$ — all at the noise level $\sigma = 0.02$,
indeed marginally below it — and rise to 0.0210 at $10^{-5}$ and 0.0450 at
$10^{-4}$. So $\lambda = 10^{-6}$ is the selection: it has the smallest model
error among those that still fit the data to the noise level
($2.4\times10^{-3}$, essentially the minimum $2.4\times10^{-3}$), whereas
$\lambda = 10^{-8}$ has twice the model error
($5.1\times10^{-3}$) for no gain in misfit. Fitting *below* the noise level is
fitting noise.

**(b)** For $\lambda \ge 10^{-5}$ the damping term $\lambda\|m\|^{2}$ becomes
comparable with the data misfit, so the solution is pulled away from the
least-squares point and the misfit rises — the regularisation bias, visible as a
misfit increase, which is the operational signal that $\lambda$ is too large.

**(c)** With half the noise the whole model-error column would shrink (roughly
proportionally to $\sigma$ in the well-resolved directions), and the largest
acceptable $\lambda$ would move *down* — the smallest misfit achievable falls,
so damping starts to show in the misfit at a smaller $\lambda$. The chosen
$\lambda$ is a function of the noise level, which is exactly why it must be
reported with the image.

**★★5.** **(a)** $30 - 22 = 8$ exact null directions at the stated threshold.
(The demonstration reports exactly this for the same configuration.)

**(b)** Because the amplitude block of the Jacobian is an identity on each
event's rays, so it is full rank. If a vector $v$ had a non-zero amplitude
component, $Jv$ would have a non-zero component in the amplitude rows, which
cannot be cancelled by the $1/Q$ part; hence $Jv = 0$ forces the amplitude block
of $v$ to vanish. All eight exact null directions are therefore spatial, and the
source–amplitude trade-off is only ever an *approximate* degeneracy.

**(c)** *Acceptable:* "The $1/Q$ field is resolved only in the subspace spanned by
the 22 singular directions above the threshold; the component of the model
along the 8 exact null directions is not determined by these data, and a
perturbation of up to $1.0\times10^{-3}\ \mathrm{s^{-1}}$ in rms $1/Q$
(25\% of the mean field) changes the data by less than one part in $10^{16}$."
*Not acceptable:* "Cell 24 has $1/Q = 0$" — the demonstration shows that this
cell is given exactly zero by the fit because it lies in the null space, so the
value is an artefact of the minimum-norm choice, not a measurement.

**★★6.** **(a)**
$$\frac{\mathrm{d}\ln\tau}{\mathrm{d}T} = -\frac{H^{*}}{RT^{2}}
= -\frac{2.5\times10^{5}}{8.314 \times 1.44\times10^{6}}
= -\frac{2.5\times10^{5}}{1.1972\times10^{7}} = -2.088\times10^{-2}\
\mathrm{K^{-1}} .$$

**(b)** A factor 4 in $\tau$ means $|\ln 4| = 1.386294$ in $\ln\tau$, so
$$\Delta T = \frac{\ln 4}{H^{*}/(RT^{2})} = \frac{1.386294}{2.088\times10^{-2}}
= 66.4\ \mathrm{K}.$$

**(c)** $\Delta T = \ln 4 \cdot RT^{2}/H^{*}$ is *inversely* proportional to
$H^{*}$, so a $\pm15\%$ error in $H^{*}$ is a $\mp15\%$ error in $\Delta T$:
$66.4 \times (1 \mp 0.15)$, i.e. $\Delta T = 57\ \mathrm{K}$ to
$78\ \mathrm{K}$. The inferred temperature contrast is only as good as the
activation enthalpy, which is why its provenance must be stated (and why the
inference is a *model* statement, not a measurement).

## ★★★ Research-oriented

**★★★7.** **Test design.**

- **Input model:** a known $1/Q$ field with features at two scales — a broad
  anomaly (two or three cells across) and a single-cell spike, plus a background.
  A checkerboard is acceptable but a two-scale model is better because it
  distinguishes "not resolved at all" from "smeared".
- **Ray geometry:** the actual ray fan of the proposed experiment (not a uniform
  parallel-ray fan), because the null space is a property of the geometry. State
  the number of events, receivers, and rays; include the amplitude parameters as
  unknowns.
- **Noise:** synthetic Gaussian noise with the measured $\sigma$ in $\ln A$, over
  many independent realisations (at least 20), because one realisation cannot
  distinguish bias from noise.
- **Inversion settings:** the parametrisation, the damping rule and how
  $\lambda$ was chosen (e.g. by the discrepancy principle against the same
  $\sigma$), and any constraints. Report the same settings used later on real
  data.
- **Diagnostics to report:** the singular spectrum and numerical rank; the
  resolution matrix (or a row of it, i.e. the smoothing kernel for one cell);
  the rms recovery error per cell and the rms null-space component of the input
  model; the recovered value versus the true value for the spike, before and
  after damping.
- **Criterion for "resolvable":** a feature is resolvable if the recovered
  anomaly has the correct sign and the confidence interval excludes zero
  *across the noise realisations*, and if its amplitude is recovered to better
  than $50\%$; otherwise it is reported as "a feature of scale $\ge$ the
  smoothing length", not as a cell value.

**What failure looks like, and the fix:** if the recovered spike amplitude is
systematically low by a factor of 2 with no dependence on noise, the cause is the
smoothing kernel, not the data; the design fix is to add rays crossing that cell
(geometry), or to reduce the damping while accepting a noisier image, not to
adjust the report. If the recovered field has a large component along a null
direction that varies wildly between realisations, the parametrisation is
over-fitted for the geometry and cells should be merged.

**★★★8.** **(a)** The table gives central-decade deviations of $19.08\%$ at
$N = 4$, $1.77\%$ at $N = 6$ and $0.17\%$ at $N = 8$, with a $5\%$ target
falling between $N = 4$ and $N = 6$: **$N = 6$ relaxations suffice** (with
$N = 8$ giving a comfortable margin). The table cannot answer the question
exactly because it reports two different metrics (maximum deviation over the
central decade, and the fraction of the full band within $10\%$) at seven values
of $N$; a $5\%$ specification on a two-decade band involves the band-edge
behaviour too, so the honest answer is to **re-run the fit with the requested
target, metric and band** (which the demonstration's code supports by changing
its inputs) rather than to interpolate a table.

**(b)** Each relaxation requires one memory variable per grid point and one extra
update per time step, so the storage and the per-step cost are both linear in
$N$; memory, not accuracy, is usually the binding constraint in 3-D
finite-difference viscoacoustic modelling, since the state must be held for every
grid point at every time step. That is why production codes accept a plateau with
$N$ of order a few rather than an exact constant $Q$.

**(c)** The band-edge value differs from the target by a factor
$521.776/100 = 5.218$, i.e. $\ln Q$ is wrong by $\ln 5.218 = 1.652$. At
$T \approx 1000\ \mathrm{K}$, where $\mathrm{d}\ln\tau/\mathrm{d}T = 3.61\times
10^{-2}\ \mathrm{K^{-1}}$, this converts to a spurious temperature of

$$\Delta T = \frac{1.652}{3.61\times10^{-2}} = 45.8\ \mathrm{K}.$$

So a band edge left inside the analysis band can manufacture a temperature
anomaly of several tens of kelvin with no temperature change at all — comparable
with the $\sim 64\ \mathrm{K}$ that a genuine factor-of-10 $Q$ contrast would
imply. The practical consequence: **report the band, and check that $Q$ is flat
across it before attaching a temperature to it.**

## Module mastery checkpoint (worked)

The module [README](../README.md) sets a checkpoint on a $60\ \mathrm{km}$ path
in a medium with $v = 3400\ \mathrm{m\,s^{-1}}$, a spectral-ratio slope
$m = 0.55\ \mathrm{Hz^{-1}}$ fitted over $[0.5, 8]\ \mathrm{Hz}$ with 40 samples
and $\sigma_y = \sqrt{2}$, plus a coda measurement $Q_{\text{coda}} = 300$.

**(a)**
$$Q_{\text{app}} = \frac{\pi \Delta x}{v\,m}
= \frac{3.141593 \times 6\times10^{4}}{3400 \times 0.55}
= \frac{1.884956\times10^{5}}{1870} = 100.8,$$
$$\tau_r = \frac{x}{v} = \frac{6\times10^{4}}{3400} = 17.647\ \mathrm{s},
\qquad t^{*} = \frac{\tau_r}{Q} = \frac{17.647}{100.8} = 0.1751\ \mathrm{s},$$
$$\alpha(4\ \mathrm{Hz}) = \frac{\pi f}{Q v}
= \frac{3.141593 \times 4}{100.8 \times 3400} = 3.667\times10^{-5}\
\mathrm{m^{-1}} .$$

**(b)** $W = 7.5\ \mathrm{Hz}$, $N = 40$:
$\sum_i(f_i-\bar f)^2 \approx NW^{2}/12 = 40 \times 56.25/12 = 187.5$,
$\sqrt{\sum} = 13.693$, so

$$\sigma_m = \frac{\sqrt{2}}{13.693} = 0.10328\ \mathrm{Hz^{-1}}, \qquad
\frac{\sigma_Q}{Q} = \frac{\sigma_m}{m} = \frac{0.10328}{0.55} = 18.8\%.$$

**Not remotely a $1\%$ measurement.** Reaching $1\%$ would need
$\sqrt{\sum} = \sqrt{2}/(0.55 \times 0.01) = 257$, i.e. a band of
$W = \sqrt{12 \times 66\,000/40} = 141\ \mathrm{Hz}$, which no body-wave
measurement has.

**(c)** With $1/Q_{\text{app}} = 0.0099207$ and
$1/Q_{\text{coda}} = 1/300 = 0.0033333$:
$$\frac{1}{Q_{\text{int}}} = 0.0099207 - 0.0033333 = 0.0065874
\Rightarrow Q_{\text{int}} = 151.8 .$$
The assumption is that the coda is **single-scattered**, so that its decay is
governed by the intrinsic loss of the volume it samples — i.e.
$Q_{\text{coda}} \approx Q_{\text{int}}$ — and that the coda window contains no
depth phases. In multiple scattering this equivalence fails and the coda decay is
set by the transport mean free path.

**(d)** The implied $Q$ contrast for $\Delta T = 50\ \mathrm{K}$ with
$H^{*} = 300\ \mathrm{kJ\,mol^{-1}}$ at $T = 1000\ \mathrm{K}$ is

$$\frac{Q_2}{Q_1} = \exp\!\left(\frac{H^{*}\Delta T}{RT^{2}}\right)
= \exp\!\left(\frac{3.0\times10^{5} \times 50}{8.314 \times 10^{6}}\right)
= e^{1.8042} = 6.1,$$

i.e. the same anomaly would be produced by a factor-6 change in $Q$. Two
non-thermal explanations, and the test for each:

1. **Scattering.** Test: the two-band frequency test of
   [lesson 02](02-scattering-vs-intrinsic-solutions.md) over two sub-bands
   straddling a regime change; an intrinsic-only medium gives a ratio of 1,
   scattering gives a ratio far from 1 (the demonstration measures 1.95 against
   1.00).
2. **A band-edge artefact.** Test: widen the analysis band and check whether
   $1/Q$ is flat within it; the demonstration's band-edge value
   ($Q = 521.776$ against a target of 100 at $0.001\ \mathrm{Hz}$) shows that a
   factor $\sim 5$ can appear with no physical change.

(A third, the fluid or melt explanation, would be tested with an independent
$V_p/V_s$ measurement — the topic of the sibling modules below.)
