from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
import json
import re


class Vybe(GridLayout):
    def on_enter(instance, value):
        print('User pressed enter in '+str(instance.mood.text), instance)
        instance.update_song()
    
    def __init__(self, **var_args):
 
        super(Vybe, self).__init__(**var_args)
        self.cols = 1     
        self.add_widget(Label(text='What is your mood?'))
        self.mood = TextInput(multiline=False)
        self.mood.bind(on_text_validate=self.on_enter)
        self.add_widget(self.mood)
        self.lbl=Label(text='Your Song:')
        self.add_widget(self.lbl)
        self.rec=Label(text='')
        self.add_widget(self.rec)
        self.list=[]
    
    def update_song(self):
        txt=(self.mood.text)
        res=requests.post('http://127.0.0.1:5000/predict?data='+str(txt))
        print("API RES: "+str(res.text))
        self.rec.text=str(res.text)
        

class MyApp(App):
    def build(self):
        return Vybe()
 
 
if __name__ == '__main__':
    MyApp().run()




