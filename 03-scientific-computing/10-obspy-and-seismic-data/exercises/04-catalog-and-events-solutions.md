# Solutions — 03-10-04 Event Catalogs, QuakeML and Phase Metadata

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output. Values marked *measured* come from a modified copy of
> the demonstration, with the modification stated.

---

## ★1 — Units in QuakeML

| field | unit |
|---|---|
| `origin.depth` | **metres** |
| `origin.latitude` | degrees (positive north) |
| `arrival.distance` | degrees |
| `magnitude.mag` | dimensionless |

`origin.longitude` is in degrees positive east, `origin.time` is an absolute
UTC instant, and `arrival.time_residual` is in seconds.

---

## ★2 — `depth = 8000.0`

8000.0 m = **8.0 km**.

A reader who assumed kilometres would place the event at 8000 km depth. That is
deeper than the Earth's centre (6371 km) and 1130 km below the core–mantle
boundary. Every depth-filtered selection (`maxdepth=700 km`) would drop the
event; a map coloured by depth would show it in the deepest colour; a
magnitude–depth plot would show it as an outlier and invite a "deep earthquake"
interpretation. The error is a factor of 1000 and it produces a physically
impossible object, which is the only reason it is usually caught.

---

## ★3 — $M_w$ for $M_0 = 3.2\times10^{19}$ N·m

$$\log_{10} M_0 = \log_{10}(3.2) + 19 = 0.50515 + 19 = 19.50515,$$

$$M_w = \frac{19.50515 - 9.1}{1.5} = \frac{10.40515}{1.5} = 6.9368.$$

So $M_w \approx 6.94$.

---

## ★4 — 0.885075° in kilometres

Spherical rule of thumb:
$0.885075 \times 111.195 = 98.4158$ km, which is exactly the demonstration's
"spherical mean-radius convert" value.

Measured ellipsoidal value: 98.4461 km. The difference is
$98.4461 - 98.4158 = 0.0303$ km = **30.3 m**, i.e. a relative difference of
$3.08\times10^{-4}$. The ellipsoidal distance is *larger* here because the
stations are at 48–49° N, where the meridional radius of curvature exceeds the
mean radius.

---

## ★★5 — Energy ratio for 2.0933 magnitude units

$$\log_{10}\frac{E_2}{E_1} = 1.5(M_2 - M_1) = 1.5 \times 2.0933 = 3.13995,$$

$$\frac{E_2}{E_1} = 10^{3.13995} = 1380.4.$$

This matches the printed `energy ratio Mw vs ML : 1380.384`. The relation is
the same slope-1.5 law that gives $10^{1.5} = 31.6228$ per magnitude unit, and
the demonstration prints both. Two estimates of the same event's size,
differing by a factor of 1380 in energy, is the reason a magnitude must always
be quoted with its scale name.

---

## ★★6 — Two origins, one preferred

```python
from obspy import Catalog, UTCDateTime
from obspy.core.event import Event, Origin, ResourceIdentifier, CreationInfo

event = Event(resource_id=ResourceIdentifier("smi:local/ev"))
fast = Origin(resource_id=ResourceIdentifier("smi:local/fast"),
              time=UTCDateTime("2024-03-15T08:30:12.345Z"),
              latitude=48.10, longitude=11.20, depth=11500.0,
              creation_info=CreationInfo(author="rt", agency_id="XX"))
refined = Origin(resource_id=ResourceIdentifier("smi:local/refined"),
                 time=UTCDateTime("2024-03-15T08:30:12.101Z"),
                 latitude=48.104, longitude=11.206, depth=11800.0,
                 creation_info=CreationInfo(author="analyst", agency_id="XX"))
event.origins.extend([fast, refined])
event.preferred_origin_id = refined.resource_id
event.write("two_origins.xml", format="QUAKEML")

from obspy import read_events
back = read_events("two_origins.xml")[0]
print(len(back.origins), back.preferred_origin().resource_id)
```

Measured: 2 origins survive; the preferred one is `smi:local/refined`; the file
is 1893 bytes. Both origins are retained with their authors, which is the point
of the format: the rapid automatic solution is not destroyed by the analyst's
revision, and a later study can compare them.

---

## ★★7 — 90 % confidence to 1σ

For a normal distribution the two-sided 90 % interval is
$\pm 1.6449\sigma$, so

$$\sigma = \frac{1.1}{1.6449} = 0.6687\ \text{deg} \approx 74.4\ \text{km}.$$

The conversion factor is 1.6449. It is valid only under normality, and location
uncertainties are frequently *not* normal: they are elongated along the
station distribution's weakest direction, sometimes bimodal (two possible
depths), and bounded by the depth range of the search. Converting a 90 %
half-width to a σ and then treating σ as a standard deviation of a normal
distribution is a common and unjustified step. If the catalog gives a
confidence level, propagate at that confidence level and do not invent a
distribution.

---

## ★★8 — Interpreting a 0.31 s S residual

At 30° the S travel time is about 667.6 s (the demonstration tabulates 667.6449 s
at 30° for a 10 km source). The residual is

$$\frac{0.31}{667.6} = 4.64\times10^{-4},$$

i.e. 0.046 % of the travel time.

A 0.31 s residual at 30° corresponds, at a slowness of about 16 s/deg for S, to
$\Delta x \approx 0.31/16 = 0.02$ deg, about 2 km of path length. That is a
plausible mislocation, and it is also a plausible velocity-model error. The
discriminator is **pattern, not size**: a source-location error produces
residuals that vary systematically with azimuth around the event (early on one
side, late on the other), whereas a velocity-model error produces residuals
that correlate with distance or with the ray's turning depth. A single 0.31 s
residual cannot distinguish them, and that is the correct answer to the
question as posed. The full test is in
[06-04-02 Velocity Model Dependence](../../../06-seismology/04-earthquake-location-and-magnitude/02-velocity-model-dependence.md).

---

## ★★★9 — Are the uncertainties consistent with the station geometry?

```python
import numpy as np
from obspy.geodetics import gps2dist_azimuth, degrees2kilometers

def flags(catalog) -> list[str]:
    out = []
    for event in catalog:
        origin = event.preferred_origin() or event.origins[0]
        if not origin.latitude_errors or origin.latitude_errors.uncertainty is None:
            out.append(f"{event.resource_id.id}: no latitude uncertainty")
            continue
        spread_km = origin.latitude_errors.uncertainty * 111.195
        distances = []
        for arrival in origin.arrivals:
            pick = event.picks[[p.resource_id for p in event.picks].index(arrival.pick_id)]
            sta = pick.waveform_id.station_code
            # station coordinates would come from an Inventory; here we use the
            # arrival's own distance in degrees as a proxy
            if arrival.distance is not None:
                distances.append(arrival.distance * 111.195)
        if distances and max(distances) < spread_km:
            out.append(f"{event.resource_id.id}: uncertainty {spread_km:.1f} km "
                       f"exceeds the largest station distance {max(distances):.1f} km")
    return out
```

*Measured* on two hand-built catalogs: the tight one (0.01° latitude
uncertainty = 1.1 km, stations at 88–140 km) raises no flag; the loose one
(1.5° = 167 km, same stations) raises the second flag, because the location
uncertainty exceeds the aperture of the network that produced it. That is a
physically meaningful diagnostic: a network cannot constrain a hypocentre to
better than its own extent.

Note the caveat built into the code: the proxy for the station distance is the
arrival's own reported distance, which is part of the *solution*. A rigorous
version reads the station coordinates from the `Inventory`. The exercise is
worth doing properly with a real inventory; the diagnostic's logic is unchanged.

---

## ★★★10 — Three distance conventions at 5000 km

*Measured* between two points chosen to give a nominal 5000 km separation
(45.0° N 10.0° E to 85.0° N 60.0° E):

| convention | value |
|---|---|
| angular, `locations2degrees` | 45.0577 deg |
| spherical mean radius, `degrees2kilometers` | 5009.44 km |
| WGS84 ellipsoid, `gps2dist_azimuth` | 5016.53 km |
| relative difference | $1.4\times10^{-3}$ |

The difference is 7.09 km. At $p = \mathrm{d}T/\mathrm{d}\Delta \approx 5$ s/deg
and 111.195 km/deg, 7.09 km is 0.0638 deg, i.e. **0.32 s** of P travel time.

**Can a mixed-convention catalog produce a mislocation of more than 1 km?**
The distance error is 7 km in the range, and a mislocation is bounded by
roughly the distance error divided by the number of well-distributed stations
that constrain the same direction. With four to six stations the answer is
easily more than 1 km; with a well-distributed network the direction-dependent
part averages down and the residual bias is smaller. The honest conclusion:
a 1.4 × 10⁻³ relative distance error is *not* negligible for accurate relative
locations, and the fix is trivial — state which convention each stage uses and
convert explicitly.
