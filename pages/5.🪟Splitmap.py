import streamlit as st
import streamlit_folium as folium_st
import watergeo.foliumap as watergeo
import ee

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://watergeo.streamlit.app/>
GitHub Repository: <https://github.com/Andyzxm/webmap_template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://images-platform.99static.com/7WcMmZPzGbVHYpeaib5FcOYR314=/100x100:900x900/500x500/top/smart/99designs-contests-attachments/122/122380/attachment_122380314"
st.sidebar.image(logo)

st.title("Split Map")

# Initialize the Earth Engine library.
ee.Initialize()

# Define the Earth Engine layers.
layer1 = ee.Image('USGS/SRTMGL1_003')
layer2 = ee.Image('CGIAR/SRTM90_V4')

# Define the visualization parameters.
vis_params1 = {
    'min': 0,
    'max': 3000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
}
vis_params2 = {
    'min': 0,
    'max': 6000,
    'palette': ['0000CC', 'CCFFFF', 'FFFFCC', 'CC0000']
}

with st.expander("See source code for split map"):
    with st.echo():
        # Create a map.
        m = watergeo.Map()

        # Create a split map.
        split_m = m.split_map(layer1, layer2, vis_params1, vis_params2)

# Display the split map in Streamlit.
folium_st.folium_static(split_m)


# Second example
st.title("Split Map Example 2")

# Define the Earth Engine layers.
surface_water = watergeo.ee.Image("JRC/GSW1_2/GlobalSurfaceWater")
appacounties = watergeo.ee.FeatureCollection('projects/ee-ut-andyzhang/assets/appawateruse')
clipped_surface_water = surface_water.clipToCollection(appacounties)

# Set thresholds for 'occurrence'
threshold_80 = 80
threshold_20 = 20

vis_params_80 = {
    'bands': ['occurrence'],
    'palette': ['white', 'blue']
}
vis_params_20 = {
    'bands': ['occurrence'],
    'palette': ['white', 'blue']
}

# Consider only those pixels as reliable water sources which have an 'occurrence' greater than the thresholds
reliable_water_80 = clipped_surface_water.gte(threshold_80).selfMask()
reliable_water_20 = clipped_surface_water.gte(threshold_20).selfMask()

with st.expander("See source code for split map example 2"):
    with st.echo():
        # Create a map.
        Map = watergeo.Map()

        # Create a split map.
        split_m2 = Map.split_map(reliable_water_80, reliable_water_20, vis_params_80, vis_params_20)

# Display the split map.
folium_st.folium_static(split_m2)