#!/usr/bin/env python3
"""Validate the staged Hermes SEO skill pack without external access."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "hermes-seo-orchestrator",
    "hermes-seo-research",
    "hermes-seo-audit",
    "hermes-seo-strategy",
    "hermes-seo-copywriting",
    "hermes-seo-editing",
]
REQUIRED = ("OBSERVED", "INFERRED", "GAP", "explicit human approval")
FORBIDDEN = re.compile(r"(?:api[_ -]?key|password|secret|token)\s*[:=]\s*[^\s<]{8,}", re.I)
errors: list[str] = []

for name in SKILLS:
    source = ROOT / "skills" / name / "SKILL.md"
    local = ROOT / ".agents" / "skills" / name / "SKILL.md"
    if not source.is_file():
        errors.append(f"missing canonical skill: {source.relative_to(ROOT)}")
        continue
    text = source.read_text(encoding="utf-8")
    if not text.startswith("---\n") or text.count("---\n", 0, 4096) < 2:
        errors.append(f"invalid frontmatter: {source.relative_to(ROOT)}")
    if f"name: {name}" not in text[:512]:
        errors.append(f"wrong name field: {source.relative_to(ROOT)}")
    for phrase in REQUIRED:
        if phrase not in text:
            errors.append(f"missing required safety/evidence phrase {phrase!r}: {name}")
    if FORBIDDEN.search(text):
        errors.append(f"possible credential literal: {name}")
    if not local.is_file():
        errors.append(f"missing Hermes local copy: {local.relative_to(ROOT)}")
    elif source.read_bytes() != local.read_bytes():
        errors.append(f"local copy differs from canonical: {name}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"VALIDATION PASSED: {len(SKILLS)} canonical skills and matching Hermes project-local copies")
for name in SKILLS:
    path = ROOT / "skills" / name / "SKILL.md"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"- {name}: {digest}")
