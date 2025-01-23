import math
a = int(input("Enter coeffcient of x^2: "))
b = int(input("Enter coeffcient of x: "))
c = int(input("Enter constant: "))
ans = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
ans2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
print(ans, ans2)