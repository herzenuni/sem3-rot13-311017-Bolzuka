# Практичское задание ROT13
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
#
# ЧАСТЬ 2
#
# Для задания по созданию шифровальщика на основе ROT13 создайте отдельный модуль, в котором бы тестировался функционал шифровальщика.
#
# Требования к модулю:
# Наличие docstring для модуля, в котором бы кратко описывалась его назначение
# Тестирование проводится с помощью assert, находящихся внутри функции.
# Тестирование должно быть параметризовано, т.е. вы пишете например, одну функцию например, test_rot13(inp, out), а из основного файла, где находится код ROT13 вызываете её с разными параметрами.
# Подумайте какие тесты требуется сделать для того, чтобы проверить максимально функциональность работы ROT13.

def ROT132(string):
    """
    Функция шифрования строки по алгоритму rot13.
    return возвращает искомую строку
    """

    def rot(alfabit):
        i = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'.find(alfabit)
        if i != -1:
            return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[i]
        else:
            return alfabit

    return "".join(map(rot, string))


# ________________________________________________________________________________
# ПРОВЕРКА
assert (ROT132(ROT132('How can you tell an extrovert from an introvert at NSA?')) == 'How can you tell an extrovert from an introvert at NSA?') # Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?
assert (ROT132(ROT132('The quick brown fox jumps over the lazy dog.')) == 'The quick brown fox jumps over the lazy dog.') # Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
assert (ROT132(ROT132('winter is coming')) == 'winter is coming')  # jvagre vf pbzvat