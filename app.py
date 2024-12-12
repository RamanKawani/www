import streamlit as st
import geopandas as gpd

# Load a shapefile (example)
@st.cache
def load_shapefile():
    # Replace with the actual path to your shapefile
    shapefile_path = 'path_to_your_shapefile.shp'
    return gpd.read_file(shapefile_path)

# Main Streamlit app
def main():
    st.title('Geospatial Data with GeoPandas and Streamlit')

    try:
        # Load shapefile data
        gdf = load_shapefile()
        st.write(gdf)

        # Optionally, plot the data
        st.map(gdf)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

