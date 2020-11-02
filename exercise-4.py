# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = input("Enter the length of side a in the triangle: ")
b = input("Enter the length of side b in the triangle: ")
c = input("Enter the length of side c in the triangle: ")
triangle = ''

if a == b and b == c:
    triangle = 'equalateral'
    print(f"A triangle with sides of {a}, {b} & {c} is a {triangle} triangle")
elif a != b and b != c:
    triangle = 'scalene'
    print(f"A triangle with sides of {a}, {b} & {c} is a {triangle} triangle")
else:
    triangle = 'isosceles'
    print(f"A triangle with sides of {a}, {b} & {c} is a {triangle} triangle")

