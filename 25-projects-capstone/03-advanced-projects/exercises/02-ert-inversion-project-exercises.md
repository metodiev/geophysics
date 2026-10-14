# Exercises — 25-03-02 Project: ERT Inversion with Resolution Assessment

Attempt these before reading the
[solutions](./02-ert-inversion-project-solutions.md). The project is
[02 ERT Inversion](../02-ert-inversion-project.md). Values printed by
[`code/ert_inversion_demo.py`](../code/ert_inversion_demo.py):

| Quantity | Value |
|---|---|
| true model | $\rho_1 = 100$, $\rho_2 = 1000\ \Omega\,\mathrm{m}$, $h = 10.0\ \mathrm{m}$ |
| reflectance | $k = 0.8182$ |
| data | 25 Wenner spacings, 1.0–60.0 m, $3\%$ + $1\ \Omega\,\mathrm{m}$ noise |
| fitted model | $100.367$, $1155.38\ \Omega\,\mathrm{m}$, $10.5558\ \mathrm{m}$ |
| misfit | $\chi^{2} = 28.631$, rms $1.070\sigma$ |
| linearised relative 1σ | $1.43\%$, $11.42\%$, $4.20\%$ |
| correlation | $\rho_1\rho_2 +0.224$, $\rho_1 h +0.584$, $\rho_2 h +0.834$ |
| profile likelihood | $h = 10.20$–$10.90\ \mathrm{m}$, $\rho_2 = 1073$–$1246\ \Omega\,\mathrm{m}$ |
| trade-off rows | $(8.00, 721.1)$, $(9.25, 893.6)$, $(10.50, 1141.7)$, $(11.75, 1531.7)$, $(13.00, 2233.8)$ |
| sensitivity 50% spacing | $36.68\ \mathrm{m}$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the reflectance $k$ for $\rho_1 = 50\ \Omega\,\mathrm{m}$ and
$\rho_2 = 500\ \Omega\,\mathrm{m}$, and state the two limits of $\rho_a(a)$ as
$a \to 0$ and $a \to \infty$.

**★2.** The fit gives $\chi^{2} = 28.631$ for 25 data and 3 parameters. Compute
the misfit per datum and per degree of freedom, and state which of the two is
used to test goodness of fit and why.

**★3.** Convert the three linearised relative uncertainties to absolute values
with units: $1.43\%$ on $\rho_1$, $11.42\%$ on $\rho_2$, $4.20\%$ on $h$.

## ★★ Applied

**★★4.** Using the trade-off rows $(8.00\ \mathrm{m}, 721.1\
\Omega\,\mathrm{m})$ and $(13.00\ \mathrm{m}, 2233.8\ \Omega\,\mathrm{m})$, compute
the local exponent $\mathrm{d}\ln\rho_2/\mathrm{d}\ln h$, and compute the
transverse resistance $\rho_2 h$ at both ends. State which quantity is better
conserved along the trade-off.

**★★5.** The sensitivity of $\rho_a$ to $\rho_2$ reaches half its maximum at
$a = 36.68\ \mathrm{m}$. Using the Wenner median depth-of-investigation rules
$a/2$ and $a/3$, compute the two depth estimates, and state whether a 25 m thick
surface layer could be resolved by this survey.

**★★6.** The profile-likelihood interval for $h$ is $\pm 0.35\ \mathrm{m}$ and
the linearised interval is $\pm 0.44\ \mathrm{m}$. Compute the ratio and explain
in two sentences why the profile interval is the narrower one and which the
report should quote.

## ★★★ Research-oriented

**★★★7.** A client requires the depth to a resistive bedrock to
$\pm 10\%$ at a site where the overburden may be 30 to 50 m thick. Design the
acquisition: the array type, the electrode spacing and maximum spread, the number
of electrodes, the expected depth of investigation, and the test you would run on
the data to detect that the requirement is *not* met before reporting a number.
State the cost driver. A design without the failure test is a failed answer.
