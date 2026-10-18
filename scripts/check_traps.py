#!/usr/bin/env python3
"""Verify that Cerune safely rejects known runtime-invalid programs."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

ROUTES = ("run", "run-mir", "run-vm")
DIAGNOSTIC = re.compile(rb"(?m)^cerune: runtime-v1 code=([a-z0-9-]+)(?=\s|$)")


def matches_trap(result, code, expected_stdout):
    """A signal, timeout or unrelated CLI error must never count as a trap."""
    codes = DIAGNOSTIC.findall(result.stderr)
    return (
        result.returncode == 1
        and result.stdout == expected_stdout.encode("utf-8")
        and codes == [code.encode("ascii")]
    )


def run(binary, arguments, timeout):
    return subprocess.run(
        [str(binary), *arguments],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--cases", type=Path, default=Path("cases"))
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")

    manifest = json.loads((args.cases / "expectations.json").read_text(encoding="utf-8"))
    actual = {file.stem for file in args.cases.glob("*.ceru")}
    if not manifest or actual != set(manifest):
        parser.error("fixture names and expectations.json entries must match")

    binary = args.binary.resolve()
    failures = 0
    for name, spec in sorted(manifest.items()):
        source = str((args.cases / (name + ".ceru")).resolve())
        try:
            check = run(binary, ["check", source], args.timeout)
            if check.returncode != 0:
                print(f"FAIL {name} [check]: {check.stderr[:500]!r}", file=sys.stderr)
                failures += 1
                continue

            for route in ROUTES:
                result = run(
                    binary, [route, source, "--diagnostic-format", "runtime-v1"], args.timeout
                )
                if matches_trap(result, spec["code"], spec["stdout"]):
                    print(f"PASS {name} [{route}]: {spec['code']}")
                else:
                    failures += 1
                    print(
                        f"FAIL {name} [{route}]: expected {spec['code']!r}, "
                        f"exit={result.returncode}, stdout={result.stdout!r}, "
                        f"stderr={result.stderr[:500]!r}",
                        file=sys.stderr,
                    )
        except (OSError, subprocess.TimeoutExpired) as exc:
            failures += 1
            print(f"FAIL {name}: {exc}", file=sys.stderr)

    print(f"Checked {len(manifest)} cases across {len(ROUTES)} execution routes; failures: {failures}")
    return int(failures != 0)


if __name__ == "__main__":
    sys.exit(main())
