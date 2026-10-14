# Exercises — 13-04-04 Interseismic Coupling and Megathrust Locking

Attempt these before reading the
[solutions](04-interseismic-coupling-solutions.md). The lesson is
[04 Interseismic Coupling and Megathrust Locking](../04-interseismic-coupling.md).
All models and data in this module are **SYNTHETIC**.

Use $V = 40\ \mathrm{mm\,yr^{-1}}$ as the default long-term rate,
$\mu = 30\ \mathrm{GPa}$, $1\ \mathrm{mm\,yr^{-1}} = 1\ \mathrm{km\,Myr^{-1}}$,
and $M_w = \tfrac23(\log_{10}M_0 - 9.1)$.

## ★ Foundational

**★1.** For a single patch with $\chi = 1$ locked from $0$ to
$d = 25\ \mathrm{km}$ and $V = 40\ \mathrm{mm\,yr^{-1}}$, evaluate the profile
$v(x) = V/2 - (\chi V/\pi)\operatorname{atan2}(d,x)$ at $x = 5$, $25$ and
$100\ \mathrm{km}$, and state the far-field value.

**★2.** For the same patch, compute the **relative** velocity across the fault
trace (the limit $x\to0^+$ minus $x\to0^-$) and compare with $V(1-\chi)$.

**★3.** State the units of the kernel
$\left[\operatorname{atan2}(z_{j+1},x) - \operatorname{atan2}(z_j,x)\right]/\pi$
and explain why the model's output is in $\mathrm{mm\,yr^{-1}}$ when it is
multiplied by $V$.

## ★★ Applied

**★★4.** Two SYNTHETIC models: A with $\chi = 1$ from $0$ to $20\ \mathrm{km}$,
B with $\chi = 0.6$ from $0$ to $40\ \mathrm{km}$, both with $V = 40\
\mathrm{mm\,yr^{-1}}$. Compute the profiles at $x = 5$, $20$, $50$ and
$200\ \mathrm{km}$ and state the smallest $\lvert x\rvert$ at which the two
differ by less than $1\ \mathrm{mm\,yr^{-1}}$.

**★★5.** A network has stations at $x = 8$, $25$ and $90\ \mathrm{km}$ with
$1\ \mathrm{mm\,yr^{-1}}$ noise. Using ★4's numbers, state which pairs of
$(d, \chi)$ can and cannot be distinguished, and what single additional station
would most improve the discrimination.

**★★6.** Compute the moment deficit rate for $L = 250\ \mathrm{km}$,
$V = 50\ \mathrm{mm\,yr^{-1}}$, $\mu = 30\ \mathrm{GPa}$ and a coupled depth
extent of $30\ \mathrm{km}$. Then compute the $50$-year magnitude and the
magnitude change if the coupled extent is revised to $20\ \mathrm{km}$.

**★★7.** Explain why the kernel for a patch at depth $z_j$ is approximately
$\frac{1}{\pi}\arctan(x/z_j)$ in the far field, and use it to explain
quantitatively why a deep patch requires stations at $\lvert x\rvert \gtrsim z_j$
to be resolved.

## ★★★ Research-oriented

**★★★8.** The lesson's inversion uses a first-difference smoothness operator with
weight $\lambda = 2.0\ \mathrm{mm\,yr^{-1}}$ per unit coupling. Write the
damped inverse problem explicitly, derive the resolution matrix
$R = (G^{\mathsf T}G)^{-1}K^{\mathsf T}K$ with $G = [K; \lambda D]$, and explain
how $\lambda$ trades the resolution diagonal against the parameter standard
deviation. State what $\lambda \to 0$ and $\lambda \to \infty$ give.

**★★★9.** Design a SYNTHETIC experiment to determine the smallest coupled depth
extent that a given network can resolve, specifying the network geometry, the
noise model, the model family, the metric (resolution diagonal or $\Delta
\chi^{2}$ contours), and the expected scaling of the resolution with the
closest-station distance. A specification that could not be executed is a failed
answer.
