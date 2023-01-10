# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# !!! k > 0
encoding='utf-8'


k = int(input("Введите показатель степени: "))
print(k)

def get_equasion(k):

    import random

    coeff = random.randint(0, 101)
    # power_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'] # это у меня пока не получилось

    equasion = ""

    for poww in range(1, k+1):
        coef = random.randint(0, 101)
        if coef != 0:
            
            if coef == 1:
                if poww == 1:
                    equasion = str(coef) + "*x" + equasion
                else:
                    equasion = "x**" + str(poww) + equasion
                # if  poww != k+1:
                equasion = " + "  + equasion
            else:
                if poww == 1:
                    equasion = str(coef) + "*x" + equasion
                    
                elif coef != 0:
                    equasion = str(coef) + "x**" + str(poww) + equasion
                    # if  poww != k+1:
                equasion = " + "  + equasion
            

    if equasion.startswith(' +'):
        equasion = equasion[3:]
      


    if coeff == 0:
        equasion += " = 0"
    else:
        equasion += " + " + str(coeff) + " = 0"
        
    print(equasion)
   
    return equasion


eq_string1 = get_equasion(k)
eq_string2 = get_equasion(k)
data = open( 'file.txt', 'w')
data.writelines(eq_string1)

data = open( 'file2.txt', 'w')
data.writelines(eq_string2)