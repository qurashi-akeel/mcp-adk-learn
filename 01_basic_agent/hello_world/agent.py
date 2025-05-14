from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os

from dotenv import load_dotenv

# Load ollama baseURL
load_dotenv()

print(
    "Hello world agent started with local OLLAMA:",
    os.getenv("OLLAMA_API_BASE")
)

root_agent = Agent(
    name="HelloWorld",
    description="A simple joker greeting agent",
    model=LiteLlm(
        model="ollama_chat/granite3.3:2b"
    ),
    instruction="You are a funny greeting assistant. Say hello world with a funny message if user doesn't provide their name, else greet them in a funny way with there name.",
)
