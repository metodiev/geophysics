# Exercises — 14-03-04 Building Geophysical Proxies for Hydrological Properties

Attempt before the [solutions](./04-geophysical-proxy-relations-solutions.md).
Lesson:
[04 Building Geophysical Proxies for Hydrological Properties](../04-geophysical-proxy-relations.md).
All models, data and posteriors are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For the chain $\rho_t \to \phi \to k$ with $m = 2$, derive
$\mathrm{d}\ln k/\mathrm{d}\ln\rho_t$ at $\phi = 0.30$ and evaluate it.

**★2.** Using ★1, compute the permeability error produced by a $3\%$ error in
$\rho_t$. State the units convention you are relying on.

**★3.** In a Monte Carlo, $\phi$ has a $10\%$ relative one-sigma spread. Predict
the relative one-sigma spread of $k$ from the amplification factor, and check
your prediction against the lesson's table.

## ★★ Applied

**★★4.** A proxy reports a single number $k = 6.2\times10^{-12}\ \mathrm{m^{2}}$
with no error bar. **(a)** List the four quantities that the number silently
assumes. **(b)** For each, state whether it is a measurement, a fitted model
parameter, or a model choice. **(c)** State which one you would attack first in
a real study and why.

**★★5.** In the lesson's two-parameter grid, resistivity alone gives
$\phi$ to $\pm0.0636$ and $V_p$ alone gives $S_w$ to $\pm0.2742$; jointly they
give $\pm0.0043$ and $\pm0.0122$. **(a)** Explain, in terms of the forward
operators, why each datum is weak on one parameter and strong on the other.
**(b)** Explain why the joint improvement is so much better than either single
measurement.

**★★6.** A study needs $\sigma_{\ln k} \le 0.693$ (a factor of two). The
resistivity is known to $2\%$, the cementation exponent to $\pm0.2$, and the
grain size to $\pm30\%$. Compute each contribution to $\sigma_{\ln k}$, rank
them, and name the single most effective action.

## ★★★ Research-oriented

**★★★7.** Two measurements that constrain the *same* parameter direction reduce
$\sigma$ at best by $\sqrt{2}$. Two measurements that constrain *orthogonal*
directions reduce it much more. **(a)** State the general result for combining
two Gaussian likelihoods in terms of their Fisher information. **(b)** Show with
the lesson's numbers that resistivity and velocity are closer to orthogonal than
to parallel. **(c)** State the practical acquisition rule that follows.

**★★★8.** Design a monitoring proxy for a tracer injection that must detect a
$5\%$ change in water saturation. **(a)** Write the chain from the measured
quantity to the target. **(b)** Compute the smallest detectable change in the
measured quantity given a stated $2\%$ noise level on each measurement.
**(c)** State which single modelling assumption dominates the result, and how you
would test it in the field. **(d)** Explain why the *difference* between two
surveys is a better estimator than either survey alone, and compute the noise
penalty that difference-taking imposes.
