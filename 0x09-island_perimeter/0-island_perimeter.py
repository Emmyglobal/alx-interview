#!/usr/bin/python3
"""Module that calculates the perimeter of the island
described in grid.
"""


def island_perimeter(grid):
    """Returns the perimetr of the island"""

    perimeter = 0
    # Loops through the grid cell by cell.
    for n in range(len(grid)):
        for m in range(len(grid[n])):
            # If the cell is not 0.
            if grid[n][m]:
                # Increments the perimeter by counting
                # the water around the cell
                perimeter += num_water(grid, n, m)

    return perimeter


def num_water(grid, n, m):
    """Returns the number of water a cell has in a grid."""

    # num increases if water is detected.
    num = 0
    # First Condition to check water on the cell's top side.
    if n <= 0 or not grid[n - 1][m]:
        num += 1
        # print(f"first if, {i},{j}")
    # Second Condition to check water on the cell's left side.
    if m <= 0 or not grid[n][m - 1]:
        num += 1
        # print(f"second if, {i},{j}")
    # Third Condition checks water on the cell's left side
    # and the if it's at the end grid.

    if m >= len(grid[n]) - 1 or not grid[n][m - 1]:
        num += 1
        # print(f"third if, {i},{j}")
    # Fourth Condition checks water on the cell's down side.
    if n >= len(grid) - 1 or not grid[n + 1][m]:
        num += 1
        # print(f"fourth if, {i},{j}")

    return num
