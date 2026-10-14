# Solutions — 23-04-03 Magnetotelluric Fieldwork: Sites, Remote Reference, Noise

> Read after attempting. Lesson:
> [03 MT Fieldwork](../03-mt-fieldwork.md). All values are **SYNTHETIC**.

---

## ★1 — Impedance and apparent resistivity

$$\omega \mu_0 = 2\pi f \mu_0 = 2\pi \times 2 \times 4\pi\times10^{-7}
= 1.57914\times10^{-5}\ \Omega\,\mathrm{s/m}.$$

$$|Z| = \sqrt{\omega\mu_0\rho} = \sqrt{1.57914\times10^{-5} \times 50}
= \sqrt{7.8957\times10^{-4}} = 0.028099\ \Omega.$$

Note the coincidence worth checking: $f\rho = 2 \times 50 = 100$ gives the same
$|Z|$ as $f = 1$ Hz with $\rho = 100\ \Omega\,\mathrm{m}$, because $|Z|$ depends on
the product $\omega\mu_0\rho$. Apparent resistivity from a measurement:

$$\rho_a = \frac{|Z|^{2}}{\omega\mu_0}
= \frac{0.05^{2}}{1.57914\times10^{-5}} = \frac{0.0025}{1.57914\times10^{-5}}
= 158.3\ \Omega\,\mathrm{m}.$$

Units: $|Z|$ in Ω, $\omega\mu_0$ in Ω·s/m (or Ω/m per (m/s)), and $\rho_a$ in Ω·m.
The phase would be needed as well: at a single frequency, $|Z|$ alone gives
$\rho_a$ but says nothing about whether the ground is layered, and it is the phase
that carries the depth information.

---

## ★2 — Coherence for 3 % from 50 estimates

$$\gamma = \frac{1}{\sqrt{1 + 2N\sigma^{2}}}
= \frac{1}{\sqrt{1 + 2 \times 50 \times 0.03^{2}}}
= \frac{1}{\sqrt{1.09}} = 0.95783 .$$

So a coherence of **0.958** is required. The relation used is
$\sigma_{|Z|}/|Z| \approx \sqrt{(1-\gamma^{2})/(2N\gamma^{2})}$, inverted. Note
that this assumes the estimates are independent and that $\gamma$ is the *true*
coherence; an estimated coherence raised by coherent noise would make the required
value look easier to reach than it is.

---

## ★★3 — The cost of falling coherence

$$N_{\text{rel}}(\gamma) = \frac{1-\gamma^{2}}{\gamma^{2}}, \qquad
\text{reference } N_{\text{rel}}(0.99) = 0.020304 .$$

At $\gamma = 0.97$:

$$N_{\text{rel}} = \frac{1 - 0.9409}{0.9409} = 0.062812
\;\Rightarrow\; \frac{0.062812}{0.020304} = 3.09 .$$

At $\gamma = 0.88$:

$$N_{\text{rel}} = \frac{1 - 0.7744}{0.7744} = 0.291323
\;\Rightarrow\; \frac{0.291323}{0.020304} = 14.35 .$$

So going from a coherence of 0.97 to 0.88 multiplies the required number of
independent estimates, and therefore the recording time, by

$$\frac{14.35}{3.09} = 4.64 .$$

**Practical reading.** Neither 0.97 nor 0.88 is a disaster in itself; the lesson is
that the cost is *non-linear* in coherence. Reducing the local noise (moving the
site, removing a nearby source) or removing it in processing (remote reference,
robust estimation) is worth more than extending the recording by an hour, and the
arithmetic above says how much more.

---

## ★★4 — Dipole length and SNR

$$V = E\,L = 1.0\times10^{-6}\ \mathrm{V/m} \times 150\ \mathrm{m}
= 1.5\times10^{-4}\ \mathrm{V} = 150\ \mathrm{\mu V}.$$

$$20\log_{10}\!\left(\frac{150}{5}\right) = 20\log_{10}(30) = 29.54\ \mathrm{dB}.$$

**Dipole for 40 dB:**

$$40 = 20\log_{10}\!\left(\frac{V}{5\ \mathrm{\mu V}}\right)
\;\Rightarrow\; V = 5 \times 10^{2} = 500\ \mathrm{\mu V}
\;\Rightarrow\; L = \frac{500\ \mathrm{\mu V}}{1.0\ \mathrm{\mu V/m}}
= 500\ \mathrm{m}.$$

So a 500 m dipole would be needed — a large site, and the reason that array MT
deployments accept lower SNR per site and rely on coherence and stacking across
stations, or that permanent installations bury long dipoles once. Note also that
the 40 dB figure is a *spectral* SNR; for the impedance estimate what matters is
coherence, which depends on both fields, so a marginal telluric SNR can still give
usable coherence where the magnetic field is quiet.

---

## ★★★5 — A site layout for a 1 s target in a resistive terrane

**Expected field and dipole length.** For a resistive terrane take
$\rho \approx 500\ \Omega\,\mathrm{m}$. At 1 s period ($f = 1$ Hz):

$$|Z| = \sqrt{2\pi \times 1 \times 4\pi\times10^{-7} \times 500}
= \sqrt{3.948\times10^{-3}} = 0.06283\ \Omega,$$

and with a 1 nT (7.958 × 10⁻⁴ A/m) magnetic signal the telluric field is

$$E = |Z| H = 0.06283 \times 7.958\times10^{-4} = 5.0\times10^{-5}\ \mathrm{V/m}
= 50\ \mathrm{mV/km}.$$

That is a healthy telluric signal. With a 5 µV noise floor and a target SNR of
30 dB, the required dipole is

$$L \ge \frac{5 \times 31.6\ \mathrm{\mu V}}{50\ \mathrm{\mu V/m}}
= 3.2\ \mathrm{m},$$

which is absurdly short — because the field here is 50× larger than the lesson's
1 mV/km example. The practical minimum is set by other considerations: the
electrode noise, the spatial averaging needed to sample the plane wave, and the
need for the dipole to be long compared with the electrode pits and the local
lateral inhomogeneity. **Choose 100 m dipoles**, which give a comfortable margin,
a manageable footprint (0.01 km²) and adequate averaging.

**Magnetic sensor placement.** Three sensors (Hx, Hy, Hz), levelled and oriented
with their azimuths measured against true north, placed at least 10–20 m from the
telluric electrodes and from the telluric cables, and preferably on their own small
pits. Verify with a test recording: measure with the dipoles connected and
disconnected, and compare the magnetic spectra — any difference indicates coupling
from the telluric circuit.

**Remote reference.** **Required**, at 5 km from a railway. The railway's traction
current is a coherent source with a strong 1 s-period-band component, and from the
lesson's table a coherence of 0.7 in the local noise produces a 96 % error in the
apparent resistivity. Site the remote reference **at least 30–50 km away, in a
direction that has no shared infrastructure**, and check that its own noise is low
(by processing it against a third site, or simply by looking at its spectra). A
remote reference that shares the railway's noise removes nothing.

**Recording time.** From the coherence relation, with
$N = (1-\gamma^{2})/(2\sigma^{2}\gamma^{2})$: for a 2 % target accuracy at a dead-band
coherence of 0.90,

$$N = \frac{1-0.81}{2 \times 0.0004 \times 0.81} = \frac{0.19}{6.48\times10^{-4}}
= 293 \text{ independent estimates}.$$

At 1 s period with, say, one independent estimate per 20 s of usable data in the
band, that is of order **1.6 hours of *good* data**, which with a 50 % duty cycle
and the coherence losses implies a **recording time of 1–2 days**. Budget two to
three days per site to allow for a poor first night, and record the site's spectra
daily so that the decision to stay longer is made from data rather than from hope.

**Checks before leaving the site.** (i) All four electrode resistances and the
telluric noise spectra recorded. (ii) Magnetic sensor orientations, levelling and
signal levels recorded. (iii) A test showing that the magnetic channels are
unaffected by the telluric circuit. (iv) The remote reference recording
synchronised and its clock checked against the local site's. (v) A first
processing pass at the site (or the next morning) showing coherence in the target
band above the level the accuracy target requires. Without (v) the crew cannot know
whether the site has produced data until after demobilisation.

---

## ★★★6 — Testing whether coherence has been raised by noise

**Measurements.**

1. The **local site's** E and H spectra and the estimated coherence between them.
2. The **remote reference's** H spectrum and its coherence with the local H.
3. A **quiet-period** repeat: the same processing applied to a subset of the record
   selected by an activity index or by a low-noise period identified from the local
   spectra.

**Comparison.** Compute the impedance in three ways: single-station (local E, local
H), remote-reference (local E, remote H), and remote-reference restricted to the
quiet subset. If they agree, the coherence is genuine signal coherence. If the
single-station impedance is systematically higher — particularly at the frequencies
where a local source operates (the railway's 1 s band, a power line's harmonics) —
then coherent noise has raised the apparent coherence and biased the impedance.

**Metric.** The ratio $\rho_a^{\text{single}}/\rho_a^{\text{remote}}$ as a function
of frequency (dimensionless; the expected bias is $1/(1-\gamma_n^{2})$ in
resistivity, so 1.25 for $\gamma_n = 0.6$ and 5.26 for $\gamma_n = 0.9$), together
with the **coherence between the local H and the remote H**: a high local–remote
coherence means the noise is present at both sites, and therefore that the remote
reference cannot remove it.

**What the test cannot detect.**

1. **Noise coherent between the local E and H that is also present at the remote
   site.** The remote reference removes it as if it were signal, and both the
   single-station and the remote-reference impedances are biased in the same
   direction. Detecting this requires a *third* site, or an independent
   measurement of the source's field, or simply knowing that the source exists.
2. **A genuine galvanic distortion or static shift** caused by a shallow
   inhomogeneity at the site. This is not noise, it is a real (if unwanted)
   response of the ground, and no reference site can remove it — it is handled by
   the interpretation, not the acquisition.
