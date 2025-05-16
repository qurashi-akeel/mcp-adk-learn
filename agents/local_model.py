from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv

# Load ollama baseURL
load_dotenv()

print(
    "Current agent started with local OLLAMA:",
    os.getenv("OLLAMA_API_BASE")
)


def ollama_model(local_model_name: str = "llama3.2:latest"):
    return LiteLlm(
        model=f"ollama_chat/{local_model_name}"
    )
