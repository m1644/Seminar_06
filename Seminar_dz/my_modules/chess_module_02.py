import random
import sys


__all__ = ['main']

class ChessBoard:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.solutions = []

    def place_queen(self, row, col):
        self.board[row][col] = 1

    def remove_queen(self, row, col):
        self.board[row][col] = 0

    def is_valid_move(self, row, col):
        for i in range(8):
            if self.board[row][i] == 1 or self.board[i][col] == 1:
                return False
            if row + i < 8 and col + i < 8 and self.board[row + i][col + i] == 1:
                return False
            if row - i >= 0 and col - i >= 0 and self.board[row - i][col - i] == 1:
                return False
            if row + i < 8 and col - i >= 0 and self.board[row + i][col - i] == 1:
                return False
            if row - i >= 0 and col + i < 8 and self.board[row - i][col + i] == 1:
                return False
        return True

    def solve_queens(self, row):
        if row == 8:
            solution = []
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == 1:
                        solution.append((i+1, j+1))
            self.solutions.append(solution)
            return

        for col in range(8):
            if self.is_valid_move(row, col):
                self.place_queen(row, col)
                self.solve_queens(row + 1)
                self.remove_queen(row, col)

    def find_solutions(self):
        self.solve_queens(0)

    def print_solutions(self, num_solutions):
        for i in range(num_solutions):
            solution = self.solutions[i]
            print("Успешная расстановка ферзей:")
            for row in range(8):
                line = ['Q' if (row+1, col+1) in solution else '.' for col in range(8)]
                print(' '.join(line))
            print()

def main():
    chess_board = ChessBoard()
    attempts = 0
    num_solutions = 4

    while len(chess_board.solutions) < num_solutions and attempts < 1000:
        chess_board = ChessBoard()
        chess_board.find_solutions()
        attempts += 1

    if len(chess_board.solutions) > 0:
        chess_board.print_solutions(num_solutions)
    else:
        print("Не удалось найти {} успешные расстановки ферзей.".format(num_solutions))


if __name__ == "__main__":
    main()
    sys.exit()
