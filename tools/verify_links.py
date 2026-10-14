"""Verify external links and keep ``tools/verified_links.tsv`` honest.

Two jobs:

1. ``--audit-markdown`` (default): extract every external URL cited in the
   repository's Markdown and confirm each one appears in
   ``tools/verified_links.tsv``. This is the important check -- it makes it
   impossible to cite a dataset or resource that was never verified.

2. ``--check``: re-request every URL in the TSV and report status changes, so
   link rot is detected explicitly rather than discovered by a learner.

Network access is required for ``--check``; ``--audit-markdown`` works offline.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TSV = Path(__file__).resolve().parent / "verified_links.tsv"
SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "site-packages",
    # Keep this set identical to tools/check_all.py: tool caches are generated
    # artefacts, not repository content. pytest writes a .pytest_cache/README.md
    # containing docs.pytest.org, which is not a link this repository cites.
    ".pytest_cache", ".mypy_cache", ".ruff_cache", ".ipynb_checkpoints",
    "build", "dist",
}

URL_RE = re.compile(r"https?://[^\s\)\]\"'<>]+")

# Loopback and other non-routable addresses. These cannot be external resources,
# so requiring them in a registry of verified *external* links is meaningless.
# Lessons on offline testing legitimately show a deliberately dead endpoint such
# as http://127.0.0.1:9/fdsnws/ to demonstrate how a client fails.
NON_ROUTABLE_RE = re.compile(
    r"^https?://(?:localhost|127\.|0\.0\.0\.0|\[::1\]"
    r"|10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.|169\.254\.)",
    re.IGNORECASE,
)


def load_registry() -> dict[str, tuple[str, str]]:
    """Return {url: (status, note)} from the TSV."""
    registry: dict[str, tuple[str, str]] = {}
    for line in TSV.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        status, _date, url = parts[0], parts[1], parts[2]
        note = parts[3] if len(parts) > 3 else ""
        registry[url] = (status, note)
    return registry


def iter_markdown() -> list[Path]:
    return [
        path for path in sorted(REPO_ROOT.rglob("*.md"))
        if not any(part in SKIP_DIRS for part in path.parts)
    ]


def audit_markdown() -> int:
    registry = load_registry()
    unregistered: dict[str, set[str]] = {}
    for path in iter_markdown():
        rel = path.relative_to(REPO_ROOT).as_posix()
        for url in URL_RE.findall(path.read_text(encoding="utf-8")):
            url = url.rstrip(".,;:`")
            if NON_ROUTABLE_RE.match(url):
                continue  # cannot be an external resource; nothing to verify
            if url not in registry:
                unregistered.setdefault(url, set()).add(rel)

    if not unregistered:
        print(f"All cited external URLs are registered in {TSV.name}. OK")
        return 0

    print(f"{len(unregistered)} external URL(s) cited but NOT verified in {TSV.name}:\n")
    for url, files in sorted(unregistered.items()):
        print(f"  {url}")
        for name in sorted(files):
            print(f"      cited in {name}")
    print("\nAdd each URL to tools/verified_links.tsv with an observed status,")
    print("after confirming it in a browser. Never cite an unverified link.")
    return 1


def _fetch(url: str, timeout: int = 25) -> int:
    """Return the HTTP status for url, or 0 on any transport failure."""
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def check_urls() -> int:
    registry = load_registry()
    target_status = {200, 301, 302}
    # Reachable, but refusing automated clients. 403 is documented bot
    # protection; 406 and 429 show up the same way when a checker walks a
    # large registry quickly, and a retry distinguishes a real block from
    # transient rate limiting.
    bot_block_codes = {403, 406, 429}
    # Reachable, and the service is correctly rejecting a bare request because it
    # requires query parameters. FDSN endpoints such as dataselect/query return
    # this for an unparameterised GET, so it is a pass rather than link rot.
    needs_params_codes = {422}
    acceptable = target_status | bot_block_codes | needs_params_codes
    changes = 0
    for url, (status, _note) in sorted(registry.items()):
        if status in {"404", "000"}:
            # Recorded as unusable, deliberately, so they are documented as
            # "do not cite" rather than re-reported as a status change on every
            # run. Re-checking them would also re-request known-dead endpoints.
            continue
        observed = _fetch(url)
        if observed in bot_block_codes:
            time.sleep(1.5)
            retry = _fetch(url)
            if retry in target_status:
                observed = retry  # transient rate limit; the link itself is fine
        flag = ""
        if observed not in acceptable:
            flag = "  <-- CHANGED"
            changes += 1
        print(f"{observed:>3}  (was {status:>3})  {url}{flag}")

    if changes:
        print(f"\n{changes} link(s) changed status. Update tools/verified_links.tsv.")
        return 1
    print("\nNo unexpected link status changes.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="re-request every registered URL")
    mode.add_argument("--audit-markdown", action="store_true",
                      help="confirm every cited URL is registered (default)")
    args = parser.parse_args(argv)
    if args.check:
        return check_urls()
    return audit_markdown()


if __name__ == "__main__":
    raise SystemExit(main())
