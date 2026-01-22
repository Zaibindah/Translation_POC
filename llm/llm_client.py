import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Read API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env")

# Configure Gemini (OLD SDK)
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash-lite-preview-09-2025"
)

def clean_markdown_json(text: str) -> str:
    """
    Remove markdown ```json ``` wrappers
    """
    lines = text.strip().splitlines()
    lines = [
        line for line in lines
        if not re.match(r'^```(?:json)?$', line.strip(), re.IGNORECASE)
    ]
    return "\n".join(lines).strip()


def call_gemini(prompt: str) -> str:
    """
    Calls Gemini Flash and returns raw text output
    """

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.0,
            "top_p": 0.9,
            "max_output_tokens": 2048
        }
    )

    return clean_markdown_json(response.text)
