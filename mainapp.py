from kivy.app import App

from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label,Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout
from kivy.properties import (ObjectProperty , NumericProperty , ReferenceListProperty)
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.vector import Vector
from random import randint
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    def serve_ball(self ):
        self.ball.center = self.center
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))
    def update(self ,dt):
        self.ball.move()
        if (self.ball.y < 0) or (self.ball.top > self.height) :
            self.ball.velocity_y *= -1
        #if (self.ball.x < 0) or (self.ball.right > self.width) :
        #    self.ball.velocity_x *= -1
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        if (self.ball.x < 0):
            self.player2.score +=1
            self.serve_ball()
        if (self.ball.right > self.width):
            self.player1.score +=1
            self.serve_ball()
    def on_touch_move(self, touch):
        if touch.x < self.width/3 :
            self.player1.center_y = touch.y
        if touch.x > 2* self.width/3 :
            self.player2.center_y = touch.y    

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)
    def move(self):
        self.pos = Vector(self.pos) + Vector(self.velocity) 
     
class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self ,ball):
        if self.collide_widget(ball):
            vx,vy = ball.velocity 
            bounced = Vector(-1*vx , vy)
            vel = 1.1*bounced
            ball.velocity = vel.x , vel.y


class PongApp(App):
    def build(self):
        game=PongGame()
        #return super().build()
        game.serve_ball()
        Clock.schedule_interval(game.update , 1.0/60.0)
        return game
    

PongApp().run()