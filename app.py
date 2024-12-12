import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
@st.cache_data
def load_data():
    # Replace with your path to the geospatial data (e.g., GeoJSON, shapefile, etc.)
    gdf = gpd.read_file('data/your_geo_data.geojson')  # Change this to your file
    return gdf

# Display map function
def plot_map(gdf):
    # Plot the map
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, color='lightblue', edgecolor='black')
    ax.set_title("Geospatial Data Map", fontsize=16)
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("Geospatial Data Viewer")
    
    st.write("""
    This app visualizes geospatial data using Streamlit and GeoPandas.
    """)
    
    # Load data
    gdf = load_data()

    # Display map
    st.write("Map of the Geospatial Data:")
    plot_map(gdf)

    # Optionally, show some information about the data
    st.write("Data Info:")
    st.write(gdf.head())  # Show first few rows of the data

if __name__ == "__main__":
    main()
