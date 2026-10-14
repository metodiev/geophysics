---
id: 03-04-02
title: "Indexing, Selection, loc/iloc and Boolean Masks"
level: beginner
prereqs: ["03-04-01"]
estimated_minutes: 75
tags: [pandas, indexing, loc, iloc, boolean-mask, chained-assignment]
---

# Indexing, Selection, loc/iloc and Boolean Masks

Having a labelled table is only useful if you can ask precise questions of it.
"Which events are deeper than 60 km?" and "what is the magnitude of event
S0007?" are different kinds of question — one selects a *set* of rows by a
condition, the other addresses a *single* cell by its labels — and pandas
answers them with different tools.

The tools are `[]`, `.loc`, `.iloc` and `.at`/`.iat`. The single most important
thing in this lesson is that **`.loc` works in labels and `.iloc` works in
positions**, and that mixing them up produces either a wrong answer or an
`IndexError` rather than a shrug. The second most important thing is that
assigning through a chained expression does not do what it looks like it does.

> The catalogue is **SYNTHETIC** (see `code/synthetic_catalog.py`): generated
> in-code, not the USGS catalogue and not an observation of the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a boolean mask, use it to select rows, and say what type it is and
   how long it is relative to the frame.
2. **Combine** masks with `&`, `|` and `~`, and explain why every comparison
   must be parenthesised.
3. **Select** rows and columns in one step with `.loc[mask, columns]` and state
   why that single step is the correct pattern for assignment.
4. **Distinguish** `.loc` from `.iloc`, including the inclusive-versus-exclusive
   slicing asymmetry, and predict the labels each returns.
5. **Explain** what Copy-on-Write does to a chained assignment, what pandas 3
   raises in response, and why the old `SettingWithCopyWarning` is gone.
6. **Choose** between `between`, `isin`, `query` and an explicit mask for a
   given condition, and say which one documents the intent best.
7. **Select** a single scalar with `.at`/`.iat` and know when the index look-up
   is not worth it.

## Prerequisites

- [03-04-01 Series, DataFrame and the Labeled-Data Model](./01-series-dataframe.md)
  — the index is what `.loc` addresses, so it must be understood first.

## 1. Four ways to address a table, and what each addresses

| Form | Addresses | Notes |
|---|---|---|
| `df[bool_mask]` | rows by condition | the workhorse selection |
| `df["col"]` / `df[["a", "b"]]` | columns by name | never rows, despite appearances |
| `df.loc[rows, cols]` | label-based | inclusive on label slices |
| `df.iloc[rows, cols]` | position-based | exclusive on slices, like Python |
| `df.at[r, c]` / `df.iat[i, j]` | one scalar | faster than `loc`/`iloc` for scalars |

The confusing part of `df[...]` is that it is a hybrid: given a boolean mask it
selects rows, given a column name it selects a column. That overloading is
historical. The unambiguous modern spelling is `.loc`, and code that reads well
six months later uses it.

## 2. Boolean masks

### 2.1 What a mask is

`df["depth_km"] < 30` does not return numbers. It returns a `Series` of `bool`
with the *same index* as the frame and one entry per row. That is why it can be
used as a row selector: pandas takes the `True` positions and keeps those rows,
carrying the remaining columns along.

Because the mask is a `Series`, it participates in alignment like anything else.
`len(mask)` equals the number of rows; `mask.sum()` counts the `True`s, because
`True` is 1 when you sum it. Counting by summing a mask is a habit worth having:
`int((df["mw"] >= 3.0).sum())` is a per-condition event count in one expression.

### 2.2 Combining conditions, and the precedence trap

Python's `and`, `or` and `not` do not work element-wise on arrays; they attempt
to reduce the whole object to a single truth value and raise
`ValueError: The truth value of a Series is ambiguous`. Use the bitwise
operators, which for `bool` Series are element-wise logical operators:

| Intent | Operator |
|---|---|
| both | `&` |
| either | `|` |
| not | `~` |

Every comparison must be parenthesised, because `&` binds *tighter* than
comparison in Python's grammar:

```python
ok  = df[(df["mw"] > 2.0) & (df["depth_km"] < 30.0)]
bad = df[df["mw"] > 2.0 & df["depth_km"] < 30.0]
```

The second form is not a subtle wrong answer; it is a `TypeError`, because it
parses as `2.0 & df["depth_km"]` — a bitwise AND between a float and an array.
The demo reports the message verbatim:

```
TypeError: Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]
```

An error is the good outcome. It would be far worse if the expression had parsed
and quietly selected the wrong rows.

### 2.3 Readable alternatives

Three helpers express intent better than a hand-built mask:

- `df["depth_km"].between(10, 25)` — inclusive on both ends, one call.
- `df["region"].isin(["Northvale", "Westhold"])` — membership in a set; the list
  can be large and the check stays linear.
- `df.query("mw >= 3.5 and depth_km < 20 and region in @names")` — the mask with
  `and`/`or` available because the expression is parsed by pandas, not by
  Python. Variables from the enclosing scope are referenced with `@`.

`query` is a readability tool, not a different execution path: it builds the
same mask. Prefer it when the condition would otherwise be a wall of
parentheses, and prefer the explicit mask when you need to reuse the mask object
or combine it with something exotic.

## 3. `.loc` and `.iloc`

### 3.1 Labels versus positions

With the event identifier as the index:

- `df.iloc[0:3]` is the first three rows **by position**, and the stop is
  excluded — it behaves like a Python slice.
- `df.loc["S0002":"S0005"]` is the four rows whose labels lie between `S0002`
  and `S0005` **inclusive** — it behaves like a labelled range.

The asymmetry is deliberate. A positional range has a natural half-open
convention; a labelled range reads as "from here to there" and a reader expects
both ends. The practical consequence is that mistakes show up as an off-by-one
row count, which is easy to miss in a 400-row table. Print the index of the
result, not just its shape, when you are learning the distinction.

Both accept the same row-then-column structure: `df.loc[rows, cols]`,
`df.iloc[row_positions, col_positions]`. A slice `:` means "all" in either slot.

### 3.2 Selecting and assigning in one step

This is the pattern to memorise:

```python
df.loc[df["depth_km"] > 60.0, "agency"] = "SYN-REVIEW"
```

It reads left to right: in `df`, for the rows where depth exceeds 60 km, set the
column `agency`. Three properties make it correct:

1. **One step.** pandas resolves the target once and writes to the frame itself.
2. **Label-addressed rows and name-addressed column**, so a reordering of the
   frame cannot change what gets written.
3. **The mask is explicit.** Anyone reading the line can see the selection.

### 3.3 Scalars: `.at` and `.iat`

`df.at["S0003", "mw"]` and `df.iat[2, 3]` retrieve one value with almost no
overhead. `df.loc["S0003", "mw"]` works identically and is slower because the
general machinery handles the general case. Use `.at`/`.iat` inside a loop over
a few known keys; do not use a loop over all keys — that is the vectorisation
failure lesson [07](./07-performance-pandas.md) measures.

## 4. Assignment, and the chained-assignment trap

### 4.1 The trap

```python
df[df["depth_km"] > 60.0]["mag_type"] = "XX"
```

This looks like the correct pattern with two brackets instead of `loc`. It is
not. `df[mask]` returns a **new object**, and the `[...] = "XX"` writes into
*that* temporary, which is then discarded. Nothing warns you in poetry, and the
frame is unchanged.

Historically pandas emitted `SettingWithCopyWarning` here. Under pandas 3,
Copy-on-Write is always enabled — there is no longer an option to disable it —
so the intermediate is unambiguously a copy, and the assignment is unambiguously
lost. pandas 3 raises `ChainedAssignmentError`, which is a `Warning` subclass, so
by default the code runs, the warning is printed, and **the write is dropped**.

That last point is worth saying twice. It is not an exception that stops your
program. The demo captures the warning and prints it:

```
  warnings raised: ['ChainedAssignmentError']
  message begins : A value is being set on a copy of a DataFrame or Series through chained assignment.
  mag_type of that first deep event before : 'Mw'
  mag_type of that deep event after        : 'Mw'
  -> modified? False
```

`modified? False`. In a long script, one lost assignment in a cleaning step is
the difference between "cleaned" and "believed cleaned", and every downstream
number inherits the error.

### 4.2 Checking for it

Two habits:

- **Look at the warnings.** `-W error::Warning` on the command line, or
  `warnings.simplefilter("error")` in a script, turns the lost write into a
  crash you cannot ignore.
- **Verify the write.** After a cleaning step, assert that it happened:
  `assert (df.loc[mask, "agency"] == "SYN-REVIEW").all()`.

Both are cheap. The alternative is discovering the bug when a figure looks
slightly wrong, which is a much more expensive route.

### 4.3 Why pandas made this change

Copy-on-Write removes the ambiguity about *who owns a value*. Before it, the
behaviour of a mutating operation could depend on whether a previous operation
had produced a view or a copy — an implementation detail leaking into results.
Under CoW, mutations never propagate through an intermediate object, so the rule
is statable in one sentence: **assign to the frame you mean to change.**

## 5. Worked code: selecting events

From [`code/indexing_selection_demo.py`](./code/indexing_selection_demo.py),
working on the 400-event de-duplicated catalogue:

```python
df = sc.raw_catalog().drop_duplicates("event_id", keep="first")

shallow  = df["depth_km"] < 30.0
strong   = df["mw"] >= 3.0
both     = shallow & strong
either   = shallow | strong
not_shallow = ~shallow

deep = df["depth_km"] > 60.0
df.loc[deep, "agency"] = "SYN-REVIEW"
```

Measured on the synthetic catalogue:

| Selection | Rows |
|---|---|
| `depth_km < 30` | 275 |
| `mw >= 3.0` | 48 |
| both (`&`) | 36 |
| either (`\|`) | 287 |
| not shallow (`~`) | 125 |

The union is 287, the intersection is 36, and the complement of shallow is 125.
Check any of them against the arithmetic: 275 + 125 = 400 rows total, and
48 = 36 + 12, so the two conditions disagree on 12 events. Numbers like these
are the cheapest possible test that a mask means what you think.

Selecting on two variables at once — `mw >= 4.0` and `0 <= depth <= 70 km` —
leaves one event in the synthetic catalogue. That is not a bug; it is what the
generator's rate and magnitude distribution imply. When a selection returns very
few rows, the correct response is to check the marginal counts (how many events
are above M 4.0 at all?) before suspecting the expression.

Two further selection idioms are worth knowing because they replace a mask plus
a sort:

```python
df.nlargest(5, "mw")                 # top five by magnitude, mask built for you
df.nsmallest(3, "depth_km")          # the three deepest (careful: NaN sorts last)
df.loc[df["region"] == "Northvale", ["event_id", "mw", "depth_km"]]
```

`nlargest` keeps ties arbitrarily at the cutoff, so it is a preview, not a
definition of "the five largest"; for a reproducible top-N, sort explicitly with
`sort_values("mw", ascending=False, kind="stable")` and take a slice. The third
form shows the column selector as a list, which preserves the `DataFrame` type
and leaves room to add or remove columns without rewriting the expression.

## 6. Physical interpretation

Selection is the operation that turns a catalogue into a *question about
tectonics*. "Deep events" is a statement about where deformation is happening;
"events above M 4" is a statement about which events are large enough to be felt
or to matter for hazard. Every such question is a mask, and the mask is where
the science enters the code.

This is also why a selection must be *reported*, not just performed. A map of
events deeper than 60 km answers a different question from a map of all events,
and the difference — how many events the criterion excluded — belongs in the
caption. Pandas makes the criterion explicit; it does not make you report it.

The other physical point is about assignment. Annotating events (as
`SYN-REVIEW` above) is how a catalogue acquires reviewer flags, quality classes
and magnitude-type overrides. If the annotation silently fails to write, the
catalogue looks annotated and is not.

## 7. Assumptions and limits

- **A mask is positional in effect but aligned by index in construction.** A
  mask built from a *different* frame aligned to the same index will select rows
  you did not intend. Build masks from the frame you are selecting from.
- **`df[...]` with a mask returns a copy, not a view.** That is safe and, under
  CoW, never a performance concern worth worrying about at this scale.
- **`between` is inclusive at both ends.** `between(10, 25)` includes exactly
  10.0 and 25.0. For a half-open range use `>=` and `<`, and say so.
- **Floating-point equality is a trap in a mask.** `df["mw"] == 3.0` is exact
  here only because the generator rounds to 0.1. On measured magnitudes, use a
  tolerance or a binned key (lesson [06](./06-earthquake-catalog-pandas.md)).
- **`query` cannot express everything.** Column names with spaces need
  backticks; complex objects need `@`; some expressions are simply clearer as
  masks. Readability is the criterion, not novelty.
- **`.loc` on a non-unique index returns several rows.** After a group-by index
  (lesson [04](./04-groupby-aggregation.md)), `.loc["Northvale"]` is a
  `DataFrame`, not a `Series`. The index is a key, not a primary key.

## 8. Python demonstration

```
.venv/bin/python 03-scientific-computing/04-pandas/code/indexing_selection_demo.py
```

**The precedence trap, reported verbatim:**

```
    correct : df[(df['mw'] > 2.0) & (df['depth_km'] < 30.0)]
    wrong   : df[df['mw'] > 2.0 & df['depth_km'] < 30.0]
              -> TypeError: Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]
```

**Label versus position:**

```
  .iloc[0:3]  -> first three ROWS by position (stop is exclusive):
    labels ['S0001', 'S0002', 'S0003']
  .loc['S0002':'S0005'] -> rows by LABEL (stop is INCLUSIVE):
    labels ['S0002', 'S0003', 'S0004', 'S0005']
```

Three positions give three rows; four labels give four rows. Same table, same
question, different counting rule.

**Scalar access.** `df.loc['S0003', 'mw']` returns `-1.0` — the injected error
code — while `df.iloc[2]['depth_km']` returns `47.44` and `df.iat[2, 3]` returns
the same `47.44`, because column position 3 is `depth_km`. The label form is
self-documenting; the positional form requires you to remember the column order.

**Single-step assignment:**

```
  events deeper than 60 km: 10
  after df.loc[deep, 'agency'] = 'SYN-REVIEW':
agency
SYN-REVIEW    10
```

Ten rows matched, ten rows changed. That equality is the check to perform every
time.

**The chained form:**

```
  warnings raised: ['ChainedAssignmentError']
  -> modified? False
...
  first five mag_type values now:
mag_type
Mw           309
mb            81
Mw-review     10
```

The chained form modified nothing; the one-step `.loc` form changed exactly the
10 deep events. Note also that the one-step form raised no warning at all — the
absence of a warning is the signal that the write happened.

## 9. Common mistakes

1. **`and`/`or`/`not` on Series.** `ValueError: The truth value of a Series is
   ambiguous`. Use `&`, `|`, `~`.
2. **Missing parentheses around comparisons.** A `TypeError` if you are lucky.
3. **Chained assignment.** `df[mask]["col"] = x` writes to a temporary. Use one
   `.loc`. Under pandas 3 the loss is reported as `ChainedAssignmentError`, but
   the program keeps running.
4. **Assuming `.loc` is positional.** With an integer index, `.loc[0:5]` is five
   labels inclusive and `.iloc[0:5]` is five positions exclusive — coincidentally
   similar here and wildly different when the index is not `0..n`.
5. **Assuming a mask has the frame's length when it came from elsewhere.**
   Alignment will silently reorder or introduce `NaN`, and `NaN > 0` is `False`,
   so rows quietly disappear from the selection.
6. **Selecting with `==` on floats.** Exact equality on measured values.
7. **Forgetting that `.loc[mask]` with no column selector returns *all*
   columns.** That is usually what you want; if you then sum the frame, you sum
   text columns too.
8. **Immutable chained edits in a notebook.** Re-running a cell that depends on
   an edit which was silently dropped gives a *different* result each run,
   because the cell above re-created the frame. Restart-and-run-all is the only
   reliable detector.

## 10. Real-world applications

- **Hazard screening.** "Events within 100 km of the site and above M 4.5" is a
  boolean mask on a catalogue; the count it returns is the input to a
  probabilistic hazard calculation, so the parentheses matter.
- **Quality control.** Flagging events with too few stations, large residuals or
  no depth solution is a mask plus a single-step assignment — the exact pattern
  in Section 3.2.
- **Subsetting for inversion.** A receiver-function or tomography workflow
  selects a station, a time window and a magnitude band; those selections are
  masks, and the same mask must select the waveform metadata and the arrivals.
- **Regional statistics.** Depth and magnitude thresholds define "crustal" and
  "subduction" events in every seismicity study, and the two selections must be
  made with the same code, not by two hand-written loops.

## 11. Further reading

- The pandas user guide sections *Indexing and selecting data* and *Copy-on-Write
  (CoW)* — the authoritative statement of the alignment and warning semantics
  used in Sections 3 and 4.
- The pandas release notes introducing Copy-on-Write: they contain the
  before/after table for chained assignment that Section 4 summarises.
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) — where the
  magnitude and depth thresholds used in real screening are defined.

## 12. Related lessons

- Previous: [01 Series, DataFrame and the Labeled-Data Model](./01-series-dataframe.md).
- Next: [03 Cleaning: Missing Values, Duplicates and Outliers](./03-cleaning-data.md)
  — masks applied to defects.
- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](../01-python-fundamentals/03-control-flow.md)
  — the loop that a mask replaces.
- [03-02-02 Indexing, Slicing, Views vs Copies and Fancy Indexing](../02-numpy/02-indexing-slicing.md)
  — the array-level view/copy distinction that CoW makes moot in pandas.

## Exercises

[`exercises/02-indexing-selection-exercises.md`](./exercises/02-indexing-selection-exercises.md),
with full worked answers in
[`exercises/02-indexing-selection-solutions.md`](./exercises/02-indexing-selection-solutions.md).

## Self-assessment checklist

- [ ] I can build a mask, count its `True`s, and combine it with another mask.
- [ ] I write every comparison inside parentheses, always.
- [ ] I can give the label and the position form of the same row selection.
- [ ] I know which slicing is inclusive and which is not.
- [ ] I can state what a chained assignment does under pandas 3 in one sentence.
- [ ] I know that `SettingWithCopyWarning` no longer exists in pandas 3 and what
      replaced it.
- [ ] I can name two habits that catch a dropped write.
- [ ] I know `.at`/`.iat` exist for scalars and that a loop over all rows is
      still a mistake.
