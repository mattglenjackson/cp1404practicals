from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a Silver Service Taxi Object."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initializes a Silver Service Taxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the Silver Service Taxi trip."""
        return super().get_fare() + self.flagfall
