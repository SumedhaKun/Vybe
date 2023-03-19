from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
import json



class Vybe(GridLayout):
    
    def __init__(self, **var_args):
 
        super(Vybe, self).__init__(**var_args)
        self.cols = 1     
        self.add_widget(Label(text='What is your mood?'))
        self.mood = TextInput(multiline=False)
        self.add_widget(self.mood)
        self.btn=Button(text="Done")
        self.btn.bind(on_press = self.get_synonyms)
        self.add_widget(self.btn)
        self.list=[]
    def get_synonyms(self, event):
        req=requests.get(f"https://tuna.thesaurus.com/pageData/"+str(self.mood))
        dict_synonyms=req.json()['data']
        #synonyms=[r['term'] for r in dict_synonyms]
        print(dict_synonyms)
        

class MyApp(App):
    def build(self):
        return Vybe()
 
 
if __name__ == '__main__':
    MyApp().run()




