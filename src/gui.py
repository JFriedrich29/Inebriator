from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class InAPP(App):
    def build(self):
        return InGui()


class InGui(Widget):
    test = ObjectProperty(None)
    pass

    def btn(self):
        print(self.test.text)

class InLayout(GridLayout):
    """ Testcode for programatic widget adding
    def __init__(self, **kwargs):
        super(InLayout, self).__init__(**kwargs)

        self.nestedgrid = GridLayout()
        self.nestedgrid.cols = 2

        self.cols = 1
        self.nestedgrid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.nestedgrid.add_widget(self.name)

        self.add_widget(self.nestedgrid)
        
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        print(self.name.text)
"""


if __name__ == "__main__":
    InAPP().run()