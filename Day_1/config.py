import os
from dotenv import load_dotenv
from openai import OpenAI

# Load values from .env
load_dotenv(override=True)

# Read configuration
PROVIDER = os.getenv("PROVIDER")
MODEL = os.getenv("MODEL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create LLM client
if PROVIDER == "groq":
    client = OpenAI(
        api_key=GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1"
    )
else:
    raise ValueError(f"Unsupported provider: {PROVIDER}")

# Private course data
COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

# Questions used throughout the lab
QUESTIONS = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Write a two-line welcome message for new AI students."
]