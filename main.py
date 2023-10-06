import math

print("this is solving maths quadratic equation")

# a * x * x + b * x + c = 0
# define factors of equation
a = 2
b = 4
c = -4
# fine discriminant

D = b * b - 4 * a * c
print(f"Discrinant = {D}")

if D > 0:

    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print(f"there are two roots:{x1} , {x2}")

if D < 0:
    print("there are no roots...")

if D == 0:

    x = -b / 2 * a
    print(f"there is only one roots:{x}")



