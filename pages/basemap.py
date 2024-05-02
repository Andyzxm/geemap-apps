import streamlit as st
import watergeo.foliumap as watergeo

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://watergeo.streamlit.app/>
GitHub Repository: <https://github.com/Andyzxm/webmap_template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://images-platform.99static.com/7WcMmZPzGbVHYpeaib5FcOYR314=/100x100:900x900/500x500/top/smart/99designs-contests-attachments/122/122380/attachment_122380314"
st.sidebar.image(logo)

st.title("watergeo map")

with st.expander("See source code"):
    with st.echo():
        m = watergeo.Map()
        m.add_basemap("OpenTopoMap")

m.to_streamlit(height=700)