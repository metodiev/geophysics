# Exercises — 06-07-02 Retrieving the Green's Function by Cross-Correlation

Attempt these before reading the
[solutions](./02-cross-correlation-green-solutions.md). The lesson is
[02 Retrieving the Green's Function by Cross-Correlation](../02-cross-correlation-green.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Two stations are $45\ \mathrm{km}$ apart in a medium with
$c = 3.00\ \mathrm{km\,s^{-1}}$. Compute the causal and acausal arrival lags of
the retrieved correlation and state what measurement the pair of lags makes
possible.

**★2.** The demonstration's simulated pair has $d = 60\ \mathrm{km}$,
$c = 3.20\ \mathrm{km\,s^{-1}}$, $dt = 0.5\ \mathrm{s}$, ring radius
$R = 500\ \mathrm{km}$. Compute the two station delays in samples
($\tau_A/dt$, $\tau_B/dt$), round them to whole samples, and state the arrival
lag of the **discrete** model. Compare with the continuum value.

**★3.** From the demonstration's emergence table, the noise floor falls from
$0.41719$ at $N=1$ to $0.04801$ at $N=64$ segments. Compute the ratio and the
implied exponent $\log(\text{ratio})/\log(64)$, and state the theoretical value.

## ★★ Applied

**★★4.** The demonstrated error in the measured arrival lag is $-0.750\
\mathrm{s}$ against the continuum value $d/c$. Using the sample interval
$dt = 0.5\ \mathrm{s}$, decompose this error into the part caused by rounding
the model delays to whole samples and the part caused by the estimator, and
justify the split with arithmetic.

**★★5.** The one-sided-source table gives causal/acausal ratios of $10.99$ for a
$180^\circ$ and $9.04$ for a $90^\circ$ sector — not monotone. Explain why the
ratio need not be monotone in the sector width, and design a control that would
reveal whether the non-monotonicity is physics or a finite-source artefact.

**★★6.** A study needs the arrival time of a $60\ \mathrm{km}$ pair to
$0.050\ \mathrm{s}$. Using $\sigma_t \approx 1/(2\pi f\,\text{SNR})$, compute the
signal-to-noise ratio required at $f = 1.0\ \mathrm{Hz}$, and state how the
requirement changes at $f = 0.25\ \mathrm{Hz}$.

## ★★★ Research-oriented

**★★★7.** Design a test of the equipartition assumption for a two-station
retrieval, given that you may deploy an additional independent source (a
controlled shot) and you have one year of noise data. State the observable, the
prediction if equipartition holds, the prediction if it fails, and the decision
rule including its uncertainty.

**★★★8.** The correlation-type representation theorem relates the correlation
of a diffuse field to $\tfrac{d}{dt}\big[G(t)-G(-t)\big]$. Explain the origin of
the time derivative, state precisely which measurements it affects and which it
leaves unchanged, and give one situation in which neglecting it would produce a
wrong published number.
