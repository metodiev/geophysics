# Solutions — 03-11-01 PyGMT Fundamentals and the GMT Ecosystem

> **Read this after attempting the exercises.** All values are the demonstration's
> actual output, produced with PyGMT 0.19.0, GMT 6.7.0, Ghostscript 10.08.0 and
> Python 3.14.4.

---

## ★1 — Four components, four failures

| Component | Failure if missing |
|---|---|
| `pygmt` | `ModuleNotFoundError: No module named 'pygmt'` at import |
| `libgmt` | import may succeed; the first drawing call fails |
| `gmt` executable | data and defaults are unavailable; some calls fail |
| Ghostscript (`gs`) | drawing succeeds; `savefig` raises `GMTCLibError` about executing `gs` |

Measured on this machine: `GMT library :
/opt/homebrew/Cellar/gmt/6.7.0/lib/libgmt.dylib`,
`GMT sharedir : /opt/homebrew/Cellar/gmt/6.7.0/share/gmt`,
`ghostscript : 10.08.0`. Install with `brew install gmt ghostscript` (macOS) and
`pip install pygmt`.

---

## ★2 — Decoding projections

| Argument | Projection | Use |
|---|---|---|
| `-JM12c` | Mercator, 12 cm wide | navigation-style maps; conformal, exaggerates high latitudes |
| `-JQ45/12c` | equidistant cylindrical at standard parallel 45° | quick rectangular regional maps; east-west scale true at 45° |
| `-JL0/45/43/47/12c` | Lambert conformal conic, centre 0/45, parallels 43 and 47 | mid-latitude regional maps with little distortion |
| `-JW0/12c` | Mollweide | whole-Earth equal-area context maps |

---

## ★3 — 160 mm at 300 dpi

$$160\ \mathrm{mm} = 6.299\ \mathrm{in}, \qquad 6.299 \times 300 = 1890\ \mathrm{px}.$$

The measured relationship confirming the arithmetic: `width/dpi = 2.833 in` at
three different dpi values (204/72, 425/150, 850/300).

---

## ★4 — `-R`, `-J`, `-B`

`-R` is the region, wrapped by `region=[lon_min, lon_max, lat_min, lat_max]`;
`-J` is the projection, wrapped by `projection="M8c"`; `-B` is the frame and axes,
wrapped by `frame=["a2f1", "WSen"]`. Measured equivalence:
`fig.basemap(region=REGION, projection="M8c", frame=["a2f1", "WSen"])` is
`gmt basemap -R-10/10/35/45 -JM8c -Ba2f1 -BWSen`.

---

## ★5 — Why a scale bar is latitude-specific

Because the scale factor varies with latitude on any projection that is not
equidistant along the bar's direction. Measured: `Q` and `M` both give east-west
scale factors of `1.24253` at 36.5° N and `1.37641` at 43.5° N, so a bar drawn at
one of those latitudes understates or overstates distance at the other by about
10 %. Only where $k = 1$ is the bar exact.

---

## ★6 — Mercator and equidistant cylindrical share their east-west scale

Both have $x = R(\lambda - \lambda_0)$, so the east-west spacing per degree of
longitude is identical, and therefore $k_{\text{EW}} = 1/\cos\phi$ for both.
Measured (which is the evidence, not the algebra):

```
     Q   1.24253  1.30360   1.37641    1.30541  363 x 182
     M   1.24253  1.30360   1.37641    1.30541  363 x 230
```

They differ only in the north-south direction, which is what makes Mercator
conformal and the equidistant cylindrical projection not.

---

## ★7 — Choosing a projection for 20° × 15° at 30–45° N

Two measured candidates:

- **Albers equal-area (`B`) with standard parallels 30 and 45**: $k = 1.00000$ on
  both parallels and slightly less between them, with exact area preservation.
- **Mercator (`M`)**: $k = 1/\cos\phi$, so at 45° N it is 1.41 — a 41 % east-west
  stretch, and areas are distorted by the square of that.

**Choose Albers** for a geological or anomaly-density map: the distortion is an
order of magnitude smaller, and area is preserved, which matters if the map is read
quantitatively.

---

## ★8 — The 6 MB figure

```
  frame=['WSen']   ...   45510 x 45510 px, 6189144 bytes
```

The undefined parameter is the annotation interval. A frame with only side letters
draws no axes, so GMT cannot determine a bounding box and rasterises the whole
PostScript medium. Passing `crop=False` to `savefig` has the same effect. The same
call with `frame=["a2f1"]` produced `284 x 178 px, 2544 bytes` — a factor of
2434 in file size.

---

## ★9 — dpi and pixel width

Measured for `M6c`:

| dpi | width (px) | bytes |
|---|---|---|
| 100 | 204 | 1534 |
| 200 | 425 | 3985 |
| 400 | 850 | 7410 |

Ratios: $425/204 = 2.083$ against a dpi ratio of 2, and $850/204 = 4.167$ against
4. The small excess is the rounding of the physical size to whole pixels; the
measured `width/dpi` was constant at 2.833 in to three decimals.

---

## ★10 — Your version block

Report what your machine prints; the comparison that matters is the *major*
version of GMT (projection syntax has changed across versions) and whether PyGMT is
0.19 or later (the `Position` API and `scalebar` differ from earlier releases). If
your GMT is older, the conic projection syntax in ★2 may need different parameters,
and the `params.Position` usage in lesson 04 will not exist.

---

## ★11 — A distortion atlas

The measured template is the lesson's table: for a $12° \times 8°$ region,
`Q`/`M` give 1.30 at the centre (a 30 % east-west stretch), `L`/`B` give 0.996–1.000,
`E`/`S` give 1.000 at the centre and 1.001 at 3.5° away, and `W` gives 0.977–1.015.
The report should state min, max and spatial standard deviation per projection.

Recommendations: (a) geological map — a conformal projection (`L`, `S` or UTM) so
angles and local shapes are right; (b) equal-area comparison — `B` or `W`;
(c) location index map — anything, because only the relative position of features
matters, and a familiar projection is better than a correct one.

---

## ★12 — GMT against `pyproj`

For Mercator the closed form is $k = 1/\cos\phi$ on a sphere; `pyproj` with an
ellipsoid adds the factor $\sqrt{1 - e^2\sin^2\phi}/\cos\phi$-type correction. The
measured difference at 40° N was `0.14 %`:
`spherical 1/cos(40.0) = 1.30541`, `Mercator measured = 1.30360`.

Whether that is *entirely* the sphere-versus-ellipsoid distinction is not
established by this single number — the geodesic reference on WGS84 and the
projection's own radius convention both contribute, and separating them needs a
controlled test with `+a`/`+b` set explicitly. **State the number and the
limitation.** The lesson does exactly that.
