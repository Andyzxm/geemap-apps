import streamlit as st
import streamlit_folium as folium_st
import pandas as pd
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

st.title("Choropleth Map")

# Create a pandas DataFrame with income data
# Create a pandas DataFrame with income data for all states
income = pd.DataFrame({
    'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
    'Income': [43296, 73181, 51492, 42336, 67169, 65458, 74168, 63436, 50883, 52977, 74511, 52225, 62992, 52182, 58570, 56422, 48375, 45727, 55425, 78916, 77385, 54909, 68388, 43529, 53560, 50801, 59116, 57598, 73381, 79363, 46718, 64894, 52413, 61285, 54021, 50051, 60212, 59445, 61043, 50570, 54126, 48708, 59570, 68358, 57808, 68766, 70116, 44921, 59305, 60938]  # Hypothetical income data for all states
})

with st.expander("See source code for choropleth map"):
    with st.echo():
        # Create an instance of the FoliumMap class from the watergeo package
        fmap = watergeo.Map()

        # Add a choropleth layer to the map
        fmap.add_choropleth(
            geo_data='https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json',
            data=income,
            columns=['State', 'Income'],
            key_on='feature.properties.name',
            fill_color='BuGn',  # You can change the color scheme
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Income (in US dollars)'
        )

# Display the map
folium_st.folium_static(fmap)