import math

class Circle:
    PI = 3.14159265359

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        print(f"Creating a circle with radius {radius} (from diameter {diameter}).")
        return cls(radius)

    @staticmethod
    def get_pi():
        return Circle.PI

circle_a = Circle(radius=10)
print(f"Area of Circle A (Radius 10): {circle_a.area():.2f}")

print("\nUsing Class Method:")
circle_b = Circle.from_diameter(diameter=16)
print(f"Area of Circle B (Diameter 16): {circle_b.area():.2f}")

print(f"\nValue of PI from Static Method: {Circle.get_pi()}")