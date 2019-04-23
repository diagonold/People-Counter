from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color

Builder.load_file('homepage.kv')

class homepage_(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  #passing all arguments)

    def block59_page(self):
        self.parent.parent.current = 'block59page'

class homepageApp(App):
    def build(self):
        return homepage_()

if __name__== "__main__":
    homepageApp().run()

