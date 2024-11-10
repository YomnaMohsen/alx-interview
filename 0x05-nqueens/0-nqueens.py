#!/usr/bin/python3
"""N queens module"""
import sys

# without trace !
# backtracking needs revision


def SolveNqueens(N):
    """function to solve n queens problem"""
    col = []
    pos_dig = []
    neg_dig = []
    res = []

    def solve_backtrack(r):
        """implement backtrack"""
        if r == N:
            res.append([[i, col[i]] for i in range(N)])
            return
        for c in range(N):
            if c in col or (r + c) in pos_dig or (r-c) in neg_dig:
                continue

            col.append(c)
            pos_dig.append(r + c)
            neg_dig.append(r - c)
            solve_backtrack(r + 1)
            col.pop()
            pos_dig.pop()
            neg_dig.pop()

    solve_backtrack(0)
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = int(sys.argv[1])
    res = SolveNqueens(N)
    for i in res:
        print(i)
