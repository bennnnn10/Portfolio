def calculate_triangle_area(base, height):
    try:
        if base >= 0 and height >= 0:
            area = 0.5 * base * height
            return area
        else:
            raise ValueError("Base and height need to be non-negative numbers.")
    except ValueError as e:
        return str(e)