import streamlit as st
import ee
pip install -r my_project/requirements.txt
import watergeo.foliumap as watergeo

markdown = """
Web App URL: <https://watergeo.streamlit.app/>
GitHub Repository: <https://github.com/Andyzxm/webmap_template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://images-platform.99static.com/7WcMmZPzGbVHYpeaib5FcOYR314=/100x100:900x900/500x500/top/smart/99designs-contests-attachments/122/122380/attachment_122380314"
st.sidebar.image(logo)

st.title("Google Earth Engine") 

# Initialize Earth Engine
ee.Initialize()

with st.expander("See source code"):
    with st.echo():
        # Create a geemap map
        m = watergeo.Map(center=[40, -100], zoom=4)

        # Add Earth Engine data or layers to the map
        image = ee.Image('JRC/GSW1_3/GlobalSurfaceWater')
        vis_params = {'bands': ['occurrence'], 'min': 0, 'max': 100, 'palette': ['blue']}
        m.add_ee_layer(image, vis_params, 'Global Surface Water')

# Display the map in Streamlit
m.to_streamlit()