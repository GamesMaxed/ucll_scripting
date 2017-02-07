def add_bombcounts(grid):
    width = len(grid[0])
    height = len(grid)
    
    def is_inside(p):
        x, y = p
        return x in range(0, width) and y in range(0, height)
    
    def around(p):
        x, y = p
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                q = (x + dx, y + dy)
                
                if is_inside(q) and p != q:
                    yield q

    for x in range(0, width):
        for y in range(0, height):
            if grid[y][x] != 'B':
                count = 0

                for qx, qy in around((x,y)):
                    if grid[qy][qx] == 'B':
                        count += 1

                grid[y][x] = count
