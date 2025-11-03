from math import sqrt

def calculate_coordinates(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the approximate planar distance between two geographic coordinates
    in meters, ignoring the curvature of the Earth.

    Args:
        lat1: Latitude of the first point in degrees.
        lon1: Longitude of the first point in degrees.
        lat2: Latitude of the second point in degrees.
        lon2: Longitude of the second point in degrees.

    Returns:
        Approximate distance in meters between the two coordinates.
    """
    lat_scale = 111_320
    lon_scale = 111_320
    return sqrt(((lat2 - lat1) * lat_scale)**2 + ((lon2 - lon1) * lon_scale)**2)