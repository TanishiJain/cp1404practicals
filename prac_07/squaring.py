<<<<<<< HEAD


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
<<<<<<< HEAD
=======
from kivy import Config
>>>>>>> 1e9e6e2 (Update)




class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):

        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
<<<<<<< HEAD

=======
>>>>>>> 1e9e6e2 (Update)
=======


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window




class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):

        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
>>>>>>> 141d9f1 (Update)
