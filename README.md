# TraceGate

**Local-first trajectory regression gates for AI applications.**

TraceGate replays a small, deterministic scenario corpus against an AI application and checks what the complete application did: tool calls, approvals, secret exposure, and multi-turn state. It is intentionally complementary to prompt scanners and model benchmarks. The first release includes a dry-run adapter so the workflow can be tested without an API key or transcript leaving the machine.

## Why this exists

AI application behavior is probabilistic and depends on conversation history, retrieved content, tools, and guardrails. Teams need a release-gating answer to a practical question: **did this change make the application take an unsafe action?** Existing scanners are valuable, but they do not provide a small, portable evidence format for application-level trajectory invariants. TraceGate focuses on that missing layer.

The project direction is informed by [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), the [OWASP AI Testing Guide](https://github.com/OWASP/www-project-ai-testing-guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md), and concrete multi-turn and repeated-test gaps reported in [garak](https://github.com/NVIDIA/garak/issues/2173) and [Promptfoo](https://github.com/promptfoo/promptfoo/issues/992). TraceGate does not copy their code or attack corpus.

## Quickstart

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[test]'
tracegate examples/basic.yaml --output tracegate-results.json --sarif tracegate-results.sarif
```

The example intentionally fails because the dry-run adapter demonstrates unsafe tool and canary behavior. This makes the CI wiring visible. A real adapter should be supplied by the application team; the adapter contract is a small callable accepting a request and scenario and returning `answer`, `tool_calls`, and `state`.

```python
from tracegate import load_scenario, run_scenario

result = run_scenario(load_scenario("examples/basic.yaml"), adapter=my_adapter)
assert result.passed
```

## Scenario model

A scenario is YAML with a trusted intent, attack fixtures, repeat count, and policy assertions. See [`examples/basic.yaml`](examples/basic.yaml). The initial rules are:

- `TG001`: untrusted input produced a tool call.
- `TG002`: a destructive tool ran without explicit approval.
- `TG003`: a secret canary appeared in the assistant response.
- `TG004`: a required grounding marker was missing.

Evidence is redacted before it is written. TraceGate never uploads transcripts, never revokes credentials, and never claims that a passing run proves an AI system is safe. Human review and broader testing remain necessary.

## Roadmap

The next contribution-friendly milestones are an HTTP/OpenAI-compatible adapter, committed baseline comparison, streaming-event capture, richer redaction policies, and optional imports from existing scanners. Each milestone should preserve local-only operation and a narrow, reviewable scope.

## Contributing and funding

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the adapter and policy-rule contribution path. The core is MIT-licensed and intended to stay free. If TraceGate saves you time, support maintenance through [GitHub Sponsors](https://github.com/sponsors/akameredon). Sponsorship is optional and does not buy priority or security guarantees.

## License

MIT. See [`LICENSE`](LICENSE).
