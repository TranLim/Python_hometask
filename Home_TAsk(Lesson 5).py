

#Task 1 (вивод імені)
def hi(name):

    if  name:
        print("Hello", name)
    elif not name:
        print("Hello, Vlad")




hi("Vasia")
hi("")
hi("Alex")





print("-------------------------------------------")




#Task 3(калькулятор)
def  add (a , b):
    return a + b
def sub (a , b):
    return a - b
def div (a, b ):
    if b == 0:
        return "ділення на ноль"
    else:
        return a / b
def mul (a , b):
    return a * b

i = True

a = float(input("Введіть чило 1 ---  "))
b = float(input("Введіть чило 2 ---  "))
while i :
    znak = input("Введіть знак ")
    if znak == "+" or znak == "-" or znak == "*" or znak == "/" :
        break
if znak == "+":
    print(add(a , b))

elif znak == "-":
    print(sub(a , b))

elif znak == "*":
    print(mul(a , b))

elif znak == "/":
    print(div(a,b))




print("-------------------------------------------")




#Task (Додаткове завдання)
def midlenum(num1,num2,num3):
    return (num1+num2+num3)/3
i =True
while i:
    num1 = float(input("Введіть число 1 "))
    num2 = float(input("Введіть число 2 "))
    num3 = float(input("Введіть число 3 "))
    print("Середнє значення --- ",midlenum(num1,num2,num3))
    break







print("-------------------------------------------")




#Task 2 (функція)


def function(x):
    if x > 0:
        return 3 * x + 5
    elif x <= 0 :
        return 4 + 5 * x


def main():
    for i in range(-10, 11):
        i = i / 2
        y = function(i)
        print('Функція від (', i, ') =  ', y, sep='  ')


main()





