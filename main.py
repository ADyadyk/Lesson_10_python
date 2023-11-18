import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst) # Функция перемешивает элементы изменяемой последовательности
data = pd.DataFrame({'whoAmI':lst})
print(data.head(20))



# Перевод в one hot кодировку, используя метод pandas get_dummies:
print(pd.get_dummies(data))



# -----------------------------------------------------------------

# Перевод в one hot кодировку, не используя метод get_dummies:

# Создадим списки, в которые будем записывать 0 или 1 в зависимости от того какое значение в data
human = []
robot = []
# Переберём data и заполним наши списки:
for i in range(len(lst)):
    if data.values[i] == 'human': # Извлекаем из data очередное значение с помощью метода values
        human.append(1)
        robot.append(0)
    else:
        human.append(0)
        robot.append(1)
# Создадим словарь:
dic_data = {'humun' : human, 'robot' : robot}
# Создадим Data Frame из нашего словаря:
oneHot = pd.DataFrame(dic_data)
# Выведем получившеюся кодировку one hot, которую получили не использовав метод get_dummies:
print(oneHot)