def ex_1(number_1, number_2):

     print('Ex 1 = ',end=" ")
     while number_1 <= number_2:
       print(f'{number_1}', end=" ")
       number_1 += 1

def ex_2(number_1, number_2):
    print('Ex 2 = ',end=" ")
    while number_2 >= number_1:
       print(f'{number_2}', end=" ")
       number_2 -= 1

def ex_3(number_1, number_2):
    print('Ex 3 = ',end=" ")
    if number_1 % 7 != 0:
        if number_1 < 7:
            number_1 += (7 % number_1);
        else:
            number_1 += (number_1 % 7);
    while number_1 <= number_2:
        print(f'{number_1}', end=" ")
        number_1 += 7

def ex_4(number_1, number_2):
    print('Ex 4 = ',end=" ")
    if number_1 % 5 != 0:
        if number_1 < 5:
            number_1 += (5 % number_1);
    else:
        number_1 += (number_1 % 5);

    while number_1 <= number_2:
        print(f'{number_1}', end=" ")
        number_1 += 5

if __name__ == "__main__":
    number_1 = int(input('1 number -> '))
    number_2 = int(input('2 number -> '))
    ex_1(number_1, number_2)
    print()
    ex_2(number_1, number_2)
    print()
    ex_3(number_1, number_2)
    print()
    ex_4(number_1, number_2)
    print()
