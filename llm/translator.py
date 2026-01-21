from llm.llm_client import call_llm

def translate_text(arabic_text: str) -> str:
    with open("prompts/translation_prompt.txt", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{TEXT}}", arabic_text)

    response = call_llm(
        prompt=prompt,
        temperature=0.3
    )

    return response.strip()
