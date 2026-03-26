from student import Student

class Classroom:
    """
    A Manager class acting as a container holding multiple Student objects natively.
    Demonstrates working with lists of objects and sorting them structurally.
    """

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student):
        """Composition: We pass an independent Student object into the Classroom."""
        if isinstance(student, Student):
            self.students.append(student)

    def get_top_student(self):
        if not self.students:
            return None
        # We sort objects explicitly by passing a lambda function pointing to the @property attribute!
        return max(self.students, key=lambda s: s.average)

    def generate_report(self):
        """Returns a string-formatted report sorting students descending by average."""
        if not self.students:
            return "No students enrolled."
            
        report = [f"Classroom Report: {self.course_name}", "-" * 30]
        
        # Sort objects iteratively using python's native descending reverse logic
        ranked = sorted(self.students, key=lambda s: s.average, reverse=True)
        
        for rank, student in enumerate(ranked, start=1):
            report.append(f"{rank}. {student}")
            
        return "\n".join(report)
