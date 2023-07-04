import sys


__all__ = ['main']

class ChessBoard:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]

    def place_queen(self, row, col):
        self.board[row][col] = 1

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

    def check_queens(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == 1:
                    if not self.is_valid_move(row, col):
                        return False
        return True


def main():
    chess_board = ChessBoard()

    for i in range(8):
        try:
            row, col = map(int, input(f"Введите координаты ферзя {i+1} (в формате 'row col'): ").split())
            if 1 <= row <= 8 and 1 <= col <= 8:
                chess_board.place_queen(row-1, col-1)
            else:
                print("Координаты должны быть в диапазоне от 1 до 8.")
                return
        except ValueError:
            print("Некорректный ввод.")
            return

    if chess_board.check_queens():
        print("Ферзи не бьют друг друга.")
    else:
        print("Есть ферзи, которые бьют друг друга.")


if __name__ == "__main__":
    main()
    sys.exit()
