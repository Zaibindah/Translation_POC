import streamlit as st
from llm import extract_value, translate_values, translate_text


st.set_page_config(
    page_title="Arabic Ethical Value Analyzer",
    layout="centered"
)

st.title("📜 Arabic Ethical Value Analyzer (POC)")

arabic_text = st.text_area(
    "Enter Arabic text",
    height=220,
    placeholder="اكتب النص العربي هنا..."
)

if st.button("Analyze"):
    if not arabic_text.strip():
        st.error("Please enter Arabic text.")
    else:
        with st.spinner("Analyzing..."):
            # 1️⃣ Extract ethical value (Arabic)
            value_result = extract_value(arabic_text)

            # 2️⃣ Translate full Arabic text (existing behavior)
            translation = translate_text(arabic_text)

            # 3️⃣ Translate extracted values + sub-values (NEW)
            translated_values = translate_values(value_result)

        # ----------- OUTPUT SECTIONS -----------

        st.subheader("🧭 Dominant Ethical Value (Arabic)")
        st.json(value_result)

        st.subheader("🌍 Dominant Ethical Value (English)")
        st.json(translated_values)

        st.subheader("📖 English Translation of Input Text")
        st.write(translation)
