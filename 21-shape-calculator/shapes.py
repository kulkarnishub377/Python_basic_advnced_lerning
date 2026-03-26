from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    An Abstract Base Class (ABC) serving purely as a contract.
    You cannot instantiate a 'Shape', you must specifically build a subclass!
    """

    def __init__(self, color="Black"):
        self.color = color

    @abstractmethod
    def area(self):
        """Every single subclass MUST implement this method or it will crash."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every single subclass MUST implement this mathematically!"""
        pass

class Circle(Shape):
    """Inherits from Shape, implementing specific abstract methods."""

    def __init__(self, radius, color="Red"):
        # the super() call initializes the parent class properties natively
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"{self.color} Circle (r={self.radius})"

class Rectangle(Shape):
    """Inherits from Shape, calculating explicit geometric operations."""

    def __init__(self, width, height, color="Blue"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.color} Rectangle ({self.width}x{self.height})"
