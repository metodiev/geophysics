# Exercises — 11-02-05 Radiometrics and Alteration Mapping

Attempt these before reading the
[solutions](./05-radiometrics-for-minerals-solutions.md). The lesson is
[05 Radiometrics and Alteration Mapping](../05-radiometrics-for-minerals.md). All
concentrations, sensitivities, stripping ratios and counting times are
**SYNTHETIC**; the air density and the air mass attenuation coefficients are
standard constants as stated in the lesson.

Useful: $E_2(z) = \int_1^\infty e^{-zt}t^{-2}\,\mathrm{d}t$,
$\rho_{\text{air}} = 1.225\times10^{-3}\ \mathrm{g\,cm^{-3}}$,
$\mu_K = 6.49\times10^{-3}\ \mathrm{m^{-1}}$,
$\mu_{\text{Th}} = 4.41\times10^{-3}\ \mathrm{m^{-1}}$,
$\mathrm{HVL} = \ln 2/\mu$.

## ★ Foundational

**★1.** Soil of density $1.9\ \mathrm{g\,cm^{-3}}$ has
$\mu/\rho = 0.06\ \mathrm{cm^{2}\,g^{-1}}$. Compute its linear attenuation
coefficient, its half-value layer, and the fraction of the flux from bedrock that
escapes through $25\ \mathrm{cm}$ of it.

**★2.** Compute $E_2(\mu h)$ for the K window at $h = 0$, $50$, $100$ and
$200\ \mathrm{m}$, and state the count rate at $100\ \mathrm{m}$ as a fraction of
the ground-level rate.

**★3.** For the demonstration's stripping matrix and sensitivities, compute the
window count rates for a rock with $K = 3.0\%$, $eU = 4.0$ ppm, $eTh = 8.0$ ppm,
then invert and verify that the concentrations are recovered.

**★4.** A K window records $250\ \mathrm{counts\,s^{-1}}$. Compute the relative
uncertainty after $30$, $300$ and $3000\ \mathrm{s}$ and state the ratio of the
$30\ \mathrm{s}$ to the $3000\ \mathrm{s}$ uncertainty.

## ★★ Applied

**★★5.** A SYNTHETIC area has a ground Th/K of $4.30$. Compute the Th/K you would
measure at $80\ \mathrm{m}$ and at $160\ \mathrm{m}$ flying height, and the
percentage difference between them. State what this implies for a draped survey
over $80\ \mathrm{m}$ of relief.

**★★6.** An altered zone has K = $4.2\%$, eU = $2.4$ ppm, eTh = $7.0$ ppm against
a host of K = $2.0\%$, eU = $1.8$ ppm, eTh = $9.0$ ppm. Compute Th/K and
K/(K+U+Th) for both, the fractional change in each, and decide which diagnostic is
the better discriminator. Then compute the counting uncertainty in each ratio at
$120\ \mathrm{s}$ integration using the count rates from the demonstration's
sensitivities, and state whether the discrimination is counting-noise limited.

**★★7.** A spectrometer's stripping matrix is
$\mathbf{S} = \begin{pmatrix}1&0.4&0.2\\0.1&1&0.4\\0&0.05&1\end{pmatrix}$.
Compute its condition number, then compute the change in the recovered
concentrations produced by a $1\%$ error in the U window count rate, and compare
with the same experiment for $\mathbf{S}$ of the lesson. State the practical
consequence.

**★★8.** Repeat the lesson's height calculation for a Th window attenuation
coefficient $20\%$ larger than the K-window value, and state how the Th/K drift
with height changes. Explain why the *sign* of the drift is fixed by physics
regardless of the exact coefficients used.

## ★★★ Research-oriented

**★★★9.** Design an airborne radiometric survey to map a potassic alteration
halo whose Th/K contrast is $40\%$ against a host with Th/K $= 5.0$ and a K-window
count rate of $200\ \mathrm{counts\,s^{-1}}$ at $60\ \mathrm{m}$. Choose flying
height, ground speed, line spacing and integration length so that the halo is
resolved at $\ge 3\sigma$ in each pixel, and report the pixel size, the cost driver
and the one assumption that would invalidate the design.

**★★★10.** eU is inferred from a radon daughter. Model a disequilibrium factor
$D = ^{214}\mathrm{Bi}/^{238}\mathrm{U}$ ranging from $0.6$ to $1.4$ and compute
the bias this introduces into (a) the reported eU, (b) the Th/K ratio and
(c) the K/(K+U+Th) index. State which of the three is most robust to
disequilibrium and why, and how you would detect a disequilibrium problem in a
survey's own data.

**★★★11.** Transported cover of $20\ \mathrm{cm}$ over bedrock with a
$\mu/\rho = 0.06\ \mathrm{cm^{2}\,g^{-1}}$ and $\rho = 1.7\ \mathrm{g\,cm^{-3}}$
is proposed as an explanation for a suppressed anomaly. Compute the transmitted
fraction, then compute the cover thickness that would reduce a bedrock signal by
$90\%$. Specify the two measurements you would make to decide whether the cover
hypothesis is correct, and state what each measurement's *failure* would look
like.
