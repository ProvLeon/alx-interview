def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    print(rows, cols)
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Check the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check the cell to the left
                    perimeter -= 2

    return perimeter


