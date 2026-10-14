# Exercises — 03-04-02 Indexing, Selection, loc/iloc and Boolean Masks

Attempt these **closed-book** before opening the
[solutions](./02-indexing-selection-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/indexing_selection_demo.py`](../code/indexing_selection_demo.py); report
its **actual** output. The catalogue is **SYNTHETIC**
([`../code/synthetic_catalog.py`](../code/synthetic_catalog.py)) and is not the
USGS catalogue.

Where a problem asks for a count, give the count *and* the expression that
produced it.

---

## ★ Foundational

**★1.** For

```python
df = pd.DataFrame({"event_id": list("ABCDE"),
                   "mw": [2.2, 3.4, 2.9, 4.1, 3.0],
                   "depth_km": [5.0, 12.0, 8.0, 60.0, 25.0]})
```

compute the number of rows selected by each:

(a) `df["mw"] >= 3.0`
(b) `df["depth_km"] >= 10.0`
(c) the intersection of (a) and (b)
(d) the complement of (a)

---

**★2.** With the index of the same frame set to `event_id`:

(a) What labels does `df.iloc[1:4]` return?
(b) What labels does `df.loc["B":"D"]` return?
(c) How many rows does each return, and why do the two counts differ from a
naive reading of the slice bounds?

---

**★3.** A colleague writes

```python
subset = df[df["mw"] > 2.5 & df["depth_km"] < 30.0]
```

(a) What exception is raised, and what is the expression actually parsed as?
(b) Rewrite the line correctly.
(c) State the general rule for combining comparisons in pandas.

---

**★4.** Using the synthetic catalogue (400 de-duplicated events), report the
number of rows satisfying each condition:

(a) `mw >= 3.0`
(b) `depth_km < 30`
(c) `mw >= 3.0 & depth_km < 30`
(d) `~ (depth_km < 30)`

---

## ★★ Applied

**★★5.** Run the demo, Section 4.

(a) What warning class is raised by the chained assignment?
(b) Report the value of the target cell before and after, and the printed
`-> modified?` line.
(c) State what the code would look like as a single-step assignment.
(d) The one-step form raised no warning. Explain why the absence of a warning is
itself the evidence that the write happened.

---

**★★6.** Run the demo, Section 3.

(a) How many events are deeper than 60 km?
(b) Report the agency counts before and after the assignment.
(c) Write the assertion that would fail loudly if the assignment had not
happened.

---

**★★7.** Write a single expression that selects events with magnitude at least
3.5 **and** depth below 20 km **and** region in `{"Northvale", "Southgate"}`, in
two forms: a boolean mask, and a `query` call.

(a) Give both expressions.
(b) Report the count from the demo's equivalent query.
(c) State one situation in which the mask form is preferable and one in which
`query` is preferable.

---

**★★8.** The demo, Section 5, reports `depth_km.between(10, 25)` = 143 and
`mw.between(3.5, 4.5)` = 16.

(a) State whether `between` is inclusive at each end.
(b) Write the equivalent mask that contains 10 and 25 but excludes values equal
to neither bound — i.e. reproduce `between(10, 25)` exactly.
(c) Rewrite it as a half-open interval `[10, 25)` and say how many rows you would
expect to lose relative to (b), given that depths are recorded to 0.01 km.

---

## ★★★ Research-oriented

**★★★9.** A cleaning pipeline performs four sequential edits:

```python
df[df["depth_km"] > 60.0]["agency"] = "DEEP"          # (i)
df.loc[df["mw"] > 4.0, "mag_type"] = "Mw"            # (ii)
df["n_stations"] = df["n_stations"].fillna(0)         # (iii)
df[df["depth_km"] < 0]["depth_km"] = np.nan           # (iv)
```

(a) Which of the four do not modify the frame, and why?
(b) For each failing line, give the repair.
(c) Design a two-line guard that would have caught all of them automatically at
the end of the pipeline.

---

**★★★10.** You are asked to assign a quality class to every event from three
binary criteria — `depth_known`, `mw_known`, `n_stations >= 4` — with the
priority: an event with no depth is `"depth-missing"`; otherwise an event with no
magnitude is `"mag-missing"`; otherwise an event with fewer than four stations is
`"sparse"`; otherwise `"ok"`.

(a) Write the sequence of single-step assignments that implements this priority.
(b) Explain why the *order* of the assignments encodes the priority, and what
would change if they were reordered.
(c) State the invariant you would assert at the end (what must the four class
counts sum to?).
(d) A colleague implements the same logic with `np.select` in one expression.
State one advantage and one disadvantage relative to the sequential form.
