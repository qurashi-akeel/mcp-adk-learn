from google.adk.agents import Agent

from agents.local_model import llm_model

root_agent = Agent(
    name="hello_world",
    description="A simple joker greeting agent",
    model=llm_model(),
    instruction="You are a funny greeting assistant. Say hello world with a funny message if user doesn't provide their name, else greet them in a funny way with there name.",
)
