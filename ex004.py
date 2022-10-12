# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def coding(txt):
    count_word = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count_word+=1
        else:
            res = res + str(count_word) + txt[i]
            count_word = 1
    if count_word > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count_word) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input('Введите текст для кодировки - ')
print(coding(s))
print(decoding(coding(s)))
