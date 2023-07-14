# circle class

import random
from utils.cowboy import cowboy


class circle(object):
    def __init__(self, num_cowboys: int) -> None:
        '''define circle with n cowboys'''
        self.number: int = num_cowboys
        self.order: dict[str, cowboy] = self._create_order()
        self.round_metrics: list[dict] = []
        self.first_shooter: str = ""

    def _create_order(self) -> dict:
        '''create initial circle order'''
        tmp_circle: dict[str, cowboy] = {}
        # order: list[str] = []
        for i in range(0, self.number):
            name = "cowboy_" + str(i)
            # ith_cowboy: cowboy = cowboy(name)
            tmp_circle[name] = cowboy(name)
            # order.append(ith_cowboy.name)
        tmp_circle = self._tell_neighbors(tmp_circle)
        return tmp_circle

    def _tell_neighbors(self, order: dict[str, cowboy]) -> dict[str, cowboy]:
        '''tell cowboys their neigbors'''
        names: tuple = tuple(order.keys())
        for i, name in enumerate(names):
            if i == 0:
                left: str = names[-1]
                right: str = names[i+1]
            elif i == len(names)-1:
                left: str = names[i-1]
                right: str = names[0]
            else:
                left: str = names[i-1]
                right: str = names[i+1]
            order[name].left_hand = left
            order[name].right_hand = right
        return order

    def high_noon(self):
        ''' start the shooting '''
        names: tuple = tuple(self.order.keys())
        first_no: int = random.randint(0, len(names)-1)
        self.first_shooter: str = names[first_no]
        self.shoot_another_round(self.first_shooter)

    def shoot_another_round(self, name) -> str:
        shooter: cowboy = self.order[name]
        shot: int = shooter.shoot()
        opponent: str = shooter.shoot_who()
        opponent_health: int = self.order[opponent].health - shot
        next_shooter: str = ""
        if opponent_health <= 0:
            opponent_health = 0
            self._update_opponents(shooter, opponent)
            self.order.pop(opponent)
            next_shooter = name
        else:
            self.order[opponent].health = opponent_health
            next_shooter = self.order[opponent].name

        metrics: dict = {
            "shooter": shooter.name,
            "shot_strenght": shot,
            "opponent": opponent,
            "opponent_health": opponent_health,
            "round": len(self.round_metrics)
        }
        self.round_metrics.append(metrics)
        # return next_shooter
        if len(self.order) > 1:
            self.shoot_another_round(next_shooter)

    def _update_opponents(self, shooter: cowboy, opponent: str):
        if shooter.last_shot == "left":
            new_opponent: str = self.order[opponent].left_hand
            for this_cowboy in self.order:
                if self.order[this_cowboy].left_hand == opponent:
                    self.order[this_cowboy].left_hand = new_opponent
                if self.order[this_cowboy].right_hand == opponent:
                    self.order[this_cowboy].right_hand = shooter.name
        else:
            new_opponent: str = self.order[opponent].right_hand
            for this_cowboy in self.order:
                if self.order[this_cowboy].right_hand == opponent:
                    self.order[this_cowboy].right_hand = new_opponent
                if self.order[this_cowboy].left_hand == opponent:
                    self.order[this_cowboy].left_hand = shooter.name

    def report(self):
        import json
        report = json.dumps(self.round_metrics, indent=2)
        print(report)
        last_man_standing: str = list(self.order.keys())[0]
        print(f"\n\n{self.first_shooter} started")
        print(f"\n{last_man_standing} won")
