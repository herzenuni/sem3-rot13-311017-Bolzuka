# Практичское задание ROT13
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
#
# TEST!!!
#
# Для задания по созданию шифровальщика на основе ROT13 создайте отдельный модуль, в котором бы тестировался функционал шифровальщика.
#
# Требования к модулю:
# Наличие docstring для модуля, в котором бы кратко описывалась его назначение
# Тестирование проводится с помощью assert, находящихся внутри функции.
# Тестирование должно быть параметризовано, т.е. вы пишете например, одну функцию например, test_rot13(inp, out), а из основного файла, где находится код ROT13 вызываете её с разными параметрами.
# Подумайте какие тесты требуется сделать для того, чтобы проверить максимально функциональность работы ROT13.

import ROT13 as str

def test_ROT13(s):
    """
    Функция проверяет функцию шифрования Rot13
    """
    assert (str.ROT13(str.ROT13(s)) == s)
    return str.ROT13(str.ROT13(s)) == s
