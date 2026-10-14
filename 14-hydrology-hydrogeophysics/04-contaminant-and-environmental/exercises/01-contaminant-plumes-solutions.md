# Solutions — 14-04-01 Contaminant Plumes and Their Geophysical Signature

> Read after attempting. Lesson:
> [01 Contaminant Plumes and Their Geophysical Signature](../01-contaminant-plumes.md).
> All models **SYNTHETIC**.

---

## ★1 — Retardation and solute velocity

$$R = 1 + \frac{\rho_b K_d}{\theta} = 1 + \frac{1.800 \times 0.02}{0.28}
= 1 + 0.12857 = 1.1286 .$$

$$\frac{v}{R} = \frac{0.060}{1.1286} = 0.0532\ \mathrm{m\,day^{-1}} .$$

**Units.** $\rho_b$ in $\mathrm{g\,cm^{-3}}$ ($1.800$) times $K_d$ in
$\mathrm{cm^{3}\,g^{-1}}$ ($0.02$) is dimensionless, and dividing by $\theta$
keeps it dimensionless, so the factor $1$ in $R = 1 + \ldots$ is legitimate. If
$\rho_b$ is left in $\mathrm{kg\,m^{-3}}$ and $K_d$ in $\mathrm{mL\,g^{-1}}$ the
product is 1000 times too large — the most common arithmetic error in this topic.

---

## ★2 — Front and width at 5 years

$t = 5\times365.25 = 1826.25$ days, $v_s = 0.0382\
\mathrm{m\,day^{-1}}$, $D_s = \alpha_L v_s = 0.03819\
\mathrm{m^{2}\,day^{-1}}$.

$$x_f = v_s t = 0.0382\times1826.25 = 69.7\ \mathrm{m},$$

$$w_{10\text{–}90} = 2.563\sqrt{2D_s t}
= 2.563\sqrt{2\times0.03819\times1826.25}
= 2.563\times11.81 = 30.3\ \mathrm{m}.$$

The width is $43\%$ of the travel distance — the plume is still young enough that
the transition zone is a large part of it.

---

## ★3 — Concentration to bulk resistivity

Background: $\sigma_w = 0.050\ \mathrm{S\,m^{-1}}$,
$\sigma_b = \phi^{m}\sigma_w/a = 0.09\times0.050 = 0.00450\
\mathrm{S\,m^{-1}}$, $\rho_b = 222.2\ \Omega\,\mathrm{m}$.

At $C = 300$ CU: $\sigma_w = 0.050 + 1.0\times10^{-4}\times300 = 0.0800\
\mathrm{S\,m^{-1}}$, $\sigma_b = 0.00720\ \mathrm{S\,m^{-1}}$,
$\rho_b = 138.9\ \Omega\,\mathrm{m}$.

**Assumption.** The conversion assumes a clean, clay-free matrix, full
saturation, a known and uniform porosity, and the linear
concentration–conductivity relation with the stated slope. Every one of these is
a model choice, not a measurement.

---

## ★★4 — Detection thresholds

**(a)** From $\Delta\rho/\rho = \Delta\sigma_w/\sigma_w$ and
$\Delta\sigma_w = \beta C$:

$$C_\text{min} = \frac{\varepsilon\,\sigma_{w0}}{\beta(1-\varepsilon)} ,
\qquad \varepsilon = \frac{\Delta\rho}{\rho}.$$

One sigma ($\varepsilon = 0.03$):
$C_\text{min} = 0.03\times0.050/[1.0\times10^{-4}\times0.97]
= 0.001500/9.70\times10^{-5} = 15.5$ CU.

Two sigma ($\varepsilon = 0.06$):
$C_\text{min} = 0.06\times0.050/(1.0\times10^{-4}\times0.94)
= 0.003000/9.40\times10^{-5} = 31.9$ CU.

**(b)** With $\sigma_{w0} = 0.500\ \mathrm{S\,m^{-1}}$ both thresholds are
multiplied by ten: $154.6$ CU and $319.1$ CU. The ratio is exactly $10$ in each
case, because $C_\text{min} \propto \sigma_{w0}$.

---

## ★★5 — A sensor at 30 m

**(a)** $t_\text{arrival} = 30/v_s = 30/0.0382 = 785.5$ days.

**(b)** Evaluating the step solution at $x = 30$ m and $t = 785.5$ days gives
$C = 550.7$ CU — slightly *above* the naive half-source value, because the second
term of the Ogata–Banks solution (the reflection at the inlet boundary) adds a
few per cent at this distance. Then
$\sigma_w = 0.050 + 1.0\times10^{-4}\times550.7 = 0.1051\
\mathrm{S\,m^{-1}}$, $\sigma_b = 0.09\times0.1051 = 0.009456\
\mathrm{S\,m^{-1}}$, and

$$\rho_b = \frac{1}{0.009456} = 105.8\ \Omega\,\mathrm{m} .$$

**(c)** 517 days later, $t = 1302.5$ days: $C = 983.1$ CU,
$\sigma_w = 0.1483\ \mathrm{S\,m^{-1}}$, $\rho_b = 74.9\
\Omega\,\mathrm{m}$.

The full change is from $222.2$ to $74.1\ \Omega\,\mathrm{m}$, i.e.
$148.1\ \Omega\,\mathrm{m}$. At arrival the change is
$222.2 - 105.8 = 116.4\ \Omega\,\mathrm{m}$, which is **$78.6\%$ of the full
change**; 517 days later it is $99.4\%$. **The arrival is fast and the
completion is slow**, which is exactly why the rising limb carries the transport
information and why a survey schedule clustered around $t_a$ is worth more than
one that continues long after.

---

## ★★6 — Three other mechanisms for a $2.5\times$ drop

| mechanism | independent measurement |
|---|---|
| clay-rich rock with fresh water | natural gamma, cation exchange capacity, or an NMR bound-fluid fraction |
| increased water saturation in the vadose zone | a fluid sample showing the pore-fluid conductivity unchanged |
| higher porosity (same fluid) | an independent porosity measurement (neutron, NMR, seismic) |

A metallic conductor body is a fourth possibility that is unlikely at this
magnitude but not impossible; it is separated by a strong induced-polarisation
phase and a magnetic response if the conductor is magnetic.

---

## ★★★7 — The threshold formula

Starting from $\sigma_w = \sigma_{w0} + \beta C$ and
$\sigma_b = \phi^{m}\sigma_w/a$ (so $\rho_b \propto 1/\sigma_w$):

$$\frac{\Delta\rho}{\rho} = -\frac{\Delta\sigma_w}{\sigma_w}
\;\;\Longrightarrow\;\;
\varepsilon = \frac{\beta C}{\sigma_{w0} + \beta C}
\;\;\Longrightarrow\;\;
\varepsilon\sigma_{w0} + \varepsilon\beta C = \beta C
\;\;\Longrightarrow\;\;
C = \frac{\varepsilon\sigma_{w0}}{\beta(1-\varepsilon)} .$$

**(a)** $C_\text{min} \propto \sigma_{w0}$ exactly. **Screening consequence:** a
fresh aquifer is a good target and a brackish one is a poor target, for reasons
that have nothing to do with the tracer. A feasibility study must use the site's
own background conductivity, measured, not assumed.

**(b)** As $\varepsilon \to 1$ the denominator vanishes and $C_\text{min} \to
\infty$. The limit is not physical because the linearisation of
$\Delta\rho/\rho = \Delta\sigma_w/\sigma_w$ (equivalently, the assumption that the
anomaly is a small perturbation) has already failed, and because a
concentration large enough to double the bulk conductivity would change the
survey's own sensitivity pattern — the linear detectability argument is a
*screening* tool, valid for small anomalies.

**(c)** The repeatability $\varepsilon$. Since $C_\text{min} \propto
\varepsilon$ for small $\varepsilon$, halving the noise halves the detectable
concentration. Note what does **not** help: more electrodes, a finer inversion
mesh or a lower regularization parameter, none of which changes the repeatability
of the measurement.

---

## ★★★8 — Monitoring design (model answer)

**(a) Saturation of the schedule.** The only informative part of the record is the
rising limb of the breakthrough curve, which occupies roughly the interval
between $0.2t_a$ and $2t_a$ around the arrival time $t_a$. Budget the surveys so
that at least four occupy that interval (for example at $0.5t_a$, $0.9t_a$,
$1.2t_a$, $1.6t_a$), with one before it to establish the background. Surveys
outside that window measure a constant and add nothing. A first estimate of
$t_a$ comes from a Darcy-flux calculation; if it is wrong by a factor of two the
schedule is corrected after the first arrival is seen.

**(b) Dense versus sparse.** A dense array over a small area near the source
resolves the plume's transverse width and the dispersive spread; a sparse array
along the flow direction, with a few stations far down-gradient, resolves the
advective travel time over a long baseline. Putting everything in the dense
array gives a good shape and a poor velocity; the far stations are what convert a
shape into a transport parameter.

**(c) Systematic errors removed by differencing:** the static electrode
positions and the array geometry (both of which cancel exactly), and any
time-invariant geological heterogeneity. **Not removed:** errors that change
between surveys — electrode coupling drift, a seasonally varying water table, or
a temperature change in the pore fluid, which changes its conductivity and thus
mimics a tracer. The last is the dangerous one and is why the differenced survey
must be accompanied by a fluid-temperature record.

**(d) Velocity resolution.** If the arrival time is determined to $\pm\Delta t$
and the path length is $L$, then $v = L/t$ gives
$\Delta v/v = \Delta t/t$. For $L = 30\ \mathrm{m}$,
$v_s = 0.0382\ \mathrm{m\,day^{-1}}$ ($t_a = 785.5$ days) and a survey schedule
that dates the crossing to $\pm30$ days:

$$\frac{\Delta v}{v} = \frac{30}{785.5} = 3.8\% , \qquad
\Delta v = 0.0382\times0.038 = 1.5\times10^{-3}\ \mathrm{m\,day^{-1}} .$$

Since $v_s = v/R$, a $3.8\%$ resolution in $v_s$ is a $3.8\%$ resolution in
$v$ only if $R$ is known; otherwise the measurement constrains $v/R$ and the
distinction is a model choice, not a measurement.
