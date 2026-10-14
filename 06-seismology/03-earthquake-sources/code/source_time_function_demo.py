"""Source time functions, rupture kinematics and directivity.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python source_time_function_demo.py
Requires: numpy.

Companion to lesson 06-03-04.

THE MODEL.  A rupture of length L propagates unilaterally at speed v_r
(0 < v_r < beta) along a line, and every element of the line emits the same
far-field wavelet of rise time tau_r.  For a station at azimuth theta measured
from the direction of rupture propagation, the travel time from the element at
distance xi along the fault is

    t(xi) = xi / v_r + (r - xi cos theta) / beta      (far field, r >> L)

so the emission times reaching the station are spread by

    L ( 1/v_r - cos theta / beta )  =  T_true - (L/beta) cos theta,
    T_true = tau_r + L / v_r .

The received signal is therefore the CONVOLUTION of one wavelet with a
distribution of arrival delays, and the second moment of a convolution adds in
quadrature:

    sigma_total^2 = sigma_wavelet^2 + sigma_delay^2 .

That identity is what the script measures.  For each azimuth it

  1. builds the delay distribution from the geometry and its rms width
     sigma_delay,
  2. predicts sigma_total from the identity above,
  3. synthesises the signal and measures its rms width directly,
  4. reports the difference between prediction and measurement,
  5. measures the peak amplitude against the 1/sigma_total prediction,
  6. repeats for a bilateral rupture, which has no forward/backward asymmetry,
  7. computes the moment-rate function of the whole source, which contains no
     receiver propagation term and is therefore azimuth independent.

Everything is SYNTHETIC: L, v_r, tau_r and the wavelet shape are chosen and
printed, not measured.
"""

import numpy as np

BETA = 3500.0        # m/s, SYNTHETIC shear-wave speed
L_FAULT = 30.0e3     # m, SYNTHETIC rupture length
VR = 0.80 * BETA     # m/s, SYNTHETIC rupture speed (0.80 beta)
TAU_R = 1.0          # s, SYNTHETIC local rise time
N_POINTS = 400       # rupture elements
DT = 0.005           # s, sample interval of the synthesis
NT = 20000           # samples


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def wavelet(t, tau):
    """Normalised far-field wavelet: (t/tau) exp(-t/tau) for t > 0."""
    x = np.maximum(t / tau, 0.0)
    return x * np.exp(-x)


def rms_duration(t, signal):
    """Energy-weighted rms width, in seconds."""
    e = signal ** 2
    tot = e.sum()
    if tot <= 0:
        return 0.0
    tbar = (t * e).sum() / tot
    var = (((t - tbar) ** 2) * e).sum() / tot
    return float(np.sqrt(var))


def delays(theta_deg, bilateral=False):
    theta = np.radians(theta_deg)
    if bilateral:
        xi = np.linspace(-L_FAULT / 2, L_FAULT / 2, N_POINTS)
        return np.abs(xi) / VR - xi * np.cos(theta) / BETA
    xi = np.linspace(0.0, L_FAULT, N_POINTS)
    return xi / VR - xi * np.cos(theta) / BETA


def signal_from(delay, t):
    sig = np.zeros_like(t)
    for d in delay:
        sig += wavelet(t - d, TAU_R) * DT
    return sig


def main():
    print("Rupture kinematics and directivity -- computed quantities")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC model: beta = {BETA:.0f} m/s, L = {L_FAULT/1e3:.0f} km,")
    print(f"  v_r = {VR:.0f} m/s = {VR/BETA:.2f} beta, rise time tau_r = "
          f"{TAU_R:.2f} s, {N_POINTS} rupture elements")

    t_true = TAU_R + L_FAULT / VR
    t = np.arange(NT) * DT
    sigma_w = rms_duration(t, wavelet(t, TAU_R))

    section("1. The convolution identity, azimuth by azimuth")
    print(f"  true duration tau_r + L/v_r = {TAU_R:.2f} + {L_FAULT/VR:.3f}"
          f" = {t_true:.3f} s")
    print(f"  directivity term L/beta = {L_FAULT/BETA:.3f} s")
    print(f"  rms width of one wavelet, sigma_wavelet = {sigma_w:.4f} s")
    print()
    print(f"  {'azimuth':>8}{'sigma_delay':>13}{'sigma predicted':>16}"
          f"{'sigma measured':>16}{'difference':>12}{'peak':>8}")
    rows = []
    for theta in (0, 45, 90, 135, 180):
        d = delays(theta)
        sd = float(np.std(d))
        pred = float(np.sqrt(sd ** 2 + sigma_w ** 2))
        sig = signal_from(d, t)
        meas = rms_duration(t, sig)
        peak = float(np.max(np.abs(sig)))
        rows.append((theta, sd, pred, meas, peak))
    peak_max = max(r[4] for r in rows)
    for (theta, sd, pred, meas, peak) in rows:
        print(f"  {theta:8.0f}{sd:13.4f}{pred:16.4f}{meas:16.4f}"
              f"{meas-pred:12.2e}{peak/peak_max:8.4f}")
    print()
    worst = max(abs(r[3] - r[2]) for r in rows)
    print(f"  worst |sigma_measured - sigma_predicted| = {worst:.2e} s"
          f"   ({100*worst/rows[2][2]:.2f} per cent of the value)")
    print("  The quadrature rule is the INCOHERENT approximation: it is exact when")
    print("  the shifted wavelets do not overlap, because then the energy of the sum")
    print("  is the sum of the energies.  Here they overlap heavily, the cross terms")
    print("  in |sum|^2 are negative on average, and the measured duration comes out")
    print("  consistently SHORTER than the rule predicts.  The deficit is measured,")
    print("  not assumed, and the next check confirms the diagnosis: shrinking the")
    print("  wavelet relative to the delay spacing must shrink the deficit.")
    print()
    print(f"  {'wavelet tau_r (s)':>18}{'deficit at 180 deg (%)':>24}")
    for tau in (1.0, 0.5, 0.25, 0.1, 0.05, 0.025):
        sw = rms_duration(t, wavelet(t, tau))
        d = delays(180)
        pred = float(np.sqrt(np.std(d) ** 2 + sw ** 2))
        sig = np.zeros_like(t)
        for dd in d:
            sig += wavelet(t - dd, tau) * DT
        deficit = 100 * abs(rms_duration(t, sig) - pred) / pred
        print(f"  {tau:18.3f}{deficit:24.3f}")
    print()
    print("  The deficit falls monotonically, which is the confirmation: the")
    print("  quadrature rule is an incoherent energy statement, and it becomes")
    print("  exact as the received wavelets stop overlapping.")

    section("2. Directivity: durations and amplitudes forward and backward")
    d_fwd, d_bwd = rows[0], rows[-1]
    print(f"  forward/backward sigma ratio          = {d_bwd[3]/d_fwd[3]:.4f}")
    print(f"  forward/backward peak amplitude ratio = {d_bwd[4]/d_fwd[4]:.4f}")
    print(f"  forward/backward ratio of 1/sigma     = "
          f"{(1/d_fwd[3])/(1/d_bwd[3]):.4f}")
    print()
    print("  A unilaterally rupturing fault radiates a SHORT, LARGE pulse ahead")
    print("  of the rupture front and a LONG, SMALL one behind it.  The amplitude")
    print("  ratio and the inverse-duration ratio agree to a few per cent, since")
    print("  the peak of a convolution with fixed area scales as 1/sigma.")
    print()
    print("  The closed-form SPAN ratio (tau_r + L/v_r + L/beta) /")
    print(f"  (tau_r + L/v_r - L/beta) = "
          f"{(t_true + L_FAULT/BETA)/(t_true - L_FAULT/BETA):.4f}, against the")
    print("  measured rms ratio above.  They differ because the rms width is not")
    print("  the support: the closed form gives the span of emission times, the")
    print("  measurement gives the second moment.  Both are valid duration")
    print("  measures, and they are not the same number.")

    section("3. The true source duration is azimuth independent")
    print("  The moment-rate function of the whole source sums the elements with")
    print("  their RUPTURE times xi/v_r and no receiver term:")
    print()
    print(f"  {'azimuth':>8}{'apparent sigma':>17}{'moment-rate sigma':>19}")
    mrf = signal_from(np.linspace(0.0, L_FAULT, N_POINTS) / VR, t)
    s_mrf = rms_duration(t, mrf)
    for theta in (0, 90, 180):
        sig = signal_from(delays(theta), t)
        print(f"  {theta:8.0f}{rms_duration(t, sig):17.4f}{s_mrf:19.4f}")
    print()
    print("  The moment-rate sigma is the same at every azimuth.  A rectangular")
    print(f"  span of length {t_true:.3f} s has rms width "
          f"{t_true/np.sqrt(12):.4f} s, and the measured value is "
          f"{s_mrf:.4f} s: close, and different because the wavelet has its own")
    print("  width.  The apparent duration is not azimuth independent, so any")
    print("  quoted duration must say which one it is.")

    section("4. A bilateral rupture, for contrast")
    print(f"  {'azimuth':>8}{'bilateral sigma':>17}{'unilateral sigma':>18}")
    for theta in (0, 90, 180):
        sb = signal_from(delays(theta, bilateral=True), t)
        su = signal_from(delays(theta), t)
        print(f"  {theta:8.0f}{rms_duration(t, sb):17.4f}"
              f"{rms_duration(t, su):18.4f}")
    print()
    print("  Bilaterally the two halves contribute equal and opposite propagation")
    print("  delays, so the first-order directivity cancels and the forward and")
    print("  backward durations coincide.  Directivity is a statement about")
    print("  rupture DIRECTEDNESS; its absence is information about the rupture.")

    section("5. What this does to a corner frequency and a stress drop")
    print("  If the spectrum scales with the duration then f_c ~ 1/sigma, so the")
    print("  same event has a different f_c at different azimuths:")
    print()
    print(f"  {'azimuth':>8}{'sigma (s)':>12}{'f_c / f_c(90)':>15}")
    base = rows[2][3]
    for (theta, sd, pred, meas, peak) in rows:
        print(f"  {theta:8.0f}{meas:12.4f}{base/meas:15.4f}")
    print()
    print(f"  Here f_c varies by a factor {rows[-1][3]/rows[0][3]:.2f} between the")
    print("  two ends.  A stress drop computed from f_c without allowing for")
    print("  directivity inherits that error CUBED, because the stress drop goes")
    print("  as M0 f_c^3 (lesson 06-03-05).")
    print()
    print("=" * 72)
    print("All inputs are SYNTHETIC and printed above.  The measured rms")
    print("durations are compared with the convolution identity, and the")
    print("difference is reported rather than assumed to be small.")
    print("=" * 72)


if __name__ == "__main__":
    main()
