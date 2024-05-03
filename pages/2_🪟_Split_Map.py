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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "ESA WorldCover 2020 S2 FCC"
        after = "ESA WorldCover 2020"
        m.split_map(
            left_layer=before, right_layer=after
        )
        m.center = (35.8, -86.0)
        m.zoom = 7

m.to_streamlit(height=700)
