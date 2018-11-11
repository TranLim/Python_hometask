import math as m

def input_values():
    i = True
    a = True
    while a:
        list = ["+","-","*","/","sin","cos","tg","sqrt","^"]
        print()
        print("List of operations >>>   +    -   *   / sin   cos tg   sqrt  ^ ")
        type_of_operation = input("Choose the operation from the list >>>   ")
        print()
        if any(type_of_operation in s for s in list) and type_of_operation != "":
            a = False
        else:
            print("No operation in the list, choose another")
            print()
            a = True
    while i:
        list1 = ["sin","cos","tg","sqrt","^"]

        try:
            if any(type_of_operation in s for s in list1):
                first_number = float(input("First number  >>>  "))
            else:
                first_number = float(input("First number  >>>  "))
                second_number = float(input("Second number >>>  "))
                print()
            i = False
        except(ValueError) as error:
            print('Error:', error)
            i = True
    res = None
    flag = True
    while flag:
        if type_of_operation == "+":
            res = add(first_number,second_number)
        elif type_of_operation == "-":
            res = sub(first_number,second_number)
        elif type_of_operation == "*":
            res = mul(first_number,second_number)
        elif type_of_operation == "/":
            res = div(first_number,second_number)
        elif type_of_operation == "sin":
            res = sin(first_number)
        elif type_of_operation == "cos":
            res = cos(first_number)
        elif type_of_operation == "tg":
            res = tg(first_number)
        elif type_of_operation == "sqrt":
            res = sqrt(first_number)
        elif type_of_operation == "^":
            res = rise_to_square(first_number)
        else:
            print("We dont have this operation")

        flag = False
    return res


def div (a,b):
    flag1 = True
    while flag1:
        try:
            print("Result >>> ", "{} / {} = {}".format(a, b, a / b))
            flag1 = False
        except (ValueError,ZeroDivisionError) as error:
            flag1 = False
            print("Error", error)
            print("Try another numbers ")
            input_values()
def sqrt(a):
    flag1 = True
    while flag1:
        try:
            print("Result >>> ", "sqrt {}  = {}".format(a, m.sqrt(a)))
            flag1 = False
        except (ValueError, ZeroDivisionError) as error:
            flag1 = False
            print("Error", error)
            print("Try another numbers ")
            input_values()




def  add (a,b):
    return print("Result >>> ", "{} + {} = {}".format(a, b, a + b))
def sub (a,b):
    return print("Result >>> ", "{} - {} = {}".format(a, b, a - b))
def mul (a,b):
    return print("Result >>> ", "{} * {} = {}".format(a, b, a * b))
def sin(a):
    return  print("Result >>> ", "sin {}  = {}".format(a, m.sin(a)))
def cos(a):
    return  print("Result >>> ", "cos {}  = {}".format(a, m.cos(a)))
def tg(a):
    return print("Result >>> ", "tan {}  = {}".format(a, m.tan(a)))
def rise_to_square(a):
    return  print("Result >>> ", "rise to square {}  = {}".format(a, a**2))







def main():
    i = True
    input_values()
    while i:
        print()
        print("Do you want to continue ? да/нет , д/н  , yes/no , y/n ")
        answer = input(" >>> ").replace(' ', '').lower()
        if answer == 'нет' or answer == 'н' or answer == 'no' or answer == 'n':
            print("Have a nice day ")
            i = False
        elif answer == 'да' or answer == 'д' or answer == 'yes' or answer == 'y':
            input_values()
            i = True
        else:
            print()
            print("What the fuck? Try once more ")
            i = True





main()
