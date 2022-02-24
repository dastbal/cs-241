from re import M
import arcade
from point import Point
from variable import PADDLE_HEIGHT
from variable import PADDLE_WIDTH
from variable import MOVE_AMOUNT
from variable import SCREEN_WIDTH
from variable import SCREEN_HEIGHT
import arcade


class Paddle:
    """
    Create a paddle in the center of the screen height
    """

    def __init__(self) -> None:
        self.center = Point(SCREEN_WIDTH, SCREEN_HEIGHT // 2)

    def draw(self):
        """
         draw the paddle with the params and with color black
        """
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLACK)

    def move_up(self):
        """move  up the paddle
        """
        if self.center.y > (SCREEN_HEIGHT - PADDLE_HEIGHT//2):
            pass  # when it is near of the edge will stop
        else:
            self.center.y += MOVE_AMOUNT

    def move_down(self):
        """move down the paddle
        """
        if self.center.y < PADDLE_HEIGHT//2:
            pass  # when it is near of the edge will stop
        else:
            self.center.y -= MOVE_AMOUNT
