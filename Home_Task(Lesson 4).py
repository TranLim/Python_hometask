#Task 1 (прямокутник)
width  = int(input("ведіть ширину прямокутника  :"))
height  = int(input("ведіть висоту прямокутника :"))

for i in range(height):
    for j in range(width):
        print("* ", end="")
    print()


print("-------------------------------------------")

#Task 2(трикутник прямокутний )
height= int(input("ведіть висоту :"))
for i in range(height):
    print( '*' * (i + 1))


print("-------------------------------------------")




#Task 3 (трикутник рівнобедренний)
height= int(input("ведіть висоту :"))
for i in range(height):
    print( ' ' * (height - i)+ "*" * (i+1) + "*" * i )




print("-------------------------------------------")



#Task 4 (сума натуральних чисел)
i = True
while i:
    num1 = int(input(" Ведіть переше число "))
    num2 = int(input("Введіть друге число "))
    if num1 < num2 and num1 > 0 and num2 > 0:
        suma = sum(range(num1,num2 + 1))
        print(suma)
        i = False


print("-------------------------------------------")




# Task 5 (факторіал)

num = int(input("Введіть число : "))
fact = 1
i = 0
while i < num :
    i += 1
    fact = fact * i

print("Факторіал числа = ", fact)

