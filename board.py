from game.player import Player

EMPTY = ' '
WHITE_SYMBOL = 'O'
BLACK_SYMBOL = 'X'
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

Gamefield = list[list[str]]


class Board:
    def __init__(self, size: int):

        if not self._is_valid_board_size(size):
            raise ValueError("Size must be even and greater than 4.")

        self.size = size
        self.board_state = self._initialize_board()

    def _is_valid_board_size(self, n: int) -> bool:
        return n >= 4 and n % 2 == 0

    def _initialize_board(self) -> Gamefield:
        result: Gamefield = [
            [EMPTY for _ in range(self.size)] for _ in range(self.size)]
        mid: int = self.size // 2
        result[mid - 1][mid - 1] = BLACK_SYMBOL
        result[mid - 1][mid] = WHITE_SYMBOL
        result[mid][mid] = BLACK_SYMBOL
        result[mid][mid - 1] = WHITE_SYMBOL
        return result

    def get_valid_moves(self, player: Player) -> list[tuple[int, str]]:
        valid_moves: list[tuple[int, str]] = []
        for row in range(1, self.size + 1):
            for col in range(self.size):
                move = chr(ord('A') + col) + str(row)
                score: int = self._calculate_flipped(move, player)
                if score > 0:
                    valid_moves.append((score, move))

        return valid_moves

    def _calculate_flipped(self, move: str, player: Player) -> int:
        if len(move) < 2:
            return 0

        col_letter = move[0].upper()
        try:
            row_index = abs(int(move[1:]) - self.size)
        except ValueError:
            return 0

        col_index = ord(col_letter) - ord('A')

        if not (0 <= row_index < self.size and 0 <= col_index < self.size):
            return 0

        if self.board_state[row_index][col_index] != EMPTY:
            return 0

        opponent = WHITE_SYMBOL if player.color == BLACK_SYMBOL else BLACK_SYMBOL
        total_flipped = 0

        for dx, dy in DIRECTIONS:
            x, y = row_index + dx, col_index + dy
            path = []

            while 0 <= x < self.size and 0 <= y < self.size:
                if self.board_state[x][y] == opponent:
                    path.append((x, y))
                elif self.board_state[x][y] == player.color:
                    total_flipped += len(path)
                    break
                else:
                    break
                x += dx
                y += dy

        return total_flipped

    def is_game_over(self, player1: Player, player2: Player) -> bool:
        return self.get_valid_moves(player1) == [] and self.get_valid_moves(player2) == []

    def make_move(self, move: str, player: Player):
        row = abs(int(move[1:]) - self.size)
        col = ord(move[0]) - ord('A')
        self.board_state[row][col] = player.color
        opponent = WHITE_SYMBOL if player.color == BLACK_SYMBOL else BLACK_SYMBOL

        for dx, dy in DIRECTIONS:
            x, y = row + dx, col + dy
            path = []

            while 0 <= x < self.size and 0 <= y < self.size:
                if self.board_state[x][y] == opponent:
                    path.append((x, y))
                elif self.board_state[x][y] == player.color:
                    for px, py in path:
                        self.board_state[px][py] = player.color

                    break

                else:
                    break

                x += dx
                y += dy

    def print_board(self):
        # Generate column headers
        letters = [chr(ord('A') + i) for i in range(self.size)]

        print("  " + " ".join(letters))

        for row_index, row in enumerate(self.board_state):
            row_number = self.size - row_index
#            print(f"{row_number} " + " ".join(row) + f" {row_number}")
            print(f"{row_number} " +
                  " ".join(self._get_colored_row(row)) + f" {row_number}")

        print("  " + " ".join(letters))  # Bottom column labels
        print()
