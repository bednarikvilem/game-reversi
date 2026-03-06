from game.player import Player

RESET = "\033[0m"


class HumanPlayer(Player):
    def __init__(self, symbol: str, style: str) -> None:
        super().__init__(symbol)
        self.symbol = symbol
        self.style = style

    def get_move(self, valid_moves: list[tuple[int, str]]) -> tuple[int, str]:

        while True:
            user_input: str = input(
                f"{self.style}{self.symbol}{RESET} is playing!\nEnter your move (or type QUIT to exit): ").strip().upper()

            if user_input == "QUIT":
                return 0, 'QUIT'

            for score, move in valid_moves:
                if move == user_input:
                    return score, move

            print("Invalid move. Please try again. Valid options are:")
            print("   ", ", ".join(move for _, move in valid_moves))
