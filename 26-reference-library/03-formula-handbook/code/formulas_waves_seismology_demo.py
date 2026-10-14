"""Check the waves, elasticity and seismology formula sheet with explicit numbers.

Print-only, seeded, no plots, no file I/O. Numbers quoted in
26-03-03-formulas-waves-seismology.md come from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_waves_seismology_demo.py
"""

from __future__ import annotations

import math

import numpy as np

SEED = 20261014
RHO = 2700.0      # kg/m^3, nominal crustal rock
VP = 6000.0       # m/s
VS = 3500.0       # m/s


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Waves, elasticity and seismology formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print("PROVENANCE: SYNTHETIC -- elastic parameters below are chosen, not measured.")

    banner(1, "Isotropic elastic moduli from rho, Vp, Vs")
    mu = RHO * VS**2
    lame = RHO * (VP**2 - 2.0 * VS**2)
    bulk = lame + 2.0 * mu / 3.0
    poisson = (VP**2 - 2.0 * VS**2) / (2.0 * (VP**2 - VS**2))
    young = mu * (3.0 * lame + 2.0 * mu) / (lame + mu)
    print(f"  rho = {RHO:.0f} kg/m^3, Vp = {VP:.0f} m/s, Vs = {VS:.0f} m/s")
    print(f"  mu (shear modulus) = {mu:.6e} Pa = {mu/1e9:.4f} GPa")
    print(f"  lambda             = {lame:.6e} Pa = {lame/1e9:.4f} GPa")
    print(f"  K (bulk modulus)   = {bulk:.6e} Pa = {bulk/1e9:.4f} GPa")
    print(f"  E (Young's modulus)= {young:.6e} Pa = {young/1e9:.4f} GPa")
    print(f"  nu (Poisson ratio) = {poisson:.6f}")
    check_vp = math.sqrt((lame + 2.0 * mu) / RHO)
    check_vs = math.sqrt(mu / RHO)
    print(f"  back-substitution: Vp = {check_vp:.3f} m/s, Vs = {check_vs:.3f} m/s")
    print(f"  Vp/Vs ratio        = {VP/VS:.6f}")

    banner(2, "Snell's law: ray parameter and critical angle")
    p_ray = math.sin(math.radians(30.0)) / VP
    angle_layer2 = math.degrees(math.asin(p_ray * 8000.0))
    crit = math.degrees(math.asin(VP / 8000.0))
    print(f"  incidence 30 deg in Vp = {VP:.0f} m/s -> ray parameter p = {p_ray:.6e} s/m")
    print(f"  refraction angle in Vp = 8000 m/s      = {angle_layer2:.6f} deg")
    print(f"  critical angle                         = {crit:.6f} deg")
    print(f"  horizontal slowness check: p*8000      = {p_ray * 8000.0:.10f} (= sin 30 deg)")

    banner(3, "Acoustic impedance and normal-incidence reflection")
    z1, z2 = 2200.0 * 2000.0, 2400.0 * 2600.0
    refl = (z2 - z1) / (z2 + z1)
    print(f"  Z1 = {z1:.1f} kg m^-2 s^-1 (rho*v), Z2 = {z2:.1f} kg m^-2 s^-1")
    print(f"  R (normal incidence) = {refl:+.6f}, T = {1.0 - refl:+.6f}")
    print(f"  energy: R^2 = {refl**2:.6f}, 1 - R^2 = {1.0 - refl**2:.6f}")

    banner(4, "Travel time, NMO and two-way time")
    t0, offset, v_rms = 1.20, 1500.0, 3000.0
    t_nmo = math.sqrt(t0**2 + (offset / v_rms) ** 2)
    print(f"  t0 = {t0:.2f} s, offset x = {offset:.0f} m, v_rms = {v_rms:.0f} m/s")
    print(f"  hyperbolic travel time = {t_nmo:.6f} s")
    print(f"  normal moveout dt      = {t_nmo - t0:.6f} s = {(t_nmo - t0)*1000:.3f} ms")
    print(f"  quadratic approx dt    = {offset**2 / (2.0 * t0 * v_rms**2):.6f} s")
    depth = v_rms * t0 / 2.0
    print(f"  depth from t0 and v_rms= {depth:.1f} m (assuming constant velocity)")

    banner(5, "Rayleigh wave: phase and group velocity from a dispersion relation")
    c0, b_rate = 3000.0, 0.05          # c(f) = c0 * (1 - b_rate / f), with f in Hz
    phase = lambda f_hz: c0 * (1.0 - b_rate / f_hz)
    k_cyc = lambda f_hz: f_hz / phase(f_hz)     # cycles per metre
    for f_hz in (0.10, 0.20, 0.40):
        print(
            f"  f = {f_hz:.2f} Hz, T = {1.0 / f_hz:.2f} s -> c = {phase(f_hz):.3f} m/s"
        )
    secant = (phase(0.40) * 0.40 - phase(0.20) * 0.20) / (0.40 - 0.20)
    f0, df = 0.30, 1.0e-5
    local = 2.0 * df / (k_cyc(f0 + df) - k_cyc(f0 - df))
    print(f"  secant group velocity over 0.2-0.4 Hz = {secant:.3f} m/s")
    print(f"  local group velocity at 0.30 Hz       = {local:.3f} m/s")
    print(f"  phase velocity at 0.30 Hz             = {phase(f0):.3f} m/s")

    banner(6, "Seismic moment and moment magnitude")
    mu_src, area, slip = 3.0e10, 1.0e9, 2.0
    moment = mu_src * area * slip
    mw = (2.0 / 3.0) * (math.log10(moment) - 9.1)
    print(f"  mu = {mu_src:.3e} Pa, fault area = {area:.3e} m^2, mean slip = {slip:.1f} m")
    print(f"  M0 = {moment:.6e} N m")
    print(f"  Mw = {mw:.6f} (dimensionless)")
    print(f"  log10 energy estimate (log10 E = 1.5 Mw + 4.8) -> E = {10**(1.5*mw + 4.8):.4e} J")

    print("\nAll six checks completed; exit status 0.")


if __name__ == "__main__":
    main()
