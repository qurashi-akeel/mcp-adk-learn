import random

from google.adk.agents import Agent

from agents.local_model import llm_model


def get_joke() -> str:
    """
    A simple function to return a random joke.

    This function is used as a tool in the agent.
    """
    jokes: list[str] = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the math book look sad? Because it had too many problems!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    ]

    return random.choice(jokes)


root_agent = Agent(
    name="joke_picker",
    description="A simple agent that picks a random joke.",
    model=llm_model("openai/gpt-4o-mini"),
    instruction="You are a joke agent. Use only `get_joke` tool to tell a joke.",
    tools=[get_joke],
)
