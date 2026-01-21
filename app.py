import streamlit as st
from llm.value_extractor import extract_value
from llm.translator import translate_text

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
            value_result = extract_value(arabic_text)
            translation = translate_text(arabic_text)

        st.subheader("Dominant Ethical Value")
        st.json(value_result)

        st.subheader("English Translation")
        st.write(translation)
