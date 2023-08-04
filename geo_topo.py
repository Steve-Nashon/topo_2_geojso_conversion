
import json
from pytopojson import topology


# Create Topology object
topology_ = topology.Topology()

# Read the geojson file
with open("worldmap_geojson.geojson", 'r') as f:
    test_geojson = json.load(f)
    # Call it using a GeoJSON (dict) object, a name for the object and a quantization value (optional)
    topojson = topology_({"object_name": test_geojson})

# Write the created topojson object into a json file
with open('worldmap_topojson.json', 'w') as dest:
    dest.write(json.dumps(topojson))





