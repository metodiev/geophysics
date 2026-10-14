---
id: 08-03-05
title: "Depth Estimation: Werner, Euler, Peters and Spectral Methods"
level: doctoral
prereqs: ["08-03-04", "01-14-04"]
tags: [geomagnetism, electromagnetism, depth-estimation, euler-deconvolution, werner-deconvolution, spectral-analysis]
---

# Depth Estimation: Werner, Euler, Peters and Spectral Methods

Depth is the quantity every magnetic survey is asked for and the one it is worst
at supplying. Four classical methods dominate practice — **Euler
deconvolution**, **Werner deconvolution**, the **half-width (Peters) rule** and
the **spectral** (mean-depth) method — and each is a *model* disguised as a
measurement. This lesson derives all four, runs them on synthetic data whose
depths are known exactly, and reports the errors. The pattern that emerges is
consistent: a method works precisely when its model matches the body, and its
reported number is a model assumption as much as a datum.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** Euler's equation from the homogeneity of a potential field and
   **state** the structural index of a dipole, a cylinder, a thin sheet and a
   contact.
2. **Implement** Euler deconvolution on a gridded anomaly and **measure** how the
   recovered depth depends on the assumed structural index.
3. **Quantify** the effect of noise on the depth scatter, and **explain** why
   smoothing is both necessary and biasing.
4. **Set up** the Werner linear system for a 2-D thin sheet and **recover** the
   depth and position of a synthetic dike.
5. **Derive** the half-width rule for a line source, **measure** it, and
   **quantify** the error when the model is wrong.
6. **Derive** the $k^{2}e^{-2kz}$ power spectrum of a dipole ensemble and
   **compare** the fitted depth with the true distribution.
7. **State** for each method what it assumes and what it therefore cannot test.

## Prerequisites

- [08-03-04 Forward Modelling Magnetic Bodies](04-magnetic-forward-modelling.md) —
  the anomaly of a body of finite size.
- [01-14-04 Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the linear estimation used by Euler and Werner.

## 1. Euler deconvolution

### 1.1 The equation

A potential field anomaly that is homogeneous of degree $-N$ about a source
location $\mathbf{r}_0$ satisfies Euler's theorem,

$$\left(\mathbf{r}-\mathbf{r}_0\right)\cdot\nabla T = -N\left(T - T_0\right),$$

where $T_0$ is a regional (background) level. The dipole anomaly of
[04](04-magnetic-forward-modelling.md) is homogeneous of degree $-3$: both terms
of $C m\left(3u^{2}r^{-5} - r^{-3}\right)$ scale as the third power of a distance
measured from the source. Hence $N = 3$ for a dipole.

Rearranging for an observation plane at $z = 0$ gives a **linear** equation in
the four unknowns $\left(x_0, y_0, z_0, T_0\right)$ when $N$ is assumed:

$$x\,T_x + y\,T_y + N\,T = x_0\,T_x + y_0\,T_y + z_0\,T_z + N\,T_0 .$$

Each grid point supplies one equation; a moving window of points supplies an
over-determined system solved by least squares, and the window's solution is
accepted or rejected on its residual. The depths reported are the $z_0$ of the
accepted windows.

The standard structural indices are a convention, stated here as such:

| Source geometry | Structural index $N$ |
|---|---|
| Contact (step) | 0 |
| Thin sheet, dike, fault | 1 |
| Vertical cylinder, pipe | 2 |
| Sphere, dipole | 3 |

### 1.2 What the choice of index does

A **synthetic** dipole of moment $1.00\times10^{10}$ A m$^2$ is placed at
$(0, 0, 3.0\ \mathrm{km})$, with a vertical magnetisation and a vertical
measurement. Gradients are formed from the grid, the vertical gradient by the
upward-continuation relation $\partial_z \leftrightarrow +\left|k\right|$, and a
$4\times4$ km window is slid over a $7\times7$ set of window centres:

| Assumed $N$ | Accepted windows | Median depth (km) | Ratio to true | Interquartile range (km) |
|---|---|---|---|---|
| 3 (dipole) | 49 | 3.018 | 1.006 | 0.017 |
| 2 (cylinder) | 49 | 2.424 | 0.808 | 0.397 |
| 1 (thin sheet) | 45 | 1.830 | 0.610 | 0.794 |
| 0 (contact) | 20 | 1.181 | 0.394 | 0.820 |

With the correct index the method is accurate to $0.6\%$ and tightly clustered
(interquartile range 17 m). With the wrong index the answer is systematically
wrong and *much* more scattered: choosing $N = 0$ puts the body at 1.18 km
instead of 3.00 km and produces a spread of 0.82 km among windows that all claim
to be solutions. **The structural index is not a free parameter to be tuned for
prettiness: it is the model.**

## 2. Noise, gradients and the price of smoothing

Vertical gradients on a grid are obtained from the wavenumber domain, where the
symbol is $\left|k\right|$: differentiating multiplies high-wavenumber noise by
$\left|k\right|$, which is the amplification that
[03 Reduction to the Pole](03-reduction-to-pole.md) also suffers. The practical
remedy is to smooth before differencing. The remedy has a cost, and the
demonstration measures both.

| Noise rms (nT) | Accepted | Median depth (km) | Ratio to true | Interquartile (km) |
|---|---|---|---|---|
| 0.0 | 49 | 4.052 | 1.351 | 1.592 |
| 0.5 | 45 | 4.175 | 1.392 | 1.505 |
| 2.0 | 18 | 5.641 | 1.880 | 1.091 |
| 10.0 | 7 | 6.160 | 2.053 | 0.482 |

Read the zero-noise row first: **smoothing alone biases the depth upward by
35%**, from 3.00 to 4.05 km, because a smoothed anomaly is the anomaly of a
deeper body. Adding noise makes the bias worse and shrinks the number of windows
that pass the residual test. The two effects fight: without smoothing the Euler
system is unusable in noise, with smoothing it is biased. An honest Euler result
therefore has to report both the smoothing length and the residual threshold, and
its depth carries the smoothing bias explicitly.

## 3. Werner deconvolution

Werner's method assumes a *specific* 2-D model and solves for its parameters
linearly. For a thin sheet or dike striking perpendicular to the profile,

$$T(x) = \frac{A\,z}{\left(x-x_0\right)^{2}+z^{2}},$$

a symmetric anomaly of amplitude $A/z$ centred on $x_0$ with a half-width of $z$.
Set $\left(x^{2}+b_1x+b_2\right)T = a_0 + a_1x$ and expand. The result is linear
in the four parameters $\left(a_0, a_1, b_1, b_2\right)$:

$$x^{2}T = a_0 + a_1x - b_1xT - b_2T .$$

Least squares over the profile gives $b_1$ and $b_2$, and then

$$x_0 = -\frac{b_1}{2}, \qquad z = \sqrt{b_2 - \frac{b_1^{2}}{4}} .$$

**Numerical check (SYNTHETIC).** A sheet with $x_0 = 1.00$ km, $z = 2.00$ km and
$A = 400$ nT km gives a peak of 200.0 nT. The fit returns

$$b_1 = -2.00000\ \mathrm{km}, \qquad b_2 = 5.00000\ \mathrm{km^{2}},$$

so $x_0 = +1.0000$ km and $z = \sqrt{5.00000 - 1.00000} = 2.0000$ km: a depth
error of $0.0000\%$. The recovery is exact because the synthetic data *are* the
model. The method's error is entirely the error of the model, which is why the
diagnostic to watch is the goodness of fit of the rational function, not the
least-squares residual of the depth.

## 4. The half-width rule (Peters' method)

The sheet model above has a maximum of $A/z$ at $x = x_0$, and at
$x = x_0 \pm z$ the value is $A/(2z)$ — exactly half. Therefore

$$\text{FWHM} = 2z \qquad \Longrightarrow \qquad z = \frac{\text{FWHM}}{2}.$$

**Measured on the synthetic sheet:** FWHM $= 4.000$ km, so $z = 2.000$ km
against a true 2.00 km. Exact, for the model.

**Measured on the wrong model.** Applying the same rule to the profile of a
*dipole* at 2.00 km depth gives FWHM $= 2.000$ km and therefore $z = 1.000$ km:
an error of $-50\%$. The rule is blind to which model it is being applied to, and
it is the *model* that supplies the factor of two. This is the cleanest
illustration in the module that a depth estimator is a model plus arithmetic, and
that the arithmetic is the cheap part.

## 5. The spectral method

For a set of compact sources, the radial power spectrum of the anomaly is the
incoherent sum of the individual spectra. For a vertically magnetised dipole
observed with a vertical field, the amplitude spectrum is proportional to
$k\,e^{-kz_0}$ — one factor of $k$ from the vertical derivative in the Poisson
relation and one from the source depth — so the **power** spectrum is

$$P(k) \propto k^{2}\,e^{-2kz_0},
\qquad \ln P - 2\ln k = \text{const} - 2kz_0 .$$

A straight-line fit of $\ln P - 2\ln k$ against $k$ therefore has slope $-2z_0$,
and the method returns a *mean* depth over whatever ensemble produced the
spectrum.

**Measured for single bodies** (fit over the band $2\pi/30$ to $2\pi/6$
rad km$^{-1}$, 17 radial bins):

| True depth (km) | Fitted depth (km) | Error (%) |
|---|---|---|
| 2.0 | 2.018 | $+0.92$ |
| 3.0 | 3.016 | $+0.52$ |
| 5.0 | 5.009 | $+0.18$ |

For a single body the method is good to about 1%. **Measured for an ensemble** of
equal-moment dipoles half at 2 km and half at 6 km:

| Bodies | Fitted depth (km) | Moment-squared weighted mean at the band centre (km) |
|---|---|---|
| 160 | 2.951 | 2.022 |
| 800 | 3.146 | 2.022 |

The fitted value is not the weighted mean, and it *moves with the number of
bodies*. The reason is the assumption the derivation makes and the experiment
breaks: the sum of the fields of many random sources is not the sum of their
powers, because the cross terms between sources do not cancel in a finite
ensemble. The Spector–Grant method requires a genuinely incoherent source
distribution; when that fails, the number returned is an artefact of the
source-count, not a depth.

## 6. Assumptions and regime of validity

| Method | Model assumed | Fails when |
|---|---|---|
| Euler | A homogeneous source of known index $N$, plus a constant regional level | $N$ is wrong; the regional is not constant; the source is a distributed body |
| Werner | A 2-D thin sheet, or a contact, with a linear background | The body is 3-D; several bodies overlap; the profile crosses the strike obliquely |
| Peters (half-width) | A 2-D line source | The body is not a line source — a $50\%$ error for a dipole (Section 4) |
| Spectral | An incoherent ensemble of compact sources at a common mean depth | The sources are coherent, few, or spread over a wide depth range |

Three further shared conditions:

1. **Adequate sampling.** All four methods read gradients or half-widths, and
   all four are degraded or aliased when the station spacing approaches the
   anomaly half-width.
2. **Correct removal of the regional field.** A wrong regional level biases every
   method; for Euler it enters as $T_0$, and for Werner as an unmodelled linear
   trend.
3. **An isolated anomaly.** All four are single-source methods at heart; sliding
   them over a multi-source map is an exercise in deciding which windows to
   believe, and the accepted-window count is itself a result.

## 7. Python demonstration

`code/magnetic_depth_estimation_demo.py`:

1. builds a synthetic dipole anomaly at 3.0 km and prints its gradients;
2. runs Euler deconvolution for four structural indices and tabulates the medians
   and interquartile ranges;
3. repeats Euler with four noise levels after spectral smoothing, showing the
   smoothing bias;
4. recovers a synthetic dike by Werner deconvolution to four decimal places;
5. measures the half-width rule on the right model and the wrong one;
6. fits the power spectrum of single dipoles and of ensembles, and compares the
   ensemble fit with the model's weighted mean.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_depth_estimation_demo.py
```

Fixed seed, print-only, exits 0.

## 8. Exercises

[`exercises/05-magnetic-depth-estimation-exercises.md`](./exercises/05-magnetic-depth-estimation-exercises.md)
and
[`exercises/05-magnetic-depth-estimation-solutions.md`](./exercises/05-magnetic-depth-estimation-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** survey over a buried pipe produces an anomaly whose maximum
> horizontal gradient is 12 nT km$^{-1}$. **(a)** State the structural index you
> would assume and justify it in one sentence. **(b)** Given that the accepted
> Euler windows return 3.9 km while the pipe's top is at 4.0 km, and that the
> data were smoothed with a 1 km Gaussian, state the two corrections you would
> make before reporting a depth. **(c)** A colleague fits a rational function
> $A z/((x-x_0)^{2}+z^{2})$ to the profile and reports $z = 4.6$ km; explain why
> a different model gives a different depth from the same data. **(d)** Compute
> the half-width you would predict if the pipe were a line source, and state why
> the prediction may not match the map. **(e)** State one independent measurement
> that would settle the depth.

## Common pitfalls

1. **Tuning the structural index until the map looks right.** The index is a
   model choice; changing it changes the depth by tens of per cent (Section 1.2).
2. **Reporting an Euler depth without the smoothing length.** Smoothing broadens
   anomalies and biases the depth upward; the bias is measured, not hypothetical.
3. **Believing a Werner depth whose rational function does not fit.** The method
   will return a number from noise; the fit quality is the test.
4. **Applying the half-width rule to the wrong model.** A factor of two in the
   answer, for a dipole.
5. **Reading the spectral depth as a depth distribution.** It is one number from
   a weighted average, and it is only as good as the incoherent-source
   assumption.
6. **Combining methods without checking they agree for a defensible reason.**
   Agreement between two methods that share a model assumption is not evidence.

## Related modules

- [04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) — where the
  anomalies come from.
- [06 Magnetic Inversion](06-magnetic-inversion.md) — the general treatment of
  which depths the data can distinguish.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  the estimation theory behind every least-squares step here.
- [20-02 Fourier and Spectral Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/README.md) —
  spectral estimation, windowing and the resolution limits of the spectral
  method.
- [05-07 Interpretation and Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md) —
  how several methods are combined and reported.
