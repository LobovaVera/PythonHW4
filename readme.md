A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
Расширить значение коэффициентов до [-100..100]

# import random

# coef1 = random.randrange(0, 101)
# coef2 = random.randrange(0, 101)
# coef3 = random.randrange(0, 101)



# if coef1 ==0 and coef2 == 0 and coef3 == 0:
#     print("Все коэффициенты равны нулю, что-то пошло не так")
#     exit()
# if coef1 ==0 and coef2 == 0 and coef3 != 0:
#     print("Цифра равна нулю, что-то пошло не так")
#     exit()


# def bisq_equasion(a, b, c):
#         eq_parts = []
#         if a != 0:
#             eq_parts.append(str(a) + "*x**2")
#         if b != 0:
#             eq_parts.append(" + " + str(b) + "*x")
#         if c != 0:
#             eq_parts.append(" + " + str(c))
#         return eq_parts

# equasion = bisq_equasion(coef1, coef2, coef3)

# eq_string = ""
# for el in equasion:
#     eq_string += el

# if eq_string.startswith(" + "):
#     eq_string = eq_string[3:]

# print(eq_string + " = 0")

# if coef1 != 0 and coef2 == 0 and coef3 == 0:
#     print("В таком случае х = 0")

# if coef1 == 0 and coef2 != 0 and coef3 == 0:
#     print("В таком случае х = 0")
