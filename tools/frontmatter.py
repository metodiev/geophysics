"""Minimal, dependency-free YAML-frontmatter reader for curriculum lessons.

The repository deliberately supports only a small, well-defined subset of YAML
in lesson frontmatter so that the whole quality gate can run on a bare Python
installation with no third-party packages:

    ---
    id: 01-01-01
    title: "Number Systems and Precision"
    level: beginner
    prereqs: ["00-02-01", "01-01-01"]
    estimated_minutes: 90
    tags: [arithmetic, floating-point]
    datasets: []
    ---

Supported value forms
---------------------
* bare scalars            -> key: beginner
* quoted scalars          -> key: "Number Systems"
* integers                -> key: 90
* inline lists            -> key: [a, b, c]  /  key: []
* block lists            -> key:
                              - a
                              - b

Anything outside this subset raises FrontmatterError so that malformed metadata
fails loudly instead of being silently skipped.
"""

from __future__ import annotations

import re
from pathlib import Path

DELIMITER = "---"
_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$")

# Frontmatter keys every lesson must define, and the keys that may be absent.
REQUIRED_KEYS = ("id", "title", "level", "prereqs", "tags")
OPTIONAL_KEYS = ("estimated_minutes", "datasets", "status", "see_also")

VALID_LEVELS = (
    "beginner",
    "intermediate",
    "advanced",
    "graduate",
    "doctoral",
    "research",
)


class FrontmatterError(ValueError):
    """Raised when frontmatter is absent or does not match the supported subset."""


def _coerce_scalar(raw: str) -> object:
    text = raw.strip()
    if text == "":
        return ""
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if text in ("true", "false"):
        return text == "true"
    return text


def _split_inline_list(raw: str) -> list[object]:
    body = raw.strip()[1:-1].strip()
    if not body:
        return []
    return [_coerce_scalar(part) for part in body.split(",") if part.strip()]


def parse_frontmatter(text: str) -> tuple[dict[str, object], int]:
    """Return (metadata, body_start_line_index) for a lesson's raw text.

    ``body_start_line_index`` is the 0-based index of the first line after the
    closing delimiter, so callers can report accurate line numbers.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != DELIMITER:
        raise FrontmatterError("file does not begin with a '---' frontmatter delimiter")

    closing = None
    for index in range(1, len(lines)):
        if lines[index].strip() == DELIMITER:
            closing = index
            break
    if closing is None:
        raise FrontmatterError("frontmatter block is never closed with '---'")

    meta: dict[str, object] = {}
    pending_key: str | None = None
    for offset, line in enumerate(lines[1:closing], start=1):
        if not line.strip():
            continue
        stripped = line.strip()
        if pending_key is not None and stripped.startswith("- "):
            meta[pending_key].append(_coerce_scalar(stripped[2:]))  # type: ignore[union-attr]
            continue
        pending_key = None
        match = _KEY_RE.match(line)
        if not match:
            raise FrontmatterError(f"line {offset + 1}: not a 'key: value' pair -> {line!r}")
        key, raw = match.group(1), match.group(2)
        if key in meta:
            raise FrontmatterError(f"line {offset + 1}: duplicate key {key!r}")
        if raw.strip() == "":
            meta[key] = []
            pending_key = key
        elif raw.strip().startswith("[") and raw.strip().endswith("]"):
            meta[key] = _split_inline_list(raw)
        else:
            meta[key] = _coerce_scalar(raw)

    for key in REQUIRED_KEYS:
        if key not in meta:
            raise FrontmatterError(f"missing required frontmatter key {key!r}")
    for key in meta:
        if key not in REQUIRED_KEYS and key not in OPTIONAL_KEYS:
            raise FrontmatterError(f"unknown frontmatter key {key!r}")
    return meta, closing + 1


def read_lesson(path: Path) -> dict[str, object]:
    """Parse a lesson file, annotating the metadata with its path."""
    meta, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
    meta["_path"] = path
    return meta
