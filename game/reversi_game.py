from game.human_player import HumanPlayer
from game.computer_player import ComputerPlayer
from board import Board
from game.player import Player
import copy

WHITE_SYMBOL = 'O'
BLACK_SYMBOL = 'X'
BLACK_COLOR = "\033[31m"
WHITE_COLOR = "\033[34m"
RESET = "\033[0m"


class ReversiGame:
    def __init__(self, size: int, player1: Player, player2: Player):
        self.size = size
        self.board = Board(size)
        self.player1 = player1
        self.player2 = player2
        self.current_player: Player = player1
        self.openent: Player = player2

    def play(self) -> tuple[int, int]:
        game_quit: bool = False
        while not self.board.is_game_over(self.current_player, self.openent):
            self.print_board()

            moves = self.board.get_valid_moves(self.current_player)

            if moves:
                score, move = self.current_player.get_move(moves)

                if move == "QUIT":
                    game_quit = True
                    print("Goodbye...")
                    break

                self.board.make_move(move, self.current_player)
                self.adjust_score(score)

            self.switch_players()

        if not game_quit:
            self.print_board()
            self.results()
            return self.player1.score, self.player2.score

        return 0, 0

    def switch_players(self) -> None:
        self.current_player, self.openent = self.openent, self.current_player

    def adjust_score(self, score: int) -> None:
        self.current_player.score += score + 1
        self.openent.score -= score

    def print_board(self) -> None:
        # Generate column headers
        letters = [chr(ord('A') + i) for i in range(self.size)]

        print("  " + " ".join(letters))

        for row_index, row in enumerate(self.board.board_state):
            row_number = self.size - row_index
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
        if self.player1.score == self.player2.score:
            print("It's a tie!")
        elif self.player2.score > self.player1.score:
            print(
                f"White won by {self.player2.score - self.player1.score} points!")
        else:
            print(
                f"Black won by {self.player1.score - self.player2.score} points!")

    def clone(self) -> "ReversiGame":
        return copy.deepcopy(self)


# g = ReversiGame(8, HumanPlayer(BLACK_SYMBOL, BLACK_COLOR),
#                 ComputerPlayer(WHITE_SYMBOL, 1))

# g.play()
