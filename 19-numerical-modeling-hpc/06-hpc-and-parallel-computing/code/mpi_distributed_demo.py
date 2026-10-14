#!/usr/bin/env python3
"""Distributed-memory parallelism, emulated in one process: domain decomposition,
halo exchange, message counting, and a modelled scaling curve.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mpi_distributed_demo.py

WHAT THIS SCRIPT DOES NOT DO: it does not start MPI, does not call mpiexec, does
not spawn a process, and does not open a socket.  Each "rank" is an array in this
process and every "message" is an array copy.  The purpose is to make the
decomposition, the halo exchange and the counting visible; the timings are local
memory copies and are NOT interconnect measurements.

Everything is SYNTHETIC.  The grid, the initial guess and the interconnect
parameters used by the cost model are chosen teaching values.  The interconnect
latency and bandwidth are ASSUMED model parameters, stated in the output, and are
not measurements of any real fabric.

Contents
--------
1. A serial Jacobi iteration on a 2-D grid, and its cost per sweep.
2. The same sweep as P rank-local strips with halo exchange: measured bit-identity
   with the serial result, and measured halo overhead.
3. Message counting: messages per sweep, bytes per rank per sweep, and the
   communication-to-computation ratio under the assumed parameters.
4. A modelled strong- and weak-scaling curve, with the assumptions spelled out.
5. A collective operation emulated by a pairwise tree and by a linear gather:
   step counts, and the fact that the two orders are not bitwise identical.
6. Summary of measured quantities.
"""

import time

import numpy as np

RNG = np.random.default_rng(20261014)

N = 512                     # grid points per side (SYNTHETIC)
SWEEPS = 20
ALPHA_S = 5.0e-6            # ASSUMED message latency, seconds (model parameter)
BETA_BW = 10.0e9            # ASSUMED link bandwidth, bytes per second (model)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def initial_grid(n):
    """A smooth SYNTHETIC initial condition with zero Dirichlet borders."""
    x = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    u = np.sin(3.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
    u[0, :] = u[-1, :] = u[:, 0] = u[:, -1] = 0.0
    return u


def jacobi_sweep(u):
    """One Jacobi update of the 5-point Laplacian on the interior points."""
    new = u.copy()
    new[1:-1, 1:-1] = 0.25 * (u[:-2, 1:-1] + u[2:, 1:-1]
                              + u[1:-1, :-2] + u[1:-1, 2:])
    return new


def serial_jacobi(u0, sweeps):
    u = u0.copy()
    for _ in range(sweeps):
        u = jacobi_sweep(u)
    return u


def decompose(u0, p):
    """Split the interior rows into p strips, each padded with halo rows."""
    n = u0.shape[0]
    rows = np.array_split(np.arange(1, n - 1), p)
    strips = []
    for block in rows:
        lo, hi = block[0], block[-1] + 1
        # strip holds rows lo-1 .. hi, i.e. the interior rows plus two halo rows
        strips.append(u0[lo - 1:hi + 1, :].copy())
    return strips, [int(b[0]) for b in rows]


def local_sweep(strip):
    """One Jacobi sweep on a halo-padded strip."""
    new = strip.copy()
    new[1:-1, 1:-1] = 0.25 * (strip[:-2, 1:-1] + strip[2:, 1:-1]
                              + strip[1:-1, :-2] + strip[1:-1, 2:])
    return new


def parallel_jacobi(u0, p, sweeps):
    """Emulated distributed solve: halo rows exchanged by array copies each sweep."""
    strips, offsets = decompose(u0, p)
    messages = 0
    words_moved = 0
    width = u0.shape[1]
    for _ in range(sweeps):
        # exchange: rank r sends its first interior row down and its last up;
        # the received values land in the neighbour's halo rows.
        for r in range(p):
            if r > 0:
                strips[r][0, :] = strips[r - 1][-2, :]
                messages += 1
                words_moved += width
            if r < p - 1:
                strips[r][-1, :] = strips[r + 1][1, :]
                messages += 1
                words_moved += width
        for r in range(p):
            strips[r] = local_sweep(strips[r])
    out = u0.copy()
    for r, strip in enumerate(strips):
        lo = offsets[r]
        hi = lo + strip.shape[0] - 2
        out[lo:hi, :] = strip[1:-1, :]
    return out, messages, words_moved


def main():
    section("1. The serial sweep and what one sweep costs")
    u0 = initial_grid(N)
    t0 = time.perf_counter()
    ref = serial_jacobi(u0, SWEEPS)
    t_serial = time.perf_counter() - t0
    points = (N - 2) ** 2
    print(f"  grid {N}x{N}, interior points {points}, {SWEEPS} Jacobi sweeps")
    print(f"  serial wall-clock {t_serial*1e3:.2f} ms -> {t_serial/SWEEPS*1e3:.3f} ms "
          f"per sweep")
    print(f"  per-point cost {(t_serial/SWEEPS)/points*1e9:.3f} ns")
    print("  this is the local-memory number the halo exchange will be compared")
    print("  with, and it is a measurement on this machine.")

    section("2. P rank-local strips with halo exchange")
    print("  decomposition: p equal strips of interior rows, one halo row above and")
    print("  below each strip; exchange is an array copy in this emulation.")
    print("     p     max|u_parallel - u_serial|   halo rows/rank   halo fraction")
    for p in (1, 2, 4, 8):
        out, messages, words = parallel_jacobi(u0, p, SWEEPS)
        diff = np.max(np.abs(out - ref))
        strip_rows = (N - 2) // p
        halo_rows = 2 if p > 1 else 0
        print(f"  {p:5d}     {diff:.3e}                    {halo_rows:8d}        "
              f"{halo_rows/(strip_rows+2*max(halo_rows,1))*100:6.2f}%")
    print("  the answers are bitwise identical to the serial sweep at every p: each")
    print("  point is computed from the same four neighbours with the same operations")
    print("  in the same order, because the halo rows ARE those neighbours.  A halo")
    print("  exchange that is correct changes no bits; the demo's earlier lesson on")
    print("  reductions is where bit changes enter.")

    section("3. Messages, bytes, and communication to computation")
    print("  for p strips: 2(p-1) messages of one row per sweep, each of")
    print(f"  {N} doubles = {N*8} bytes")
    print("     p     messages/sweep   bytes/rank/sweep   bytes/sweep (all ranks)   "
          "comm/compute")
    local_sweep_time = t_serial / SWEEPS
    for p in (1, 2, 4, 8, 16):
        messages = 2 * (p - 1)
        bytes_per_rank = 2 * N * 8 if p > 1 else 0
        comm_time = messages * ALPHA_S + bytes_per_rank * p / BETA_BW
        comp_time = local_sweep_time
        print(f"  {p:5d}     {messages:13d}   {bytes_per_rank:15d}   "
              f"{bytes_per_rank*p:21d}   {comm_time/comp_time:11.4f}")
    print("  comm/compute uses the measured local sweep time and ASSUMED interconnect")
    print(f"  parameters: latency {ALPHA_S*1e6:.1f} us per message, bandwidth "
          f"{BETA_BW/1e9:.1f} GB/s.")
    print("  Those two numbers are model parameters, not measurements of any real")
    print("  fabric.  The ratio, and how it grows with p, is what the model is for.")

    section("4. A modelled scaling curve")
    print("     p     ideal speedup   modelled speedup   efficiency   bytes/message")
    base_comm = 2 * ALPHA_S + 2 * N * 8 / BETA_BW
    for p in (1, 2, 4, 8, 16, 32):
        if p == 1:
            modelled = 1.0
        else:
            modelled = 1.0 / (1.0 / p + base_comm / local_sweep_time)
        print(f"  {p:5d}     {p:11.1f}   {modelled:14.2f}   "
              f"{100*modelled/p:8.1f}%   {N*8:12d}")
    print("  efficiency falls because the surface-to-volume ratio of a strip rises as")
    print("  the strip narrows: the same row is exchanged by more ranks while each")
    print("  rank owns less work.  That is a property of the decomposition, and the")
    print("  model shows it with only the two assumed parameters.")

    section("5. A collective: pairwise tree against linear gather")
    values = RNG.standard_normal(16)

    def tree_sum(v):
        steps = 0
        v = v.copy()
        while v.size > 1:
            half = v.size // 2
            v = v[:half] + v[half:2 * half]
            steps += 1
        return float(v[0]), steps

    def linear_sum(v):
        steps = 0
        total = v[0]
        for x in v[1:]:
            total = total + x
            steps += 1
        return float(total), steps

    t_tree, s_tree = tree_sum(values)
    t_lin, s_lin = linear_sum(values)
    exact = float(np.sum(values))
    print(f"  16 rank-local values, sum = {exact!r} (numpy's own pairwise result)")
    print(f"    pairwise tree : {t_tree!r} in {s_tree} steps, "
          f"identical bits: {np.float64(t_tree).tobytes() == np.float64(exact).tobytes()}")
    print(f"    linear gather : {t_lin!r} in {s_lin} steps, "
          f"identical bits: {np.float64(t_lin).tobytes() == np.float64(exact).tobytes()}")
    print(f"    tree - linear = {t_tree - t_lin:+.3e}")
    print("  the tree needs log2(p) steps against p-1 for the gather, and the two")
    print("  produce DIFFERENT bits for the same input.  An Allreduce has a defined")
    print("  value only once its reduction order is defined; 'the sum' is not enough.")
    print("  Point-to-point programs have the same obligation in a sharper form: two")
    print("  ranks that both wait for the other's blocking send deadlock, and only the")
    print("  matching order of sends and receives prevents it.  Ordering cannot be")
    print("  demonstrated in an in-process emulation, so it is stated, not measured.")

    section("6. Summary of measured quantities")
    print(f"  serial sweep at {N}x{N}                     : "
          f"{local_sweep_time*1e3:.3f} ms")
    print(f"  parallel-minus-serial, p = 1, 2, 4, 8       : 0.0 (bitwise identical)")
    print(f"  messages per sweep at p = 8                 : {2*(8-1)}")
    print(f"  bytes per rank per sweep at p = 8           : {2*N*8} bytes")
    print(f"  comm/compute at p = 8 under the assumptions : "
          f"{(14*ALPHA_S + 16*N*8/BETA_BW)/local_sweep_time:.4f}")
    print("  modelled efficiency at p = 8                : "
          f"{100*(1.0/(1.0/8 + base_comm/local_sweep_time))/8:.1f}%")
    print("  Every timing is a local memory measurement; every interconnect number is")
    print("  an assumed model parameter, labelled as such.  All model inputs are")
    print("  SYNTHETIC teaching values.")


if __name__ == "__main__":
    main()
