'''
Basic camera example
'''

from os import getcwd
from os.path import exists
from os.path import splitext

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.logger import Logger

from plyer import camera

from send import sendpic


class CameraDemo(FloatLayout):
    def __init__(self):
        super(CameraDemo, self).__init__()

    def do_capture(self):
        filepath = App.get_running_app().user_data_dir + '/mlpic.png'
        self.ids.path_label.text = "Machine Learning"
        ext = splitext(filepath)[-1].lower()

        try:
            camera.take_picture(
                filename=filepath, on_complete=self.camera_callback)
        except NotImplementedError:
            popup = MsgPopup(
                msg="This feature has not yet been implemented for this platform."
            )
            popup.open()

    def camera_callback(self, filepath):
        if (exists(filepath)):
            popup = MsgPopup(msg=sendpic(filepath))
            popup.open()
        else:
            popup = MsgPopup(msg="Could not save your picture!")
            popup.open()


class CameraDemoApp(App):
    def __init__(self):
        super(CameraDemoApp, self).__init__()
        self.demo = None
        data_dir = getattr(self, "user_data_dir")

    def build(self):
        self.demo = CameraDemo()
        return self.demo

    def on_pause(self):
        return True

    def on_resume(self):
        pass


class MsgPopup(Popup):
    def __init__(self, msg):
        super(MsgPopup, self).__init__()
        self.ids.message_label.text = msg


if __name__ == '__main__':
    CameraDemoApp().run()
