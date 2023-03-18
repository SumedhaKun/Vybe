from kivy.app import App
# GridLayout arranges children in a matrix.
from kivy.uix.gridlayout import GridLayout
# Label is used to label something
from kivy.uix.label import Label
# used to take input from users
from kivy.uix.textinput import TextInput



class Vybe(GridLayout):
    
    def __init__(self, **var_args):
 
        super(Vybe, self).__init__(**var_args)
        self.cols = 1     # You can change it accordingly
        self.add_widget(Label(text='What is your mood?'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
class MyApp(App):
    def build(self):
        return Vybe()
 
 
if __name__ == '__main__':
    MyApp().run()



