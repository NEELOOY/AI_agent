import os
os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "2000"
os.environ["OPENAI_API_KEY"] = "sk-kqwmAlddn5UP7Ts6Q8u7M74Ln68ZOBmN9qRVxMaY_4T3BlbkFJOCeEyk8XFe9BrGkT2kXSFLz_9Du5b2ds5dO4maOmAA"
import streamlit as st

# Set Streamlit to wide mode - this is the ONLY set_page_config() call we should have
st.set_page_config(
    layout="wide",
    page_title="Data Insights Dashboard",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

data_visualisation_page = st.Page(
    "./Pages/python_visualisation_agent.py", title="Data Visualisation", icon="📈"
)

pg = st.navigation(
    {
        "Visualisation Agent": [data_visualisation_page]
    }
)

pg.run()
