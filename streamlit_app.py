import importlib.util
from pathlib import Path

import streamlit as st


def load_module(path: Path):
    module_name = path.stem.replace(" ", "_")
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


st.set_page_config(
    page_title="Main App",
    page_icon="🚀",
    layout="centered",
)

st.title("Main page")
st.write("This page includes the story generator, hehe app, and oh-no app.")

story_module = load_module(Path(__file__).with_name("story generator.py"))
hehe_module = load_module(Path(__file__).with_name("hehe.py"))
oh_no_module = load_module(Path(__file__).with_name("oh no.py"))

tab1, tab2, tab3 = st.tabs(["Story Generator", "Hehe", "Oh No"])

with tab1:
    story_module.main()

with tab2:
    hehe_module.show()

with tab3:
    oh_no_module.show()


