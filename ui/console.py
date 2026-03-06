from game.reversi_game import ReversiGame
from game.reversi_game import BLACK_SYMBOL
from game.reversi_game import BLACK_COLOR
from game.reversi_game import WHITE_SYMBOL
from game.reversi_game import WHITE_COLOR
from game.reversi_game import RESET


class ConsoleUI:
    def __init__(self, reversi_game: ReversiGame):
        self.reversi_game = reversi_game

    def draw_board(self) -> None:
        # Generate column headers
        letters = [chr(ord('A') + i) for i in range(self.reversi_game.size)]

        print("  " + " ".join(letters))

        for row_index, row in enumerate(self.reversi_game.board.board_state):
            row_number = self.reversi_game.size - row_index
#            print(f"{row_number} " + " ".join(row) + f" {row_number}")
            print(f"{row_number} " +
                  " ".join(self._get_colored_row(row)) + f" {row_number}")

        print("  " + " ".join(letters))  # Bottom column labels
        self._print_score()
        print()

    def _get_colored_row(self, row: list[str]) -> list[str]:

        result: list[str] = []
        for char in row:

            if char == WHITE_SYMBOL:
                result.append(WHITE_COLOR + char + RESET)
            elif char == BLACK_SYMBOL:
                result.append(BLACK_COLOR + char + RESET)
            else:
                result.append(char)

        return result

    def _print_score(self):
        print(
            f"{BLACK_COLOR}{BLACK_SYMBOL}{RESET}: {self.player1.score},  {WHITE_COLOR}{WHITE_SYMBOL}{RESET}: {self.player2.score}")

    def results(self) -> None:
        if self.reversi_game.player1.score == self.reversi_game.player2.score:
            print("It's a tie!")
        elif self.reversi_game.player2.score > self.reversi_game.player1.score:
            print(
                f"White won by {self.reversi_game.player2.score - self.reversi_game.player1.score} points!")
        else:
            print(
                f"Black won by {self.reversi_game.player1.score - self.reversi_game.player2.score} points!")
