# llm/llm_client.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash"
)


def call_llm(prompt: str, temperature: float = 0.2) -> str:
    """
    Calls Gemini 2.5 Flash with strict text output.
    """

    generation_config = genai.types.GenerationConfig(
        temperature=0.0,
        top_p=0.9,
        max_output_tokens=512
    )

    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )
    print("HI")
    print(response)
    # Gemini may return multiple parts — we want plain text
    return response.text.strip()
