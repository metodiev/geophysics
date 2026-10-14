# Solutions — 24-06-02 Persistent Identifiers

> Read after attempting. Numbers computed. Lesson:
> [02 Persistent Identifiers](../02-persistent-identifiers.md).

---

## ★1 — Check character by hand

Digits: $0,0,0,0,0,0,0,2,1,8,2,5,0,0,9$. Apply
$\text{total} \leftarrow (\text{total} + d) \times 2 \bmod 11$:

| step | digit | total before | total after |
|---|---|---|---|
| 1 | $0$ | $0$ | $0$ |
| 2 | $0$ | $0$ | $0$ |
| 3 | $0$ | $0$ | $0$ |
| 4 | $0$ | $0$ | $0$ |
| 5 | $0$ | $0$ | $0$ |
| 6 | $0$ | $0$ | $0$ |
| 7 | $0$ | $0$ | $0$ |
| 8 | $2$ | $0$ | $4$ |
| 9 | $1$ | $4$ | $10$ |
| 10 | $8$ | $10$ | $36 \bmod 11 = 3$ |
| 11 | $2$ | $3$ | $10$ |
| 12 | $5$ | $10$ | $30 \bmod 11 = 8$ |
| 13 | $0$ | $8$ | $16 \bmod 11 = 5$ |
| 14 | $0$ | $5$ | $10$ |
| 15 | $9$ | $10$ | $38 \bmod 11 = 5$ |

$$c = (12 - 5) \bmod 11 = 7 \;\Rightarrow\; \text{check} = 7 .$$

The full identifier is `0000000218250097`, formatted as `0000-0002-1825-0097` — which
is the form the demonstration's algorithm reproduces.

---

## ★2 — DOI versus URL

A DOI is a **name**: a string registered with a resolution system, whose meaning is the
work it identifies. The resolver form of an identifier — the name carried by a
resolution service — is a **convenience location** for that name. The distinction
matters because URLs move, and a reference list containing a raw publisher URL is a
reference list that will decay, while a DOI will keep resolving as long as the
registrar's mapping is maintained.

In a reference list, record the DOI (and the version, where the venue distinguishes
versions) in the venue's format; record the resolver URL only if the venue's style
requires a link. Either way, the identifier, not the location, is the citation.

---

## ★3 — Structural validity

| String | Valid? | Reason |
|---|---|---|
| `10.1000/abc` | yes | prefix has $4$ digits, suffix non-empty, no whitespace |
| `10.12/abc` | no | prefix has $2$ digits; the rule needs $4$–$9$ |
| `10.1234567/` | no | empty suffix |
| `10.5555/data set 12` | no | whitespace in the suffix |

Two of four are invalid, and the validator can state why for each. That is exactly what
a structural check is for.

---

## ★4 — Flagging rates at scale

| Error rate | Errors in $10^{6}$ | Flagged with a check character | Flagged without |
|---|---|---|---|
| $1$ per $1000$ | $1000$ | $1000$ | $0$ |
| $1$ per $10^{4}$ | $100$ | $100$ | $0$ |
| $1$ per $10^{5}$ | $10$ | $10$ | $0$ |

The scheme's detection is not probabilistic for these error classes: every single-digit
substitution is caught in the demonstration ($1200$ of $1200$), so the flagged count is
the number of errors. Without redundancy nothing is flagged and every mistyped
identifier is a legal string — which is why a reference manager that validates check
characters catches typos that a plain text field cannot.

---

## ★5 — Equal adjacent digits

For a uniform random digit in $0$–$9$ and an independent second digit, the probability
they are equal is $1/10 = 0.10$. So about $10\%$ of adjacent pairs are equal, and
transposing such a pair produces an identical string: there is nothing to detect.

If those cases are counted as failures, the measured detection rate for transpositions
falls to about

$$1 - 0.10 = 90\%,$$

and the demonstration's $77.6\%$ before the correction reflected a mixture of equal-digit
transpositions and the specific pairs chosen by its random draws. With the
equal-digit case excluded — as it should be, since the identifier did not change — the
detection rate is $100\%$, matching the design of the scheme.

---

## ★6 — Accepted by a structural validator

$$100\% - 66.3\% = 33.7\%\ \text{accepted}.$$

In a corpus of $300$ strings that is $101$ accepted strings, matching the
demonstration. Among those accepted:

- **Strings that do not exist.** A well-formed prefix and suffix is easy to invent; a
  validator cannot check registration.
- **Strings that exist and point at something else.** A plausible-looking identifier
  may resolve to a different work, which is the failure mode that structural checking
  cannot address and that citation practice must.

So the accepted set is a set of *candidates*, not of valid citations. The useful
asymmetry is the other direction: a structurally invalid string is certainly wrong,
which is why offline validation belongs in a reference manager even though it cannot
certify anything.

---

## ★7 — Unresolved identifiers in reference lists

**Corpus.** Reference lists of research articles in a stated set of journals and a
stated window, restricted to references that carry an identifier. Report the flow from
articles to identifiers, since the fraction that carry identifiers is itself a result.

**Sampling.** Random sample of articles, then all identifiers within each — a two-stage
design that keeps the cost bounded and allows clustering by article to be accounted
for, since reference lists within one article share an author's habits.

**Resolution protocol.** Resolve each identifier through the registrar's resolution
service with rate limiting and retries; record the HTTP status, the final landing page
and whether the landing page's title matches the cited title. Define outcomes as:
resolved-and-matches, resolved-and-differs, does-not-resolve, and rate-limited or
inconclusive.

**Outcome definitions.** Distinguish the two failures explicitly: a dead link is a
persistence failure of the publisher, while a resolved identifier that points at a
different work is a citation error by the author. Conflating them produces a rate with
no actionable meaning.

**Why the failure rate is a lower bound.** Resolution depends on the resolver and on
transient network conditions; a failure in your run may succeed tomorrow, and some
identifiers are registered with services your resolver does not reach. Report the
protocol, the retry policy and the inconclusive count, and present the measured rate
as a lower bound on identifier error with the sources of undercounting named.

---

## ★8 — Does a citation requirement change behaviour?

**Unit.** One published research article.

**Outcome.** Whether the article formally cites (in its reference list, with an
identifier) the software that was actually used to produce its analysis.

**Detecting software actually used without asking the authors.** Three complementary
sources: (a) archived code or notebooks deposited with the article, whose import lines
and `environment.yml` list the packages; (b) the data-availability and
code-availability statements; (c) for some journals, the reproducibility check report.
Where none exists, the article is unclassifiable for this outcome and must be excluded
with the exclusion count reported, because assuming "no archive means no software" would
manufacture the treatment effect.

**Design.** Difference-in-differences across journals: a journal that adds a software
citation requirement is a treatment; matched journals without one are controls. Compare
the change in the citation rate before and after the policy date, since the level
differs between journals for reasons unrelated to the policy.

**Threat to validity.** Policy dates coincide with other changes in the field's
norms — community campaigns for software citation, changes in reference managers'
defaults — so some of the observed increase would have happened anyway. The matched
control group is the mitigation, and the honest report includes the control group's
own trend as the counterfactual, stated explicitly.
