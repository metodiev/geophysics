# Solutions — 15-02-01 Marine Seismic Reflection: Airguns, Streamers, Processing

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [01 Marine Seismic Reflection](../01-marine-seismic-reflection.md).

---

## ★1 — Impedances, $R$ and $T$

$$Z_1 = \rho_1 v_1 = 1900 \times 1600 = 3.040\times10^{6}\
\mathrm{kg\,m^{-2}\,s^{-1}},$$
$$Z_2 = \rho_2 v_2 = 2200 \times 2400 = 5.280\times10^{6}\
\mathrm{kg\,m^{-2}\,s^{-1}},$$

$$\text{contrast} = \frac{Z_2 - Z_1}{Z_2 + Z_1}
= \frac{5.280 - 3.040}{5.280 + 3.040}
= \frac{2.240}{8.320} = 0.2692,$$

$$R = +0.2692, \qquad T = 1 + R = 1.2692 .$$

**Polarity: positive**, so the second medium is *harder* than the first — the
reflection has the same sign as the incident pulse. Check: $1 + 0.2692 = 1.2692 = T$ ✔.
Note $T > 1$: the transmitted *pressure* amplitude exceeds the incident one at a
hard interface, which is a common source of confusion. Energy is conserved
because the transmitted wave also carries a smaller particle velocity.

---

## ★2 — A negative coefficient

$R = -0.18$ means the reflected pressure has the opposite sign to the incident
pulse, which happens when $Z_2 < Z_1$: **the interface is softer below than
above.** The transmitted coefficient is

$$T = 1 + R = 1 - 0.18 = 0.82,$$

so $82\,\%$ of the incident pressure amplitude continues downward and the
remaining $18\,\%$ returns with reversed polarity. The magnitude of the
impedance contrast is $|R| = 0.18$, i.e. a $Z_2/Z_1$ ratio of
$(1-0.18)/(1+0.18) = 0.695$, so the lower medium has about $70\,\%$ of the
impedance above it.

---

## ★3 — Dimensional analysis

$$\left[\frac{Z_2-Z_1}{Z_2+Z_1}\right]
= \frac{\mathrm{kg\,m^{-2}\,s^{-1}}}{\mathrm{kg\,m^{-2}\,s^{-1}}}
= 1 \ ✔,$$

$$[Z] = [\rho][v] = \mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-1}}
= \mathrm{kg\,m^{-2}\,s^{-1}} \ ✔ .$$

$Z$ is an acoustic impedance per unit area — sometimes called the *characteristic
impedance*. It is not a resistivity-like quantity despite the shared symbol; the
units make the difference unmistakable.

---

## ★★4 — Hyperbolic moveout

Place the midpoint at the origin with source and receiver at $\pm x/2$. The
reflected ray has two legs, each of length $\sqrt{h^{2} + (x/2)^{2}}$, so

$$t = \frac{2}{v}\sqrt{h^{2} + \frac{x^{2}}{4}}
= \sqrt{\frac{4h^{2}}{v^{2}} + \frac{x^{2}}{v^{2}}}
= \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}},
\qquad t_0 = \frac{2h}{v}. \ ✔$$

Numerically, with $t_0 = 1.5\ \mathrm{s}$, $x = 1200\ \mathrm{m}$,
$v = 2000\ \mathrm{m\,s^{-1}}$:

$$t = \sqrt{1.5^{2} + \left(\frac{1200}{2000}\right)^{2}}
= \sqrt{2.25 + 0.36} = \sqrt{2.61} = 1.6155\ \mathrm{s},$$

$$\text{moveout} = 1.6155 - 1.5 = 0.1155\ \mathrm{s} = 115.5\ \mathrm{ms}.$$

**115 ms of moveout against, typically, a 15–20 ms wavelet half-width.** Stacking
without NMO would not merely reduce the event; it would cancel it.

---

## ★★5 — Residual moveout for a 3 % velocity error

$$\Delta t_{\text{res}} = \frac{x^{2}}{2t_0}\left(\frac{1}{v_{\text{try}}^{2}}
- \frac{1}{v^{2}}\right), \qquad v_{\text{try}} = v(1+e), \quad e = 0.03.$$

Prefactor: $x^{2}/(2t_0) = 9.0\times10^{6}/2.0 = 4.5\times10^{6}\
\mathrm{m^{2}\,s^{-1}}$. Velocities: $v^{2} = 4.0\times10^{6}$,
$v_{\text{try}}^{2} = (2060)^{2} = 4.2436\times10^{6}$.

$$\frac{1}{v_{\text{try}}^{2}} - \frac{1}{v^{2}}
= \frac{1}{4.2436\times10^{6}} - \frac{1}{4.0\times10^{6}}
= (2.3565 - 2.5000)\times10^{-7} = -1.4350\times10^{-8},$$

$$\Delta t_{\text{res}} = 4.5\times10^{6} \times(-1.4350\times10^{-8})
= -6.458\times10^{-2}\ \mathrm{s} = -64.6\ \mathrm{ms}.$$

The half-width of a $30\ \mathrm{Hz}$ wavelet is
$1/(2 \times 30) = 16.7\ \mathrm{ms}$, so the residual is **3.9 half-widths**.
This matches the exact form evaluated in Section 5 of the lesson
($-43\ \mathrm{ms}$ for a $10\,\%$ error is the same formula with a larger $e$;
the prefactor differs here because $x = 3000\ \mathrm{m}$ and
$t_0 = 1.0\ \mathrm{s}$ rather than the demonstration's $1800\ \mathrm{m}$ and
$2.0\ \mathrm{s}$).

**Will the stack survive? No.** A residual of several half-widths destroys the
coherent sum: the demonstration measured a stacked amplitude of $0.30$ of the
correct value for a $5\,\%$ error at $1800\ \mathrm{m}$, and the geometry here has
a prefactor 2.5 times larger. An error of this size would have to be found and
fixed by velocity analysis.

---

## ★★6 — Normalising by the water-bottom amplitude

$$R_{\text{second}}/R_{\text{water}} = 0.1481/0.3908 = 0.3790, \qquad
R_{\text{third}}/R_{\text{water}} = 0.2169/0.3908 = 0.5550 .$$

Normalising by the water-bottom peak makes the reported amplitudes equal
$0.3790$ and $0.5550$ regardless of the absolute scale of the source, the
spreading and the receiver response.

**Relative amplitudes survive** because every factor that is common to all
events — source strength, geometric spreading within the window, receiver gain,
the normalisation itself — cancels in a ratio. **Absolute amplitudes do not**,
because to convert a ratio back into an $R$ you must know the value you divided
by, and the water-bottom $R$ depends on the sediment's density and velocity,
which are what you were trying to measure. This is the sense in which reflection
amplitudes are *relative by construction*: the reference is itself an unknown in
the interpretation.

---

## ★★7 — $\lambda/4$ in four cases

$$\Delta z = \frac{v}{4f}.$$

| case | $v$ (m s$^{-1}$) | $f$ (Hz) | $\lambda/4$ (m) |
|---|---|---|---|
| (a) water | 1500 | 30 | 12.5 |
| (b) sediment | 1800 | 30 | 15.0 |
| (c) sediment | 3000 | 30 | 25.0 |
| (d) same, after attenuation | 3000 | 12 | 62.5 |

**Which change costs more?** Going from (a) to (c) — doubling the velocity —
costs a factor 2. Going from (c) to (d) — halving the frequency through
attenuation — costs a factor 2.5. Frequency loss is the larger penalty per unit
change, and it compounds with the depth increase that caused it: in a real
section the resolution degrades along a diagonal in the
(depth, frequency) plane. Quoting a single resolution for a section is therefore
almost always wrong.

---

## ★★★8 — Resolving the thin-bed/thick-bed ambiguity

**The ambiguity.** The tuning curve of the lesson is non-monotonic: at
$v = 1800\ \mathrm{m\,s^{-1}}$ and $30\ \mathrm{Hz}$, a composite peak of $0.71$
times a single wavelet's peak occurs at a separation of $11\ \mathrm{ms}$
($9.9\ \mathrm{m}$) **and** a composite of $0.64$ occurs at $16\ \mathrm{ms}$
($14.4\ \mathrm{m}$). Amplitude alone cannot tell "$10\ \mathrm{m}$" from
"$14\ \mathrm{m}$", and the failure grows more severe deeper into the tuning
curve where a single amplitude maps onto two thicknesses.

**What to measure.** Two independent observables, each of which breaks the
degeneracy in a different way:

1. **Spectral character.** Below $\lambda/4$ the composite's spectrum is that of
   a single wavelet; above it, the interference produces *notches* in the
   spectrum at frequencies $f = v/(2d)$, $3v/(2d)$, … whose spacing is inversely
   proportional to the thickness. Measuring the notch spacing is a direct
   thickness estimate that does not rely on amplitude, and it works precisely
   where amplitude is ambiguous.
2. **Offset dependence (AVO).** Tuning changes with incidence angle, because the
   reflection coefficients and the two-way times inside the wedge differ with
   angle. The *gradient* of amplitude with offset therefore differs between a
   thin and a thick bed, even when the normal-incidence amplitudes coincide.

**The assumption the test relies on.** That the wavelet is known and stationary
over the interval — for spectral notches, that the wavelet's spectrum has no
notch of its own in the band of interest; for AVO, that the overburden's
transmission effects are accounted for. Both are assumptions about the
processing, not about the Earth.

**The failure mode that produces a confident wrong answer.** A time-variant or
offset-variant wavelet. If deconvolution has already removed energy at the
interference-notch frequencies (which is exactly what a predictive deconvolution
with a short gap does), the notches are gone and the spectral test returns the
wavelet's own spectral shape — a smooth, plausible, wrong answer. The remedy is
to run the test on data before that deconvolution, and to state the processing
order in the report.

---

## ★★★9 — Worst-case residual over an offset range

**Derivation.** With $v_{\text{try}} = v(1+e)$ and the exact residual

$$\Delta t_{\text{res}}(x) = \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}}
- \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}(1+e)^{2}}},$$

the residual grows monotonically with $x$ (the derivative with respect to $x$ is
positive for $e>0$), so the worst case is at the maximum offset $x_2$:

$$\Delta t_{\max} = \left|\Delta t_{\text{res}}(x_2)\right| .$$

For small $e$ and small $x/(vt_0)$, the first-order form used in the lesson
suffices:

$$\Delta t_{\max} \approx \frac{x_2^{2}}{2t_0v^{2}}\left|
\frac{1}{(1+e)^{2}} - 1\right| \approx \frac{x_2^{2}}{t_0v^{2}}|e| .$$

**Amplitude loss.** For a Gaussian wavelet of standard deviation $\sigma_t$ in
time, the stack of mis-aligned traces averages the wavelet over the residual
distribution, which reduces the peak by
$\exp(-\Delta t^{2}/(8\sigma_t^{2}))$ for a uniformly distributed residual in
$[0,\Delta t]$ (the variance of a uniform distribution is
$\Delta t^{2}/12$, and the loss factor for a time shift of variance
$\sigma_s^{2}$ is $\exp(-\sigma_s^{2}/(2\sigma_t^{2}))$). Requiring the loss to be
below $5\,\%$:

$$\frac{\Delta t_{\max}^{2}}{24\sigma_t^{2}} \lesssim 0.05
\;\Longrightarrow\;
\Delta t_{\max} \lesssim 1.10\,\sigma_t .$$

**The requirement on the velocity error.** Combining,

$$|e| \lesssim \frac{1.10\,\sigma_t\,t_0v^{2}}{x_2^{2}}
= 1.10\,\sigma_t\,\frac{t_0 v^{2}}{x_2^{2}} .$$

**Scaling.** The tolerance on $e$ grows linearly with two-way time $t_0$ and with
the *square* of the velocity, and falls as the square of the cable length. Three
practical consequences:

- **Doubling the cable length requires four times better velocities** for the same
  fractional stack loss. Long-cable surveys are velocity-analysis projects.
- **Deep events tolerate larger velocity errors**, which is why velocity analysis
  is usually run in windows of increasing length with time.
- Expressing the requirement in terms of the *time* residual
  ($\Delta t_{\max} \lesssim 1.1\sigma_t$) is better practice than expressing it in
  terms of $e$, because it is the residual that damages the stack, and $e$
  translates into a residual differently at every $t_0$ and every $x$.
