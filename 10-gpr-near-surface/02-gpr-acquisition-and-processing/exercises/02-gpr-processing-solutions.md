# Solutions — 10-02-02 Processing Steps

> Read after attempting. Lesson: [02 Processing Steps](../02-gpr-processing.md).

---

## ★1 — Amplitude bias from a drift

The drift adds a slowly varying offset of order $\pm0.075$ (half the
peak-to-peak amplitude) to a reflection whose peak amplitude is $0.40$:

$$\text{fractional bias} \approx \frac{0.075}{0.40} = 19\%,$$

**positive** (the reflection reads too large), because the drift is added rather
than multiplied. In the demonstration the same mechanism moved an amplitude ratio
from $0.5488$ to $0.7071$, $+28.8\%$, with a drift of peak-to-peak $0.25$ against
a first reflection of $1.00$ and a second of $0.5488$.

---

## ★2 — Constant gain versus AGC

A constant gain multiplies by a function of time that is known in closed form
(and therefore reversible); AGC multiplies by a *data-dependent* factor that
equalises local signal strength. AGC destroys the **ratio of two reflection
amplitudes**, which is the measurement that reflection-coefficient and
attenuation work depends on.

---

## ★3 — Resolution cost of the filter

Pulse width grows from $2.0$ to $3.0\ \mathrm{ns}$, i.e. by $1.0\ \mathrm{ns}$;
in depth that is $(v/2)\Delta t = (0.075/2)\times1.0 = 0.0375\ \mathrm{m} =
3.75\ \mathrm{cm}$. The resolution degrades from $7.5$ to $11.25\ \mathrm{cm}$.

---

## ★★4 — Dipping reflector

Time dip: $2\sin25^\circ/v = 2\times0.42262/0.09993 = 8.459\
\mathrm{ns\,m^{-1}}$.

Apparent dip: $\arctan(\sin25^\circ) = \arctan(0.42262) = 22.90^\circ$.

Imaged dip with $v_{\text{mig}} = 0.95v$:
$\sin\theta_{\text{mig}} = 0.95\times0.42262 = 0.40149$, so
$\theta_{\text{mig}} = 23.68^\circ$ (the true dip being $25.00^\circ$).

---

## ★★5 — A $5\ \mathrm{cm}$ depth discrepancy

Two plausible causes: (i) the velocity used for migration/depth conversion is a
few per cent too high — $0.05/1.80 = 2.8\%$ of the depth; (ii) the migration's
depth grid or the reflector's peak-picking on a dipping event biases the pick
(the demonstration's correct-velocity migration of a $20^\circ$ interface at
$2.00\ \mathrm{m}$ returned $2.100\ \mathrm{m}$, a $10\ \mathrm{cm}$ bias, with
the *correct* velocity).

Distinguishing them: migrate with a velocity deliberately varied by $\pm5\%$ and
see whether the depth moves as the depth-conversion ratio predicts
($\propto v$); if it does not, the residual is a picking/grid artefact. An
independent check is to predict a time from the migrated position — a velocity
error changes the *time* by the same percentage, while a grid artefact does not.

---

## ★★6 — Background removal

Target-to-clutter improves from 18 to 26 dB ($+8\ \mathrm{dB}$), while the target
peak falls by $20\log_{10}(0.45/0.90) = -6.02\ \mathrm{dB}$. Since the clutter
falls and the target falls, the clutter reduction is
$8 + 6.0 = 14.0\ \mathrm{dB}$ — i.e. the filter attenuated the clutter by
$14\ \mathrm{dB}$ while attenuating the target by $6\ \mathrm{dB}$.

A flat-lying target that is laterally continuous over the filter's window has
exactly the property the filter removes: it would be suppressed by roughly the
$14\ \mathrm{dB}$ of the clutter, not by $6\ \mathrm{dB}$. That is the cost of the
method and must be declared in the processing report.

---

## ★★★7 — Sequence for a $400\ \mathrm{MHz}$ noisy grid

The justified order:

1. **Dewow** (before any amplitude use; the drift biases ratios by tens of per
   cent).
2. **Time zero** from the air wave, per line (before any depth conversion).
3. **Band-pass** (before migration and before amplitude analysis, because the
   filter changes the spectrum being measured; for the two-day comparison, a
   *common* filter and its documentation are essential).
4. **Deterministic gain**, with the gain function recorded, so the two days can be
   compared in true amplitude; AGC is applied **only for display** and must not
   enter the comparison.
5. **Background removal** (before migration: the ringing would otherwise be
   smeared along migration operators; declared, because it attenuates flat-lying
   real reflectors).
6. **Migration** with the velocity from the CMP sounding.

For the two-day comparison, the steps that must be identical and documented are
the filter, the gain and the background-removal window; and any step that is
*data-dependent* (gain, background removal) is a candidate for the observed
$6\ \mathrm{dB}$ difference, which must therefore be attributed before
interpretation.

---

## ★★★8 — Making a $40^\circ$ interface look vertical

Vertical means $\theta_{\text{mig}} = 90^\circ$, so
$\sin\theta_{\text{mig}} = 1 = (v_{\text{mig}}/v)\sin40^\circ$, hence
$v_{\text{mig}}/v = 1/0.6428 = 1.556$: a velocity $56\%$ too high.

In practice this never happens for two reasons. First, an error that large would
be obvious in the near-offset moveout, which would be grossly misfit. Second, the
migration aperture limits the dip that can be imaged at all: as the
[10-01-05](../../01-gpr-principles/05-gpr-resolution.md) measurement shows, a
$\pm2\ \mathrm{m}$ aperture at $1\ \mathrm{m}$ depth already smears the image, and
a near-vertical event is at the aperture's edge, so it is attenuated rather than
rotated. Large apparent dips in a migrated section are usually aperture and noise
artefacts, not velocity errors.
