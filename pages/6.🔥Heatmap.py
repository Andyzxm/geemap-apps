import streamlit as st
import watergeo.foliumap as watergeo
import requests
from streamlit_folium import folium_static

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://watergeo.streamlit.app/>
GitHub Repository: <https://github.com/Andyzxm/webmap_template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://images-platform.99static.com/7WcMmZPzGbVHYpeaib5FcOYR314=/100x100:900x900/500x500/top/smart/99designs-contests-attachments/122/122380/attachment_122380314"
st.sidebar.image(logo)

st.title("watergeo heat map")

# Fetch earthquake data
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson")
data = response.json()

# Extract latitude, longitude, and magnitude from data
heatmap_data = [[float(earthquake['geometry']['coordinates'][1]), float(earthquake['geometry']['coordinates'][0]), float(earthquake['properties']['mag'])] for earthquake in data['features']]

# Create a map
m = watergeo.Map()

# Add a heatmap to the map
m.add_heatmap(heatmap_data)

with st.expander("See source code"):
    with st.echo():
        m = watergeo.Map()
        m.add_heatmap(heatmap_data)

# Display the map in Streamlit
folium_static(m, height=700)