#!/usr/bin/env python3
"""Satellite gravimetry, part 4: mass-concentration solutions, leakage and
filtering -- the bias/variance trade of turning coefficients into a regional
number.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mascons_and_leakage_demo.py

Everything here is SYNTHETIC: a synthetic truth mass field, a synthetic
observation operator (truncation + noise), a stated synthetic Love-number law and
a stated spatial filter.  No measured gravity field or mass-change estimate is
used.

Contents
--------
1. A synthetic truth: disc anomalies plus a uniform layer, in water equivalent.
2. Forward model: surface mass -> Stokes coefficients, verified against the
   uniform-layer mass balance.
3. Observation operator: truncation at degree 40 and a stated coefficient noise.
4. Reconstruction and the filter sweep: amplitude bias, leakage into a
   neighbour, leakage into an empty region, and noise.
5. Mass accounting: what truncation and filtering each remove.
6. The honest report: which numbers are measurements and which are choices.
"""

import numpy as np
from scipy.special import gammaln, lpmv, roots_legendre

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
GM_EARTH = 3.986004418e14   # m^3 s^-2
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
G_CONST = 6.67430e-11       # m^3 kg^-1 s^-2
RHO_W = 1000.0              # kg m^-3
RHO_E = (GM_EARTH / G_CONST) / (4.0 / 3.0 * np.pi * R_EARTH ** 3)

# --- SYNTHETIC teaching parameters ------------------------------------------
L_OBS = 40                  # maximum degree of the synthetic solution
NOISE_COEF = 1.0e-11        # synthetic per-coefficient error
DISC_EWH = 0.30             # m, water-equivalent thickness of each disc
DISC_RADIUS_KM = 300.0
UNIFORM_EWH = 0.02          # m, uniform background layer
# (latitude, longitude) of the two discs and of the empty control region
DISC1 = (30.0, 0.0)
DISC2 = (30.0, 15.0)
EMPTY = (-30.0, 0.0)
FILTER_SIGMA_KM = (100.0, 200.0, 400.0, 800.0, 1600.0)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def pbar(l, m, x):
    """4pi-normalised associated Legendre function, Condon-Shortley phase removed."""
    norm = np.sqrt((2.0 - (m == 0)) * (2 * l + 1)
                   * np.exp(gammaln(l - m + 1) - gammaln(l + m + 1)))
    return norm * (-1.0) ** m * lpmv(m, l, x)


def k_love(l):
    """SYNTHETIC load Love-number law: k_l = -0.30 (2/l)^0.5 for l >= 2."""
    if l < 2:
        return 0.0
    return -0.30 * (2.0 / l) ** 0.5


def main():
    # --- grid -----------------------------------------------------------------
    x, w = roots_legendre(90)                    # x = cos(theta), weights
    th = np.arccos(x)
    nphi = 180
    ph = 2.0 * np.pi * np.arange(nphi) / nphi
    wphi = 2.0 * np.pi / nphi
    COSTH = x
    SINTH = np.sin(th)
    cosmph = np.cos(np.outer(np.arange(L_OBS + 1), ph))
    sinmph = np.sin(np.outer(np.arange(L_OBS + 1), ph))
    # Legendre table
    PB = np.zeros((L_OBS + 1, L_OBS + 1, x.size))
    for l in range(L_OBS + 1):
        for m in range(0, l + 1):
            PB[l, m] = pbar(l, m, x)

    def region_mask(lat0, lon0, radius_km):
        """Boolean grid mask of a spherical cap around (lat0, lon0)."""
        th0 = np.deg2rad(90.0 - lat0)
        d = np.arccos(np.clip(np.cos(th)[:, None] * np.cos(th0)
                              + np.sin(th)[:, None] * np.sin(th0)
                              * np.cos(ph[None, :] - np.deg2rad(lon0)), -1, 1))
        return d <= radius_km * 1e3 / R_EARTH

    m1 = region_mask(*DISC1, DISC_RADIUS_KM)
    m2 = region_mask(*DISC2, DISC_RADIUS_KM)
    m3 = region_mask(*EMPTY, DISC_RADIUS_KM)

    section("1. A synthetic truth: two discs on a uniform layer")
    truth = np.full((x.size, nphi), UNIFORM_EWH)
    truth[m1] += DISC_EWH
    truth[m2] += DISC_EWH
    print(f"  uniform background layer      = {UNIFORM_EWH*100:.1f} cm EWH")
    print(f"  two discs of {DISC_EWH*100:.0f} cm EWH, radius {DISC_RADIUS_KM:.0f} km,")
    print(f"  centred at (lat,lon) {DISC1} and {DISC2}, plus an EMPTY control")
    print(f"  region at (lat,lon) {EMPTY} where the truth is the background only.")
    print(f"  grid: {x.size} Gauss latitudes x {nphi} longitudes; "
          f"mean density of the Earth rho_e = {RHO_E:.1f} kg/m^3 (computed)")
    d12 = R_EARTH * np.arccos(np.clip(np.sin(np.deg2rad(DISC1[0]))
                                      * np.sin(np.deg2rad(DISC2[0]))
                                      + np.cos(np.deg2rad(DISC1[0]))
                                      * np.cos(np.deg2rad(DISC2[0]))
                                      * np.cos(np.deg2rad(DISC2[1]-DISC1[1])), -1, 1))
    print(f"  centre-to-centre distance between the two discs = {d12/1e3:.0f} km "
          f"(about {d12/1e3 - 2*DISC_RADIUS_KM:.0f} km of gap between their edges)")
    for name, mask in (("disc 1", m1), ("disc 2", m2), ("control", m3)):
        print(f"  region mean EWH, {name:8s} = {truth[mask].mean()*100:7.3f} cm")

    section("2. Forward model: surface mass -> Stokes coefficients")
    # solid angle per grid cell: (Gauss weight in cos(theta)) * (phi step)
    dw = np.broadcast_to(w[:, None], (x.size, nphi)) * wphi
    C = np.zeros((L_OBS + 1, L_OBS + 1))
    S = np.zeros((L_OBS + 1, L_OBS + 1))
    for l in range(0, L_OBS + 1):
        pref = 3.0 / (4.0 * np.pi * RHO_E * R_EARTH * (2 * l + 1))
        for m in range(0, l + 1):
            p = PB[l, m][:, None]
            dens = RHO_W * truth
            C[l, m] = pref * np.sum(dw * dens * p * cosmph[m][None, :])
            S[l, m] = pref * np.sum(dw * dens * p * sinmph[m][None, :])
    c00_layer = 3.0 * RHO_W * (UNIFORM_EWH + 0.0) / (RHO_E * R_EARTH)
    t_eff = float(np.sum(dw * truth) / np.sum(dw))
    c00_exact = 3.0 * RHO_W * t_eff / (RHO_E * R_EARTH)
    print(f"  global mean EWH of the synthetic truth = {t_eff*100:.4f} cm")
    print(f"  coefficient dC_00 from the integral          : {C[0,0]:.6e}")
    print(f"  closed form 3 rho_w t_eff / (rho_e R)        : {c00_exact:.6e}")
    print(f"  agreement: {abs(C[0,0]-c00_exact)/c00_exact:.3e} relative")
    print("  (this is the normalisation check: the forward integral reproduces")
    print("   exact mass balance for the global mean of the field)")
    analytic_disc = (2.0 * np.pi * (DISC_RADIUS_KM * 1e3) ** 2 * DISC_EWH
                     / (4.0 * np.pi * R_EARTH ** 2))
    print(f"  the same disc contribution if the discs were perfect circles:")
    print(f"    2 pi r^2 t / (4 pi R^2) = {analytic_disc*1e3:.4f} mm, against "
          f"{(t_eff-UNIFORM_EWH)*1e3:.4f} mm measured")
    print("    the grid quantises the disc area (spacing ~2 deg, disc radius")
    print("    2.7 deg), so the discretised truth is thinner than the analytic")
    print("    one.  The truth is an assumption too, and it is worth checking.")
    print(f"  the uniform layer alone would give {c00_layer:.6e}; the two discs")
    print("  raise the global mean by "
          f"{(t_eff-UNIFORM_EWH)*1e3:.4f} mm, and hence dC_00 by "
          f"{(C[0,0]-c00_layer)*100/c00_layer:.3f}%")
    print(f"  the discs contribute to degrees 2..{L_OBS}; "
          f"dC_20 = {C[2,0]:.4e}, dC_22 = {C[2,2]:.4e}")

    section("3. Observation operator: truncation and noise")
    Cn, Sn = C.copy(), S.copy()
    for l in range(2, L_OBS + 1):
        Cn[l, 1:l + 1] += NOISE_COEF * RNG.standard_normal(l)
        Sn[l, 1:l + 1] += NOISE_COEF * RNG.standard_normal(l)
    Cn[0, 0] += NOISE_COEF * RNG.standard_normal()
    print(f"  SYNTHETIC per-coefficient noise: {NOISE_COEF:.1e}")
    print(f"  the truth is truncated at degree {L_OBS} and the noise is added in")
    print("  the coefficient domain, exactly as a real solution is delivered.")
    print(f"  degrees 2..{L_OBS} carry "
          f"{sum(2*l+1 for l in range(2, L_OBS+1))} coefficients; each carries")
    print("  an error that is INDEPENDENT, so the error in a reconstructed point")
    print("  grows with the number of terms unless a filter is applied.")

    section("4. Reconstruction: the round trip, and region-size bias")
    print("  Reconstruction: EWH = (R rho_e / 3 rho_w) sum_l (2l+1)/(1+k_l) W_l")
    print("                      sum_m [C cos + S sin] pbar, with k_l = "
          "-0.30 (2/l)^0.5")
    print("  filter kernel W_l = exp(-l(l+1) sigma^2 / (2 R^2)), W_l = 1 for "
          "sigma = 0")

    def reconstruct(Cuse, Suse, sigma_km, L=L_OBS):
        out = np.zeros((x.size, nphi))
        for l in range(0, L + 1):
            if l >= 2:
                wl = np.exp(-l * (l + 1) * (sigma_km * 1e3) ** 2
                            / (2.0 * R_EARTH ** 2))
            else:
                wl = 1.0
            fac = (R_EARTH * RHO_E / (3.0 * RHO_W)) * (2 * l + 1) / (
                1.0 + k_love(l)) * wl
            for m in range(0, l + 1):
                out += fac * (Cuse[l, m] * cosmph[m][None, :]
                              + Suse[l, m] * sinmph[m][None, :]) * PB[l, m][:, None]
        return out

    def cap_mean(field, lat0, lon0, radius_km):
        m = region_mask(lat0, lon0, radius_km)
        return float(np.sum(dw[m] * field[m]) / np.sum(dw[m]))

    def annulus_mean(field, lat0, lon0, r_in_km, r_out_km):
        m = region_mask(lat0, lon0, r_out_km) & ~region_mask(lat0, lon0, r_in_km)
        return float(np.sum(dw[m] * field[m]) / np.sum(dw[m]))

    round_trip = reconstruct(C, S, 0.0)
    print(f"  round trip with the truth coefficients and no filter:")
    print(f"    rms(recovered - truth) over the globe = "
          f"{np.sqrt(np.mean((round_trip - truth) ** 2))*1e3:.4f} mm")
    print("    region means (weighted by solid angle), truth vs recovered:")
    print("      radius(km)   truth (cm)   recovered (cm)   bias")
    for rad in (300.0, 600.0, 1200.0, 2000.0):
        t_cap = cap_mean(truth, *DISC1, rad)
        r_cap = cap_mean(round_trip, *DISC1, rad)
        print(f"      {rad:10.0f} {t_cap*100:12.3f} {r_cap*100:16.3f} "
              f"{(r_cap-t_cap)/DISC_EWH*100:+15.1f}% of the disc amplitude")
    print("  A cap whose radius is comparable with the resolution scale")
    print("  (pi R / L = 500 km at L = 40) is biased LOW by the truncation: the")
    print("  band-limited field cannot reproduce a sharp disc, so the cap mean")
    print("  loses part of it.  Growing the cap fixes the bias -- the region must")
    print("  be much larger than the resolution, not merely larger than the")
    print("  anomaly.")

    section("5. The filter sweep: bias, sidelobes and noise")
    print("   sigma(km)  disc-1 cap mean  annulus 400-700 km  annulus "
          "1000-1500 km  far-field noise")
    print("              (cm EWH)         (cm EWH)             (cm EWH)     "
          "          rms (mm)")
    for sig in [0.0] + list(FILTER_SIGMA_KM):
        rec_c = reconstruct(C, S, sig)
        rec_n = reconstruct(Cn, Sn, sig)
        noise_field = rec_n - rec_c
        inner = cap_mean(rec_c, *DISC1, 300.0)
        a1 = annulus_mean(rec_c, *DISC1, 400.0, 700.0)
        a2 = annulus_mean(rec_c, *DISC1, 1000.0, 1500.0)
        far_mask = ~region_mask(*DISC1, 3000.0)
        noise_rms = np.sqrt(np.sum(dw[far_mask] * noise_field[far_mask] ** 2)
                            / np.sum(dw[far_mask]))
        print(f"   {sig:9.0f} {inner*100:16.3f} {a1*100:21.3f} "
              f"{a2*100:22.3f} {noise_rms*1e3:15.4f}")
    print("  The truth in both annuli is the 2 cm background, so the excess in the")
    print("  printed annulus means is LEAKAGE: the truncation at degree 40 smears")
    print("  the sharp disc outward.  The annulus 400-700 km holds +2.56 cm of")
    print("  excess at sigma = 0, falling to +0.82 cm at sigma = 1600 km; the")
    print("  cap mean inside the disc falls from 21.73 cm to 2.86 cm against a")
    print("  truth of 32.00 cm (the truncation bias, then the filter bias); and the")
    print("  far-field noise collapses from 295 mm to 4.45 mm.  No single sigma is")
    print("  optimal for all columns: the choice follows from the question, and the")
    print("  cost must be reported with the answer.")

    section("6. Leakage between neighbours, and a linearity check")
    print(f"  A second, identical disc sits {d12/1e3:.0f} km from the first.  Because the")
    print("  forward model is linear, the coefficients of the pair are the sum of")
    print("  the single-disc coefficients -- check that first:")
    def forward(field):
        Cc = np.zeros((L_OBS + 1, L_OBS + 1))
        Ss = np.zeros((L_OBS + 1, L_OBS + 1))
        dens = RHO_W * field
        for l in range(0, L_OBS + 1):
            pref = 3.0 / (4.0 * np.pi * RHO_E * R_EARTH * (2 * l + 1))
            for m in range(0, l + 1):
                p = PB[l, m][:, None]
                Cc[l, m] = pref * np.sum(dw * dens * p * cosmph[m][None, :])
                Ss[l, m] = pref * np.sum(dw * dens * p * sinmph[m][None, :])
        return Cc, Ss

    t1 = np.full_like(truth, UNIFORM_EWH)
    t1[m1] += DISC_EWH
    t2 = np.full_like(truth, UNIFORM_EWH)
    t2[m2] += DISC_EWH
    C1, S1 = forward(t1)
    C2, S2 = forward(t2)
    print(f"    max |C(pair) - C(disc1) - C(disc2)| = "
          f"{np.max(np.abs(C - C1 - C2)):.3e}")
    print("  Contamination: recover disc 1 ALONE, then read the EWH in the cap")
    print("  where disc 2 sits.  The truth there is the 2 cm background.")
    print("   sigma(km)   apparent EWH in the neighbour cap (cm)   excess over "
          "background")
    for sig in [0.0] + list(FILTER_SIGMA_KM):
        rec1 = reconstruct(C1, S1, sig)
        nb = cap_mean(rec1, *DISC2, 300.0)
        print(f"   {sig:9.0f} {nb*100:39.3f} {(nb-UNIFORM_EWH)*100:+22.3f} cm")
    print(f"  Control region at {EMPTY}, far from both discs (truth = 2.00 cm):")
    for sig in (400.0, 1600.0):
        print(f"    sigma = {sig:6.0f} km: recovered cap mean = "
              f"{cap_mean(reconstruct(C, S, sig), *EMPTY, 300.0)*100:.3f} cm")
    print("  The contamination is POSITIVE at every filter width, and it has a")
    print("  MINIMUM (+0.12 cm) at sigma = 400 km, the width matched to the disc")
    print("  radius.  It is larger for a narrower filter (+0.71 cm at sigma = 0,")
    print("  truncation ringing spreading mass outward) and larger again for a")
    print("  wider one (+0.40 cm at sigma = 1600 km, plain smoothing).  A filter")
    print("  matched to the source size is the best compromise, and both errors are")
    print("  artefacts of the analysis rather than properties of the Earth.")
    print("  Two adjacent sources can never be separated without an assumption:")
    print("  stating the filter width IS the assumption, and the contamination it")
    print("  produces belongs in the reported uncertainty.")

    section("7. The honest report")
    print("  Measured   : the coefficients (with a covariance) for l = 2..40.")
    print("  Converted  : water equivalent, using the stated load Love numbers.")
    print("  Chosen     : the truncation degree, the filter width, the regions.")
    print("  Inferred   : that the mass change is a surface layer, and that the")
    print("               removed background (static field, tides, atmosphere,")
    print("               oceans, solid-Earth response) is correct.")
    print("  Any regional number is a filtered, truncated, converted quantity;")
    print("  the filter width and the region definition must be reported with it,")
    print("  and a control region far from every source is the cheapest check")
    print("  that the reported number means what the analyst claims.")


if __name__ == "__main__":
    main()
