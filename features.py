import io
import json
# Function to create a point array structure


def point(latitude, longitude):
    return [round(longitude, 7), round(latitude, 7)]

# Function to create a line array structure


def line(points):
    return [points]

# Function to create a polygon structure
# It receives an array of points and the first is assumed to be the point
# where the polygon closes


def polygon(point_array):
    polygon = point_array.copy()
    polygon.append(point_array[0])

    return [polygon]

# Function to create Points, Lines, Polygons, or any other GeoJSON geometry primitive (not GeometryCollections)
# Geometry Object
# Parameters are: type (i.e "Point", "MultiLineString"), coordinates (array with coordinate information)


def create_geometry_object(type, coordinates):
    return {"type": type, "coordinates": coordinates}

# Creates basic GeoJson feature from a geometry object and a dictionary with the feature's properties


def create_feature(geometry_object, properties):
    return {"type": "Feature", "geometry": geometry_object, "properties": properties}

# Creates a geometry collection from an array of geometry_objects


def create_geometry_collection(geometries):
    return {"type": "GeometryCollection", "geometries": geometries}

# Creates a feature collection from an array of feature objects


def create_feature_collection(features):
    return {"type": "FeatureCollection", "features": features}


def save_geojson(geojson, filename):
    with open(filename, 'w') as f:
        json.dump(geojson, f)
