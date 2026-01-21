# llm/value_extractor.py

import json
import re
from llm.llm_client import call_llm


def _clean_json(text: str) -> str:
    """
    Removes markdown code fences if Gemini returns them.
    """
    text = re.sub(r"```json|```", "", text)
    return text.strip()


def extract_value(arabic_text: str) -> dict:
    with open("prompts/value_prompt.txt", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{TEXT}}", arabic_text)

    response = call_llm(prompt, temperature = 0.2)
    response = _clean_json(response)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "value": "غير_محدد",
            "sub_values": []
        }
