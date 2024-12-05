#!/usr/bin/python3
"""Island preimeter module"""


# not depth 1st search as neetcode
def island_perimeter(grid):
    """return island perimeter"""

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                count += 4
                if row > 0 and grid[row - 1][col] == 1:
                    count -= 2
                if col > 0 and grid[row][col-1] == 1:
                    count -= 2
    return count
