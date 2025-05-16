# Agents with tools:

Types of tools:

- Function tools: custom/specific functions/tools (mostly used).
- Buit-in-tools: Only work with gemini models.
- Third-Party tools: LangChain, CrewAI etc.

## What we did here:

We have two tools here:
  - Current time
  - Magic sum

General LLM can't answer such questions because they have information about the past events only not the current. Also Magic sum does some calculation which any LLM doesn't know because it is a custom usecase.

So to run the code:

1. Navigate to `02_tools_agent` from root:

```sh
cd agents/02_tools_agent
```

2. Start the ADK web version:

```sh
adk web # Access from localhost:8000
```
