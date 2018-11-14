""" Задание №2.
Переделать Задание №1 с созданием и использованием собственное исключение
WhitespaceError с атрибутами:
    position - позиция в строке
    symbol - какой именно непечатный символ
Функция main() демонстрирует работу вашей функции, должна красиво показывать
что именно вызвало исключение.
"""
from string import whitespace

class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol
def string_processing(text):
    for elem in text:
        if elem in whitespace:
            symbol = (repr(elem))
            position = text.index(elem) + 1
            raise   WhitespaceError(position,symbol)
    result = text.lower()
    print(result)
    return result
def main():
    try:
        string_processing("gggw3r\ng")
    except WhitespaceError as e:
        print("Massage ", e.position, e.symbol)

if __name__ == "__main__":
    main()
