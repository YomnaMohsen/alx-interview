#!/usr/bin/python3
"""Island preimeter module"""
from typing import List


# need more trace
def island_perimeter(grid: List[List[int]]) -> int:
    """return island perimeter"""
    visit = set()

    def dfs(i, j):
        """helper function using depth 1st search"""
        if i >= len(grid) or j >= len(grid[0]) or \
           i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0
        visit.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i, j - 1)
        perim += dfs(i + 1, j)
        perim += dfs(i - 1, j)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)