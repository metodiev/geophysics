# Exercises — 06-06-06 Global Mantle Tomography and Its Geodynamic Interpretation

Worked answers are in
[06-global-mantle-tomography-solutions.md](06-global-mantle-tomography-solutions.md).
The lesson is
[06-global-mantle-tomography.md](../06-global-mantle-tomography.md) and the
demonstration is
[../code/global_mantle_tomography_demo.py](../code/global_mantle_tomography_demo.py).

## ★ Foundational

1. For the teaching profile $v(r) = 8.0\,(R/r)\ \mathrm{km\,s^{-1}}$ with
   $R = 6371$ km, compute $v$ at the surface and at a core-mantle boundary at
   $r = 3480$ km.
2. Solve $r/v(r) = p$ for the turning radius with $p = 423.3$ s, and convert it
   to a depth.
3. A travel-time residual of 0.8 s is measured by a ray turning at 1500 km
   depth. Using $\mathrm{d}T/\mathrm{d}\Delta = p$ with $p = 500$ s, compute the
   corresponding distance error in radians and in degrees.

## ★★ Applied

4. From the ray table, interpolate the turning depth of a ray with
   $p = 700$ s/rad, and state which two table rows you interpolated between.
5. In the angular-filter experiment a degree-12 input produced low-degree
   coefficients up to 6.07 per cent of the input amplitude. Compute the implied
   apparent degree-2 anomaly for a true degree-12 anomaly of 0.5 per cent, and
   state why a reader who only sees the degree-2 map would be misled.
6. The depth–amplitude table admits 0.827-1.086 per cent for depths of
   1200-1800 km at $\sigma = 1.0$ s. If the assumed noise level is doubled,
   argue from the residual column whether the admitted depth range widens or
   narrows, and estimate the amplitudes needed at 800 and 2200 km to fit within
   the new level.

## ★★★ Research-oriented

7. Design a joint inversion for a region where body-wave travel times alone
   admit a 800 km range of depths. State which second measurement type you would
   add, what its kernel looks like, and the quantitative criterion you would use
   to claim that the depth is now determined.
8. The synthetic conversion $\partial\ln v_s/\partial T = -1.0\times10^{-4}\
   \mathrm{K^{-1}}$ is a teaching value. List the physical effects that make the
   real conversion spatially variable, and state which of them would tend to make
   a published temperature anomaly *too large*.
