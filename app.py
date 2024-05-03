import streamlit as st
import geemap.foliumap as geemap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://watergeo.streamlit.app/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://images-platform.99static.com/7WcMmZPzGbVHYpeaib5FcOYR314=/100x100:900x900/500x500/top/smart/99designs-contests-attachments/122/122380/attachment_122380314"
st.sidebar.image(logo)

# Customize page title
st.title("Watergeo Web App")

st.markdown(
    """
    This multipage app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [watergeo](https://andyzxm.github.io/watergeo/). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/geemap-apps).
    """
)

st.header("Key Features")

markdown = """
(more to be included in the future):
- Interactive maps with basemap dropdown lists
- Data Visualization with vectors and rasters
- Google Earth Engine implementation for spatial analysis
- Split map 
- Time series
- Zonal statistics

"""

st.markdown(markdown)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)