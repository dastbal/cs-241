from turtle import width
import arcade
MAX_WIDTH = 10
MAX_HEIGHT = 10


class Box():
    # Draw the square
    def __init__(self, x=0, y=0, width=50, height=35) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_rectangle_filled(
            self.x, self.y, self.width, self.height, arcade.color.GREEN)

    def advance(self):
        self.x += 1
        self.y += 1


class DemoApp(arcade.Window):
    """[summary]

    Args:
        arcade ([type]): [description]
    """

    def __init__(self, width, height) -> None:
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)
        self.box = Box()

    def on_draw(self):
        arcade.start_render()

        self.box.draw()

    def update(self, delta_time: float):

        self.box.advance()


window = DemoApp(500, 400)
window.run()
