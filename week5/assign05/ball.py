from point import Point
from velocity import Velocity
from variable import BALL_RADIUS
import arcade


class Ball:
    """
    Class Ball will have methods to draw a 
    ball and move it in diferents direcctions and restart it
    """

    def __init__(self) -> None:
        self.center = Point()
        self.velocity = Velocity()

    def draw(self):
        """
        Create a ball
        """

        arcade.draw_circle_filled(
            self.center.x, self.center.y, BALL_RADIUS, arcade.color.RED)

    def advance(self):
        """
        to move the ball with the velocity
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        """ change the dirrection of the velocity in the x axis
        """
        self.velocity.dx *= -1

    def bounce_vertical(self):
        """[summary]
        change the dirrection of the velocity in the y axis
        """
        self.velocity.dy *= -1

    def restart(self):
        self.center = Point()
