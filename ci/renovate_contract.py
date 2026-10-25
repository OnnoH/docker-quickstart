#!/usr/bin/env python3
"""Check that renovate.json still matches the acceptance criteria of ONN-23.

Run it from the repository root:

    python3 ci/renovate_contract.py

The ci-contract job reaches it through ci/ci_contract.py; the workflow itself
is the board's and stays untouched. Each check carries the issue and the
number of the criterion it covers:

  ONN-23 AC-1  renovate.json sits at the repository root and holds the
               configuration the board agreed on.
  ONN-23 AC-2  renovate-config-validator accepts that file.
  ONN-23 AC-4  nothing under .github/ changes along with it; the workflows,
               CODEOWNERS and the Dependabot configuration are the board's.
"""

import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "renovate.json"

# The configuration as the issue spells it out. This duplication is the point:
# the expected value lives in the check, not in the file under test.
EXPECTED = {
    "$schema": "https://docs.renovatebot.com/renovate-schema.json",
    "extends": ["config:recommended"],
    "packageRules": [
        {
            "description": (
                "Merge minor, patch, pin and digest updates once CI is green; "
                "majors wait for a maintainer."
            ),
            "matchUpdateTypes": ["minor", "patch", "pin", "digest"],
            "automerge": True,
        }
    ],
}

failures = []


def check(ac, description, ok):
    status = "PASS" if ok else "FAIL"
    print(f"{status} [ONN-23 {ac}] {description}")
    if not ok:
        failures.append(f"[ONN-23 {ac}] {description}")


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True
    )


# AC-1 the file is there and says what it is supposed to say.
check("AC-1", "renovate.json sits at the repository root", CONFIG.is_file())

if CONFIG.is_file():
    try:
        config = json.loads(CONFIG.read_text())
    except json.JSONDecodeError as error:
        config = None
        print(f"renovate.json is not valid JSON: {error}")
    check("AC-1", "renovate.json holds the configuration the board agreed on",
          config == EXPECTED)
    if config is not None and config != EXPECTED:
        print("  expected:", json.dumps(EXPECTED, sort_keys=True))
        print("  found:   ", json.dumps(config, sort_keys=True))

# AC-2 Renovate's own validator accepts it. The validator is the only thing
# that can say whether Renovate will read the file at all.
if shutil.which("npx") is None:
    check("AC-2", "npx is available to run renovate-config-validator", False)
else:
    validator = subprocess.run(
        ["npx", "--yes", "--package", "renovate",
         "renovate-config-validator", "renovate.json"],
        cwd=ROOT, capture_output=True, text=True,
    )
    check("AC-2", "renovate-config-validator accepts renovate.json",
          validator.returncode == 0)
    if validator.returncode != 0:
        print(validator.stdout)
        print(validator.stderr)

# AC-4 the change leaves .github/ alone. Which files changed is a property of
# the pull request, so the base of the comparison comes from the event payload
# on a pull_request run and from origin/main when run by hand on a branch.
def comparison_base():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and pathlib.Path(event_path).is_file():
        payload = json.loads(pathlib.Path(event_path).read_text())
        base_sha = ((payload.get("pull_request") or {}).get("base") or {}).get("sha")
        if not base_sha:
            return None  # a push run; the pull_request run does this check
        if git("cat-file", "-e", f"{base_sha}^{{commit}}").returncode != 0:
            git("fetch", "--no-tags", "--depth=1", "origin", base_sha)
        return base_sha
    if git("rev-parse", "--verify", "HEAD").returncode != 0:
        return None
    if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() == "main":
        return None  # on main itself there is nothing to compare against
    shallow = git("rev-parse", "--is-shallow-repository").stdout.strip() == "true"
    git("fetch", "--no-tags", *(["--depth=50"] if shallow else []), "origin", "main")
    return "origin/main"


base = comparison_base()
if base is None:
    print("NOTE [ONN-23 AC-4] no pull request to compare against, not checked here")
else:
    diff = git("diff", "--name-only", base, "HEAD")
    if diff.returncode != 0:
        check("AC-4", f"the tree can be compared against {base}", False)
        print(diff.stderr)
    else:
        touched = [path for path in diff.stdout.split() if path.startswith(".github/")]
        check("AC-4", "no file under .github/ changes" +
              (": " + ", ".join(touched) if touched else ""), not touched)

if failures:
    print(f"\n{len(failures)} check(s) failed:")
    for failure in failures:
        print(f"  - {failure}")
    sys.exit(1)

print("\nrenovate.json matches the acceptance criteria.")
