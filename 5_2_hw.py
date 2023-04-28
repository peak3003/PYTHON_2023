# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:\
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений

def rle_cod(txt):
   if txt.isalpha() == False:
       return "Невалидная строка"
   else:
        count = 1
        res = ''
        for i in range(len(txt) - 1):
            if txt[i] == txt[i + 1]:
                count += 1
            else:
                res = res + txt[i]
                if count > 1:
                    res = res + str(count)
                    count = 1
        if count > 1 or (txt[len(txt) - 2] != txt[-1]):
            res = res + txt[-1]
            if count > 1:
                res = res + str(count)
        return res


s = input("Введите строку: ")
print(f"Строка после RLE-кодирования: {rle_cod(s)}")

