"""
Basic Kivy pong game built using Kivy docs tutorial
"""

import kivy
from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty,
    ReferenceListProperty,
    ObjectProperty
)

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

    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off of left and right sides
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        return


class PongApp(App):
    """
    PongApp inherits from kivy App class
    """

    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongApp().run()
