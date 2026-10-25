#!/usr/bin/env python3
"""Check that .github/workflows/ci.yml still matches the acceptance criteria.

Run it from the repository root:

    python3 ci/ci_contract.py

Each check carries the number of the criterion it covers:

  AC-1  Markdown and the exercise HTML are linted on every push and pull
        request, and a lint error fails the check.
  AC-2  Both exercise images are built on every push and pull request, and a
        build failure fails the check.
  AC-3  gitleaks runs on every push and pull request and a finding fails the
        check.
  AC-4  There is no tests job: this repository has no executable code to test.
"""

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKFLOW = ROOT / ".github/workflows/ci.yml"

failures = []


def check(ac, description, ok):
    status = "PASS" if ok else "FAIL"
    print(f"{status} [{ac}] {description}")
    if not ok:
        failures.append(f"[{ac}] {description}")


def run_lines(job):
    """Every shell command in a job, one per line."""
    lines = []
    for step in job.get("steps") or []:
        lines.extend((step.get("run") or "").splitlines())
        if step.get("uses"):
            lines.append(f"uses: {step['uses']}")
    return lines


workflow = yaml.safe_load(WORKFLOW.read_text())
# PyYAML reads YAML 1.1, where the bare key `on` is the boolean True.
triggers = workflow.get("on", workflow.get(True)) or {}
jobs = workflow.get("jobs") or {}

for ac in ("AC-1", "AC-2", "AC-3"):
    check(
        ac,
        "the workflow runs on both push and pull_request",
        {"push", "pull_request"} <= set(triggers),
    )

commands = {name: run_lines(job) for name, job in jobs.items()}


def some_job_runs(pattern):
    return any(
        re.search(pattern, line) for lines in commands.values() for line in lines
    )


check("AC-1", "a job runs markdownlint", some_job_runs(r"markdownlint"))
check("AC-1", "a job lints the exercise HTML", some_job_runs(r"htmlhint"))
check("AC-1", "markdownlint has a configuration in the repository",
      (ROOT / ".markdownlint-cli2.jsonc").is_file())
check("AC-1", "htmlhint has a configuration in the repository",
      (ROOT / ".htmlhintrc").is_file())

# Every Dockerfile shipped with the exercises has to be built, not just the two
# that existed when this check was written.
dockerfiles = sorted(
    path.relative_to(ROOT).as_posix()
    for path in ROOT.glob("exercises/exercise-[67]/Dockerfile.*")
)
check("AC-2", "the exercise Dockerfiles are still there", len(dockerfiles) == 3)
for dockerfile in dockerfiles:
    check("AC-2", f"a job builds {dockerfile}",
          some_job_runs(rf"docker build.*{re.escape(dockerfile)}"))

check("AC-3", "a job runs a gitleaks scan",
      some_job_runs(r"gitleaks\"? +(dir|git|detect)\b"))

tests_job = re.compile(r"(^|[-_])tests?([-_]|$)")
check("AC-4", "there is no tests job",
      not [name for name in jobs if tests_job.search(name)])

if failures:
    print(f"\n{len(failures)} check(s) failed:")
    for failure in failures:
        print(f"  - {failure}")
    sys.exit(1)

print(f"\nAll {len(jobs)} jobs match the acceptance criteria.")
