from kivy.app import App
 
from kivy.uix.button import  Button
 
from kivy.uix.textinput import TextInput
 
from kivy.uix.boxlayout import BoxLayout

from imageai.Prediction.Custom import CustomImagePrediction

from kivy.uix.image import Image

import os

 
class TheRisingSunApp(App):
 
    def build(self):
 
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        
        self.box1 = BoxLayout(orientation='horizontal', spacing=20)
        
        self.txt = TextInput(hint_text='Write here', size_hint=(.5,.1))
        
        #self.img = Image('cotimage.jpeg')
 
        self.btn = Button(text='Submit', on_press=self.clearText, size_hint=(.1,.1))
        
 
        self.box.add_widget(self.txt)
 
        self.box.add_widget(self.btn)
        
        return self.box
 
    def clearText(self, instance):
        
        filename = self.txt.text
        
        execution_path = os.getcwd()

        prediction = CustomImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath("model_ex-148_acc-0.843750.h5")
        prediction.setJsonPath("model_class.json")
        prediction.loadModel(num_objects=8)

        predictions, probabilities = prediction.predictImage(filename, result_count=1)

        crop=""
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            crop += str(eachPrediction)
     
        self.txt.text = crop
 
TheRisingSunApp().run()
