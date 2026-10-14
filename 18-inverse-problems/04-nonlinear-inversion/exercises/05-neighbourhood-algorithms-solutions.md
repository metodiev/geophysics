# Solutions — Neighbourhood and Very Fast Simulated Annealing

**1.1** The Voronoi cell of the best model $u_b$ is $\{u : \lVert u - u_b\rVert \le \lVert u - u_j\rVert \ \forall j\}$. Its inscribed ball has radius half the distance to the nearest sample, $r_{\text{ins}} = \tfrac12\min_{j\ne b}\lVert u_b - u_j\rVert$, because the bisecting hyperplane towards the nearest neighbour is the closest boundary of the cell.

**1.2** $\Delta u_i = \mathrm{sgn}(r_i - 0.5)\,T\left[(1 + 1/T)^{\lvert 2r_i - 1\rvert} - 1\right]$ with $r_i \sim U(0,1)$. As $T \to 0$, $1/T \to \infty$, so for any $r_i \ne 0.5$ the bracket becomes negligible unless $\lvert 2r_i-1\rvert$ is extremely small: the proposal concentrates on a very small neighbourhood with rare large jumps (a Cauchy-like tail).

**1.3** Radius 0.137896 to 0.000101, a factor $1.366\times10^{3}$; volume at $n = 2$ scales as $r^{2}$, so $1.87\times10^{6}$ — matching the printed factors $1.493\times10^{-2} \to 8.050\times10^{-9}$, i.e. $1.85\times10^{6}$.

**2.1** $V/V_{\text{box}} = \pi r^{2}/4$ for a square box of side 2. Generation 1: $\pi(0.137896)^2/4 = \pi(0.0190153)/4 = 0.014935$, printed 0.01493 — agreement to three figures. Generation 5: $\pi(0.000101)^2/4 = 8.01\times10^{-9}$, printed 8.050e-09 — agreement to two figures (the printed value uses the unrounded radius).

**2.2** $a = \exp(-0.3/T)$: at $T = 0.5$, $\exp(-0.6) = 0.5488$; at $T = 0.1$, $\exp(-3) = 0.04979$; at $T = 0.02$, $\exp(-15) = 3.059\times10^{-7}$.

**2.3** $T_k = 0.5(0.995)^k = 0.05$ gives $(0.995)^k = 0.1$, so $k = \ln 0.1/\ln 0.995 = -2.302585/(-0.0050125) = 459.4$, i.e. step 460. For $T = 0.01$: $(0.995)^k = 0.02$, $k = \ln 0.02/\ln 0.995 = 780.5$, i.e. step 781.

**3.1** Mechanism: the acceptance rate depends on the local improvement available, not on the cell size, because the proposal is always drawn around a model that was itself the best found so far; as long as the cell still straddles an improving direction the rate stays roughly constant, and once it does not, the rate collapses towards zero rather than the radius being the driver. Test: hold the radius fixed (draw from a fixed-radius ball around the best model) and measure the acceptance fraction. If it falls the same way, the radius is not the cause; if it stays high, the contraction is the cause.

**3.2** With a restart it is a different algorithm and must be measured as such. Run twelve times at 640 evaluations with the restart rule and twelve without, compute success rates and their standard errors $\sqrt{p(1-p)/12}$ (at $p = 0.25$ that is 0.125, so the difference must exceed roughly 0.25 to be resolved by twelve runs); if it does not, increase the number of runs or the budget before claiming a benefit.

**3.3** They cannot. Both methods define success as reaching a value within a tolerance of a reference minimum that the demo computed by dense local search on a declared function; on real data no reference minimum exists, so the quantity is undefined. What can be reported on real data is the best objective found, the model norm, the evaluation budget, the number of independent runs and their spread — the quantities the lesson's Section 7 tabulates — and none of those is a success rate.
