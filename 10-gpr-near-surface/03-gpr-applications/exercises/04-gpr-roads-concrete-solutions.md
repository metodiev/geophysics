# Solutions — 10-03-04 GPR for Pavements, Concrete and Infrastructure Inspection

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment. Where a problem has more than one defensible answer, that
> is said.

Lesson: [04 GPR for Pavements, Concrete and Infrastructure Inspection](../04-gpr-roads-concrete.md).
All values are **SYNTHETIC** teaching values except the physical constants
$c = 0.299792458\ \mathrm{m\,ns^{-1}}$ and $\varepsilon_{\mathrm{air}} = 1$.

---

## ★1 — Metal plate calibration to thickness

$$\varepsilon_r = \left(\frac{1-R_s}{1+R_s}\right)^{2}
= \left(\frac{1+0.42}{1-0.42}\right)^{2} = \left(\frac{1.42}{0.58}\right)^{2}
= 2.44828^{2} = 5.994.$$

$$v = \frac{0.299792458}{\sqrt{5.994}} = \frac{0.299792458}{2.44828}
= 0.122450\ \mathrm{m\,ns^{-1}}.$$

$$h = \frac{vt}{2} = \frac{0.122450 \times 1.20}{2}
= 0.0734703\ \mathrm{m} = 73.47\ \mathrm{mm}.$$

Units: $R_s$ dimensionless, $\varepsilon_r$ dimensionless, $v$ in
$\mathrm{m\,ns^{-1}}$, $t$ in ns, $h$ in m (reported in mm).

Note the arithmetic is *exactly* invertible: the same two measurements give the
permittivity and the thickness with no iteration and no model beyond the plane
layer.

---

## ★2 — Resolution at $1.5\ \mathrm{GHz}$

$$v = \frac{0.299792458}{\sqrt{4.5}} = 0.141324\ \mathrm{m\,ns^{-1}},$$

$$\lambda = \frac{v}{f} = \frac{0.141324}{1.5} = 0.094216\ \mathrm{m}
= 94.2\ \mathrm{mm},$$

$$\frac{\lambda}{4} = 23.55\ \mathrm{mm},$$

$$t(15\ \mathrm{mm}) = \frac{2(0.015)}{0.141324} = 0.2123\ \mathrm{ns}.$$

**The $15\ \mathrm{mm}$ layer cannot be measured as two echoes.** Its thickness is
$64\%$ of $\lambda/4$, and its two-way time ($0.212\ \mathrm{ns}$) is below the
$\lambda/4$ two-way time ($2 \times 23.55/141.324 = 0.333\ \mathrm{ns}$). The
demonstration's table agrees: at $15\ \mathrm{mm}$ the response is a single
composite wavelet of p2p $0.3314$ (wet base) or $0.4362$ (dry base) rather than two
resolvable events. It is still *detectable* — the wavelet is measurably different
from a thick layer's — but its thickness is a model inversion, not a pick.

---

## ★3 — The layer multiple

$$\tau = \frac{2h}{v} = \frac{2(0.050)}{0.141324} = 0.7076\ \mathrm{ns},$$

$$\tau_m = 2\tau = 1.4152\ \mathrm{ns},$$

apparent depth if read as a primary:

$$h_{\mathrm{app}} = \frac{v\tau_m}{2} = \frac{0.141324 \times 1.4152}{2}
= 0.10000\ \mathrm{m} = 100.0\ \mathrm{mm}.$$

The multiple appears exactly where a $100\ \mathrm{mm}$ layer would be — twice the
true thickness, as the algebra requires. It is separated from a real interface by
its moveout (a multiple of a shallow layer has more moveout, having spent more time
in the slow layer) and by its behaviour: it vanishes if the surface reflection is
suppressed with a coupling mat.

---

## ★4 — What interference amplitude would be mis-read as

Applying the plate inversion to the p2p values of Section 3.3:

$$h = 20\ \mathrm{mm},\ \mathrm{wet\ base}:\quad
\varepsilon_r = \left(\frac{1+0.3165}{1-0.3165}\right)^{2}
= \left(\frac{1.3165}{0.6835}\right)^{2} = 1.92611^{2} = 3.710,$$

$$h = 20\ \mathrm{mm},\ \mathrm{dry\ base}:\quad
\varepsilon_r = \left(\frac{1+0.4441}{1-0.4441}\right)^{2}
= \left(\frac{1.4441}{0.5559}\right)^{2} = 2.59768^{2} = 6.748.$$

Against the true $4.5$:

| base | computed $R_{\mathrm{eff}}$ | inferred $\varepsilon_r$ | error |
|---|---|---|---|
| wet | $0.3165$ | $3.71$ | $-17.6\%$ |
| dry | $0.4441$ | $6.75$ | $+50.0\%$ |

**Both are warning signs, of different severity.** The wet-base case
($-18\%$) looks like a calibration error — the kind of disagreement an experienced
analyst checks against the plate reading. The dry-base case ($+50\%$) looks like a
*different material*, which is exactly the error a report would carry silently:
the analyst would report a permittivity of $6.75$ and a thickness $18\%$ too small,
with no inconsistency visible in the data.

---

## ★5 — Decomposing the cover-depth uncertainty

$$\sigma_c(\text{picking}) = \frac{v\sigma_t}{2} = \frac{0.1224 \times 0.02}{2}
= 1.224\ \mathrm{mm},$$

$$\sigma_c(\text{velocity}) = c\,\frac{\sigma_v}{v} = 60.0 \times 0.009
= 0.54\ \mathrm{mm}.$$

$$\text{quadrature sum} = \sqrt{1.224^{2} + 0.54^{2}} = \sqrt{1.498 + 0.292}
= 1.337\ \mathrm{mm}.$$

| term | $\sigma_c$ | share of variance |
|---|---|---|
| picking ($0.02\ \mathrm{ns}$) | $1.22\ \mathrm{mm}$ | $83.8\%$ |
| velocity ($0.9\%$) | $0.54\ \mathrm{mm}$ | $16.2\%$ |

The **picking term is larger**, by a factor of $2.26$. The Monte Carlo's
$1.5\ \mathrm{mm}$ exceeds the quadrature sum of $1.337\ \mathrm{mm}$ because the
fitted velocity and the fitted cover depth are correlated (the previous lesson's
result: $\rho \to +1$ for a single hyperbola), so the two errors add rather than
combine in quadrature. This is the opposite ranking to the deep-glacier case of
the previous module, and for a contained reason: shallow cover means a short
two-way time, so the same absolute pick error is a much larger fraction of it.

**Consequence for practice:** for cover surveys, averaging many traces along the
bar (or averaging several bars) reduces the picking term as $1/\sqrt N$ and is
worth more than a better velocity model.

---

## ★6 — A wet deck, read with a dry permittivity

Wet layer: $\varepsilon_r = 8.0$,

$$v_{\mathrm{wet}} = \frac{0.299792458}{\sqrt{8.0}} = 0.105995\
\mathrm{m\,ns^{-1}},$$

$$t_{\mathrm{apex}} = \frac{2(0.060)}{0.105995} = 1.1322\ \mathrm{ns}.$$

Read with the dry permittivity $\varepsilon_r = 6.0$,
$v_{\mathrm{dry}} = 0.122379\ \mathrm{m\,ns^{-1}}$:

$$c_{\mathrm{reported}} = \frac{0.122379 \times 1.1322}{2} = 0.069291\ \mathrm{m}
= 69.3\ \mathrm{mm}.$$

$$\text{error} = 69.3 - 60.0 = +9.3\ \mathrm{mm} \quad (+15.5\%).$$

**The error is always an over-estimate of cover when a wet layer is read with a
dry permittivity**, because the same physical cover takes *longer* in a slower
(wet) medium, while the conversion velocity is too fast. The size follows the
square-root rule exactly:
$\sqrt{8/6} - 1 = 15.47\%$.

In a practical survey this is also a self-consistency test: the *amplitude* of the
bar reflection changes when the surrounding concrete wets (a lower contrast against
a higher-permittivity host), so a sudden change in the reported cover that is
accompanied by a change in bar amplitude is moisture, not geometry.

---

## ★7 — Certifying a $50\ \mathrm{mm}$ layer to $\pm3\ \mathrm{mm}$

**Required relative accuracy:** $3/50 = 6\%$ in thickness.

**Permittivity term.** $\mathrm{d}h/h = -\frac{1}{2}\mathrm{d}\varepsilon_r/\varepsilon_r$,
so $\pm6\%$ in thickness needs $\pm12\%$ in permittivity. From
$\mathrm{d}\varepsilon_r/\varepsilon_r = 4\mathrm{d}R/(1-R^2)$ with
$R = -0.3592$:

$$\mathrm{d}R = \frac{0.12 \times 0.8710}{4} = 0.0261.$$

So the plate-referenced surface amplitude must be read to about $\pm0.026$ in
$R$, i.e. to $2.6\%$ of the plate amplitude. That is undemanding: the plate and
surface reflections are the two strongest events on the trace, and a $2\%$
amplitude read is routine.

**Timing term.** The two-way time is $t = 2(0.050)/0.141324 = 0.7076\ \mathrm{ns}$,
and $\pm3\ \mathrm{mm}$ corresponds to

$$\mathrm{d}t = \frac{2\,\mathrm{d}h}{v} = \frac{2(0.003)}{0.141324}
= 0.0425\ \mathrm{ns} = 42.5\ \mathrm{ps}.$$

The pick must be good to $\pm42\ \mathrm{ps}$ on a $1.4\ \mathrm{ns}$-period
wavelet, i.e. about $3\%$ of a period. That is achievable with high SNR and a
repeatable wavelet, but it is the tightest term in the budget and it is a
*systematic* risk: a wavelet that changes shape between the calibration and the
survey shifts the baseline of the pick.

**Model term — the tack coat.** A $5\ \mathrm{mm}$ tack coat of
$\varepsilon_r = 6$ beneath $50\ \mathrm{mm}$ of $\varepsilon_r = 4.5$ asphalt adds
an extra two-way time

$$\Delta t = 2(0.005)\left(\frac{1}{0.1224} - \frac{1}{0.141324}\right)
= 0.01\,(8.169 - 7.076) = 0.0109\ \mathrm{ns},$$

i.e. $0.0109/0.014146 = 0.77\ \mathrm{mm}$ of apparent extra thickness — where
$0.014146\ \mathrm{ns\,mm^{-1}} = 2/v$ converts time to thickness. A tack coat is
therefore a $0.8\ \mathrm{mm}$ bias, inside the tolerance, and if it is unknown it
is a *bias* rather than a scatter, i.e. it does not average out.

**Which term sets the specification?** The **timing term** ($42.5\ \mathrm{ps}$),
followed by the model bias ($0.8\ \mathrm{mm}$), with the calibration term a
distant third ($2.6\%$ amplitude). The practical consequence is that the survey
should maximise SNR and pick consistency rather than chase calibration precision:
stack several traces along the line (the paving thickness that matters is an
average over metres, not at one point), and report the mean with its standard
error. Averaging $N = 25$ traces reduces the random picking term by a factor of
five to $0.85\ \mathrm{mm}$ and leaves the tack-coat bias untouched.

**Frequency.** Use the highest centre frequency whose attenuation still delivers
the base reflection with margin. For $50\ \mathrm{mm}$ at
$0.141\ \mathrm{m\,ns^{-1}}$, $\lambda/4 = 23.6\ \mathrm{mm}$ at $1.5\ \mathrm{GHz}$
and $14.1\ \mathrm{mm}$ at $2.5\ \mathrm{GHz}$; both leave the layer well above
the resolution limit, so the choice is decided by loss, not by resolution —
and a wet surface raises the loss fast, which is why $1.5\ \mathrm{GHz}$ is the
safer standard choice and $2.5\ \mathrm{GHz}$ the one to use on a dry surface with
a shallow target.

---

## ★8 — Resolving the thin-layer ambiguity

The ambiguity exists because a slab thinner than $\lambda/4$ produces one wavelet,
and its p2p depends on $h$, on both interface coefficients and on the source
spectrum. Three procedures resolve it, in order of reliability:

**1. Make the layer resolvable.** Choose a frequency such that
$h > \lambda/4$, i.e. $\lambda < 4h$, i.e.

$$f > \frac{c}{4h\sqrt{\varepsilon_r}}.$$

For $h = 20\ \mathrm{mm}$ and $\varepsilon_r = 4.5$:

$$f > \frac{0.299792458}{4(0.020)\sqrt{4.5}} = \frac{0.299792458}{0.169588}
= 1.768\ \mathrm{GHz}.$$

So a $2\ \mathrm{GHz}$ antenna resolves a $20\ \mathrm{mm}$ layer into two echoes
*if* the base reflection is still detectable — the condition that is not
guaranteed, and the reason this is a trade rather than an answer. The working
range is $h \gtrsim 20\ \mathrm{mm}$ on a dry base, less on a contrasting one.

**2. Fit the full waveform with the exact slab response.** The forward model of
Section 3.3 has four parameters ($h$, $\varepsilon_r$, $r_{01}$, $r_{12}$), and a
waveform has many samples, so the fit can be over-determined — but only if the
source wavelet is known and the interface coefficients are constrained. The
practical statement of the ambiguity that remains: $h$ and $r_{12}$ trade, because
a thinner layer with a larger contrast mimics a thicker one with a smaller
contrast. The measurable that breaks this particular trade is the **spectral
shape**: the interference factor $e^{-i\phi}$ has a known frequency dependence, so
the position of the spectral notch (or the phase-versus-frequency slope) gives
$\phi = 2\omega h/v$ and hence $h$ independently of the contrast amplitude. This
requires the band to cover a significant fraction of the interference period,
$f_{\max}\tau \gtrsim 1$, i.e. $\tau \gtrsim 1/f_{\max}$: for a $1.5\ \mathrm{GHz}$
band, $\tau \gtrsim 0.67\ \mathrm{ns}$, which corresponds to
$h \gtrsim 47\ \mathrm{mm}$ at $0.1413\ \mathrm{m\,ns^{-1}}$. Note the resulting
gap: above $\sim47\ \mathrm{mm}$ the spectral method works, above
$\sim24\ \mathrm{mm}$ a $2\ \mathrm{GHz}$ pick works, and between them a direct
measurement is needed.

**3. Measure the missing parameter.** Core or drill one point and measure $h$;
that fixes $\varepsilon_r$ and the base contrast, after which the amplitude
becomes a calibration for the rest of the line. This is always available and is
always the cheapest way out of an ill-posed problem.

---

## ★9 — Detecting a change of coupling without a plate

**Why it matters.** The metal plate reference is a coupling measurement: it fixes
the system's response with the antenna on one particular surface. If the coupling
changes along the line (a rougher surface, a patch of sealant, a change of moisture
under the antenna), every amplitude-derived number changes with it, and the metal
plate at the start of the line does not know.

**Procedure.**

1. **Reference every trace to its own surface echo.** Divide the layer amplitude
   by the surface amplitude of the same trace before computing anything. Because
   both are multiplied by the same coupling factor, the ratio is
   coupling-independent; what it is *not* independent of is the surface
   permittivity, so this normalization must be paired with per-zone plate
   measurements. This is the same reference trick used for a glacier bed.
2. **A repeat line.** Walk a fixed $20\ \mathrm{m}$ line at the start and the end
   of each day (and after any equipment change). A coupling change appears as a
   common-mode amplitude change with **no** time shift; a real change of surface
   material appears as an amplitude change **with** a time shift (the surface
   reflection itself moves if the permittivity changed) or with a phase change.
   The presence or absence of a time shift is the discriminator.
3. **A drift monitor on the direct coupling.** With the antenna held stationary on
   a smooth reference patch and no target, the near-field coupling response is the
   largest event on the trace; logging its amplitude every 15 minutes detects
   drift in the electronics with no survey-traffic coupling change.

**What change is detectable?** Take the per-trace surface amplitude to have a
$3\%$ coefficient of variation from roughness and coupling (a stated
assumption; a real survey would measure it from the repeat line). The mean over a
$100$-trace window then has a standard error of
$3\%/\sqrt{100} = 0.3\%$. A long-wavelength coupling change of $1\%$ therefore
stands at $3.3\sigma$ against the noise of the mean, while a change of $0.5\%$ is
marginal at $1.7\sigma$. Since $1\%$ in coupling is $1\%$ in inferred permittivity
through the inversion — far less than the $12\%$ the thickness tolerance allows —
**the procedure detects the coupling changes that matter, with margin**, provided
the window is long enough that averaging is honest (i.e. the change is not itself
inside the window).
