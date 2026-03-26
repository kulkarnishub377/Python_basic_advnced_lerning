class Book:
    """
    A pure Python blueprint tracking the explicit structural state of a 
    physical library book mapped mathematically into memory.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Tracking the structural state: None means available, a string name means checked out
        self.borrowed_by = None

    @property
    def is_available(self):
        """Safely evaluates boolean state computationally instead of manual variables."""
        return self.borrowed_by is None

    def __str__(self):
        """
        The __str__ 'dunder' method defines precisely how this object behaves when printed.
        Without this, printing a Book returns `<__main__.Book object at 0x...>`
        """
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"'{self.title}' by {self.author} [{status}]"
