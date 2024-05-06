import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://homepy-5jkvf5cmrtwn7hpdntlxap.streamlit.app/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://cdn.dribbble.com/users/282075/screenshots/2669824/media/3d6b4f00f002736d03d0fb2fae793d84.gif"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://raw.githubusercontent.com/OmIImO05/wellwiz/main/csv/Oil%26Gas.csv"
        m = leafmap.Map(center=[35.8, -86.0], zoom=8)
        m.add_heatmap(
            filepath,
            latitude="Latitude",
            longitude="Longitude",
            value="Elevation",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
