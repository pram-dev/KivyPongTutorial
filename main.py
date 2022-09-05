"""
Basic Kivy pong game built using Kivy docs tutorial
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
kivy.require("2.1.0")


class PongBall(Widget):
    """
    PongBall class to represent pong ball
    """

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # ReferenceListProperty allows "velocity" to refer to both velocity x and y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        return


class PongGame(Widget):
    """
    PongGame inherits from kivy Widget class
    """
    pass


class PongApp(App):
    """
    PongApp inherits from kivy App class
    """

    def build(self):
        return PongGame()


if __name__ == "__main__":
    PongApp().run()
