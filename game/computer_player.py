from game.player import Player
import random
import time


class ComputerPlayer(Player):
    def __init__(self, symbol: str, type: int) -> None:
        super().__init__(symbol)
        self.symbol = symbol
        self.type: int = type

    def get_move(self, valid_moves: list[tuple[int, str]]) -> tuple[int, str]:

        match self.type:
            case 1:
                time.sleep(2)
                return self.calculate_move_hungry(valid_moves)
            case _:
                time.sleep(2)
                return self.calculate_move_randomly(valid_moves)

    def calculate_move_hungry(self, valid_moves: list[tuple[int, str]]) -> tuple[int, str]:

        if len(valid_moves) == 0:
            raise ValueError("The list is empty!")

        valid_moves.sort()
        valid_moves.reverse()

        best_score, _ = valid_moves[0]
        possible_moves: list[tuple[int, str]] = []

        for score, move in valid_moves:
            if score != best_score:
                break
            possible_moves.append((score, move))

        result: tuple[int, str] = random.choice(possible_moves)

        return result

    def calculate_move_randomly(self, valid_moves: list[tuple[int, str]]) -> tuple[int, str]:

        if len(valid_moves) == 0:
            raise ValueError("The list is empty!")

        result = random.choice(valid_moves)

        return result

    # def calculate_move_dfs(self, game: ReversiGame, valid_moves: list[tuple[int, str]]) -> tuple[int, str]:
    #     best_score = -math.inf
    #     best_move = None

    #     for score, move in valid_moves:

    #     return 0, 'a'
