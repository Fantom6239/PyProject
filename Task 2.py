natur = []      # Массив натуральных чисел
integers = []   # Массив целых чисел
raz = []        # Массив рациональных чисел
vesh = []       # Массив вещественных чисел
complexs = []   # Массив комплексных чисел
chet = []       # Массив чётных чисел
nechet = []     # Массив нечётных чисел
prost = []      # Массив простых чисел

floats = []     # Массив дробных чисел

# Ввод чисел
number = input()
number = number.replace(',','') # Запятые пришлось удалить, поскольку при использовании метода split они заносились в строку
number = number.split()

#Сначала распределим числа на три основные группы
for i in range(len(number)):
    if number[i] == 'pi' or number[i] == 'e':
        vesh.append(number[i]) # Математические константы относятся к вещественным числам
    elif complex(number[i]).imag == 0 and complex(number[i]).real % 1 == 0:
        integers.append(int(number[i])) # Целые числа не имеют мнимой части и делятся на 1 без остатка
    elif complex(number[i]).imag == 0:
        floats.append(float(number[i])) # Дробные числа не имеют мнимой части
    else:
        complexs.append(complex(number[i])) # Остаются комплексные числа
        
#Распределение целых чисел на группы
for i in range(len(integers)):
    if integers[i] > 0:
        natur.append(integers[i]) # Натуральные числа больше нуля
    if integers[i] % 2 == 0:
        chet.append(integers[i]) # Чётные числа
    else:
        nechet.append(integers[i]) # Нечётные числа
        
# Поиск простых чисел
for i in range(len(natur)):
    for j in range(2, natur[i]):
        if natur[i] > 1 and natur[i] % j == 0:
            break
    else:
          prost.append(natur[i])
    
# К рациональным относятся все целые и дробные числа, кроме бесконечных дробей
raz.extend(integers)
raz.extend(floats)

# К вещественным числам относятся все рациональные, а также бесконечные дроби
# С клавиатуры можно ввести лишь константы, которые были добавлены в массив ранее
vesh.extend(raz)

# Сортировка 
natur.sort()
integers.sort()
raz.sort()
chet.sort()
nechet.sort()
prost.sort()

# Вывод
print("Натуральные числа: ", natur)
print("Целые числа: ", integers)
print("Рациональные числа: ", raz)
print("Вещественные числа: ", vesh)
print("Комплексные числа: ", complexs)
print("Чётные числа: ", chet)
print("Нечётные числа: ", nechet)
print("Простые числа: ", prost)
