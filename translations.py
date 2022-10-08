from math import sin, cos, pi, acos
# Function to rotate a point from a given angle:


def rotate(point, alpha):
    return [point[0]*cos(alpha)-point[1]*sin(alpha), point[0]*sin(alpha)+point[1]*cos(alpha)]

# Function to convert degrees to radians


def deg_to_rad(x):
    return x * pi/180

# Function to convert a cartesian coordinate into a
# point of the form [longitude, latitude]


def cartesian_to_geo(x, y):
    return [x/(111.32*cos(deg_to_rad(y / 111.32))), y/111.32]

# Function to convert a geographical coordinate into a
# point of the form [x, y], receives a point in format [latitude, longitude]


def geo_to_cartesian(p):
    return [p[1]*111.32*cos(deg_to_rad(p[0])), 111.32*p[0]]

# Function to make a translation over a geographical point
# start and end are points with coordinates defined as [lon, lat]


def translate(start, end):
    return [start[0] + end[0], start[1] + end[1]]
