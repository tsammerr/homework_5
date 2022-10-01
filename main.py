number_1 = int(input('1 number -> '))
number_2 = int(input('2 number -> '))

def ex_1():
     while number_1 <= number_2:
       print(f'number = {number_1}')
       number_1 += 1

def ex_2():
    while number_2 >= number_1:
       print(f'number = {number_2}')
       number_2 -= 1

def ex_3():
 if number_1 % 7 != 0:
    if number_1 < 7:
        number_1 += (7 % number_1);
    else:
        number_1 += (number_1 % 7);

while number_1 <= number_2:
    print(f'number = {number_1}')
    number_1 += 7

def ex_4():

 if number_1 % 5 != 0:
    if number_1 < 5:
        number_1 += (5 % number_1);
    else:
        number_1 += (number_1 % 5);

while number_1 <= number_2:
    print(f'number = {number_1}')
    number_1 += 5

ex_1()
ex_2()
ex_3()
ex_4()