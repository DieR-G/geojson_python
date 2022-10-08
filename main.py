from features import *
import json

feature1 = create_feature(
    create_geometry_object(
        "Point", [102.0, 0.5]
    ),
    {
        "name": "point1",
        "status": "active"
    }
)

feature2 = create_feature(
    create_geometry_object(
        "LineString", [[102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]]
    ),
    {
        "name": "line1",
        "status": "active"
    }
)

feature3 = create_feature(
    create_geometry_object(
        "Polygon",
        [
            [
                [100.0, 0.0], [101.0, 0.0], [
                    101.0, 1.0], [100.0, 1.0], [100.0, 0.0]
            ]
        ]
    ),
    {
        "prop0": "value0"
    }
)

geojson = create_feature_collection([feature1, feature2, feature3])

save_geojson(geojson, "wikipediageojson.geojson")
