# cowboy class

import random


class cowboy(object):
    def __init__(self, new_name: str) -> None:
        self.name: str = new_name
        self.health: int = 10
        self._left_hand: str = ""
        self._right_hand: str = ""
        self.last_shot: str = ""

    @property
    def left_hand(self) -> str:
        return self._left_hand

    @left_hand.setter
    def left_hand(self, name: str) -> None:
        self._left_hand = name

    @property
    def right_hand(self) -> str:
        return self._right_hand

    @right_hand.setter
    def right_hand(self, name: str) -> None:
        self._right_hand = name

    def shoot(self) -> int:
        return random.randint(1, 5)

    def shoot_who(self) -> str:
        if self.health % 2 == 0:
            self.last_shot = "right"
            return self.right_hand
        else:
            self.last_shot = "left"
            return self.left_hand
