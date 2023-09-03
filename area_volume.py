import math

width = int(input("Enter the width: "))
length = int(input("Enter the length: "))
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

area = length * width
volume = math.pi*pow(radius,2)*height

print(f"The area of the rectangle is: {area}")
print(f"The volume of the cylinder is: {volume:.2f}")