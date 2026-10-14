"""Geodynamic model-data comparison: seafloor depth and heat flow versus age (SYNTHETIC).

Half-space-cooling and plate models of oceanic lithosphere are compared with
synthetic bathymetry and heat flow: parameter estimation, systematic residuals,
the trade-off between ridge depth and subsidence rate, and what each observable
resolves. Print-only: no files, no plots, no network.
"""
import numpy as np

rng = np.random.default_rng(20261014)
KAPPA, RHO_M, RHO_W, ALPHA, TM, CONDUCT = 1.0e-6, 3300.0, 1030.0, 3.0e-5, 1300.0, 3.2
MYR = 3.1557e13
L_TRUE, D_RIDGE = 95.0e3, 2500.0
NSER = 400

print("=" * 74)
print("SYNTHETIC geodynamic model-data comparison: seafloor depth and heat flow")
print("=" * 74)

def plate_profile(L, t):
    """Depth-integrated temperature deficit of the plate model, in metres of subsidence
    (excluding the ridge offset), from T(z,t) = T_m[z/L + (2/pi) sum sin(n pi z/L)/n exp(...)]."""
    tt = np.atleast_1d(t) * MYR
    n = np.arange(1, NSER + 1)
    odd = n % 2 == 1
    s = np.zeros_like(tt, dtype=float)
    for n0 in n[odd]:
        s += np.exp(-(n0 * np.pi / L) ** 2 * KAPPA * tt) / n0 ** 2
    deficit = TM * (L / 2.0 - 4.0 * L / np.pi ** 2 * s)          # K m
    return (RHO_M * ALPHA / (RHO_M - RHO_W)) * deficit            # m

def halfspace_depth(t, a, d0):
    return d0 + a * np.sqrt(np.atleast_1d(t))

def plate_depth(t, c, d0, L):
    return d0 + c / (plate_ref(L)) * plate_profile(L, t)

def plate_ref(L):
    return (RHO_M * ALPHA * TM * L / 2.0) / (RHO_M - RHO_W)

def heat_flow(L, t):
    """Surface heat flow in mW/m2, from q = k T_m (1 + 2 sum exp(-(n pi/L)^2 kappa t))/L."""
    tt = np.atleast_1d(t) * MYR
    s = np.zeros_like(tt, dtype=float)
    for n0 in np.arange(1, NSER + 1):
        s += np.exp(-(n0 * np.pi / L) ** 2 * KAPPA * tt)
    return 1000.0 * CONDUCT * TM * (1.0 + 2.0 * s) / L             # mW/m2

A_TRUE = 2 * RHO_M * ALPHA * TM * np.sqrt(KAPPA / np.pi) / (RHO_M - RHO_W) * np.sqrt(MYR)
print("\n1. The models")
print(f"  half-space cooling:  depth = d_ridge + a.sqrt(t),  a_theory = {A_TRUE:.1f} m/Myr^0.5")
print(f"  plate model:         same cooling but a fixed base T = T_m at {L_TRUE/1000:.0f} km")
print(f"  parameters: kappa = {KAPPA:.1e} m2/s, alpha = {ALPHA:.1e} /K, T_m = {TM:.0f} C,")
print(f"              rho_m = {RHO_M:.0f}, rho_w = {RHO_W:.0f} kg/m3, k = {CONDUCT} W/m/K")
print(f"  ridge depth {D_RIDGE:.0f} m; plate-model saturation subsidence "
      f"{plate_ref(L_TRUE):.0f} m at t -> infinity")

ages = np.linspace(2.0, 160.0, 60)
d_true = D_RIDGE + plate_profile(L_TRUE, ages)
q_true = heat_flow(L_TRUE, ages)
sig_d, sig_q = 100.0, 0.05
d_obs = d_true + rng.normal(0.0, sig_d, ages.size)
q_obs = q_true * (1.0 + rng.normal(0.0, sig_q, ages.size))
print("\n2. Synthetic observations (the truth is the plate model above)")
print(f"  bathymetry: {ages.size} ages {ages[0]:.0f}-{ages[-1]:.0f} Myr, "
      f"depth {d_obs.min():.0f}-{d_obs.max():.0f} m, noise {sig_d:.0f} m rms")
print(f"  heat flow:  same ages, {q_obs.max():.1f}-{q_obs.min():.1f} mW/m2 "
      f"(decreasing with age), multiplicative noise {sig_q*100:.0f}% rms")

def lsq_linear(basis, y, sigma):
    """Weighted linear least squares for y = sum_k beta_k basis_k, with covariance."""
    A = np.column_stack(basis)
    ATA_inv = np.linalg.inv(A.T @ A)
    beta = ATA_inv @ (A.T @ y)
    cov = sigma ** 2 * ATA_inv
    res = y - A @ beta
    return beta, cov, res

beta_h, cov_h, res_h = lsq_linear([np.ones(ages.size), np.sqrt(ages)], d_obs, sig_d)
print("\n3. Half-space cooling fitted to the bathymetry")
print(f"  d_ridge = {beta_h[0]:.0f} +/- {np.sqrt(cov_h[0,0]):.0f} m "
      f"(true {D_RIDGE:.0f}), a = {beta_h[1]:.1f} +/- {np.sqrt(cov_h[1,1]):.1f} m/Myr^0.5 "
      f"(true {A_TRUE:.1f})")
print(f"  residual rms {res_h.std():.1f} m against a noise level of {sig_d:.0f} m "
      f"-> misfit chi2/dof = {np.mean(res_h**2)/sig_d**2:.2f}")
print(f"  systematic residual (mean of the 10 lowest / middle 10 / highest 10 ages): "
      f"{res_h[:10].mean():+.0f} / {res_h[25:35].mean():+.0f} / {res_h[-10:].mean():+.0f} m")
print(f"  correlation between the d_ridge and a estimates: "
      f"{cov_h[0,1]/np.sqrt(cov_h[0,0]*cov_h[1,1]):+.2f}")

L_grid = np.linspace(60e3, 160e3, 101)
best = None
for L in L_grid:
    bb, cc, rr = lsq_linear([np.ones(ages.size), plate_profile(L, ages) / plate_ref(L)],
                            d_obs, sig_d)
    chi = np.mean((rr / sig_d) ** 2)
    if best is None or chi < best[0]:
        best = (chi, L, bb, rr)
chi_p, L_fit, beta_p, res_p = best
amp_p = beta_p[1]
print("\n4. Plate model fitted to the same bathymetry (1-D grid search over L)")
print(f"  L = {L_fit/1000:.1f} km (true {L_TRUE/1000:.0f} km, grid step "
      f"{(L_grid[1]-L_grid[0])/1000:.1f} km) -> the base of the plate is resolved to "
      f"{abs(L_fit-L_TRUE)/1000:.1f} km")
print(f"  d_ridge = {beta_p[0]:.0f} m, saturation subsidence {amp_p:.0f} m "
      f"(true {plate_ref(L_TRUE):.0f} m)")
print(f"  residual rms {res_p.std():.1f} m, chi2/dof = {chi_p:.2f} "
      f"(half-space model {np.mean(res_h**2)/sig_d**2:.2f})")
print(f"  improvement in residual rms: "
      f"{(1 - res_p.std()/res_h.std())*100:.1f}%")
chis = []
for L in L_grid:
    bb, cc, rr = lsq_linear([np.ones(ages.size), plate_profile(L, ages) / plate_ref(L)],
                            d_obs, sig_d)
    chis.append(ages.size * np.mean((rr / sig_d) ** 2))
chis = np.array(chis)
ok = L_grid[chis <= chis.min() + 1.0]
print(f"  the grid step is {L_grid[1]-L_grid[0]:.0f} m but the PRECISION of L comes from")
print(f"  the curvature of chi2: chi2 <= chi2_min + 1 gives L = {L_fit/1000:.1f} "
      f"[{ok.min()/1000:.1f}, {ok.max()/1000:.1f}] km, i.e. +/- "
      f"{0.5*(ok.max()-ok.min())/1000:.1f} km - not +/- 1 km")

iy = ages <= 40.0
ny = int(iy.sum())
beta_y, cov_y, res_y = lsq_linear([np.ones(ny), np.sqrt(ages[iy])], d_obs[iy], sig_d)
beta_yn, cov_yn, res_yn = lsq_linear([np.ones(ny), np.sqrt(ages[iy])], d_true[iy], sig_d)
print(f"\n5. The same half-space fit restricted to the young seafloor "
      f"({ages[iy][0]:.0f}-{ages[iy][-1]:.0f} Myr, {ny} ages)")
print(f"  noisy data:      a = {beta_y[1]:.1f} +/- {np.sqrt(cov_y[1,1]):.1f} m/Myr^0.5, "
      f"d_ridge = {beta_y[0]:.0f} m, residual rms {res_y.std():.1f} m")
print(f"  noiseless truth: a = {beta_yn[1]:.1f} +/- {np.sqrt(cov_yn[1,1]):.1f} m/Myr^0.5, "
      f"residual rms {res_yn.std():.1f} m")
print(f"  full 2-160 Myr fit gave a = {beta_h[1]:.1f}; restricting the range moves the")
print(f"  noiseless fit from {beta_h[1]:.1f} to {beta_yn[1]:.1f} m/Myr^0.5 towards the true "
      f"{A_TRUE:.1f}, so most of the")
print(f"  full-range bias is MODEL error (the plate saturates beyond 40 Myr) and the")
print(f"  remaining {A_TRUE-beta_yn[1]:.0f} m/Myr^0.5 is the plate model's own departure from sqrt(t).")
print(f"  correlation between d_ridge and a: {cov_y[0,1]/np.sqrt(cov_y[0,0]*cov_y[1,1]):+.2f} "
      f"(full range {cov_h[0,1]/np.sqrt(cov_h[0,0]*cov_h[1,1]):+.2f}); it is high at every")
print(f"  range because 1 and sqrt(t) are correlated, so an error in the ridge depth")
print(f"  trades directly into the subsidence rate - which is why d_ridge is quoted with a.")
C_fit = np.sum(q_obs * ages ** -0.5) / np.sum(ages ** -1.0)
res_q = q_obs - C_fit * ages ** -0.5
print("\n6. Heat flow fitted to q = C/sqrt(t)")
print(f"  C = {C_fit:.1f} mW/m2/Myr^0.5, expected from k T_m/sqrt(pi kappa T_MYR) "
      f"= {1000*CONDUCT*TM/np.sqrt(np.pi*KAPPA*MYR):.1f}")
print(f"  residual {res_q.std():.2f} mW/m2, chi2/dof for 5% noise: "
      f"{np.mean((res_q/(sig_q*q_obs))**2):.2f} -> the half-space heat-flow model is")
print(f"  rejected as well; the residual is systematic at old ages where the plate model")
print(f"  keeps a basal flux that the half-space model cannot have.")
bestq = None
for L in L_grid:
    shape = heat_flow(L, ages) / heat_flow(L, np.array([1.0]))[0]
    bb, cc, rr = lsq_linear([shape], q_obs, sig_q * q_obs)
    if bestq is None or np.mean((rr / (sig_q * q_obs)) ** 2) < bestq[0]:
        bestq = (np.mean((rr / (sig_q * q_obs)) ** 2), L)
print(f"  plate-model heat flow with L free: L = {bestq[1]/1000:.1f} km "
      f"(true {L_TRUE/1000:.0f} km), chi2/dof = {bestq[0]:.2f}")
print(f"  observed heat flow at 10 / 50 / 150 Myr: {q_obs[3]:.1f} / {q_obs[18]:.1f} / "
      f"{q_obs[54]:.1f} mW/m2 against the model "
      f"{heat_flow(L_TRUE, 10.0)[0]:.1f} / {heat_flow(L_TRUE, 50.0)[0]:.1f} / "
      f"{heat_flow(L_TRUE, 150.0)[0]:.1f}")
print("\n7. What each observable determines")
print("  bathymetry  -> alpha.T_m (the product) and the plate thickness L")
print("  heat flow   -> k.T_m/sqrt(kappa) (a different product of the same unknowns)")
print("  the two together separate kappa from T_m only if alpha, k and rho are assumed:")
print("  geodynamics is a field of products and ratios, and the report must say which")
print("  one it measured.")
print("\n" + "=" * 74)
print(f"SYNTHETIC demo complete: the half-space model fits with a = {beta_h[1]:.0f} "
      f"m/Myr^0.5 but leaves")
print(f"{res_h.std():.0f} m of residual against {sig_d:.0f} m of noise and a clear systematic signal,")
print(f"the plate model recovers L = {L_fit/1000:.0f} km with {res_p.std():.0f} m of residual, and")
print("the young-seafloor fit shows the d_ridge-a trade-off.")
print("=" * 74)
