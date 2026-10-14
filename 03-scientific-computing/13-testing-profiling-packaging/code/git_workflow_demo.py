"""Git as a reproducibility instrument, measured with read-only commands.

Run:  python git_workflow_demo.py
Requires: git on PATH; standard library only

Every command below is read-only. Nothing is committed, staged, checked out,
stashed or written: the script inspects the repository it is run from and
prints what it finds. That is deliberate -- a lesson about history hygiene
should not rewrite anybody's history.

The five questions answered here are the ones a reviewer actually asks:

1. What exactly is in the repository? (``git ls-files``, sizes, extensions)
2. What is deliberately NOT in it, and which rule says so? (``git check-ignore``)
3. Is the repository's identity its content or its filenames? (``git hash-object``)
4. What would a fresh clone contain? (``git archive``, compared with ``ls-files``)
5. What is currently uncommitted, and what would a gate do about it?
"""

from __future__ import annotations

import collections
import hashlib
import io
import pathlib
import subprocess
import tarfile

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]

BINARY_SUFFIXES = {
    ".nc", ".tif", ".tiff", ".mseed", ".sac", ".segy", ".sgy", ".h5", ".hdf5",
    ".grd", ".zarr", ".npy", ".npz", ".pkl", ".zip", ".tar", ".gz", ".pdf",
    ".png", ".jpg", ".jpeg", ".dat", ".bin", ".so", ".dylib", ".dll",
}


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def _run(args: list[str], text: bool = True, stdin: str | None = None):
    return subprocess.run(
        ["git", "--no-pager", *args], cwd=REPO_ROOT, input=stdin,
        capture_output=True, text=text, check=False,
    )


def git(*args: str) -> str:
    """Run a git command in the repository and return stdout as text."""
    result = _run(list(args))
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


# --------------------------------------------------------------------------
# 1. What is in the repository
# --------------------------------------------------------------------------

def demo_what_is_tracked() -> None:
    section("1. What is actually in the repository")
    files = [line for line in git("ls-files").splitlines() if line]
    sizes = []
    for rel in files:
        path = REPO_ROOT / rel
        if path.is_file():
            sizes.append((path.stat().st_size, rel))
    total = sum(size for size, _ in sizes)
    print(f"  tracked files      : {len(files)}")
    print(f"  tracked bytes      : {total:,} ({total / 1e6:.2f} MB)")
    print("  largest tracked:")
    for size, rel in sorted(sizes, reverse=True)[:5]:
        print(f"    {size:>9,} B  {rel}")

    extensions = collections.Counter(
        pathlib.Path(rel).suffix.lower() for rel in files if pathlib.Path(rel).suffix
    )
    print("  most common extensions: "
          + ", ".join(f"{ext} ({n})" for ext, n in extensions.most_common(6)))

    offenders = [rel for rel in files
                 if pathlib.Path(rel).suffix.lower() in BINARY_SUFFIXES]
    print(f"\n  tracked files with a large-binary extension: {len(offenders)}")
    for rel in offenders[:10]:
        print(f"    {rel}")
    if not offenders:
        print("    none -- the .gitignore rules are doing their job")

    text_files = text_lines = 0
    for _size, rel in sizes:
        try:
            content = (REPO_ROOT / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        text_files += 1
        text_lines += content.count("\n")
    print(f"\n  text files that decode as UTF-8: {text_files}")
    print(f"  total text lines               : {text_lines:,}")
    print("  Why it matters: git stores a complete copy of every version of a")
    print("  binary. A 200 MB seismic volume committed ten times is 2 GB of clone,")
    print("  forever, for every person and every CI runner. A 4 kB lesson revision")
    print("  is 4 kB. The ratio is not a preference; it is the arithmetic.")


# --------------------------------------------------------------------------
# 2. What is excluded, and by which rule
# --------------------------------------------------------------------------

def demo_gitignore() -> None:
    section("2. .gitignore: the exclusions, and the rule responsible for each")
    probes = [
        "data/station_gravity.csv",
        "waveforms/2019-07-06.mseed",
        "field/line_a.sac",
        "grids/bouguer.tif",
        "model/result.nc",
        "logs/run.log",
        "__pycache__/module.cpython-314.pyc",
        "examples/small-gravity.csv",
        "03-scientific-computing/13-testing-profiling-packaging/README.md",
        "README.md",
    ]
    for probe in probes:
        result = _run(["check-ignore", "-v", "--no-index", probe])
        out = result.stdout.strip()
        if not out:
            print(f"  committed  {probe:>52}  (no ignore rule matches)")
            continue
        source, line, pattern = out.split(":", 2)
        pattern = pattern.split("\t")[0]
        verdict = "re-included" if pattern.startswith("!") else "IGNORED   "
        print(f"  {verdict}  {probe:>52}  by {source}:{line} `{pattern}`")
    print("\n  Two things are being demonstrated. First, the rules are specific:")
    print("  `data/`, `*.mseed`, `*.sac`, `*.nc`, `*.tif` -- instrument formats and")
    print("  grids, which are large and belong in a DOI-bearing archive instead.")
    print("  Second, a negation can re-include one file inside an ignored")
    print("  directory: `!examples/**/small-*.csv` lets a 3 kB purpose-built")
    print("  fixture be committed while the 3 GB dataset it was cut from stays out.")
    print("  Note that `git check-ignore` exits 0 for a negation too, so the")
    print("  deciding evidence is the leading `!`, not the exit status -- a small")
    print("  detail that has caused real CI bugs.")


# --------------------------------------------------------------------------
# 3. Content addressing
# --------------------------------------------------------------------------

def demo_hash_object() -> None:
    section("3. The repository's identity is content, not filenames")

    def hash_stdin(text: str) -> str:
        return _run(["hash-object", "-t", "blob", "--stdin"], stdin=text).stdout.strip()

    content = "g = 6.67430e-11\n"
    a = hash_stdin(content)
    b = hash_stdin(content)
    c = hash_stdin(content + "\n")
    print(f"  hash('{content.strip()}' + newline)     = {a}")
    print(f"  hash(the very same string)          = {b}   equal: {a == b}")
    print(f"  hash(the same text, one more newline) = {c}   equal: {a == c}")
    print("\n  The hash is a function of the bytes. Renaming a file does not change")
    print("  it; changing one byte does. This is why a commit hash is a citation,")
    print("  why a DOI'd data release is identified by a checksum, and why 'the same")
    print("  analysis' is meaningless without the revision it ran on.")
    print(f"\n  HEAD            = {git('rev-parse', '--short', 'HEAD').strip()} "
          f"({git('rev-parse', 'HEAD').strip()})")
    print(f"  branch          = {git('rev-parse', '--abbrev-ref', 'HEAD').strip()}")
    print(f"  commits from HEAD = {git('rev-list', '--count', 'HEAD').strip()}")
    trailer = git("log", "-1", "--format=%(trailers:key=Co-authored-by)")
    print(f"  Co-authored-by trailer on HEAD: {trailer.strip() or '(none)'}")
    print("  A trailer is metadata git parses and displays; it is how authorship of")
    print("  a pair-programmed or agent-assisted commit is recorded honestly.")


# --------------------------------------------------------------------------
# 4. What a fresh clone contains
# --------------------------------------------------------------------------

def demo_archive_equals_tracked() -> None:
    section("4. A fresh clone is exactly the tracked files")
    tracked = sorted(line for line in git("ls-files").splitlines() if line)
    result = _run(["archive", "--format=tar", "HEAD"], text=False)
    if result.returncode != 0:
        print(f"  git archive failed: {result.stderr!r}")
        return
    archive_bytes = result.stdout
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as tar:
        members = sorted(m.name for m in tar.getmembers() if m.isfile())

    print(f"  files in `git ls-files`             : {len(tracked)}")
    print(f"  regular files in `git archive HEAD` : {len(members)}")
    print(f"  sets identical: {set(tracked) == set(members)}")
    missing = sorted(set(tracked) - set(members))
    extra = sorted(set(members) - set(tracked))
    if missing:
        print(f"    only in ls-files ({len(missing)}): {missing[:5]}")
    if extra:
        print(f"    only in archive  ({len(extra)}): {extra[:5]}")
    digest = hashlib.sha256(archive_bytes).hexdigest()
    print(f"  size of the whole committed tree as a tar: "
          f"{len(archive_bytes) / 1e6:.2f} MB")
    print(f"  sha256(git archive HEAD) = {digest[:40]}...")
    print("\n  `git archive` reproduces the committed tree straight out of the object")
    print("  database, so its content does not depend on the working directory, on")
    print("  untracked files, or on anything in .gitignore. That is what makes")
    print("  'verify the build at a clean checkout' a meaningful instruction: the")
    print("  archive IS the clean checkout, and its hash identifies it.")
    if missing:
        print("\n  The count differs here because `git ls-files` includes the staged")
        print("  additions of this working session, which are not yet in HEAD. A")
        print("  clean clone sees exactly the archive.")


# --------------------------------------------------------------------------
# 5. Working-tree state
# --------------------------------------------------------------------------

def demo_status() -> None:
    section("5. Working-tree state, and how a gate reads it")
    porcelain = [ln for ln in git("status", "--porcelain").splitlines() if ln]
    print(f"  entries in `git status --porcelain`: {len(porcelain)}")
    for line in porcelain[:14]:
        print(f"    {line}")
    if len(porcelain) > 14:
        print(f"    ... and {len(porcelain) - 14} more")

    staged = git("diff", "--cached", "--name-only").split()
    unstaged = git("diff", "--name-only").split()
    untracked = [ln[3:] for ln in porcelain if ln.startswith("??")]
    print(f"\n  staged changes   : {len(staged)}")
    print(f"  unstaged changes : {len(unstaged)}")
    print(f"  untracked paths  : {len(untracked)}")
    scratch = [p for p in untracked
               if pathlib.Path(p).suffix in {".tmp", ".out", ".orig", ".bak"}
               or pathlib.Path(p).name.startswith(".")]
    print(f"  untracked scratch-looking files: {len(scratch)} {scratch[:5]}")
    print("\n  A gate that demands 'only my module's files' is reading exactly this")
    print("  list. The practical rule: a file you cannot name in a commit message")
    print("  does not belong in the commit, and a file you would not want a reviewer")
    print("  to read does not belong in the working tree either.")

    print("\n  worktrees attached to this repository:")
    for line in git("worktree", "list", "--porcelain").splitlines():
        if line.startswith(("worktree ", "HEAD ", "branch ", "detached")):
            print(f"    {line}")
    print("  `git worktree add ../repo-v2 -b feature` creates a second working")
    print("  directory backed by the SAME object database, on a different branch,")
    print("  with no clone and nothing downloaded twice. It is the cheap way to run")
    print("  a long test against the previous revision while continuing to edit the")
    print("  current one. (This script does not create one; that would be a")
    print("  mutation, and a lesson must not have side effects.)")


def main() -> int:
    if not (REPO_ROOT / ".git").exists():
        print(f"Not a git repository: {REPO_ROOT}")
        return 1
    print(f"Repository: {REPO_ROOT}")
    demo_what_is_tracked()
    demo_gitignore()
    demo_hash_object()
    demo_archive_equals_tracked()
    demo_status()
    section("Summary")
    print("ls-files says what ships; check-ignore says what deliberately does not;")
    print("hash-object says identity is content; archive says a clone IS the")
    print("commit; status says what is not yet committed. Four commands, all")
    print("read-only, and together they answer 'can anyone reproduce this?'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
