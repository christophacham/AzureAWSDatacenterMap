import folium

# AWS and Azure data center locations with hard-coded coordinates
aws_locations = [
    {"city": "Northern Virginia", "country": "USA", "latitude": 38.9, "longitude": -77.2},
    {"city": "Ohio", "country": "USA", "latitude": 40.0, "longitude": -83.0},
    {"city": "Northern California", "country": "USA", "latitude": 37.8, "longitude": -122.4},
    {"city": "Oregon", "country": "USA", "latitude": 45.5, "longitude": -122.7},
    {"city": "Montréal", "country": "Canada", "latitude": 45.5, "longitude": -73.6},
    {"city": "São Paulo", "country": "Brazil", "latitude": -23.55, "longitude": -46.63},
    {"city": "Ireland", "country": "Ireland", "latitude": 53.33, "longitude": -6.25},
    {"city": "Frankfurt", "country": "Germany", "latitude": 50.11, "longitude": 8.68},
    {"city": "London", "country": "UK", "latitude": 51.51, "longitude": -0.13},
    {"city": "Paris", "country": "France", "latitude": 48.85, "longitude": 2.35},
    {"city": "Stockholm", "country": "Sweden", "latitude": 59.33, "longitude": 18.06},
    {"city": "Milan", "country": "Italy", "latitude": 45.46, "longitude": 9.19},
    {"city": "Cape Town", "country": "South Africa", "latitude": -33.92, "longitude": 18.42},
    {"city": "Bahrain", "country": "Bahrain", "latitude": 26.07, "longitude": 50.55},
    {"city": "Singapore", "country": "Singapore", "latitude": 1.35, "longitude": 103.82},
    {"city": "Tokyo", "country": "Japan", "latitude": 35.68, "longitude": 139.69},
    {"city": "Osaka", "country": "Japan", "latitude": 34.69, "longitude": 135.50},
    {"city": "Seoul", "country": "South Korea", "latitude": 37.56, "longitude": 126.97},
    {"city": "Mumbai", "country": "India", "latitude": 19.08, "longitude": 72.88},
    {"city": "Sydney", "country": "Australia", "latitude": -33.87, "longitude": 151.21},
    {"city": "Melbourne", "country": "Australia", "latitude": -37.81, "longitude": 144.96},
    {"city": "Jakarta", "country": "Indonesia", "latitude": -6.21, "longitude": 106.85},
    {"city": "Hong Kong", "country": "Hong Kong", "latitude": 22.32, "longitude": 114.17},
    {"city": "São Paulo", "country": "Brazil", "latitude": -23.55, "longitude": -46.63},
    {"city": "Hyderabad", "country": "India", "latitude": 17.38, "longitude": 78.48},
    {"city": "Beijing", "country": "China", "latitude": 39.90, "longitude": 116.40},
    {"city": "Ningxia", "country": "China", "latitude": 38.47, "longitude": 106.27}
]


azure_locations = [
    {"city": "Central US", "country": "USA", "latitude": 41.6, "longitude": -93.6},
    {"city": "East US", "country": "USA", "latitude": 37.5, "longitude": -79.5},
    {"city": "East US 2", "country": "USA", "latitude": 36.7, "longitude": -79.5},
    {"city": "North Central US", "country": "USA", "latitude": 41.8, "longitude": -87.6},
    {"city": "South Central US", "country": "USA", "latitude": 29.4, "longitude": -98.5},
    {"city": "West US", "country": "USA", "latitude": 37.7, "longitude": -122.4},
    {"city": "West US 2", "country": "USA", "latitude": 47.6, "longitude": -122.2},
    {"city": "Canada Central", "country": "Canada", "latitude": 43.7, "longitude": -79.4},
    {"city": "Brazil South", "country": "Brazil", "latitude": -23.55, "longitude": -46.63},
    {"city": "North Europe", "country": "Ireland", "latitude": 53.33, "longitude": -6.25},
    {"city": "West Europe", "country": "Netherlands", "latitude": 52.37, "longitude": 4.90},
    {"city": "UK South", "country": "UK", "latitude": 51.5, "longitude": -0.13},
    {"city": "UK West", "country": "UK", "latitude": 53.48, "longitude": -3.03},
    {"city": "France Central", "country": "France", "latitude": 48.85, "longitude": 2.35},
    {"city": "Germany West Central", "country": "Germany", "latitude": 50.11, "longitude": 8.68},
    {"city": "Switzerland North", "country": "Switzerland", "latitude": 47.38, "longitude": 8.54},
    {"city": "Switzerland West", "country": "Switzerland", "latitude": 46.20, "longitude": 6.15},
    {"city": "Norway East", "country": "Norway", "latitude": 59.91, "longitude": 10.75},
    {"city": "Norway West", "country": "Norway", "latitude": 58.97, "longitude": 5.73},
    {"city": "Japan East", "country": "Japan", "latitude": 35.68, "longitude": 139.69},
    {"city": "Japan West", "country": "Japan", "latitude": 34.69, "longitude": 135.50},
    {"city": "Korea Central", "country": "South Korea", "latitude": 37.56, "longitude": 126.97},
    {"city": "Korea South", "country": "South Korea", "latitude": 35.18, "longitude": 129.07},
    {"city": "Australia East", "country": "Australia", "latitude": -33.87, "longitude": 151.21},
    {"city": "Australia Southeast", "country": "Australia", "latitude": -37.81, "longitude": 144.96},
    {"city": "East Asia", "country": "Hong Kong", "latitude": 22.32, "longitude": 114.17},
    {"city": "Southeast Asia", "country": "Singapore", "latitude": 1.35, "longitude": 103.82},
    {"city": "India Central", "country": "India", "latitude": 18.52, "longitude": 73.85},
    {"city": "India South", "country": "India", "latitude": 12.97, "longitude": 77.59},
    {"city": "India West", "country": "India", "latitude": 19.08, "longitude": 72.88},
    {"city": "China East", "country": "China", "latitude": 31.23, "longitude": 121.47},
    {"city": "China North", "country": "China", "latitude": 39.90, "longitude": 116.40},
    {"city": "UAE North", "country": "UAE", "latitude": 25.27, "longitude": 55.30},
    {"city": "South Africa North", "country": "South Africa", "latitude": -25.73, "longitude": 28.22}
]


custom_locations = [
    {"city": "New York", "country": "USA", "latitude": 40.71, "longitude": -74.01},
    {"city": "Paris", "country": "France", "latitude": 48.85, "longitude": 2.35},
    {"city": "Tokyo", "country": "Japan", "latitude": 35.68, "longitude": 139.69},
    {"city": "Sydney", "country": "Australia", "latitude": -33.87, "longitude": 151.21},
    {"city": "Mumbai", "country": "India", "latitude": 19.08, "longitude": 72.88}
]


# Function to add markers to the map
def add_markers(map_obj, locations, color):
    for loc in locations:
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            popup=f"{loc['city']}, {loc['country']}",
            icon=folium.Icon(color=color)
        ).add_to(map_obj)


# Create a map object
world_map = folium.Map(location=[20, 0], zoom_start=2)

# Add AWS data centers in orange
add_markers(world_map, aws_locations, 'orange')

# Add Azure data centers in blue
add_markers(world_map, azure_locations, 'blue')

# Add custom locations in pink
add_markers(world_map, custom_locations, 'pink')

# Save the map to an HTML file
world_map.save("data_centers_map.html")
