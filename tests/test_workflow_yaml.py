"""Validate .github/workflow YAML files for duplicate top-level keys.

Catches duplicate-key bugs (e.g. duplicate 'on:' or 'permissions:' blocks)
that YAML silently merges. Must pass before CI/PR merge.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
WORKFLOWS = REPO / ".github" / "workflows"


def check_workflow_yaml(filepath: Path) -> int:
    """Return 0 if file has no duplicate top-level keys, 1 otherwise."""
    text = filepath.read_text()
    top_keys: dict[str, int] = {}
    errors = 0

    for i, line in enumerate(text.split("\n"), 1):
        m = re.match(r"^([\w][\w-]*):", line)
        if m:
            key = m.group(1)
            if key in top_keys:
                print(
                    f"{filepath.name}:{i}: duplicate top-level key"
                    f" '{key}' (first at line {top_keys[key]})"
                )
                errors += 1
            top_keys[key] = i

    if errors == 0:
        print(f"  {filepath.name}: OK ({len(top_keys)} top-level keys)")
    return errors


def main() -> int:
    if not WORKFLOWS.is_dir():
        print(f"SKIP: {WORKFLOWS} not found")
        return 0

    total_errors = 0
    for wf in sorted(WORKFLOWS.glob("*.yml")):
        total_errors += check_workflow_yaml(wf)

    if total_errors:
        print(f"\nFAIL: {total_errors} error(s) in workflow YAML files")
        return 1

    print("\nAll workflow YAML files valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
