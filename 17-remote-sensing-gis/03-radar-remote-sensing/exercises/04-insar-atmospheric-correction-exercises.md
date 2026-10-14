# Exercises — 17-03-04 Atmospheric and Orbital Error Correction in InSAR

Attempt these before reading the
[solutions](./04-insar-atmospheric-correction-solutions.md). The lesson is
[04 Atmospheric and Orbital Error Correction](../04-insar-atmospheric-correction.md).
All models are **SYNTHETIC** teaching values.

Constants: $\lambda = 5.6565\ \mathrm{cm}$,
$4\pi/\lambda = 222.16\ \mathrm{rad\,m^{-1}}$, $\cos 35^\circ = 0.8192$.

## ★ Foundational

**★1.** Compute the zenith excess path for a refractivity profile
$N(z) = N_s\exp(-z/H)$ with $N_s = 300\ \mathrm{ppm}$ and $H = 7.5\ \mathrm{km}$,
and then its value at zenith angle $z = 45^\circ$ in the plane-parallel mapping.
State the units at each step.

**★2.** A differential path delay of $15\ \mathrm{mm}$ is suspected in an
interferogram. Convert it into phase (rad), fringes, and apparent line-of-sight
displacement. Then give the vertical displacement that the same fringe pattern
would imply if the motion were assumed purely vertical at $\theta = 35^\circ$.

**★3.** Name the three error sources treated in the lesson and give, for each,
one spatial signature and one temporal signature that would help identify it in a
stack.

## ★★ Applied

**★★4.** The lesson fits a straight line to a screen that truly varies as
$3.00\,(h/1\,\mathrm{km}) - 0.25\,(h/1\,\mathrm{km})^{2}$ mm over
$228 \le h \le 816\ \mathrm{m}$ and recovers a slope of $2.3077\
\mathrm{mm\,km^{-1}}$ with a residual rms of $0.0150\ \mathrm{mm}$. **(a)** Explain
the *sign and size* of the slope bias in terms of the least-squares formula
$\hat{c}_1 = \mathrm{cov}(h,d)/\mathrm{var}(h)$. **(b)** State what the residual
rms would have been if the true relation had been exactly linear, and what that
tells you about the diagnostic value of the residual.

**★★5.** For a turbulent screen the structure function follows
$D(r) = D_0 (r/r_0)^{0.71}$. With $D(1\ \mathrm{km}) = 4.0\ \mathrm{mm^{2}}$,
compute $D(4\ \mathrm{km})$, the rms difference at 4 km, and the largest
separation at which $D$ is still below the $5\ \mathrm{mm^{2}}$ value typical of a
well-corrected pair.

**★★6.** A stack of 30 epochs has screens of rms $8.0\ \mathrm{mm}$, of which a
fraction $\rho$ of the *variance* is common to all epochs. Using the model
$\sigma_{\text{mean}} = \sigma\sqrt{\rho + (1-\rho)/N}$, tabulate the residual of
the epoch mean for $\rho = 0,\ 0.3,\ 0.6,\ 0.9$ and state the practical
consequence for the length of a stack.

## ★★★ Research-oriented

**★★★7.** You are asked to validate an atmospheric correction for a subsidence
study where the target signal is $2\ \mathrm{mm\,yr^{-1}}$ over 4 years. Specify
the validation experiment: which independent data you would use, which statistic
you would compute, what residual you would accept for the correction to be
"adequate", and how you would detect the failure mode of the correction removing
part of the real signal. A specification that could not be executed is a failed
answer.

**★★★8.** The demonstration needed $131\,072$ samples spanning a $500$-fold
wavenumber band to recover the predicted structure-function exponent to within
$0.06$. Using the conditions $k_{\min}r \ll 1$ and $k_{\max}r \gg 1$, argue
quantitatively why a $300 \times 300$ pixel scene cannot measure a turbulent
exponent for a screen whose smallest structure is $10$ pixels across, and state
what *can* legitimately be estimated from such a scene.
