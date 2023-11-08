import math

def calculate_circle_area(radius):
    try:
        if isinstance(radius, int) and radius > 0:
            area = math.pi * (radius ** 2)
            return area
        else:
            raise ValueError("Radius must be a positive integer.")
    except ValueError as e:
        return str(e)