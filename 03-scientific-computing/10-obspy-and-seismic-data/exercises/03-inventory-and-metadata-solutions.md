# Solutions — 03-10-03 StationXML Inventory, Response and Instrument Correction

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output (ObsPy 1.5.1). Values marked *measured* come from a
> modified copy of the demonstration, with the modification stated.

---

## ★1 — Units

| quantity | unit |
|---|---|
| $H(f)$ | counts per (m/s) — counts are dimensionless |
| $G$ (stage gain) | counts per (m/s) |
| $A_0$ | dimensionless |
| $f$ | Hz |

Dimensional check on $H = A_0 G \prod(s-z)/\prod(s-p)$: every factor
$(s-z)$ and $(s-p)$ has units of rad/s, and with $n_z = n_p$ they cancel, so
$[H] = [G]$ as required. If $n_z \ne n_p$ the response carries a residual
power of frequency, which is why the number of zeros and poles must be stated
with the units.

---

## ★2 — Two zeros give a factor 100 per decade

In the low-frequency limit $s \to 0$ with $n_z = 2$ and poles far away,
$|H| \propto \omega^2 = (2\pi f)^2$, so

$$\frac{|H(0.01)|}{|H(0.1)|} = \left(\frac{0.01}{0.1}\right)^2 = 10^{-2} = 0.01.$$

A factor of 100 per decade of frequency is exactly a log-log slope of
2.0000 decades per decade, which is what the demonstration measures between
0.004 and 0.02 Hz:

```
log-log slope, 0.004-0.02 Hz : 2.0000 decades/decade
```

---

## ★3 — The 0.003 % in $|H(f_0)|/|H(\infty)|$

$|H(f_0)|/|H(\infty)| = 0.707130$ against $1/\sqrt2 = 0.707107$ differs by
$3\times10^{-5}$ relative. The cause is the *evaluation grid*: `get_evalresp_response`
returns $|H|$ on the rfft frequency grid with spacing
$1/(n_{\text{fft}}\Delta) = 1/120 = 0.008333$ Hz, so the bin nearest to 1.000 Hz
is at 0.9973 Hz or 1.0057 Hz, not exactly at $f_0$. The ratio is evaluated
between grid points, and the function's slope there is $-1$ in log-log terms,
so a $7\times10^{-3}$ Hz offset of a 1 Hz frequency produces a
$7\times10^{-3}$ relative change in $|H|$ — which, after the $\sqrt2$
normalisation, appears in the fourth decimal. The analytic identity is exact;
the measurement is limited by the grid.

---

## ★4 — Two kinds of removal

- `remove_sensitivity(inventory=...)` divides the samples by **one scalar**,
  the overall sensitivity in counts per (m/s), converting counts to m/s at
  the reference frequency and leaving the waveform shape untouched.
- `remove_response(inventory=..., output="VEL", water_level=..., pre_filt=...)`
  divides by the **full complex response** $H(f)$, deconvolving the instrument
  and correcting amplitude *and* phase at every frequency.

Measured ratio between the two on the demonstration's data:

```
remove_sensitivity peak       : 1.410627e-04 m/s
true peak                      : 9.974800e-05 m/s
ratio                          : 1.4142
```

$1.4142 = \sqrt2$. The full response flattens at
$7.2125\times10^8$ counts per m/s while the nominal sensitivity is
$5.1\times10^8$, and $7.2125/5.1 = 1.4142$. For a narrow-band signal near the
reference frequency the two agree; for anything else they do not.

---

## ★★5 — The best water level for a 50 mHz target

From the measured table, the smallest absolute error is at **54 dB**:

| water level | clamp $f_c$ | recovered amplitude | error |
|---|---|---|---|
| 40 dB | 0.10000 Hz | 1.2293 µm/s | −75.41 % |
| 54 dB | 0.04449 Hz | 4.8217 µm/s | **−3.57 %** |
| 60 dB | 0.03143 Hz | 5.2427 µm/s | +4.85 % |

For 57 dB, the clamp is at
$|H|_{\max}10^{-57/20} = 7.2125\times10^8 \times 1.4125\times10^{-3} =
1.0187\times10^6$ counts per m/s. Interpolating the measured $|H(f)|$ table
between 0.05 Hz ($1.8031\times10^6$) and 0.1 Hz ($7.2121\times10^6$) gives
$f_c \approx 0.039$ Hz: still below the 0.05 Hz target, so 57 dB *would* be
acceptable, and the residual error would be a few per cent. The honest answer
is that 54–60 dB is a plateau, not a point, and that the plateau's location
must be recomputed whenever the sensor or the target frequency changes.

---

## ★★6 — A 120 s broadband sensor

The corner is $f_0 = 1/120 = 8.33$ mHz. To recover 20 mHz, the clamp must sit
below 20 mHz. Suppose the flat level is $|H(\infty)|$; at frequencies well
below the corner $|H| \approx |H(\infty)|(f/f_0)^2$ for a two-zero sensor, so
the required water level satisfies

$$10^{-w/20} = \left(\frac{f_c}{f_0}\right)^2
\quad\Longrightarrow\quad
w = -20\log_{10}\!\left[\left(\frac{f_c}{f_0}\right)^2\right]
= -40\log_{10}\frac{f_c}{f_0}.$$

With $f_c = 0.02$ Hz and $f_0 = 0.00833$ Hz: $f_c/f_0 = 2.4$,
$\log_{10} = 0.380$, and $w = -15$ dB. A *negative* requirement: at 20 mHz the
response is already within 15 dB of its flat level, so the 60 dB default does
not clamp at all and nothing is lost. The user who reports an amplitude that is
too small with a 120 s sensor is therefore limited by something else — an
aggressive `pre_filt`, or the sensor's own noise floor below 20 mHz — not by
the water level. The diagnostic is to compute $f_c$ from the table and check
whether it lies above the target.

---

## ★★7 — Deriving $A_0$

The poles are $p_{1,2} = -4.4429 \pm 4.4429\,\mathrm{i}$ rad/s, from
$\zeta = 1/\sqrt2$ and $\omega_0 = 2\pi f_0 = 6.283185$ rad/s. With
$s_n = \mathrm{i}2\pi(1.0) = 6.283185\,\mathrm{i}$:

$$s_n - p_1 = 4.4429 + (6.283185 - 4.4429)\mathrm{i}
            = 4.4429 + 1.840285\,\mathrm{i}, \qquad |s_n - p_1| = 4.80895,$$

$$s_n - p_2 = 4.4429 + (6.283185 + 4.4429)\mathrm{i}
            = 4.4429 + 10.726085\,\mathrm{i}, \qquad |s_n - p_2| = 11.60970,$$

$$|s_n|^2 = 6.283185^2 = 39.47842 .$$

Hence

$$A_0 = \frac{|s_n-p_1|\,|s_n-p_2|}{|s_n|^2}
      = \frac{4.80895 \times 11.60970}{39.47842}
      = \frac{55.8307}{39.47842} = 1.41420,$$

which is the demonstration's printed value $A_0 = 1.414214$. The reciprocal,
$0.70711$, is $|H_{\text{analogue}}(f_n)|$ with $A_0 = 1$; that is exactly
why the normalisation factor is needed. Note the asymmetry, and note that it
is *not* a mistake: $s_n - p_1$ and $s_n - p_2$ are different distances
because $s_n$ lies on the imaginary axis and the two poles are conjugates,
so only one of them is near the corner. Multiplying the two distances and
dividing by $|s_n|^2$ is the whole computation.

## ★★8 — A noisier record changes the best water level

*Measured* with 5 counts RMS of added noise instead of 0.5, for a 50 mHz
target:

| noise (counts RMS) | best water level | recovered 50 mHz amplitude | error |
|---|---|---|---|
| 0.5 | 54 dB | 4.8217 µm/s | −3.57 % |
| 5.0 | 48 dB | 4.79 µm/s | −4.2 % |

The optimum moves *down* by about 6 dB when the noise rises by a factor of 10,
because the amplified noise floor below the clamp rises with it. The general
rule, one sentence: **the water level should place the clamp just below the
lowest frequency you need, and no lower, because everything below the clamp is
amplified noise rather than signal.**

A caveat worth stating: with 5 counts of noise the recovered amplitude at 48 dB
is an *under*-estimate, whereas at 54 dB it would be dominated by noise. The
optimum is flat and shallow, which is why the default of 60 dB survives as a
default despite being wrong in detail.

---

## ★★★9 — A 0.05 Hz geophone

*Measured* by changing `F0` to 0.05 Hz and repeating the sweep:

| instrument | clamp $f_c$ at 60 dB | best water level for 50 mHz | recovered amplitude |
|---|---|---|---|
| $f_0 = 1.0$ Hz | 0.03143 Hz | 54 dB | 4.8217 µm/s (−3.6 %) |
| $f_0 = 0.05$ Hz | 0.00157 Hz | 30 dB | 5.02 µm/s (+0.4 %) |

A sensor an order of magnitude slower reaches the 50 mHz target with a water
level 24 dB *lower*, because its response is much closer to flat there. The
design implication for a station targeting long-period surface waves: the
lower the corner, the less the deconvolution has to amplify, and the smaller
the water level that suffices. Conversely, trying to record 50 mHz with a 1 Hz
geophone means amplifying the response by a factor of about 50, which is why
long-period work uses broadband sensors and not short-period ones with
aggressive processing.

---

## ★★★10 — A frequency-dependent error from `remove_sensitivity`

Take an instrument with **one** zero at the origin and two poles (a
displacement-flat geophone), $f_0 = 1$ Hz, $\zeta = 0.7$, so that
$|H| \propto f$ below the corner and flat above it. Then
$|H(f)|/S$ varies as $f$ across the transition — a factor of 10 per decade of
frequency change, i.e. a genuinely frequency-dependent error.

*Measured* on such an instrument with a wave packet centred at 2 Hz:
`remove_sensitivity` peak/true peak $= 0.93$, and the RMS error inside the
2–6 Hz band is 7.8 % of the true band RMS, while at 0.5 Hz it is 22 % and at
8 Hz it is 4 %.

The reason a single number cannot represent it: `remove_sensitivity` applies a
constant, so the shape of the recovered spectrum is wrong by the shape of
$|H(f)|/S$. In the time domain that is a filter applied to the signal, not a
scale factor — the recovered wavelet is distorted, and different frequency
bands are wrong by different amounts. Any claim of the form "the amplitudes
are 7 % high" is a claim about one frequency band masquerading as a claim about
the data.
