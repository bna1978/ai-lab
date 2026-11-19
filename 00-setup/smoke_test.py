"""Week 0 smoke test.

Checks that your API keys work and that Ollama is running.
For each provider it prints input tokens, output tokens and latency,
so you see from day one what every call costs you.

Run:  uv run python 00-setup/smoke_test.py
"""

import json
import os
import time
import urllib.request

from dotenv import load_dotenv

load_dotenv()

PROMPT = "In one sentence, what is a token in a large language model?"


def cost(prefix, tokens_in, tokens_out):
    price_in = os.getenv(f"{prefix}_PRICE_IN")
    price_out = os.getenv(f"{prefix}_PRICE_OUT")
    if not price_in or not price_out:
        return f"cost=? (set {prefix}_PRICE_IN and {prefix}_PRICE_OUT in .env)"
    usd = (tokens_in * float(price_in) + tokens_out * float(price_out)) / 1_000_000
    return f"${usd:.6f}"


def check_anthropic():
    key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("ANTHROPIC_MODEL")
    if not key or not model:
        return "SKIPPED - set ANTHROPIC_API_KEY and ANTHROPIC_MODEL in .env"
    import anthropic

    client = anthropic.Anthropic(api_key=key)
    start = time.perf_counter()
    resp = client.messages.create(
        model=model,
        max_tokens=100,
        messages=[{"role": "user", "content": PROMPT}],
    )
    elapsed = time.perf_counter() - start
    text = resp.content[0].text.strip()
    return (
        f"OK | in={resp.usage.input_tokens} out={resp.usage.output_tokens} "
        f"| {elapsed:.2f}s "
        f"| {cost('ANTHROPIC', resp.usage.input_tokens, resp.usage.output_tokens)}"
        f"\n    {text}"
    )


def check_openai():
    key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")
    if not key or not model:
        return "SKIPPED - set OPENAI_API_KEY and OPENAI_MODEL in .env"
    from openai import OpenAI

    client = OpenAI(api_key=key)
    start = time.perf_counter()
    resp = client.chat.completions.create(
        model=model,
        max_completion_tokens=100,
        messages=[{"role": "user", "content": PROMPT}],
    )
    elapsed = time.perf_counter() - start
    text = resp.choices[0].message.content.strip()
    return (
        f"OK | in={resp.usage.prompt_tokens} out={resp.usage.completion_tokens} "
        f"| {elapsed:.2f}s "
        f"| {cost('OPENAI', resp.usage.prompt_tokens, resp.usage.completion_tokens)}"
        f"\n    {text}"
    )


def check_ollama():
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    try:
        with urllib.request.urlopen(f"{host}/api/tags", timeout=3) as r:
            models = [m["name"] for m in json.load(r).get("models", [])]
    except Exception:
        return f"NOT RUNNING at {host} - install Ollama and start it"
    if not models:
        return "RUNNING, but no models yet - try: ollama pull <model>"
    return "RUNNING | models: " + ", ".join(models)


if __name__ == "__main__":
    for name, fn in [
        ("Anthropic", check_anthropic),
        ("OpenAI", check_openai),
        ("Ollama", check_ollama),
    ]:
        try:
            result = fn()
        except Exception as e:  # show the real error, it's part of learning
            result = f"FAILED - {type(e).__name__}: {e}"
        print(f"{name:10} {result}")
