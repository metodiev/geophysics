"""A genuine pytest suite: fixtures, parametrisation and approximate comparison.

Run:
    <repo>/.venv/bin/pytest \
        03-scientific-computing/13-testing-profiling-packaging/code/test_pytest_basics.py

Every assertion below is one the lesson discusses. The suite is deliberately
small: five test functions, most of them parametrised, and it exercises
fixtures at three scopes, ``pytest.approx``, ``pytest.raises``, ``tmp_path``,
``monkeypatch``, a skip and an expected failure.
"""

from __future__ import annotations

import math
import sys

import numpy as np
import pytest

import geophys_tools as gt


# --------------------------------------------------------------------------
# Fixtures: shared setup, three scopes
# --------------------------------------------------------------------------

@pytest.fixture(scope="session")
def constants() -> dict[str, float]:
    """Physical constants, built once for the whole session."""
    return {
        "g": 9.80665,          # m/s^2, standard gravity
        "R": 6.371e6,          # m, mean Earth radius
        "G": 6.67430e-11,      # m^3 kg^-1 s^-2
    }


@pytest.fixture
def simple_profile() -> np.ndarray:
    """A three-station elevation profile, function scope (rebuilt per test)."""
    return np.array([100.0, 110.0, 120.0])


@pytest.fixture(scope="module")
def noisy_profile() -> np.ndarray:
    """A reproducible 512-sample synthetic profile, built once per module."""
    return gt.synthetic_elevation_profile(512, seed=20240101)


# --------------------------------------------------------------------------
# Approximate comparison
# --------------------------------------------------------------------------

def test_free_air_gradient_matches_spherical_formula():
    """The spherical 2g/R value is 0.30785 mGal/m, measured to 5 digits."""
    value = gt.spherical_free_air_gradient_mgal_per_m()
    assert value == pytest.approx(0.30785, rel=1e-5)
    assert abs(value - 0.3086) / 0.3086 < 3e-3     # 0.24% from the conventional value
    assert abs(value - 0.3086) * 1000.0 > 0.5      # >0.5 mGal over 1 km of relief


def test_point_mass_gravity_is_small_but_detectable():
    g_mgal = gt.point_mass_gravity_mgal(1.0e9, 300.0)
    assert g_mgal == pytest.approx(7.4156e-2, rel=1e-4)
    assert g_mgal > 0.01          # repeatability of a modern gravimeter


def test_inverse_square_routeings_are_not_bit_identical():
    """`d**-2` and `(1/d)**2` differ by 1 ulp -- so equality is the wrong test."""
    d = 300.0
    assert d ** -2 != (1.0 / d) ** 2
    assert d ** -2 == pytest.approx((1.0 / d) ** 2, rel=1e-15)


# --------------------------------------------------------------------------
# Parametrisation
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    ("t0_s", "v_ms", "offset_m", "expected_s"),
    [
        (1.0, 2000.0, 0.0, 1.0),                 # zero offset is exactly t0
        (1.0, 2000.0, 2000.0, math.sqrt(1.0 + 1.0)),   # 3-4-5 style: sqrt(2)
        (2.0, 1500.0, 3000.0, math.sqrt(4.0 + 4.0)),
        (1.0, 1000.0, 1000.0, math.sqrt(2.0)),
    ],
)
def test_normal_moveout(t0_s, v_ms, offset_m, expected_s):
    assert gt.normal_moveout(t0_s, v_ms, offset_m) == pytest.approx(expected_s, rel=1e-12)


def test_normal_moveout_offset_never_advances_time():
    """Monotonicity in offset, checked on a grid rather than at one point."""
    t0, v = 0.8, 2500.0
    times = np.array([gt.normal_moveout(t0, v, x) for x in (0.0, 500.0, 1000.0, 2000.0)])
    assert np.all(np.diff(times) > 0.0)
    assert times[0] == pytest.approx(t0, abs=0.0)


@pytest.mark.parametrize("bad", [
    (1.0, -1.0, 100.0),
    (1.0, 0.0, 100.0),
    (-1.0, 2000.0, 100.0),
    (1.0, 2000.0, -5.0),
])
def test_normal_moveout_rejects_unphysical_input(bad):
    with pytest.raises(ValueError):
        gt.normal_moveout(*bad)


def test_bouguer_slab_round_trip():
    """Thickness -> effect -> thickness must return the input."""
    for drho in (200.0, 400.0, 600.0):
        thickness = 1500.0
        dg = 2.0 * math.pi * gt.G_SI * drho * thickness * gt.GAL_PER_MS2
        assert gt.bouguer_slab_thickness_m(dg, drho) == pytest.approx(thickness, rel=1e-12)


# --------------------------------------------------------------------------
# Array-valued assertions
# --------------------------------------------------------------------------

def test_phase_wrapping_is_idempotent():
    phi = np.linspace(-20.0, 20.0, 401)
    once = gt.wrap_phase(phi)
    twice = gt.wrap_phase(once)
    np.testing.assert_allclose(once, twice, rtol=0.0, atol=1e-14)
    assert np.all(np.abs(once) <= np.pi + 1e-15)


def test_synthetic_profile_is_reproducible(noisy_profile):
    again = gt.synthetic_elevation_profile(512, seed=20240101)
    np.testing.assert_array_equal(noisy_profile, again)
    assert noisy_profile.size == 512
    assert float(noisy_profile.mean()) == pytest.approx(250.0, abs=1.0)


def test_synthetic_profile_differs_for_other_seed(noisy_profile):
    other = gt.synthetic_elevation_profile(512, seed=1)
    assert not np.array_equal(noisy_profile, other)


def test_dominant_frequency_of_a_known_sine():
    dt = 0.01
    t = np.arange(0.0, 10.0, dt)
    signal = np.sin(2 * np.pi * 2.0 * t)      # exactly 2 Hz
    assert gt.dominant_frequency_hz(signal, dt) == pytest.approx(2.0, abs=0.11)


# --------------------------------------------------------------------------
# Filesystem: tmp_path, and no network anywhere
# --------------------------------------------------------------------------

def test_load_elevations_round_trip(tmp_path):
    path = tmp_path / "line_a.dat"
    path.write_text("# station_m elevation_m\n0 100.0\n10 101.5\n20 99.0\n",
                    encoding="utf-8")
    data = gt.load_elevations(path)
    assert data.shape == (3, 2)
    np.testing.assert_allclose(data[:, 1], [100.0, 101.5, 99.0])


def test_load_elevations_rejects_one_column(tmp_path):
    path = tmp_path / "bad.dat"
    path.write_text("1\n2\n3\n", encoding="utf-8")
    with pytest.raises(ValueError):
        gt.load_elevations(path)


# --------------------------------------------------------------------------
# Environment: monkeypatch
# --------------------------------------------------------------------------

@pytest.mark.parametrize("threads", ["1", "4"])
def test_thread_environment_is_visible(monkeypatch, threads):
    monkeypatch.setenv("OMP_NUM_THREADS", threads)
    import os
    assert os.environ["OMP_NUM_THREADS"] == threads
    assert int(os.environ["OMP_NUM_THREADS"]) >= 1


# --------------------------------------------------------------------------
# Conditions: skip and expected failure
# --------------------------------------------------------------------------

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires modern typing syntax")
def test_modern_syntax_available():
    assert isinstance(gt.wrap_phase(0.0), np.floating | float)


@pytest.mark.xfail(reason="bitwise equality of two routeings is not a property of the physics")
def test_this_is_expected_to_fail():
    d = 300.0
    assert d ** -2 == (1.0 / d) ** 2
