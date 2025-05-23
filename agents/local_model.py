import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

print(
    "Current agent started with local OLLAMA:",
    os.getenv("OLLAMA_API_BASE"),
)


def llm_model(
    model_name: str = "llama3.2:latest",
) -> LiteLlm:
    api_key: str | None = None

    if len(model_name.split("/")) == 1:  # local model
        return LiteLlm(model=f"ollama/{model_name}")

    # remote model
    match model_name.split("/")[0]:
        # In case of gemini we can pass it directly
        case "openai":
            api_key = os.getenv("OPENAI_API_KEY")
        case _:
            msg: str = f"{model_name} is not supported."
            raise ValueError(msg)

    return LiteLlm(model=model_name, api_key=api_key)
