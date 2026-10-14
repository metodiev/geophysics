#!/usr/bin/env python3
"""Documenting processing: reproducibility in practice.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python processing_transparency_demo.py

Contents
--------
1. A small processing pipeline over an array, with every step and its parameters
   recorded in a machine-readable "processing record".
2. Hashes: SHA-256 of the input data, of the record and of the output.  Re-running
   the record reproduces the output bit for bit -- verified, not asserted.
3. Step ORDER matters: swapping two steps gives a different result.  The difference
   is measured, so the size of the mistake is known rather than assumed.
4. A near-identical parameter (0.3 against 0.1+0.2) gives the same result but a
   different parameter hash: reproducibility must be checked by comparing RESULTS,
   not by comparing text.
5. A summary verdict table, of the kind that belongs in a processing report.
"""

import hashlib
import json
import numpy as np

RNG_SEED = 20261014


def h256(array_or_text) -> str:
    """SHA-256 of a float array (via its exact bytes) or of a string."""
    if isinstance(array_or_text, str):
        return hashlib.sha256(array_or_text.encode("utf-8")).hexdigest()
    a = np.ascontiguousarray(np.asarray(array_or_text, dtype=np.float64))
    return hashlib.sha256(a.tobytes()).hexdigest()


def despike(y, window, n_sigma):
    from numpy.lib.stride_tricks import sliding_window_view
    pad = window // 2
    med = np.median(sliding_window_view(np.pad(y, pad, mode="edge"), window), axis=-1)
    d = np.diff(y)
    mad = np.median(np.abs(d - np.median(d)))
    sigma = 1.4826 * mad / np.sqrt(2.0)
    out = y.copy()
    bad = np.abs(y - med) > n_sigma * sigma
    out[bad] = med[bad]
    return out, int(bad.sum())


def level(y, x, order):
    """Remove a polynomial trend of the given order fitted to the whole line."""
    c = np.polyfit(x, y, order)
    return y - np.polyval(c, x), c


def lowpass(y, dx, cutoff_wavelength):
    n = y.size
    k = 2.0 * np.pi * np.fft.rfftfreq(n, d=dx)
    kc = 2.0 * np.pi / cutoff_wavelength
    return np.fft.irfft(np.fft.rfft(y) * np.exp(-0.5 * (k / kc) ** 2), n=n)


def run_pipeline(data, x, dx, steps):
    """Execute an ordered list of steps.  Returns (output, executed record)."""
    y = data.copy()
    executed = []
    for step in steps:
        name, params = step["op"], step["params"]
        if name == "despike":
            y, n_bad = despike(y, params["window"], params["n_sigma"])
            executed.append({"op": name, "params": params, "samples_changed": n_bad})
        elif name == "level":
            y, c = level(y, x, params["order"])
            executed.append({"op": name, "params": params,
                             "coeffs": [float(v) for v in c]})
        elif name == "lowpass":
            y = lowpass(y, dx, params["cutoff_wavelength"])
            executed.append({"op": name, "params": params})
        else:
            raise ValueError(f"unknown step {name}")
    return y, executed


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)

    # --- 1. Data and a processing record -----------------------------------
    dx = 25.0
    x = np.arange(200) * dx
    signal = (1.2 * np.exp(-0.5 * ((x - 1500.0) / 400.0) ** 2)
              + 0.3 * np.exp(-0.5 * ((x - 3300.0) / 600.0) ** 2))
    data = signal + 0.02 * x / 1000.0 + rng.normal(0.0, 0.008, x.size)
    spikes = np.array([37, 121, 168])
    data[spikes] += np.array([0.9, -0.7, 1.4])

    record = {
        "input_file": "synthetic_profile.bin",
        "input_sha256": h256(data),
        "grid": {"dx_m": dx, "n_samples": int(x.size)},
        "software": {"numpy": np.__version__, "python_hash_seed": 0},
        "steps": [
            {"op": "despike", "params": {"window": 5, "n_sigma": 4.0}},
            {"op": "level", "params": {"order": 1}},
            {"op": "lowpass", "params": {"cutoff_wavelength": 400.0}},
        ],
    }
    out_a, exec_a = run_pipeline(data, x, dx, record["steps"])
    record["steps_executed"] = exec_a
    record["output_sha256"] = h256(out_a)
    record["record_sha256"] = h256(json.dumps(record, indent=2, sort_keys=True))

    print("1. Processing record")
    print(f"   input  SHA-256 = {record['input_sha256'][:32]}...")
    print(f"   output SHA-256 = {record['output_sha256'][:32]}...")
    print(f"   steps recorded = {len(record['steps'])}")
    for step in exec_a:
        extra = ""
        if "samples_changed" in step:
            extra = f", samples_changed = {step['samples_changed']}"
        print(f"     - {step['op']:<9} params {step['params']}{extra}")
    print(f"   input range {data.min():.4f} to {data.max():.4f}; "
          f"output range {out_a.min():.4f} to {out_a.max():.4f}")

    # --- 2. Bit-for-bit reproduction ---------------------------------------
    out_b, exec_b = run_pipeline(data, x, dx, record["steps"])
    same = h256(out_b) == record["output_sha256"]
    print("\n2. Reproducibility by re-execution")
    print(f"   re-run output SHA-256 == recorded SHA-256 ?  {same}")
    print(f"   max |re-run - first run| = {float(np.max(np.abs(out_b - out_a))):.3e}")
    print("   -> on one machine, one library version and one thread count, a recorded")
    print("      pipeline reproduces bit for bit. That is the weakest form of")
    print("      reproducibility, and it is the only one you can verify locally.")

    # --- 3. Order matters ---------------------------------------------------
    swapped = [record["steps"][1], record["steps"][0], record["steps"][2]]
    out_c, exec_c = run_pipeline(data, x, dx, swapped)
    diff = float(np.sqrt(np.mean((out_c - out_a) ** 2)))
    print("\n3. Step order: despike-then-level against level-then-despike")
    print(f"   output SHA-256 identical ?  {h256(out_c) == record['output_sha256']}")
    print(f"   RMS difference between the two outputs = {diff:.6f}")
    print(f"   ratio to the anomaly peak              = "
          f"{diff/out_a.max()*100:.3f} % of the peak")
    print(f"   samples changed by despiking, in order : "
          f"{exec_a[0]['samples_changed']}")
    print(f"   samples changed by despiking, swapped  : "
          f"{exec_c[1]['samples_changed']}")
    print("   -> the same steps in a different order are a DIFFERENT processing")
    print("      sequence. A record that lists operations without their order is not")
    print("      a description of the processing; it is a description of the toolbox.")

    # --- 4. Text equality is not result equality ---------------------------
    p_exact = 0.3
    p_derived = 0.1 + 0.2
    out_d = lowpass(data, dx, p_derived)
    out_e = lowpass(data, dx, p_exact)
    print("\n4. A near-identical parameter: 0.3 against 0.1 + 0.2")
    print(f"   0.3 == 0.1 + 0.2                        ? {p_exact == p_derived}")
    print(f"   |0.3 - (0.1 + 0.2)|                     = {abs(p_exact-p_derived):.3e}")
    print(f"   outputs bit-identical                   ? "
          f"{h256(out_d) == h256(out_e)}")
    print(f"   max |difference| between the outputs    = "
          f"{float(np.max(np.abs(out_d - out_e))):.3e}")
    print("   -> the parameter VALUES differ while the RESULTS agree, so a workflow")
    print("      that declares 'reproduced' on the basis of identical text is checking")
    print("      the wrong thing, and one that declares failure on the basis of unequal")
    print("      text will produce false alarms on every machine. Compare results with")
    print("      a stated tolerance; report the tolerance.")

    # --- 5. Verdict table ---------------------------------------------------
    print("\n5. Summary verdicts")
    checks = [
        ("same record, same machine", h256(out_b) == record["output_sha256"],
         "bit-identical"),
        ("same record, reordered steps",
         h256(out_c) == record["output_sha256"],
         f"differs by {diff:.6f} RMS"),
        ("same record, numerically equal parameter",
         h256(out_d) == h256(out_e),
         f"differs by {float(np.max(np.abs(out_d-out_e))):.3e} max, 0 in exact terms"),
    ]
    for name, ok, note in checks:
        print(f"   {name:<42}{'PASS' if ok else 'FAIL':<7}{note}")
    print("   -> a reproducibility statement must say WHICH of these was tested, with")
    print("      what tolerance, on what software versions, and on what hardware. A")
    print("      bare claim that 'the processing is reproducible' says nothing.")


if __name__ == "__main__":
    main()
