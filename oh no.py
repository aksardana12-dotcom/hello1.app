import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Language Translator", page_icon="(╯°□°）╯︵ ┻━┻")
st.title("AI Language Translator")
st.write("Translate English into different languages.")

@st.cache_resource

def load_model():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-fr"
    )
translator = load_model()

languages = {
    "French": "Helsinki-NLP/opus-mt-en-fr"
    "German": "Helsinki-NLP/opus-mt-en-de"
    "Spanish": "Helsinki-NLP/opus-mt-en-es"
    "Pizza": "Helsinki-NLP/opus-mt-en-it"
    "Japanese": "Helsinki-NLP/opus-mt-en-jp"
}

langauge = st.selectbox(
    "Select Lnaguage",
    list(languages.keys())
)

text = st.text_aea("enter english")

if st.button("translate"):
    with st.spinner("nice spinny thing"):

        translator = pipeline(
            "translation",
            model= languages[language]
        )

        resut = translator(text)

        st.success(result[0]["translation_text"])

def show():
    st.subheader("Oh no app")
    st.warning("This is the oh-no app.")
    if st.button("Trigger warning"):
        st.error("Oh no! Something happened.")

show()