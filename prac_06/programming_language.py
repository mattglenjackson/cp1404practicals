class ProgrammingLanguage:

    def __init__(self, name='', typing_method='', reflection='', year=0):
        """Constructor method for ProgrammingLanguage"""
        self.name = name
        self.typing_method = typing_method
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string when ProgrammingLanguage is printed."""
        return f"{self.name}, {self.typing_method} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing_method == "Dynamic"