# Практичское задание ROT13
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
#
# ЧАСТЬ 3
#
# Для задания по созданию шифровальщика на основе ROT13 создайте отдельный модуль, в котором бы тестировался функционал шифровальщика.
#
# Требования к модулю:
# Наличие docstring для модуля, в котором бы кратко описывалась его назначение
# Тестирование проводится с помощью assert, находящихся внутри функции.
# Тестирование должно быть параметризовано, т.е. вы пишете например, одну функцию например, test_rot13(inp, out), а из основного файла, где находится код ROT13 вызываете её с разными параметрами.
# Подумайте какие тесты требуется сделать для того, чтобы проверить максимально функциональность работы ROT13.

def ROT13():
    """
    Функция считывает строку из консоли или из файла
    Сопоставляет каждый элемент со значением/ключом из словаря для кодирования
    Выводит результат в консоль или отдельный файл для результата
    """
    try:
        print('What do you want to do? \n1. From console \n2. From document?  \n')
        y = float(input('Enter operation number: '))
    except ValueError:
        print('!Enter the number!')
    try:
        print('What do you want to do? \n3. ROT13 -> EN \n4. EN -> ROT13 \n')
        x = float(input('Enter operation number: '))
    except ValueError:
        print('!Enter the number!')
    else:
        if y == 1:
            s = input('Enter the string: ')
            if x == 3:
                for item in s:
                    str = (import __init__ as s)  # jvagre vf pbzvat
            if x == 4:
                for item in s:
                    str = (import __init__2 as s)  # winter is coming

        ###########################################################################

        elif y == 2:
            if x == 3:
                str = ''
                try:
                    file = open("string R-E.txt")
                except OSError:
                    print('OSError!')
                try:
                    cont = file.read()
                    result = open("Result.txt", "w")
                    for item in cont:
                        str += (import __init__ as item)  # winter is coming
                finally:
                    file.close()
                    result.write(str)
                    result.close()

            if x == 4:
                str = ''
                try:
                    file = open("string E-R.txt")
                except OSError:
                    print('OSError!')
                try:
                    cont = file.read()
                    result = open("Result.txt", "w")
                    for item in cont:
                         str += (import __init__2 as item)  # jvagre vf pbzvat
                finally:
                    file.close()
                    result.write(str)
                    result.close()


        print("Finish!")
        print('Answer:', str)


ROT13()