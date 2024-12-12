# Import necessary libraries
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# Function to load geospatial data (for example, a shapefile)
def load_data(shapefile_path):
    try:
        # Load the shapefile into a Geopandas dataframe
        gdf = gpd.read_file(shapefile_path)
        return gdf
    except Exception as e:
        st.error(f"Error loading shapefile: {e}")
        return None

# Function to plot the geospatial data
def plot_map(gdf):
    try:
        # Plotting the geospatial data using Matplotlib
        ax = gdf.plot(figsize=(10, 6), cmap='viridis')
        plt.title('Geospatial Data')
        st.pyplot(fig=plt.gcf())  # Display the plot in the Streamlit app
    except Exception as e:
        st.error(f"Error plotting the map: {e}")

# Streamlit app setup
def main():
    st.title("Geospatial Data Viewer")

    # Upload shapefile
    uploaded_file = st.file_uploader("Upload a shapefile", type=["shp"])
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with open("/tmp/temp_shapefile.shp", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Load and display the shapefile data
        gdf = load_data("/tmp/temp_shapefile.shp")
        
        if gdf is not None:
            # Display dataframe and plot map
            st.write("Geospatial Data")
            st.dataframe(gdf.head())  # Display first few rows of the dataframe
            plot_map(gdf)
        else:
            st.warning("No data available to plot.")
    
if __name__ == "__main__":
    main()

