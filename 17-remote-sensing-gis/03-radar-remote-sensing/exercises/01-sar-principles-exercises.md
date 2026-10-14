# Exercises — 17-03-01 SAR Principles: Geometry, Polarisation, Backscatter

Attempt these before reading the
[solutions](./01-sar-principles-solutions.md). The lesson is
[01 SAR Principles](../01-sar-principles.md). All models are **SYNTHETIC**
teaching values.

Numbers you may need: $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$,
$k_B = 1.380\,649\times10^{-23}\ \mathrm{J\,K^{-1}}$,
$GM = 3.986\,004\,418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
mean Earth radius $6371\ \mathrm{km}$.

## ★ Foundational

**★1.** A radar transmits with $B = 60\ \mathrm{MHz}$ and images at local
incidence $\theta = 30^\circ$. Compute the slant-range resolution and the
ground-range resolution, with units, and state the assumption you used to
convert between them.

**★2.** With $\lambda = 3.123\ \mathrm{cm}$, $L = 4\ \mathrm{m}$ and
$R = 700\ \mathrm{km}$, compute the real-aperture azimuth resolution and the
synthetic-aperture azimuth resolution. State in one sentence which one depends
on range and why.

**★3.** A distributed scene has $\sigma^{0} = -10\ \mathrm{dB}$ and the
resolution cell measures $4.0\ \mathrm{m}$ (range) by $5.0\ \mathrm{m}$
(azimuth). Give the radar cross section of one cell in $\mathrm{m^{2}}$ and in
$\mathrm{dB\,m^{2}}$, and explain why $\sigma^{0}$ is the more useful
normalisation of the two.

## ★★ Applied

**★★4.** A platform flies at $v = 7500\ \mathrm{m\,s^{-1}}$ with an azimuth
antenna of $L = 4\ \mathrm{m}$ and must image a swath $W = 60\ \mathrm{km}$ wide.
Write the two PRF inequalities, evaluate both bounds, and decide whether any
PRF satisfies them. If not, compute the minimum antenna length that makes the
window non-empty, and interpret the result.

**★★5.** In the lesson's budget the compressed SNR for a $1\ \mathrm{m^{2}}$
target at $R = 800\ \mathrm{km}$ is $0.892$. **(a)** By how many dB does the
SNR change if the range doubles? **(b)** If the transmit power doubles at the
same time, what is the net change? **(c)** What compressed SNR does a
$5\ \mathrm{m^{2}}$ target give at the original range?

**★★6.** A planar facet dips toward the sensor by $\alpha = 50^\circ$ at
$\theta = 35^\circ$. Is it foreshortened, in layover, or in shadow? Repeat for
$\alpha = 30^\circ$ at $\theta = 35^\circ$, and for a facet facing *away* from
the sensor with $\alpha = 60^\circ$ at $\theta = 35^\circ$. Give the
foreshortening factor where it is defined.

## ★★★ Research-oriented

**★★★7.** A quality-control question: given a single-look intensity image, you
suspect that part of the variability is multiplicative speckle and part is
additive receiver noise. Specify a measurement that separates them, stating the
statistic, the model for each contribution, what you expect to observe if only
speckle is present, and how you would report the result. A specification that
could not be executed is a failed answer.

**★★★8.** The measured $-3\ \mathrm{dB}$ width of the focused response is
$0.886\,L/2$ for an unweighted aperture. Derive where $0.886$ comes from, then
state what changes if the aperture is weighted with a raised-cosine taper:
explain qualitatively which of (mainlobe width, peak sidelobe level, integrated
sidelobe ratio, SNR) improves and which degrades, and why an imaging system
might still choose the taper.
