# Exercises — 16-02-06 Aerosols, Clouds and Their Radiative Effects

Attempt these before reading the
[solutions](./06-aerosols-and-clouds-radiation-solutions.md). The lesson is
[06 Aerosols, Clouds and Their Radiative Effects](../06-aerosols-and-clouds-radiation.md).

Use $\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$,
$S = 1361\ \mathrm{W\,m^{-2}}$, $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$T_s = 288.15\ \mathrm{K}$ and the stated lapse-rate convention
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$. From the lesson's synthetic cloud
($r_e = 10\ \mu$m, $v_e = 0.10$, visible): mass extinction coefficient
$k_{\text{ext}} = 156.76\ \mathrm{m^2\,kg^{-1}}$, $g = 0.8619$, and
$k_{\text{abs}} = 49.94\ \mathrm{m^2\,kg^{-1}}$ in the thermal infrared.
**All models and data in this module are SYNTHETIC.**

## ★ Foundational

**★1.** Compute the shortwave optical depth of a cloud with
$\text{LWP} = 50\ \mathrm{g\,m^{-2}}$ for $r_e = 8\ \mu$m and $r_e = 16\ \mu$m
using the geometric relation $\tau = 3\,\text{LWP}/(2\rho_wr_e)$. Then correct
each value with the Mie-integrated coefficient obtained by linear interpolation
between the tabulated ratios (1.0721 at $5\ \mu$m, 1.0451 at $10\ \mu$m, 1.0368
at $15\ \mu$m, 1.0272 at $20\ \mu$m). State which radius the correction matters
more for, and why.

**★2.** For $\text{LWP} = 30\ \mathrm{g\,m^{-2}}$ compute the thermal absorption
optical depth, the cloud emissivity $\varepsilon = 1 - e^{-\tau_{\text{abs}}}$,
and the longwave cloud radiative forcing for a cloud at 3 km defined as
$\text{CF}_{\text{LW}} = \varepsilon(\sigma T_s^4 - \sigma T_c^4)$.

**★3.** Using the delta-Eddington albedos of the lesson's §3.6 table
($A = 0.3703$ at $\tau = 5$, $0.5330$ at $\tau = 10$, $0.6907$ at $\tau = 20$,
all at $\mu_0 = 0.6$), estimate $\mathrm{d}A/\mathrm{d}\tau$ over the intervals
$[5,10]$ and $[10,20]$ and state in one sentence what the decrease means.

## ★★ Applied

**★★4.** Explain why the identity $R + T = 1$ for a conservative layer
($\omega_0 = 1$) over a black surface follows from the flux-difference equation
alone, without any knowledge of the flux-sum equation. Then state which of the
three identities in the lesson's §3.2 fails for an absorbing layer and why.

**★★5.** A cloud has $\text{LWP} = 100\ \mathrm{g\,m^{-2}}$ and
$r_e = 10\ \mu$m, so $\tau = 15.676$ and $A = 0.6380$. The droplet number is
increased by a factor of 4 with LWP held fixed. Compute the new $r_e$, the new
$\tau$, the new albedo, and compare the albedo change with the asymptotic
susceptibility prediction $A(1-A)/3 \times \ln 4$. State the percentage by which
the asymptotic form is wrong.

**★★6.** Using the thin-layer criterion of the lesson's §3.7, with $g = 0.30$ and
$\mu_0 = 0.6$: (a) determine whether an aerosol layer with $\omega_0 = 0.85$ over
a surface of albedo $\alpha_s = 0.3$ brightens or dims the scene; (b) find the
critical $\omega_0$ for $\alpha_s = 0.3$; (c) state how the criterion changes when
$g$ is increased to 0.6 and explain the direction of the change physically.

**★★7.** The Eddington closure implies a backscattered beam fraction
$b_{\text{Edd}} = \tfrac12(1 - \tfrac32g\mu_0)$. Compute $b_{\text{Edd}}$ for
$g = 0.70$ and $g = 0.8619$ at $\mu_0 = 0.6$; the exact azimuth-averaged
Henyey–Greenstein values are $0.1468$ and $0.0613$ respectively. Give the ratio
in each case and explain why delta-Eddington scaling reduces the error.

## ★★★ Research-oriented

**★★★8.** Design a validation protocol for a two-stream radiative-transfer code
that computes cloud reflectance. Order the checks from strongest to weakest,
state for each what a failure would look like in the output, and explain which
check would detect a wrong beam sign in the flux-sum equation but not in the
flux-difference equation. Do not repeat the checks of the lesson verbatim; add at
least one that is not in it.

**★★★9.** The lesson's §3.5 computes a cloud radiative forcing from a
single-layer model with an overcast scene. Critique that decomposition: identify
which terms are artefacts of the closure rather than physics, quantify the closure
sensitivity using the delta-Eddington versus plain-Eddington albedos at
$\text{LWP} = 5$ and $20\ \mathrm{g\,m^{-2}}$ ($R_{\delta} = 0.1904$ and $0.3409$;
$R_{\text{plain}} = 0.2086$ and $0.3496$; scene insolation
$\mu_0S = 816.6\ \mathrm{W\,m^{-2}}$), and specify exactly what additional
information a global mean would require.

**★★★10.** Design a synthetic experiment to test whether a change in cloud albedo
attributable to droplet number could be detected at all, given a 2 per cent
radiometric error on reflectance and a 10 per cent error on liquid-water path.
State the observable, the retrieval, the error propagation, the confounders you
must exclude, and the conclusion you would be entitled to draw if the experiment
succeeded. Be explicit about which quantities in your design are measured,
retrieved and modelled.
