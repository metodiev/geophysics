---
id: 06-10-02
title: "Delay-Time (Plus-Minus) Methods and Depth Estimation"
level: advanced
prereqs: ["06-10-01", "06-02-03"]
tags: [seismology, near-surface, delay-time, plus-minus, refraction, uncertainty]
---

# Delay-Time (Plus-Minus) Methods and Depth Estimation

> **All models and data in this module are SYNTHETIC.** The velocities, the
> undulating refractor, the spreads and the picking errors are chosen teaching
> values. No field survey, site or borehole is referred to.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the forward and reverse head-wave times
   $t_f(x) = x/v_2 + d(0) + d(x)$ and $t_r(x) = (L-x)/v_2 + d(L) + d(x)$ from the
   ray geometry, with the delay time $d(x) = z(x)\cos i_c/v_1$.
2. **Show** that the reciprocal time is the sum of the two end delays, and
   **derive** the plus term $d(x) = \tfrac12[t_f(x)+t_r(x)-T]$.
3. **Derive** the minus term and show that its slope is $2/v_2$, so that the
   refractor velocity is obtained independently of the reciprocal time.
4. **Convert** a delay time into a depth, and **derive** the exact logarithmic
   sensitivities $1.0667$ and $-0.0667$ of the depth to the two velocities for a
   stated model.
5. **Propagate** a picking error into a depth error, and **verify** the analytic
   propagation against a Monte Carlo simulation.
6. **Quantify** two violated assumptions: a lateral change in overburden
   velocity, and a datum that is not the ground surface.
7. **State** why the depth from a delay time is conditional on the overburden
   velocity, and what measurement would remove that condition.

## Prerequisites

- [01 Refraction Survey Geometry and Travel-Time Interpretation](01-refraction-basics.md) —
  the head-wave equation, the intercept time and the crossover distance.
- [06-02-03 The tau-p Transform and Intercept Time](../02-ray-theory-and-travel-times/03-tau-p.md) —
  the slowness-domain view of the same quantities, which makes the delay time a
  natural observable rather than a trick.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  the picking and bookkeeping this method depends on.

## 1. Intuition: from one number to a depth under every receiver

Lesson 01 produced three numbers — $v_1$, $v_2$ and one depth — and it did so by
assuming a flat interface everywhere. Real refractors undulate, and an engineer
who is deciding where to put a footing wants to know where, not the average.

The delay-time idea is a change of bookkeeping that costs almost nothing. Shoot
the line twice, once from each end. For every receiver you now have two arrival
times instead of one, plus one number you can read off either record: the time at
the far shot point, seen from the other shot. Those three numbers per receiver
determine the depth beneath that receiver, with no assumption about the shape of
the interface between receivers.

The two shots give two combinations that do different jobs, and the names are
older than the arithmetic:

- the **minus term** $t_f(x) - t_r(x)$ removes the depth and leaves the velocity;
- the **plus term** $t_f(x) + t_r(x)$ removes the velocity and leaves the depth.

Both are ordinary differences and sums of picked times. The whole method lives in
knowing *which* linear combination of picks cancels which unknown — the same
question that dominates every inverse problem in this curriculum.

## 2. Precise definitions

| Quantity | Symbol | Definition | Unit |
|---|---|---|---|
| spread | $L$ | distance between the two shot points | m |
| forward time | $t_f(x)$ | first arrival from the shot at $x=0$ | s |
| reverse time | $t_r(x)$ | first arrival from the shot at $x=L$ | s |
| reciprocal time | $T$ | $t_f(L) = t_r(0)$ | s |
| delay time | $d(x)$ | $z(x)\cos i_c/v_1$ | s |
| depth-to-delay factor | $v_1/\cos i_c$ | converts $d$ into depth | m s$^{-1}$ |

The **delay time** $d(x)$ has a name that hides a simple meaning: it is the extra
time the head wave spends in the overburden above receiver $x$, compared with a
ray that would have travelled the same horizontal distance at the refractor
speed. It is a time, not a depth, and the conversion between the two is exactly
the factor $v_1/\cos i_c$ — which for the synthetic model below is
$600/0.968246 = 619.6773\ \mathrm{m\,s^{-1}}$.

## 3. Derivations

### 3.1 Forward and reverse head-wave times

Let the refractor be at depth $z(x)$ beneath a flat surface, with uniform
overburden $v_1$ and uniform refractor $v_2$. Splitting the ray at the refractor,
each end contributes one delay time and the middle leg travels at $v_2$:

$$t_f(x) = \frac{x}{v_2} + d(0) + d(x), \qquad
t_r(x) = \frac{L-x}{v_2} + d(L) + d(x).$$

The middle leg needs no knowledge of the interface shape: the along-refractor
distance is adjusted automatically because the two diagonal legs project onto
$z(0)\tan i_c$ and $z(x)\tan i_c$ on their respective ends. This is why the
method tolerates an undulating refractor but not a varying $v_1$.

### 3.2 The reciprocal time and the plus term

Adding the two expressions,

$$t_f(x) + t_r(x) = \frac{L}{v_2} + d(0) + d(L) + 2d(x) = T + 2d(x),$$

because $T \equiv t_f(L) = t_r(0) = L/v_2 + d(0) + d(L)$. Hence

$$\boxed{\;d(x) = \tfrac{1}{2}\left[t_f(x) + t_r(x) - T\right],\qquad
z(x) = \frac{v_1}{\cos i_c}\, d(x).\;}$$

The plus term is thus a *depth profile*, receiver by receiver, and it needs the
reciprocal time $T$ as one further observable. Reciprocity is not an
assumption here: it is a consequence of the wave equation for a reciprocal
source–receiver pair, and a measured disagreement is a measurement of error
(Section 5).

### 3.3 The minus term gives the velocity

Subtracting,

$$t_f(x) - t_r(x) = \frac{2x - L}{v_2} + d(0) - d(L),$$

a straight line in $x$ with slope $2/v_2$. Therefore

$$\boxed{\;v_2 = \frac{2}{\text{slope of } [t_f - t_r]\text{ against } x}.\;}$$

Two consequences matter. The unknown depths cancel *exactly*, so the refractor
velocity is obtained without any assumption about its shape; and the two picks
at the same receiver are differenced, so a constant timing offset (a trigger
delay, a clock error) cancels too. Only the random part of the picking error
survives.

### 3.4 How much does a wrong velocity cost?

Write $h = d\, v_1/\cos i_c$ with
$\cos i_c = \sqrt{1 - (v_1/v_2)^{2}}$ and hold the measured delay $d$ fixed.
Logarithmic differentiation gives the exact result

$$\frac{\partial \ln h}{\partial \ln v_1}
= 1 + \frac{(v_1/v_2)^{2}}{1 - (v_1/v_2)^{2}}, \qquad
\frac{\partial \ln h}{\partial \ln v_2}
= -\frac{(v_1/v_2)^{2}}{1 - (v_1/v_2)^{2}}.$$

For the demonstration's $v_1/v_2 = 0.25$ these are $+1.0667$ and $-0.0667$,
exactly the numbers the demonstration prints from its Jacobian. Two statements
follow:

- **the depth is about 16 times more sensitive to the overburden velocity than to
  the refractor velocity**, which is the opposite of the usual intuition. The
  reason is that $\cos i_c \approx 1$, so the depth is essentially
  $d\,v_1$: the refractor velocity enters only through the small correction
  $\cos i_c$;
- **the refractor velocity is the parameter you can measure well and the
  overburden velocity is the one you must know independently.** A direct-wave
  pick on the near branch, or a borehole, is what supplies it.

### 3.5 End-to-end example

Using the demonstration's SYNTHETIC model in Section 4, the delay-time chain
reproduces the true depths to $6.2\times10^{-15}\ \mathrm{m}$ in maximum
absolute error and $2.2\times10^{-15}\ \mathrm{m}$ in RMS. That is not a
coincidence: the forward model and the inversion are the same three equations,
so this experiment measures the *arithmetic*, and it sets the baseline that
Sections 5–6 then perturb.

## 4. The synthetic model and its exact times

The demonstration uses $v_1 = 600\ \mathrm{m\,s^{-1}}$,
$v_2 = 2400\ \mathrm{m\,s^{-1}}$, a spread $L = 120\ \mathrm{m}$, 232 receivers
at $0.5\ \mathrm{m}$ spacing, and a sinusoidally undulating refractor

$$z(x) = 6 + 4\sin\!\left(\frac{2\pi x}{120}\right)\ \mathrm{m},$$

ranging from $2.000\ \mathrm{m}$ at $x = 90\ \mathrm{m}$ to $10.000\ \mathrm{m}$ at
$x = 30\ \mathrm{m}$. $\cos i_c = 0.968246$, the depth-to-delay factor is
$0.001613743\ \mathrm{s\,m^{-1}}$, and the delay times span $3.2275$ to
$16.1374\ \mathrm{ms}$.

| $x$ (m) | $t_f$ (ms) | $t_r$ (ms) | $z_{\text{true}}$ (m) |
|---|---|---|---|
| 0 | 19.36492 | 69.36492 | 6.000 |
| 20 | 33.28842 | 66.62175 | 9.464 |
| 40 | 41.62175 | 58.28842 | 9.464 |
| 60 | 44.36492 | 44.36492 | 6.000 |
| 80 | 47.10808 | 30.44141 | 2.536 |
| 100 | 55.44141 | 22.10808 | 2.536 |
| 120 | 69.36492 | 19.36492 | 6.000 |

Three features of this table are worth reading before doing any arithmetic. At
$x = 60\ \mathrm{m}$ the two shots give the *same* time, because the receiver sits
at the midpoint of the spread and the two paths differ only beyond it. At
$x = 0$ the forward shot records the direct arrival at $19.36\ \mathrm{ms}$
while the reverse shot records the head wave from the far end at
$69.36\ \mathrm{ms}$: the same receiver, two different branches. And the
intercept-time estimate $\tfrac12[t_f + t_r]$ is not the quantity used — the
reciprocal time must be subtracted.

### Worked example — depth beneath the receiver at $x = 20$ m

1. **Reciprocal time.** $T = t_f(120) = 69.36492\ \mathrm{ms}$, which equals
   $t_r(0)$ to all printed digits.
2. **Plus term.** $t_f(20) + t_r(20) = 33.28842 + 66.62175 = 99.91017\
   \mathrm{ms}$.
3. **Delay time.** $d(20) = \tfrac12(99.91017 - 69.36492) = 15.272625\
   \mathrm{ms}$.
4. **Depth.** $z(20) = 619.6773 \times 15.272625\times10^{-3} = 9.464\
   \mathrm{m}$.
5. **Check.** $6 + 4\sin(2\pi\cdot20/120) = 6 + 4\sin 60^\circ = 9.464\
   \mathrm{m}$. ✔

At the deepest point $x = 30\ \mathrm{m}$ the same chain gives
$z = 10.000\ \mathrm{m}$, and at the shallowest $x = 90\ \mathrm{m}$ it gives
$z = 2.000\ \mathrm{m}$: the delay time is a *profile*, not a constant.

## 5. Reciprocity as a measurement of error

The exact model satisfies $t_f(L) = t_r(0)$ identically; the demonstration prints
$69.364916731\ \mathrm{ms}$ for both and a misfit of $0.000\times10^{0}\
\mathrm{s}$. Add independent picking noise of $\sigma = 1\ \mathrm{ms}$ to the two
shot-point picks, and the difference becomes a random variable with zero mean and
standard deviation $\sqrt{2}\,\sigma$:

| $\sigma$ (ms) | measured misfit (ms) | predicted $\sqrt{2}\sigma$ (ms) |
|---|---|---|
| 1.0 | $-0.0713 \pm 1.4187$ | 1.4142 |
| 2.0 | $-0.0115 \pm 2.8269$ | 2.8284 |

The prediction is a one-line derivation: the difference of two independent picks
of the same arrival has variance $2\sigma^{2}$. The practical value is that a
real survey's reciprocal misfit *is* a noise estimate — a free, in-situ error bar
that no repeat shots are needed to obtain.

## 6. Error propagation: from picks to a depth profile

### 6.1 The plus term

$d = \tfrac12(t_f + t_r - T)$, and if $T$ is itself estimated as the mean of two
picks, $\sigma_T^{2} = \sigma^{2}/2$. Propagating,

$$\sigma_d^{2} = \frac{1}{4}\left(\sigma^{2} + \sigma^{2}
+ \frac{\sigma^{2}}{2}\right) = \frac{2.5}{4}\,\sigma^{2} = 0.625\,\sigma^{2},$$

so $\sigma_d = 0.79\,\sigma$ and the depth error is
$\sigma_z = 619.6773 \times 0.79\,\sigma$. The demonstration measures it:

| $\sigma$ (ms) | RMS depth error (m) | analytic (m) | ratio |
|---|---|---|---|
| 1.0 | 0.4894 | 0.4899 | 0.999 |
| 2.0 | 0.9564 | 0.9798 | 0.976 |
| 5.0 | 2.4103 | 2.4495 | 0.984 |

The ratio drifts below 1 as the noise grows because $\sigma_z$ is quoted as an
RMS over receivers while the delay-time conversion also inherits the *velocity*
error, which is itself $\sigma$-dependent and correlated between receivers. A
sub-centimetre depth error from a $1\ \mathrm{ms}$ pick is remarkable and is
exactly why the method is used: the head wave averages over the overburden
instead of measuring it pointwise.

### 6.2 The two-layer fit and its error ellipse

For a *flat* model ($v_1 = 600$, $v_2 = 2400$, $h = 10\ \mathrm{m}$, crossover
$25.8199\ \mathrm{m}$, 11 near-branch and 47 far-branch picks), the least-squares
covariance of the fitted branches together with the Jacobian of
$h = t_i v_1 v_2/(2\sqrt{v_2^{2}-v_1^{2}})$ gives

| $\sigma$ (ms) | method | $\sigma_{v_1}$ (m/s) | $\sigma_{v_2}$ (m/s) | $\sigma_h$ (m) | corr$(v_1,h)$ |
|---|---|---|---|---|---|
| 1.0 | predicted | 17.162 | 30.970 | 0.3311 | 0.932 |
| 1.0 | measured | 17.340 | 31.272 | 0.3323 | 0.932 |
| 2.0 | predicted | 34.325 | 61.939 | 0.6621 | 0.931 |
| 2.0 | measured | 34.526 | 61.845 | 0.6586 | 0.931 |

Three readings of this table:

- **the depth error is sub-metre for a $1\ \mathrm{ms}$ pick** in this geometry;
- **$v_1$ and $h$ are $93\%$ correlated**, and the $95\%$ error ellipse has
  semi-axes $0.641$ and $3.402$ in units of $\sigma_{v_1}$ and $\sigma_h$, with
  its major axis at $+45^\circ$. The quoted $95\%$ interval at $\sigma = 1\
  \mathrm{ms}$ is $v_1 = 600.0 \pm 34.68\ \mathrm{m\,s^{-1}}$ and
  $h = 10.00 \pm 0.665\ \mathrm{m}$ — but that joint statement is a rectangle
  around a tilted ellipse, so most of its corners are configurations the data
  exclude. **A depth and a velocity are one measurement with two names until
  something else breaks the correlation**;
- the analytic prediction matches the Monte Carlo to a few per cent, so the
  propagation needs no simulation once the survey geometry is fixed.

## 7. Two violated assumptions, quantified

### 7.1 A lateral change in the overburden velocity

Suppose $v_1 = 600\ \mathrm{m\,s^{-1}}$ for $x < 60\ \mathrm{m}$ and
$750\ \mathrm{m\,s^{-1}}$ beyond, while the interpretation assumes $600\
\mathrm{m\,s^{-1}}$ everywhere. The method's own sensitivity, $+1.0667$ in
logarithmic terms, predicts a depth bias of the order of the velocity error, and
the demonstration measures

| $x$ (m) | $z_{\text{true}}$ (m) | $z_{\text{interpreted}}$ (m) | bias (m) |
|---|---|---|---|
| 65.0 | 4.96 | 3.90 | $-1.07$ |
| 85.0 | 2.14 | 1.68 | $-0.46$ |
| 100.0 | 2.54 | 1.99 | $-0.55$ |

with a maximum absolute bias of $1.291\ \mathrm{m}$. The bias is largest where the
refractor is deep, because the delay time is proportional to the depth and the
velocity error multiplies it. Nothing in the data announces the error: the plus
term is a smooth profile computed from smooth picks. The only defences are an
independent measurement of $v_1$ (a borehole, a downhole measurement, or a
careful direct-wave fit over short offsets) and a survey designed so that the
overburden is sampled where it changes.

### 7.2 Topography and the reference datum

Let the ground rise linearly by $4\ \mathrm{m}$ across the spread while the
refractor stays flat in absolute terms. A delay time measures a time, and
converting it gives a depth **below the receiver**, because that is where the
ray's two ends are. The demonstration's elevations run from $0.133$ to
$3.983\ \mathrm{m}$, and reporting the result as depth below a datum is wrong by
exactly the elevation:

| $x$ (m) | depth below ground (m) | elevation (m) | error if reported below datum (m) |
|---|---|---|---|
| 4 | 6.832 | 0.133 | 0.133 (2%) |
| 119.5 | 5.895 | 3.983 | 3.983 |

The maximum error, $3.983\ \mathrm{m}$, is larger than the depth error from a
$5\ \mathrm{ms}$ pick by a factor of $1.6$. **Topography is not a correction to
be applied at the end; it is part of the definition of the output**, and a
delivery that does not state its datum is not interpretable.

## 8. Assumptions and regime of validity

1. **Two layers, each with a laterally constant velocity.** Section 7.1 measures
   the cost of violating the constancy; a three-layer site needs the delay-time
   decomposition applied per interface, not to the first arrivals as a whole.
2. **Velocity increasing with depth at the refractor.** The method inherits the
   blind zone of Lesson 01: a low-velocity layer is not merely poorly resolved, it
   is absent from the data.
3. **The refractor velocity is measured, not assumed.** The minus term delivers it
   from the data; if the minus term is not available (a single-ended spread), $v_2$
   becomes an assumption and the depth inherits its error.
4. **The overburden velocity must come from somewhere else.** It is the dominant
   term in the depth error (Section 3.4) and no property of the head wave
   determines it. This is the honest difficulty of the method.
5. **Small dip.** The derivation assumes a horizontal interface. Moderate dip
   changes the two end delays asymmetrically; the plus term then returns an
   *apparent* depth profile that must be corrected, and the correction requires
   both apparent velocities — the standard reason to shoot reversed.
6. **Ray theory.** The head wave is treated as a ray. At offsets comparable to a
   wavelength, or where the refractor is only a fraction of a wavelength below
   the surface, the first arrival is a diffracted or interfering wavefield and
   the delay-time equations no longer describe it (Lesson 06 gives the
   quarter-wavelength numbers).
7. **Pick times are the only random errors, and they are independent.**
   Correlation between picks (a mis-set trigger, a drifting clock) cancels
   partially in the minus term and not at all in the plus term — which is why a
   reciprocal misfit is checked *before* any depth is computed.

## Mastery checkpoint

Using the demonstration's model ($v_1 = 600\ \mathrm{m\,s^{-1}}$,
$v_2 = 2400\ \mathrm{m\,s^{-1}}$, $L = 120\ \mathrm{m}$):

**(a)** Compute the delay time and depth at $x = 100\ \mathrm{m}$ from
$t_f = 55.44141\ \mathrm{ms}$, $t_r = 22.10808\ \mathrm{ms}$ and
$T = 69.36492\ \mathrm{ms}$. Compare with $z(100) = 6 + 4\sin(2\pi\cdot100/120)$.
**(b)** Derive $\partial \ln h/\partial \ln v_1$ for arbitrary $v_1/v_2$ and
evaluate it at $v_1/v_2 = 0.25$.
**(c)** A 20% error in $v_1$ is present. Predict the depth bias at
$x = 100\ \mathrm{m}$ to two significant figures.
**(d)** The reciprocal misfit on a real line is $1.5\ \mathrm{ms}$. Estimate the
pick standard deviation and the depth standard deviation.
**(e)** State two measurements that would remove the overburden-velocity
condition, and say for each what it costs.

A worked version is in the
[solutions](exercises/02-plus-minus-method-solutions.md).

## Common pitfalls

1. **Using $\tfrac12(t_f+t_r)$ as the delay time.** The reciprocal time must be
   subtracted; omitting it adds $T/2 \approx 35\ \mathrm{ms}$ to every delay, i.e.
   tens of metres of spurious depth.
2. **Computing $v_2$ from the slope of $t_f$ alone.** Only the *difference* of the
   forward and reverse picks cancels the depth; a one-sided slope measures an
   apparent velocity that includes the interface shape.
3. **Treating the two branches as one curve.** The near offsets are usually direct
   arrivals. Mixing them into the far-branch fit biases $v_2$ low and the depth
   high.
4. **Forgetting the datum.** Section 7.2's $3.983\ \mathrm{m}$ error comes from a
   plausible hill and no arithmetic mistake.
5. **Reporting a depth without its $v_1$.** The depth–velocity correlation is
   $0.93$; the two are not independent numbers and a rectangle around a tilted
   ellipse misrepresents the uncertainty.
6. **Assuming reciprocity rather than measuring it.** It is a check with a free
   error bar, and skipping it discards the only in-situ noise estimate the survey
   provides.
7. **Applying the method across a three-layer site.** The plus term then contains
   the delays of both interfaces, and the single-interface conversion to depth is
   wrong by the depth of the ignored layer.

## Related modules

- [01 Refraction Survey Geometry and Travel-Time Interpretation](01-refraction-basics.md) —
  the two-layer baseline and the blind zone this method inherits.
- [03 Refraction Tomography and First-Arrival Inversion](03-tomography-refraction.md) —
  what to do when neither a flat nor a single interface is defensible, and how
  coverage replaces the delay-time decomposition.
- [06-02-03 The tau-p Transform and Intercept Time](../02-ray-theory-and-travel-times/03-tau-p.md) —
  the systematic version of the same linear combinations.
- [06-04-01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](../04-earthquake-location-and-magnitude/01-hypocentre-location.md) —
  the same least-squares covariance and error-ellipse bookkeeping applied to
  earthquake locations.
- [10-04-03 Near-Surface Refraction for Static Corrections](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/03-refraction-static.md) —
  delay times used as statics for a reflection survey, where their error becomes a
  mis-tie.

## Code and exercises

The demonstration for this lesson is
[`code/delay_time_demo.py`](code/delay_time_demo.py):

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python delay_time_demo.py
```

It prints every number quoted here, with units, and exits 0.

Exercises:
[`exercises/02-plus-minus-method-exercises.md`](exercises/02-plus-minus-method-exercises.md);
worked solutions:
[`exercises/02-plus-minus-method-solutions.md`](exercises/02-plus-minus-method-solutions.md).
Module overview: [`README.md`](README.md).
