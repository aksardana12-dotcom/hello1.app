from pathlib import Path
import runpy

script_path = Path(__file__).with_name("streamlit_app.py")
runpy.run_path(str(script_path), run_name="__main__")