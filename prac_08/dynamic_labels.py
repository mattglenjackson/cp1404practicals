from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Jack', 'Mary', 'Jenny', 'Mike', 'James', 'Natalie', 'Sophie', 'Jason']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_label.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels for items in names in GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.label_box.add_widget(temp_label)


DynamicLabels().run()
