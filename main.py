"""
Basic Kivy pong game built using Kivy docs tutorial
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
kivy.require("2.1.0")

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
