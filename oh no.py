import streamlit as st

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="(╯°□°）╯︵ ┻━┻",
)
st.title("AI Language Translator")
st.write("Translate English into different languages.")

# Simple built-in demo translations so the app works without heavy ML packages.
demo_translations = {
    "French": {
        "hello": "bonjour",
        "world": "monde",
        "thank you": "merci",
        "goodbye": "au revoir",
    },
    "German": {
        "hello": "hallo",
        "world": "Welt",
        "thank you": "danke",
        "goodbye": "auf Wiedersehen",
    },
    "Spanish": {
        "hello": "hola",
        "world": "mundo",
        "thank you": "gracias",
        "goodbye": "adiós",
    },
    "Italian": {
        "hello": "ciao",
        "world": "mondo",
        "thank you": "grazie",
        "goodbye": "arrivederci",
    },
    "Japanese": {
        "hello": "こんにちは",
        "world": "世界",
        "thank you": "ありがとうございます",
        "goodbye": "さようなら",
    },
}

def translate_text(text, language):
    normalized = text.strip().lower()
    if normalized in demo_translations[language]:
        return demo_translations[language][normalized]
    return f"[{language}] {text}"

languages = list(demo_translations.keys())
language = st.selectbox("Select Language", languages)
text = st.text_area("Enter English")

if st.button("Translate"):
    translated = translate_text(text, language)
    st.success(translated)

def show():
    st.subheader("Oh no app")
    st.warning("This is the oh-no app.")
    if st.button("Trigger warning"):
        st.error("Oh no! Something happened.")

show()