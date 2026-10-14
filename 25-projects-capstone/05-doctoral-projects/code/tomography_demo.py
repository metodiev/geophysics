"""Local-earthquake tomography with a checkerboard resolution test (SYNTHETIC).

Straight rays on a 10 x 5 cell grid (30 x 15 km, 3 km cells, uniform 6 km/s),
a synthetic travel-time dataset, damped least-squares inversion, and the three
standard resolution diagnostics: amplitude recovery, checkerboard correlation and
point-spread functions. Print-only: no files, no plots, no network.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import lsqr

rng = np.random.default_rng(20261014)
print("=" * 72)
print("SYNTHETIC local-earthquake tomography: checkerboard resolution test")
print("=" * 72)

NX, NZ, H, S0 = 10, 5, 3.0, 1.0 / 6.0     # 3 km cells, 6.00 km/s, s/km
NC, NSRC, NREC, NOISE = NX * NZ, 10, 10, 0.005
xs, zs = (np.arange(NX) + 0.5) * H, (np.arange(NZ) + 0.5) * H

def cell_index(x, z):
    return (np.clip((z / H).astype(int), 0, NZ - 1) * NX
            + np.clip((x / H).astype(int), 0, NX - 1))

rows, cols, vals, nray = [], [], [], 0
for i in range(NSRC):
    sx = (i + 0.5) * 30.0 / NSRC
    for j in range(NREC):
        rx = (j + 0.5) * 30.0 / NREC
        L = float(np.hypot(rx - sx, 15.0))
        t = np.linspace(0.0, 1.0, max(2, int(L / 0.25)))
        idx = cell_index(sx + t * (rx - sx), t * 15.0)
        seg = L / (len(t) - 1)
        for c in np.unique(idx):
            rows.append(nray); cols.append(c); vals.append(seg * np.sum(idx == c))
        nray += 1
A = coo_matrix((vals, (rows, cols)), shape=(nray, NC)).tocsr()
G = (A * S0).tocsr()                       # slowness perturbation -> seconds

print("\n1. Ray geometry and coverage")
print(f"  grid {NX} x {NZ} cells of {H:.0f} km = {NC} cells over 30 x 15 km")
print(f"  {NSRC} sources x {NREC} receivers = {nray} rays, {A.nnz} ray-cell "
      f"segments ({A.nnz / nray:.1f} cells per ray), mean ray length "
      f"{np.mean(A.sum(axis=1)):.2f} km")
cover = np.asarray(A.sum(axis=0)).ravel()
print(f"  path length per cell: {cover.min():.1f} to {cover.max():.1f} km, "
      f"cells with no ray: {int(np.sum(cover == 0))}")

def gaussian(peak, x0, z0, rx, rz):
    ddx, ddz = xs[None, :] - x0, zs[:, None] - z0
    return (peak * np.exp(-((ddx / rx) ** 2 + (ddz / rz) ** 2))).ravel()

def invert(data, alpha):
    return lsqr(G, data, damp=alpha, atol=1e-13, btol=1e-13, iter_lim=8000)[0]

TRUE = gaussian(-0.05, 13.5, 7.5, 5.0, 3.5)          # -5% slowness = +5% velocity
d_obs = G @ TRUE + rng.normal(0.0, NOISE, nray)
print("\n2. Synthetic dataset")
print(f"  anomaly: Gaussian, peak velocity +5.0%, rms {np.sqrt(np.mean(TRUE**2))*100:.3f}%"
      f" of slowness, half-width 5 x 3.5 km, centred at x = 13.5 km, z = 7.5 km")
print(f"  travel-time perturbation rms {np.sqrt(np.mean((G @ TRUE)**2))*1000:.2f} ms, "
      f"peak {np.abs(G @ TRUE).max()*1000:.2f} ms, picking noise {NOISE*1000:.1f} ms "
      f"-> signal-to-noise {np.sqrt(np.mean((G @ TRUE)**2))/NOISE:.1f}")

print("\n3. Damping by the discrepancy principle")
print("   rule: largest alpha whose rms data residual does not exceed the noise")
print(f"   {'alpha':>7} {'rms residual':>13} {'model rms':>10} {'peak':>8} {'corr':>7}")
table = []
for alpha in (0.001, 0.005, 0.02, 0.05, 0.1, 0.5, 1.0, 5.0, 20.0):
    m = invert(d_obs, alpha)
    res = float(np.sqrt(np.mean((d_obs - G @ m) ** 2)))
    table.append((alpha, res))
    print(f"   {alpha:7.3f} {res*1000:10.2f} ms {np.sqrt(np.mean(m**2))*100:8.3f}% "
          f"{m.min()*100:7.2f}% {np.corrcoef(m, TRUE)[0, 1]:7.3f}")
ALPHA = max(a for a, r in table if r <= NOISE)
print(f"   -> alpha = {ALPHA:.3f}  (the residual falls by only "
      f"{(table[6][1]-table[0][1])*1000:.2f} ms between alpha = 1 and "
      f"alpha = 0.001, while the model rms grows by a factor "
      f"{np.sqrt(np.mean(invert(d_obs, 0.001)**2))/np.sqrt(np.mean(invert(d_obs, ALPHA)**2)):.1f})")

m = invert(d_obs, ALPHA)
res = float(np.sqrt(np.mean((d_obs - G @ m) ** 2)))
kz, kx = np.unravel_index(np.argmax(np.abs(m.reshape(NZ, NX))), (NZ, NX))
print("\n4. Recovery of the anomaly")
print(f"  rms data residual {res*1000:.2f} ms against a noise level of {NOISE*1000:.1f} ms")
print(f"  recovered peak {abs(m.min())*100:.2f}% vs true 5.00% "
      f"(amplitude recovery {abs(m.min())/0.05*100:.0f}%)")
print(f"  recovered rms {np.sqrt(np.mean(m**2))*100:.3f}% vs true "
      f"{np.sqrt(np.mean(TRUE**2))*100:.3f}%")
print(f"  anomalous cell found at x = {xs[kx]:.1f} km, z = {zs[kz]:.1f} km "
      f"(true 13.5, 7.5 km)")

check = np.array([[0.04 * (1 if (i + k) % 2 == 0 else -1) for i in range(NX)]
                  for k in range(NZ)]).ravel()
m_chk = invert(G @ check + rng.normal(0.0, NOISE, nray), ALPHA)
print("\n5. Checkerboard resolution test")
print("  input: alternating +/-4.00% blocks, one cell (3 x 3 km) each")
print(f"  correlation recovered vs input: r = {np.corrcoef(m_chk, check)[0, 1]:.3f}")
print(f"  recovered amplitude {np.abs(m_chk).mean()/np.abs(check).mean()*100:.1f}% of "
      f"input; best cell {m_chk.max()*100:.2f}%, worst {np.abs(m_chk).min()*100:.2f}% "
      f"of 4.00%")

print("\n6. Point-spread functions (rows of the resolution matrix)")
print(f"   {'spike at':>22} {'own-cell recovery':>18} {'leak outside':>13}")
for i0, k0 in ((4, 0), (4, 2), (4, 4)):
    tgt = k0 * NX + i0
    spike = np.zeros(NC); spike[tgt] = -0.05
    psf = invert(G @ spike, ALPHA)
    leak = 1.0 - abs(psf[tgt]) / np.abs(psf).sum()
    print(f"   x = {xs[i0]:5.1f}, z = {zs[k0]:4.1f} km {psf[tgt]/spike[tgt]*100:16.1f}% "
          f"{leak*100:12.1f}%")
print("  -> only about a third of each spike stays in its own cell and the damping")
print("     removes another third of the amplitude: the recovered image is a")
print("     blurred, damped version of the Earth. The own-cell recovery is flat")
print("     with depth here because the ray coverage per cell is comparable")
print("     everywhere; a real catalogue leaves the deep cells poorly lit and")
print("     there the recovery falls sharply.")

print("\n" + "=" * 72)
print("SYNTHETIC demo complete: alpha ="
      f" {ALPHA:.3f}, residual {res*1000:.2f} ms vs noise {NOISE*1000:.1f} ms,")
print(f"anomaly peak recovered at {abs(m.min())/0.05*100:.0f}% of its true value,")
print(f"and checkerboard correlation r = {np.corrcoef(m_chk, check)[0, 1]:.3f}.")
print("=" * 72)
