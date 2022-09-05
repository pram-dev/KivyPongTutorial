"""
Basic Kivy pong game built using Kivy docs tutorial
"""

import kivy
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


class PongPaddle(Widget):
    """
    PongPaddle class to represent player paddles
    """

    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            offset = 0.02 * Vector(0, ball.center_y - self.center_y)
            ball.velocity = speedup * (offset - ball.velocity)


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


class PongGame(Widget):
    """
    PongGame inherits from kivy Widget class
    """

    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # player paddle bounce
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # ball went past a player paddle and scored a point
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(4, 0))

    def on_touch_move(self, touch):
        if touch.x < (self.width / 3):
            self.player1.center_y = touch.y
        if touch.x > (self.width - (self.width / 3)):
            self.player2.center_y = touch.y


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
