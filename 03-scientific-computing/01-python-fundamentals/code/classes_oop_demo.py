"""Classes and objects: when a class earns its place, and when it does not.

Run:  python3 classes_oop_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-08.  A class is justified by *invariants* - facts
that must stay true for every object of the type - and by behaviour that
belongs to the data.  A bag of numbers with no invariants and no behaviour is a
dict, a tuple or a dataclass, and dressing it as a class buys nothing.

Demonstrates:

1. A SeismicTrace class that does earn its place: metadata plus samples plus
   an invariant enforced at construction.
2. __repr__, __len__, __eq__ and a computed property.
3. classmethod construction from a row, and staticmethod for a pure formula.
4. A frozen dataclass for a station record, with validation in __post_init__.
5. Size and clarity compared across tuple, namedtuple, dataclass and class.
6. The counter-example: a function that is better than a class.
"""

import math
import sys
from dataclasses import dataclass, field

SECTION_WIDTH = 72


def section(title):
    print(f"\n{'=' * SECTION_WIDTH}\n{title}\n{'=' * SECTION_WIDTH}")


# --------------------------------------------------------------------------
# 1. A class that earns its place
# --------------------------------------------------------------------------

class SeismicTrace:
    """A single-channel seismic trace: samples plus the metadata they need.

    The invariant of this type is: *samples are meaningless without a
    sampling rate*.  That is why the two travel together and why the
    constructor refuses to build a trace without a positive rate.

    Attributes are deliberately simple types: a list of floats in volts, an
    integer sample rate in hertz, and a station code as text.
    """

    __slots__ = ("station", "sampling_rate_hz", "samples", "units")

    def __init__(self, station, sampling_rate_hz, samples, units="V"):
        if not isinstance(station, str) or not station:
            raise ValueError(f"station must be a non-empty string, got {station!r}")
        if sampling_rate_hz <= 0:
            raise ValueError(
                f"sampling rate must be positive, got {sampling_rate_hz!r} Hz")
        if not samples:
            raise ValueError("a trace with no samples is not a trace")
        self.station = station
        self.sampling_rate_hz = float(sampling_rate_hz)
        self.samples = [float(s) for s in samples]
        self.units = units

    # -- representation ----------------------------------------------------
    def __repr__(self):
        return (f"SeismicTrace({self.station!r}, {self.sampling_rate_hz:g} Hz, "
                f"{len(self.samples)} samples, peak {self.peak:.3e} {self.units})")

    def __len__(self):
        return len(self.samples)

    def __eq__(self, other):
        if not isinstance(other, SeismicTrace):
            return NotImplemented
        return (self.station == other.station
                and self.sampling_rate_hz == other.sampling_rate_hz
                and self.samples == other.samples)

    # -- computed properties ----------------------------------------------
    @property
    def npts(self):
        """Number of samples."""
        return len(self.samples)

    @property
    def duration_s(self):
        """Length of the trace in seconds: (n - 1) sample intervals.

        The (n - 1) is the whole reason this is a property and not an
        attribute: a trace of n samples spans n-1 intervals, and the
        off-by-one is the most common error in seismology code.
        """
        return (self.npts - 1) / self.sampling_rate_hz

    @property
    def mean(self):
        return sum(self.samples) / self.npts

    @property
    def rms(self):
        return math.sqrt(sum(s * s for s in self.samples) / self.npts)

    @property
    def peak(self):
        return max(abs(s) for s in self.samples)

    # -- behaviour ---------------------------------------------------------
    def detrend(self):
        """Remove the mean amplitude in place and return self."""
        m = self.mean
        self.samples = [s - m for s in self.samples]
        return self

    def decimate(self, factor):
        """Return a new trace with every ``factor``-th sample kept."""
        if factor < 1:
            raise ValueError("decimation factor must be >= 1")
        return SeismicTrace(self.station, self.sampling_rate_hz / factor,
                            self.samples[::factor], self.units)

    # -- alternative constructors and pure helpers -------------------------
    @classmethod
    def from_row(cls, row):
        """Build a trace from a parsed CSV row (a dict of strings)."""
        samples = [float(x) for x in row["samples"].split("|")]
        return cls(row["station"], float(row["sampling_rate_hz"]), samples)

    @staticmethod
    def impedance(density, velocity):
        """A pure formula that needs no instance: rho * v."""
        return density * velocity

    # -- arithmetic --------------------------------------------------------
    def __add__(self, other):
        """Stack two traces with identical geometry, end to end."""
        if (self.station != other.station
                or self.sampling_rate_hz != other.sampling_rate_hz):
            raise ValueError("cannot stack traces with different geometry")
        return SeismicTrace(self.station, self.sampling_rate_hz,
                            self.samples + other.samples, self.units)


def synthetic_trace(station="STA01", rate_hz=100.0, n=500):
    """A SYNTHETIC decaying sinusoid: deterministic, no random numbers."""
    samples = [2.5 * math.exp(-t / 120.0) * math.sin(2.0 * math.pi * 4.0 * t / 100.0)
               for t in range(n)]
    return SeismicTrace(station, rate_hz, samples)


@dataclass(frozen=True, order=True)
class Station:
    """A station record: data with no behaviour, so a frozen dataclass."""

    code: str
    latitude: float
    longitude: float
    elevation_m: float = field(default=0.0)

    def __post_init__(self):
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError(f"latitude out of range: {self.latitude}")
        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError(f"longitude out of range: {self.longitude}")


def part1_class():
    section("1. A class that carries its own invariants")
    trace = synthetic_trace()
    print(f"  {trace}")
    print(f"  npts          = {trace.npts}")
    print(f"  duration_s    = {trace.duration_s:.4f} s"
          f"  (= {trace.npts - 1} intervals at {trace.sampling_rate_hz:g} Hz)")
    print(f"  mean          = {trace.mean:.6e} V")
    print(f"  rms           = {trace.rms:.6e} V")
    print(f"  peak          = {trace.peak:.6e} V")
    print(f"  len(trace)    = {len(trace)}")
    print()
    for bad, why in ((0.0, "zero sampling rate"), (-1.0, "negative rate")):
        try:
            SeismicTrace("STA01", bad, [1.0, 2.0])
        except ValueError as exc:
            print(f"  rejected {why}: {exc}")
    print()
    print("  The invariant is enforced once, in __init__, and every method can")
    print("  then assume it.  That is the difference between a class and a")
    print("  dict: a dict cannot refuse to hold a zero sampling rate.")


def part2_repr_eq():
    section("2. __repr__, __eq__ and why they are not cosmetic")
    a = synthetic_trace()
    b = synthetic_trace()
    c = synthetic_trace(station="STA02")
    print(f"  a == b (same data)  : {a == b}")
    print(f"  a is b              : {a is b}")
    print(f"  a == c (other code) : {a == c}")
    print(f"  repr(b)             : {b!r}")
    print()
    print("  __eq__ makes 'did this processing step change the trace?' a")
    print("  one-line test.  __repr__ makes a failing assertion print the data")
    print("  rather than '<SeismicTrace object at 0x10f2...>'.")


def part3_constructors():
    section("3. classmethod and staticmethod: two different jobs")
    row = {"station": "STA07", "sampling_rate_hz": "50",
           "samples": "0.0|1.0|-1.0|0.5"}
    trace = SeismicTrace.from_row(row)
    print(f"  from_row -> {trace!r}")
    print(f"  impedance(2670.0, 3000.0) = {SeismicTrace.impedance(2670.0, 3000.0):,.1f}"
          f" kg m^-2 s^-1")
    print()
    print("  from_row is a classmethod because it needs the class (for cls(...))")
    print("  and not an instance.  impedance is a staticmethod: it is a formula")
    print("  that happens to live with the class for discoverability.  Calling")
    print("  it never touches self, which is the test for staticmethod.")


def part4_dataclass():
    section("4. A frozen dataclass for a record with no behaviour")
    stations = [Station("STA02", 47.3769, 8.5417, 408.0),
                Station("STA01", 47.3711, 8.5421, 412.0)]
    print(f"  {stations[0]}")
    print(f"  frozen: assignment is refused -> ", end="")
    try:
        stations[0].elevation_m = 500.0
    except Exception as exc:
        print(f"{type(exc).__name__}: {exc}")
    print(f"  order=True, sorted : {[s.code for s in sorted(stations)]}")
    print(f"  hashable           : {{s: i for i, s in enumerate(stations)}} has"
          f" {len({s: i for i, s in enumerate(stations)})} entries")
    print()
    try:
        Station("STA03", 91.0, 8.0)
    except ValueError as exc:
        print(f"  validation fires   : {exc}")
    print()
    print("  A dataclass generates __init__, __repr__ and __eq__; frozen adds")
    print("  hashability and immutability; __post_init__ adds validation.  That")
    print("  is a record, and no class body of hand-written methods is needed.")


def part5_sizes():
    section("5. Four ways to hold the same four fields")
    from collections import namedtuple

    def plain_class(code, lat, lon, elev):
        """A bare class with instance attributes and no __slots__."""
        class _S:
            pass
        s = _S()
        s.code, s.latitude, s.longitude = code, lat, lon
        s.elevation_m = elev
        return s

    Named = namedtuple("Named", "code latitude longitude elevation_m")
    variants = [
        ("tuple", ("STA01", 47.3711, 8.5421, 412.0), True),
        ("namedtuple", Named("STA01", 47.3711, 8.5421, 412.0), True),
        ("dataclass", Station("STA01", 47.3711, 8.5421, 412.0), True),
        ("plain class", plain_class("STA01", 47.3711, 8.5421, 412.0), False),
    ]
    print(f"  {'form':<16}{'sys.getsizeof':>14}{'has names':>12}{'immutable':>11}")
    for name, obj, frozen in variants:
        print(f"  {name:<16}{sys.getsizeof(obj):>14,}"
              f"{str(hasattr(obj, 'code')):>12}{str(frozen):>11}")
    print()
    print("  __slots__ on SeismicTrace removes the per-instance dict: it costs")
    print("  you dynamic attributes and buys back memory in a 10^6-trace loop.")
    print("  getsizeof is shallow, so read this table as guidance, not truth.")


def part6_counterexample():
    section("6. The counter-example: a function is better than a class")
    def bouguer_slab_mgal(h_m, rho=2670.0):
        return 2.0 * math.pi * 6.67430e-11 * rho * h_m / 1.0e-5

    print(f"  bouguer_slab_mgal(100.0) = {bouguer_slab_mgal(100.0):.4f} mGal")
    print()
    print("  Wrapping this in a BouguerCorrector class would add a constructor,")
    print("  an attribute and a name to learn, and remove nothing.  Use a class")
    print("  when there is state to protect across calls or several operations")
    print("  that share that state - a trace with metadata, a survey with an")
    print("  instrument calibration.  Otherwise use a function.")


if __name__ == "__main__":
    part1_class()
    part2_repr_eq()
    part3_constructors()
    part4_dataclass()
    part5_sizes()
    part6_counterexample()
