"""
Connect 4

Simple Connect4 class with a play method.

Usage:
    game = Connect4()
    print(game.play(0))

The columns are 0-6 (left to right). Player 1 starts.
"""

class Connect4:
    def __init__(self):
        # 6 rows x 7 columns board, 0 = empty, 1 = player1, 2 = player2
        self.board = [[0] * 7 for _ in range(6)]
        self.current_player = 1
        self.game_over = False

    def get_row(self, col):
        # Return the lowest empty row index for a column, or -1 if full
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                return row
        return -1

    def check_win(self, player):
        # Horizontal
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True
        # Vertical
        for col in range(7):
            for row in range(3):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True
        # Diagonal down-right
        for row in range(3):
            for col in range(4):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True
        # Diagonal down-left
        for row in range(3):
            for col in range(3, 7):
                if all(self.board[row + i][col - i] == player for i in range(4)):
                    return True
        return False

    def play(self, col):
        if self.game_over:
            return "Game has finished!"
        # Validate column index
        if not (0 <= col <= 6):
            raise IndexError("Column out of range")
        # Check if column is full
        if self.board[0][col] != 0:
            return "Column full!"
        row = self.get_row(col)
        if row == -1:
            return "Column full!"

        player = self.current_player
        self.board[row][col] = player

        if self.check_win(player):
            self.game_over = True
            return f"Player {player} wins!"
        # switch player
        self.current_player = 2 if player == 1 else 1
        return f"Player {self.current_player} has a turn"


if __name__ == "__main__":
    # simple manual play example
    g = Connect4()
    moves = [3,3,2,2,4,4,1]
    for m in moves:
        print(g.play(m))
