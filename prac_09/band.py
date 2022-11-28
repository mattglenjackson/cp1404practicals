class Band:
    """Represents a band object."""

    def __init__(self, name=''):
        """Construct a Band with a name and list musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """String representation of a Band."""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])}"

    def add(self, musician):
        """Add musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing musicians playing their instruments."""
        for musician in self.musicians:
            print(musician.play())
