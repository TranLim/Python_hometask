#Task 1( формула Герона)
import math
square = 0
side1 = float(input("Введіть першу сторону "))
side2 = float(input("Введіть другу сторону "))
side3 = float(input("Введіть третю сторону "))
if side1 < 0 or side1 < 0 or side1 < 0 :
    print("Від`ємна сторона ")
else:
    perymetr = (side1 + side2 + side3) / 2
    square = math.sqrt(perymetr*(perymetr - side3)*(perymetr - side2)*(perymetr - side1))
    print(round(square, 3 ))


print("---------------------------------------------------")

#Task 2 (змінити місцями змінні)
a = 2
b = 3
a,b = b,a
print(a)
print(b)

print("---------------------------------------------------")

#Task 3  (змінити місцями змінні)
a = 15
b = 10
a = a + b
b = a - b
a = a - b
print(a)
print(b)

print("---------------------------------------------------")

#Task 4 (парне . не парне)
num1 = float(input("Введіть  число  "))
if num1 % 2  == 0 :
    print(num1 ** 2)
else:
    print(num1 * 2)