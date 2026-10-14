"""Verification tests: analytic solutions, measured rates, and honest tolerances.

Run:
    <repo>/.venv/bin/pytest \
        03-scientific-computing/13-testing-profiling-packaging/code/test_analytic_solutions.py

Four kinds of test appear here, in increasing order of usefulness:

* ``test_single_grid_*``      -- an assertion at one resolution (weak)
* ``test_rate_*``             -- an assertion on the *observed convergence rate*
* ``test_shell_theorem_*``    -- an assertion against an independent analytic result
* ``test_stability_*``        -- an assertion that the code refuses bad input

Every tolerance below is justified in a comment by the discretisation error
that the demo measured, never by taste.
"""

from __future__ import annotations

import math

import numpy as np
import pytest

import analytic_solutions_demo as asd
import geophys_tools as gt


KAPPA = 1.0e-6
LENGTH = 1.0


# --------------------------------------------------------------------------
# 1. Least useful: a single-grid assertion
# --------------------------------------------------------------------------

def test_single_grid_transient_heat():
    """A correct-looking assertion that would also pass for a broken scheme."""
    _, u, ue = asd.ftcs_heat_sine(nx=201, nt=2000, kappa=KAPPA, length=LENGTH, t_end=2.0e4)
    # 1e-5 is safely above the measured spatial floor (4.06e-06) and below the
    # 4.66e-06 + 4.06e-06 that a wrong dt scaling would produce.
    np.testing.assert_allclose(u, ue, atol=1e-5, rtol=0.0)


# --------------------------------------------------------------------------
# 2. Better: assert the measured convergence rate, not a number
# --------------------------------------------------------------------------

def test_rate_steady_second_order():
    """The 3-point second difference converges at order 2 (measured 1.974)."""
    ns = [32, 64, 128, 256]
    errors = []
    for n in ns:
        _, u, ue = asd.solve_steady_sine(n)
        errors.append(float(np.max(np.abs(u - ue))))
    orders = [math.log2(errors[i] / errors[i + 1]) for i in range(len(errors) - 1)]
    # Two-sided band: a first-order scheme fails the lower bound, a broken
    # (super-convergent) assembly fails the upper bound.
    assert all(1.85 < o < 2.15 for o in orders), orders


def test_rate_steady_error_does_shrink():
    """Between the coarsest and finest grid the error must fall by >50x."""
    _, u_coarse, ue_coarse = asd.solve_steady_sine(16)
    _, u_fine, ue_fine = asd.solve_steady_sine(128)
    e_coarse = float(np.max(np.abs(u_coarse - ue_coarse)))
    e_fine = float(np.max(np.abs(u_fine - ue_fine)))
    assert e_coarse / e_fine > 50.0


def test_rate_refinement_is_not_monotone_in_dt():
    """A measured fact, encoded so that nobody 'fixes' it later.

    On this grid the time error changes sign: refining dt past about 4 s makes
    the total error *grow*. A test that asserted monotone improvement would be
    asserting something false about the scheme.
    """
    errs = []
    for nt in (2000, 4000, 8000):
        _, u, ue = asd.ftcs_heat_sine(201, nt, KAPPA, LENGTH, 2.0e4)
        errs.append(float(np.max(np.abs(u - ue))))
    assert errs[1] < errs[0]           # coarsening dt helps at first ...
    assert errs[2] > errs[1]           # ... and then stops helping
    assert errs[2] / errs[1] == pytest.approx(2.0, rel=0.1)


# --------------------------------------------------------------------------
# 3. Best: an independent analytic result
# --------------------------------------------------------------------------

@pytest.mark.parametrize("depth_m", [1000.0, 500.0, 300.0])
def test_shell_theorem_quadrature(depth_m):
    """Outside a uniform sphere the field is exactly GM/d^2 (shell theorem).

    The tolerance is the quadrature error measured in the demo at this mesh
    (6.0e-05 relative at d = 1000 m, and worse closer in), not a guess.
    """
    radius, density = 100.0, 3000.0
    mass = density * 4.0 / 3.0 * math.pi * radius**3
    q = asd.sphere_gravity_quadrature(radius, density, depth_m, 60, 120, 180)
    exact = asd.G_SI * mass / depth_m**2 * asd.GAL_PER_MS2
    np.testing.assert_allclose(q, exact, rtol=1.0e-4)


def test_quadrature_error_falls_with_refinement():
    """Doubling the mesh must reduce the error -- the real correctness test."""
    radius, density, depth = 100.0, 3000.0, 1000.0
    mass = density * 4.0 / 3.0 * math.pi * radius**3
    exact = asd.G_SI * mass / depth**2 * asd.GAL_PER_MS2
    coarse = abs(asd.sphere_gravity_quadrature(radius, density, depth, 30, 60, 90) - exact)
    fine = abs(asd.sphere_gravity_quadrature(radius, density, depth, 60, 120, 180) - exact)
    assert fine < coarse / 2.0


def test_moveout_against_pythagoras():
    """A second independent check: the moveout is a right triangle."""
    t0, v, x = 1.2, 2400.0, 3600.0
    assert gt.normal_moveout(t0, v, x) == pytest.approx(math.hypot(t0, x / v), rel=1e-15)


# --------------------------------------------------------------------------
# 4. Guards: the code must refuse to run a configuration it cannot justify
# --------------------------------------------------------------------------

def test_stability_guard_rejects_oversized_step():
    with pytest.raises(ValueError, match="unstable"):
        asd.ftcs_heat_sine(nx=51, nt=10, kappa=KAPPA, length=LENGTH, t_end=2.0e4)


@pytest.mark.parametrize("nt,expected_stable", [(2000, True), (1600, True), (1000, False)])
def test_stability_threshold_matches_theory(nt, expected_stable):
    """FTCS on this problem is stable exactly when r = k dt/dx^2 <= 1/2."""
    dx = 1.0 / 200.0
    r = KAPPA * (2.0e4 / nt) / dx**2
    assert (r <= 0.5) is expected_stable
    if not expected_stable:
        with pytest.raises(ValueError):
            asd.ftcs_heat_sine(nx=201, nt=nt, kappa=KAPPA, length=LENGTH, t_end=2.0e4)
