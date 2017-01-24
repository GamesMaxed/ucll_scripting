def monotone(x, y, z):
    return (x <= y and y <= z) or (x >= y and y >= z)
