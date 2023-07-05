#!/usr/bin/python3
import sys

def is_safe(board, x, y, N):
    """
    Check if a queen can be placed at a given position on the board without
    attacking any other queens.
    
    Args:
        board (list): The chessboard represented as a 2D list.
        x (int): The x-coordinate (row index) of the position to check.
        y (int): The y-coordinate (column index) of the position to check.
        N (int): The size of the chessboard.
    
    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check the row on the left side
    for i in range(y):
        if board[x][i] == 1:
            return False
    
    # Check the upper diagonal on the left side
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the lower diagonal on the left side
    for i, j in zip(range(x, N), range(y, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    Recursive utility function to solve the N queens problem.
    
    Args:
        board (list): The chessboard represented as a 2D list.
        col (int): The current column to place a queen in.
        N (int): The size of the chessboard.
        solutions (list): A list to store the solutions.
    """
    # Base case: If all queens are placed, add the solution to the list
    if col == N:
        queens = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens.append([i, j])
        solutions.append(queens)
        return
    
    # Try placing a queen in each row of the current column
    for x in range(N):
        if is_safe(board, x, col, N):
            # Place the queen at board[x][col]
            board[x][col] = 1
            
            # Recur for the next column
            solve_nqueens_util(board, col + 1, N, solutions)
            
            # Backtrack and remove the queen from board[x][col]
            board[x][col] = 0


def solve_nqueens(N):
    """
    Solve the N queens problem and print the solutions.
    
    Args:
        N (int): The size of the chessboard and the number of queens.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    
    solve_nqueens_util(board, 0, N, solutions)
    
    for solution in solutions:
        print(solution)


def main():
    """
    Main function that parses command-line arguments and invokes the solver.
    """
    # Parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)


if __name__== "__main__":
    main()
