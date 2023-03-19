from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class Vybe(GridLayout):
    
    def __init__(self, **var_args):
 
        super(Vybe, self).__init__(**var_args)
        self.cols = 1     
        self.add_widget(Label(text='What is your mood?'))
        self.mood = TextInput(multiline=False)
        self.add_widget(self.mood)
        self.list=[]
        
class MyApp(App):
    def build(self):
        return Vybe()
 
 
if __name__ == '__main__':
    MyApp().run()




