from kivy.app import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

layout = GridLayout( cols=1, spacing=10 , size_hint_y=None ,)
layout.bind(minimum_height=layout.setter('height'))
for i in range (100):
    btn = Button( size_hint_y=None , height=40 , text = "Button" + str(i))
    layout.add_widget(btn)
root = ScrollView()
root.add_widget(layout)
runTouchApp(root)
