"""A tiny, reusable rock-physics module: seismic velocities from elastic moduli.

Run:  python3 velocity_lib.py       (executes the module's self-test)
Requires: Python standard library only.

This file is the worked example for lesson 03-01-04.  It is deliberately a
*separate file* rather than a second half of the demo, because the lesson's
claim is that a formula becomes trustworthy only when it is packaged as a
named, documented, importable function with its own test.

All values are for an idealised isotropic elastic medium.  The relations are
exact within that model and wrong outside it: the anisotropy of a real rock
changes both speeds by several per cent, and a fluid-saturated rock needs
Gassmann substitution, which is not implemented here.
"""

from __future__ import annotations

import math

__all__ = [
    "vp_from_moduli",
    "vs_from_moduli",
    "poisson_ratio",
    "impedance",
    "vp_vs_ratio",
    "two_way_time",
    "VELOCITY_MODEL",
]

# Nominal elastic parameters for three idealised media.
# These are teaching values, not measurements of any named rock.
VELOCITY_MODEL = {
    "sandstone (nominal)": {"rho": 2350.0, "lam": 9.0e9, "mu": 8.0e9},
    "limestone (nominal)": {"rho": 2600.0, "lam": 2.0e10, "mu": 2.1e10},
    "steel (nominal)":     {"rho": 7850.0, "lam": 1.1e11, "mu": 8.2e10},
}


def vp_from_moduli(lam: float, mu: float, rho: float) -> float:
    """P-wave speed in m/s: ``sqrt((lambda + 2*mu) / rho)``.

    Parameters
    ----------
    lam : float
        First Lame parameter, in Pa (N m^-2).
    mu : float
        Shear modulus, in Pa.  Must be positive for a solid.
    rho : float
        Mass density, in kg m^-3.  Must be positive.

    Raises
    ------
    ValueError
        If ``rho`` is not positive, or if ``mu`` is not positive.

    Examples
    --------
    >>> round(vp_from_moduli(9.0e9, 8.0e9, 2350.0), 1)
    3261.6
    """
    if rho <= 0.0:
        raise ValueError(f"density must be positive, got {rho!r}")
    if mu <= 0.0:
        raise ValueError(f"shear modulus must be positive, got {mu!r}")
    return math.sqrt((lam + 2.0 * mu) / rho)


def vs_from_moduli(mu: float, rho: float) -> float:
    """S-wave speed in m/s: ``sqrt(mu / rho)``.

    A fluid has ``mu = 0``, so ``vs_from_moduli`` would return 0.0 for a fluid
    rather than raising: a fluid *does* transmit no shear wave.  The caller
    decides whether that is the answer they want.
    """
    if rho <= 0.0:
        raise ValueError(f"density must be positive, got {rho!r}")
    if mu < 0.0:
        raise ValueError(f"shear modulus cannot be negative, got {mu!r}")
    return math.sqrt(mu / rho)


def poisson_ratio(vp: float, vs: float) -> float:
    """Poisson's ratio from the two speeds.

    ``nu = (vp^2 - 2*vs^2) / (2*(vp^2 - vs^2))``.  For a physical isotropic
    solid, ``-1 < nu <= 0.5``; a value outside that range means the input
    speeds are inconsistent, which is a check the caller can use.
    """
    if vs <= 0.0:
        raise ValueError(f"S-wave speed must be positive, got {vs!r}")
    if vp <= vs:
        raise ValueError("an isotropic solid requires vp > vs")
    vp2, vs2 = vp * vp, vs * vs
    return (vp2 - 2.0 * vs2) / (2.0 * (vp2 - vs2))


def impedance(rho: float, vp: float) -> float:
    """Acoustic impedance ``Z = rho * vp``, in kg m^-2 s^-1 (a ray).

    The normal-incidence reflection coefficient between two media is
    ``(Z2 - Z1) / (Z2 + Z1)``; the impedance *contrast*, not the absolute
    speed, is what a reflection survey images.
    """
    return rho * vp


def vp_vs_ratio(vp: float, vs: float) -> float:
    """The ratio ``vp / vs``, the standard lithology discriminant."""
    if vs <= 0.0:
        raise ValueError("vs must be positive")
    return vp / vs


def two_way_time(depth_m: float, velocity: float) -> float:
    """Two-way vertical travel time in seconds.

    ``t0 = 2 * depth / velocity``.  Assumes a straight vertical ray; a dipping
    reflector or a velocity gradient requires a different (and larger) time.
    """
    if velocity <= 0.0:
        raise ValueError("velocity must be positive")
    return 2.0 * depth_m / velocity


def _self_test() -> None:
    """Every assertion here is a physical invariant, not a magic number."""
    vp = vp_from_moduli(9.0e9, 8.0e9, 2350.0)
    vs = vs_from_moduli(8.0e9, 2350.0)
    assert vp > vs > 0.0, (vp, vs)
    nu = poisson_ratio(vp, vs)
    assert -1.0 < nu < 0.5, nu
    # A fluid transmits no shear wave.
    assert vs_from_moduli(0.0, 1000.0) == 0.0
    # Impedance is linear in each factor.
    assert impedance(2000.0, 3000.0) == 2.0 * impedance(1000.0, 3000.0)
    # A sphere of unit density and unit velocity has unit impedance.
    assert abs(impedance(1.0, 1.0) - 1.0) < 1e-15
    # Guard rails must actually guard.
    for bad in (0.0, -1.0):
        try:
            vp_from_moduli(9.0e9, 8.0e9, bad)
        except ValueError:
            pass
        else:
            raise AssertionError("non-positive density was accepted")
    print("velocity_lib: all self-tests passed")


if __name__ == "__main__":
    _self_test()
