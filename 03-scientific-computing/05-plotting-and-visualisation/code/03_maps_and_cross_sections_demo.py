"""Maps, cross-sections and the cost of plotting longitude as if it were x.

Run:  .venv/bin/python 03_maps_and_cross_sections_demo.py
Requires: numpy, matplotlib (Agg), pyproj, cartopy.

Companion to lesson 03-05-03.

Part 1 measures, with pyproj, how much a degree of longitude is worth in
metres at different latitudes. Part 2 measures the Mercator scale factor and
compares the ellipsoidal value from pyproj with the spherical 1/cos(phi).
Part 3 draws one set of synthetic epicentres on three Cartopy projections so
that the disagreement between them is visible rather than described. Part 4
builds a crustal cross-section and computes, rather than asserts, its vertical
exaggeration, then redraws it with true metric aspect.

Cartopy downloads Natural Earth coastlines on first use and caches them. If the
download is unavailable the map parts still run and report the failure instead
of aborting the script.

Images are written to a temporary directory, never into the repository.
"""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo03_")
RNG = np.random.default_rng(19920817)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def part1_degree_of_longitude():
    section("1. A degree of longitude is not a fixed distance")

    from pyproj import Geod

    geod = Geod(ellps="WGS84")
    print("  WGS84 ellipsoid, geodesic distance for 1 degree of longitude")
    print()
    print(f"  {'latitude':>9}{'1 deg lon (km)':>17}{'1 deg lat (km)':>17}"
          f"{'lon ratio':>12}{'cos(lat)':>10}")
    base = None
    for lat in (0.0, 30.0, 45.0, 60.0, 75.0, 89.0):
        _, _, d_lon = geod.inv(0.0, lat, 1.0, lat)
        _, _, d_lat = geod.inv(0.0, lat, 0.0, lat + 1.0)
        if base is None:
            base = d_lon
        print(f"  {lat:>9.1f}{d_lon / 1000:>17.3f}{d_lat / 1000:>17.3f}"
              f"{d_lon / base:>12.4f}{np.cos(np.radians(lat)):>10.4f}")
    print()
    print("  At the equator one degree of longitude is 111.319 km; at 60 degrees")
    print("  north (Oslo, Bergen) it is 55.799 km, a factor of 1.99 -- exactly")
    print("  cos 60 = 0.500 to three decimals. A scatter plot of (longitude,")
    print("  latitude) on a linear grid gives both bars the SAME width in pixels,")
    print("  so it misstates the ground distance by that factor. Latitude barely")
    print("  varies (110.6 to 111.7 km per degree), so the distortion is")
    print("  one-sided: the plot shears east-west and leaves north-south alone.")


def part2_mercator_scale():
    section("2. The Mercator scale factor and why Greenland looks huge")

    from pyproj import Transformer

    fwd = Transformer.from_crs("EPSG:4326", "EPSG:3395", always_xy=True)
    print("  EPSG:3395 World Mercator; numerical dy/d(phi) against 1/cos(phi)")
    print()
    print(f"  {'phi (deg)':>10}{'dy/dphi (m/deg)':>18}{'scale factor':>14}"
          f"{'1/cos(phi)':>12}{'rel. diff':>11}")
    dphi = 1e-4
    ref = None
    for phi in (0.0, 30.0, 45.0, 60.0, 70.0, 80.0):
        _, y1 = fwd.transform(0.0, phi)
        _, y2 = fwd.transform(0.0, phi + dphi)
        slope = (y2 - y1) / dphi
        if ref is None:
            ref = slope
        scale = slope / ref
        spherical = 1.0 / np.cos(np.radians(phi))
        print(f"  {phi:>10.1f}{slope:>18.1f}{scale:>14.4f}{spherical:>12.4f}"
              f"{abs(scale - spherical) / spherical:>11.4f}")
    print()
    print("  The ellipsoidal scale factor tracks the spherical 1/cos(phi) to")
    print("  within 0.7 per cent at worst in the table above; the residual is the")
    print("  ellipsoid's eccentricity correction, which the sphere cannot supply.")
    print("  At 80 degrees north the map stretches east-west distances by a")
    print("  factor of 5.80, which is why a Mercator wall map is the wrong choice")
    print("  for any polar basin.")


def part3_projection_comparison():
    section("3. One dataset, three projections: the projection is an argument")

    import cartopy.crs as ccrs

    # SYNTHETIC epicentres: a linear belt plus scatter, deliberately spanning
    # low and high latitude so the projections disagree.
    n = 220
    lon = 10.0 + 3.0 * RNG.standard_normal(n)
    lat = -40.0 + 1.1 * lon + 6.0 * RNG.standard_normal(n)

    projections = [
        ("PlateCarree", ccrs.PlateCarree()),
        ("Robinson", ccrs.Robinson()),
        ("Orthographic (30E, 20N)", ccrs.Orthographic(central_longitude=30.0,
                                                      central_latitude=20.0)),
    ]

    fig = plt.figure(figsize=(13.0, 4.2), dpi=150)
    for i, (name, proj) in enumerate(projections, start=1):
        ax = fig.add_subplot(1, 3, i, projection=proj)
        ax.set_global()
        try:
            ax.coastlines(resolution="110m", linewidth=0.4)
            status = "coastlines drawn"
        except Exception as exc:  # network/cache unavailable
            status = f"coastlines unavailable ({type(exc).__name__})"
        ax.scatter(lon, lat, s=6, c="crimson", alpha=0.75,
                   transform=ccrs.PlateCarree())  # <- the DATA crs, not the map crs
        ax.gridlines(draw_labels=False, linewidth=0.3, color="0.6")
        ax.set_title(name, fontsize=9)
        print(f"  panel {i}: {name:<26} aspect={ax.get_aspect():<8} {status}")

    fig.suptitle("SYNTHETIC epicentre belt -- same 220 points, three projections",
                 fontsize=10)
    path = os.path.join(OUTDIR, "03_projections.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi)")
    print()
    print("  Note the keyword that matters: `transform=ccrs.PlateCarree()` tells")
    print("  Cartopy the CRS of the DATA. The projection of the Axes decides how")
    print("  it is drawn. Omitting the transform is the single most common")
    print("  Cartopy error and it silently treats degrees as projected metres.")
    print("  Panel 1 preserves neither area nor angle away from the equator;")
    print("  panel 2 preserves neither exactly but distorts area only mildly;")
    print("  panel 3 is an azimuthal view where the visible hemisphere hides the")
    print("  rest of the belt. No projection is right -- only stated.")


def part4_cross_section_ve():
    section("4. A cross-section, and the vertical exaggeration it hides")

    # SYNTHETIC 2-D velocity model: a sediment wedge over basement.
    x_km = np.linspace(0.0, 400.0, 401)
    z_km = np.linspace(0.0, 40.0, 201)
    X, Z = np.meshgrid(x_km, z_km)
    basement_top = 8.0 - 5.0 * np.tanh((X - 220.0) / 70.0)   # 3-13 km deep
    v = np.where(Z < basement_top, 2.2 + 0.05 * Z, 5.8 + 0.02 * Z)
    top_profile = basement_top[0, :]

    W_in, H_in = 6.4, 2.4
    h_scale = 400.0 / W_in     # km per inch, horizontally
    v_scale = 40.0 / H_in      # km per inch, vertically
    ve = h_scale / v_scale
    print(f"  panel size {W_in} x {H_in} in for 400 km x 40 km of section")
    print(f"    horizontal scale = {h_scale:.3f} km per inch")
    print(f"    vertical scale   = {v_scale:.3f} km per inch")
    print(f"    vertical exaggeration = {ve:.3f}")
    print()
    print(f"  A reader who assumes 1:1 sees every dip {ve:.2f} times steeper than")
    print("  it is. The only honest fixes are to state the exaggeration in the")
    print("  caption or to draw true metric aspect.")

    # Height needed for genuine 1:1 aspect at the chosen width.
    true_h_in = 40.0 / h_scale
    print(f"  a 1:1 panel of the same 400 km width would be {true_h_in:.3f} in tall")
    print(f"    (a strip {H_in / true_h_in:.1f} times thinner than the panel drawn)")

    fig, axes = plt.subplots(2, 1, figsize=(W_in, 2 * H_in + 1.0), dpi=150)
    for ax, equal in zip(axes, (False, True)):
        im = ax.pcolormesh(x_km, z_km, v, cmap="viridis", shading="auto")
        ax.plot(x_km, top_profile, color="k", lw=1.0)
        ax.set_ylim(40.0, 0.0)     # depth increases downward: invert the axis
        ax.set_xlabel("distance x (km)")
        ax.set_ylabel("depth z (km)")
        if equal:
            ax.set_aspect("equal")
            ax.set_title("true 1:1 aspect -- topography and structure, no exaggeration",
                         fontsize=8)
        else:
            ax.set_aspect("auto")
            ax.set_title(f"VE = {ve:.2f}:1 -- the conventional view", fontsize=8)
        fig.colorbar(im, ax=ax, label=r"$v_p$ (km s$^{-1}$, SYNTHETIC)")
    fig.tight_layout()
    path = os.path.join(OUTDIR, "03_cross_section.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 2 panels)")
    print()
    print("  Note also that z increases DOWNWARD. `ax.set_ylim(40, 0)` inverts")
    print("  the axis. Plotting depth increasing upward puts the Moho above the")
    print("  surface, which is not a stylistic preference.")


def main():
    part1_degree_of_longitude()
    part2_mercator_scale()
    part3_projection_comparison()
    part4_cross_section_ve()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
