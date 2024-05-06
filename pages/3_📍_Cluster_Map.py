import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[35.8, -85.0], zoom=7)
        wells = "https://raw.githubusercontent.com/OmIImO05/wellwiz/main/csv/Oil%26Gas.csv"
        regions = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson"

        m.add_geojson(regions, layer_name="US Regions")
        m.add_points_from_xy(
            wells,
            x="Longitude",
            y="Latitude",
            color_column="County",
            #icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)