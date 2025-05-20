from datetime import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent

from agents.local_model import llm_model


def get_current_datetime(tz_identifier: str) -> dict:
    """
    Returns the current time in a specified tz_identifier (converted from city).

    Args:
        tz_identifier (str): The tz_identifier of the city for which to retrieve the current date and time.

    Example:
        - new york = "America/New_York"
        - London = "Europe/London"
        - Tokyo = "Asia/Tokyo"
        - dubia = "Asia/Dubai"
        - sydney = "Australia/Sydney"

    Tool Return format:
        message: The current date and time in {city} is {time}.

    """
    print(f"\nCalling datetime tool with {tz_identifier}\n")
    tz = ZoneInfo(tz_identifier)
    now: datetime = datetime.now(tz)
    current: str = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    return {
        "message": f"The current date and time in {tz_identifier.split('/')[1]} is {current}.",
    }


def magic_sum_string(user_string: str) -> dict:
    """
    Returns the unicode code sum (aka magic sum) of the characters in a string.

    Args:
        user_string (str): The string to sum.

    Tool Return format:
        message: The magic sum {user_string} is {sum}.

    """
    print(f"\nCalling magic sum tool with {user_string}\n")
    total = 0
    for char in user_string:
        total += ord(char)

    return {"message": f"The magic sum {user_string} is {total}."}


root_agent = Agent(
    name="time_sum_agent",
    description="Agent to retrieve the current time for the given city and magic sum of a string.",
    # Here we are using the reasoning model to generate the tools because other models don't work well with tools.
    model=llm_model("qwen3:4b"),
    instruction="You are a helpful agent who can provide the current time of a city or magic sum of a string.",
    tools=[get_current_datetime, magic_sum_string],
)
