#!/usr/bin/env python
# -*- coding: utf-8 -*-
# загружаем модуль для работы с регулярными выржениями
import re
# https://pypi.python.org/pypi/colorama
# там есть ESC коды
#import colorama
#colorama.init()
#from colorama import Fore, Back, Style
#t = Terminal()

# загружаем исходный файл
f = open('002-easter.txt', 'r', encoding='utf8')
text = f.read()
f.close()

# переводим все символы в нижний регистр
text = text.lower()

# удаляем слова с апострофами и цифры
text = re.sub('[a-z]+’[a-z]+|[^a-z]\d+|[a-z]+@[a-z]+\.[a-z]+|[a-z]+(\.[a-z]+)+', ' ', text)

# определяем список символов для удаления из файла
symbolsDelete = ['“', '”', ':', ';', '–', '?', '…', '.', ',', '!', '\n', '(', ')']

# цикл удаляет ненужные символы
for i in symbolsDelete:
  text = text.replace(i, ' ')
  
# цикл удаляет двойные пробелы
while text.find('  ') > 0:
    text = text.replace('  ', ' ')
    
# преобразовываем строку в список
text = text.split()

# создаем список уникальных слов
textUnique = []

# выбираем уникальные слова из текста
for i in text:
  k = 0
  for y in textUnique:
    if i == y:
      k += 1
      break
  if k == 0:
    textUnique.append(i)
    #print(textUnique)

# сортируем список
textUnique.sort()
text.clear()
text.extend(textUnique)
#print(text)
#textUnique.clear()

# открываем список известных слов для удаления из файла
f = open('knownWords.txt', 'r', encoding='utf8')
knownWorlds = f.read().split()
f.close()


# цикл удаляет известные слова из списка
# триггер, чтоб указать будем проверять дальше или нет
wordSelect = 1
k = 0
print('Выводятся неизвестные слова, варианты ответов: YES/No/Exit(save)/eXit(no save)')
for i in text:
  k += 1
  #print(i)
  try:
    if knownWords.index(i) >= 0:
      textUnique.remove(i)
  except ValueError:
    if wordSelect:
      cmdInput = input(str(k) + '/' + str(len(textUnique)) + ' ' + '\033[32m' + i + '\033[0m'+ ' ')
      if cmdInput in ['', 'y', 'Y']:
        knownWords.append(i)
        textUnique.remove(i)
        #print('Известное слово: ' + i)
      elif cmdInput in ['e', 'E']:
        print('Выхожу из ручного отбора')
        wordSelect = 0
      elif cmdInput in ['x', 'X']:
        print('Выхожу из отбора без сохранения')
        break

# сохраняем известные слова
if cmdInput not in ['x', 'X']:
  print('Сохраняю известные слова')
  # сортируем, т.к. новые слова добавлялись в конец
  knownWords.sort()
  # записываем в файл
  f = open('knownWords.txt', 'w', encoding='utf8')
  for i in knownWords:
    f.write(i + '\n')
  f.close()

print('Сохраняю неизвестные слова') 
# создаем файл с конечным результатом
f = open('text.txt', 'w')

# записываем результат в файл
for i in textUnique:
  f.write(i + '\n')
f.close()

f.close()
