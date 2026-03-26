class Student:
    """
    A foundational Object-Oriented representation of a Student.
    Demonstrates data encapsulation, constructors, and the @property decorator!
    """

    def __init__(self, student_id, name, scores=None):
        self.student_id = student_id
        self.name = name
        # If no scores are provided, default to an empty list cleanly
        self.scores = scores if scores is not None else []

    def add_score(self, score):
        """Standard instance method modifying the object's internal state."""
        if 0 <= score <= 100:
            self.scores.append(score)
            return True
        return False

    @property
    def average(self):
        """
        The @property decorator transforms this method into an attribute!
        You can call `student.average` instead of `student.average()`.
        """
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    @property
    def letter_grade(self):
        """Dynamic computation derived natively from the average property."""
        avg = self.average
        if avg >= 90: return 'A'
        if avg >= 80: return 'B'
        if avg >= 70: return 'C'
        if avg >= 60: return 'D'
        return 'F'

    def __str__(self):
        """Dunder method dictating exactly how this object prints natively."""
        return f"[{self.student_id}] {self.name} - Avg: {self.average:.1f}% ({self.letter_grade})"
