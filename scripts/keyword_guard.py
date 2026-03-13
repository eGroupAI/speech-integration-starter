"""Fail CI when forbidden terms appear in repository files."""

from __future__ import annotations

import re
from pathlib import Path


def _word(code_points: list[int]) -> str:
    return "".join(chr(code) for code in code_points)


_token_01 = _word([111, 115, 115])
_token_02 = _word([100, 117, 99, 107, 100, 98])
_token_03 = _word([109, 105, 108, 118, 117, 115])
_token_04 = _word([115, 101, 110, 99, 118, 111, 105, 99, 99, 101])
_token_05 = _word([110, 101, 111, 52, 106])
_token_06 = _word([97, 105])
_token_07 = _word([115, 97, 110, 100, 98, 111, 120])

FORBIDDEN_PATTERNS = [
    re.compile(rf"\b{re.escape(_token_01)}\b", re.IGNORECASE),
    re.compile(re.escape(_token_02), re.IGNORECASE),
    re.compile(re.escape(_token_03), re.IGNORECASE),
    re.compile(re.escape(_token_04), re.IGNORECASE),
    re.compile(re.escape(_token_05), re.IGNORECASE),
    re.compile(rf"{re.escape(_token_06)}[-_ ]?{re.escape(_token_07)}", re.IGNORECASE),
]

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".toml",
    ".yml",
    ".yaml",
    ".txt",
    ".svg",
}

SKIP_DIR_NAMES = {".git", ".venv", "__pycache__", "build", "dist", "out"}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.name == "keyword_guard.py":
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    violations: list[str] = []

    for file in iter_files(root):
        try:
            lines = file.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(lines, start=1):
            for pattern in FORBIDDEN_PATTERNS:
                if pattern.search(line):
                    violations.append(
                        f"{file.relative_to(root)}:{line_no}: forbidden term `{pattern.pattern}`"
                    )

    if violations:
        print("[keyword_guard] Forbidden terms detected:")
        for item in violations:
            print(f"  - {item}")
        return 1

    print("[keyword_guard] OK: no forbidden terms found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
