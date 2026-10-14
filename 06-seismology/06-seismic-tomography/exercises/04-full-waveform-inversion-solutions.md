# Solutions — 06-06-04 Full-Waveform Inversion: Objective Functions and Reliability

Exercises:
[04-full-waveform-inversion-exercises.md](04-full-waveform-inversion-exercises.md).

## ★ Foundational

**1.** $\Delta t = 0.8\times10\ \mathrm{m}/3200\ \mathrm{m\,s^{-1}} =
2.50\times10^{-3}\ \mathrm{s} = \mathbf{2.5\ ms}$, matching the reported value.
The check is the CFL condition $c\,\Delta t/\Delta x \le 1$, which gives
$0.80$ here; the demonstration measures the blow-up at 1.02.

**2.** $1.2/20 = \mathbf{60\ ms}$. Adding it to the predicted two-way time gives
$1.000 + 0.060 = 1.060$ s against a picked 1.105 s; the remaining 45 ms is the
finite offset of the source and receiver (20 m below the free surface) and the
shape of the reflected wavelet. This is why the demonstration verifies the
*separation* of two arrivals (0.775 s against 0.769 s) rather than a single pick.

**3.** $\lambda = c/f = 2600/20 = \mathbf{130\ m}$, i.e. $130/10 = \mathbf{13}$
grid points per wavelength at the dominant frequency — comfortably resolved;
the 32 Hz band in the landscape experiment has only 8 points per wavelength at
the same velocity.

## ★★ Applied

**4.** The measured first secondary minima are at $\alpha = 0.130$, $0.068$,
$0.028$, i.e. arrival shifts of 115.0, 63.2 and 26.8 ms, against $1/f_c$ of 125,
62.5 and 31.2 ms. So the spacing tracks **one period**, not half a period; the
basin half-width (the distance to the first secondary minimum) is 115, 63 and
27 ms. Both statements are the same measurement: the misfit between a wavelet and
its shifted copy has minima at multiples of one period.

**5.** 48 ms is inside the 8 Hz basin (115 ms) and outside the 16 Hz (63 ms) and
32 Hz (27 ms) basins. Prediction: the 8 Hz descent reaches the truth; the 16 and
32 Hz descents do not. The demonstration confirms: 32 Hz from $+0.050$ ends at
$+0.0475$ (45.3 ms error), 16 Hz at $+0.0675$ (63.2 ms), while 8 → 16 → 32 Hz
ends at $0.0000$ with zero misfit.

**6.** The three denominators are (i) the misfit that pure noise of rms
$\sigma$ would give over the *whole record* in the full band,
$0.5\,N_{\text{rec}}\sigma^2$; (ii) the same over the *window*
$0.5\,N_{\text{win}}\sigma^2$; (iii) the same over the window but for the
*band-limited* noise, $0.5\,N_{\text{win}}(\beta\sigma)^2$ with $\beta = 0.26$
for a 16 Hz low-pass. Only (iii) is a meaningful test of whether the inversion
has fitted noise, so that is the one a paper must state, together with the
window and the band.

## ★★★ Research-oriented

**7.** Mechanism: with the two-way time and the reflection coefficient fixed,
the *impedances* differ ($Z = \rho c$ with $c_1$ from 1400 to 2600 m/s), so the
transmitted and reflected amplitudes differ even though the timing and the
coefficient do not; the waveform therefore carries the depth, but only through
amplitude. Test: multiply each synthetic trace by an independent random factor
uniform in $[0.9, 1.1]$ (a stand-in for source coupling and attenuation), rerun
the five family members and compare residuals. If the family members become
indistinguishable at the noise level, the depth information was carried entirely
by absolute amplitude and is not available in real data without a calibration;
that is the argument for joint inversion with a data type whose amplitudes are
understood.

**8.** Schedule: start at 8 Hz (basin 115 ms) and stay there until the misfit
stops decreasing; advance when the *current model's* predicted arrival-time
mismatch, measured on the band being proposed, is smaller than that band's basin
half-width. Concretely: 8 Hz until the 16 Hz mismatch is below 63 ms, then
16 Hz until the 32 Hz mismatch is below 27 ms, then 32 Hz (and beyond if the
data have energy). With a 0.4 s initial error the first stage must be *below*
8 Hz — 4 Hz gives roughly a 230 ms basin by the same scaling, still too small —
so the schedule requires an even lower starting band, or a better starting
model, and either of those is the honest answer to "why does FWI not work with a
1-D starting model here".
