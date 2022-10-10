# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line = input('Введите строку - ')
 
words = line.split(' ')
 
new_words = []
for word in words:
     if 'а' not in word:
        if 'б' not in word:
            if 'в' not in word:
                new_words.append(word)
print(' '.join(new_words))