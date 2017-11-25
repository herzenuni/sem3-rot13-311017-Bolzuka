# Практичское задание ROT13
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
#
# ЧАСТЬ 1
#
# Для задания по созданию шифровальщика на основе ROT13 создайте отдельный модуль, в котором бы тестировался функционал шифровальщика.
#
# Требования к модулю:
# Наличие docstring для модуля, в котором бы кратко описывалась его назначение
# Тестирование проводится с помощью assert, находящихся внутри функции.
# Тестирование должно быть параметризовано, т.е. вы пишете например, одну функцию например, test_rot13(inp, out), а из основного файла, где находится код ROT13 вызываете её с разными параметрами.
# Подумайте какие тесты требуется сделать для того, чтобы проверить максимально функциональность работы ROT13.

def ROT131(string):
    """
    Функция шифрования строки по алгоритму rot13
    return возвращает искомую строку
    """

    def rot(alfabit):
        i = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(alfabit)
        if i != -1:
            return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[i]
        else:
            return alfabit

    return "".join(map(rot, string))


# ________________________________________________________________________________
# ПРОВЕРКА
assert (ROT131(ROT131('jvagre vf pbzvat')) == 'jvagre vf pbzvat')  # winter is coming
assert (ROT131(ROT131('Gur dhvpx oebja sbk whzcf bire gur ynml qbt.')) == 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.')  # The quick brown fox jumps over the lazy dog.
assert (ROT131(ROT131( 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?')) == 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?')  # How can you tell an extrovert from an introvert at NSA?

