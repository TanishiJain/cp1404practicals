<<<<<<< HEAD
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class Dynamic_labels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"James": "909", "Helen": "238", "Tanishi" : "007"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_button = Button(text=name)
            self.root.ids.main.add_widget(temp_button)


Dynamic_labels().run()
=======
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class Dynamic_labels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"James": "909", "Helen": "238", "Tanishi" : "007"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_button = Button(text=name)
            self.root.ids.main.add_widget(temp_button)


Dynamic_labels().run()
>>>>>>> origin/prac_05_feedback
