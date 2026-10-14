"""Log interpretation: a full petrophysical workflow with a Monte Carlo budget.

The workflow is the one used in practice, and the demonstration reports the
uncertainty of the answer together with its dominant source:

  1. Vsh from a natural-gamma index, using a stated shale baseline and matrix
     baseline.
  2. Porosity from a density log, using a matrix and fluid density.
  3. Water saturation from Archie, using a porosity, a formation-water
     resistivity and the Archie parameters.
  4. MONTE CARLO UNCERTAINTY: a, m, n, Rw, the matrix density and the shale
     baselines are all uncertain, and the script samples them to produce a
     distribution of Sw and a ranked uncertainty budget.

All log values, baselines and parameter uncertainties are STATED SYNTHETIC INPUTS.
No parameter is a remembered literature value presented as fact; each is given as
a range with its width stated in the script.

Run:  python3 petrophysics_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    section("1. The synthetic log readings at one depth")
    gr, gr_sand, gr_shale = 62.0, 22.0, 110.0      # SYNTHETIC API, all three
    rho_b = 2320.0                                  # SYNTHETIC bulk density
    rho_ma, rho_fl = 2650.0, 1000.0                 # SYNTHETIC matrix, fluid
    rt = 18.0                                       # SYNTHETIC deep resistivity
    print(f"GR = {gr:.0f} API (sand baseline {gr_sand:.0f}, shale baseline "
          f"{gr_shale:.0f})")
    print(f"rho_b = {rho_b:.0f} kg/m^3 (matrix {rho_ma:.0f}, fluid {rho_fl:.0f})")
    print(f"Rt = {rt:.1f} ohm m")

    section("2. Point estimate")
    igr = (gr - gr_sand) / (gr_shale - gr_sand)
    vsh = 0.33 * (2.0 ** (2.0 * igr) - 1.0)        # stated non-linear Vsh relation
    vsh = float(np.clip(vsh, 0.0, 1.0))
    phi = (rho_b - rho_ma) / (rho_fl - rho_ma)
    phi_eff = max(phi - vsh * 0.10, 1e-6)          # stated shale-porosity correction
    a_arc, m_arc, n_arc, rw = 1.0, 2.0, 2.0, 0.12
    sw = (a_arc * rw / (phi_eff ** m_arc * rt)) ** (1.0 / n_arc)
    sw = float(np.clip(sw, 0.0, 1.0))
    print(f"I_GR = {igr:.3f} -> Vsh = {vsh:.3f}")
    print(f"total density porosity = {phi:.3f}; shale-corrected effective "
          f"porosity = {phi_eff:.3f}")
    print(f"Archie Sw = {sw:.3f}  (so hydrocarbon saturation = {1 - sw:.3f})")
    print("Every one of those four relations contains at least one constant chosen\n"
          "by the analyst.  The point estimate is therefore a point estimate of an\n"
          "interval, and the next section measures the interval.")

    section("3. Monte Carlo uncertainty budget")
    rng = np.random.default_rng(20261014)
    n = 200_000
    # SYNTHETIC parameter uncertainties, each stated as a relative or absolute
    # 1-sigma width chosen for this demonstration.
    a_s = rng.normal(a_arc, 0.10 * a_arc, n)
    m_s = rng.normal(m_arc, 0.10 * m_arc, n)
    n_s = rng.normal(n_arc, 0.10 * n_arc, n)
    rw_s = rng.normal(rw, 0.20 * rw, n)
    rho_ma_s = rng.normal(rho_ma, 40.0, n)
    vsh_scale_s = rng.normal(1.0, 0.20, n)

    phi_s = (rho_b - rho_ma_s) / (rho_fl - rho_ma_s)
    phi_eff_s = np.maximum(phi_s - vsh * vsh_scale_s * 0.10, 1e-6)
    sw_s = np.clip((a_s * rw_s / (phi_eff_s ** m_s * rt)) ** (1.0 / n_s), 0.0, 1.0)
    q = np.percentile(sw_s, [5, 25, 50, 75, 95])
    print(f"samples = {n}")
    print("Sw percentiles 5/25/50/75/95 = "
          + " / ".join(f"{v:.3f}" for v in q))
    print(f"Sw point estimate           = {sw:.3f}")
    print(f"90 per cent interval width  = {q[4] - q[0]:.3f}")
    print(f"hydrocarbon saturation range at 90 per cent = "
          f"{1 - q[4]:.3f} to {1 - q[0]:.3f}")

    print("\nranked contribution to the variance of Sw (one-at-a-time, others "
          "fixed):")
    base = sw
    terms = {
        "a  (+/-10 per cent)": (a_arc * 1.1, a_arc * 0.9),
        "m  (+/-10 per cent)": (m_arc * 1.1, m_arc * 0.9),
        "n  (+/-10 per cent)": (n_arc * 1.1, n_arc * 0.9),
        "Rw (+/-20 per cent)": (rw * 1.2, rw * 0.8),
        "rho_ma (+/-40 kg/m^3)": (rho_ma + 40.0, rho_ma - 40.0),
    }
    ranked = []
    for name, (hi, lo) in terms.items():
        def sw_at(a_v=a_arc, m_v=m_arc, n_v=n_arc, rw_v=rw, rho_v=rho_ma):
            p = (rho_b - rho_v) / (rho_fl - rho_v)
            pe = max(p - vsh * 0.10, 1e-6)
            return float(np.clip((a_v * rw_v / (pe ** m_v * rt)) ** (1.0 / n_v),
                                 0.0, 1.0))
        if name.startswith("a"):
            spread = sw_at(a_v=hi) - sw_at(a_v=lo)
        elif name.startswith("m"):
            spread = sw_at(m_v=hi) - sw_at(m_v=lo)
        elif name.startswith("n"):
            spread = sw_at(n_v=hi) - sw_at(n_v=lo)
        elif name.startswith("Rw"):
            spread = sw_at(rw_v=hi) - sw_at(rw_v=lo)
        else:
            spread = sw_at(rho_v=hi) - sw_at(rho_v=lo)
        ranked.append((abs(spread), name, spread))
    for mag, name, spread in sorted(ranked, reverse=True):
        print(f"  {name:26s} delta Sw = {spread:+.3f}")

    section("4. What the budget says to do next")
    print("The largest single contributor is not the log reading: it is one of the\n"
          "Archie or matrix parameters.  The consequences are concrete -- if 'n' or\n"
          "Rw dominates, measure Rw from a produced-water sample rather than\n"
          "assuming it; if the matrix density dominates, identify the mineralogy\n"
          "from a crossplot or a core measurement.  Buying a better density log will\n"
          "not narrow the answer.  This is the same calculation as the measurement\n"
          "floor of module 05-07, applied to petrophysics: find the dominant term\n"
          "before spending money.")
    print("\nA final, necessary warning: a Monte Carlo over parameter distributions\n"
          "quantifies the MODEL uncertainty for the assumed relations.  It says\n"
          "nothing about whether Archie's law applies to this rock.  That is\n"
          "structural uncertainty, and it is larger than everything above.")


if __name__ == "__main__":
    main()
