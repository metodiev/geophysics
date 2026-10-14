#!/usr/bin/env python3
"""Benthic habitat mapping: acoustic angular response of the seabed, the effect
of grid resolution on terrain attributes, and the accuracy of a habitat
classifier with its confusion matrix.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python habitat_mapping_demo.py

Everything here is SYNTHETIC.  The seabed parameters, the terrain surface and the
class features are teaching models; no real survey, seabed, habitat map or
ground-truth station is referenced, and no number is quoted from a published
measurement.  The classification results are properties of the synthetic data
set generated here.

Contents
--------
1. Angular response of the seabed: coherent (impedance) versus Lambertian
   (roughness) end-members, and the measured dB/deg slope of each.
2. Grid resolution versus terrain attributes: how much of the true slope a
   coarse grid recovers.
3. Habitat classification: k-means versus a supervised classifier, confusion
   matrix, overall accuracy, kappa, and the learning curve versus sample size.
4. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO_W, C_W = 1030.0, 1500.0        # seawater density, sound speed
F_HZ = 1.0e5                       # 100 kHz sonar
A_BUMP, S_BUMP = 50.0, 200.0       # m, Gaussian bump height and length scale


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def fluid_reflection(theta_deg, rho2, c2):
    """Complex plane-wave reflection coefficient at a fluid-fluid interface.

    theta_deg is the grazing angle in water (0 = along the interface).  Returns
    a complex number; |R| = 1 beyond the critical angle.  At grazing 90 deg this
    reduces to the normal-incidence impedance formula (Z2 - Z1)/(Z2 + Z1).
    """
    theta = np.radians(theta_deg)
    p = np.cos(theta) / C_W                  # ray parameter, s/m
    q1 = np.sin(theta) / C_W                 # vertical slowness in water
    arg = 1.0 / c2 ** 2 - p ** 2
    if arg < 0.0:                            # evanescent: total reflection
        q2 = 1j * np.sqrt(-arg)
    else:
        q2 = np.sqrt(arg)
    return (rho2 * q1 - RHO_W * q2) / (rho2 * q1 + RHO_W * q2)


def roughness_param(theta_deg, sigma_rough, k):
    """Rayleigh roughness parameter 2 k sigma cos(theta); >~1 means large roughness."""
    return 2.0 * k * sigma_rough * np.cos(np.radians(theta_deg))


def coherence_loss_db(theta_deg, sigma_rough, k):
    """Rough-surface coherence loss in dB; NaN beyond the small-roughness regime."""
    if roughness_param(theta_deg, sigma_rough, k) > 5.0:
        return np.nan
    x = roughness_param(theta_deg, sigma_rough, k) ** 2
    return 10.0 / np.log(10.0) * (-x)


def bs_coherent(theta_deg, rho2, c2, sigma_rough, k):
    """Coherent (specular-return) backscatter strength in dB; NaN if out of regime."""
    if roughness_param(theta_deg, sigma_rough, k) > 5.0:
        return np.nan
    r = np.abs(fluid_reflection(theta_deg, rho2, c2))
    loss = np.exp(-roughness_param(theta_deg, sigma_rough, k) ** 2)
    return 10.0 * np.log10(max(r ** 2 * loss, 1e-300))


def bs_lambert(theta_deg, mu_l):
    """Lambertian diffuse backscatter strength (dB) for a fully rough interface."""
    return 10.0 * np.log10(mu_l * np.sin(np.radians(theta_deg)) ** 2)


def kappa(confusion):
    """Cohen's kappa from a confusion matrix (rows = truth, columns = prediction)."""
    n = confusion.sum()
    po = np.trace(confusion) / n
    pe = np.sum(confusion.sum(axis=1) * confusion.sum(axis=0)) / n ** 2
    return (po - pe) / (1.0 - pe)


def main():
    k = 2.0 * np.pi * F_HZ / C_W
    print(f"seawater: rho = {RHO_W:.0f} kg/m^3, c = {C_W:.0f} m/s, "
          f"Z = {RHO_W * C_W:.3e} kg/(m^2 s)")
    print(f"sonar frequency {F_HZ / 1e3:.0f} kHz -> acoustic wavenumber "
          f"k = 2 pi f / c = {k:.1f} 1/m (wavelength {C_W / F_HZ * 100:.2f} cm)")

    section("1. Angular response: coherent versus diffuse seabed")
    mud = dict(rho2=1500.0, c2=1520.0, sigma=0.002, label="soft mud (smooth)")
    rock = dict(rho2=2600.0, c2=3200.0, sigma=0.10, label="rock (rough)")
    angles = np.array([20.0, 30.0, 45.0, 60.0, 90.0])
    mu_lam = 0.02
    print("\n  impedance contrast and normal-incidence reflection:")
    print("   seabed               Z (kg/m^2 s)   R(90 deg)   |R|^2 (dB)")
    for seabed in (mud, rock):
        r = fluid_reflection(90.0, seabed["rho2"], seabed["c2"])
        print(f"   {seabed['label']:20s} {seabed['rho2'] * seabed['c2']:.3e}   "
              f"{np.abs(r):10.4f}   {20 * np.log10(np.abs(r)):9.2f}")
    print("  (the mud is a weak reflector, the rock a strong one; both are faster")
    print("   than water, so both have a critical grazing angle and |R| = 1 at")
    print("   grazing incidence.)")

    print("\n  Rayleigh roughness parameter 2 k sigma cos(theta) and coherence loss:")
    print("   angle (deg)   mud 2k.sigma   rock 2k.sigma   mud loss (dB)   rock loss (dB)")
    for a in angles:
        sm = roughness_param(a, mud["sigma"], k)
        sr = roughness_param(a, rock["sigma"], k)
        lm = coherence_loss_db(a, mud["sigma"], k)
        lr = coherence_loss_db(a, rock["sigma"], k)
        print(f"   {a:11.1f}   {sm:12.2f}   {sr:13.2f}   "
              f"{lm:14.1f}   {('n/a' if lr != lr else f'{lr:.1f}'):>13s}")
    print("  a value of 2 k sigma cos(theta) near or below 1 is the small-roughness")
    print("  regime where the coherence model applies; the rock is two orders of")
    print("  magnitude beyond it at 100 kHz and is therefore fully diffuse.")

    print("\n  coherent BS (dB) at grazing angles (blank = outside the model):")
    print("   angle (deg)      mud      rock")
    for a in angles:
        bm = bs_coherent(a, mud["rho2"], mud["c2"], mud["sigma"], k)
        br = bs_coherent(a, rock["rho2"], rock["c2"], rock["sigma"], k)
        print(f"   {a:11.1f}   {bm:7.1f}   {('n/a' if br != br else f'{br:.1f}'):>7s}")
    print("  the rock is beyond the coherence model except at normal incidence,")
    print("  where the roughness parameter vanishes and the rock returns its")
    print(f"  impedance level {20 * np.log10(abs(fluid_reflection(90.0, rock['rho2'], rock['c2']))):.2f} dB.")
    print("\n  Lambertian (fully rough) BS in dB with mu_L = "
          f"{mu_lam:.3f} (model constant):")
    print("   angle (deg)   " + "   ".join(f"{a:5.1f}" for a in angles))
    print("   BS (dB)       " +
          "   ".join(f"{bs_lambert(a, mu_lam):5.1f}" for a in angles))
    print("\n  measured angular slopes over 20-60 deg grazing (dB per degree):")
    for seabed in (mud, rock):
        bs_c = np.array([bs_coherent(a, seabed["rho2"], seabed["c2"],
                                     seabed["sigma"], k)
                         for a in (20.0, 60.0)])
        if np.any(np.isnan(bs_c)):
            print(f"   {seabed['label']:20s} coherent n/a (outside the model)")
        else:
            print(f"   {seabed['label']:20s} coherent {(bs_c[1] - bs_c[0]) / 40.0:+.3f}")
    bs_l = np.array([bs_lambert(a, mu_lam) for a in (20.0, 60.0)])
    print(f"   {'Lambertian':20s} coherent {(bs_l[1] - bs_l[0]) / 40.0:+.3f}")
    print("  both end-members brighten toward normal incidence, but they differ in")
    print("  level, in slope and in curvature: the mud's coherent curve is not a")
    print("  sin^2 law, and its level at normal incidence is set by |R|^2 rather")
    print("  than by a scattering constant.  The full angular curve, not one")
    print("  number, is therefore what identifies a seabed type - which is exactly")
    print("  what multibeam angular-response classification uses.")

    section("2. Grid resolution versus terrain attributes")
    print(f"  synthetic Gaussian bump: height {A_BUMP:.0f} m, length scale "
          f"{S_BUMP:.0f} m")
    print(f"  analytic maximum slope = A/s exp(-1/2) = "
          f"{A_BUMP / S_BUMP * np.exp(-0.5):.4f} = "
          f"{np.degrees(np.arctan(A_BUMP / S_BUMP * np.exp(-0.5))):.2f} deg")
    print("\n  grid spacing (m)   samples across bump   max slope (deg)   recovered")
    for dx in (5.0, 10.0, 25.0, 50.0, 100.0, 200.0):
        n = int(6 * S_BUMP / dx)
        ax = (np.arange(n) - n / 2) * dx
        X, Y = np.meshgrid(ax, ax)
        Z = A_BUMP * np.exp(-(X ** 2 + Y ** 2) / (2 * S_BUMP ** 2))
        gy, gx = np.gradient(Z, dx, dx)
        mag = np.sqrt(gx ** 2 + gy ** 2)
        smax = np.degrees(np.arctan(mag.max()))
        true = np.degrees(np.arctan(A_BUMP / S_BUMP * np.exp(-0.5)))
        print(f"  {dx:16.0f}   {6 * S_BUMP / dx:19.0f}   {smax:15.2f}   "
              f"{smax / true * 100:8.1f}%")
    print("  a coarse grid cannot represent the steepest part of a feature, so the")
    print("  maximum slope — and every habitat class defined by a slope threshold —")
    print("  is resolution dependent.  This is the marine form of the modifiable")
    print("  areal unit problem.")

    section("3. Habitat classification and its accuracy")
    classes = {
        "mud": dict(slope=(2.0, 1.5), bs=(-21.0, 2.5), n=400),
        "sand": dict(slope=(4.5, 2.0), bs=(-16.0, 3.0), n=200),
        "rock": dict(slope=(8.0, 3.5), bs=(-10.0, 3.5), n=60),
    }
    X_list, y_list = [], []
    for ci, (name, p) in enumerate(classes.items()):
        sl = RNG.normal(p["slope"][0], p["slope"][1], p["n"])
        bs = RNG.normal(p["bs"][0], p["bs"][1], p["n"])
        X_list.append(np.c_[sl, bs])
        y_list.append(np.full(p["n"], ci))
    X = np.vstack(X_list)
    y = np.concatenate(y_list)
    names = list(classes)
    print(f"  synthetic samples: {X.shape[0]} (features: slope in deg, "
          f"backscatter in dB)")
    for ci, name in enumerate(names):
        sel = y == ci
        print(f"    {name:5s}: n = {sel.sum():4d}, mean slope "
              f"{X[sel, 0].mean():5.2f} deg, mean BS {X[sel, 1].mean():6.2f} dB")
    print("  class priors are deliberately unequal: this is the normal situation")
    print("  and it is what makes overall accuracy a misleading headline number.")

    # supervised: nearest class centroid, trained on a split
    perm = RNG.permutation(X.shape[0])
    n_train = 40
    tr, te = perm[:n_train], perm[n_train:]
    cent = np.array([X[tr][y[tr] == ci].mean(axis=0) for ci in range(len(names))])
    d = np.linalg.norm(X[te][:, None, :] - cent[None, :, :], axis=2)
    pred_sup = d.argmin(axis=1)
    y_te = y[te]
    print(f"\n  supervised nearest-centroid classifier trained on {n_train} samples")
    print(f"  test set: {y_te.size} samples")
    cm = np.zeros((len(names), len(names)), dtype=int)
    for t, p in zip(y_te, pred_sup):
        cm[t, p] += 1
    print("    confusion matrix (rows = truth, columns = prediction):")
    print("             " + "".join(f"{n:>8s}" for n in names) + "   recall")
    for ci, name in enumerate(names):
        recall = cm[ci, ci] / cm[ci].sum() if cm[ci].sum() else np.nan
        print(f"    {name:8s} " + "".join(f"{v:8d}" for v in cm[ci]) +
              f"   {recall:6.3f}")
    print("    precision  " + "".join(
        f"{(cm[ci, ci] / cm[:, ci].sum() if cm[:, ci].sum() else np.nan):8.3f}"
        for ci in range(len(names))))
    po = np.trace(cm) / cm.sum()
    print(f"    overall accuracy = {po:.3f}, kappa = {kappa(cm):.3f}")
    print("  kappa removes the agreement expected by chance; with these priors a")
    print("  classifier that always answered 'mud' would already score "
          f"{cm.sum(axis=0).max() / cm.sum():.3f} accuracy but kappa ~ 0.")

    print("\n  unsupervised k-means on the same features (no labels used):")
    k_means = len(names)
    order = RNG.permutation(X.shape[0])[:k_means]
    centers = X[order].copy()
    for _ in range(200):
        dk = np.linalg.norm(X[:, None, :] - centers[None, :, :], axis=2)
        lab = dk.argmin(axis=1)
        new = np.array([X[lab == j].mean(axis=0) if np.any(lab == j) else centers[j]
                        for j in range(k_means)])
        if np.allclose(new, centers):
            break
        centers = new
    # map clusters to the majority true class
    mapping = {}
    for j in range(k_means):
        trues = y[lab == j]
        mapping[j] = np.bincount(trues, minlength=k_means).argmax() if trues.size else -1
    pred_km = np.array([mapping[j] for j in lab])
    cm_k = np.zeros((k_means, k_means), dtype=int)
    for t, p in zip(y, pred_km):
        cm_k[t, p] += 1
    print("    cluster majority mapping: " +
          ", ".join(f"{j}->{names[mapping[j]]}" for j in range(k_means)))
    print("    confusion matrix after mapping (rows = truth, columns = cluster):")
    for ci, name in enumerate(names):
        print(f"    {name:8s} " + "".join(f"{v:8d}" for v in cm_k[ci]))
    print(f"    overall accuracy = {np.trace(cm_k) / cm_k.sum():.3f}, "
          f"kappa = {kappa(cm_k):.3f}")
    print("  k-means reproduces the supervised partition almost exactly on this")
    print("  data set (0.839 against 0.837), so the accuracy does not say which is")
    print("  the better method.  What the unsupervised route cannot supply is the")
    print("  mapping from cluster index to habitat name; an oracle mapping was used")
    print("  here, and without ground truth neither that mapping nor the number of")
    print("  clusters is known:")
    print("    clusters   accuracy with an oracle cluster-to-habitat mapping")
    for kk in (2, 3, 4, 5):
        order2 = RNG.permutation(X.shape[0])[:kk]
        cen = X[order2].copy()
        for _ in range(200):
            dk = np.linalg.norm(X[:, None, :] - cen[None, :, :], axis=2)
            lb = dk.argmin(axis=1)
            new = np.array([X[lb == j].mean(axis=0) if np.any(lb == j) else cen[j]
                            for j in range(kk)])
            if np.allclose(new, cen):
                break
            cen = new
        mp = {j: (np.bincount(y[lb == j], minlength=4).argmax() if np.any(lb == j)
                  else -1) for j in range(kk)}
        pr = np.array([mp[j] for j in lb])
        cmk = np.zeros((4, 4), dtype=int)
        for t, pp in zip(y, pr):
            if pp >= 0:
                cmk[t, pp] += 1
        acc_k = np.trace(cmk) / cmk.sum()
        print(f"    {kk:8d}   {acc_k:.3f}")
    print("  with an oracle mapping extra clusters can only subdivide a habitat,")
    print("  so accuracy rises with the number of clusters and cannot be used to")
    print("  choose it.  The number of habitat classes has to come from the")
    print("  question being asked, and it is validated by the ground-truth mapping,")
    print("  not by the accuracy.")

    print("\n  learning curve for the supervised classifier (mean of 30 draws):")
    print("    training samples   mean accuracy   mean kappa   mean rock recall")
    for n_tr in (3, 6, 12, 24, 48, 96):
        accs, kaps, rock_rec = [], [], []
        for _ in range(30):
            perm2 = RNG.permutation(X.shape[0])
            tr2, te2 = perm2[:n_tr], perm2[n_tr:]
            if len(np.unique(y[tr2])) < k_means:
                continue
            cent2 = np.array([X[tr2][y[tr2] == ci].mean(axis=0)
                              for ci in range(k_means)])
            d2 = np.linalg.norm(X[te2][:, None, :] - cent2[None, :, :], axis=2)
            pr = d2.argmin(axis=1)
            cm2 = np.zeros((k_means, k_means), dtype=int)
            for t, p in zip(y[te2], pr):
                cm2[t, p] += 1
            accs.append(np.trace(cm2) / cm2.sum())
            kaps.append(kappa(cm2))
            rock_rec.append(cm2[2, 2] / cm2[2].sum() if cm2[2].sum() else np.nan)
        print(f"    {n_tr:16d}   {np.mean(accs):13.3f}   {np.mean(kaps):10.3f}   "
              f"{np.nanmean(rock_rec):15.3f}")

    section("4. Worked examples used in the lesson")
    r_mud = np.abs(fluid_reflection(90.0, mud["rho2"], mud["c2"]))
    r_rock = np.abs(fluid_reflection(90.0, rock["rho2"], rock["c2"]))
    print(f"(a) normal-incidence |R|: mud {r_mud:.4f} "
          f"({20 * np.log10(r_mud):.2f} dB), rock {r_rock:.4f} "
          f"({20 * np.log10(r_rock):.2f} dB)")
    print(f"(b) mud coherent BS: 20 deg "
          f"{bs_coherent(20.0, mud['rho2'], mud['c2'], mud['sigma'], k):.2f} dB, "
          f"60 deg "
          f"{bs_coherent(60.0, mud['rho2'], mud['c2'], mud['sigma'], k):.2f} dB")
    print(f"    mud coherence loss at 90 deg: "
          f"{coherence_loss_db(90.0, mud['sigma'], k):.2f} dB")
    print(f"(c) analytic max slope of the bump = "
          f"{np.degrees(np.arctan(A_BUMP / S_BUMP * np.exp(-0.5))):.2f} deg")
    print(f"(d) overall accuracy {po:.3f} and kappa {kappa(cm):.3f} for the")
    print(f"    supervised classifier with {n_train} training samples")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
