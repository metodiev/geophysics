#!/usr/bin/env python3
"""Induced-polarisation applications: synthetic end-members, the confusion
between them, mixture non-uniqueness, and the two-pathway model that links bulk
conductivity to polarisability for clays, sulphides, permafrost and plumes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_applications_demo.py

All models and data in this file are SYNTHETIC.  The end-member parameters are
teaching values chosen to span a plausible range; they are NOT measurements of
any rock, sample, ore body, soil, site or instrument.  Nothing here is a
published laboratory or field result.

Contents
--------
1. Six synthetic end-members: spectra, peak phase, peak frequency.
2. The two-pathway model: polarisability from the conduction pathway split.
3. Confusion between end-members as a function of measurement noise.
4. Mixture non-uniqueness: two different mixtures, one fitted spectrum.
5. Frozen ground and a conductive plume: what each measurement would see.
"""

import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching end-members (chosen to span the range, not measured) --
# name: (rho0 [ohm m], m0 [-], c [-], tau [s])
END_MEMBERS = {
    "clean sand": (800.0, 0.010, 1.00, 0.05),
    "clay-rich soil": (40.0, 0.060, 0.30, 0.002),
    "disseminated sulphide": (120.0, 0.200, 0.55, 0.30),
    "massive sulphide": (2.0, 0.450, 0.75, 2.00),
    "graphitic schist": (15.0, 0.350, 0.60, 5.00),
    "frozen ground": (3000.0, 0.020, 0.40, 0.01),
}
F_TABLE = (0.01, 0.1, 1.0, 10.0, 100.0)


def cole_cole(f_hz, rho0, m, c, tau):
    """Cole-Cole complex resistivity in ohm m."""
    w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
    return rho0 * (1.0 - m * (1.0 - 1.0 / (1.0 + (1j * w * tau) ** c)))


def two_pathway(sigma_e, sigma_s, m0):
    """Effective chargeability of a polarisable pathway in parallel with a
    non-polarisable one.

    With the electrolyte pathway carrying conductance A = sigma_e and the
    surface (or electronic) pathway carrying B = sigma_s, and with the surface
    pathway polarising with intrinsic chargeability m0, the total response is a
    Cole-Cole-like element with

        m_eff = m0 B / (A (1 - m0) + B),

    i.e. the intrinsic polarisability weighted by the fraction of current that
    the polarisable pathway carries.  The bulk conductivity is A + B.
    """
    return m0 * sigma_s / (sigma_e * (1.0 - m0) + sigma_s)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def peak_of(rho0, m, c, tau):
    f = np.logspace(-6, 6, 240001)
    ph = -np.angle(cole_cole(f, rho0, m, c, tau))
    i = int(np.argmax(ph))
    return ph[i], f[i]


def main():
    section("1. Six synthetic end-members")
    print("name                  rho0       m0      c     tau      peak|phi|   "
          "f_peak")
    print("                     (ohm m)            (-)   (s)        (mrad)     (Hz)")
    for name, (rho0, m0, c, tau) in END_MEMBERS.items():
        ph, fp = peak_of(rho0, m0, c, tau)
        print(f"{name:20s} {rho0:8.1f}  {m0:6.3f}  {c:5.2f}  {tau:7.3f}   "
              f"{1000 * ph:9.4f}   {fp:9.5f}")
    print("\nphase (mrad) at fixed frequencies:")
    header = "name                 " + "".join(f"{f:>12.2f} Hz" for f in F_TABLE)
    print(header)
    for name, (rho0, m0, c, tau) in END_MEMBERS.items():
        row = f"{name:20s} "
        for f in F_TABLE:
            row += f"{1000 * -np.angle(cole_cole(f, rho0, m0, c, tau)):12.3f}   "
        print(row)
    print("\nreading: the smallest peak phase here belongs to clean sand and")
    print("frozen ground (a few mrad), the largest to massive sulphide (tens to")
    print("hundreds of mrad), and the peak frequency separates fast (clay) from")
    print("slow (graphite) polarisation.  The four numbers, not the phase alone,")
    print("are the discriminant - section 3 measures how well they discriminate.")

    section("2. The two-pathway model: polarisability from a pathway split")
    m0 = 0.90   # intrinsic chargeability of the polarisable (surface) pathway
    sigma_s = 0.010   # S/m, surface / electronic pathway conductance
    print(f"intrinsic polarisable-pathway chargeability m0 = {m0:.2f}")
    print(f"surface pathway conductance sigma_s = {sigma_s:.4f} S/m")
    print("sigma_e is the non-polarisable electrolyte pathway (Archie-style:")
    print("sigma_e = sigma_w phi^CEM with porosity phi = 0.35 and cementation")
    print("exponent CEM = 1.80, i.e. the formation factor F = phi^-CEM)")
    phi, cem = 0.35, 1.80
    form_factor = phi ** (-cem)
    print(f"formation factor F = phi^-CEM = {form_factor:.3f}")
    print("\n  sigma_w (S/m)   sigma_e (S/m)   sigma_bulk (S/m)   rho_bulk "
          "(ohm m)   m_eff    peak phase (mrad)")
    for sigma_w in (0.005, 0.02, 0.05, 0.2, 1.0):
        sigma_e = sigma_w / form_factor
        sigma_bulk = sigma_e + sigma_s
        m_eff = two_pathway(sigma_e, sigma_s, m0)
        rho0 = 1.0 / sigma_bulk
        ph, _ = peak_of(rho0, m_eff, 0.5, 0.3)
        print(f"  {sigma_w:11.3f}   {sigma_e:12.4f}   {sigma_bulk:14.4f}   "
              f"{rho0:13.4f}   {m_eff:7.4f}   {1000 * ph:14.3f}")
    print("the surface pathway dominates the current only when the electrolyte is")
    print("weak; m_eff then approaches the intrinsic m0.  As the pore fluid")
    print("becomes more conductive the same surface polarisation is swamped, so")
    print("m_eff falls (0.893 to 0.358 across this table) while the bulk")
    print("conductivity rises 15-fold.  That single sentence is the whole reason")
    print("a conductive pore fluid reduces the measured phase even though it")
    print("raises the conductivity - the two quantities are not independent")
    print("indicators, they are two projections of one pathway split.")

    section("3. Confusion between end-members versus measurement noise")
    f_band = np.logspace(-2, 2, 41)
    names = list(END_MEMBERS)
    sigma_phase = 2.0e-3      # rad, stated phase noise
    sigma_amp = 0.01          # 1 %, stated amplitude noise
    print(f"band {f_band[0]:.2f}-{f_band[-1]:.2f} Hz, {f_band.size} "
          f"frequencies")
    print(f"stated noise: {1000 * sigma_phase:.1f} mrad on phase, "
          f"{100 * sigma_amp:.0f}% on |rho|")
    chi_ph = np.zeros((len(names), len(names)))
    chi_both = np.zeros((len(names), len(names)))
    for i, nd in enumerate(names):
        rd, md, cd, td = END_MEMBERS[nd]
        obs = cole_cole(f_band, rd, md, cd, td)
        for j, nm in enumerate(names):
            rm, mm, cm, tm = END_MEMBERS[nm]
            mod = cole_cole(f_band, rm, mm, cm, tm)
            d_ph = (np.angle(mod) - np.angle(obs)) / sigma_phase
            d_am = (np.log(np.abs(mod)) - np.log(np.abs(obs))) / sigma_amp
            chi_ph[i, j] = np.sqrt(np.mean(d_ph ** 2))
            chi_both[i, j] = np.sqrt(np.mean(np.concatenate([d_ph, d_am])
                                             ** 2))
    for label, chi in (("phase only", chi_ph),
                       ("phase + |rho|", chi_both)):
        print(f"\nrms misfit in units of the noise, {label}:")
        print("  data \\ model         " + "".join(f"{n[:9]:>11s}"
                                                    for n in names))
        for i, nd in enumerate(names):
            print(f"  {nd[:16]:18s}" + "".join(f"{chi[i, j]:11.1f}"
                                                for j in range(len(names))))
    conf_ph = [(names[i], names[j]) for i in range(len(names))
               for j in range(i + 1, len(names)) if chi_ph[i, j] < 3.0]
    conf_both = [(names[i], names[j]) for i in range(len(names))
                 for j in range(i + 1, len(names)) if chi_both[i, j] < 3.0]
    print(f"\npairs with rms misfit below 3 sigma (not separable):")
    print("  phase only : " + "; ".join(f"{a} / {b}" for a, b in conf_ph))
    print("  phase+|rho|: " + ("; ".join(f"{a} / {b}" for a, b in conf_both)
                               if conf_both else "none"))
    print("adding the amplitude removes the confusion, because those pairs")
    print("differ in rho0, not in shape.  The discriminant is the pair")
    print("(rho0, phase spectrum): neither alone separates the end-members.")

    section("4. Non-uniqueness: one band, two admissible models")
    def mixture(f_hz, rho0, m_tot, weights, taus, cs):
        w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
        pol = sum(wt / (1.0 + (1j * w * t) ** c)
                  for wt, t, c in zip(weights, taus, cs))
        return rho0 * ((1.0 - m_tot) + m_tot * pol)

    f_fit = np.logspace(-2, 2, 61)
    rho_true = mixture(f_fit, 60.0, 0.25, (0.5, 0.5), (0.02, 2.0), (0.5, 0.5))
    rho_obs = rho_true * (1.0 + sigma_amp * RNG.standard_normal(f_fit.size)) \
        * np.exp(1j * sigma_phase * RNG.standard_normal(f_fit.size))
    print("SYNTHETIC data: an exact two-component mixture, rho0 = 60.0 ohm m,")
    print("m = 0.25, equal weights at tau = 0.02 s and 2.0 s, c = 0.50 each,")
    print(f"observed over {f_fit[0]:.2f}-{f_fit[-1]:.2f} Hz with the noise above")

    def residuals(p):
        m, c, log_tau, rho0 = p
        r = cole_cole(f_fit, rho0, m, c, 10.0 ** log_tau)
        return np.concatenate([(np.angle(r) - np.angle(rho_obs)) / sigma_phase,
                               (np.log(np.abs(r)) - np.log(np.abs(rho_obs)))
                               / sigma_amp])

    sol1 = least_squares(residuals, x0=[0.2, 0.5, 0.0, 60.0],
                         bounds=([0.001, 0.05, -5.0, 1.0],
                                 [0.60, 1.00, 3.0, 2000.0]))
    m1, c1, lt1, r1 = sol1.x

    def residuals2(p):
        rho0, m, lt_a, lt_b, w = p
        r = mixture(f_fit, rho0, m, (w, 1.0 - w), (10.0 ** lt_a, 10.0 ** lt_b),
                    (0.5, 0.5))
        return np.concatenate([(np.angle(r) - np.angle(rho_obs)) / sigma_phase,
                               (np.log(np.abs(r)) - np.log(np.abs(rho_obs)))
                               / sigma_amp])

    sol2 = least_squares(residuals2, x0=[60.0, 0.25, -1.5, 0.3, 0.5],
                         bounds=([10.0, 0.001, -4.0, -2.0, 0.05],
                                 [200.0, 0.60, 0.0, 1.0, 0.95]))
    r2, m2, la2, lb2, w2 = sol2.x
    pred1 = cole_cole(f_fit, r1, m1, c1, 10 ** lt1)
    pred2 = mixture(f_fit, r2, m2, (w2, 1 - w2), (10 ** la2, 10 ** lb2),
                    (0.5, 0.5))
    res1 = 1000.0 * np.sqrt(np.mean(((np.angle(pred1)
                                     - np.angle(rho_obs))
                                    / sigma_phase) ** 2)) * sigma_phase
    res2 = 1000.0 * np.sqrt(np.mean(((np.angle(pred2)
                                     - np.angle(rho_obs))
                                    / sigma_phase) ** 2)) * sigma_phase
    print(f"\nmodel 1, single Cole-Cole (4 parameters): rho0 = {r1:.2f} ohm m, "
          f"m = {m1:.4f}, c = {c1:.4f}, tau = {10 ** lt1:.4f} s")
    print(f"   rms phase residual = {res1:.3f} mrad "
          f"(noise {1000 * sigma_phase:.1f} mrad)")
    print(f"model 2, two-component mixture (5 parameters): rho0 = {r2:.2f} "
          f"ohm m, m = {m2:.4f}, c = 0.50 fixed,")
    print(f"   tau = {10 ** la2:.4f} s (weight {w2:.3f}) and "
          f"{10 ** lb2:.4f} s (weight {1 - w2:.3f})")
    print(f"   rms phase residual = {res2:.3f} mrad")
    print("\nboth are admissible inside the band.  Outside it they part:")
    print("   f (Hz)     model 1 phase   model 2 phase   difference   "
          "|rho| ratio")
    for f in (1e-4, 1e-3, 0.01, 100.0, 1e3, 1e4):
        p1 = cole_cole(f, r1, m1, c1, 10 ** lt1)
        p2 = mixture(np.array([f]), r2, m2, (w2, 1 - w2),
                     (10 ** la2, 10 ** lb2), (0.5, 0.5))[0]
        print(f"  {f:9.2e}   {1000 * -np.angle(p1):12.3f}   "
              f"{1000 * -np.angle(p2):12.3f}   "
              f"{1000 * (np.angle(p2) - np.angle(p1)):+11.3f}   "
              f"{abs(p2) / abs(p1):8.4f}")
    print("(phases in mrad, difference in mrad).  Inside the band the two models")
    print("are the same measurement; outside it they differ by up to 6.6 mrad in")
    print("phase and 1.8% in amplitude.  The two-component model recovers the")
    print("truth (tau = 0.021 s and 2.26 s, weights 0.51/0.49) while the single")
    print("Cole-Cole does not (tau = 0.204 s, c = 0.311) - and yet the band")
    print("cannot tell them apart.  The internal structure is therefore decided")
    print("by bandwidth, not by fitting quality: the honest report is the pair of")
    print("admissible models and the extra decade that would separate them.")

    section("5. Frozen ground, a plume and a clay: the (rho, phase) plane")
    m0 = 0.30        # intrinsic chargeability of the polarisable pathway
    sigma_s = 0.002  # S/m, surface pathway conductance (unfrozen, base case)
    print(f"intrinsic pathway chargeability m0 = {m0:.2f}, surface conductance")
    print(f"sigma_s = {sigma_s:.4f} S/m (unfrozen), formation factor "
          f"F = {form_factor:.3f}")
    print("scenarios, each a stated change to the base case:")
    print("  clay-rich   : surface conductance x 20, pore fluid 0.02 S/m")
    print("  plume       : pore fluid 1.0 S/m (surface unchanged)")
    print("  frozen      : pore fluid 1e-5 S/m, surface conductance x 0.02,")
    print("                and intrinsic pathway chargeability 0.02 because an")
    print("                ice-coated surface has no polarisable double layer")
    print("                in this teaching model")
    print("\n  scenario      rho (ohm m)   m_eff    peak phase (mrad)   "
          "sigma_bulk (S/m)")
    scen = {}
    cases = (("base", 0.05, sigma_s, m0),
             ("clay-rich", 0.02, 20.0 * sigma_s, m0),
             ("plume", 1.0, sigma_s, m0),
             ("frozen", 1e-5, 0.02 * sigma_s, 0.02))
    for label, sigma_w, surf, m_intr in cases:
        sigma_e = sigma_w / form_factor
        sigma_bulk = sigma_e + surf
        m_eff = two_pathway(sigma_e, surf, m_intr)
        rho0 = 1.0 / sigma_bulk
        ph, _ = peak_of(rho0, m_eff, 0.5, 0.3)
        scen[label] = (rho0, m_eff, ph)
        print(f"  {label:12s}  {rho0:12.2f}   {m_eff:7.4f}   "
              f"{1000 * ph:16.3f}   {sigma_bulk:14.5f}")
    print("\nchanges against the base case, with the stated detection thresholds")
    print("(1% on conductivity, 2 mrad on phase):")
    print("  scenario      d rho (%)   detected?   d phase (mrad)   detected?")
    rho_base, _, ph_base = scen["base"]
    for label in ("clay-rich", "plume", "frozen"):
        rho_s, _, ph_s = scen[label]
        d_rho = 100.0 * (rho_s - rho_base) / rho_base
        d_ph = 1000.0 * (ph_s - ph_base)
        print(f"  {label:12s}  {d_rho:+9.1f}   "
              f"{'yes' if abs(d_rho) > 1.0 else 'no ':>8s}   "
              f"{d_ph:+14.3f}   {'yes' if abs(d_ph) > 2.0 else 'no'}")
    print("\nthe two measurements separate different pairs:")
    print("  * resistivity alone: the plume (-93.8%) and the clay-rich case")
    print("    (-77.8%) are both 'a conductor'; the phase value, 1.16 against")
    print("    69.27 mrad, is what tells a conductive pore fluid from a clay")
    print("    content change;")
    print("  * phase alone: the plume (1.16 mrad) and the frozen case (4.03 mrad)")
    print("    are both 'low phase'; the resistivity, 6.53 against 24089.88")
    print("    ohm m, is what tells a saline pore fluid from frozen ground.")
    print("acquiring both puts the three scenarios at distinct points of the")
    print("(rho, phase) plane, which is the quantitative reason a resistivity")
    print("and an IP measurement are made together rather than either alone.")
    print("\ncaution: this model has no unfrozen water film, no ice dielectric")
    print("relaxation and no temperature dependence.  It quantifies the")
    print("sensitivity logic of the two-pathway idea, and nothing else.")


    section("6. Detection thresholds for a small change in pore fluid")
    base_w = 0.05
    sigma_e0 = base_w / form_factor
    sigma_b0 = sigma_e0 + sigma_s
    m_eff0 = two_pathway(sigma_e0, sigma_s, m0)
    ph0, _ = peak_of(1.0 / sigma_b0, m_eff0, 0.5, 0.3)
    print(f"base case: sigma_w = {base_w:.3f} S/m -> rho = "
          f"{1.0 / sigma_b0:.2f} ohm m, m_eff = {m_eff0:.4f}, peak phase = "
          f"{1000 * ph0:.3f} mrad")
    print("stated thresholds: 1% on conductivity (equivalently on rho),")
    print("2 mrad on phase")
    w_grid = np.linspace(base_w, 0.20, 601)
    d_ph = np.zeros_like(w_grid)
    d_rho = np.zeros_like(w_grid)
    for i, sw in enumerate(w_grid):
        se = sw / form_factor
        sb = se + sigma_s
        me = two_pathway(se, sigma_s, m0)
        ph, _ = peak_of(1.0 / sb, me, 0.5, 0.3)
        d_ph[i] = 1000.0 * (ph - ph0)
        d_rho[i] = 100.0 * ((1.0 / sb) - (1.0 / sigma_b0)) / (1.0 / sigma_b0)
    i_ph = int(np.argmax(d_ph <= -2.0))
    i_rho = int(np.argmax(d_rho <= -1.0))
    print("\n  change that reaches the threshold   sigma_w (S/m)   change in "
          "sigma_w   change in rho   change in phase")
    for label, i in (("2 mrad of phase", i_ph), ("1% of resistivity", i_rho)):
        print(f"  {label:34s} {w_grid[i]:12.5f}   "
              f"{100.0 * (w_grid[i] - base_w) / base_w:+11.2f}%   "
              f"{d_rho[i]:+12.2f}%   {d_ph[i]:+15.3f} mrad")
    print(f"clearing the 2 mrad phase threshold needs sigma_w = {w_grid[i_ph]:.5f}")
    print(f"S/m, a change of {100.0 * (w_grid[i_ph] - base_w) / base_w:+.2f}%, and")
    print(f"by then the resistivity has already moved {d_rho[i_ph]:+.2f}% - about")
    print(f"{abs(d_rho[i_ph]) / 1.0:.0f} times its own 1% threshold.  Conversely a")
    print(f"{abs(d_rho[i_rho]):.2f}% resistivity change (sigma_w = "
          f"{w_grid[i_rho]:.5f} S/m,")
    print(f"{100.0 * (w_grid[i_rho] - base_w) / base_w:+.2f}%) moves the phase by")
    print(f"only {d_ph[i_rho]:+.3f} mrad, well below the 2 mrad threshold.")
    print("resistivity is therefore the more sensitive detector of a small")
    print("salinity change and the phase the better classifier of a large one;")
    print("both statements follow from the same pathway equation.")


if __name__ == "__main__":
    main()
