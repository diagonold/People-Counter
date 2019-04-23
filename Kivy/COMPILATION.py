from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from homepage import homepage_
from block59page import block59pageWindow
from intro import intro_
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from libdw import pyrebase
from kivy.uix.label import Label


Builder.load_file("homepage.kv")

class mainWindow(BoxLayout):

    homepage_page = homepage_()
    block59page_page = block59pageWindow()
    intro_page = intro_()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_intro_screen = self.ids.intro
        main_homepage_screen = self.ids.homepage
        main_block59page_screen = self.ids.block59page
        main_intro_screen.add_widget(self.intro_page)
        main_homepage_screen.add_widget(self.homepage_page)
        main_block59page_screen.add_widget(self.block59page_page)

        t = self.block59page_page
        Clock.schedule_interval(t.update, 1)

class COMPILATIONApp(App):
    def build(self):
        return mainWindow()

if __name__ == "__main__":
    display = COMPILATIONApp()
    display.run()