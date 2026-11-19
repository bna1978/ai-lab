# Learning log

One entry per week. Keep it short and honest.

## Week 0 - Setup
- **Built:** Installed everything that was needed to connec tto API and run Llama 3.2 locally, created a smoke test script with Python. Git is working and pushing all my changes there. Claude CLI is working directly on Terminal on VS Code. gtp-5 was deprecated and I have toc hange it on the env file to gpt-5.6-luna. Show latency tokens and costs per call.
- **What broke:**
 OpenAI rejected `max_tokens`: newer reasoning models need
  `max_completion_tokens`. Each provider's API has its own quirks.
- gpt-5-nano is being shut down on 11 Dec 2026, so I switched to
  gpt-5.6-luna. Models get retired every few months.
- Git push asked for the Mac keychain password; fixed by signing in
  with the GitHub CLI (`gh auth login`).
- **The number I got:** Anthropic  OK | in=24 out=50 | 1.22s | $0.000027 and Anthropic  OK | in=24 out=50 | 1.22s | $0.000027 - I cannot compare models, since thye may be different, but Anthropic looked cheaper and faster
- Anthropic: [ ] tokens in, [ ] out, [ ]s, cost [ ] USD
- OpenAI: [ ] tokens in, [ ] out, [ ]s, cost [ ] USD
- The OpenAI answer was one short sentence, but output tokens were [ ].
  The difference is hidden reasoning tokens, which are billed as outpu
- **What I'd tell a client:**
- Estimate costs from real calls, not from the visible answer length.
  Reasoning models can bill several times more output than you see.
- Keep model names in config, not in code, and have an eval set ready,
  because providers retire models with a few months' notice.