from features import *
from math import cos, pi, sin, atan

from translations import cartesian_to_geo, geo_to_cartesian, rotate, translate
# Function to define an equilateral triangle as a Geometry Collection
# that goes from a center point and has a radius in kilometers


def create_eq_triangle(lat, lon, r=20):
    center = point(lat, lon)

    up_direction = cartesian_to_geo(0, r)
    left_direction = cartesian_to_geo(-r*cos(pi/6), -r/2)
    right_direction = cartesian_to_geo(r*cos(pi/6), -r/2)

    up_vertex = translate(center, up_direction)
    left_vertex = translate(center, left_direction)
    right_vertex = translate(center, right_direction)

    triangle = polygon([up_vertex, left_vertex, right_vertex])
    center_point = create_geometry_object("Point", center)
    triangle_polygon = create_geometry_object("Polygon", triangle)

    return [create_feature(center_point, {}), create_feature(triangle_polygon, {})]

# Function to define an object that represents a zigzag from a point
# the function receives a direction angle, an starting point, the angle between lines
# and a count of the number of lines


def create_zigzag(start_point, angle, count, l):
    points = [start_point]
    angle = pi - angle
    vec = [l*cos((pi-angle/2)), l*sin((pi-angle/2))]
    vec = cartesian_to_geo(vec[0], vec[1])
    for i in range(count):
        next_point = translate(points[i], vec)
        points.append(next_point)
        vec[1] = -vec[1]
    return create_geometry_object("LineString", points)


def multi_geometry_zigzag(start_point, angle, count, l, r):
    base_zig_zag = create_zigzag(start_point, angle, count, l)
    triangles_array = []
    for p in base_zig_zag["coordinates"]:
        triangles_array += create_eq_triangle(p[1], p[0], r)
    triangles_array.append(create_feature(create_geometry_object(
        "LineString", base_zig_zag["coordinates"]), {}))
    return create_feature_collection(triangles_array)


lat = 13.681116987998028
lon = -89.2358381465663

geojson = multi_geometry_zigzag(point(lat, lon), pi/3, 5, 1, 0.1)
geojson2 = create_feature_collection(create_eq_triangle(lat, lon, 30))
save_geojson(geojson, 'zigzags.geojson')
save_geojson(geojson2, 'triangle.geojson')
