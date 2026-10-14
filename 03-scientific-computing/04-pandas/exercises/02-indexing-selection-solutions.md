# Solutions — 03-04-02 Indexing, Selection, loc/iloc and Boolean Masks

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The catalogue is SYNTHETIC; no number below is
> a claim about the Earth.

---

## ★1 — Mask counts on a five-row frame

**(a)** `df["mw"] >= 3.0` selects B (3.4), D (4.1) and E (3.0) — **3 rows**.

**(b)** `df["depth_km"] >= 10.0` selects B (12), D (60) and E (25) — **3 rows**.

**(c)** The intersection is B, D, E — **3 rows**. Here the two conditions happen
to select the same set; that is a coincidence of the numbers, not a rule.

**(d)** The complement of (a) is A (2.2) and C (2.9) — **2 rows**. Check:
3 + 2 = 5 = the number of rows.

---

## ★2 — Label and position slicing

**(a)** `df.iloc[1:4]` returns positions 1, 2 and 3, i.e. labels
`['B', 'C', 'D']`.

**(b)** `df.loc["B":"D"]` returns labels `B`, `C` and `D`.

**(c)** Both return **three rows**, and they agree here only because the index is
contiguous and in order. The slice bounds look different in intent: `iloc`
excludes its stop, so `1:4` is three positions, while `loc` includes its stop, so
`"B":"D"` is three labels. Confusing the two is an off-by-one that shows up as a
row count; check the returned `.index`, not just `len()`.

---

## ★3 — Precedence

**(a)** `TypeError`. The expression parses as
`df["mw"] > (2.5 & df["depth_km"]) < 30.0`, because `&` binds tighter than a
comparison. The demo prints the actual message for the analogous expression:

```
TypeError: Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]
```

**(b)**

```python
subset = df[(df["mw"] > 2.5) & (df["depth_km"] < 30.0)]
```

**(c)** Every comparison goes in its own parentheses, and `&`, `|`, `~` are used
instead of `and`, `or`, `not`.

---

## ★4 — Counts on the synthetic catalogue

From the demo, Section 1:

**(a)** `mw >= 3.0` → **48**.
**(b)** `depth_km < 30` → **275**.
**(c)** `mw >= 3.0 & depth_km < 30` → **36**.
**(d)** `~(depth_km < 30)` → **125**.

Cross-checks: 275 + 125 = 400 rows, and 48 = 36 + 12, so twelve events are at
least M 3.0 and deeper than 30 km.

---

## ★5 — Chained assignment

**(a)** `ChainedAssignmentError`.

**(b)** The target cell held `'Mw'` before and holds `'Mw'` after; the demo prints
`-> modified? False`.

**(c)**

```python
df.loc[df["depth_km"] > 60.0, "mag_type"] = "XX"
```

**(d)** Because pandas only emits the warning when it detects a write through a
temporary object. A write that reaches the frame produces no warning, so the
absence of `ChainedAssignmentError` means the assignment was performed on the
frame itself. (The absence of a warning is evidence, not proof, which is why the
end-of-pipeline assertion in ★9 is worth having as well.)

---

## ★6 — Select and assign

**(a)** **10** events are deeper than 60 km.

**(b)** Before: six rows `SYN-NET1`, four rows `SYN-NET2`. After
`df.loc[deep, "agency"] = "SYN-REVIEW"`: **ten** rows `SYN-REVIEW`. In the demo
this is the output after the assignment:

```
agency
SYN-REVIEW    10
```

**(c)**

```python
assert (df.loc[df["depth_km"] > 60.0, "agency"] == "SYN-REVIEW").all()
```

or, more robustly, capture the mask in a variable and assert on the group sizes
before and after.

---

## ★7 — Two spellings of one selection

**(a)**

```python
mask = ((df["mw"] >= 3.5) & (df["depth_km"] < 20.0)
        & df["region"].isin(["Northvale", "Southgate"]))

q = df.query("mw >= 3.5 and depth_km < 20 and region in @names")   # names = [...]
```

**(b)** **7 events** — the demo's query returns S0043, S0065, S0153, S0206,
S0298, S0340 and S0367.

**(c)** The mask form is preferable when the mask is reused (a second
selection with the same criterion, or a count followed by a selection) because
you then express the criterion once. `query` is preferable when the criterion
involves several `and`/`or` terms and the parentheses would obscure the logic,
and when the criterion is best read as prose.

---

## ★8 — `between` and intervals

**(a)** `between(a, b)` is **inclusive at both ends**: it keeps values `v` with
`a <= v <= b`.

**(b)** `(df["depth_km"] >= 10) & (df["depth_km"] <= 25)` — 143 rows, matching
`between(10, 25)` exactly.

**(c)** `(df["depth_km"] >= 10) & (df["depth_km"] < 25)`. A row is lost only if a
depth is **exactly 25.00**. In the demo's frame the count of depths equal to
exactly 25.0 is **0**, so the half-open interval also returns 143 rows. That is
the honest answer for this dataset, and it is not a general guarantee: on a
catalogue with a coarser depth rounding, values sit on the round numbers and the
two intervals differ by however many events are exactly on the excluded bound.
Always check `(x == bound).sum()` rather than assuming either way.

---

## ★9 — Four sequential edits

**(a)** Lines **(i)** and **(iv)** do not modify the frame.

- **(i)** `df[mask]["agency"] = "DEEP"` is a chained assignment: the boolean
  selection produces a new object, the `"agency"` selection produces another, and
  the write goes to a temporary that is discarded. Under pandas 3 this raises
  `ChainedAssignmentError` (a warning) and nothing is written.
- **(iv)** `df[df["depth_km"] < 0]["depth_km"] = np.nan` is the same pattern one
  level deeper and fails identically.
- **(ii)** and **(iii)** are fine: (ii) is a single-step `.loc` assignment on the
  frame, and (iii) assigns a whole column with `df["n_stations"] = ...`.

**(b)** Repairs:

```python
df.loc[df["depth_km"] > 60.0, "agency"] = "DEEP"
df.loc[df["depth_km"] < 0, "depth_km"] = np.nan
```

The general repair is to turn the two-step chain into a single `.loc[rows, col]`.

**(c)** Turn warnings into errors for the duration of the pipeline, and then
assert on the effect:

```python
with warnings.catch_warnings():
    warnings.simplefilter("error")                 # any chained write becomes fatal
    run_the_pipeline(df)
assert df.loc[df["depth_km"] > 60.0, "agency"].eq("DEEP").all()
```

`simplefilter("error")` converts the silently-dropped write into a crash at the
line that causes it, and the assertion re-checks the effect in case a future
pandas behaves differently.

---

## ★10 — Quality classes with a priority order

**(a)** Assign the lowest-priority class first and overwrite with each
higher-priority one, using single-step `.loc` assignments:

```python
df["quality"] = "ok"
df.loc[df["n_stations"] < 4, "quality"] = "sparse"
df.loc[df["mw"].isna(), "quality"] = "mag-missing"
df.loc[df["depth_km"].isna(), "quality"] = "depth-missing"
```

**(b)** Because each later assignment overwrites the earlier ones for the rows it
matches, the *last* assignment wins, so the list must run from lowest to highest
priority. Reordering the lines reorders the priority: with `"sparse"` written
last, a row with no depth would be labelled `"sparse"` instead of
`"depth-missing"`, and the class counts would change even though every
individual rule was applied correctly.

**(c)** The four class counts must sum to the number of rows, since every row
receives exactly one class:

```python
assert df["quality"].value_counts().sum() == len(df)
```

This is the invariant that catches an assignment that silently failed — the
counts would not sum. On the 400-row frame it returns `ok = 317`,
`sparse = 58`, `depth-missing = 20`, `mag-missing = 5`, and 317 + 58 + 20 + 5 =
400. Note `mag-missing = 5` rather than 7: two of the seven events with no
magnitude also have no depth, and the higher-priority rule claims them.

**(d)** `np.select(conditions, choices, default="ok")` expresses the priority
in one vectorised call and removes any dependence on statement order — a genuine
advantage, since the order-dependence in (b) is a latent bug waiting for someone
to reorganise the lines. The disadvantage is that it builds all the intermediate
masks before selecting, so on a large frame it uses more peak memory, and it is
harder to insert a per-rule count (`how many rows did rule 2 claim?`) than the
sequential form, which can log after each step.
