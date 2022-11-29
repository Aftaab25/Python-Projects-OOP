from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def searchImage(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()