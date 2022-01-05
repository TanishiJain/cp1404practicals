from kivy.app import App
from kivy.lang import Builder
<<<<<<< HEAD
=======
from kivy.uix.label import Label

>>>>>>> 1e9e6e2 (Update)


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        print("clear")
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
<<<<<<< HEAD

=======
>>>>>>> 1e9e6e2 (Update)
