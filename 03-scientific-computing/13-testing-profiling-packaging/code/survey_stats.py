"""A small gravity-reduction module -- the subject of the coverage lesson.

Two defects are planted here deliberately. Both survive a test suite with 100%
line coverage, and one of them survives a *branch* test as well. The third
function shows a branch that no test in ``coverage_demo.py`` reaches.

This file is teaching material, not a correct library: do not copy it.
"""

from __future__ import annotations

import numpy as np

FREE_AIR_GRADIENT_MGAL_PER_M = 0.3086


def free_air_anomaly(elevation_m: float, observed_mgal: float) -> float:
    """Free-air corrected gravity anomaly, mGal.

    Defect 1 (sign): the free-air correction must be ADDED to the observed
    value to refer it to the ellipsoid, because observed gravity falls with
    elevation. This function subtracts it, producing an anomaly wrong by
    2 * 0.3086 * h mGal -- 61.7 mGal at 100 m of relief.
    """
    return observed_mgal - FREE_AIR_GRADIENT_MGAL_PER_M * elevation_m


def mean_elevation(elevations_m: np.ndarray) -> float:
    """Arithmetic mean elevation, as used for a survey's datum statement."""
    return float(np.mean(elevations_m))


def station_anomaly(
    elevation_m: float,
    observed_mgal: float,
    terrain_correction_mgal: float | None = None,
) -> float:
    """Free-air and (optionally) terrain-corrected anomaly.

    Defect 2 (untested branch): the sign inside the ``if`` is wrong, and no
    test in the lesson ever passes a ``terrain_correction_mgal``, so the branch
    contributes zero coverage information and the defect ships.
    """
    anomaly = free_air_anomaly(elevation_m, observed_mgal)
    if terrain_correction_mgal is not None:
        anomaly -= terrain_correction_mgal
    return anomaly


def normal_gravity_mgal(latitude_deg: float) -> float:
    """Somigliana normal gravity on the GRS80 ellipsoid, in mGal.

        gamma(phi) = gamma_e (1 + k sin^2 phi) / sqrt(1 - e^2 sin^2 phi)

    with gamma_e = 9.7803267715 m/s^2, k = 0.001931851353 (the "gravitational
    flattening") and e^2 = 0.00669438002290.  Reference values: 978032.677
    mGal at the equator, 980619.9 mGal at 45 degrees, 983218.64 mGal at the
    pole.
    """
    lat = np.radians(latitude_deg)
    gamma_e, k, e2 = 9.7803267715, 0.001931851353, 0.00669438002290
    s2 = np.sin(lat) ** 2
    g = gamma_e * (1.0 + k * s2) / np.sqrt(1.0 - e2 * s2)
    return float(g * 1.0e5)
