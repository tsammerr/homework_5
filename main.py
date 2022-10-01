number_1 = int(input('1 number -> '))
number_2 = int(input('2 number -> '))

while number_1 <= number_2:
    print(f'{number_1} - ', end = "")
    if number_1 % 3 == 0 and number_1 % 5 != 0:
        print('Fizz')
    elif number_1 % 5 == 0 and number_1 % 3 != 0:
        print('Buzz')
    elif number_1 % 3 == 0 and number_1 % 5 == 0:
        print('Fizz Buzz')
    else:
        print(f'{number_1}')
    number_1+=1