#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.
"""

import sys


class N_queens:
    """Class N_queens used to solve the N queens problem"""
    def __init__(self, N):
        """Initializing"""
        self.N = N
        self.solution = []

    def solver(self):
        """
        Initialize wheere the queens are before starting
        """
        queens = [-1] * self.N
        # pass the queens list starting with row at index 0
        self.queens_algo(queens, 0)
        return self.solution

    def queens_algo(self, queens, row):
        """
        Recursive algorithm that attempts to place
        the queens on the chessboard
        """
        if (row == self.N):
            self.sum_solution(queens)
            return

        for column in range(self.N):
            if self.its_safe(queens, column, row):
                queens[row] = column
                # if its safe, take note of config and then
                # move to the next row
                self.queens_algo(queens, row + 1)
                # to reset its position and look for more possible
                # configurations or solution
                queens[row] = -1

    def its_safe(self, queens, column, row):
        """
        Function to determine if its safe to place a queen in that
        specific position
        A queen placed where it is not safe will result in the
        queens attacking each other
        """
        for a in range(row):
            if queens[a] == column or queens[a] - a == column - row\
                  or queens[a] + a == column + row:
                return False
        return True

    def sum_solution(self, queens):
        """adds up the total solutions found"""
        total_solution = []

        for row in range(self.N):
            total_solution.append([row, queens[row]])
        self.solution.append(total_solution[:])


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if (N < 4):
        print("N must be at least 4")
        sys.exit(1)

    # solve the n queens puzzle
    n_queens_puzzle = N_queens(N)
    n_queens_puzzle.solver()

    # print result
    for result in n_queens_puzzle.solution:
        print(result)


if __name__ == "__main__":
    main()
