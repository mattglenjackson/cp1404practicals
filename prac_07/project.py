class Project:
    """Represents a project object."""

    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string value for project."""
        return f"{self.name}, start {self.start_date}, priority {self.priority}, " \
               f"estimate ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
