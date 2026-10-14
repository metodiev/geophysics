# Exercises — 16-02-05 Zero- and One-Dimensional Energy Balance Models

Attempt these before reading the
[solutions](./05-energy-balance-models-solutions.md). The lesson is
[05 Energy Balance Models](../05-energy-balance-models.md). Use
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$,
$S = 1361\ \mathrm{W\,m^{-2}}$,
$\rho_{\text{water}} = 1000\ \mathrm{kg\,m^{-3}}$,
$c_p = 4000\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and
$R_E = 6.371\times10^{6}\ \mathrm{m}$. All models are **SYNTHETIC**.

## ★ Foundational

**★1.** For the zero-dimensional EBM with $a = 0.20$ and with $a = 0.40$, compute
$F$ and the equilibrium temperature. State the sensitivity
$\mathrm{d}T/\mathrm{d}a$ between the two in $\mathrm{K}$ per unit albedo.

**★2.** Compute the heat capacity per unit area for mixed layers of $30$, $80$ and
$100\ \mathrm{m}$, and the relaxation time $C/B$ with
$B = 3.7423\ \mathrm{W\,m^{-2}\,K^{-1}}$. State what changes and what does not.

**★3.** Linearise the OLR about $T_0 = 270\ \mathrm{K}$: compute $A$ and $B$,
then the linearised equilibrium temperature for $F = 238.175\ \mathrm{W\,m^{-2}}$.
Compare with the exact $\sigma T^4$ solution ($254.578\ \mathrm{K}$) and explain
the sign of the difference.

**★4.** A step forcing of $4.0\ \mathrm{W\,m^{-2}}$ is applied. With the $B$ of ★3,
compute the equilibrium temperature change and the change after one and three
relaxation times.

## ★★ Applied

**★★5.** Derive the relaxation time of the linearised zero-dimensional EBM from
$C\,\mathrm{d}T/\mathrm{d}t = F - (A + BT)$ and show that the equilibrium
temperature is independent of $C$. Then explain why the measured e-folding time of
the *nonlinear* model exceeds $C/B$, and estimate the sign and rough size of the
effect without computing it.

**★★6.** Derive the finite-volume discretisation of
$D\,\partial_x[(1-x^2)\partial_x T]$ on a uniform $x$ grid, state the two boundary
conditions and show that they arise from the operator rather than being imposed.
Then sum the discrete steady-state equations over all $i$ and show that the
area-weighted mean temperature satisfies
$\langle T\rangle = (\langle Q(1-a)\rangle - A)/B$.

**★★7.** For the hysteresis of §3.4, compute the change in the planetary albedo
between the ice-free and frozen branches at $S/S_0 = 1.40$ using the tabulated
global means ($271.67\ \mathrm{K}$ and $239.34\ \mathrm{K}$) and the relation
$\sigma T^4 = Q(1-a)$ with $Q = 1.40S/4$. Explain why the two albedos must differ
and check that they do.

**★★8.** A grey radiative-equilibrium atmosphere gives a surface temperature of
$330\ \mathrm{K}$. Compute the flux the surface must export non-radiatively to sit
at $288\ \mathrm{K}$ instead, express it as a fraction of the absorbed solar flux
($238.175\ \mathrm{W\,m^{-2}}$), and state whether it is physically possible.

**★★9.** For the one-dimensional model with $D = 0.6\ \mathrm{W\,m^{-2}\,K^{-1}}$
and the equator-pole contrast of $24.052\ \mathrm{K}$, estimate the peak poleward
transport using
$H \approx 2\pi R_E^2 D\,\Delta T / \Delta x$ with the contrast over the range
$x \in [0,1]$, and compare your estimate with the model's $2.643\ \mathrm{PW}$.
State which approximation you made.

## ★★★ Research-oriented

**★★★10.** Design a numerical procedure that locates the two bifurcation points of
the ice-albedo model to within $10^{-3}$ in $S/S_0$. Specify the continuation
method, the order parameter, the tolerance, and the failure mode you would expect
when the iteration is started exactly on the branch. State what would falsify the
claim that the two points are the ends of a hysteresis loop rather than two
independent transitions.

**★★★11.** The lesson's §3.3 proves that a linear EBM's area-weighted mean
temperature is independent of the transport. Design a numerical experiment that
demonstrates the *failure* of that identity once the ice-albedo nonlinearity is
switched on, and quantify the failure as a function of the ice-covered area. Then
state, in one paragraph, what this implies about the statement "changing the ocean
circulation cannot change the global mean temperature".

**★★★12.** An EBM can be tuned to reproduce a global-mean temperature with several
different parameter combinations. Design a validation protocol that uses the
*pattern* (the latitudinal temperature profile, the seasonal cycle, the ice edge)
rather than the mean, specify at least three independent observables, and state
what each one constrains. Then identify which single observable would most
efficiently rule out the largest number of parameter combinations, and justify the
choice with the structure of the model rather than with a number.
