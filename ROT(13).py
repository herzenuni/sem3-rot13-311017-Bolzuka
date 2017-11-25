# Практичское задание ROT13
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# ROT13
# Разработать программу, реализовывающую алгоритм шифрования ROT13.
# Программа должна уметь:
#       считать текстовую строку из файла и из консоли;
#       закодировать/раскодировать строку и отобразить её на экране;
#       записать закодированную/раскодированную строку в файл;
#
# В программе должен использоваться механизм обработки исключений.


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
assert (ROT131(ROT131(
    'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.')) == 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.')  # The quick brown fox jumps over the lazy dog.
assert (ROT131(ROT131(
    'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?')) == 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?')  # How can you tell an extrovert from an introvert at NSA?


# ________________________________________________________________________________


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
assert (ROT132(ROT132(
    'How can you tell an extrovert from an introvert at NSA?')) == 'How can you tell an extrovert from an introvert at NSA?')
# Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?
assert (
ROT132(ROT132('The quick brown fox jumps over the lazy dog.')) == 'The quick brown fox jumps over the lazy dog.')
# Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
assert (ROT132(ROT132('winter is coming')) == 'winter is coming')  # jvagre vf pbzvat


###########################################################################


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
                    str = (ROT132(s))  # jvagre vf pbzvat
            if x == 4:
                for item in s:
                    str = (ROT131(s))  # winter is coming

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
                        str += (ROT131(item))  # winter is coming
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
                         str += (ROT132(item))  # jvagre vf pbzvat
                finally:
                    file.close()
                    result.write(str)
                    result.close()


        print("Finish!")
        print('Answer:', str)


ROT13()
