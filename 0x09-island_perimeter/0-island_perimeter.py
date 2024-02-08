#!/usr/bin/python3

"""
Create a function def island_perimeter(grid): that returns
the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island
    """
    row_len = len(grid)
    column_len = len(grid[0])

    perimeter = 0
    connections = 0

    for x in range(0, row_len):
        for y in range(0, column_len):

            if grid[x][y] == 1:
                perimeter += 4
                if x != 0 and grid[x - 1][y]:
                    connections += 1
                if y != 0 and grid[x][y - 1]:
                    connections += 1

    return perimeter - (connections * 2)
