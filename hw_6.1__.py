""" Задание №1.
функция что-то делает со строкой и для непечатных символов (string.whitespace)
вызывает исключение ValueError
"""
from string import whitespace

def string_processing(text):
    for elem in text:
        if elem in whitespace:
            raise ValueError("Warning ")
    result = text.lower()
    print(result)
    return result
if __name__ == "__main__":
    try:
        string_processing("somes tring")
    except ValueError as e:
        print("ERROR - ",e)



