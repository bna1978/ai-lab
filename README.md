# ai-lab

My hands-on AI training: 12 weeks, about 7 hours a week.
Full plan: "AI Hands-on Training Plan" doc.

| Folder | Phase | Weeks |
|---|---|---|
| 00-setup | Setup | 0 |
| 01-prompting | LLM fundamentals and prompting | 1 |
| 02-rag | RAG and retrieval | 2-3 |
| 03-evals-guardrails | Evaluation and guardrails | 4-5 |
| 04-agents-mcp | Agents and MCP | 6-7 |
| 05-local-models | Local and open-weight models | 8 |
| 06-llmops | LLMOps, cost and vetting | 9 |
| 07-capstone | Capstone | 10-12 |

Rules: public data only, a number for every experiment, write LEARNINGS.md every week.

## Run
```
uv sync
cp .env.example .env   # then fill in keys and model names
uv run python 00-setup/smoke_test.py
```
