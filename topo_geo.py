
import json
from pytopojson import feature


# Read the Topojson file
with open("worldmap_topojson.json", 'r') as f:
    test_topojson = json.load(f)
 

# Write the geojson to a file
with open('worldmap_geojson_2.json', 'w') as dest:
    # Create a feature object
    feat = feature.Feature()

    # Call the feature object and pass the topojson file plus all its objects
    test_geojson = feat(test_topojson,"object_name")
    dest.write(json.dumps(test_geojson))





