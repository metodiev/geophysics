# Exercises — 25-03-06 Project: Gravity Inversion with Uncertainty Quantification

Attempt these before reading the
[solutions](./06-gravity-inversion-uq-solutions.md). The project is
[06 Gravity Inversion](../06-gravity-inversion-uq.md). Values printed by
[`code/gravity_inversion_uq.py`](../code/gravity_inversion_uq.py):

| Quantity | Value |
|---|---|
| model | 8 blocks $\times$ 4 layers = 32 parameters, 25 data |
| layers | 0–1, 1–3, 3–6, 6–10 km |
| data | noise 0.05 mGal, range $-11.173$ to $+23.589$ mGal |
| kernel maximum | 0.0672 mGal per kg m⁻³ |
| condition number | $3.4\times10^{17}$ |
| $\chi^2/n$ at $\alpha$ | $0.0001$ ($10^{-6}$), $0.8641$ ($3.16\times10^{-4}$), $27.3837$ ($10^{-2}$) |
| mean 1σ / mean error | $15.09$ / $24.43\ \mathrm{kg\,m^{-3}}$ |
| $\operatorname{tr}R$ | $21.42$ of 32 |
| per-layer resolution | $0.612$, $0.656$, $0.665$, $0.745$ |
| equivalence class | deep spread $21.08\ \mathrm{kg\,m^{-3}}$, data spread $0.0459$ mGal, $16.8\%$ sign flips |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Estimate the gravity of a 2-D block of cross-section
$6.25\ \mathrm{km}\times1\ \mathrm{km}$ at $2.5\ \mathrm{km}$ depth with
$\Delta\rho = 1\ \mathrm{kg\,m^{-3}}$, using $g \approx 2G\Delta\rho A/d$, in both
m s⁻² and mGal. State the unit.

**★2.** The $\chi^2$ scan gives $0.0001$ at $\alpha = 10^{-6}$ and $27.3837$ at
$\alpha = 10^{-2}$. State what each of the two values means about the fit, and
state which side of 1 each is on.

**★3.** Define the resolution matrix $R = C_m A^{\mathsf T}W_dA$ and state what
$R_{ii} = 1$ and $R_{ii} = 0$ mean for parameter $i$.

## ★★ Applied

**★★4.** The trace of $R$ is $21.42$ for 32 parameters and 25 data. Compute the
ratio of resolved parameters to total parameters and to data. State which ratio is
the meaningful one and why.

**★★5.** The mean parameter uncertainty is $15.09\ \mathrm{kg\,m^{-3}}$ and the
mean actual error is $24.43\ \mathrm{kg\,m^{-3}}$. Compute the ratio, and explain
in two sentences which term of the error decomposition is missing from the
covariance and why it cannot be estimated from the data alone.

**★★6.** The posterior ensemble predicts data with an rms spread of
$0.0459\ \mathrm{mGal}$ while the data noise is $0.05\ \mathrm{mGal}$, and
$16.8\%$ of draws give the deep body a positive density. Compute the ratio of the
two spreads, and state what these two numbers together establish about the
equivalence class.

## ★★★ Research-oriented

**★★★7.** Design an experiment that would reduce the unresolved directions of
this inversion. Name the new observation, the mechanism by which it adds
information that gravity lacks (state which *kernel* it provides), how many data
you would need to raise $\operatorname{tr}R$ to at least 29 of 32, and the test
that would show the improvement is real rather than an artefact of a changed
prior. A design that changes only the prior is a failed answer.
