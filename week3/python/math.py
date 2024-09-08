import math
a=int(input("请输入a的值"))
b=int(input("请输入b的值"))
c=int(input("请输入c的值"))
print((-b+math.sqrt(b**2-4*a*c))/(2*a))
print((-b-math.sqrt(b**2-4*a*c))/(2*a))