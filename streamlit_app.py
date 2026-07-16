import streamlit as st
import random
import math
from pathlib import Path
import runpy

st.title("🎈 this is a ballon")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

script_path = Path(__file__).with_name("story generator.py")
runpy.run_path(str(script_path), run_name="__main__")


