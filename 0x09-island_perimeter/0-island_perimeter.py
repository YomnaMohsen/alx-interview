#!/usr/bin/python3
"""Island preimeter module"""


# not depth 1st search as neetcode
def island_perimeter(grid):
    """return island perimeter"""

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 4
                if grid[i - 1][j] == 1:
                    count -= 2
                if grid[i][j-1] == 1:
                    count -= 2
    return count
