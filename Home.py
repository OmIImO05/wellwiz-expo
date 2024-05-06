import streamlit as st
import wellwiz.folium as wellwiz

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://homepy-5jkvf5cmrtwn7hpdntlxap.streamlit.app/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://cdn.dribbble.com/users/282075/screenshots/2669824/media/3d6b4f00f002736d03d0fb2fae793d84.gif"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Well Risk")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://homepy-5jkvf5cmrtwn7hpdntlxap.streamlit.app/).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://homepy-5jkvf5cmrtwn7hpdntlxap.streamlit.app/) or [use it as a template](https://homepy-5jkvf5cmrtwn7hpdntlxap.streamlit.app//generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""


st.markdown(markdown)

m = wellwiz.Map(minimap_control=True)
m.add_basemap('OpenTopoMap')
m.to_streamlit(height=500)