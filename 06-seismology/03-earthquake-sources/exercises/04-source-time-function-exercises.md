# Exercises — 06-03-04 Source Time Functions, Rupture Kinematics and Directivity

Attempt these before reading the
[solutions](./04-source-time-function-solutions.md). The lesson is
[04 Source Time Functions, Rupture Kinematics and Directivity](../04-source-time-function.md)
and the demonstration is
[`../code/source_time_function_demo.py`](../code/source_time_function_demo.py).
All values are **SYNTHETIC**. Unless stated otherwise use the demo model:
$\beta = 3500\ \mathrm{m\,s^{-1}}$, $L = 30\ \mathrm{km}$,
$v_r = 2800\ \mathrm{m\,s^{-1}}$, $\tau_r = 1.00\ \mathrm{s}$.

## ★ Foundational

**★1.** Compute $L/v_r$ and $L/\beta$ in seconds, then the emission-time spans
$D(0^\circ)$, $D(90^\circ)$ and $D(180^\circ)$. State the unit of each.

**★2.** Add the rise time to the three spans to get the apparent durations, and
compute the forward/backward span ratio. Repeat the ratio *without* the rise
time and state how much the rise time reduces the contrast.

**★3.** Using $\sigma_{\text{delay}}\approx (L/\sqrt{12})\lvert1/v_r -
\cos\theta/\beta\rvert$, compute $\sigma_{\text{delay}}$ at $0^\circ$, $90^\circ$
and $180^\circ$, and compare with the demo's discrete values $0.6201$, $3.1007$
and $5.5812\ \mathrm{s}$.

## ★★ Applied

**★★4.** With $\sigma_{\text{wavelet}} = 0.8660\ \mathrm{s}$, predict the
incoherent width $\sigma_{\text{total}}$ at $90^\circ$ and compare with the
demo's measured $2.9039\ \mathrm{s}$. Express the discrepancy as a percentage and
state the physical reason for its sign.

**★★5.** Derive $\sigma_{\text{wavelet}} = (\sqrt3/2)\tau_r$ for the wavelet
$w(t) = (t/\tau_r)e^{-t/\tau_r}$ ($t>0$) using the energy density $w^{2}$.

**★★6.** The demo reports a forward/backward rms duration ratio of $5.4171$, a
peak amplitude ratio of $0.1671$ and a closed-form span ratio of $6.4545$.
Explain in three sentences why these three numbers are all different, and which
one is a property of the emission-time *support* rather than of the second moment.

**★★7.** Using the demo's $f_c/f_c(90^\circ)$ ratios ($2.9792$ at $0^\circ$,
$0.6349$ at $135^\circ$, $0.5500$ at $180^\circ$), compute the point-source
stress-drop error factor $(f_c/f_c(90^\circ))^{3}$ at each azimuth and the ratio
between the largest and smallest.

## ★★★ Research-oriented

**★★★8.** Design an inversion of apparent duration versus azimuth to recover
$L$ and $v_r$ from a single earthquake. Specify the station distribution, the
forward relation, the parameters you would solve for, and the *non-uniqueness*
you expect (in particular, which combinations of $L$, $v_r$ and $\tau_r$ give
the same curve). State clearly how many stations you need and why.

**★★★9.** The model is a *line* source. Argue how a rupture of down-dip width
$W$ comparable to $L$ changes the directivity pattern, and design a numerical
experiment using the demo's superposition machinery to measure the change in the
forward/backward rms ratio as a function of $W/L$. Predict the sign of the effect.

**★★★10.** Apparent duration measured at a station is the convolution of the
source duration with the medium's attenuation operator, which also broadens the
pulse. Design an experiment to separate the two, specifying the observable, the
model you would fit, and the frequency band in which you predict the separation
to be best. A specification that could not be executed is a failed answer.
