class Guitar:
    """Represent a guitar object."""
    CURRENT_YEAR = 2022
    VINTAGE_THRESHOLD = 50

    def __init__(self, name='', year=0, cost=0.0):
        """Initialize a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string when Guitar is printed."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get age of guitar."""
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        return self.get_age() >= self.VINTAGE_THRESHOLD
