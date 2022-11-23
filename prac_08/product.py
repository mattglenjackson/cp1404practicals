class Product:
    """Resembles a Product object."""

    def __init__(self, name, price):
        """Instance of a product."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return string value for instance."""
        return f"{self.name} ${self.price:.2f}"
