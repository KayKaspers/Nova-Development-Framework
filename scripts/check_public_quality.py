#!/usr/bin/env python3
"""NDF Public Repository Quality Gate.

Checks that the public NDF repository stays neutral and clean:

1. Public neutrality: no denylisted terms in tracked text files.
   The denylist is intentionally NOT part of the repository. It is provided
   via the environment variable NDF_PUBLIC_NEUTRALITY_DENYLIST (comma-separated)
   and/or the untracked local file .ndf/public-neutrality-terms.local.txt.
2. Root hygiene: no package/import artifacts in the repository root.
3. History separation: import package artifacts belong to docs/import-history/.
4. README structure: README.md exists and contains required framework terms.

Uses only the Python standard library.

Usage:
    python scripts/check_public_quality.py
    python scripts/check_public_quality.py --strict
    python scripts/check_public_quality.py --self-test
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import subprocess
import sys
import tempfile
from pathlib import Path

TEXT_EXTENSIONS = {
    ".md", ".mdx", ".txt", ".yaml", ".yml", ".json", ".toml", ".ini", ".cfg",
}

IGNORED_DIRS = {
    ".git", ".venv", "venv", "node_modules", "dist", "build",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".ndf",  # holds the neutrality term files themselves
}

ROOT_ALLOWED_MARKDOWN = {
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
}

# Package/import artifacts that must not (re)appear in the repository root.
ROOT_ARTIFACT_PATTERNS = [
    "NDF_*IMPORT_ANLEITUNG.md",
    "README_WP_*.md",
    "CHANGELOG_WP_*.md",
    "CHANGELOG_*_INTEGRATION.md",
    "CHANGELOG_*_PLANNING.md",
    "CHANGELOG_*_VALIDATION.md",
    "README_*PACK.md",
]

# Import package artifacts that belong under docs/import-history/ only.
IMPORT_ARTIFACT_PATTERNS = [
    "*_IMPORT_ANLEITUNG.md",
    "README_WP_*.md",
    "CHANGELOG_WP_*.md",
]

IMPORT_HISTORY_DIR = "docs/import-history"
RELEASE_HISTORY_DIR = "docs/release/history"

README_REQUIRED_TERMS = [
    "Nova Development Framework",
    "Work Package",
    "Security",
    "Maintainer",
    "Foundation",
]

ENV_DENYLIST_VAR = "NDF_PUBLIC_NEUTRALITY_DENYLIST"
LOCAL_DENYLIST_FILE = Path(".ndf") / "public-neutrality-terms.local.txt"

INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"


class Finding:
    def __init__(self, level: str, message: str) -> None:
        self.level = level
        self.message = message

    def __repr__(self) -> str:
        return f"[{self.level}] {self.message}"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def git_tracked_files(root: Path) -> list[str]:
    """Return repo-relative paths of tracked files; fall back to a walk."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=root, capture_output=True, check=True,
        ).stdout
        return [p.decode("utf-8", "replace") for p in out.split(b"\0") if p]
    except (OSError, subprocess.CalledProcessError):
        files: list[str] = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
            for name in filenames:
                rel = Path(dirpath, name).relative_to(root)
                files.append(rel.as_posix())
        return files


def is_scannable(rel_path: str) -> bool:
    parts = Path(rel_path).parts
    if any(part in IGNORED_DIRS for part in parts):
        return False
    return Path(rel_path).suffix.lower() in TEXT_EXTENSIONS


def load_denylist(root: Path, env: dict[str, str] | None = None) -> tuple[list[str], list[Finding]]:
    """Collect denylist terms from environment variable and local file."""
    env = os.environ if env is None else env
    findings: list[Finding] = []
    terms: list[str] = []

    raw = env.get(ENV_DENYLIST_VAR, "")
    for term in raw.split(","):
        term = term.strip()
        if term:
            terms.append(term)

    local_file = root / LOCAL_DENYLIST_FILE
    if local_file.is_file():
        for line in local_file.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                terms.append(line)

    # dedupe, keep order
    seen: set[str] = set()
    unique = []
    for term in terms:
        key = term.lower()
        if key not in seen:
            seen.add(key)
            unique.append(term)

    if not unique:
        findings.append(Finding(INFO, "No custom neutrality denylist configured."))
    return unique, findings


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

def scan_files_for_terms(root: Path, rel_paths: list[str], terms: list[str]) -> list[Finding]:
    """Case-insensitive substring scan of text files for denylisted terms."""
    findings: list[Finding] = []
    if not terms:
        return findings
    lowered = [(t, t.lower()) for t in terms]
    for rel in rel_paths:
        if not is_scannable(rel):
            continue
        path = root / rel
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            line_lower = line.lower()
            for term, term_lower in lowered:
                if term_lower in line_lower:
                    findings.append(Finding(
                        ERROR,
                        f"neutrality: denylisted term '{term}' found in {rel}:{lineno}",
                    ))
    return findings


def check_root_hygiene(tracked: list[str]) -> list[Finding]:
    """Repository root must stay free of package/import artifacts."""
    findings: list[Finding] = []
    root_files = [p for p in tracked if "/" not in p]
    for name in sorted(root_files):
        for pattern in ROOT_ARTIFACT_PATTERNS:
            if fnmatch.fnmatch(name, pattern):
                findings.append(Finding(
                    ERROR,
                    f"root-hygiene: package artifact '{name}' in repository root "
                    f"(matches '{pattern}'); move it to {IMPORT_HISTORY_DIR}/",
                ))
                break
        else:
            if name.endswith(".md") and name not in ROOT_ALLOWED_MARKDOWN:
                findings.append(Finding(
                    WARNING,
                    f"root-hygiene: unexpected markdown file '{name}' in repository "
                    f"root (allowed: {', '.join(sorted(ROOT_ALLOWED_MARKDOWN))})",
                ))
    return findings


def check_history_separation(tracked: list[str]) -> list[Finding]:
    """Import package artifacts must live under docs/import-history/."""
    findings: list[Finding] = []
    for rel in sorted(tracked):
        if "/" not in rel:
            continue  # root is handled by check_root_hygiene
        name = Path(rel).name
        for pattern in IMPORT_ARTIFACT_PATTERNS:
            if fnmatch.fnmatch(name, pattern):
                if not rel.startswith(IMPORT_HISTORY_DIR + "/"):
                    findings.append(Finding(
                        ERROR,
                        f"history-separation: import artifact '{rel}' must live "
                        f"under {IMPORT_HISTORY_DIR}/ "
                        f"({RELEASE_HISTORY_DIR}/ is reserved for release history)",
                    ))
                break
    if not any(p.startswith(IMPORT_HISTORY_DIR + "/") for p in tracked):
        findings.append(Finding(
            WARNING,
            f"history-separation: {IMPORT_HISTORY_DIR}/ not found or empty",
        ))
    return findings


def check_readme_content(text: str) -> list[Finding]:
    findings: list[Finding] = []
    for term in README_REQUIRED_TERMS:
        if term.lower() not in text.lower():
            findings.append(Finding(
                ERROR,
                f"readme: required term '{term}' missing from README.md",
            ))
    return findings


def check_readme(root: Path) -> list[Finding]:
    readme = root / "README.md"
    if not readme.is_file():
        return [Finding(ERROR, "readme: README.md is missing")]
    text = readme.read_text(encoding="utf-8", errors="replace")
    return check_readme_content(text)


# ---------------------------------------------------------------------------
# runner
# ---------------------------------------------------------------------------

def run_checks(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    tracked = git_tracked_files(root)

    terms, denylist_findings = load_denylist(root)
    findings.extend(denylist_findings)
    findings.extend(scan_files_for_terms(root, tracked, terms))
    findings.extend(check_root_hygiene(tracked))
    findings.extend(check_history_separation(tracked))
    findings.extend(check_readme(root))
    return findings


def report(findings: list[Finding], strict: bool) -> int:
    errors = [f for f in findings if f.level == ERROR]
    warnings = [f for f in findings if f.level == WARNING]
    infos = [f for f in findings if f.level == INFO]

    for finding in errors + warnings + infos:
        print(finding)

    failed = bool(errors) or (strict and bool(warnings))
    print(f"---\n{len(errors)} error(s), {len(warnings)} warning(s), "
          f"{len(infos)} notice(s){' [strict mode]' if strict else ''}")
    if failed:
        print("Public quality gate FAILED.")
        return 1
    print("Public quality gate passed.")
    return 0


# ---------------------------------------------------------------------------
# self-test (uses neutral placeholders only)
# ---------------------------------------------------------------------------

def self_test() -> int:
    failures: list[str] = []

    def expect(condition: bool, label: str) -> None:
        if not condition:
            failures.append(label)

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # 1. denylist via environment-style mapping
        env = {ENV_DENYLIST_VAR: "PRIVATE_PROJECT_A, PRIVATE_PERSON_A"}
        os.environ[ENV_DENYLIST_VAR] = env[ENV_DENYLIST_VAR]
        try:
            terms, notes = load_denylist(root)
        finally:
            del os.environ[ENV_DENYLIST_VAR]
        expect(terms == ["PRIVATE_PROJECT_A", "PRIVATE_PERSON_A"], "env denylist parsing")
        expect(not notes, "no notice when denylist configured")

        # 2. denylist via local file (plus dedupe, comments)
        (root / ".ndf").mkdir()
        (root / LOCAL_DENYLIST_FILE).write_text(
            "# comment\nPRIVATE_OWNER_A\n\nprivate_owner_a\n", encoding="utf-8",
        )
        terms, notes = load_denylist(root, env={})
        expect(terms == ["PRIVATE_OWNER_A"], "local file denylist parsing + dedupe")

        # 3. empty denylist yields a notice, not a failure
        terms, notes = load_denylist(Path(tmp) / "nowhere", env={})
        expect(terms == [], "empty denylist")
        expect(len(notes) == 1 and notes[0].level == INFO, "missing denylist is a notice")

        # 4. neutrality scan finds terms case-insensitively
        (root / "docs").mkdir()
        (root / "docs" / "sample.md").write_text(
            "Line one is fine.\nThis mentions private_project_a here.\n",
            encoding="utf-8",
        )
        hits = scan_files_for_terms(root, ["docs/sample.md"], ["PRIVATE_PROJECT_A"])
        expect(len(hits) == 1 and hits[0].level == ERROR, "neutrality scan hit")
        expect("docs/sample.md:2" in hits[0].message, "neutrality scan location")

        # 5. neutrality scan skips non-text and .ndf files
        hits = scan_files_for_terms(
            root,
            [".ndf/public-neutrality-terms.local.txt"],
            ["PRIVATE_OWNER_A"],
        )
        expect(hits == [], "neutrality scan skips .ndf/")

        # 6. root hygiene flags package artifacts
        tracked = ["README.md", "README_WP_001.md", "NDF_SAMPLE_IMPORT_ANLEITUNG.md",
                   "NOTES.md", "docs/guide.md"]
        hits = check_root_hygiene(tracked)
        expect(
            sum(1 for h in hits if h.level == ERROR) == 2,
            "root hygiene flags artifacts",
        )
        expect(
            any(h.level == WARNING and "NOTES.md" in h.message for h in hits),
            "root hygiene warns on unexpected markdown",
        )

        # 7. history separation flags misplaced import artifacts
        tracked = [
            "docs/import-history/README_WP_001.md",
            "docs/release/history/CHANGELOG_WP_099.md",
        ]
        hits = check_history_separation(tracked)
        expect(
            len([h for h in hits if h.level == ERROR]) == 1
            and "CHANGELOG_WP_099.md" in hits[0].message,
            "history separation flags misplaced artifact",
        )

        # 8. README content check
        good = ("Nova Development Framework, Work Package, Security, "
                "Maintainer, Foundation")
        expect(check_readme_content(good) == [], "readme accepts required terms")
        hits = check_readme_content("Nova Development Framework only")
        expect(len(hits) == 4, "readme flags missing terms")

    if failures:
        for label in failures:
            print(f"self-test FAILED: {label}")
        return 1
    print("self-test passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="NDF public repository quality gate")
    parser.add_argument("--strict", action="store_true",
                        help="treat warnings as errors")
    parser.add_argument("--self-test", action="store_true",
                        help="run internal test cases and exit")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    root = Path(__file__).resolve().parent.parent
    findings = run_checks(root)
    return report(findings, strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
