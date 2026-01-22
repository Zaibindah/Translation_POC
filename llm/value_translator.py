import json
from llm import call_gemini


def translate_values(value_data: dict) -> dict:
    """
    Translate extracted Arabic value + sub_values into English.
    """

    with open("prompts/value_translation.txt", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace(
        "{{JSON}}",
        json.dumps(value_data, ensure_ascii=False)
    )

    response = call_gemini(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "value": "",
            "sub_values": []
        }
