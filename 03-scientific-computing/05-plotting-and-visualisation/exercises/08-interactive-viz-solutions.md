# Solutions — 03-05-08 Interactive Exploration: Plotly and HoloViews

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — Pixel budget

**(a)** $496 \times 308 = 152\,768$ distinct pixels.

**(b)** Points per occupied pixel $= 1\,000\,000/14\,287 = 70.0$; fraction of the
budget used $= 14\,287/152\,768 = 9.35$ %.

**(c)** The points per occupied pixel. The fraction of the budget says only how much
of the canvas is touched; a figure could occupy 100 % of the canvas with a dense
field and still carry a readable gradient. The points per occupied pixel says how
many observations are competing for the same colour, and once that number is well
above 1 the display saturates: additional data change the darkness of a region, not
its apparent structure.

---

## ★2 — What a clip removes

**(a)** If magnitude and depth were independent and each variable's 1–99 box removed
1 % at each end, the joint box would remove
$1 - 0.99 \times 0.99 = 1.99$ % of the catalogue.

**(b)** The measured 3.67 % is larger because magnitude and depth are *not*
independent: shallower events are on average smaller in the synthetic model
(magnitude decreases with $\log_{10}$ depth), so the corners of the percentile box
contain more events than independence would predict. A joint percentile box on
correlated variables always removes at least the independent expectation and
usually more.

**(c)** Because the removed events are not a random sample. The deepest events in a
catalogue are the ones that argue for a subducting slab, and the largest are the
hazard; a clip that removes them removes exactly the observations the figure may
have been drawn to show. A count of 7347 conveys none of that.

---

## ★3 — A brushing selection

**(a)** $54/60\,120 = 0.000898 = 0.09$ %.

**(b)** The two x limits, the two y limits, and the rule — five numbers in total
(here `magnitude ∈ [5.2, 6.4]`, `depth ∈ [250.0, 690.0]` km, bounds inclusive and
combined with AND).

**(c)** The five numbers defining the window, and the criterion for the statistic
(count, mean, median, and whether the statistic is unweighted). Without the window
the selection cannot be reproduced, and without the statistic definition the
reported numbers cannot be checked.

---

## ★4 — Interactions and their counterparts

| Interaction | Static counterpart | What static does better |
|---|---|---|
| (a) Zoom | the author's chosen view | shows the whole extent at once, so the reader knows what is not visible |
| (b) Hover | a table or a data appendix | shows many values simultaneously and is printable |
| (c) Brushing | a stated subset with its statistics | makes the criterion explicit, so the result can be checked |
| (d) Toggling a series | a small multiple or a panel per series | guarantees that every reader sees the same comparison |

---

## ★5 — Running the demonstration

**(a)** The axes box and the budget:

```text
  the axes box of a 6.4 x 4.0 in figure at 100 dpi measures 496 x 308 px
  = 152768 distinct pixels. That is the entire budget the
  display has for showing how many events fall where.
```

**(b)** Pixel occupancy:

```text
    n points   savefig (s)  file (kB)   occupied pixels  points / pixel
        1000         0.019       18.3               804            1.24
       10000         0.018       28.1              3322            3.01
      100000         0.022       36.1              7386           13.54
     1000000         0.062       54.0             14287           69.99
```

**(c)** The catalogue:

```text
  catalogue: 200400 SYNTHETIC events
  magnitude 1-99 percentile box: [3.419, 5.722]
  depth     1-99 percentile box: [1.854, 83.133] km
  events outside the box: 7347  (3.67 %)
    of those, deepest 689.2 km, largest magnitude 7.60
```

**(d)** The brush:

```text
  brush window: magnitude in [5.2, 6.4], depth in [250.0, 690.0] km
  selected: 54 of 60120 events (0.09 %)

  statistic                full catalogue     selection
  count                         60120.000        54.000
  mean magnitude                    4.561         5.968
  median magnitude                  4.557         5.995
  mean depth (km)                  17.390       508.374
  median depth (km)                11.942       500.317
```

**(e)** Live state: eighteen numbers in total, from two x limits through
`which series are visible: 1`.

---

## ★6 — Reading the occupancy table

**(a)** Point ratios: $10\,000/1000 = 10$; $100\,000/10\,000 = 10$;
$1\,000\,000/100\,000 = 10$. Occupied-pixel ratios: $3322/804 = 4.13$;
$7386/3322 = 2.22$; $14\,287/7386 = 1.93$.

**(b)** $1000/804 = 1.24$; $10\,000/3322 = 3.01$; $100\,000/7386 = 13.54$;
$1\,000\,000/14\,287 = 69.99$ — the same values the table reports.

**(c)** The threshold should be where the occupied-pixel growth rate drops well
below the point-count growth rate. Between 1000 and 10 000 points the ratio of
growth rates is $4.13/10 = 0.41$; between 100 000 and 1 000 000 it is
$1.93/10 = 0.19$. By 100 000 points the display already has 13.54 points per
occupied pixel, so no single pixel is showing a distinguishable value. A defensible
threshold is therefore around $10^4$–$10^5$ points, i.e. when the points per
occupied pixel passes about 10 — at which stage a density encoding, aggregation or
interactivity is indicated rather than a denser scatter.

---

## ★7 — A percentile clip

**(a)** $0.0367 \times 200\,400 = 7355$ events — the demonstration measures 7347,
the small difference being whether the fraction is taken as 3.67 % exactly or
recomputed from the integer count.

**(b)** An exact mean depth for the removed events needs their individual depths, or
at least the sum of depths over the removed set; the deepest value and the
catalogue mean are not sufficient. What can be said is a bound: since the removed
set contains 689.2 km and the catalogue spans 0–700 km, and the removed set is only
3.67 % of the catalogue, the removed mean must be well above the catalogue mean of
17.39 km, and the demonstration's brushing exercise shows that several hundred
kilometres is the right order.

**(c)** Plot the events outside the clip in a distinct symbol — for example small
unfilled circles drawn on top of the clipped field — and state the clip in the
caption. The events become visible; the clip is unchanged; and the reader can see
both the field's contrast and the outliers.

---

## ★8 — Fixing a view as numbers

**(a)** A plain scatter view with a brush selection needs: 2 x limits, 2 y limits,
4 selection-window numbers and 2 numbers for the selection rule — 10 of the 18.
Add the 2 colour limits if the figure displays a colour scale, giving 12.

**(b)** Irrelevant here: the z/colour limits (2 numbers) when no colour scale is
shown, the zoom level and centre (3, because the axis limits already fix the view),
the hovered datum (2, a transient state with no bearing on the figure), and which
series are visible (1, because there is only one series). That is 8 of the 18.

**(c)** The selection *rule* is hardest to report as a number, because it is a
predicate rather than a quantity: inclusive versus exclusive bounds, AND versus OR
combination, and whether the comparison is on raw or derived values. It is reported
in words, precisely enough to be reimplemented — for example "events with
$5.2 \le M \le 6.4$ and $250 \le z \le 690$ km".

---

## ★9 — Choosing a display for a cluster

**(a)** The static **raster-density map** answers it. The question is whether a
cluster is spatially distinct, which is a question about *density contrast*. With
500 000 events and a pixel budget of order $10^5$, a scatter puts 70 points per
occupied pixel and the cluster's internal structure merges into a dark blob, so the
scatter cannot show the contrast that the question asks about. A density map
computes the density explicitly — via a 2-D histogram, a hexbin, or a KDE — and
displays the one quantity that carries the answer, with a sequential palette so the
contrast is readable.

**(b)** The interactive scatter contributes the *individual* events: once the
cluster is identified as distinct by density, the reader may want to know how many
events it contains, whether they form a lineament, and whether a few large events
dominate it. Those are per-event questions, and they are answered by zooming and
hovering on the cluster — which is exactly the "details on demand" step.

**(c)** By recording the density estimator and its bandwidth (or the histogram's bin
size), the colour limits, and the extent; and, if a cluster was outlined or its
members counted, by publishing the polygon or the selection window plus the count
and the statistic. Then a reader can regenerate the same raster and verify the
cluster's contrast without needing the interactive tool.

---

## ★10 — Pinning an interactive artifact

**(a)** Four things: the library version (Plotly or HoloViews and its backend), the
renderer or browser version, the figure specification itself (which must be
committed, not only the HTML output), and the data snapshot or a content hash of it.
Without all four, the same specification can render differently.

**(b)** It has a property a PNG cannot have: the reader can interrogate it —
zoom, hover, select — and can follow a link from a point to a record. It lacks a
property a PNG has: a single, fixed, citable view. A reader who wants to refer to a
specific observation in an interactive artifact has to describe the state, whereas
a PNG's pixel content is the reference.

**(c)** The risk is silent drift: the artifact renders differently after a library
or browser update, with no diff and no error, so a figure that supported a
published claim can change without anyone noticing. The mitigation is to commit the
specification and a pinned environment (a lock file, or a container image) alongside
the HTML, and to include a static export of the claim-bearing view — so the claim
remains checkable even if the interactive artifact drifts.
