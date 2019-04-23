from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from libdw import pyrebase
from kivy.uix.label import Label
from kivy.graphics import Color

Builder.load_file('block59page.kv')

config = {
  "apiKey": "AIzaSyD4sBcO_63b0zj2gJ82W-5g_bEW0p5hzOI",
  "databaseURL": "https://dwmeetingroom-6aef1.firebaseio.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
value = db.child('/')

class block59pageWindow(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  #passing all arguments

    def homepageee(self):
        self.parent.parent.current = 'homepage'

    def button3shiftDOWN(self):
        study59_button = self.ids.study_59_parent
        study59_button.pos_hint = {"x":0.1, "top":0.3}
        print('DROPDOWN OPEN')

    def button3shiftUP(self):
        study59_button = self.ids.study_59_parent
        study59_button.pos_hint = {"x":0.1, "top":0.525}
        print ('DROPDOWN CLOSE')

    def update(self, *args):
        value7 = value.child('Block 59').child('Meeting Rooms').child('Level 7').get().val()
        value10 = value.child('Block 59').child('Meeting Rooms').child('Level 10').get().val()
        if value7 >= value10:
            level_7 = self.ids.firstlabel
            level_10 = self.ids.secondlabel
        else:
            level_10 = self.ids.firstlabel
            level_7 = self.ids.secondlabel
        level_7.text = 'Level 7:     ' + str(value7)
        level_10.text = 'Level 10:     ' + str(value10)

        print (level_7.text + '  |  ' + level_10.text)


class block59pageApp(App):
    def build(self):
        return block59pageWindow()

if __name__== "__main__":
    block59pageApp().run()