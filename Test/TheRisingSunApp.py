import kivy
from kivy.app import App
from kivy.uix.label import Label
import crop_detection as crd

class TheRisingSunApp(App):
    def build(self):
        crop = crd.executable()
        return Label(text = crop)

if __name__ == "__main__":
    TheRisingSunApp().run()


