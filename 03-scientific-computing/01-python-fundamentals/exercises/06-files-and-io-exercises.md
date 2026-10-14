# Exercises — 03-01-06 Files, Text I/O and Data Encodings

Attempt these **closed-book** before opening the
[solutions](./06-files-and-io-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/files_io_demo.py`](../code/files_io_demo.py) require you to run it and
report its **actual** output. Write all scratch files beside your script, never in
a shared temporary directory, and delete them when you are done.

---

## ★ Foundational

**★1.** For each action, state the exact bytes written, or the exception raised.

(a) `"Zürich".encode("utf-8")`
(b) `"Zürich".encode("ascii")`
(c) `"Zürich".encode("latin-1")`
(d) `"Zürich".encode("utf-8").decode("latin-1")`
(e) `"Zürich".encode("latin-1").decode("utf-8")`

---

**★2.** A file contains the three bytes `ef bb bf` followed by the ASCII text
`Station`.

(a) Which codec wrote that file?
(b) What does `open(path, encoding="utf-8").read()` return, precisely?
(c) What does `open(path, encoding="utf-8-sig").read()` return?
(d) State the failure this causes in a parser that compares the first field with
`== "Station"`.

---

**★3.** State the line terminators produced by each, and which one you would use
for a CSV file.

(a) `open(p, "w").write("a\nb\n")` on Windows in text mode with the default
translation.
(b) `open(p, "w", newline="").write("a\r\nb\r\n")`.
(c) `open(p, "w", newline="").write("a\nb\n")`.
(d) Reading (a) with `newline=""` versus with the default.

---

## ★★ Applied

**★★4.** Run `python3 files_io_demo.py` and report:

(a) the byte size of the synthetic catalogue and its first four lines;
(b) the row count from `csv.reader` and the record count from `csv.DictReader`,
and the reason they differ by two;
(c) the magnitude range, the mean and maximum depth, and the number of distinct
places;
(d) the encoding table (byte counts for `utf-8`, `utf-8-sig`, `latin-1`) and which
codec failed.

---

**★★5.** Diagnose each mojibake string: name the codec used to *write* and the
codec used to *read*, and say how you know.

(a) `ZÃ¼rich`
(b) `itâ€™s`
(c) `SeismologÃ\xada` (note the control character)
(d) A field that reads `Station-01` correctly in a file that also contains
`ZÃ¼rich` — what does that tell you about the file?

---

**★★6.** Write a round-trip test.

(a) Write a 3-record CSV whose fields include `Zürich`, a comma inside a quoted
field, and a longitude of `8.5417`. Use `newline=""` and `encoding="utf-8"`.
(b) Read it back with `csv.DictReader` after skipping `#` comment lines.
(c) Assert that every field round-trips exactly, including the comma.
(d) Print the file's raw bytes for the quoted field and state why the quotes are
present.

---

## ★★★ Research-oriented

**★★★7.** Write a robust reader for a delimited file that must detect, and report
on, four defects:

1. a truncated final line (no trailing newline on a record that has fewer fields);
2. a wrong encoding (decoding the whole file as UTF-8 raises);
3. a row with the wrong number of fields;
4. a header that is missing an expected column.

(a) Implement it, with a `Report` object carrying counts of accepted and rejected
rows and one line of explanation per defect class.
(b) For each defect, state whether a correct program should **raise**, **skip and
count**, or **repair** — and justify the choice in terms of the physics.
(c) Show the report for a file you construct with all four defects present.

---

**★★★8.** A legacy archive has ten thousand files. Half are UTF-8, some carry a
BOM, some are Windows-1252, and a few have one truncation. Design a *detection*
procedure that does not modify any file, and explain:

(a) why a byte-order-mark check is the cheapest first test;
(b) why a UTF-8 decode failure is a *conclusive* result but a success is not;
(c) how you would adjudicate a file that decodes as both UTF-8 and Windows-1252;
(d) what you would record in a manifest so that the classification is reproducible
without re-scanning the archive.
