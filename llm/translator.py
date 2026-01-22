from llm import call_gemini

def translate_text(arabic_text: str) -> str:
    with open("prompts/translation_prompt.txt", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{TEXT}}", arabic_text)

    response = call_gemini(
        prompt=prompt
    )

    return response.strip()
