#!/usr/bin/env python3
"""Validate the public shape and safety boundary of the starter."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED_FILES = {
    ".github/ISSUE_TEMPLATE/first-use-report.yml",
    ".github/workflows/checks.yml",
    "CONTRIBUTING.md",
    "FOR_AGENTS.md",
    "LICENSE",
    "README.md",
    "REVIEW_LOG.md",
    "SECURITY.md",
    "SOURCE_SHELF.md",
    "TODAY.md",
    "USAGE_EVIDENCE.md",
    "WORKING_AGREEMENT.md",
    "context/README.md",
    "outputs/README.md",
}
REQUIRED_AGREEMENT_SECTIONS = {
    "## Purpose",
    "## Source Order",
    "## Authority",
    "## Definition of Done",
    "## Learning Rule",
}
BLOCKED_TEXT = (
    "/" + "Users/",
    "BEGIN " + "PRIVATE KEY",
    "customer " + "export",
    "connector " + "payload",
)
SETUP_ALLOWED_FILES = (
    "WORKING_AGREEMENT.md, TODAY.md, and SOURCE_SHELF.md",
    "Do not take any external action.",
)
TEMPLATE_URL = (
    "https://github.com/new?template_owner=TheDarkniteFalls&"
    "template_name=reliable-ai-work-starter&visibility=private"
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL {message}")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_shape() -> None:
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).is_file())
    if missing:
        fail("missing starter files: " + ", ".join(missing))


def check_agreement() -> None:
    agreement = read("WORKING_AGREEMENT.md")
    missing = sorted(section for section in REQUIRED_AGREEMENT_SECTIONS if section not in agreement)
    if missing:
        fail("working agreement sections missing: " + ", ".join(missing))


def check_setup_boundary() -> None:
    readme = " ".join(read("README.md").split())
    missing = [text for text in SETUP_ALLOWED_FILES if text not in readme]
    if missing:
        fail("setup prompt boundary is incomplete: " + ", ".join(missing))


def check_public_text() -> None:
    paths = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and path.suffix not in {".pyc"}
    )
    combined = "\n".join(path.read_text(encoding="utf-8") for path in paths).lower()
    findings = [text for text in BLOCKED_TEXT if text.lower() in combined]
    if findings:
        fail("public-safety text found: " + ", ".join(findings))


def check_links() -> None:
    if TEMPLATE_URL not in read("README.md"):
        fail("private template URL is missing or stale")
    form = read(".github/ISSUE_TEMPLATE/first-use-report.yml")
    if "Public-data check" not in form or "Starter version" not in form:
        fail("first-use issue form is missing required public evidence fields")


def main() -> int:
    check_shape()
    print("PASS starter_shape")
    check_agreement()
    print("PASS working_agreement")
    check_setup_boundary()
    print("PASS setup_boundary")
    check_public_text()
    print("PASS public_safe_text")
    check_links()
    print("PASS template_links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
