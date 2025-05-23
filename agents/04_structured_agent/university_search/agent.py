from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

load_dotenv()


class UniversitySearchOrEmailGen(BaseModel):
    # University Search
    name: str | None = Field(description="The name of the university.")
    location: str | None = Field(description="The location of the university.")
    budget: int | None = Field(description="The budget for the university.")
    programs: list[str] | None = Field(
        description="List of programs offered by the university.",
    )
    website: str | None = Field(description="The website of the university.")
    # Email
    subject: str | None = Field(description="The subject of the email.")
    body: str | None = Field(description="The body of the email.")
    recipient: str | None = Field(description="The recipient of the email.")
    sender: str | None = Field(description="The sender of the email.")


# class EmailGenerator(BaseModel):


root_agent = LlmAgent(
    name="university_search",
    description="An agent that helps finding universities based on user preferences.",
    model="gemini-2.0-flash",
    instruction="""You are a university search agent and email generator based on user needs.
    You will be given a user's preferences for a university and field, based on the past performance of related universities you have to suggest the best university with the all necessary details.
    Else, you will be given some text and you have to generate a response email with the necessary details.

    University Example:
    {
        "field": "Computer Science",
        "location": "California",
        "budget": 50000,
        "rank": 10
    }

    Email Example:
    {
        "subject": "Inquiry about Computer Science Program",
        "body": "Dear Admissions Office, I am interested in the Computer Science program at XYZ University. Could you please provide more information?\nThanks and Regards,\nJohn Doe",
        "recipient": "admissionsoffice@xyz.com",
        "sender": "john@doe.com"
    }
    """,
    output_schema=UniversitySearchOrEmailGen,
    output_key="result",
)
