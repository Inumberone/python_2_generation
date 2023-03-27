
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

num = int(input("Введи число которое нужно возвести в степень: "))
exp = int(input("Введи степень: "))

def exponentiation(a,b):
    if b == 1:
        return a
    if b ==0:
        return False
    return a**b

print(f'{num} в степени {exp} = {(exponentiation(num,exp))}')


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

print(f'{num1} + {num2} = {sum(num1, num2)}')


