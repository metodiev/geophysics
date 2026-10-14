#!/usr/bin/env python3
"""Building geophysical proxies for hydrological properties: error amplification
through a chained petrophysical transform, transform bias, and the reduction of
the non-uniqueness volume when two measurements replace one.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysical_proxy_relations_demo.py

All models, data and priors here are SYNTHETIC teaching constructs.  Nothing is
fitted to a site, a log or a published dataset.

Contents
--------
1.  The chain resistivity -> porosity -> permeability and its amplification
    factor, computed analytically and by finite difference.
2.  Monte Carlo through the nonlinear transform: bias, spread and the
    difference between f(E[m]) and E[f(m)].
3.  A two-parameter hypothesis grid (phi, S_w) with two forward operators:
    Archie resistivity and Gassmann velocity.
4.  Likelihood, posterior and marginals for each data set alone and combined.
5.  Information gain in bits and the posterior width that a survey can claim.
6.  Reference numbers used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC petrophysical model ------------------------------------------
A_ARCHIE = 1.0
M_ARCHIE = 2.0
N_ARCHIE = 2.0
RHO_W = 2.50                    # pore-fluid resistivity, ohm m (SYNTHETIC)
K_MIN, MU_MIN, RHO_MIN = 36.0, 45.0, 2650.0
PHI_C = 0.42                    # SYNTHETIC critical porosity of the closure

# --- SYNTHETIC measurement noise (1 sigma, relative) ------------------------
SIG_RHO = 0.02                  # 2% on formation resistivity
SIG_VP = 0.01                   # 1% on P velocity

# --- SYNTHETIC "true" state the observations are generated from -------------
PHI_TRUE, SW_TRUE = 0.25, 0.60


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def kozeny_carman(phi, d_m=0.20e-3, tau=2.5):
    """KC permeability in m^2 for the fixed SYNTHETIC grain size d."""
    s0 = 6.0 / d_m
    return phi ** 3 / (2.0 * tau * s0 ** 2 * (1.0 - phi) ** 2)


def archie_rho(phi, sw, rho_w=RHO_W, a=A_ARCHIE, mm=M_ARCHIE, n=N_ARCHIE):
    """Formation resistivity from Archie, in ohm m."""
    return a * rho_w / (phi ** mm * sw ** n)


def dry_moduli(phi, k_min=K_MIN, mu_min=MU_MIN, phi_c=PHI_C):
    """SYNTHETIC critical-porosity closure for the dry frame (GPa)."""
    return k_min * (1.0 - phi / phi_c), mu_min * (1.0 - phi / phi_c)


def gassmann(k_dry, k_min, k_fl, phi):
    num = (1.0 - k_dry / k_min) ** 2
    den = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min ** 2
    return k_dry + num / den


def wood_fluid(sw, k_w=2.20, k_g=1.0e-4):
    return 1.0 / (sw / k_w + (1.0 - sw) / k_g)


def vp_model(phi, sw):
    """P velocity in km/s from the synthetic closure plus Gassmann."""
    k_dry, mu_dry = dry_moduli(phi)
    k_sat = gassmann(k_dry, K_MIN, wood_fluid(sw), phi)
    rho = (1.0 - phi) * RHO_MIN + phi * (sw * 1000.0 + (1.0 - sw) * 1.2)
    return np.sqrt((k_sat * 1e9 + 4.0 * mu_dry * 1e9 / 3.0) / rho) / 1.0e3


def gaussian_loglike(model, observed, sigma_rel):
    """Gaussian log-likelihood for a relative measurement uncertainty."""
    sigma = sigma_rel * observed
    return -0.5 * ((model - observed) / sigma) ** 2


def entropy_bits(p):
    """Shannon entropy of a normalised grid density, in bits."""
    q = p[p > 0]
    return float(-np.sum(q * np.log2(q)))


def main():
    section("1. Chained transform and its amplification factor")
    phi = 0.25
    dlnk_dphi = 3.0 / phi + 2.0 / (1.0 - phi)
    dlnphi_dlnrho = -1.0 / M_ARCHIE
    print(f"  chain: rho_t -> phi (Archie, m = {M_ARCHIE:.1f}) -> k (KC)")
    print(f"  d ln phi / d ln rho_t = -1/m = {dlnphi_dlnrho:.4f}")
    print(f"  d ln k / d phi        = 3/phi + 2/(1-phi) = {dlnk_dphi:.4f}")
    dlnk_dlnrho = dlnk_dphi * phi * dlnphi_dlnrho
    print(f"  d ln k / d ln rho_t   = (d ln k/d phi)(phi)(d ln phi/d ln rho_t)")
    print(f"                        = {dlnk_dlnrho:.4f}")
    eps = 1e-6
    r0 = archie_rho(phi, SW_TRUE)
    r1 = r0 * (1.0 + eps)
    phi1 = (A_ARCHIE * RHO_W / (r1 * SW_TRUE ** N_ARCHIE)) ** (1.0 / M_ARCHIE)
    finite = (np.log(kozeny_carman(phi1)) - np.log(kozeny_carman(phi))) / eps
    print(f"  finite difference of the same derivative = {finite:.4f}")
    for drho in (0.01, 0.02, 0.05):
        print(f"  a {100 * drho:.0f}% resistivity error gives a "
              f"{100 * abs(dlnk_dlnrho) * drho:.1f}% permeability error")

    section("2. Monte Carlo through the nonlinear transform")
    n_draw = 200000
    print(f"  input: phi = {phi:.3f} with a stated 1-sigma (SYNTHETIC)")
    print("      sigma_phi   sigma_phi/phi   k median (m^2)   k mean (m^2)   "
          "rel sd   bias of k(phi)")
    ref = None
    for sigma_phi in (0.012, 0.025, 0.050):
        phi_draw = RNG.normal(phi, sigma_phi, n_draw)
        phi_draw = phi_draw[(phi_draw > 0.05) & (phi_draw < 0.40)]
        k_draw = kozeny_carman(phi_draw)
        med, mean, sd = float(np.median(k_draw)), float(k_draw.mean()), float(k_draw.std())
        if abs(sigma_phi - 0.012) < 1e-12:
            ref = (med, mean, sd)
        print(f"  {sigma_phi:10.3f}   {100 * sigma_phi / phi:12.1f}%   "
              f"{med:.5e}   {mean:.5e}   {100 * sd / mean:6.1f}%   "
              f"{100.0 * (kozeny_carman(phi) - med) / kozeny_carman(phi):+9.2f}%")
    med, mean, sd = ref
    print(f"  at sigma_phi = 0.012 the plug-in k(phi = {phi:.3f}) = "
          f"{kozeny_carman(phi):.5e} m^2")
    print(f"  the relative spread of k ({100 * sd / mean:.1f}%) is about "
          f"{sd / mean / (0.012 / phi):.2f} times the")
    print(f"  relative spread of phi, as the amplification factor 3/phi + 2/(1-phi) "
          f"predicts.")
    print(f"  k is convex in phi, so the distribution is skewed: its mean sits")
    print(f"  {100 * (mean / med - 1.0):.1f}% above its median.")
    print("  At a few per cent the plug-in estimate is nearly unbiased, but the")
    print("  spread and the skew grow fast: this is why a proxy must be reported as")
    print("  a distribution, not as one number.")

    section("3. Two-parameter hypothesis grid with two forward operators")
    phis = np.linspace(0.16, 0.38, 111)
    sws = np.linspace(0.06, 1.00, 95)
    PHI_G, SW_G = np.meshgrid(phis, sws, indexing="ij")
    rho_grid = archie_rho(PHI_G, SW_G)
    vp_grid = vp_model(PHI_G, SW_G)
    rho_obs = float(archie_rho(PHI_TRUE, SW_TRUE))
    vp_obs = float(vp_model(PHI_TRUE, SW_TRUE))
    print(f"  SYNTHETIC truth: phi = {PHI_TRUE:.2f}, S_w = {SW_TRUE:.2f}")
    print(f"  forward 1: Archie resistivity  rho_t = {rho_obs:.3f} ohm m")
    print(f"  forward 2: Gassmann velocity   Vp    = {vp_obs:.4f} km/s")
    print(f"  grid: {phis.size} x {sws.size} = {phis.size * sws.size} hypotheses")
    print(f"  stated noise: {100 * SIG_RHO:.0f}% on rho_t, {100 * SIG_VP:.0f}% on Vp")

    section("4. Likelihood, posterior and marginals")
    ll_rho = gaussian_loglike(rho_grid, rho_obs, SIG_RHO)
    ll_vp = gaussian_loglike(vp_grid, vp_obs, SIG_VP)
    prior = np.ones_like(PHI_G)
    prior /= prior.sum()
    results = {}
    for label, ll in (("rho_t only", ll_rho), ("Vp only", ll_vp),
                      ("joint", ll_rho + ll_vp)):
        w = prior * np.exp(ll - ll.max())
        w /= w.sum()
        results[label] = w
    print("      data used      phi (mean +- sd)      S_w (mean +- sd)")
    for label, w in results.items():
        mp = (w.sum(axis=1) * phis).sum()
        sp = np.sqrt((w.sum(axis=1) * (phis - mp) ** 2).sum())
        ms = (w.sum(axis=0) * sws).sum()
        ss = np.sqrt((w.sum(axis=0) * (sws - ms) ** 2).sum())
        print(f"  {label:>14s}   {mp: 6.4f} +- {sp:6.4f}      "
              f"{ms: 6.4f} +- {ss:6.4f}")
    w_rho = results["rho_t only"].sum(axis=1)
    print(f"  with rho_t alone the porosity marginal is broad: the 5-95% range spans")
    lo = phis[np.searchsorted(np.cumsum(w_rho), 0.05)]
    hi = phis[np.searchsorted(np.cumsum(w_rho), 0.95)]
    print(f"  {lo:.3f} to {hi:.3f} in phi, because a change in phi and a change in")
    print("  S_w produce the same resistivity.")

    section("5. Information gain from the second measurement")
    h_prior = entropy_bits(prior.ravel())
    print(f"  entropy of the prior over the grid      = {h_prior:.4f} bits "
          f"({np.log2(phis.size * sws.size):.4f} bits for a flat grid)")
    for label, w in results.items():
        print(f"  entropy of the {label:>10s} posterior = {entropy_bits(w.ravel()):.4f} bits"
              f"   gain = {h_prior - entropy_bits(w.ravel()):.4f} bits")
    print("  the joint posterior is narrower than either marginal, but it is still a")
    print("  distribution: the survey constrains a trade-off curve, not a point.")

    section("6. Error budget for the composed proxy: rho_t -> phi -> k")
    sw_ref = 0.60
    rho_ref = float(archie_rho(phi, sw_ref))
    const = A_ARCHIE * RHO_W / (rho_ref * sw_ref ** N_ARCHIE)
    print(f"  model: phi = {phi:.3f}, S_w = {sw_ref:.2f}, rho_t = {rho_ref:.3f} ohm m")
    print(f"  Archie constant C = a rho_w/(rho_t S_w^n) = {const:.6f}")
    print("      error source        stated 1 sigma        contribution to sigma(ln k)")
    phi_pert = float(archie_rho(phi, sw_ref) * 1.02)
    phi_2 = (A_ARCHIE * RHO_W / (phi_pert * sw_ref ** N_ARCHIE)) ** (1.0 / M_ARCHIE)
    c_rho = abs(np.log(kozeny_carman(phi_2) / kozeny_carman(phi)))
    phi_m = (const) ** (1.0 / (M_ARCHIE + 0.2))
    c_m = abs(np.log(kozeny_carman(phi_m) / kozeny_carman(phi)))
    c_d = 2.0 * 0.30
    print(f"  rho_t                      2% relative error    {c_rho:.4f}")
    print(f"  cementation exponent m     +-0.20               {c_m:.4f}")
    print(f"  grain diameter d           +-30% relative       {c_d:.4f}")
    total = float(np.sqrt(c_rho ** 2 + c_m ** 2 + c_d ** 2))
    print(f"  total in quadrature                              {total:.4f}")
    print(f"  a factor-of-two target is sigma(ln k) <= ln 2 = {np.log(2.0):.4f}")
    print(f"  verdict: {'meets' if total <= np.log(2.0) else 'fails'} the target; "
          f"the largest single term is the grain diameter")
    print(f"  improving rho_t from 2% to 0.5% changes the total to "
          f"{np.sqrt((c_rho / 4.0) ** 2 + c_m ** 2 + c_d ** 2):.4f}, which is not a fix.")

    section("7. Reference numbers used in the lesson")
    print(f"  d ln k / d ln rho_t = {dlnk_dlnrho:.4f}")
    print(f"  Monte Carlo: phi = 0.250 +- 0.012 -> k median {med:.4e} m^2,")
    print(f"    k mean {mean:.4e} m^2, relative sd {100 * sd / mean:.1f}%")
    print(f"  synthetic truth: phi = {PHI_TRUE:.2f}, S_w = {SW_TRUE:.2f}, "
          f"rho_t = {rho_obs:.3f} ohm m, Vp = {vp_obs:.4f} km/s")


if __name__ == "__main__":
    main()
