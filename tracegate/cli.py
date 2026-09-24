from __future__ import annotations

import argparse
import sys

from .core import load_scenario, run_scenario, write_result


def main() -> int:
    parser = argparse.ArgumentParser(prog="tracegate", description="Run local-first AI application trajectory policy checks.")
    parser.add_argument("scenario", help="YAML scenario file")
    parser.add_argument("--output", default="tracegate-results.json", help="JSON evidence output")
    parser.add_argument("--sarif", help="Optional SARIF output for GitHub code scanning")
    args = parser.parse_args()
    try:
        result = run_scenario(load_scenario(args.scenario))
        write_result(result, args.output, args.sarif)
    except (OSError, ValueError) as exc:
        print(f"TraceGate configuration error: {exc}", file=sys.stderr)
        return 2
    for finding in result.findings:
        print(f"{finding.rule_id}: {finding.message}", file=sys.stderr)
    print(f"{result.scenario}: {'PASS' if result.passed else 'FAIL'} ({len(result.findings)} unique findings)")
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
