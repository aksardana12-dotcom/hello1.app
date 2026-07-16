import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="(╯°□°）╯︵ ┻━┻",
)
st.title("AI Language Translator")
st.write("Translate English into different languages.")


@st.cache_resource
def load_model(model_name):
    return pipeline("translation", model=model_name)


languages = {
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Italian": "Helsinki-NLP/opus-mt-en-it",
    "Japanese": "Helsinki-NLP/opus-mt-en-ja",
}


language = st.selectbox("Select Language", list(languages.keys()))
text = st.text_area("Enter English")

if st.button("Translate"):
    with st.spinner("Translating..."):
        translator = load_model(languages[language])
        result = translator(text)
        st.success(result[0]["translation_text"])


def show():
    st.subheader("Oh no app")
    st.warning("This is the oh-no app.")
    if st.button("Trigger warning"):
        st.error("Oh no! Something happened.")


show()