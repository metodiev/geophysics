---
id: 26-06-01
title: "OER: Mathematics, Physics and Computing"
level: beginner
prereqs: []
estimated_minutes: 20
tags: [reference, oer, mathematics, computing]
---

# OER: Mathematics, Physics and Computing

Free and openly licensed material for the mathematical and computational
foundations of geophysics: courses, open textbooks, lecture notes and
documentation. This page lists what is genuinely open, what is merely free to
read, and how the two differ.

## How to use this page

Each entry gives the resource, its access point where one is registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), the kind of licence
it typically carries, and what it is best used for. Where no access point is
given, the resource is named but not linked: it must be located through a search
or a library, because this repository cites no URL it has not checked.

**Three licence situations, which are not the same thing**

| Situation | Meaning | Reuse |
|---|---|---|
| Openly licensed | A licence (Creative Commons, OGL, MIT, BSD, Apache) grants defined reuse rights | Reuse under the licence terms, with attribution as required |
| Free to read | Available at no cost, all rights reserved | Read and cite; do not redistribute or adapt |
| Public domain | No copyright (or a CC0 dedication) | Reuse freely; attribution is still good practice and may be required by the source's terms |

*Provenance of this page:* a directory of external resources. No external content
is reproduced; all reuse questions are referred to
[26-06-04 Data Licensing, Attribution and Reuse Policy](./04-data-policy-and-licences.md).

## Mathematics

| Resource | Access point | Typical licence | Best for |
|---|---|---|---|
| MIT OpenCourseWare | [ocw.mit.edu](https://ocw.mit.edu) | Mixed: mostly CC BY-NC-SA, per-course terms must be checked | Lecture notes and problem sets for single-variable and multivariable calculus, linear algebra and differential equations. Check the licence stated on the individual course |
| NSF-funded open textbooks and the Open Textbook Library | not linked here — locate via a search | Usually CC BY or CC BY-SA | Complete, citable textbooks for calculus and linear algebra |
| Paul's Online Math Notes | not linked here | Free to read | Worked examples and quick revision; not for redistribution |
| Scipy Lecture Notes | [scipy-lectures.org](https://scipy-lectures.org) | Open (reuse terms stated on the site) | A practical, worked introduction to scientific computing that complements numerical-analysis courses |

## Physics and continuum mechanics

| Resource | Access point | Typical licence | Best for |
|---|---|---|---|
| MIT OpenCourseWare physics courses | [ocw.mit.edu](https://ocw.mit.edu) | Per-course | Classical mechanics, electromagnetism, waves and thermal physics at lecture-note depth |
| National Academies Press | [nap.edu](https://www.nap.edu) | Free to read; many reports also downloadable | Authoritative consensus reports on Earth science and on physics education |
| OpenStax and similar open textbooks | not linked here | CC BY | Introductory physics with exercises and figures licensed for reuse |
| arXiv preprints on continuum mechanics and geophysics | not linked here | Author-dependent (many CC BY) | Current research; **not peer reviewed**, and must be labelled as such when cited |

## Computing and programming

| Resource | Access point | Typical licence | Best for |
|---|---|---|---|
| The Python language documentation and tutorial | [docs.python.org](https://docs.python.org) | Open (PSF licence) | The language reference and the standard library |
| The Python tutorial | [Python tutorial](https://docs.python.org/3/tutorial/) | Open (PSF licence) | A first pass through the language |
| Virtual environments | [venv documentation](https://docs.python.org/3/library/venv.html), [venv tutorial](https://docs.python.org/3/tutorial/venv.html) | Open (PSF licence) | The environment discipline this repository uses |
| NumPy | [numpy.org](https://numpy.org) | BSD-3-Clause | Arrays, indexing, broadcasting, FFT |
| SciPy | [scipy.org](https://scipy.org), [SciPy reference](https://docs.scipy.org/doc/scipy/) | BSD-3-Clause | Optimisation, signal processing, statistics, special functions |
| SciPy lecture notes | [scipy-lectures.org](https://scipy-lectures.org) | Open | A guided tour from Python basics to scientific workflows |
| Jupyter | [jupyter.org](https://jupyter.org) | BSD-3-Clause | Notebooks for teaching, exploration and reproducible reports |
| pandas | not linked here — see the data-engineering folder | BSD-3-Clause | Tabular data handling |
| Matplotlib and Cartopy | [cartopy.readthedocs.io](https://cartopy.readthedocs.io) | Matplotlib: BSD-style; Cartopy: LGPL-3 | Plotting and map projections |
| Git and GitHub Actions documentation | [GitHub Actions](https://docs.github.com/en/actions) | Documentation; the tools themselves are open | Version control and automated validation of notebooks and lessons |
| pytest | [pytest documentation](https://docs.pytest.org/en/stable/) | MIT | Testing numerical code, with `approx` for floating-point comparisons |

## How to use these resources with this curriculum

| If you need… | Use |
|---|---|
| A second explanation of eigenvalues or SVD | OCW linear algebra plus [Formula Sheet: Linear Algebra, SVD and Numerics](../03-formula-handbook/02-formulas-linear-algebra-numerics.md) |
| Practice writing Python that computes physics | Scipy lecture notes, then the demo scripts in this repository |
| Proof that your code is reproducible from a clean checkout | the environment and testing lessons in [03-scientific-computing](../../03-scientific-computing/README.md) |
| A defensible citation for a method | the peer-reviewed literature in [module 26-04](../04-textbook-bibliography/README.md), not a course page |

## Caveats

- **Course pages move.** Institutions reorganise their sites; this page links
  only to the stable root of each provider, never to a deep course URL.
- **Licences differ per item.** "MIT OpenCourseWare" is not a single licence;
  each course states its own terms.
- **Free is not open.** Several widely used notes and tutorials are free to read
  but retain all rights. Reading them is fine; redistributing them is not.
- **Preprints are not peer reviewed.** Cite them as preprints, with the version
  and the date, and say so.
- **Documentation is not a textbook.** API documentation tells you what a
  function does; it does not tell you whether the method is appropriate.

## Related pages

- [OER: Geophysics, Seismology and Earth Science Courses](./02-oer-geophysics.md)
- [Software Directory: Open-Source Geophysics Tools](./03-software-directory.md)
- [Data Licensing, Attribution and Reuse Policy](./04-data-policy-and-licences.md)
- [01-mathematics folder overview](../../01-mathematics/README.md)
- [03-scientific-computing folder overview](../../03-scientific-computing/README.md)
