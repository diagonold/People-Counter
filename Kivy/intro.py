from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("intro.kv")

class intro_(FloatLayout):  #the name of class is the < block59pageWindow > in kivy
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def homepageeeee(self):
        self.parent.parent.current = "homepage"

class introApp(App):
    def build(self):
        return intro_()


if __name__ == "__main__":
    display = introApp()
    introApp().run()