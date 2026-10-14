"""Small geophysical helpers -- the object under test in lesson 01.

Every function here is short enough to check by hand, which is exactly why it
is a good test subject. Nothing imports anything outside the standard library
and NumPy, so the module loads in a fresh interpreter in milliseconds.

Units are stated in the docstring of every function: a test that does not know
the unit of its expected value is not a test.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

G_SI = 6.67430e-11            # m^3 kg^-1 s^-2
GAL_PER_MS2 = 1.0e5           # 1 m/s^2 = 1e5 mGal


def normal_moveout(t0_s: float, v_ms: float, offset_m: float) -> float:
    """Two-way time (s) at a source-receiver offset for a flat reflector.

    ``t(x) = sqrt(t0^2 + (x / v)^2)``.  ``t0_s`` is the zero-offset two-way
    time in seconds, ``v_ms`` the RMS velocity in m/s, ``offset_m`` the
    source-receiver distance in metres.
    """
    if v_ms <= 0:
        raise ValueError("velocity must be positive")
    if t0_s < 0 or offset_m < 0:
        raise ValueError("t0 and offset must be non-negative")
    return math.sqrt(t0_s * t0_s + (offset_m / v_ms) ** 2)


def point_mass_gravity_mgal(mass_kg: float, depth_m: float) -> float:
    """Vertical gravity anomaly of a point mass, in mGal.

    ``g_z = G M / d^2`` with ``d`` the depth in metres; converted to mGal by
    dividing by 1e-5 m/s^2.
    """
    if depth_m <= 0:
        raise ValueError("depth must be positive")
    return G_SI * mass_kg / depth_m**2 * GAL_PER_MS2


def spherical_free_air_gradient_mgal_per_m() -> float:
    """Spherical free-air gradient ``2 g / R``, in mGal/m.

    Dimensional reasoning: ``[g][R^-1] = m s^-2 m^-1 = s^-2``; one metre of
    elevation therefore changes gravity by ``2 g / R``.  With ``g = 9.80665``
    m/s^2 and ``R = 6.371e6`` m this gives **0.30785** mGal/m, not the
    conventional **0.3086** mGal/m: the conventional value additionally carries
    the flattening and centrifugal terms of normal gravity.  The 0.24% gap is
    measured in the lesson.
    """
    g = 9.80665           # m/s^2
    r = 6.371e6           # m
    return 2.0 * g / r * GAL_PER_MS2


def bouguer_slab_thickness_m(dg_mgal: float, drho_kgm3: float) -> float:
    """Thickness of an infinite horizontal slab from its gravity effect.

    ``dg = 2 pi G drho t``, so ``t = dg / (2 pi G drho)``.
    """
    if drho_kgm3 == 0:
        raise ValueError("density contrast must be non-zero")
    dg_si = dg_mgal / GAL_PER_MS2
    return dg_si / (2.0 * math.pi * G_SI * drho_kgm3)


def wrap_phase(phi_rad: float | np.ndarray) -> float | np.ndarray:
    """Wrap an angle to (-pi, pi]."""
    return (np.asarray(phi_rad) + np.pi) % (2.0 * np.pi) - np.pi


def synthetic_elevation_profile(n: int, seed: int | None = None) -> np.ndarray:
    """A reproducible synthetic elevation profile in metres.

    Uses the modern ``default_rng`` generator so that the stream is documented
    and stable for a given NumPy version.
    """
    rng = np.random.default_rng(seed)
    stations = np.linspace(0.0, 12_000.0, n)     # exactly four 3-km periods
    return 250.0 + 40.0 * np.sin(2 * np.pi * stations / 3_000.0) + rng.normal(0.0, 5.0, n)


def load_elevations(path: Path | str) -> np.ndarray:
    """Read a two-column (station_m, elevation_m) whitespace file."""
    data = np.loadtxt(path, comments="#")
    if data.ndim != 2 or data.shape[1] != 2:
        raise ValueError("expected two columns: station, elevation")
    return data


def dominant_frequency_hz(signal: np.ndarray, dt_s: float) -> float:
    """Frequency of the largest Fourier amplitude, in Hz."""
    spectrum = np.abs(np.fft.rfft(signal - signal.mean()))
    freqs = np.fft.rfftfreq(signal.size, d=dt_s)
    return float(freqs[int(np.argmax(spectrum))])
