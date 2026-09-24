# Why TraceGate

TraceGate addresses a narrow operational gap in AI application security: teams need a repeatable release gate for complete application trajectories, not only a list of adversarial prompts or isolated model outputs.

NIST recommends robustness evaluation before deployment and ongoing adversarial testing. OWASP describes direct and indirect prompt injection and emphasizes that testing must account for conversation history, retrieved content, tools, and repeated requests. Microsoft reports that manually probing generative-AI systems across harms, modalities, and attack strategies is exceedingly slow. These sources establish the need for repeatable testing, but they do not prescribe a new scanner.

The open-source gap is visible in issue activity. A garak issue reports that a multi-turn probe scores only one turn per conversation. Another requests testing for stale memory across sessions. A Promptfoo issue requests a better way to group repeated stochastic tests. TraceGate responds with an application-level trajectory, state marker, and redacted evidence format. It is designed to complement, not replace, garak and Promptfoo.

## Sustainability

AI security tooling has active contributors and organizational funding. Promptfoo offers community and enterprise tiers, while garak has a public sponsorship path. This does not prove that a new project will receive donations. TraceGate therefore keeps the core free, exposes a GitHub Sponsors path, and documents an eventual optional sustainability layer around hosted evidence retention, team dashboards, policy packs, and support. Sensitive application transcripts should remain local by default.

## Scope boundary

TraceGate does not copy proprietary prompts, attack corpora, or implementation code. The initial attack fixtures are short, original, synthetic examples. A passing result is not a safety certification. The tool reports deterministic policy violations and leaves risk interpretation to the application team.

## References

[1]: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf "NIST AI 600-1 Generative Artificial Intelligence Profile"
[2]: https://github.com/OWASP/www-project-ai-testing-guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md "OWASP AI Testing Guide: Testing for Prompt Injection"
[3]: https://www.microsoft.com/en-us/security/blog/2024/02/22/announcing-microsofts-open-automation-framework-to-red-team-generative-ai-systems/ "Microsoft: Announcing PyRIT"
[4]: https://github.com/NVIDIA/garak/issues/2173 "garak issue: trajectory-aware GOAT probe"
[5]: https://github.com/NVIDIA/garak/issues/2232 "garak issue: stale memory testing"
[6]: https://github.com/promptfoo/promptfoo/issues/992 "Promptfoo issue: grouping repeated tests"
[7]: https://github.com/promptfoo/promptfoo "Promptfoo repository"
[8]: https://github.com/NVIDIA/garak "garak repository"
[9]: https://github.com/sponsors/garak "garak sponsorship page"
