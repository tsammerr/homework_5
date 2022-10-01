number_1 = int(input('1 number -> '))
number_2 = int(input('2 number -> '))

while number_1 <= number_2:
    print(f"number = {number_1}")
    number_2 += 1

if number_1 % 7 != 0:
    if number_1 < 7:
        number_1 += (7 % number_1);
else:
    number_1 += (number_1 % 7);
while number_1 <= number_2:
        print(f'{number_1}', end=" ")
        number_1 += 7