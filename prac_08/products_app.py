"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on custom class objects
For something to do, pressing the guitar buttons changes the cost in the guitar objects
Note we can directly assign the object to the button.
This is a REFERENCE to the existing object, not a copy.
Lindsay Ward
30/01/2018
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from product import Product


class ProductsApp(App):
    """Main program - Kivy app to demo combining classes and Kivy."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        # Basic data example - list of Product objects - could be loaded from a file or something
        self.products = [Product("Cheese", 12.5), Product("Laptop", 912.95), Product("Plant", 4.75),
                         Product("Coffee Machine", 2300.00), Product("Guitar", 4399.95)]
        self.total_price = 0.0

    def build(self):
        """Build the Kivy GUI."""
        Window.size = 1000, 800
        self.title = "Kivy + Classes = Products"
        self.root = Builder.load_file('products_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from list of objects and add them to the GUI."""
        for product in self.products:
            # Create a button for each Product object, specifying the text
            temp_button = Button(text=str(product))
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the product object in the button object
            temp_button.product = product
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing product buttons."""
        # Each button was given its own ".product" object reference, so we can get it directly
        product = instance.product
        self.total_price += product.price
        self.status_text = f"Total price is ${self.total_price:,.2f}"

    def handle_clear(self):
        """Handle pressing clear button."""
        print("clear")
        self.status_text = ""
        self.total_price = 0.0


ProductsApp().run()
