# programme to get the area of the rectangle
length = input("Enter the length:")
width = input("Enter the width")
area = int(length) * int(width)
print(area)
# programme to get the area of the triangle
height = input("Enter the height of the triangle:")
base = input("Enter the base of the triangle:")
areaT = (int(height) * int(base)) / 2
print(areaT)
# programme to get the area of the square
side = input("Enter the side of the square:")
areaS = int(side) * int(side)
print(areaS)

# programme to get the area of the circle and the circumference
radius = input("Enter the radius of the circle:")
pi = 3.142
areaC = pi * float(radius) * float(radius)
circumference = 2 * pi * float(radius)
print(areaC)
print(circumference)
