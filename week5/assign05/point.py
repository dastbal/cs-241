from variable import SCREEN_HEIGHT
import random


class Point:
    """[summary] set a initial center of the object 
    """

    def __init__(self,x=0,y=random.uniform(0, SCREEN_HEIGHT)) -> None:
        self.x = x
        self.y = y
