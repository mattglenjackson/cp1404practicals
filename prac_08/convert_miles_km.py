from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

KILOMETER_CONVERSION_RATIO = 1.60934


class ConvertMilesToKilometers(App):
    output_status = StringProperty()

    def build(self):
        """Build instance of Convert Miles to Kilometers app."""
        Window.size = (300, 150)
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculate, converts miles to km."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, number, increment):
        """Handles Up and Down button presses in app to change number in input text box."""
        miles = self.convert_to_number(number) + increment
        self.root.ids.input_miles.text = str(miles)

    def convert_to_number(self, text):
        """Convert text to float or 0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

    def update_result(self, miles):
        print('update')
        self.output_status = f"{str(miles * KILOMETER_CONVERSION_RATIO)} kilometers"


# I found this one challenging. I got through everything okay until trying to handle invalid inputs. Used solutions
# to work out what I had done wrong.

ConvertMilesToKilometers().run()
