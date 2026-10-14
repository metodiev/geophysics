# Exercises — 19-08-01 Simulating a 2-D/3-D Seismic Wavefield

Attempt these before reading the
[solutions](./01-simulate-seismic-wavefield-solutions.md). The lesson is
[01 Simulating a 2-D/3-D Seismic Wavefield](../01-simulate-seismic-wavefield.md).
All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Using $c_g/c = \cos(\theta/2)/\sqrt{1-C^{2}\sin^{2}(\theta/2)}$ with
$\theta = 2\pi/\mathrm{ppw}$ and $C = 0.5$, compute the numerical group velocity at
$6$ points per wavelength. State whether the numerical wave is faster or slower
than the medium.

**★2.** A 2-D acoustic simulation uses $c = 4000$ m/s, a source with a 25 Hz upper
corner, $C = 0.6$ and a grid spacing chosen for $10$ points per wavelength at
25 Hz. Compute $\Delta x$, $\Delta t$, and say whether the run is stable, quoting
the exact limit.

**★3.** Explain in two sentences why a travel-time pick is governed by the group
velocity rather than by the phase velocity, and why the difference matters in this
scheme.

## ★★ Applied

**★★4.** At $8$ points per wavelength the demonstration measures
$c_g/c = 0.95808$. A reflector is imaged at $3.000$ km using the medium velocity.
Compute the depth error and the apparent depth, and state the sign of the error.

**★★5.** A 3-D survey must image a target at $8$ km depth in a medium with
$c = 3500$ m/s, resolving $20$ Hz. Design the grid for $10$ points per wavelength,
choose $\Delta t$ for $C = 0.5$, and compute the node count and the working-set
memory for a $15\times15\times8$ km model using seven field arrays at eight bytes
per value.

**★★6.** At $8$ points per wavelength the demonstration computes an anisotropy of
$1.312$ per cent between propagation along an axis and along the diagonal. Convert
that into a travel-time difference for a wave crossing $5$ km, and state whether it
could be mistaken for real anisotropy in a shear-wave-splitting measurement.

## ★★★ Research-oriented

**★★★7.** Design a benchmark that would detect a code whose absorbing boundary
reflects $5$ per cent of the incident amplitude, given that the interior scheme is
already verified. State the geometry, the observable, the target signal level and
the test's failure threshold.

**★★★8.** Derive the two-dimensional stability limit
$C \le 1/\sqrt{2}$ from the symbol of the five-point Laplacian, and explain why the
limit is set by the corner wavenumbers rather than by any physical property of the
medium.
