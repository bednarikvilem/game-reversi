from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, color):
        self.color = color
        self.score = 2

    @abstractmethod
    def get_move(self, valid_moves: list[tuple[int, str]]) -> tuple[int, str]:
        pass
