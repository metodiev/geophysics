# Solutions — 03-11-04 Layout, Insets, Legends and Multi-Panel Maps

> **Read this after attempting the exercises.** All values are the demonstration's
> actual output, produced with PyGMT 0.19.0, GMT 6.7.0 and Python 3.14.4.

---

## ★1 — 90 mm at 300 dpi

$$90\ \mathrm{mm} = 3.543\ \mathrm{in}, \qquad 3.543 \times 300 = 1063\ \mathrm{px}.$$

Verified against the demonstration's measured relation
`width/dpi = 2.833 in` at three dpi values.

---

## ★2 — Decoding a position

`j` introduces a justified position, `BL` is the bottom-left corner of the map
frame, and `+o0.5c/0.5c` offsets it 0.5 cm right and 0.5 cm up. Measured rendering
from a `pygmt.params.Position` object:

```
  pygmt.params.Position('BL', offset=(0.6, 0.6)) renders as 'jBL+o0.6/0.6'
```

---

## ★3 — Legend spec codes

| Code | Draws |
|---|---|
| `H` | a header line |
| `S` | a symbol (line, circle, rectangle) with a label |
| `D` | a dividing line |
| `T` | plain text |
| `G` | a vertical gap |

Measured spec (7 non-empty lines) and its note: **`G` and `T` only work once the
legend has a width**, because GMT requires `-D...+w` for codes other than
D, H, L, S, V.

---

## ★4 — Scale bars and conformality

Mercator's east-west scale factor is $1/\cos\phi$ (measured in lesson 01:
`1.24253` at 36.5° N, `1.37641` at 43.5° N). A bar of fixed drawn length therefore
represents a different true distance at every latitude. It is exact only at the
latitude for which its length was computed.

---

## ★5 — A locator rectangle

Five points: `(lon0, lat0)`, `(lon1, lat0)`, `(lon1, lat1)`, `(lon0, lat1)`,
`(lon0, lat0)`. The fifth closes the polygon; with four, GMT draws three sides and
the reader sees an open bracket rather than a box.

---

## ★6 — A 2 × 2 panel figure

Prediction: $(2 \times 6 + 0.4)/2.54 \times 150 = 732$ px for the two 6 cm panels
and the gutter. The demonstration's measured comparison at 8 cm panels and 100 dpi
was

```
  two panels plus the gap = 654 px (measured 699 px, difference +45 px)
```

so the margin was 45 px = 1.14 cm at 100 dpi. At 150 dpi expect the margin in
centimetres to be similar (it is a physical margin), i.e. about 68 px, and the
canvas width about $732 + 68 = 800$ px. **Report your measured value**: the point
is that the margin is a measurable physical quantity, not a nuisance.

---

## ★7 — Scale bars for a 20° map at 20° N

One degree of longitude at 20° N is $111.32\cos20° = 104.6$ km, so 20° spans
2092 km.

| Bar | Degrees | Fraction of map width |
|---|---|---|
| 200 km | 1.912° | 9.6 % |
| 500 km | 4.780° | 23.9 % |
| 1000 km | 9.560° | 47.8 % |

**Use 1000 km** here: it is under half the map width and gives the reader a
coarse, easily read reference. A 200 km bar would be small enough to be hard to
read against the frame.

---

## ★8 — An inset with an area ratio of 4.0

With the main map $12° \times 8°$, an inset four times the area is, for example,
$24° \times 16°$ centred on the same point — e.g. $[-18, 6]$ longitude and
$[38, 54]$ latitude. Measured template from the demonstration:

```
  main map  : [-6.0, 6.0, 42.0, 50.0], 12 x 8 deg, about 827,823 km^2
  inset     : [-14.0, 14.0, 34.0, 58.0], 28 x 24 deg, about 5,794,762 km^2
  the inset therefore shows 7.00 times the area of the main map
```

Use the same $\mathrm{km^2}$ approximation (one km-per-degree factor per
direction) and report the ratio.

---

## ★9 — The legend error

Omitting `width` while using `G` or `T` raises

```
GMTCLibError: Module 'legend' failed with status code 72:
legend [ERROR]: Must specify -D...+w<width> if codes other than D, H, L, S, V are used
```

Adding `width="5c"` fixes it. And in PyGMT 0.19 a second constraint appears if you
also pass a raw GMT position string:

```
GMTParameterError: Conflicting parameters: 'position' cannot be used with 'width',
'height', 'line_spacing'.
```

so use `position=pygmt.params.Position("TR", offset=0.2)` with `width="5c"`.
Measured canvas with the fixed legend: `(441, 404) px, 9371 bytes`.

---

## ★10 — A two-panel figure to specification

For a 184 mm double-column at 300 dpi: 2173 px total. Two panels of 88 mm
(1039 px) plus an 8 mm gutter (94 px) gives 2172 px of drawing, plus the frame and
annotation margin. **Report the difference**: it is the margin of ★6, and it is why
a figure specified "to the column width" is usually slightly over and has to be
scaled by the publisher. Choosing a map width of 86 mm instead of 88 mm is the
prophylactic.

---

## ★11 — A submission-ready figure

The eight decisions to document, from the lesson's §7 table: map width,
resolution, region, projection, scale-bar length, inset region, legend contents,
frame specification. Report them for your figure, plus:

- final canvas in pixels and millimetres (measured from the PNG header);
- file size in bytes;
- font size used and how you verified it (measure a text element's pixel height,
  or trust the point size and state that you did).

If the specification were 20 % narrower: the map width keyword shrinks (e.g. `M10c`
to `M8c`), the scale bar gets shorter (a 250 km bar would become 33 % of the width
rather than 27 %), and the inset box shrinks proportionally — but the *legend*
does not shrink, which is the decision that usually has to change.

---

## ★12 — The layout margin

Measure the same map at four widths with identical annotations and subtract. From
the demonstration's single measurement (8 cm map → 699 px canvas at 100 dpi,
requested 654 px, margin 45 px = 1.14 cm), the margin is dominated by the tick
length and the annotation text size and is therefore **approximately constant** in
centimetres, not proportional to the map width.

The implication for a hard column width: a larger map gets a *relatively* smaller
margin, so if you are just over the limit, shrinking the map is less effective
than shortening the annotations (fewer digits, smaller font) or reducing the tick
length. Fit your four measurements to check whether the margin is constant; if it
grows slightly with width, it is because longer annotations appear.
