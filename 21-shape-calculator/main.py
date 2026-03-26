from shapes import Circle, Rectangle

def factory_pattern_demo():
    """
    Demonstrates Polymorphism!
    We can iterate through entirely different classes blindly calling `.area()` 
    knowing the strict ABC Abstract Method Contract forces them to exist!
    """
    
    # We dynamically pack entirely different subclass objects into one array
    shapes = [
        Circle(radius=5, color="Crimson"),
        Rectangle(width=4, height=10, color="Azure"),
        Circle(radius=2.5, color="Emerald"),
        Rectangle(width=7, height=7, color="Gold")
    ]
    
    print("Executing Polymorphic Geometry Calculations:")
    print("-" * 50)
    
    # We don't care if 'shape' is a Circle or a Rectangle. 
    # Polymorphism guarantees `.area()` behaves dynamically correctly.
    for shape in shapes:
        a = shape.area()
        p = shape.perimeter()
        print(f"{str(shape):<30} | Area: {a:>6.2f} | Perimeter: {p:>6.2f}")
        
    print("-" * 50)

if __name__ == "__main__":
    factory_pattern_demo()
