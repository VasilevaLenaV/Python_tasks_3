# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def get_list(n):
    return list(random.randint(0, 100) for i in range(1, n + 1))

def sum_odd_position(element):
    sum = 0
    for i in range(1, len(element), 2):
        sum += element[i]
    return sum

list_of_elements = get_list(int(input('Задача 1. Введите число: ')))
print(sum_odd_position(list_of_elements))


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def get_list(n):
    return list(random.randint(0, 100) for i in range(1, n + 1))


def get_pair(arr):
    pairs = []
    len_arr = len(arr) - 1

    for i in range(round(len(arr) / 2)):
        if i == len_arr - i:
            continue
        pairs.append(arr[i] * arr[len_arr - i])

    if (len(arr) / 2) % 2 != 0:
        pairs.append(arr[int((len(arr) / 2) // 1)] ** 2)

    return pairs

N = int(input("Задача 2. Введите длину списка: "))

listN = get_list(N)
print(f"Список: {listN}")
print(f"Произведение пар чисел: {get_pair(listN)}")


# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def get_list(n):
    return list(random.uniform(0, 10) for i in range(1, n + 1))

def get_fraction(llist):
    return list(i % 1 for i in llist)

def get_difference(arr):
    arr_derived = get_fraction(arr)
    max_item = max(arr_derived)
    min_item = min(arr_derived)
    return max_item - min_item

list_of_elements = get_list(int(input('Задача 3. Введите число: ')))

print(list_of_elements)
print(f"{get_difference(list_of_elements):.2f}")


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_bin(num):
    bin = ''
    while num > 0:
        bin = str(num % 2) + bin
        num = num // 2
    return bin

number = int(input('Задача 4. Введите число: '))
print(to_bin(number))

# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonacci(n):
    if n in {1, 2}:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_n(n):
    if n == 0:
        return 0

    div = n < 1 and (n % 2) == 0

    return - fibonacci(abs(n)) if div else fibonacci(abs(n))


def get_fib(n):
    for i in range(-n, n + 1):
        yield fibonacci_n(i)


N = int(input("Задача 5. Введите число: "))
print(list(get_fib(N)))
