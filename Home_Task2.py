# #Task 1 (порівняння імені)
print("Task1 ------------------------------------------")
name = input("Введіть совє ім'я ")
my_name = "Владислав"
if name == my_name :
    print("Співпадає ")
else:
    print("Не співпадає ")
print()

#Task 2 (обчислення функції)
print("Task2 ------------------------------------------")
import math
x = float(input("Введіть значення х -- "))
PI = math.pi
if -PI <= x <= PI :
    print(math.cos(3*x))
elif x < -PI or x > PI :
    print (x)
print()
#Task 3 (дискриміннат)
print("Task3 ------------------------------------------")
import math
name_a = float(input(" Введіть першу змінну   "))
name_b = float(input(" Введіть другу змінну    "))
name_c = float(input(" Введіть третю змінну    "))
discr = name_b ** 2 - 4 * name_a * name_c
if discr < 0 :
    print("Дискримінант менше нуля ")
elif discr == 0 :
   x =(-name_b / 2 * name_a)
   print(x)
elif discr > 0:
    x1 = (-name_b + math.sqrt(discr)) / 2 * name_a
    x2 = (-name_b - math.sqrt(discr)) / 2 * name_a
    print( "x1 = " , round(x1, 3) )
    print("x2 = ", round(x2, 3))
print()
#Task 4 (два числа )
print("Task4 ------------------------------------------")
num1 = float(input("Введіть перше число = "))
num2 = float(input("Введіть друге число = "))
result = 0
if num1 > num2 :
    result = num1 - num2
    print(result)
elif num1 < num2 :
    result = num1 + num2
    print(result)
elif num1 == num2 :
    print(num1)
print()
#Task 5 (запрос даних)
print("Task5 ------------------------------------------")
name = input("Как вас зовут?(ввести без пробілу) ")
age = input("Сколько вам лет?(ввести без пробілу) ")
city = input("Как называется город, в котором вы живете?(ввести без пробілу)")
if name.isalpha() :
    print("Ваше  ім'я  =", name.capitalize())
else:
    print("В імені цифра або ви ввели з пробілом або пустота ")
if age.isdigit() :
    print("Ваш вік  =", age)
else:
    print("У віці буква або ви ввели з пробілом або пустота  ")
if city.isalpha() :
    print("Ваше місто =", city.capitalize())
else:
    print("В місті цифра або ви ввели з пробілом або пустота ")
print()
#Task 6 (0-5)
print("Task6 ------------------------------------------")
number = int(input("Введіть число від 0 до 5  "))
text = "Немає результата "
if number == 0 :
    print(0)
elif number == 1 :
    print(1)
elif number == 2 :
    print(2)
elif number == 3 :
    print(3)
elif number == 4 :
    print(4)
elif number == 5 :
    print(5)
else:
    print("Ошибка ", text )
print()
#Task 7 (високосний рік)
print("Task7 ------------------------------------------")
year = int(input("Введіть рік "))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) :
    print("Звичайний ")
else:
    print(" Високосний  ")
print()








