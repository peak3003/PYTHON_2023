# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов или символов конца строки.
# Определите, сколько различных слов содержится в этом тексте. split

# some_srt = input().split()
# print(len(set(some_srt)))

some_str = input()
some_set = set()
temp_word = ''
for letter in some_str:
    if letter != ' ':
        temp_word += letter
    else:
        if temp_word:
            some_set.add(temp_word)
        temp_word = ''
some_set.add(temp_word)
print(some_set)
