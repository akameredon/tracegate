# Contributing to TraceGate

Thank you for helping make AI application testing more reproducible. Contributions are welcome in four areas: adapters, policy assertions, redaction rules, and small attack fixtures that are safe to publish.

## Before opening a pull request

Please open an issue for substantial behavior changes. Keep pull requests narrow, add a regression test, and explain whether the change affects evidence privacy or exit-code behavior. Do not include real secrets, private prompts, customer data, or undisclosed vulnerabilities. Use synthetic canaries and public fixtures only.

## Development

```bash
pip install -e '.[test]'
pytest
tracegate examples/basic.yaml --output /tmp/tracegate.json --sarif /tmp/tracegate.sarif
```

## Good first contributions

A good first contribution can add an adapter fixture, a policy rule with a deterministic test, a redaction pattern with documented trade-offs, or an improvement to the SARIF and GitHub Actions documentation. Please avoid adding a large payload corpus without an accompanying rationale and licensing review.

## Security reports

Do not disclose active secrets or exploitable target details in public issues. Use GitHub's private vulnerability reporting if enabled, or contact the maintainer through the profile email before public disclosure.

By contributing, you agree that your work is provided under the MIT License.
