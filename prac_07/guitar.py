class Guitar:
    """Representation of a guitar object."""

    def __init__(self, name, year, cost):
        """Initialize a guitar instance."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return a string representation of a guitar."""
        return f"{self.name} was made in {self.year} and costs ${self.cost:.2f}"

    def __lt__(self, other):
        """Allow class to be sorted by year."""
        return self.year < other.year
