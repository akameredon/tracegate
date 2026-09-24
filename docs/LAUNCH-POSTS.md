# TraceGate Launch Posts

Repository: https://github.com/akameredon/tracegate

TraceGate is a local-first CLI for testing AI application trajectories. It checks whether untrusted input causes unsafe tool calls, whether destructive actions bypass approval, whether a secret canary is disclosed, and whether expected grounding markers are missing. It produces redacted JSON evidence and SARIF output. The repository is MIT-licensed and welcomes contributions.

These drafts are intentionally adapted rather than copied across platforms. Replace the optional placeholders before publishing.

## X / Twitter

**Post 1 — launch thread**

AI apps do not fail only at the prompt level.

They fail when a complete trajectory causes an unsafe tool call, bypasses approval, leaks a secret, or loses grounding after a model or retrieval change.

I built TraceGate to test those application-level invariants locally and in CI.

https://github.com/akameredon/tracegate

**Post 2 — what it does**

TraceGate is a small MIT-licensed CLI that:

• replays synthetic injection scenarios
• repeats stochastic tests
• captures redacted trajectories
• checks tool, approval, canary, and grounding policies
• emits SARIF for GitHub workflows

It complements prompt scanners instead of trying to replace them.

**Post 3 — invitation**

The first MVP is intentionally narrow. I’m looking for contributors who want to add:

• HTTP/OpenAI-compatible adapters
• streaming-event capture
• policy assertions
• safe synthetic fixtures
• baseline comparisons

If you build AI applications or security tooling, feedback is welcome.

#OpenSource #AISafety #Python

## LinkedIn

**Headline:** Introducing TraceGate: a local-first safety regression gate for AI applications

AI application testing becomes difficult when the risk is not visible in a single prompt or response.

A model, prompt, retrieval source, tool schema, or guardrail change can alter the complete application trajectory. The application may call a destructive tool from untrusted text, bypass an approval step, disclose a secret, or lose grounding. Teams need a repeatable way to detect those regressions before release.

I created TraceGate, an original MIT-licensed open-source project that focuses on this application-level gap. It runs synthetic prompt-injection scenarios, supports repeated evaluation, records redacted evidence, and checks deterministic policies for tool calls, approvals, canary disclosure, and grounding. It can also emit SARIF for GitHub workflows.

TraceGate is deliberately complementary to established prompt scanners and model benchmarks. Its focus is the observable trajectory: what the application actually did across turns and state, not only whether a model produced a suspicious string.

The project is now public and open to contributors. The first roadmap items include an HTTP/OpenAI-compatible adapter, streaming-event capture, baseline comparison, and additional privacy-preserving policy checks.

Repository: https://github.com/akameredon/tracegate

I would especially value feedback from AI application developers, red-teamers, maintainers of open-source agents, and people working on secure tool use.

#OpenSource #ArtificialIntelligence #AISafety #Cybersecurity #Python #SoftwareEngineering

## Reddit — r/opensource

**Title:** I built TraceGate, an MIT-licensed local-first regression gate for AI application trajectories

**Post:**

I’m building TraceGate to address a narrow problem in AI application testing: a prompt or model change can alter the complete trajectory of an application, but many testing workflows still focus on isolated prompts and outputs.

TraceGate runs synthetic scenarios and checks application-level policies such as:

- untrusted text must not create a tool call;
- destructive tools must require explicit approval;
- a secret canary must not appear in the assistant response; and
- required grounding markers must be present.

It stores redacted JSON evidence and can emit SARIF for GitHub workflows. The current release includes a deterministic dry-run adapter, a YAML scenario format, a Python API, an example, and tests.

This is not intended to replace Promptfoo, garak, or other scanners. The proposed niche is a portable trajectory/evidence layer that can complement them.

Repository: https://github.com/akameredon/tracegate

I’m looking for critical feedback on the scenario format and contributor interest around adapters, policy rules, streaming events, and baseline comparison. Please use synthetic fixtures only; the project should not receive real secrets or private transcripts.

## Reddit — r/LocalLLaMA or an AI engineering community

**Title:** TraceGate: test whether your AI app actually calls tools safely

**Post:**

Most AI safety demos stop at “did the model refuse the prompt?” Production failures are often different: did the agent call a tool, did it ask for approval, did it expose a canary, and what happened after several turns?

TraceGate is a small local-first open-source CLI for those checks. It runs repeatable scenarios, records redacted trajectories, and returns CI-friendly SARIF. The core is intentionally adapter-based so it can work with different AI applications instead of requiring a hosted service.

GitHub: https://github.com/akameredon/tracegate

I’m interested in feedback from people running local models, RAG systems, agents, and tool-using applications.

## Hacker News — Show HN

**Title:** Show HN: TraceGate – local-first trajectory regression gates for AI applications

**Post:**

I built TraceGate, a small MIT-licensed CLI that tests AI applications at the trajectory level rather than treating a prompt and one output as the complete unit of evaluation.

A YAML scenario defines trusted intent, untrusted attack fixtures, repeat count, and policies. The initial checks detect tool calls caused by untrusted input, destructive tools without approval, secret-canary disclosure, and missing grounding markers. TraceGate stores redacted JSON evidence and can emit SARIF for CI.

The first release includes a deterministic dry-run adapter so the example runs without an API key or any transcript leaving the machine. The adapter interface is intentionally small and is the planned extension point for HTTP/OpenAI-compatible applications and other runtimes.

This is not a replacement for prompt scanners or model benchmarks. The intended scope is a portable application-level regression and evidence layer that can complement those tools.

Repository: https://github.com/akameredon/tracegate

The main questions I’m exploring are whether this scenario format is useful, which trajectory events should be standardized first, and how to keep evidence safe by default.

## Dev.to

**Title:** Why AI safety tests should inspect trajectories, not only prompts

**Tags:** #ai #opensource #python #security

**Excerpt:**

An AI application can pass a prompt-level refusal test and still behave unsafely when retrieval content, tools, approvals, and conversation history are involved. TraceGate is an original MIT-licensed project that treats the observable application trajectory as the regression unit.

**Body:**

When an AI application changes, the risk is not limited to the text of the final answer. A new model, system prompt, retrieval source, or tool definition can change whether untrusted content leads to a tool call, whether an approval step is skipped, or whether sensitive data appears in the response.

That is the problem TraceGate is designed to make easier to test. It provides a small YAML scenario format, repeat controls, deterministic policy assertions, redacted evidence, and SARIF output for GitHub workflows.

The current policy checks are intentionally understandable:

- untrusted input must not create a tool call;
- destructive tools must have explicit approval;
- a secret canary must not be disclosed; and
- answers requiring a grounding marker must include it.

TraceGate is not a model benchmark and does not claim that a passing run proves an application is safe. It is a release-gating layer that records what the complete application did in a controlled scenario. It is also designed to complement established scanners rather than duplicate them.

The project is public on GitHub: https://github.com/akameredon/tracegate

Contributions are welcome around adapters, streaming-event capture, policy rules, privacy-preserving redaction, and baseline comparison. Please keep fixtures synthetic and never submit private prompts, customer data, or real credentials.

## Discord / Slack developer community

I’ve published TraceGate, an MIT-licensed open-source CLI for testing AI application trajectories in local development and CI.

It currently checks whether synthetic untrusted input causes unsafe tool calls, whether destructive actions bypass approval, whether a canary is disclosed, and whether grounding markers are missing. It generates redacted JSON evidence and SARIF.

Repo: https://github.com/akameredon/tracegate

I’m looking for early feedback on the YAML scenario format and contributors interested in adapters, policy assertions, streaming events, and baseline comparison. The project is local-first and should be tested only with synthetic data.

## GitHub repository announcement / Discussions

TraceGate is now public.

The project provides a local-first way to regression-test AI application trajectories. It focuses on application-level invariants that are easy to lose during model, prompt, retrieval, or tool changes: safe tool use, explicit approval, canary non-disclosure, and grounding.

The initial release includes a Python CLI, YAML scenarios, redacted evidence, SARIF output, a deterministic dry-run adapter, tests, CI, contributor guidance, and a roadmap.

Start here: https://github.com/akameredon/tracegate

Please open an issue if you have a concrete adapter, policy, fixture, or documentation improvement. Keep all examples synthetic and privacy-safe.

## Product Hunt-style short description

**Name:** TraceGate

**Tagline:** Catch unsafe AI tool and data regressions before release.

**Description:** TraceGate is a local-first, MIT-licensed CLI that replays synthetic prompt-injection scenarios against AI applications and checks complete trajectories for unsafe tool calls, missing approvals, secret-canary disclosure, and grounding failures. It produces redacted evidence and SARIF for CI.

**Maker comment:** I built TraceGate as a narrow, complementary layer for teams that already use prompt tests but need to know what their application actually did across turns, state, and tools. The core is free and open source, and I’m looking for contributors to expand adapters and policy checks.

## Publishing notes

Do not publish every post at the same time. Start with GitHub and one community where you can answer technical questions. Use the Hacker News version only when you can stay available for discussion. On Reddit, follow each subreddit’s self-promotion rules and disclose that you are the project creator. On LinkedIn, keep the post focused on the problem and practical value rather than repeating the repository README. On X, post the thread as a connected sequence and reply with the repository link rather than filling every post with hashtags.
