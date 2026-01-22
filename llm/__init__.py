"""
LLM module for Arabic Ethics POC

This package contains:
- llm_client: Gemini client wrapper
- value_extractor: Ethical value + sub-value extraction
- translator: Arabic → English translation
"""

from llm.llm_client import call_gemini
from .value_extractor import extract_value
from llm.value_translator import translate_values
from .translator import translate_text

__all__ = [
    "call_gemini",
    "extract_value",
    "translate_text",
]
