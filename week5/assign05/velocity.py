import random


class Velocity:
    """[summary] set a velocity initial
    """

    def __init__(self) -> None:
        self.dx = random.uniform(2, 4)
        self.dy = random.uniform(2, 4)
