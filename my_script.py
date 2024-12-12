import geopandas as gpd

# Example: Create a simple GeoDataFrame
data = {'geometry': ['POINT (1 1)', 'POINT (2 2)', 'POINT (3 3)']}
gdf = gpd.GeoDataFrame(data)

# Print GeoDataFrame
print(gdf)
python my_script.py
