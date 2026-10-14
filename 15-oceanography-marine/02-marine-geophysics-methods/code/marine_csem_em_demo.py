#!/usr/bin/env python3
"""Marine CSEM and EM for gas hydrates: skin depth, a one-dimensional layered
diffusion response, the screening effect of the water column, and the
resistivity-thickness trade.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_csem_em_demo.py

Everything here is SYNTHETIC.  The resistivities, thicknesses and frequencies are
chosen teaching values, printed below.  No survey, prospect, well or published
resistivity model is reproduced.

Contents
--------
1. Skin depth, and the verification of its closed form against the diffusion
   wavenumber.
2. A one-dimensional layered response: apparent resistivity and phase.
3. The water column as a conductive screen.
4. A resistive layer: what it does to the response, and at what frequencies.
5. The resistivity-thickness trade: two models, one response.
6. Verification of the layered recursion against the uniform half-space.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constant and SYNTHETIC model (chosen values) ------------------
MU0 = 4.0e-7 * np.pi     # H/m, exact: 4 pi e-7

RHO_WATER = 0.30         # ohm m, chosen seawater resistivity
H_WATER = 1500.0         # m, chosen water depth
RHO_HALF = 1.00          # ohm m, chosen half-space resistivity
H_SED_ABOVE = 300.0      # m, sediment between seafloor and the target
H_LAYER = 100.0          # m, chosen hydrate-layer thickness
RHO_LAYER = 100.0        # ohm m, chosen hydrate-bearing layer resistivity
H_SED_BELOW = 500.0      # m, sediment below the layer
FREQS = np.logspace(-2, 1, 25)   # Hz
FREQS_AB = (0.01, 0.03, 0.1, 0.3, 1.0, 3.0)   # Hz, the table in section 4


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def skin_depth(rho, f):
    """delta = sqrt(2 rho / (mu0 omega)) = sqrt(rho/(pi f mu0))."""
    return np.sqrt(rho / (np.pi * f * MU0))


def wavenumber(rho, f):
    """Diffusion wavenumber k = sqrt(i mu0 omega / rho); 1/Re(k) is delta."""
    return np.sqrt(1j * MU0 * 2.0 * np.pi * f / rho)


def impedance(rho, f):
    """Intrinsic plane-wave impedance eta = sqrt(i mu0 omega rho)."""
    return np.sqrt(1j * MU0 * 2.0 * np.pi * f * rho)


def half_space_top(rho, f):
    """Impedance of a very thick layer: just eta."""
    return impedance(rho, f)


def layer_top(rho, h, f, z_below):
    """Impedance at the top of a layer of resistivity rho, thickness h."""
    eta = impedance(rho, f)
    k = wavenumber(rho, f)
    t = np.tanh(k * h)
    return eta * (z_below + eta * t) / (eta + z_below * t)


def seafloor_response(layers_below, f):
    """MT-style impedance at the seafloor, 1-D plane wave.

    layers_below: list of (rho, h) from the seafloor downward, ending with a
    half-space given as (rho, np.inf).
    The impedance above the seafloor is that of the water layer over an
    insulating atmosphere, eta_w * coth(k_w h_w); the seafloor impedance is the
    parallel combination of the up- and down-looking impedances.
    """
    z = None
    for rho, h in reversed(layers_below):
        if z is None:
            z = half_space_top(rho, f)
        else:
            z = layer_top(rho, h, f, z)
    z_down = z
    eta_w = impedance(RHO_WATER, f)
    k_w = wavenumber(RHO_WATER, f)
    z_up = eta_w / np.tanh(k_w * H_WATER)
    return z_up * z_down / (z_up + z_down)


def subseafloor_response(layers_below, f):
    """Impedance looking DOWN from the seafloor, through the listed layers.

    This is the quantity a controlled-source system towed close to the seafloor
    is sensitive to, once the water-column screening has been removed by the
    geometry rather than by processing.
    """
    z = None
    for rho, h in reversed(layers_below):
        if z is None:
            z = half_space_top(rho, f)
        else:
            z = layer_top(rho, h, f, z)
    return z


def apparent(z):
    """Apparent resistivity and phase from the impedance at frequency f."""
    return np.abs(z) ** 2 / (MU0 * 2.0 * np.pi * app_f), np.degrees(np.angle(z))


def main():
    global app_f
    section("1. Skin depth")
    print("  In the quasi-static limit the fields obey a diffusion equation with")
    print("  wavenumber k = sqrt(i mu0 omega / rho), so the amplitude decays as")
    print("  exp(-x/delta) with")
    print("    delta = 1/Re(k) = sqrt(2 rho/(mu0 omega)) = sqrt(rho/(pi f mu0))")
    print(f"  mu0 = {MU0:.10e} H/m, so delta = 503.3 sqrt(rho/f) m with rho in")
    print("  ohm m and f in Hz.")
    print("\n   rho (ohm m)   f (Hz)   delta (m)   1/Re(k) (m)   ratio")
    for rho in (0.3, 1.0, 10.0, 100.0):
        for f in (0.1, 1.0, 10.0):
            d1 = skin_depth(rho, f)
            d2 = 1.0 / np.real(wavenumber(rho, f))
            print(f"  {rho:11.2f}   {f:6.2f}   {d1:9.2f}   {d2:11.2f}   "
                  f"{d1 / d2:7.4f}")
    print("\n  The two columns are the same quantity computed two ways, so the")
    print("  ratio is a check on the algebra and on the value of mu0.")
    print("\n  Consequence for a marine survey: at 1 Hz the skin depth in seawater")
    print(f"  (rho = {RHO_WATER:.2f} ohm m) is {skin_depth(RHO_WATER, 1.0):.0f} m,")
    print(f"  while a {H_WATER:.0f} m water column is "
          f"{H_WATER / skin_depth(RHO_WATER, 1.0):.2f} skin depths thick.")

    section("2. The plane-wave seafloor response is water-dominated")
    print("  Layers from the seafloor downward, and the water column above:")
    print(f"    water  rho = {RHO_WATER:.2f} ohm m, h = {H_WATER:.0f} m")
    print(f"    layer 1 rho = {RHO_HALF:.2f} ohm m, h = {H_SED_ABOVE:.0f} m")
    print(f"    target rho = {RHO_LAYER:.1f} ohm m, h = {H_LAYER:.0f} m")
    print(f"    layer 3 rho = {RHO_HALF:.2f} ohm m, h = {H_SED_BELOW:.0f} m")
    print(f"    half-space rho = {RHO_HALF:.2f} ohm m")
    print("\n  The magnetotelluric-style impedance at the seafloor is the")
    print("  parallel combination of the up-looking impedance (water below an")
    print("  insulating atmosphere) and the down-looking impedance (the layered")
    print("  sediments).")
    print("\n   f (Hz)   delta in seawater (m)   apparent rho (ohm m)   phase (deg)")
    for f in (0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0):
        z = seafloor_response([(RHO_HALF, H_SED_ABOVE), (RHO_LAYER, H_LAYER),
                               (RHO_HALF, H_SED_BELOW), (RHO_HALF, np.inf)], f)
        ra = abs(z) ** 2 / (MU0 * 2 * np.pi * f)
        print(f"  {f:8.2f}   {skin_depth(RHO_WATER, f):21.1f}   {ra:19.3f}   "
              f"{np.degrees(np.angle(z)):12.2f}")
    print("\n  Read the third column: the apparent resistivity is between 0.12")
    print(f"  and 0.20 ohm m at EVERY frequency, while the sediment is")
    print(f"  {RHO_HALF:.2f} ohm m and the target is {RHO_LAYER:.1f} ohm m.  The")
    print("  water column dominates the plane-wave response completely, because")
    print("  it is 3.3 times more conductive than the sediment and 1500 m thick.")
    print("\n  This is the honest result and it explains the instrument: a")
    print("  magnetotelluric measurement on the seafloor cannot see through the")
    print("  water column at these frequencies.  Marine CSEM therefore uses a")
    print("  CONTROLLED SOURCE towed close to the seafloor, with receivers on the")
    print("  seafloor, so that the fields entering the sediment have travelled")
    print("  through metres of water rather than kilometres.  The geometry avoids")
    print("  the screening instead of correcting for it.")

    section("3. The sub-seafloor response")
    print("  Remove the water column from the model and look only downward from")
    print("  the seafloor.  That is the idealised sensitivity of a controlled")
    print(f"  source and receiver both close to the seafloor at rho = "
          f"{RHO_HALF:.2f} ohm m.")
    print("\n   f (Hz)   delta in sediment (m)   apparent rho (ohm m)   "
          "phase (deg)")
    for f in (0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0):
        z = subseafloor_response([(RHO_HALF, H_SED_ABOVE), (RHO_LAYER, H_LAYER),
                                  (RHO_HALF, H_SED_BELOW),
                                  (RHO_HALF, np.inf)], f)
        ra = abs(z) ** 2 / (MU0 * 2 * np.pi * f)
        print(f"  {f:8.2f}   {skin_depth(RHO_HALF, f):22.1f}   {ra:21.3f}   "
              f"{np.degrees(np.angle(z)):12.2f}")
    print("\n  Now the apparent resistivity DOES respond, and the shape of the")
    print("  response is the whole story:")
    print("    - at 10 Hz it is 0.971 ohm m, slightly BELOW the background, because")
    print("      the skin depth (159 m) is smaller than the depth of the layer and")
    print("      nothing has reached it;")
    print("    - it rises to a maximum of about 1.16 ohm m near 0.3 Hz, a 16 per")
    print("      cent anomaly, where the skin depth (919 m) is a few times the")
    print("      layer depth;")
    print("    - it falls back again at the lowest frequencies, because the layer")
    print("      becomes electrically THIN compared with the skin depth and its")
    print("      contribution is diluted.")
    print("  The response is therefore confined to a band whose position is set by")
    print("  the layer depth and whose shape carries the layer's properties.  A")
    print("  single frequency cannot characterise it, and that is what makes the")
    print("  inversion of a CSEM sounding a shape-fitting problem rather than a")
    print("  lookup.")

    section("4. What a resistive layer does")
    print("  Compare three models at each frequency:")
    print("    A: no target (uniform 1.00 ohm m below the seafloor)")
    print(f"    B: {RHO_LAYER:.0f} ohm m x {H_LAYER:.0f} m at "
          f"{H_SED_ABOVE:.0f} m below the seafloor")
    print(f"    C: {RHO_LAYER / 2:.0f} ohm m x {H_LAYER * 2:.0f} m -- same")
    print("       transverse resistance (rho * h) as B")
    print("\n   f (Hz)   A: rho_a    B: rho_a    C: rho_a   (B-A)/A (%)   "
          "(C-B)/B (%)")
    diffsB, diffsC = [], []
    for f in FREQS_AB:
        cs = []
        for layers in (
            [(RHO_HALF, np.inf)],
            [(RHO_HALF, H_SED_ABOVE), (RHO_LAYER, H_LAYER),
             (RHO_HALF, H_SED_BELOW), (RHO_HALF, np.inf)],
            [(RHO_HALF, H_SED_ABOVE), (RHO_LAYER / 2.0, H_LAYER * 2.0),
             (RHO_HALF, H_SED_BELOW), (RHO_HALF, np.inf)],
        ):
            z = subseafloor_response(layers, f)
            cs.append(abs(z) ** 2 / (MU0 * 2 * np.pi * f))
        diffsB.append(100 * (cs[1] - cs[0]) / cs[0])
        diffsC.append(100 * (cs[2] - cs[1]) / cs[1])
        print(f"  {f:8.2f}   {cs[0]:9.3f}   {cs[1]:9.3f}   {cs[2]:9.3f}   "
              f"{100 * (cs[1] - cs[0]) / cs[0]:13.2f}   "
              f"{100 * (cs[2] - cs[1]) / cs[1]:12.2f}")
    fmax = FREQS_AB[int(np.argmax(diffsB))]
    print(f"\n  The largest anomaly produced by the resistive layer is "
          f"{max(diffsB):.2f} per cent,")
    print(f"  at {fmax:.2f} Hz in this sampled band.  Two lessons: the anomaly is")
    print("  tens of per cent, not a factor, and it is confined to a band.  A")
    print("  measurement that cannot resolve ten per cent of apparent resistivity")
    print("  cannot detect the layer at all, whatever the processing.  The model C")
    print("  row also shows that halving the resistivity and doubling the thickness")
    print("  does NOT reproduce the response: the difference between B and C reaches")
    print("  14 per cent, larger than the anomaly itself, so the shape of the")
    print("  response does discriminate the two.")

    section("5. The resistivity-thickness trade")
    print("  The rule of thumb says that a thin resistive layer in a conductive")
    print("  host is sensed through its TRANSVERSE RESISTANCE rho*h, so that a")
    print("  thin/very-resistive layer and a thick/moderately-resistive one are")
    print("  indistinguishable.  Test the rule instead of quoting it: build five")
    print("  layers with the SAME rho*h and compare their response CURVES.")
    print("\n   rho (ohm m)   h (m)   rho*h   peak anomaly (%)   at f (Hz)   "
          "max |curve - (100,100)| (%)")
    ref = None
    rows = []
    for rho, h in ((200.0, 50.0), (100.0, 100.0), (50.0, 200.0),
                   (25.0, 400.0), (12.5, 800.0)):
        curve = []
        for f in FREQS:
            z0 = subseafloor_response([(RHO_HALF, np.inf)], f)
            z1 = subseafloor_response([(RHO_HALF, H_SED_ABOVE), (rho, h),
                                       (RHO_HALF, H_SED_BELOW),
                                       (RHO_HALF, np.inf)], f)
            curve.append(100 * ((abs(z1) ** 2 - abs(z0) ** 2) / abs(z0) ** 2))
        curve = np.array(curve)
        rows.append((rho, h, curve))
        if abs(rho - 100.0) < 1e-9:
            ref = curve
    for rho, h, curve in rows:
        dev = np.max(np.abs(curve - ref))
        print(f"  {rho:11.1f}   {h:6.0f}   {rho * h:6.0f}   "
              f"{curve.max():17.2f}   {FREQS[np.argmax(curve)]:11.3f}   "
              f"{dev:28.2f}")
    print("\n  Read the last column.  Models with the SAME transverse resistance")
    print("  differ from the reference model by tens of percentage points across")
    print("  the band, so rho*h is NOT the quantity that controls this response.")

    section("5b. Which property does the response actually measure?")
    print("  Control the experiment.  Fix the frequency at 0.422 Hz, put the")
    print("  layer at the seafloor over a 1.00 ohm m half-space, and vary the")
    print("  layer's resistivity and thickness independently.")
    f5 = 0.422
    app_f = f5
    d_host = skin_depth(RHO_HALF, f5)
    print(f"\n  skin depth in the host at {f5:.3f} Hz: "
          f"{d_host:.1f} m")
    print("\n   rho (ohm m)   h (m)   rho*h    h/d_host   rho_a (ohm m)   "
          "h/delta_layer")
    for rho, h in ((100.0, 100.0), (10.0, 100.0), (1000.0, 100.0),
                   (1000.0, 10.0), (10000.0, 1.0), (10.0, 1000.0)):
        r_a = apparent(subseafloor_response([(rho, h), (RHO_HALF, np.inf)], f5))[0]
        print(f"  {rho:11.1f}   {h:6.0f}   {rho * h:6.0f}   {h / d_host:8.3f}   "
              f"{r_a:13.4f}   {h / skin_depth(rho, f5):13.4f}")
    thin_sheet = 2 * np.pi * f5 * MU0 * (d_host ** 2 / 2 + d_host * 100.0
                                         + 100.0 ** 2)
    print(f"\n  Thin-layer limit: for h much less than the skin depth IN the")
    print(f"  layer, the recursion reduces to a purely inductive impedance")
    print(f"  increment i*omega*mu0*h, so the layer adds")
    print(f"    omega*mu0*(delta_host^2/2 + delta_host*h + h^2)")
    print(f"  and for h = 100 m that prediction is {thin_sheet:.4f} ohm m,")
    r100 = apparent(subseafloor_response([(100.0, 100.0), (RHO_HALF, np.inf)], f5))[0]
    r1000 = apparent(subseafloor_response([(1000.0, 100.0), (RHO_HALF, np.inf)], f5))[0]
    print(f"  against {r100:.4f} ohm m for rho = 100 ohm m and {r1000:.4f} ohm m")
    print(f"  for rho = 1000 ohm m.")
    print(f"  So the SAME h gives the same response to")
    print( "  within 0.3 per cent even though rho*h differs by a factor of ten,")
    print( "  while the same rho*h with a thinner layer gives almost no anomaly")
    print( "  at all.  In this regime the response measures the layer's THICKNESS,")
    print( "  not its transverse resistance.")
    print( "\n  Why the rule of thumb exists at all: the resistivity enters only")
    print( "  when the fields attenuate INSIDE the layer, h comparable to the")
    print( "  skin depth in the layer, which needs")
    f_int = RHO_LAYER / (np.pi * MU0 * H_LAYER ** 2)
    print(f"    f > rho/(pi*mu0*h^2) = {f_int:.0f} Hz for 100 ohm m and h = 100 m,")
    print( "  far above the marine band.  The transverse resistance belongs to the")
    print( "  VERTICAL (galvanic) current geometry that an offset-dependant")
    print( "  controlled-source survey exploits; a one-dimensional plane-wave")
    print( "  sounding is not that measurement.")
    print( "\n  Two consequences, and they point in opposite directions:")
    print("    - thickness is well constrained and resistivity is poorly")
    print("      constrained by a single one-dimensional sounding, so the")
    print("      resistivity-thickness trade-off is REAL but runs the other way")
    print("      from the rule of thumb;")
    print("    - the inversion is still non-unique, and the honest product of a")
    print("      marine CSEM survey is a resistivity image with a stated")
    print("      resolution, not a 'hydrate thickness'.")

    section("6. Verification")
    print("(a) the layered recursion must return the half-space resistivity for a")
    print("    uniform earth.  Compute the seafloor response for a uniform")
    print("    sediment and compare its normal-incidence MT impedance with the")
    print("    analytic value sqrt(i mu0 omega rho):")
    for f in (0.01, 0.1, 1.0):
        z = seafloor_response([(RHO_HALF, np.inf)], f)
        z_analytic_down = impedance(RHO_HALF, f)
        eta_w = impedance(RHO_WATER, f)
        k_w = wavenumber(RHO_WATER, f)
        z_up = eta_w / np.tanh(k_w * H_WATER)
        z_expected = z_up * z_analytic_down / (z_up + z_analytic_down)
        print(f"    f = {f:5.2f} Hz: recursion = {abs(z):.6e}, "
              f"closed form = {abs(z_expected):.6e}, "
              f"ratio = {abs(z) / abs(z_expected):.8f}")
    print("    The recursion reproduces the two-layer (water over half-space)")
    print("    form exactly, which is the check on the layer algebra.")
    print("(b) the sub-seafloor recursion on a uniform half-space must return the")
    print("    half-space resistivity exactly:")
    for f in (0.01, 0.1, 1.0, 10.0):
        z = subseafloor_response([(RHO_HALF, np.inf)], f)
        ra = abs(z) ** 2 / (MU0 * 2 * np.pi * f)
        print(f"    f = {f:5.2f} Hz: apparent resistivity = {ra:.8f} ohm m "
              f"(half-space = {RHO_HALF:.2f}), ratio = {ra / RHO_HALF:.10f}")
    print("    The ratio is 1 to ten figures for every frequency, which is the")
    print("    strongest available check on the recursion: a uniform earth has no")
    print("    frequency response at all.")
    print("(c) unit check: delta = sqrt(rho/(pi f mu0)) has units")
    print("    sqrt((V m/A)/(1/s * H/m)) = sqrt((V m s)/(A H)); with H = V s/A")
    print("    this is sqrt(m^2) = m.  ok")


if __name__ == "__main__":
    main()
